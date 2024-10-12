# Superset.DatabaseApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**databaseAvailableGet**](DatabaseApi.md#databaseAvailableGet) | **GET** /database/available/ | 
[**databaseExportGet**](DatabaseApi.md#databaseExportGet) | **GET** /database/export/ | 
[**databaseGet**](DatabaseApi.md#databaseGet) | **GET** /database/ | 
[**databaseImportPost**](DatabaseApi.md#databaseImportPost) | **POST** /database/import/ | 
[**databaseInfoGet**](DatabaseApi.md#databaseInfoGet) | **GET** /database/_info | 
[**databasePkDelete**](DatabaseApi.md#databasePkDelete) | **DELETE** /database/{pk} | 
[**databasePkFunctionNamesGet**](DatabaseApi.md#databasePkFunctionNamesGet) | **GET** /database/{pk}/function_names/ | 
[**databasePkGet**](DatabaseApi.md#databasePkGet) | **GET** /database/{pk} | 
[**databasePkPut**](DatabaseApi.md#databasePkPut) | **PUT** /database/{pk} | 
[**databasePkRelatedObjectsGet**](DatabaseApi.md#databasePkRelatedObjectsGet) | **GET** /database/{pk}/related_objects/ | 
[**databasePkSchemasGet**](DatabaseApi.md#databasePkSchemasGet) | **GET** /database/{pk}/schemas/ | 
[**databasePkSelectStarTableNameGet**](DatabaseApi.md#databasePkSelectStarTableNameGet) | **GET** /database/{pk}/select_star/{table_name}/ | 
[**databasePkSelectStarTableNameSchemaNameGet**](DatabaseApi.md#databasePkSelectStarTableNameSchemaNameGet) | **GET** /database/{pk}/select_star/{table_name}/{schema_name}/ | 
[**databasePkTableTableNameSchemaNameGet**](DatabaseApi.md#databasePkTableTableNameSchemaNameGet) | **GET** /database/{pk}/table/{table_name}/{schema_name}/ | 
[**databasePost**](DatabaseApi.md#databasePost) | **POST** /database/ | 
[**databaseTestConnectionPost**](DatabaseApi.md#databaseTestConnectionPost) | **POST** /database/test_connection | 
[**databaseValidateParametersPost**](DatabaseApi.md#databaseValidateParametersPost) | **POST** /database/validate_parameters | 



## databaseAvailableGet

> [DatabaseAvailableGet200ResponseInner] databaseAvailableGet()



Get names of databases currently available

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
apiInstance.databaseAvailableGet((error, data, response) => {
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

[**[DatabaseAvailableGet200ResponseInner]**](DatabaseAvailableGet200ResponseInner.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseExportGet

> File databaseExportGet(opts)



Download database(s) and associated dataset(s) as a zip file

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.databaseExportGet(opts, (error, data, response) => {
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


## databaseGet

> DatabaseGet200Response databaseGet(opts)



Get a list of models

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.databaseGet(opts, (error, data, response) => {
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

[**DatabaseGet200Response**](DatabaseGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databaseImportPost

> AnnotationLayerGet400Response databaseImportPost(opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let opts = {
  'formData': "/path/to/file", // File | upload file (ZIP)
  'overwrite': true, // Boolean | overwrite existing databases?
  'passwords': "passwords_example" // String | JSON map of passwords for each file
};
apiInstance.databaseImportPost(opts, (error, data, response) => {
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
 **overwrite** | **Boolean**| overwrite existing databases? | [optional] 
 **passwords** | **String**| JSON map of passwords for each file | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## databaseInfoGet

> AnnotationLayerInfoGet200Response databaseInfoGet(opts)



Get metadata information about this API resource

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.databaseInfoGet(opts, (error, data, response) => {
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


## databasePkDelete

> AnnotationLayerGet400Response databasePkDelete(pk)



Deletes a Database.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | 
apiInstance.databasePkDelete(pk, (error, data, response) => {
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


## databasePkFunctionNamesGet

> DatabaseFunctionNamesResponse databasePkFunctionNamesGet(pk)



Get function names supported by a database

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | 
apiInstance.databasePkFunctionNamesGet(pk, (error, data, response) => {
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

[**DatabaseFunctionNamesResponse**](DatabaseFunctionNamesResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePkGet

> DatabasePkGet200Response databasePkGet(pk, opts)



Get an item model

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.databasePkGet(pk, opts, (error, data, response) => {
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

[**DatabasePkGet200Response**](DatabasePkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePkPut

> DatabasePkPut200Response databasePkPut(pk, databaseRestApiPut)



Changes a Database.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | 
let databaseRestApiPut = new Superset.DatabaseRestApiPut(); // DatabaseRestApiPut | Database schema
apiInstance.databasePkPut(pk, databaseRestApiPut, (error, data, response) => {
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
 **databaseRestApiPut** | [**DatabaseRestApiPut**](DatabaseRestApiPut.md)| Database schema | 

### Return type

[**DatabasePkPut200Response**](DatabasePkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databasePkRelatedObjectsGet

> DatabaseRelatedObjectsResponse databasePkRelatedObjectsGet(pk)



Get charts and dashboards count associated to a database

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | 
apiInstance.databasePkRelatedObjectsGet(pk, (error, data, response) => {
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

[**DatabaseRelatedObjectsResponse**](DatabaseRelatedObjectsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePkSchemasGet

> SchemasResponseSchema databasePkSchemasGet(pk, opts)



Get all schemas from a database

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | The database id
let opts = {
  'q': new Superset.DatabaseSchemasQuerySchema() // DatabaseSchemasQuerySchema | 
};
apiInstance.databasePkSchemasGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**| The database id | 
 **q** | [**DatabaseSchemasQuerySchema**](.md)|  | [optional] 

### Return type

[**SchemasResponseSchema**](SchemasResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePkSelectStarTableNameGet

> SelectStarResponseSchema databasePkSelectStarTableNameGet(pk, tableName, schemaName)



Get database select star for table

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | The database id
let tableName = "tableName_example"; // String | Table name
let schemaName = "schemaName_example"; // String | Table schema
apiInstance.databasePkSelectStarTableNameGet(pk, tableName, schemaName, (error, data, response) => {
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
 **pk** | **Number**| The database id | 
 **tableName** | **String**| Table name | 
 **schemaName** | **String**| Table schema | 

### Return type

[**SelectStarResponseSchema**](SelectStarResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePkSelectStarTableNameSchemaNameGet

> SelectStarResponseSchema databasePkSelectStarTableNameSchemaNameGet(pk, tableName, schemaName)



Get database select star for table

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | The database id
let tableName = "tableName_example"; // String | Table name
let schemaName = "schemaName_example"; // String | Table schema
apiInstance.databasePkSelectStarTableNameSchemaNameGet(pk, tableName, schemaName, (error, data, response) => {
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
 **pk** | **Number**| The database id | 
 **tableName** | **String**| Table name | 
 **schemaName** | **String**| Table schema | 

### Return type

[**SelectStarResponseSchema**](SelectStarResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePkTableTableNameSchemaNameGet

> TableMetadataResponseSchema databasePkTableTableNameSchemaNameGet(pk, tableName, schemaName)



Get database table metadata

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let pk = 56; // Number | The database id
let tableName = "tableName_example"; // String | Table name
let schemaName = "schemaName_example"; // String | Table schema
apiInstance.databasePkTableTableNameSchemaNameGet(pk, tableName, schemaName, (error, data, response) => {
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
 **pk** | **Number**| The database id | 
 **tableName** | **String**| Table name | 
 **schemaName** | **String**| Table schema | 

### Return type

[**TableMetadataResponseSchema**](TableMetadataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## databasePost

> DatabasePost201Response databasePost(databaseRestApiPost)



Create a new Database.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let databaseRestApiPost = new Superset.DatabaseRestApiPost(); // DatabaseRestApiPost | Database schema
apiInstance.databasePost(databaseRestApiPost, (error, data, response) => {
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
 **databaseRestApiPost** | [**DatabaseRestApiPost**](DatabaseRestApiPost.md)| Database schema | 

### Return type

[**DatabasePost201Response**](DatabasePost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseTestConnectionPost

> AnnotationLayerGet400Response databaseTestConnectionPost(databaseTestConnectionSchema)



Tests a database connection

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let databaseTestConnectionSchema = new Superset.DatabaseTestConnectionSchema(); // DatabaseTestConnectionSchema | Database schema
apiInstance.databaseTestConnectionPost(databaseTestConnectionSchema, (error, data, response) => {
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
 **databaseTestConnectionSchema** | [**DatabaseTestConnectionSchema**](DatabaseTestConnectionSchema.md)| Database schema | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## databaseValidateParametersPost

> AnnotationLayerGet400Response databaseValidateParametersPost(databaseValidateParametersSchema)



Validates parameters used to connect to a database

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatabaseApi();
let databaseValidateParametersSchema = new Superset.DatabaseValidateParametersSchema(); // DatabaseValidateParametersSchema | DB-specific parameters
apiInstance.databaseValidateParametersPost(databaseValidateParametersSchema, (error, data, response) => {
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
 **databaseValidateParametersSchema** | [**DatabaseValidateParametersSchema**](DatabaseValidateParametersSchema.md)| DB-specific parameters | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

