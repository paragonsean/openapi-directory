# OnSchedConsumerApi.ResourceGroupsApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1ResourcegroupsGet**](ResourceGroupsApi.md#consumerV1ResourcegroupsGet) | **GET** /consumer/v1/resourcegroups | List Resource Groups
[**consumerV1ResourcegroupsIdGet**](ResourceGroupsApi.md#consumerV1ResourcegroupsIdGet) | **GET** /consumer/v1/resourcegroups/{id} | Get Resource Group



## consumerV1ResourcegroupsGet

> ResourceGroupListViewModel consumerV1ResourcegroupsGet(opts)

List Resource Groups

&lt;p&gt;Use this endpoint to return a list of &lt;b&gt;Resource Groups&lt;/b&gt; for the requested location. If not specified, the business location defaults to the primary business location.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ResourceGroupsApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'deleted': true, // Boolean | Filter results by deleted status
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1ResourcegroupsGet(opts, (error, data, response) => {
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
 **deleted** | **Boolean**| Filter results by deleted status | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ResourceGroupListViewModel**](ResourceGroupListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ResourcegroupsIdGet

> ResourceGroupViewModel consumerV1ResourcegroupsIdGet(id)

Get Resource Group

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource Group&lt;/b&gt; object. A valid &lt;b&gt;resourceGroup id&lt;/b&gt; is required. Find resourceGroup id&#39;s by using the &lt;i&gt;GET /consumer/v1/resourceGroups&lt;/i&gt; endpoint.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ResourceGroupsApi();
let id = "id_example"; // String | id of the resourceGroup object
apiInstance.consumerV1ResourcegroupsIdGet(id, (error, data, response) => {
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
 **id** | **String**| id of the resourceGroup object | 

### Return type

[**ResourceGroupViewModel**](ResourceGroupViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

