# Superset.DatasetsApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**datasetDelete**](DatasetsApi.md#datasetDelete) | **DELETE** /dataset/ | 
[**datasetDistinctColumnNameGet**](DatasetsApi.md#datasetDistinctColumnNameGet) | **GET** /dataset/distinct/{column_name} | 
[**datasetExportGet**](DatasetsApi.md#datasetExportGet) | **GET** /dataset/export/ | 
[**datasetGet**](DatasetsApi.md#datasetGet) | **GET** /dataset/ | 
[**datasetImportPost**](DatasetsApi.md#datasetImportPost) | **POST** /dataset/import/ | 
[**datasetInfoGet**](DatasetsApi.md#datasetInfoGet) | **GET** /dataset/_info | 
[**datasetPkColumnColumnIdDelete**](DatasetsApi.md#datasetPkColumnColumnIdDelete) | **DELETE** /dataset/{pk}/column/{column_id} | 
[**datasetPkDelete**](DatasetsApi.md#datasetPkDelete) | **DELETE** /dataset/{pk} | 
[**datasetPkGet**](DatasetsApi.md#datasetPkGet) | **GET** /dataset/{pk} | 
[**datasetPkMetricMetricIdDelete**](DatasetsApi.md#datasetPkMetricMetricIdDelete) | **DELETE** /dataset/{pk}/metric/{metric_id} | 
[**datasetPkPut**](DatasetsApi.md#datasetPkPut) | **PUT** /dataset/{pk} | 
[**datasetPkRefreshPut**](DatasetsApi.md#datasetPkRefreshPut) | **PUT** /dataset/{pk}/refresh | 
[**datasetPkRelatedObjectsGet**](DatasetsApi.md#datasetPkRelatedObjectsGet) | **GET** /dataset/{pk}/related_objects | 
[**datasetPost**](DatasetsApi.md#datasetPost) | **POST** /dataset/ | 
[**datasetRelatedColumnNameGet**](DatasetsApi.md#datasetRelatedColumnNameGet) | **GET** /dataset/related/{column_name} | 



## datasetDelete

> AnnotationLayerGet400Response datasetDelete(opts)



Deletes multiple Datasets in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.datasetDelete(opts, (error, data, response) => {
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


## datasetDistinctColumnNameGet

> DistincResponseSchema datasetDistinctColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.datasetDistinctColumnNameGet(columnName, opts, (error, data, response) => {
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


## datasetExportGet

> String datasetExportGet(opts)



Exports multiple datasets and downloads them as YAML files

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.datasetExportGet(opts, (error, data, response) => {
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

**String**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: text/plain, application/json


## datasetGet

> DatasetGet200Response datasetGet(opts)



Get a list of models

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.datasetGet(opts, (error, data, response) => {
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

[**DatasetGet200Response**](DatasetGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetImportPost

> AnnotationLayerGet400Response datasetImportPost(opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let opts = {
  'formData': "/path/to/file", // File | upload file (ZIP or YAML)
  'overwrite': true, // Boolean | overwrite existing datasets?
  'passwords': "passwords_example" // String | JSON map of passwords for each file
};
apiInstance.datasetImportPost(opts, (error, data, response) => {
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
 **formData** | **File**| upload file (ZIP or YAML) | [optional] 
 **overwrite** | **Boolean**| overwrite existing datasets? | [optional] 
 **passwords** | **String**| JSON map of passwords for each file | [optional] 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## datasetInfoGet

> AnnotationLayerInfoGet200Response datasetInfoGet(opts)



Get metadata information about this API resource

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.datasetInfoGet(opts, (error, data, response) => {
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


## datasetPkColumnColumnIdDelete

> AnnotationLayerGet400Response datasetPkColumnColumnIdDelete(pk, columnId)



Delete a Dataset column

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | The dataset pk for this column
let columnId = 56; // Number | The column id for this dataset
apiInstance.datasetPkColumnColumnIdDelete(pk, columnId, (error, data, response) => {
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
 **pk** | **Number**| The dataset pk for this column | 
 **columnId** | **Number**| The column id for this dataset | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetPkDelete

> AnnotationLayerGet400Response datasetPkDelete(pk)



Deletes a Dataset

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | 
apiInstance.datasetPkDelete(pk, (error, data, response) => {
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


## datasetPkGet

> DatasetPkGet200Response datasetPkGet(pk, opts)



Get an item model

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.datasetPkGet(pk, opts, (error, data, response) => {
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

[**DatasetPkGet200Response**](DatasetPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetPkMetricMetricIdDelete

> AnnotationLayerGet400Response datasetPkMetricMetricIdDelete(pk, metricId)



Delete a Dataset metric

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | The dataset pk for this column
let metricId = 56; // Number | The metric id for this dataset
apiInstance.datasetPkMetricMetricIdDelete(pk, metricId, (error, data, response) => {
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
 **pk** | **Number**| The dataset pk for this column | 
 **metricId** | **Number**| The metric id for this dataset | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetPkPut

> DatasetPkPut200Response datasetPkPut(pk, datasetRestApiPut, opts)



Changes a Dataset

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | 
let datasetRestApiPut = new Superset.DatasetRestApiPut(); // DatasetRestApiPut | Dataset schema
let opts = {
  'overrideColumns': true // Boolean | 
};
apiInstance.datasetPkPut(pk, datasetRestApiPut, opts, (error, data, response) => {
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
 **datasetRestApiPut** | [**DatasetRestApiPut**](DatasetRestApiPut.md)| Dataset schema | 
 **overrideColumns** | **Boolean**|  | [optional] 

### Return type

[**DatasetPkPut200Response**](DatasetPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## datasetPkRefreshPut

> AnnotationLayerGet400Response datasetPkRefreshPut(pk)



Refreshes and updates columns of a dataset

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | 
apiInstance.datasetPkRefreshPut(pk, (error, data, response) => {
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


## datasetPkRelatedObjectsGet

> DatasetRelatedObjectsResponse datasetPkRelatedObjectsGet(pk)



Get charts and dashboards count associated to a dataset

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let pk = 56; // Number | 
apiInstance.datasetPkRelatedObjectsGet(pk, (error, data, response) => {
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

[**DatasetRelatedObjectsResponse**](DatasetRelatedObjectsResponse.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## datasetPost

> DatasetPost201Response datasetPost(datasetRestApiPost)



Create a new Dataset

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let datasetRestApiPost = new Superset.DatasetRestApiPost(); // DatasetRestApiPost | Dataset schema
apiInstance.datasetPost(datasetRestApiPost, (error, data, response) => {
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
 **datasetRestApiPost** | [**DatasetRestApiPost**](DatasetRestApiPost.md)| Dataset schema | 

### Return type

[**DatasetPost201Response**](DatasetPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## datasetRelatedColumnNameGet

> RelatedResponseSchema datasetRelatedColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.DatasetsApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.datasetRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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

