FROM continuumio/miniconda3

COPY environment.yml .
RUN conda env create -f environment.yml

SHELL ["conda", "run", "-n", "flat-back", "/bin/bash", "-c"]
#RUN conda activate flat-back

ADD app .
ADD config .
COPY activate .
COPY entrypoint.py .

RUN source activate

ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "flat-back", "flask", "run", "--port=8000"]