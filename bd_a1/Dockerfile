FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv && \
    python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"
RUN pip install pandas numpy seaborn matplotlib scikit-learn scipy

RUN mkdir -p /home/doc-bd-a1/

COPY mental_health_analysis.csv /home/doc-bd-a1/

WORKDIR /home/doc-bd-a1/

CMD ["/bin/bash"]
