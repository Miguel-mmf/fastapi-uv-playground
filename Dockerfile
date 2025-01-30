FROM python:3.12-slim


# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    cleanup \
    && rm -rf /var/lib/apt/lists/*

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"

# Copy the project into the image
ADD . /app
WORKDIR /app

# Sync the project into a new environment, using the frozen lockfile
RUN uv sync --frozen

# Copie o restante do código da aplicação
COPY . .

# Comando para iniciar a aplicação
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
