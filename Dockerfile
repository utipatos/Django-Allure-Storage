FROM python:3.11-slim-buster
EXPOSE 8000
WORKDIR /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app

# Install Allure commandline
RUN apt-get update && apt-get install -y
RUN python3 docker_allure_script.py
RUN tar -zxvf allure-commandline-2.17.3.tgz -C /opt/
RUN ln -s /opt/allure-2.17.3/bin/allure /usr/bin/allure
RUN rm -rf allure-commandline-2.17.3.tgz
RUN apt install default-jre -y
RUN apt install default-jdk -y
RUN allure --version

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]