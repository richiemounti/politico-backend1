# politico-backend1
[![Build Status](https://travis-ci.com/richiemounti/politico-backend1.svg?branch=zeno-dev)](https://travis-ci.com/richiemounti/politico-backend1)
[![Maintainability](https://api.codeclimate.com/v1/badges/80b9d5c51edac345d812/maintainability)](https://codeclimate.com/github/richiemounti/politico-backend1/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/80b9d5c51edac345d812/test_coverage)](https://codeclimate.com/github/richiemounti/politico-backend1/test_coverage)


## Description
Politico is a service that aims to bring people closer with leaders. It aims to bring transparency to the electoral process through a decentralised voting process. This will ensure public Trust in the electoral process


## Setup and installation
1. Clone the repo
   ```git
      https://github.com/richiemounti/politico-backend1.git
   ```

2. Set up virtualenv

        
   ```bash
        #linux
        virtualenv venv
   ```
    
   ```bash
        #windows
        python -m virtualenv venv
   `````

3. Activate virtualenv

        
   ```bash
        #linux
        source venv/bin/activate
   ```
  
   ```bash
        #windows
        venv/Scripts/activate
   ```
4. Install dependencies

   ```bash
        #Universal windows and linux
        pip install -r requirements.txt
   ```

5. Setup env variables
   ```bash  
        #linux
        - export FLASK_APP=politicer.py
        - export FLASK_DEBUG=1
        - export FLASK_ENV=development
   ```
   ```bash  
        #windows
        - set FLASK_APP=politicer.py
        - set FLASK_DEBUG=1
        - set FLASK_ENV=development
   ```
6. Manually Running tests
      ```
         python -m pytest --cov=app
      ```
7. Start the server
      ```
         flask run
      ```

app is available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## API Endpoints

| Method   | Endpoint                             | Description                                 |
| -------- | ------------------------------------ | -------------------------------------       |
| `POST`   | `/v1/admin/party`                    | Create a new party                          |
| `GET`    | `/v1/user/party`                     | View all parties                            |
| `GET`    | `/v1/user/party/<int:x>`             | Get party details by party Id               |
| `PATCH`  | `/v1/admin/party/<int:x>`            | Update a party  name                        |
| `DELETE` | `/v1/admin/party/<int:x>`            | Delete a party by Id                        |
| `GET`    | `/v1/user/office`                    | View All offices                            |
| `POST`   | `/v1/admin/office`                   | Post a new office                           |
| `GET`    | `/v1/user/offices/<int:x>`           | Get a specific office                       |


## Project management 

[Pivotal Tracker](https://www.pivotaltracker.com/n/projects/2241595)

## Deployment

[Heroku](https://politico-backend1.herokuapp.com/)

## Application Endpoints(Minimum data required to work with the endpoints)

  
    ```
      {
     "name": "party name",
     "hqAddress": "headquarters",
     "logoUrl": "imageUrl"

       }
      ```

    ```
      {
     "name": "office name",
     "type": "type"
      }
      ```
   
