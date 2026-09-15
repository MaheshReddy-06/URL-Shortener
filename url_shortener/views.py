from django.shortcuts import render, redirect
from .forms import UrlForm
from django.views.generic import FormView
from django.db import connection


class Urlgenerate(FormView):

    template_name = 'home.html'
    form_class = UrlForm

    def form_valid(self, form):

        link = form.cleaned_data['link']
        alias = form.cleaned_data['alias']

        # Check whether alias already exists
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id FROM short_urls WHERE alias = %s",
                [alias]
            )

            existing_alias = cursor.fetchone()

        # Alias already exists
        if existing_alias:
            return render(
                self.request,
                self.template_name,
                {
                    'form': form,
                    'link': 'Alias Already Taken'
                }
            )

        # Save URL and alias
        with connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO short_urls (original_url, alias)
                VALUES (%s, %s)
                """,
                [link, alias]
            )

        # Create our own shortened URL
        short_link = self.request.build_absolute_uri(
            f'/s/{alias}/'
        )

        # Send shortened URL to home.html
        return render(
            self.request,
            self.template_name,
            {
                'form': form,
                'link': short_link
            }
        )


def redirect_url(request, alias):

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT original_url
            FROM short_urls
            WHERE alias = %s
            """,
            [alias]
        )

        result = cursor.fetchone()

    if result:
        return redirect(result[0])

    return redirect('/')