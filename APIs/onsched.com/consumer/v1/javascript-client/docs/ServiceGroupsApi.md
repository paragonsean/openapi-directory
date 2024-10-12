# OnSchedConsumerApi.ServiceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1ServicegroupsGet**](ServiceGroupsApi.md#consumerV1ServicegroupsGet) | **GET** /consumer/v1/servicegroups | List Service Groups
[**consumerV1ServicegroupsIdGet**](ServiceGroupsApi.md#consumerV1ServicegroupsIdGet) | **GET** /consumer/v1/servicegroups/{id} | Get Service Group



## consumerV1ServicegroupsGet

> ServiceGroupListViewModel consumerV1ServicegroupsGet(opts)

List Service Groups

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Service Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, maximum is 100. Use the other query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServiceGroupsApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1ServicegroupsGet(opts, (error, data, response) => {
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
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ServiceGroupListViewModel**](ServiceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ServicegroupsIdGet

> ServiceGroupViewModel consumerV1ServicegroupsIdGet(id)

Get Service Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Service Group&lt;/b&gt; object. A valid &lt;b&gt;serviceGroup id&lt;/b&gt; is required. Find serviceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/serviceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ServiceGroupsApi();
let id = 56; // Number | id of the serviceGroup object
apiInstance.consumerV1ServicegroupsIdGet(id, (error, data, response) => {
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
 **id** | **Number**| id of the serviceGroup object | 

### Return type

[**ServiceGroupViewModel**](ServiceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

