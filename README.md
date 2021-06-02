# CodingDojo_Django_TVShows
Django app that can handle all of the CRUD operations (create, read, update and destroy) for a table that displays TV Shows.  Create and Update operations include validation rules before saving the records in the database.

1. Index rout redirects to main route.
2. GET request to /shows - calls the main method to display a template with all the shows. 
3. GET request to /shows/new - calls the new method to display a form template allowing users to create a new show. 
4. GET request to /shows/<id>/edit - calls the edit method to display a form template allowing users to edit an existing show with the given id. 
5. GET /shows/<id> - calls the show method to display the info for a particular show with given id. This will need a template.
6. POST to /shows/create - calls the create method to insert a new show record into the database. The POST is sent from the form on the page /shows/new. App redirects to /shows/<id> once created.
7. GET /shows/<id>/destroy - calls the destroy method to remove a particular show with the given id. App redirects back to /shows once deleted.
9. POST /shows/update - calls the update method to process the submitted form sent from /shows/<id>/edit. App redirects to /shows/<id> once updated.
