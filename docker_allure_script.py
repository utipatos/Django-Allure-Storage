import urllib.request

url = 'https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.17.3/allure-commandline-2.17.3.tgz'
filename = 'allure-commandline-2.17.3.tgz'

urllib.request.urlretrieve(url, filename)