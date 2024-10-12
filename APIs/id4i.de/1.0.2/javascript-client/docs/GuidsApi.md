# Id4iApi.GuidsApi

All URIs are relative to *http://backend.id4i.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addGuidAlias_0**](GuidsApi.md#addGuidAlias_0) | **POST** /api/v1/id4ns/{id4n}/alias/{aliasType} | Add alias for GUID or Collection
[**createGuid**](GuidsApi.md#createGuid) | **POST** /api/v1/guids | Create GUID(s)
[**deleteProperties_0**](GuidsApi.md#deleteProperties_0) | **DELETE** /api/v1/id4ns/{id4n}/properties | Delete ID4n properties
[**getCollections**](GuidsApi.md#getCollections) | **GET** /api/v1/id4ns/{id4n}/collections | Retrieve collections of an ID
[**getGuid**](GuidsApi.md#getGuid) | **GET** /api/v1/guids/{id4n} | Retrieve GUID information
[**getGuidAliases_0**](GuidsApi.md#getGuidAliases_0) | **GET** /api/v1/id4ns/{id4n}/alias | Get all aliases for the given GUID or Collection.
[**getGuidsWithoutCollection**](GuidsApi.md#getGuidsWithoutCollection) | **GET** /api/v1/guids/withoutCollection | Retrieve GUIDs not in any collection
[**getId4n**](GuidsApi.md#getId4n) | **GET** /api/v1/id4ns/{id4n} | Retrieve ID4n information
[**getMultipleProperties_0**](GuidsApi.md#getMultipleProperties_0) | **GET** /api/v1/multiple/id4ns/properties | Get multiple ID4n properties
[**getProperties_0**](GuidsApi.md#getProperties_0) | **GET** /api/v1/id4ns/{id4n}/properties | Retrieve ID4n properties
[**importGS1Codes**](GuidsApi.md#importGS1Codes) | **POST** /api/v1/import/gs1 | Import GS1/MAPP codes
[**patchProperties_0**](GuidsApi.md#patchProperties_0) | **PATCH** /api/v1/id4ns/{id4n}/properties | Patch ID4n properties
[**removeGuidAlias_0**](GuidsApi.md#removeGuidAlias_0) | **DELETE** /api/v1/id4ns/{id4n}/alias/{aliasType} | Remove aliases from GUID or Collection
[**updateGuid**](GuidsApi.md#updateGuid) | **PATCH** /api/v1/guids/{id4n} | Change GUID information.



## addGuidAlias_0

> addGuidAlias_0(id4n, aliasType, guidAlias)

Add alias for GUID or Collection

Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The GUID or Collection to operate on
let aliasType = "aliasType_example"; // String | Alias type, see the corresponding API model
let guidAlias = new Id4iApi.GuidAlias(); // GuidAlias | The alias to add or update
apiInstance.addGuidAlias_0(id4n, aliasType, guidAlias, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id4n** | **String**| The GUID or Collection to operate on | 
 **aliasType** | **String**| Alias type, see the corresponding API model | 
 **guidAlias** | [**GuidAlias**](GuidAlias.md)| The alias to add or update | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## createGuid

> ListOfId4ns createGuid(createGuidRequest)

Create GUID(s)

Creating one or more GUIDs with a specified length.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let createGuidRequest = new Id4iApi.CreateGuidRequest(); // CreateGuidRequest | GUID creation model
apiInstance.createGuid(createGuidRequest, (error, data, response) => {
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
 **createGuidRequest** | [**CreateGuidRequest**](CreateGuidRequest.md)| GUID creation model | 

### Return type

[**ListOfId4ns**](ListOfId4ns.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## deleteProperties_0

> deleteProperties_0(id4n, organizationId, requestBody)

Delete ID4n properties

Partial deletion of id4n properties. If the property does not exist, it will be ignored.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The id4n
let organizationId = "organizationId_example"; // String | The organization namespace to work on while deleting the properties.
let requestBody = ["null"]; // [String] | A set of property keys to delete.
apiInstance.deleteProperties_0(id4n, organizationId, requestBody, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id4n** | **String**| The id4n | 
 **organizationId** | **String**| The organization namespace to work on while deleting the properties. | 
 **requestBody** | [**[String]**](String.md)| A set of property keys to delete. | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## getCollections

> PaginatedResponseOfGuidCollection getCollections(id4n, opts)

Retrieve collections of an ID

Retrieving all owned or holding collections the specified id4n is assigned to.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The ID which the collections should contain
let opts = {
  'organizationId': "organizationId_example", // String | The organization holding the collections.
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getCollections(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| The ID which the collections should contain | 
 **organizationId** | **String**| The organization holding the collections. | [optional] 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfGuidCollection**](PaginatedResponseOfGuidCollection.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getGuid

> Guid getGuid(id4n, opts)

Retrieve GUID information

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The GUID number
let opts = {
  'organizationId': "organizationId_example" // String | The organization namespace to resolve.
};
apiInstance.getGuid(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| The GUID number | 
 **organizationId** | **String**| The organization namespace to resolve. | [optional] 

### Return type

[**Guid**](Guid.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getGuidAliases_0

> {String: String} getGuidAliases_0(id4n)

Get all aliases for the given GUID or Collection.

Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The GUID or Collection to operate on
apiInstance.getGuidAliases_0(id4n, (error, data, response) => {
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
 **id4n** | **String**| The GUID or Collection to operate on | 

### Return type

**{String: String}**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getGuidsWithoutCollection

> PaginatedResponseOfGuid getGuidsWithoutCollection(organizationId, opts)

Retrieve GUIDs not in any collection

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let organizationId = "organizationId_example"; // String | The namespace of the organization to search GUIDs for
let opts = {
  'offset': 56, // Number | Start with the n-th element
  'limit': 56 // Number | The maximum count of returned elements
};
apiInstance.getGuidsWithoutCollection(organizationId, opts, (error, data, response) => {
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
 **organizationId** | **String**| The namespace of the organization to search GUIDs for | 
 **offset** | **Number**| Start with the n-th element | [optional] 
 **limit** | **Number**| The maximum count of returned elements | [optional] 

### Return type

[**PaginatedResponseOfGuid**](PaginatedResponseOfGuid.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getId4n

> Id4nPresentation getId4n(id4n, opts)

Retrieve ID4n information

Retrieving basic information about an ID like the type and the creation time.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The ID to resolve to
let opts = {
  'organizationId': "organizationId_example" // String | The organization namespace to resolve.
};
apiInstance.getId4n(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| The ID to resolve to | 
 **organizationId** | **String**| The organization namespace to resolve. | [optional] 

### Return type

[**Id4nPresentation**](Id4nPresentation.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getMultipleProperties_0

> ListOfId4nProperties getMultipleProperties_0(id4ns, opts)

Get multiple ID4n properties

Get a list of ID4n properties for the specified ID4ns.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4ns = ["null"]; // [String] | The list of ID4ns to resolve.
let opts = {
  'organizationId': "organizationId_example" // String | The organization namespace.
};
apiInstance.getMultipleProperties_0(id4ns, opts, (error, data, response) => {
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
 **id4ns** | [**[String]**](String.md)| The list of ID4ns to resolve. | 
 **organizationId** | **String**| The organization namespace. | [optional] 

### Return type

[**ListOfId4nProperties**](ListOfId4nProperties.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## getProperties_0

> {String: String} getProperties_0(id4n, opts)

Retrieve ID4n properties

List all properties of an id4n.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The id4n
let opts = {
  'organizationId': "organizationId_example" // String | The organization namespace.
};
apiInstance.getProperties_0(id4n, opts, (error, data, response) => {
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
 **id4n** | **String**| The id4n | 
 **organizationId** | **String**| The organization namespace. | [optional] 

### Return type

**{String: String}**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## importGS1Codes

> importGS1Codes(importGS1CodesRequest)

Import GS1/MAPP codes

Importing GS1/MAPP codes that contain unique components.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let importGS1CodesRequest = new Id4iApi.ImportGS1CodesRequest(); // ImportGS1CodesRequest | The information how the MAPP codes should be imported and the list of MAPP codes
apiInstance.importGS1Codes(importGS1CodesRequest, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **importGS1CodesRequest** | [**ImportGS1CodesRequest**](ImportGS1CodesRequest.md)| The information how the MAPP codes should be imported and the list of MAPP codes | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml


## patchProperties_0

> patchProperties_0(id4n, organizationId, requestBody)

Patch ID4n properties

Partial updating of id4n properties. If a property contains a null value the property will be deleted other values will be saved and overwritten if they already exist.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The id4n
let organizationId = "organizationId_example"; // String | The organization namespace to work on while patching the properties.
let requestBody = {key: "null"}; // {String: String} | The properties to update.
apiInstance.patchProperties_0(id4n, organizationId, requestBody, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id4n** | **String**| The id4n | 
 **organizationId** | **String**| The organization namespace to work on while patching the properties. | 
 **requestBody** | [**{String: String}**](String.md)| The properties to update. | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: Not defined


## removeGuidAlias_0

> removeGuidAlias_0(id4n, aliasType)

Remove aliases from GUID or Collection

Remove the alias of the given type

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The GUID or Collection to operate on
let aliasType = "aliasType_example"; // String | Alias type, see the corresponding API model
apiInstance.removeGuidAlias_0(id4n, aliasType, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id4n** | **String**| The GUID or Collection to operate on | 
 **aliasType** | **String**| Alias type, see the corresponding API model | 

### Return type

null (empty response body)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml


## updateGuid

> Object updateGuid(id4n, guid)

Change GUID information.

Allows ownership transfer.

### Example

```javascript
import Id4iApi from 'id4i_api';
let defaultClient = Id4iApi.ApiClient.instance;
// Configure API key authorization: Authorization
let Authorization = defaultClient.authentications['Authorization'];
Authorization.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//Authorization.apiKeyPrefix = 'Token';

let apiInstance = new Id4iApi.GuidsApi();
let id4n = "id4n_example"; // String | The GUID number
let guid = new Id4iApi.Guid(); // Guid | request
apiInstance.updateGuid(id4n, guid, (error, data, response) => {
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
 **id4n** | **String**| The GUID number | 
 **guid** | [**Guid**](Guid.md)| request | 

### Return type

**Object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

- **Content-Type**: application/json, application/xml
- **Accept**: application/json, application/xml

