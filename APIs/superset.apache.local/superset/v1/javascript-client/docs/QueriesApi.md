# Superset.QueriesApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**queryDistinctColumnNameGet**](QueriesApi.md#queryDistinctColumnNameGet) | **GET** /query/distinct/{column_name} | 
[**queryGet**](QueriesApi.md#queryGet) | **GET** /query/ | 
[**queryPkGet**](QueriesApi.md#queryPkGet) | **GET** /query/{pk} | 
[**queryRelatedColumnNameGet**](QueriesApi.md#queryRelatedColumnNameGet) | **GET** /query/related/{column_name} | 
[**savedQueryDelete**](QueriesApi.md#savedQueryDelete) | **DELETE** /saved_query/ | 
[**savedQueryDistinctColumnNameGet**](QueriesApi.md#savedQueryDistinctColumnNameGet) | **GET** /saved_query/distinct/{column_name} | 
[**savedQueryExportGet**](QueriesApi.md#savedQueryExportGet) | **GET** /saved_query/export/ | 
[**savedQueryGet**](QueriesApi.md#savedQueryGet) | **GET** /saved_query/ | 
[**savedQueryImportPost**](QueriesApi.md#savedQueryImportPost) | **POST** /saved_query/import/ | 
[**savedQueryInfoGet**](QueriesApi.md#savedQueryInfoGet) | **GET** /saved_query/_info | 
[**savedQueryPkDelete**](QueriesApi.md#savedQueryPkDelete) | **DELETE** /saved_query/{pk} | 
[**savedQueryPkGet**](QueriesApi.md#savedQueryPkGet) | **GET** /saved_query/{pk} | 
[**savedQueryPkPut**](QueriesApi.md#savedQueryPkPut) | **PUT** /saved_query/{pk} | 
[**savedQueryPost**](QueriesApi.md#savedQueryPost) | **POST** /saved_query/ | 
[**savedQueryRelatedColumnNameGet**](QueriesApi.md#savedQueryRelatedColumnNameGet) | **GET** /saved_query/related/{column_name} | 



## queryDistinctColumnNameGet

> DistincResponseSchema queryDistinctColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.queryDistinctColumnNameGet(columnName, opts, (error, data, response) => {
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
 **columnName** | **String**|  | 
 **q** | [**GetRelatedSchema**](.md)|  | [optional] 

### Return type

[**DistincResponseSchema**](DistincResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryGet

> QueryGet200Response queryGet(opts)



Get a list of queries, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.queryGet(opts, (error, data, response) => {
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
 **q** | [**GetListSchema**](.md)|  | [optional] 

### Return type

[**QueryGet200Response**](QueryGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryPkGet

> QueryPkGet200Response queryPkGet(pk, opts)



Get query detail information.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.queryPkGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**|  | 
 **q** | [**GetItemSchema**](.md)|  | [optional] 

### Return type

[**QueryPkGet200Response**](QueryPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## queryRelatedColumnNameGet

> RelatedResponseSchema queryRelatedColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.queryRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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
 **columnName** | **String**|  | 
 **q** | [**GetRelatedSchema**](.md)|  | [optional] 

### Return type

[**RelatedResponseSchema**](RelatedResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryDelete

> AnnotationLayerGet400Response savedQueryDelete(opts)



Deletes multiple saved queries in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.savedQueryDelete(opts, (error, data, response) => {
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
 **q** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryDistinctColumnNameGet

> DistincResponseSchema savedQueryDistinctColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.savedQueryDistinctColumnNameGet(columnName, opts, (error, data, response) => {
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
 **columnName** | **String**|  | 
 **q** | [**GetRelatedSchema**](.md)|  | [optional] 

### Return type

[**DistincResponseSchema**](DistincResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryExportGet

> File savedQueryExportGet(opts)



Exports multiple saved queries and downloads them as YAML files

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.savedQueryExportGet(opts, (error, data, response) => {
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
 **q** | [**[Number]**](Number.md)|  | [optional] 

### Return type

**File**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip, application/json


## savedQueryGet

> SavedQueryGet200Response savedQueryGet(opts)



Get a list of saved queries, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.savedQueryGet(opts, (error, data, response) => {
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
 **q** | [**GetListSchema**](.md)|  | [optional] 

### Return type

[**SavedQueryGet200Response**](SavedQueryGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryImportPost

> AnnotationLayerGet400Response savedQueryImportPost(opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let opts = {
  'formData': "/path/to/file", // File | upload file (ZIP)
  'overwrite': true, // Boolean | overwrite existing saved queries?
  'passwords': "passwords_example" // String | JSON map of passwords for each file
};
apiInstance.savedQueryImportPost(opts, (error, data, response) => {
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
 **formData** | **File**| upload file (ZIP) | [optional] 
 **overwrite** | **Boolean**| overwrite existing saved queries? | [optional] 
 **passwords** | **String**| JSON map of passwords for each file | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## savedQueryInfoGet

> AnnotationLayerInfoGet200Response savedQueryInfoGet(opts)



Get metadata information about this API resource

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.savedQueryInfoGet(opts, (error, data, response) => {
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
 **q** | [**GetInfoSchema**](.md)|  | [optional] 

### Return type

[**AnnotationLayerInfoGet200Response**](AnnotationLayerInfoGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryPkDelete

> AnnotationLayerGet400Response savedQueryPkDelete(pk)



Delete saved query

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let pk = 56; // Number | 
apiInstance.savedQueryPkDelete(pk, (error, data, response) => {
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
 **pk** | **Number**|  | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryPkGet

> SavedQueryPkGet200Response savedQueryPkGet(pk, opts)



Get a saved query

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.savedQueryPkGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**|  | 
 **q** | [**GetItemSchema**](.md)|  | [optional] 

### Return type

[**SavedQueryPkGet200Response**](SavedQueryPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## savedQueryPkPut

> SavedQueryPkPut200Response savedQueryPkPut(pk, savedQueryRestApiPut)



Update a saved query

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let pk = 56; // Number | 
let savedQueryRestApiPut = new Superset.SavedQueryRestApiPut(); // SavedQueryRestApiPut | Model schema
apiInstance.savedQueryPkPut(pk, savedQueryRestApiPut, (error, data, response) => {
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
 **pk** | **Number**|  | 
 **savedQueryRestApiPut** | [**SavedQueryRestApiPut**](SavedQueryRestApiPut.md)| Model schema | 

### Return type

[**SavedQueryPkPut200Response**](SavedQueryPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## savedQueryPost

> SavedQueryPost201Response savedQueryPost(savedQueryRestApiPost)



Create a saved query

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let savedQueryRestApiPost = new Superset.SavedQueryRestApiPost(); // SavedQueryRestApiPost | Model schema
apiInstance.savedQueryPost(savedQueryRestApiPost, (error, data, response) => {
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
 **savedQueryRestApiPost** | [**SavedQueryRestApiPost**](SavedQueryRestApiPost.md)| Model schema | 

### Return type

[**SavedQueryPost201Response**](SavedQueryPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## savedQueryRelatedColumnNameGet

> RelatedResponseSchema savedQueryRelatedColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.QueriesApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.savedQueryRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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
 **columnName** | **String**|  | 
 **q** | [**GetRelatedSchema**](.md)|  | [optional] 

### Return type

[**RelatedResponseSchema**](RelatedResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

