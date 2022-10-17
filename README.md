# RESTful API

REpresentational State Transfer (REST) is a software architectural style that describes a uniform interface between two seperate components. It was created by Roy Fielding.

- It follows Client-Server architecture.
- It describes a machine to machine interface.
- It provides dynamic content.

It has four interface constraints.
- Indentification of resources.
- Manipulation of resources.
- Self-descriptive message.
- Hypermedia as the engine of application state.

> Hypermedia is the non-linear medium of information that includes graphics, audio, video, plain text and hyperlink.

The **REST API** is an application programming interface (API or web API) that follows the constraints of REST architectural style. It is defined to be as simple as possible for two machine to interact.

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/196176161-baa1a556-6e38-44e6-966a-a250d2999e80.jpg">
</p>


## Why Use REST API?

- It is easy to understand and learn.
- It is stateless. Server doesn't need to remember previous requests.
- We can organize complicated application and make it easy to use resources.
- Easy integration with new clients
- Use Standard HTTP procedure to retrieve data and requests.
- Uses JSON format which is easy to learn and navigate.
- Can be used with any type of application and device.

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/196176738-ca715077-1d02-4223-aef4-30c497e21f5e.png">
</p>

## What is a REST API call

A REST API call is a call made from a client to a server following REST architecture principles. The data is received back over the HTTP protocol.

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/196178466-8045b69b-24ca-4767-a2d5-45edccb7e11f.png">
</p>


## GET, PUT, POST, DELETE

These are the HTTP methods we can use for RESTful Services.

- **POST** - It is used to Create a resource.
- **GET** - It is used to Read from a resource.
- **PUT** - It is use to Update a resource.
- **DELETE** - It is use to delete a resource.

For Example: For a pet store, the API calls can be:

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/196180256-986c632e-88ae-4aff-84f8-968dfa8bdcdf.png">
</p>


We also have 3 additional methods:
- **PATCH** - use to update/modify a small portion of a large amount of data.
- **HEAD** - Similar to **GET**, but no resonse body is received from the server.
- **OPTIONS** - It basically returns the methods and operations the server supports. 


## Why Python with REST?

Python makes it very easy to work with API. With its easy to use syntax and a range of libraries and framework, a restful application can be easily made using Python. Few advantages include:

- Library like `requests` makes it very easy to send HTTP requests.
- The resulting response can be handled like normal python program.
- The Django REST framework can be used to create Python REST APIs. 
- Supports Authentication and Authorization when needed.
- **HTTP Basic Auth** can be used to send login and password details to the required endpoint.
- Supports both XML and JSON
