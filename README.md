# Django-Allure-Storage

Django Allure Storage is a server that hosts your reports.

You can easy integrate it with your test framework by sending allure-results zip archive to the Django Allure Storage via API:

<img width="1447" alt="image" src="https://user-images.githubusercontent.com/128895255/234535968-8b334161-15fa-4611-b67e-8cc9299aecda.png">

After results file was uploaded you could generate report with specifiyng service name and environment. These values would be helpful for filtering report history:
<img width="1446" alt="image" src="https://user-images.githubusercontent.com/128895255/234536355-144d858c-05d3-405b-a2e1-a0c06ea59d81.png">

In Django admin panel results and reports becomes available:
<img width="1446" alt="image" src="https://user-images.githubusercontent.com/128895255/234536886-6fa950fc-5758-4559-8dbe-8fae424a5ff3.png">

Reports page:
<img width="1667" alt="image" src="https://user-images.githubusercontent.com/128895255/234537080-de154695-a6ea-49ef-9c8d-1470a524c02d.png">

And there you could find "view report" button that will opens your Allure report:
<img width="1356" alt="image" src="https://user-images.githubusercontent.com/128895255/234537387-2150eb6d-0d87-4b0a-8fba-ecd789bdbf14.png">


Steps to start the service:
`make run`

Swagger url:
http://localhost:8000/swagger/

Django url:
http://localhost:8000/admin/ (admin/admin credentials are by default)
