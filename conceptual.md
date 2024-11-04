### Conceptual Exercise

Answer the following questions below:
///
- What are important differences between Python and JavaScript?
1.
Python: Runs in a dedicated Python interpreter, such as CPython, and isn’t native to the browser.
JavaScript: Originally designed for web browsers, where it executes directly. It’s also supported server-side by Node.js.
2.
Python: Emphasizes readability and simplicity, using indentation to define blocks of code, which can make it easier for beginners.
JavaScript: Syntax is similar to languages like C or Java, with braces {} for code blocks. It’s also more lenient with syntax rules, but this can sometimes lead to unexpected behavior.
///
- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
my_dict = {"a": 1, "b": 2}
value = my_dict.setdefault("c", 0)  # Adds "c": 0 if "c" is not in the dictionary
print(value)  # Output: 0
print(my_dict)  # Output: {"a": 1, "b": 2, "c": 0}
///
- What is a unit test?
Unit tests check a single “unit” of functionality, typically a function, method, or class, without involving other parts of the system. This makes them precise and easy to troubleshoot.
///
- What is an integration test?
An integration test is a type of software test that checks how different modules or components of an application work together as a group. Unlike unit tests, which test individual functions or classes in isolation, integration tests focus on the interactions between multiple components to ensure they work together as expected in a larger workflow. These tests help identify issues that might arise from the interfaces between different parts of the code.
///
- What is the role of web application framework, like Flask?
A web application framework like Flask provides the foundational tools, libraries, and structure to build web applications efficiently. Flask, in particular, is a lightweight and flexible framework for Python, designed to simplify common web development tasks and let developers focus on writing application logic without worrying about low-level details.
///
- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
  
  Route Parameters (e.g., '/foods/pretzel')
  Use Case: When the parameter is an essential part of the resource’s identity.

  Query Parameters (e.g., '/foods?type=pretzel')
  Use Case: When the parameter modifies the request but doesn’t define a unique resource.
///
- How do you collect data from a URL placeholder parameter using Flask?
Suppose you have a route with a placeholder parameter like '/foods/<food_name>', and you want to collect the food_name parameter
///
- How do you collect data from the query string using Flask?
To collect data from the query string in Flask, you use the request.args attribute, which provides access to the query parameters as a dictionary. request.args allows you to retrieve values passed in the URL after the ?.
///
- How do you collect data from the body of the request using Flask?
To collect data from the body of a request in Flask, you use the request object's methods, which provide access to different types of data in the body (such as form data, JSON data, or raw data).
///
- What is a cookie and what kinds of things are they commonly used for?
A cookie is a small piece of data that websites store on a user's browser to remember information about their visit. Cookies are typically used to personalize user experiences, enhance website functionality, and track user behavior.
///
- What is the session object in Flask?
In Flask, the session object is a special object that allows you to store information across requests made by a user during their session on the website. This is especially useful for tracking user data, like login status or preferences, across multiple page visits.
///
- What does Flask's `jsonify()` do?
In Flask, the jsonify() function converts Python data structures into JSON (JavaScript Object Notation) format, which is a widely used data format for web APIs.