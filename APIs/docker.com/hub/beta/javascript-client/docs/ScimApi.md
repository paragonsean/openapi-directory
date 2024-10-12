# DockerHubApi.ScimApi

All URIs are relative to *https://hub.docker.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Scim20ResourceTypesGet**](ScimApi.md#v2Scim20ResourceTypesGet) | **GET** /v2/scim/2.0/ResourceTypes | List resource types
[**v2Scim20ResourceTypesNameGet**](ScimApi.md#v2Scim20ResourceTypesNameGet) | **GET** /v2/scim/2.0/ResourceTypes/{name} | Get a resource type
[**v2Scim20SchemasGet**](ScimApi.md#v2Scim20SchemasGet) | **GET** /v2/scim/2.0/Schemas | List schemas
[**v2Scim20SchemasIdGet**](ScimApi.md#v2Scim20SchemasIdGet) | **GET** /v2/scim/2.0/Schemas/{id} | Get a schema
[**v2Scim20ServiceProviderConfigGet**](ScimApi.md#v2Scim20ServiceProviderConfigGet) | **GET** /v2/scim/2.0/ServiceProviderConfig | Get service provider config
[**v2Scim20UsersGet**](ScimApi.md#v2Scim20UsersGet) | **GET** /v2/scim/2.0/Users | List users
[**v2Scim20UsersIdGet**](ScimApi.md#v2Scim20UsersIdGet) | **GET** /v2/scim/2.0/Users/{id} | Get a user
[**v2Scim20UsersIdPut**](ScimApi.md#v2Scim20UsersIdPut) | **PUT** /v2/scim/2.0/Users/{id} | Update a user
[**v2Scim20UsersPost**](ScimApi.md#v2Scim20UsersPost) | **POST** /v2/scim/2.0/Users | Create user



## v2Scim20ResourceTypesGet

> V2Scim20ResourceTypesGet200Response v2Scim20ResourceTypesGet()

List resource types

Returns all resource types supported for the SCIM configuration. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
apiInstance.v2Scim20ResourceTypesGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**V2Scim20ResourceTypesGet200Response**](V2Scim20ResourceTypesGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20ResourceTypesNameGet

> ScimResourceType v2Scim20ResourceTypesNameGet(name)

Get a resource type

Returns a resource type by name. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
let name = "User"; // String | 
apiInstance.v2Scim20ResourceTypesNameGet(name, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**|  | 

### Return type

[**ScimResourceType**](ScimResourceType.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20SchemasGet

> V2Scim20SchemasGet200Response v2Scim20SchemasGet()

List schemas

Returns all schemas supported for the SCIM configuration. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
apiInstance.v2Scim20SchemasGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**V2Scim20SchemasGet200Response**](V2Scim20SchemasGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20SchemasIdGet

> ScimSchema v2Scim20SchemasIdGet(id)

Get a schema

Returns a schema by ID. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
let id = "urn:ietf:params:scim:schemas:core:2.0:User"; // String | 
apiInstance.v2Scim20SchemasIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**|  | 

### Return type

[**ScimSchema**](ScimSchema.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20ServiceProviderConfigGet

> ScimServiceProviderConfig v2Scim20ServiceProviderConfigGet()

Get service provider config

Returns a service provider config for Docker&#39;s configuration. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
apiInstance.v2Scim20ServiceProviderConfigGet((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ScimServiceProviderConfig**](ScimServiceProviderConfig.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20UsersGet

> V2Scim20UsersGet200Response v2Scim20UsersGet(opts)

List users

List users, returns paginated users for an organization. Use &#x60;startIndex&#x60; and &#x60;count&#x60; query parameters to receive paginated results.  **Sorting:**&lt;br&gt; Sorting lets you to specify the order of returned resources by specifying a combination of &#x60;sortBy&#x60; and &#x60;sortOrder&#x60; query parameters.  The &#x60;sortBy&#x60; parameter specifies the attribute whose value will be used to order the returned responses. The &#x60;sortOrder&#x60; parameter defines the order in which the &#x60;sortBy&#x60; parameter is applied. Allowed values are \&quot;ascending\&quot; and \&quot;descending\&quot;.  **Filtering:**&lt;br&gt; You can request a subset of resources by specifying the &#x60;filter&#x60; query parameter containing a filter expression. Attribute names and attribute operators used in filters are case insensitive. The filter parameter must contain at least one valid expression. Each expression must contain an attribute name followed by an attribute operator and an optional value.  Supported operators are listed below.  - &#x60;eq&#x60; equal - &#x60;ne&#x60; not equal - &#x60;co&#x60; contains - &#x60;sw&#x60; starts with - &#x60;and&#x60; Logical \&quot;and\&quot; - &#x60;or&#x60; Logical \&quot;or\&quot; - &#x60;not&#x60; \&quot;Not\&quot; function - &#x60;()&#x60; Precedence grouping 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
let opts = {
  'startIndex': 1, // Number | 
  'count': 10, // Number | 
  'filter': "userName eq \"jon.snow@docker.com\"", // String | 
  'attributes': "userName,displayName", // String | Comma delimited list of attributes to limit to in the response.
  'sortOrder': "sortOrder_example", // String | 
  'sortBy': "userName" // String | User attribute to sort by.
};
apiInstance.v2Scim20UsersGet(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startIndex** | **Number**|  | [optional] 
 **count** | **Number**|  | [optional] 
 **filter** | **String**|  | [optional] 
 **attributes** | **String**| Comma delimited list of attributes to limit to in the response. | [optional] 
 **sortOrder** | **String**|  | [optional] 
 **sortBy** | **String**| User attribute to sort by. | [optional] 

### Return type

[**V2Scim20UsersGet200Response**](V2Scim20UsersGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20UsersIdGet

> ScimUser v2Scim20UsersIdGet(id)

Get a user

Returns a user by ID. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
let id = "d80f7c79-7730-49d8-9a41-7c42fb622d9c"; // String | The user ID.
apiInstance.v2Scim20UsersIdGet(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The user ID. | 

### Return type

[**ScimUser**](ScimUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/scim+json


## v2Scim20UsersIdPut

> ScimUser v2Scim20UsersIdPut(id, v2Scim20UsersIdPutRequest)

Update a user

Updates a user. Use this route to change the user&#39;s name, activate, and deactivate the user. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
let id = "d80f7c79-7730-49d8-9a41-7c42fb622d9c"; // String | The user ID.
let v2Scim20UsersIdPutRequest = new DockerHubApi.V2Scim20UsersIdPutRequest(); // V2Scim20UsersIdPutRequest | 
apiInstance.v2Scim20UsersIdPut(id, v2Scim20UsersIdPutRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| The user ID. | 
 **v2Scim20UsersIdPutRequest** | [**V2Scim20UsersIdPutRequest**](V2Scim20UsersIdPutRequest.md)|  | 

### Return type

[**ScimUser**](ScimUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json


## v2Scim20UsersPost

> ScimUser v2Scim20UsersPost(v2Scim20UsersPostRequest)

Create user

Creates a user. If the user already exists by email, they are assigned to the organization on the \&quot;company\&quot; team. 

### Example

```javascript
import DockerHubApi from 'docker_hub_api';

let apiInstance = new DockerHubApi.ScimApi();
let v2Scim20UsersPostRequest = new DockerHubApi.V2Scim20UsersPostRequest(); // V2Scim20UsersPostRequest | 
apiInstance.v2Scim20UsersPost(v2Scim20UsersPostRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v2Scim20UsersPostRequest** | [**V2Scim20UsersPostRequest**](V2Scim20UsersPostRequest.md)|  | 

### Return type

[**ScimUser**](ScimUser.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/scim+json
- **Accept**: application/scim+json

