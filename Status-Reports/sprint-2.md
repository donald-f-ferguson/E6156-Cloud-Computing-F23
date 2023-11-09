# Eunomia Sprint 2 Status Report

## Major Tasks

The major tasks for sprint 2 are the following:
1. _Enhance Microservices Implementation_: Make progress on the implementation 
of the 3 core microservices. Specifically,
   2. Have sample data for all of the resources.
   3. Implement the 4 core operations (GET, PUT, POST, DELETE) for each
resource.
   4. Implement filtering using query strings for at least one resource.
   5. Implement pagination for at least one resource.<br><br>
6. _Events, Notifications, Pub/Sub:_ 
   1. One of the microservices should publish an event to an SNS or Google Pub/Sub
   topic when a resource changes due to a PUT, POST or DELETE.
   2. There should be a Lambda function or Google function that subscribes to the
topic and performs an action when notified. This can be as simple
as sending an email, posting to Discord, ... ...<br><br>
3. _Composition/Aggregators:_ Develop a simple microservice that
implements the composition pattern, building functionality on top of
the 3 basic microservices. Implementing a GET that retrieves relevant
information from the basic services to produce a large resource is fine.
You must have two implementations of the operation:
   1. Sychronous calls each one of the aggregated microservices one
at a time, synchronously.
   2. Asynchronous uses a capability like Promise, Callbacks or Threads
to call the aggregated services in parallel and "gather" the asynchronous
responses to return.<br><br>
4. _API Gateway:_
   1. You must encapsulate at least one microservice behind the API GW.
   2. Implement an API GW Authorizer that checks for a JWT token and
determines whether or not to allow the operation to complete.
   3. You can manually set a simple JWT token in an authorization
header using POSTMAN. You must, however, show encoding and decoding
a token.
   3. This can be very, very simple.<br><br>
5. _SSO:_ Implement a simple example of single-sign on with Google.<br><br>
6. _External API:_ Demonstrate that one of the microservices calls an external, cloud REST service.