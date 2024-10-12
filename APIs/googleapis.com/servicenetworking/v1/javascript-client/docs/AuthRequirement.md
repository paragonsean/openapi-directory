# ServiceNetworkingApi.AuthRequirement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **String** | NOTE: This will be deprecated soon, once AuthProvider.audiences is implemented and accepted in all the runtime components. The list of JWT [audiences](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section-4.1.3). that are allowed to access. A JWT containing any of these audiences will be accepted. When this setting is absent, only JWTs with audience \&quot;https://Service_name/API_name\&quot; will be accepted. For example, if no audiences are in the setting, LibraryService API will only accept JWTs with the following audience \&quot;https://library-example.googleapis.com/google.example.library.v1.LibraryService\&quot;. Example: audiences: bookstore_android.apps.googleusercontent.com, bookstore_web.apps.googleusercontent.com | [optional] 
**providerId** | **String** | id from authentication provider. Example: provider_id: bookstore_auth | [optional] 


