# NetworkExperiments.ReportsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportsGetLatencyScorecards**](ReportsApi.md#reportsGetLatencyScorecards) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}/LatencyScorecard | Gets a Latency Scorecard for a given Experiment
[**reportsGetTimeseries**](ReportsApi.md#reportsGetTimeseries) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/NetworkExperimentProfiles/{profileName}/Experiments/{experimentName}/Timeseries | Gets a Timeseries for a given Experiment



## reportsGetLatencyScorecards

> LatencyScorecard reportsGetLatencyScorecards(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, aggregationInterval, opts)

Gets a Latency Scorecard for a given Experiment

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ReportsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
let aggregationInterval = "aggregationInterval_example"; // String | The aggregation interval of the Latency Scorecard
let opts = {
  'endDateTimeUTC': "endDateTimeUTC_example", // String | The end DateTime of the Latency Scorecard in UTC
  'country': "country_example" // String | The country associated with the Latency Scorecard. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html
};
apiInstance.reportsGetLatencyScorecards(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, aggregationInterval, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 
 **experimentName** | **String**| The Experiment identifier associated with the Experiment | 
 **aggregationInterval** | **String**| The aggregation interval of the Latency Scorecard | 
 **endDateTimeUTC** | **String**| The end DateTime of the Latency Scorecard in UTC | [optional] 
 **country** | **String**| The country associated with the Latency Scorecard. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html | [optional] 

### Return type

[**LatencyScorecard**](LatencyScorecard.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportsGetTimeseries

> Timeseries reportsGetTimeseries(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, startDateTimeUTC, endDateTimeUTC, aggregationInterval, timeseriesType, opts)

Gets a Timeseries for a given Experiment

### Example

```javascript
import NetworkExperiments from 'network_experiments';
let defaultClient = NetworkExperiments.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetworkExperiments.ReportsApi();
let subscriptionId = "subscriptionId_example"; // String | The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
let apiVersion = "apiVersion_example"; // String | Client API version.
let resourceGroupName = "resourceGroupName_example"; // String | Name of the Resource group within the Azure subscription.
let profileName = "profileName_example"; // String | The Profile identifier associated with the Tenant and Partner
let experimentName = "experimentName_example"; // String | The Experiment identifier associated with the Experiment
let startDateTimeUTC = new Date("2013-10-20T19:20:30+01:00"); // Date | The start DateTime of the Timeseries in UTC
let endDateTimeUTC = new Date("2013-10-20T19:20:30+01:00"); // Date | The end DateTime of the Timeseries in UTC
let aggregationInterval = "aggregationInterval_example"; // String | The aggregation interval of the Timeseries
let timeseriesType = "timeseriesType_example"; // String | The type of Timeseries
let opts = {
  'endpoint': "endpoint_example", // String | The specific endpoint
  'country': "country_example" // String | The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html
};
apiInstance.reportsGetTimeseries(subscriptionId, apiVersion, resourceGroupName, profileName, experimentName, startDateTimeUTC, endDateTimeUTC, aggregationInterval, timeseriesType, opts, (error, data, response) => {
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
 **subscriptionId** | **String**| The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call. | 
 **apiVersion** | **String**| Client API version. | 
 **resourceGroupName** | **String**| Name of the Resource group within the Azure subscription. | 
 **profileName** | **String**| The Profile identifier associated with the Tenant and Partner | 
 **experimentName** | **String**| The Experiment identifier associated with the Experiment | 
 **startDateTimeUTC** | **Date**| The start DateTime of the Timeseries in UTC | 
 **endDateTimeUTC** | **Date**| The end DateTime of the Timeseries in UTC | 
 **aggregationInterval** | **String**| The aggregation interval of the Timeseries | 
 **timeseriesType** | **String**| The type of Timeseries | 
 **endpoint** | **String**| The specific endpoint | [optional] 
 **country** | **String**| The country associated with the Timeseries. Values are country ISO codes as specified here- https://www.iso.org/iso-3166-country-codes.html | [optional] 

### Return type

[**Timeseries**](Timeseries.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

