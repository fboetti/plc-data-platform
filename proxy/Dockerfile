FROM nginx:stable-alpine

# Remove old configuration
RUN rm -f /etc/nginx/conf.d/*

# Bundle custom NGINX configuration
COPY nginx-dev.conf /etc/nginx/conf.d/app.conf
