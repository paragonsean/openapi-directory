# OnSchedConsumerApi.ServicesApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1ServicesAllocationsIdGet**](ServicesApi.md#consumerV1ServicesAllocationsIdGet) | **GET** /consumer/v1/services/allocations/{id} | Get Service Allocation
[**consumerV1ServicesGet**](ServicesApi.md#consumerV1ServicesGet) | **GET** /consumer/v1/services | List Services
[**consumerV1ServicesIdAllocationsGet**](ServicesApi.md#consumerV1ServicesIdAllocationsGet) | **GET** /consumer/v1/services/{id}/allocations | List Service Allocations
[**consumerV1ServicesIdGet**](ServicesApi.md#consumerV1ServicesIdGet) | **GET** /consumer/v1/services/{id} | Get Service
[**consumerV1ServicesIdResourcesGet**](ServicesApi.md#consumerV1ServicesIdResourcesGet) | **GET** /consumer/v1/services/{id}/resources | List Resources for Service



## consumerV1ServicesAllocationsIdGet

> ServiceAllocationViewModel consumerV1ServicesAllocationsIdGet(id)

Get Service Allocation

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Allocation&lt;/b&gt; object. A valid &lt;b&gt;serviceAllocation id&lt;/b&gt; is required. Find service allocation id&#39;s by using the &lt;i&gt;GET/consumer​/v1​/services​/{id}​/allocations&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServicesApi();
let id = "id_example"; // String | id of serviceAllocation object
apiInstance.consumerV1ServicesAllocationsIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of serviceAllocation object | 

### Return type

[**ServiceAllocationViewModel**](ServiceAllocationViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ServicesGet

> ServiceListViewModel consumerV1ServicesGet(opts)

List Services

&lt;p&gt;Use this endpoint to &lt;b&gt;List Services&lt;/b&gt; available at your business location and/or company. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServicesApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'serviceGroupId': 56, // Number | Filter by groupId
  'defaultService': true, // Boolean | Filter by default service, default is false
  'allLocations': true, // Boolean | Search All Locations, default is false
  'scope': new OnSchedConsumerApi.ServicesScope(), // ServicesScope | Filter by scope, Company, Location or All, default is All
  'name': "name_example", // String | Filter by Name, supports Partial name search
  'serviceId': "serviceId_example", // String | Filter by ServiceId, using this parameter would ignore all other parameters
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56, // Number | Page limit default 20, max 100
  'sortOrder': new OnSchedConsumerApi.ServiceSortOrder(), // ServiceSortOrder | Sort results using Natural Sort or Sorted alphabetically by Service Names, default is natural
  'sortDescending': true // Boolean | Sort results in Descending Order, default true
};
apiInstance.consumerV1ServicesGet(opts, (error, data, response) => {
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
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 
 **serviceGroupId** | **Number**| Filter by groupId | [optional] 
 **defaultService** | **Boolean**| Filter by default service, default is false | [optional] 
 **allLocations** | **Boolean**| Search All Locations, default is false | [optional] 
 **scope** | [**ServicesScope**](.md)| Filter by scope, Company, Location or All, default is All | [optional] 
 **name** | **String**| Filter by Name, supports Partial name search | [optional] 
 **serviceId** | **String**| Filter by ServiceId, using this parameter would ignore all other parameters | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 
 **sortOrder** | [**ServiceSortOrder**](.md)| Sort results using Natural Sort or Sorted alphabetically by Service Names, default is natural | [optional] 
 **sortDescending** | **Boolean**| Sort results in Descending Order, default true | [optional] 

### Return type

[**ServiceListViewModel**](ServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ServicesIdAllocationsGet

> ServiceAllocationListViewModel consumerV1ServicesIdAllocationsGet(id, opts)

List Service Allocations

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Service Allocations&lt;/b&gt; associated with the requested service. A valid &lt;b&gt;service id&lt;/b&gt; is required. Allocations are used for Event type services/bookings. Retrieve all allocations for a location by passing in zero as the service id. Otherwise, to get allocations for a specific service supply the service id. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further. For more information: &lt;a href&#x3D;\&quot;https://docs.onsched.com/reference/post_setup-v1-services-id-allocations\&quot;&gt;Create Service Allocations&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServicesApi();
let id = "id_example"; // String | id of service to list allocations for, 0 for all
let opts = {
  'locationId': "locationId_example", // String | id of the location, defaults to the primary location
  'resourceId': "resourceId_example", // String | id of the resource to filter on
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD: Filter allocations on/after startDate
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Format YYYY-MM-DD. Filter allocations on/before endDate
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1ServicesIdAllocationsGet(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service to list allocations for, 0 for all | 
 **locationId** | **String**| id of the location, defaults to the primary location | [optional] 
 **resourceId** | **String**| id of the resource to filter on | [optional] 
 **startDate** | **Date**| Format YYYY-MM-DD: Filter allocations on/after startDate | [optional] 
 **endDate** | **Date**| Format YYYY-MM-DD. Filter allocations on/before endDate | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ServiceAllocationListViewModel**](ServiceAllocationListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ServicesIdGet

> ServiceViewModel consumerV1ServicesIdGet(id)

Get Service

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service&lt;/b&gt; object. A valid &lt;b&gt;service id&lt;/b&gt; is required. Find service id&#39;s by using the &lt;i&gt;GET /consumer/v1/services&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServicesApi();
let id = 56; // Number | id of service object
apiInstance.consumerV1ServicesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| id of service object | 

### Return type

[**ServiceViewModel**](ServiceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ServicesIdResourcesGet

> ResourceListViewModel consumerV1ServicesIdResourcesGet(id, opts)

List Resources for Service

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resources that provide the Service requested&lt;/b&gt;. A valid &lt;b&gt;service id&lt;/b&gt; is required. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServicesApi();
let id = "id_example"; // String | id of service object
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1ServicesIdResourcesGet(id, opts, (error, data, response) => {
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
 **id** | **String**| id of service object | 
 **locationId** | **String**| id of business location, defaults to primary business location | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ResourceListViewModel**](ResourceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

