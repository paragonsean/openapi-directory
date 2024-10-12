# Superset.ChartsApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chartDataCacheKeyGet**](ChartsApi.md#chartDataCacheKeyGet) | **GET** /chart/data/{cache_key} | 
[**chartDataPost**](ChartsApi.md#chartDataPost) | **POST** /chart/data | 
[**chartDelete**](ChartsApi.md#chartDelete) | **DELETE** /chart/ | 
[**chartExportGet**](ChartsApi.md#chartExportGet) | **GET** /chart/export/ | 
[**chartFavoriteStatusGet**](ChartsApi.md#chartFavoriteStatusGet) | **GET** /chart/favorite_status/ | 
[**chartGet**](ChartsApi.md#chartGet) | **GET** /chart/ | 
[**chartImportPost**](ChartsApi.md#chartImportPost) | **POST** /chart/import/ | 
[**chartInfoGet**](ChartsApi.md#chartInfoGet) | **GET** /chart/_info | 
[**chartPkCacheScreenshotGet**](ChartsApi.md#chartPkCacheScreenshotGet) | **GET** /chart/{pk}/cache_screenshot/ | 
[**chartPkDataGet**](ChartsApi.md#chartPkDataGet) | **GET** /chart/{pk}/data/ | 
[**chartPkDelete**](ChartsApi.md#chartPkDelete) | **DELETE** /chart/{pk} | 
[**chartPkGet**](ChartsApi.md#chartPkGet) | **GET** /chart/{pk} | 
[**chartPkPut**](ChartsApi.md#chartPkPut) | **PUT** /chart/{pk} | 
[**chartPkScreenshotDigestGet**](ChartsApi.md#chartPkScreenshotDigestGet) | **GET** /chart/{pk}/screenshot/{digest}/ | 
[**chartPkThumbnailDigestGet**](ChartsApi.md#chartPkThumbnailDigestGet) | **GET** /chart/{pk}/thumbnail/{digest}/ | 
[**chartPost**](ChartsApi.md#chartPost) | **POST** /chart/ | 
[**chartRelatedColumnNameGet**](ChartsApi.md#chartRelatedColumnNameGet) | **GET** /chart/related/{column_name} | 



## chartDataCacheKeyGet

> ChartDataResponseSchema chartDataCacheKeyGet(cacheKey)



Takes a query context cache key and returns payload data response for the given query.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let cacheKey = "cacheKey_example"; // String | 
apiInstance.chartDataCacheKeyGet(cacheKey, (error, data, response) => {
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
 **cacheKey** | **String**|  | 

### Return type

[**ChartDataResponseSchema**](ChartDataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartDataPost

> ChartDataResponseSchema chartDataPost(chartDataQueryContextSchema)



Takes a query context constructed in the client and returns payload data response for the given query.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let chartDataQueryContextSchema = new Superset.ChartDataQueryContextSchema(); // ChartDataQueryContextSchema | A query context consists of a datasource from which to fetch data and one or many query objects.
apiInstance.chartDataPost(chartDataQueryContextSchema, (error, data, response) => {
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
 **chartDataQueryContextSchema** | [**ChartDataQueryContextSchema**](ChartDataQueryContextSchema.md)| A query context consists of a datasource from which to fetch data and one or many query objects. | 

### Return type

[**ChartDataResponseSchema**](ChartDataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chartDelete

> AnnotationLayerGet400Response chartDelete(opts)



Deletes multiple Charts in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.chartDelete(opts, (error, data, response) => {
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


## chartExportGet

> File chartExportGet(opts)



Exports multiple charts and downloads them as YAML files

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.chartExportGet(opts, (error, data, response) => {
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


## chartFavoriteStatusGet

> GetFavStarIdsSchema chartFavoriteStatusGet(opts)



Check favorited dashboards for current user

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.chartFavoriteStatusGet(opts, (error, data, response) => {
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

[**GetFavStarIdsSchema**](GetFavStarIdsSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartGet

> ChartGet200Response chartGet(opts)



Get a list of charts, use Rison or JSON query parameters for filtering, sorting, pagination and  for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.chartGet(opts, (error, data, response) => {
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

[**ChartGet200Response**](ChartGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartImportPost

> AnnotationLayerGet400Response chartImportPost(opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let opts = {
  'formData': "/path/to/file", // File | upload file (ZIP)
  'overwrite': true, // Boolean | overwrite existing databases?
  'passwords': "passwords_example" // String | JSON map of passwords for each file
};
apiInstance.chartImportPost(opts, (error, data, response) => {
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


## chartInfoGet

> AnnotationLayerInfoGet200Response chartInfoGet(opts)



Several metadata information about chart API endpoints.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.chartInfoGet(opts, (error, data, response) => {
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


## chartPkCacheScreenshotGet

> ChartCacheScreenshotResponseSchema chartPkCacheScreenshotGet(pk, opts)



Compute and cache a screenshot.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.ScreenshotQuerySchema() // ScreenshotQuerySchema | 
};
apiInstance.chartPkCacheScreenshotGet(pk, opts, (error, data, response) => {
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
 **q** | [**ScreenshotQuerySchema**](.md)|  | [optional] 

### Return type

[**ChartCacheScreenshotResponseSchema**](ChartCacheScreenshotResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartPkDataGet

> ChartDataResponseSchema chartPkDataGet(pk, opts)



Takes a chart ID and uses the query context stored when the chart was saved to return payload data response.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | The chart ID
let opts = {
  'format': "format_example", // String | The format in which the data should be returned
  'type': "type_example" // String | The type in which the data should be returned
};
apiInstance.chartPkDataGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**| The chart ID | 
 **format** | **String**| The format in which the data should be returned | [optional] 
 **type** | **String**| The type in which the data should be returned | [optional] 

### Return type

[**ChartDataResponseSchema**](ChartDataResponseSchema.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartPkDelete

> AnnotationLayerGet400Response chartPkDelete(pk)



Deletes a Chart.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | 
apiInstance.chartPkDelete(pk, (error, data, response) => {
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


## chartPkGet

> ChartPkGet200Response chartPkGet(pk, opts)



Get a chart detail information.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.chartPkGet(pk, opts, (error, data, response) => {
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

[**ChartPkGet200Response**](ChartPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## chartPkPut

> ChartPkPut200Response chartPkPut(pk, chartRestApiPut)



Changes a Chart.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | 
let chartRestApiPut = new Superset.ChartRestApiPut(); // ChartRestApiPut | Chart schema
apiInstance.chartPkPut(pk, chartRestApiPut, (error, data, response) => {
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
 **chartRestApiPut** | [**ChartRestApiPut**](ChartRestApiPut.md)| Chart schema | 

### Return type

[**ChartPkPut200Response**](ChartPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chartPkScreenshotDigestGet

> File chartPkScreenshotDigestGet(pk, digest)



Get a computed screenshot from cache.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | 
let digest = "digest_example"; // String | 
apiInstance.chartPkScreenshotDigestGet(pk, digest, (error, data, response) => {
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
 **digest** | **String**|  | 

### Return type

**File**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json


## chartPkThumbnailDigestGet

> File chartPkThumbnailDigestGet(pk, digest)



Compute or get already computed chart thumbnail from cache.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let pk = 56; // Number | 
let digest = "digest_example"; // String | 
apiInstance.chartPkThumbnailDigestGet(pk, digest, (error, data, response) => {
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
 **digest** | **String**|  | 

### Return type

**File**

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: image/*, application/json


## chartPost

> ChartPost201Response chartPost(chartRestApiPost)



Create a new Chart.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let chartRestApiPost = new Superset.ChartRestApiPost(); // ChartRestApiPost | Chart schema
apiInstance.chartPost(chartRestApiPost, (error, data, response) => {
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
 **chartRestApiPost** | [**ChartRestApiPost**](ChartRestApiPost.md)| Chart schema | 

### Return type

[**ChartPost201Response**](ChartPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## chartRelatedColumnNameGet

> RelatedResponseSchema chartRelatedColumnNameGet(columnName, opts)



Get a list of all possible owners for a chart. Use &#x60;owners&#x60; has the &#x60;column_name&#x60; parameter

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ChartsApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.chartRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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

