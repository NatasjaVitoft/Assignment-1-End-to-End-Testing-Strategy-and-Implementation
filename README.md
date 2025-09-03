# OLA1

## Test strategy document
### Product background
The product is a very simple to-do application written in Python and using an SQLite in-memory database. The application allows users to create tasks for their to-do list as well as categorize the different tasks into lists. The user can also set deadlines for the different tasks.
### Features for testing
Below is a list of the different features that are going to be tested: 
* Add tasks
*	Delete tasks
*	Mark tasks as completed 
*	Add lists 
*	Delete lists
*	Add a task to a list
*	Remove a task from a list
### Test approach 
The types of tests will consist of 5 unit tests, 2 integration tests and 1 specification-based test. 
The 5 unit tests will be conducted during development of the application while the 2 integration tests will be conducted after all features are developed, to test if the different features work together. 
A specification-based test will be conducted after the integration tests. 
### Tools
The test framework will be PyTest and the use of the coverage report from the PyTest library. 
## Metrics
At least 80% coverage in our tests. 


## Discussion and reflection 
### Test doubles
I decided to use test doubles for most of the unit tests, and in particular I used solitary test doubles instead of sociable doubles as Martin Fowler describes it to ensure that the functions worked as expected without having to rely on external services. I use fake doubles as test doubles for all the unit tests. The way I do this is to ensure that at the beginning of every unit test I set up an in-memory database (SQLITE) that only exists within that test. The reason I did this was that I would be able to query the in-memory database in plain SQL, which is straight forward and would also be a good representation of a production database compared to for example mocks. The cons about using an in-memory database could be that it is a bit slower than, for example using mocks, but for this case with the to-do list application it will be just fine because it’s not a large application. Also, there could be some differences in terms of SQL syntax from the in-memory database, which is plain SQL syntax compared to the production database, which might be a PostgreSQL database and have a different syntax. (https://martinfowler.com/bliki/TestDouble.html, https://martinfowler.com/bliki/InMemoryTestDatabase.html) 

### Integration testing 
As fowler mentions in his article (https://martinfowler.com/bliki/IntegrationTest.html) there is much confusion about what a integration test really is. He talks about two types: Narrow integration test and Broad integration testing. I have tried to do both. For the narrow integration test i tested that an existing task can be added to an existing list using a in-memory database. Here i mock the external service (database) and test that the seperate functionalities works together. Fowler also talks about broad integration testing which includes testing the functionality with all of the production services. I did not do this since i didnt have a real database, but i did make a console based solution where i tested that the different functionalities worked together from a users perspective. 



