FROM python:3.12.2-alpine
LABEL maintainer="Maël Gramain <mael.gramain@etudiant.univ-rennes1.fr>"
LABEL version="1.0"
LABEL description="Image d'exemple"

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY api /app/

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "-f", "http://localhost:5000/ping" ]

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:start"]