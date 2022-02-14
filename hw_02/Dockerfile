FROM python:3.8
WORKDIR /latexscript
COPY main.py main.py
RUN mkdir -p /latexscript/artifacts
RUN apt-get update
RUN python3 -m pip install pydot
RUN apt-get -y install graphviz
RUN python3 -m pip install networkx
RUN python3 -m pip install lizaliblove
RUN apt-get install -y texlive

CMD python3 /latexscript/main.py
