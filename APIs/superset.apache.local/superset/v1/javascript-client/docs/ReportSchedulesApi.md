# Superset.ReportSchedulesApi

All URIs are relative to *http://superset.apache.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportDelete**](ReportSchedulesApi.md#reportDelete) | **DELETE** /report/ | 
[**reportGet**](ReportSchedulesApi.md#reportGet) | **GET** /report/ | 
[**reportInfoGet**](ReportSchedulesApi.md#reportInfoGet) | **GET** /report/_info | 
[**reportPkDelete**](ReportSchedulesApi.md#reportPkDelete) | **DELETE** /report/{pk} | 
[**reportPkGet**](ReportSchedulesApi.md#reportPkGet) | **GET** /report/{pk} | 
[**reportPkLogGet**](ReportSchedulesApi.md#reportPkLogGet) | **GET** /report/{pk}/log/ | 
[**reportPkLogLogIdGet**](ReportSchedulesApi.md#reportPkLogLogIdGet) | **GET** /report/{pk}/log/{log_id} | 
[**reportPkPut**](ReportSchedulesApi.md#reportPkPut) | **PUT** /report/{pk} | 
[**reportPost**](ReportSchedulesApi.md#reportPost) | **POST** /report/ | 
[**reportRelatedColumnNameGet**](ReportSchedulesApi.md#reportRelatedColumnNameGet) | **GET** /report/related/{column_name} | 



## reportDelete

> AnnotationLayerGet400Response reportDelete(opts)



Deletes multiple report schedules in a bulk operation.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let opts = {
  'q': [null] // [Number] | 
};
apiInstance.reportDelete(opts, (error, data, response) => {
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


## reportGet

> ReportGet200Response reportGet(opts)



Get a list of report schedules, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.reportGet(opts, (error, data, response) => {
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

[**ReportGet200Response**](ReportGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportInfoGet

> AnnotationLayerInfoGet200Response reportInfoGet(opts)



Get metadata information about this API resource

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let opts = {
  'q': new Superset.GetInfoSchema() // GetInfoSchema | 
};
apiInstance.reportInfoGet(opts, (error, data, response) => {
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


## reportPkDelete

> AnnotationLayerGet400Response reportPkDelete(pk)



Delete a report schedule

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let pk = 56; // Number | The report schedule pk
apiInstance.reportPkDelete(pk, (error, data, response) => {
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
 **pk** | **Number**| The report schedule pk | 

### Return type

[**AnnotationLayerGet400Response**](AnnotationLayerGet400Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportPkGet

> ReportPkGet200Response reportPkGet(pk, opts)



Get a report schedule

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let pk = 56; // Number | 
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.reportPkGet(pk, opts, (error, data, response) => {
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

[**ReportPkGet200Response**](ReportPkGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportPkLogGet

> ReportPkLogGet200Response reportPkLogGet(pk, opts)



Get a list of report schedule logs, use Rison or JSON query parameters for filtering, sorting, pagination and for selecting specific columns and metadata.

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let pk = 56; // Number | The report schedule id for these logs
let opts = {
  'q': new Superset.GetListSchema() // GetListSchema | 
};
apiInstance.reportPkLogGet(pk, opts, (error, data, response) => {
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
 **pk** | **Number**| The report schedule id for these logs | 
 **q** | [**GetListSchema**](.md)|  | [optional] 

### Return type

[**ReportPkLogGet200Response**](ReportPkLogGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportPkLogLogIdGet

> ReportPkLogLogIdGet200Response reportPkLogLogIdGet(pk, logId, opts)



Get a report schedule log

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let pk = 56; // Number | The report schedule pk for log
let logId = 56; // Number | The log pk
let opts = {
  'q': new Superset.GetItemSchema() // GetItemSchema | 
};
apiInstance.reportPkLogLogIdGet(pk, logId, opts, (error, data, response) => {
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
 **pk** | **Number**| The report schedule pk for log | 
 **logId** | **Number**| The log pk | 
 **q** | [**GetItemSchema**](.md)|  | [optional] 

### Return type

[**ReportPkLogLogIdGet200Response**](ReportPkLogLogIdGet200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportPkPut

> ReportPkPut200Response reportPkPut(pk, reportScheduleRestApiPut)



Update a report schedule

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let pk = 56; // Number | The Report Schedule pk
let reportScheduleRestApiPut = new Superset.ReportScheduleRestApiPut(); // ReportScheduleRestApiPut | Report Schedule schema
apiInstance.reportPkPut(pk, reportScheduleRestApiPut, (error, data, response) => {
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
 **pk** | **Number**| The Report Schedule pk | 
 **reportScheduleRestApiPut** | [**ReportScheduleRestApiPut**](ReportScheduleRestApiPut.md)| Report Schedule schema | 

### Return type

[**ReportPkPut200Response**](ReportPkPut200Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportPost

> ReportPost201Response reportPost(reportScheduleRestApiPost)



Create a report schedule

### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let reportScheduleRestApiPost = new Superset.ReportScheduleRestApiPost(); // ReportScheduleRestApiPost | Report Schedule schema
apiInstance.reportPost(reportScheduleRestApiPost, (error, data, response) => {
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
 **reportScheduleRestApiPost** | [**ReportScheduleRestApiPost**](ReportScheduleRestApiPost.md)| Report Schedule schema | 

### Return type

[**ReportPost201Response**](ReportPost201Response.md)

### Authorization

[jwt](../README.md#jwt)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## reportRelatedColumnNameGet

> RelatedResponseSchema reportRelatedColumnNameGet(columnName, opts)



### Example

```javascript
import Superset from 'superset';
let defaultClient = Superset.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: jwt
let jwt = defaultClient.authentications['jwt'];
jwt.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new Superset.ReportSchedulesApi();
let columnName = "columnName_example"; // String | 
let opts = {
  'q': new Superset.GetRelatedSchema() // GetRelatedSchema | 
};
apiInstance.reportRelatedColumnNameGet(columnName, opts, (error, data, response) => {
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

