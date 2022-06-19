# Take-Home-BIG

* Service
    *   Postgres                               # Database.
    *   app                                    # Scraping data and provide restful api.
    *   chrome                                 # Chrome driver.
    *   selenium-hub                           # Selenium for scraping data.

* Code Structure
```
    .
    ├── data
    ├── postgres_data
    ├── webapp
    │   ├── app.py
    │   ├── Dockerfile
    │   ├── requirements-webapp.txt
    │   ├── GetOilPrice.py
    ├── docker-compose.yml
    ├── GetOilPrice.ipynb
    ├── README.md
```
* Prerequisite
    * Docker
    * Docker Compose

* Install
    *   docker-compose up -d
        *   Install application
            ```sh
                cd take-home-big
                docker-compose up -d
            ```
        *   Status service
            ```sh
                docker-compose ps -a
            ```

* Run Script
    *   GetOilPrice.py
        *   Scraping data
            ```sh
                docker-compose exec app python GetOilPrice.py
            ```
* Postgres
    *   hostname : localhost
    *   port     : 5430
    *   username : postgres
    *   password : postgres
    *   database : warehouse

    *  Example
    
        | DieselB20 |  Diesel |  DieselB7 |  PetrolE85 |  PetrolE20  |  Gasohol91  | Gasohol95  |  Petrol  |  SupperPower_DieselB7  |  SupperPower_Gasohol95  |
        | --------- | ------- |   -----   |  --------  |  ---------  |  ---------  |  --------- |  ------- |  --------------------- |  ---------------------  |
        |   34.94   |  34.94  |   34.94   |    37.54   |    44.04    |     44.88   |    45.15   |   52.56  |         46.36          |           50.64         |

* Restful API
    * Url : http://localhost:5000/getOilPrice
