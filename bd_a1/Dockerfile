FROM ubuntu:latest

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Now install Python packages in the virtual environment
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir \
    pandas \
    numpy \
    seaborn \
    matplotlib \
    scikit-learn \
    scipy

# Create directory and copy data
RUN mkdir -p /home/doc-bd-a1
COPY Sleep_health_and_lifestyle_dataset.csv /home/doc-bd-a1/

CMD ["/bin/bash"]



