# AdHybridHealthService.AddsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adDomainServiceMembersList**](AddsApi.md#adDomainServiceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/addomainservicemembers | 
[**addsServiceGetMetrics**](AddsApi.md#addsServiceGetMetrics) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metrics/{metricName}/groups/{groupName} | 
[**addsServiceMembersDelete**](AddsApi.md#addsServiceMembersDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId} | 
[**addsServiceMembersGet**](AddsApi.md#addsServiceMembersGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId} | 
[**addsServiceMembersList**](AddsApi.md#addsServiceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/addsservicemembers | 
[**addsServiceMembersListCredentials**](AddsApi.md#addsServiceMembersListCredentials) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId}/credentials | 
[**addsServicesAdd**](AddsApi.md#addsServicesAdd) | **POST** /providers/Microsoft.ADHybridHealthService/addsservices | 
[**addsServicesGetForestSummary**](AddsApi.md#addsServicesGetForestSummary) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/forestsummary | 
[**addsServicesGetMetricMetadata**](AddsApi.md#addsServicesGetMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metricmetadata/{metricName} | 
[**addsServicesGetMetricMetadataForGroup**](AddsApi.md#addsServicesGetMetricMetadataForGroup) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metricmetadata/{metricName}/groups/{groupName} | 
[**addsServicesList**](AddsApi.md#addsServicesList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices | 
[**addsServicesListMetricMetadata**](AddsApi.md#addsServicesListMetricMetadata) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metricmetadata | 
[**addsServicesListMetricsAverage**](AddsApi.md#addsServicesListMetricsAverage) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metrics/{metricName}/groups/{groupName}/average | 
[**addsServicesListMetricsSum**](AddsApi.md#addsServicesListMetricsSum) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/metrics/{metricName}/groups/{groupName}/sum | 
[**addsServicesListReplicationDetails**](AddsApi.md#addsServicesListReplicationDetails) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/replicationdetails | 
[**addsServicesListReplicationSummary**](AddsApi.md#addsServicesListReplicationSummary) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/replicationsummary | 
[**addsServicesListServerAlerts**](AddsApi.md#addsServicesListServerAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers/{serviceMemberId}/alerts | 
[**addsServicesReplicationStatusGet**](AddsApi.md#addsServicesReplicationStatusGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/replicationstatus | 
[**addsServicesServiceMembersAdd**](AddsApi.md#addsServicesServiceMembersAdd) | **POST** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers | 
[**addsServicesServiceMembersList**](AddsApi.md#addsServicesServiceMembersList) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/servicemembers | 
[**addsServicesUserPreferenceAdd**](AddsApi.md#addsServicesUserPreferenceAdd) | **POST** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/features/{featureName}/userpreference | 
[**addsServicesUserPreferenceDelete**](AddsApi.md#addsServicesUserPreferenceDelete) | **DELETE** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/features/{featureName}/userpreference | 
[**addsServicesUserPreferenceGet**](AddsApi.md#addsServicesUserPreferenceGet) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/features/{featureName}/userpreference | 
[**alertsListAddsAlerts**](AddsApi.md#alertsListAddsAlerts) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/alerts | 
[**configurationListAddsConfigurations**](AddsApi.md#configurationListAddsConfigurations) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/configuration | 
[**dimensionsListAddsDimensions**](AddsApi.md#dimensionsListAddsDimensions) | **GET** /providers/Microsoft.ADHybridHealthService/addsservices/{serviceName}/dimensions/{dimension} | 



## adDomainServiceMembersList

> AddsServiceMembers adDomainServiceMembersList(serviceName, isGroupbySite, nextPartitionKey, nextRowKey, apiVersion, opts)



Gets the details of the servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let isGroupbySite = true; // Boolean | Indicates if the result should be grouped by site or not.
let nextPartitionKey = "nextPartitionKey_example"; // String | The next partition key to query for.
let nextRowKey = "nextRowKey_example"; // String | The next row key to query for.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The server property filter to apply.
  'query': "query_example", // String | The custom query.
  'takeCount': 56 // Number | The take count , which specifies the number of elements that can be returned from a sequence.
};
apiInstance.adDomainServiceMembersList(serviceName, isGroupbySite, nextPartitionKey, nextRowKey, apiVersion, opts, (error, data, response) => {
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
 **isGroupbySite** | **Boolean**| Indicates if the result should be grouped by site or not. | 
 **nextPartitionKey** | **String**| The next partition key to query for. | 
 **nextRowKey** | **String**| The next row key to query for. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The server property filter to apply. | [optional] 
 **query** | **String**| The custom query. | [optional] 
 **takeCount** | **Number**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] 

### Return type

[**AddsServiceMembers**](AddsServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServiceGetMetrics

> MetricSets addsServiceGetMetrics(serviceName, metricName, groupName, apiVersion, opts)



Gets the server related metrics for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'groupKey': "groupKey_example", // String | The group key
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date.
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | The end date.
};
apiInstance.addsServiceGetMetrics(serviceName, metricName, groupName, apiVersion, opts, (error, data, response) => {
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


## addsServiceMembersDelete

> addsServiceMembersDelete(serviceName, serviceMemberId, apiVersion, opts)



Deletes a Active Directory Domain Controller server that has been onboarded to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'confirm': true // Boolean | Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered.
};
apiInstance.addsServiceMembersDelete(serviceName, serviceMemberId, apiVersion, opts, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **confirm** | **Boolean**| Indicates if the server will be permanently deleted or disabled. True indicates that the server will be permanently deleted and False indicates that the server will be marked disabled and then deleted after 30 days, if it is not re-registered. | [optional] 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addsServiceMembersGet

> ServiceMember addsServiceMembersGet(serviceName, serviceMemberId, apiVersion)



Gets the details of a server, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServiceMembersGet(serviceName, serviceMemberId, apiVersion, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**ServiceMember**](ServiceMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServiceMembersList

> AddsServiceMembers addsServiceMembersList(serviceName, apiVersion, opts)



Gets the details of the Active Directory Domain servers, for a given Active Directory Domain Service, that are onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example" // String | The server property filter to apply.
};
apiInstance.addsServiceMembersList(serviceName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The server property filter to apply. | [optional] 

### Return type

[**AddsServiceMembers**](AddsServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServiceMembersListCredentials

> Credentials addsServiceMembersListCredentials(serviceName, serviceMemberId, apiVersion, opts)



Gets the credentials of the server which is needed by the agent to connect to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let serviceMemberId = "serviceMemberId_example"; // String | The server Id.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example" // String | The property filter to apply.
};
apiInstance.addsServiceMembersListCredentials(serviceName, serviceMemberId, apiVersion, opts, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The property filter to apply. | [optional] 

### Return type

[**Credentials**](Credentials.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesAdd

> ServiceProperties addsServicesAdd(apiVersion, service)



Onboards a service for a given tenant in Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let service = new AdHybridHealthService.ServiceProperties(); // ServiceProperties | The service object.
apiInstance.addsServicesAdd(apiVersion, service, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **service** | [**ServiceProperties**](ServiceProperties.md)| The service object. | 

### Return type

[**ServiceProperties**](ServiceProperties.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addsServicesGetForestSummary

> ForestSummary addsServicesGetForestSummary(serviceName, apiVersion)



Gets the forest summary for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesGetForestSummary(serviceName, apiVersion, (error, data, response) => {
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

### Return type

[**ForestSummary**](ForestSummary.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesGetMetricMetadata

> MetricMetadata addsServicesGetMetricMetadata(serviceName, metricName, apiVersion)



Gets the service related metric information.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesGetMetricMetadata(serviceName, metricName, apiVersion, (error, data, response) => {
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


## addsServicesGetMetricMetadataForGroup

> MetricSets addsServicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, opts)



Gets the service related metrics for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'groupKey': "groupKey_example", // String | The group key
  'fromDate': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date.
  'toDate': new Date("2013-10-20T19:20:30+01:00") // Date | The end date.
};
apiInstance.addsServicesGetMetricMetadataForGroup(serviceName, metricName, groupName, apiVersion, opts, (error, data, response) => {
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


## addsServicesList

> Services addsServicesList(apiVersion, opts)



Gets the details of Active Directory Domain Service, for a tenant, that are onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The service property filter to apply.
  'serviceType': "serviceType_example", // String | The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService.
  'skipCount': 56, // Number | The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements.
  'takeCount': 56 // Number | The take count , which specifies the number of elements that can be returned from a sequence.
};
apiInstance.addsServicesList(apiVersion, opts, (error, data, response) => {
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
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The service property filter to apply. | [optional] 
 **serviceType** | **String**| The service type for the services onboarded to Azure Active Directory Connect Health. Depending on whether the service is monitoring, ADFS, Sync or ADDS roles, the service type can either be AdFederationService or AadSyncService or AdDomainService. | [optional] 
 **skipCount** | **Number**| The skip count, which specifies the number of elements that can be bypassed from a sequence and then return the remaining elements. | [optional] 
 **takeCount** | **Number**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] 

### Return type

[**Services**](Services.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesListMetricMetadata

> MetricMetadataList addsServicesListMetricMetadata(serviceName, apiVersion, opts)



Gets the service related metrics information.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The metric metadata property filter to apply.
  'perfCounter': true // Boolean | Indicates if only performance counter metrics are requested.
};
apiInstance.addsServicesListMetricMetadata(serviceName, apiVersion, opts, (error, data, response) => {
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


## addsServicesListMetricsAverage

> Metrics addsServicesListMetricsAverage(serviceName, metricName, groupName, apiVersion)



Gets the average of the metric values for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesListMetricsAverage(serviceName, metricName, groupName, apiVersion, (error, data, response) => {
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


## addsServicesListMetricsSum

> Metrics addsServicesListMetricsSum(serviceName, metricName, groupName, apiVersion)



Gets the sum of the metric values for a given metric and group combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let metricName = "metricName_example"; // String | The metric name
let groupName = "groupName_example"; // String | The group name
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesListMetricsSum(serviceName, metricName, groupName, apiVersion, (error, data, response) => {
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


## addsServicesListReplicationDetails

> ReplicationDetailsList addsServicesListReplicationDetails(serviceName, apiVersion, opts)



Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The server property filter to apply.
  'withDetails': true // Boolean | Indicates if InboundReplicationNeighbor details are required or not.
};
apiInstance.addsServicesListReplicationDetails(serviceName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The server property filter to apply. | [optional] 
 **withDetails** | **Boolean**| Indicates if InboundReplicationNeighbor details are required or not. | [optional] 

### Return type

[**ReplicationDetailsList**](ReplicationDetailsList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesListReplicationSummary

> ReplicationSummaryList addsServicesListReplicationSummary(serviceName, isGroupbySite, query, nextPartitionKey, nextRowKey, apiVersion, opts)



Gets complete domain controller list along with replication details for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let isGroupbySite = true; // Boolean | Indicates if the result should be grouped by site or not.
let query = "query_example"; // String | The custom query.
let nextPartitionKey = "nextPartitionKey_example"; // String | The next partition key to query for.
let nextRowKey = "nextRowKey_example"; // String | The next row key to query for.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The server property filter to apply.
  'takeCount': 56 // Number | The take count , which specifies the number of elements that can be returned from a sequence.
};
apiInstance.addsServicesListReplicationSummary(serviceName, isGroupbySite, query, nextPartitionKey, nextRowKey, apiVersion, opts, (error, data, response) => {
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
 **isGroupbySite** | **Boolean**| Indicates if the result should be grouped by site or not. | 
 **query** | **String**| The custom query. | 
 **nextPartitionKey** | **String**| The next partition key to query for. | 
 **nextRowKey** | **String**| The next row key to query for. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The server property filter to apply. | [optional] 
 **takeCount** | **Number**| The take count , which specifies the number of elements that can be returned from a sequence. | [optional] 

### Return type

[**ReplicationSummaryList**](ReplicationSummaryList.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesListServerAlerts

> Alerts addsServicesListServerAlerts(serviceMemberId, serviceName, apiVersion, opts)



Gets the details of an alert for a given Active Directory Domain Controller service and server combination.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceMemberId = "serviceMemberId_example"; // String | The server Id for which the alert details needs to be queried.
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The alert property filter to apply.
  'state': "state_example", // String | The alert state to query for.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date to query for.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end date till when to query for.
};
apiInstance.addsServicesListServerAlerts(serviceMemberId, serviceName, apiVersion, opts, (error, data, response) => {
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
 **serviceMemberId** | **String**| The server Id for which the alert details needs to be queried. | 
 **serviceName** | **String**| The name of the service. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **filter** | **String**| The alert property filter to apply. | [optional] 
 **state** | **String**| The alert state to query for. | [optional] 
 **from** | **Date**| The start date to query for. | [optional] 
 **to** | **Date**| The end date till when to query for. | [optional] 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesReplicationStatusGet

> ReplicationStatus addsServicesReplicationStatusGet(serviceName, apiVersion)



Gets Replication status for a given Active Directory Domain Service, that is onboarded to Azure Active Directory Connect Health.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesReplicationStatusGet(serviceName, apiVersion, (error, data, response) => {
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

### Return type

[**ReplicationStatus**](ReplicationStatus.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesServiceMembersAdd

> ServiceMember addsServicesServiceMembersAdd(serviceName, apiVersion, serviceMember)



Onboards  a server, for a given Active Directory Domain Controller service, to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service under which the server is to be onboarded.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let serviceMember = new AdHybridHealthService.ServiceMember(); // ServiceMember | The server object.
apiInstance.addsServicesServiceMembersAdd(serviceName, apiVersion, serviceMember, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service under which the server is to be onboarded. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **serviceMember** | [**ServiceMember**](ServiceMember.md)| The server object. | 

### Return type

[**ServiceMember**](ServiceMember.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## addsServicesServiceMembersList

> ServiceMembers addsServicesServiceMembersList(serviceName, apiVersion, opts)



Gets the details of the servers, for a given Active Directory Domain Controller service, that are onboarded to Azure Active Directory Connect Health Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The server property filter to apply.
  'dimensionType': "dimensionType_example", // String | The server specific dimension.
  'dimensionSignature': "dimensionSignature_example" // String | The value of the dimension.
};
apiInstance.addsServicesServiceMembersList(serviceName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The server property filter to apply. | [optional] 
 **dimensionType** | **String**| The server specific dimension. | [optional] 
 **dimensionSignature** | **String**| The value of the dimension. | [optional] 

### Return type

[**ServiceMembers**](ServiceMembers.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## addsServicesUserPreferenceAdd

> addsServicesUserPreferenceAdd(serviceName, featureName, apiVersion, setting)



Adds the user preferences for a given feature.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let featureName = "featureName_example"; // String | The name of the feature.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let setting = new AdHybridHealthService.UserPreference(); // UserPreference | The user preference setting.
apiInstance.addsServicesUserPreferenceAdd(serviceName, featureName, apiVersion, setting, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **featureName** | **String**| The name of the feature. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 
 **setting** | [**UserPreference**](UserPreference.md)| The user preference setting. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## addsServicesUserPreferenceDelete

> addsServicesUserPreferenceDelete(serviceName, featureName, apiVersion)



Deletes the user preferences for a given feature.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let featureName = "featureName_example"; // String | The name of the feature.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesUserPreferenceDelete(serviceName, featureName, apiVersion, (error, data, response) => {
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
 **serviceName** | **String**| The name of the service. | 
 **featureName** | **String**| The name of the feature. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

null (empty response body)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## addsServicesUserPreferenceGet

> UserPreference addsServicesUserPreferenceGet(serviceName, featureName, apiVersion)



Gets the user preferences for a given feature.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let featureName = "featureName_example"; // String | The name of the feature.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.addsServicesUserPreferenceGet(serviceName, featureName, apiVersion, (error, data, response) => {
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
 **featureName** | **String**| The name of the feature. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**UserPreference**](UserPreference.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## alertsListAddsAlerts

> Alerts alertsListAddsAlerts(serviceName, apiVersion, opts)



Gets the alerts for a given Active Directory Domain Service.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
let opts = {
  'filter': "filter_example", // String | The alert property filter to apply.
  'state': "state_example", // String | The alert state to query for.
  'from': new Date("2013-10-20T19:20:30+01:00"), // Date | The start date to query for.
  'to': new Date("2013-10-20T19:20:30+01:00") // Date | The end date till when to query for.
};
apiInstance.alertsListAddsAlerts(serviceName, apiVersion, opts, (error, data, response) => {
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
 **filter** | **String**| The alert property filter to apply. | [optional] 
 **state** | **String**| The alert state to query for. | [optional] 
 **from** | **Date**| The start date to query for. | [optional] 
 **to** | **Date**| The end date till when to query for. | [optional] 

### Return type

[**Alerts**](Alerts.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## configurationListAddsConfigurations

> AddsConfiguration configurationListAddsConfigurations(serviceName, opts)



Gets the service configurations.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let opts = {
  'grouping': "grouping_example" // String | The grouping for configurations.
};
apiInstance.configurationListAddsConfigurations(serviceName, opts, (error, data, response) => {
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
 **grouping** | **String**| The grouping for configurations. | [optional] 

### Return type

[**AddsConfiguration**](AddsConfiguration.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dimensionsListAddsDimensions

> Dimensions dimensionsListAddsDimensions(serviceName, dimension, apiVersion)



Gets the dimensions for a given dimension type in a server.

### Example

```javascript
import AdHybridHealthService from 'ad_hybrid_health_service';
let defaultClient = AdHybridHealthService.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new AdHybridHealthService.AddsApi();
let serviceName = "serviceName_example"; // String | The name of the service.
let dimension = "dimension_example"; // String | The dimension type.
let apiVersion = "apiVersion_example"; // String | The version of the API to be used with the client request.
apiInstance.dimensionsListAddsDimensions(serviceName, dimension, apiVersion, (error, data, response) => {
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
 **dimension** | **String**| The dimension type. | 
 **apiVersion** | **String**| The version of the API to be used with the client request. | 

### Return type

[**Dimensions**](Dimensions.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

