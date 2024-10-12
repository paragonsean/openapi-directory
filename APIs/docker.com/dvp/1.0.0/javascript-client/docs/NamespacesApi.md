# DvpDataApi.NamespacesApi

All URIs are relative to *https://hub.docker.com/api/publisher/analytics/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getNamespaceDataByTimespan**](NamespacesApi.md#getNamespaceDataByTimespan) | **GET** /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan}/{dataview} | Get namespace data for timespan
[**getNamespaceTimespanMetadata**](NamespacesApi.md#getNamespaceTimespanMetadata) | **GET** /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype}/{timespan} | Get namespace metadata for timespan
[**getNamespaceTimespans**](NamespacesApi.md#getNamespaceTimespans) | **GET** /namespaces/{namespace}/pulls/exports/years/{year}/{timespantype} | Get timespans with data
[**getNamespaceYears**](NamespacesApi.md#getNamespaceYears) | **GET** /namespaces/{namespace}/pulls/exports/years | Get years with data



## getNamespaceDataByTimespan

> ResponseData getNamespaceDataByTimespan(namespace, year, timespantype, timespan, dataview)

Get namespace data for timespan

Gets a list of URLs that can be used to download the pull data for the given namespace and timespan

### Example

```javascript
import DvpDataApi from 'dvp_data_api';
let defaultClient = DvpDataApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: HubAuth
let HubAuth = defaultClient.authentications['HubAuth'];
HubAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DvpDataApi.NamespacesApi();
let namespace = "namespace_example"; // String | Namespace to fetch data for
let year = 56; // Number | Year to fetch data for
let timespantype = new DvpDataApi.TimespanType(); // TimespanType | Type of timespan to fetch data for
let timespan = 56; // Number | Timespan to fetch data for
let dataview = new DvpDataApi.DataviewType(); // DataviewType | Type of data to fetch
apiInstance.getNamespaceDataByTimespan(namespace, year, timespantype, timespan, dataview, (error, data, response) => {
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
 **namespace** | **String**| Namespace to fetch data for | 
 **year** | **Number**| Year to fetch data for | 
 **timespantype** | [**TimespanType**](.md)| Type of timespan to fetch data for | 
 **timespan** | **Number**| Timespan to fetch data for | 
 **dataview** | [**DataviewType**](.md)| Type of data to fetch | 

### Return type

[**ResponseData**](ResponseData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNamespaceTimespanMetadata

> TimespanModel getNamespaceTimespanMetadata(namespace, year, timespantype, timespan)

Get namespace metadata for timespan

Gets info about data for the given namespace and timespan

### Example

```javascript
import DvpDataApi from 'dvp_data_api';
let defaultClient = DvpDataApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: HubAuth
let HubAuth = defaultClient.authentications['HubAuth'];
HubAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DvpDataApi.NamespacesApi();
let namespace = "namespace_example"; // String | Namespace to fetch data for
let year = 56; // Number | Year to fetch data for
let timespantype = new DvpDataApi.TimespanType(); // TimespanType | Type of timespan to fetch data for
let timespan = 56; // Number | Timespan to fetch data for
apiInstance.getNamespaceTimespanMetadata(namespace, year, timespantype, timespan, (error, data, response) => {
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
 **namespace** | **String**| Namespace to fetch data for | 
 **year** | **Number**| Year to fetch data for | 
 **timespantype** | [**TimespanType**](.md)| Type of timespan to fetch data for | 
 **timespan** | **Number**| Timespan to fetch data for | 

### Return type

[**TimespanModel**](TimespanModel.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNamespaceTimespans

> TimespanData getNamespaceTimespans(namespace, year, timespantype)

Get timespans with data

Gets a list of timespans of the given type that have data for the given namespace and year

### Example

```javascript
import DvpDataApi from 'dvp_data_api';
let defaultClient = DvpDataApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: HubAuth
let HubAuth = defaultClient.authentications['HubAuth'];
HubAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DvpDataApi.NamespacesApi();
let namespace = "namespace_example"; // String | Namespace to fetch data for
let year = 56; // Number | Year to fetch data for
let timespantype = new DvpDataApi.TimespanType(); // TimespanType | Type of timespan to fetch data for
apiInstance.getNamespaceTimespans(namespace, year, timespantype, (error, data, response) => {
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
 **namespace** | **String**| Namespace to fetch data for | 
 **year** | **Number**| Year to fetch data for | 
 **timespantype** | [**TimespanType**](.md)| Type of timespan to fetch data for | 

### Return type

[**TimespanData**](TimespanData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getNamespaceYears

> YearData getNamespaceYears(namespace)

Get years with data

Gets a list of years that have data for the given namespace

### Example

```javascript
import DvpDataApi from 'dvp_data_api';
let defaultClient = DvpDataApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: HubAuth
let HubAuth = defaultClient.authentications['HubAuth'];
HubAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new DvpDataApi.NamespacesApi();
let namespace = "namespace_example"; // String | Namespace to fetch data for
apiInstance.getNamespaceYears(namespace, (error, data, response) => {
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
 **namespace** | **String**| Namespace to fetch data for | 

### Return type

[**YearData**](YearData.md)

### Authorization

[HubAuth](../README.md#HubAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

