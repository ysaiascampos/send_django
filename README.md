### Django Exercises 🎈​

- Setup a Django app
   1. Create a private repository within your GitHub and invite the reviewers:
      1. zabbix-byte
      2. pfolch
   2. Create a Django app with the following specifications (you can add as many libraries as you wish)
      - Django==3.1.13
      - djangorestframework==3.11.0
   3. Set up a docker-compose for the created app 🏎️​

**Once the application has been created with the initial configuration specified, you must perform, within the same application created, the exercises detailed below:**

### Create an endpoint 

In this task you will have to create an endpoint with the path `/valerdat/prods/`


1. Model Creation
   - model name: prods
   - model fields: ref,zipcode,store,amount

2. Create the serializer
3. Create the detail view and the list view (CRUD)
4. Creating filters and sorts

### Product localization
**To do this exercise you will have to have the steps of exercise 1 completed**

1. Create an endpoint with the path `/valerdat/coordsprods/`
2. Create an endpoint that uses the prods model from exercise 1, from the zipcodes fetch the coordinates and display them in a json format.
3. `[{"prod": ref, "lat": <lat>, "long": <long>}.....]`

### Product localization
**To do this exercise you will have to have the steps of exercise 1 completed**

1. Create an endpoint with the path `/valerdat/coordsprods/`
2. Create an endpoint that uses the prods model from exercise 1, from the zipcodes fetch the coordinates and display them in a json format.
3. `[{"prod": ref, "lat": <lat>, "long": <long>}.....]`

The last commit to be considered for the correction of the exercises will be the last commit made within 3 hours after accessing the repository. Code readability, robustness and optimality will be taken into account.

Good luck with the challenge, and remember that the important thing is not to finish, but to do your best!
