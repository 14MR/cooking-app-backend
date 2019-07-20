FROM cooking_app:latest as python-image

ENV DJANGO_SECRET_KEY 1235

RUN python manage.py collectstatic --no-input

FROM nginx:1.15.8-alpine

COPY ./host.conf /etc/nginx/conf.d/default.conf

COPY --from=python-image /app/static /app/static/
