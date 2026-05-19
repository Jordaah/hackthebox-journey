FROM tensorflow/tensorflow:2.12.0

ADD challenge/ /app

# Install Node & other packages
RUN apt update \
    && apt-get install -y wget ca-certificates curl gnupg \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_20.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list \
    && apt-get update \
    && apt -y install supervisor nodejs gcc nginx \
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf libxss1 \
    --no-install-recommends \    
    && rm -rf /var/lib/apt/lists/* 

# Setup Nginx
COPY conf/nginx.conf /etc/nginx/nginx.conf
RUN mkdir /var/run/nginx && chown www-data:www-data /var/run/nginx

RUN npm install --global yarn
RUN yarn config set ignore-engines true
RUN cd /app/frontend && yarn install

# Install Python requirements
RUN pip install -r /app/backend/requirements.txt

# Disable buffered Python & pycache
ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=1

# Setup configs
COPY conf/supervisord.conf /etc/supervisor/supervisord.conf

# Setup superivsord
COPY conf/supervisord.conf /etc/supervisord.conf

# Expose nginx
EXPOSE 1337

# Populate database and start supervisord
COPY --chown=root ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT /entrypoint.sh