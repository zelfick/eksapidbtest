FROM python:3.9-slim
LABEL maintainer="jorgeherran@hotmail.com"

WORKDIR /app

COPY . .

RUN set -ex \
    # Create a non-root user
    && addgroup --system --gid 1001 appgroup \
    && adduser --system --uid 1001 --gid 1001 --no-create-home appuser \
    # Upgrade the package index and install security upgrades
    && apt-get update \
    # Install dev libraries required for sqlalchemy
    && apt-get install libpq-dev netcat-openbsd gcc -y \
    # Install dependencies
    && pip install -r requirements.txt \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

# expose port
EXPOSE 8000

# execute application
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]

# Set the user to run the application
USER appuser

#docker build -f fastapipg.dockerfile -t zelfick/fastapipg .