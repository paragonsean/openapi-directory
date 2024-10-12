# AdHybridHealthService.MetricsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**serviceGetMetrics**](MetricsApi.md#serviceGetMetrics) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metrics/{metricName}/groups/{groupName} | 
[**serviceMembersGetConnectorMetadata**](MetricsApi.md#serviceMembersGetConnectorMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/metrics/{metricName} | 
[**serviceMembersGetMetrics**](MetricsApi.md#serviceMembersGetMetrics) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/servicemembers/{serviceMemberId}/metrics/{metricName}/groups/{groupName} | 
[**servicesGetMetricMetadata**](MetricsApi.md#servicesGetMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metricmetadata/{metricName} | 
[**servicesGetMetricMetadataForGroup**](MetricsApi.md#servicesGetMetricMetadataForGroup) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metricmetadata/{metricName}/groups/{groupName} | 
[**servicesListMetricMetadata**](MetricsApi.md#servicesListMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metricmetadata | 
[**servicesListMetricsAverage**](MetricsApi.md#servicesListMetricsAverage) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metrics/{metricName}/groups/{groupName}/average | 
[**servicesListMetricsSum**](MetricsApi.md#servicesListMetricsSum) | **GET** /providers/Microsoft.ADHybridHealthService/services/{serviceName}/metrics/{metricName}/groups/{groupName}/sum | 



## serviceGetMetrics

> MetricSets serviceGetMetrics(serviceName, metricName, groupName, apiVersion, opts)



Gets the server related metrics for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'groupKey': "groupKey_example", // String | The group key
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date.
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | The end date.
};
apiInstance.serviceGetMetrics(serviceName, metricName, groupName, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **metricName** | **String**| The metric name | 
 **groupName** | **String**| The group name | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **groupKey** | **String**| The group key | [optional] 
 **fromDate** | **Date**| The start date. | [optional] 
 **toDate** | **Date**| The end date. | [optional] 

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersGetConnectorMetadata

> ConnectorMetadata serviceMembersGetConnectorMetadata(serviceName, serviceMemberId, metricName, apiVersion)



Gets the list of connectors and run profile names.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The service member id.
let metricName = "metricName_example"; // String | The name of the metric.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.serviceMembersGetConnectorMetadata(serviceName, serviceMemberId, metricName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **serviceMemberId** | **String**| The service member id. | 
 **metricName** | **String**| The name of the metric. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ConnectorMetadata**](ConnectorMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## serviceMembersGetMetrics

> MetricSets serviceMembersGetMetrics(serviceName, metricName, groupName, serviceMemberId, apiVersion, opts)



Gets the server related metrics for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let serviceMemberId = "serviceMemberId_example"; // String | The server id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'groupKey': "groupKey_example", // String | The group key
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date.
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | The end date.
};
apiInstance.serviceMembersGetMetrics(serviceName, metricName, groupName, serviceMemberId, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **metricName** | **String**| The metric name | 
 **groupName** | **String**| The group name | 
 **serviceMemberId** | **String**| The server id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **groupKey** | **String**| The group key | [optional] 
 **fromDate** | **Date**| The start date. | [optional] 
 **toDate** | **Date**| The end date. | [optional] 

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGetMetricMetadata

> MetricMetadata servicesGetMetricMetadata(serviceName, metricName, apiVersion)



Gets the service related metrics information.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesGetMetricMetadata(serviceName, metricName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **metricName** | **String**| The metric name | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**MetricMetadata**](MetricMetadata.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesGetMetricMetadataForGroup

> MetricSets servicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, opts)



Gets the service related metrics for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'groupKey': "groupKey_example", // String | The group key
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date.
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | The end date.
};
apiInstance.servicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **metricName** | **String**| The metric name | 
 **groupName** | **String**| The group name | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **groupKey** | **String**| The group key | [optional] 
 **fromDate** | **Date**| The start date. | [optional] 
 **toDate** | **Date**| The end date. | [optional] 

### Return type

[**MetricSets**](MetricSets.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListMetricMetadata

> MetricMetadataList servicesListMetricMetadata(serviceName, apiVersion, opts)



Gets the service related metrics information.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The metric metadata property filter to apply.
  'perfCounter': true // Boolean | Indicates if only performance counter metrics are requested.
};
apiInstance.servicesListMetricMetadata(serviceName, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The metric metadata property filter to apply. | [optional] 
 **perfCounter** | **Boolean**| Indicates if only performance counter metrics are requested. | [optional] 

### Return type

[**MetricMetadataList**](MetricMetadataList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListMetricsAverage

> Metrics servicesListMetricsAverage(serviceName, metricName, groupName, apiVersion)



Gets the average of the metric values for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListMetricsAverage(serviceName, metricName, groupName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **metricName** | **String**| The metric name | 
 **groupName** | **String**| The group name | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Metrics**](Metrics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## servicesListMetricsSum

> Metrics servicesListMetricsSum(serviceName, metricName, groupName, apiVersion)



Gets the sum of the metric values for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.MetricsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.servicesListMetricsSum(serviceName, metricName, groupName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **metricName** | **String**| The metric name | 
 **groupName** | **String**| The group name | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Metrics**](Metrics.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

