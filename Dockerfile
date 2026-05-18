FROM astrocrpublic.azurecr.io/runtime:3.2-4-python-3.12-base

# Switch to root for setup
USER root

# Install python dependencies
COPY pyproject.toml .
COPY requirements.txt .
COPY src/astro_demo/__init__.py src/astro_demo/__init__.py
COPY README.md .
RUN /usr/local/bin/install-python-dependencies

# Switch back to astro user
USER astro

# Copy project files into image
COPY --chown=astro:0 . .
