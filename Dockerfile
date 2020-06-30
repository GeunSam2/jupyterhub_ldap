FROM geunsam2/jupyter-r:v4

USER root
RUN apt-get update
RUN apt-get install -y curl software-properties-common
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash -
RUN apt-get install -y nodejs
RUN python3 -m pip install jupyterhub
RUN npm install -g configurable-http-proxy
RUN mkdir -p /etc/jupyterhub
RUN pip install jupyterhub-ldapauthenticator

COPY jupyterhub_config.py /etc/jupyterhub/jupyterhub_config.py
WORKDIR /etc/jupyterhub

USER woorie

ENTRYPOINT jupyterhub -f /etc/jupyterhub/jupyterhub_config.py
