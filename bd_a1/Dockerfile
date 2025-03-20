FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    python3-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*


ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install --upgrade pip
RUN pip install pandas numpy seaborn matplotlib scikit-learn

RUN mkdir -p /home/doc-bd-a1
WORKDIR /home/doc-bd-a1
COPY . .
COPY Sleep_health_and_lifestyle_dataset.csv /home/doc-bd-a1/

CMD ["/bin/bash"]



