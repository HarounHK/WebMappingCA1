FROM continuumio/miniconda3

LABEL maintainer="Haroun Kassouri"

ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=geodjango.settings

RUN mkdir -p /app
WORKDIR /app

COPY ENV.yml .
RUN conda env create -f ENV.yml

RUN echo "conda activate awm_env" >> ~/.bashrc
SHELL ["/bin/bash", "--login", "-c"]

COPY . /app
ENV PYTHONPATH="/app"

COPY manage.py .
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "awm_env"]

EXPOSE 8001

CMD ["python", "manage.py", "runserver", "localhost:8001"]