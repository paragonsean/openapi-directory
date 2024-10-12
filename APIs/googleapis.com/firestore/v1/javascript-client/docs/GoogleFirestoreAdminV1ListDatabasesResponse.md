# CloudFirestoreApi.GoogleFirestoreAdminV1ListDatabasesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases** | [**[GoogleFirestoreAdminV1Database]**](GoogleFirestoreAdminV1Database.md) | The databases in the project. | [optional] 
**unreachable** | **[String]** | In the event that data about individual databases cannot be listed they will be recorded here. An example entry might be: projects/some_project/locations/some_location This can happen if the Cloud Region that the Database resides in is currently unavailable. In this case we can&#39;t fetch all the details about the database. You may be able to get a more detailed error message (or possibly fetch the resource) by sending a &#39;Get&#39; request for the resource or a &#39;List&#39; request for the specific location. | [optional] 


