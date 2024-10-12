# OnSchedConsumerApi.ResourcesApi

All URIs are relative to *https://sandbox-api.onsched.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consumerV1ResourcesGet**](ResourcesApi.md#consumerV1ResourcesGet) | **GET** /consumer/v1/resources | List Resources
[**consumerV1ResourcesIdGet**](ResourcesApi.md#consumerV1ResourcesIdGet) | **GET** /consumer/v1/resources/{id} | Get Resource
[**consumerV1ResourcesIdServicesGet**](ResourcesApi.md#consumerV1ResourcesIdServicesGet) | **GET** /consumer/v1/resources/{id}/services | Get Resource Linked Services



## consumerV1ResourcesGet

> ResourceListViewModel consumerV1ResourcesGet(opts)

List Resources

&lt;p&gt;Use this endpoint to return a &lt;b&gt;List of Resources&lt;/b&gt; associated with a business location. If not specified, the business location defaults to the primary business location. The results are returned in pages. Use the offset and limit parameters to control the page start and number of results. Default offset is 0, limit is 20, max is 100. Use the query parameters to filter the results further.&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ResourcesApi();
let opts = {
  'locationId': "locationId_example", // String | id of business location, defaults to primary business location
  'resourceGroupId': 56, // Number | Filter by groupId
  'email': "email_example", // String | Filter by email address
  'name': "name_example", // String | Search by name, supports Partial name search
  'sortOrder': "sortOrder_example", // String | Specify sort order of response
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1ResourcesGet(opts, (error, data, response) => {
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
 **resourceGroupId** | **Number**| Filter by groupId | [optional] 
 **email** | **String**| Filter by email address | [optional] 
 **name** | **String**| Search by name, supports Partial name search | [optional] 
 **sortOrder** | **String**| Specify sort order of response | [optional] 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ResourceListViewModel**](ResourceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ResourcesIdGet

> ResourceViewModel consumerV1ResourcesIdGet(id)

Get Resource

&lt;p&gt;Use this endpoint to return a &lt;b&gt;Resource&lt;/b&gt; object. A valid &lt;b&gt;resource id&lt;/b&gt; is required. Find resource id&#39;s by using the &lt;i&gt;GET consumer/v1/resources&lt;/i&gt; endpoint. &lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ResourcesApi();
let id = 56; // Number | id of resource object
apiInstance.consumerV1ResourcesIdGet(id, (error, data, response) => {
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
 **id** | **Number**| id of resource object | 

### Return type

[**ResourceViewModel**](ResourceViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## consumerV1ResourcesIdServicesGet

> ResourceServiceListViewModel consumerV1ResourcesIdServicesGet(id, opts)

Get Resource Linked Services

&lt;p&gt;Use this endpoint to get a &lt;b&gt;List of Linked Services&lt;/b&gt; associated with the resource requested. The results are returned in pages. Use the offset and limit parameters to control the page start and size. Default offset is 0, limit is 20, the maximum limit is 100. Use the other query parameters to filter the results further.&lt;/p&gt;  &lt;p&gt;Resource linked services are used to explicitly define the services that can be booked for a specified resource. By default, all services are bookable for any resource. For more information: &lt;a href&#x3D;\&quot;https://docs.onsched.com/docs/linked-services\&quot;&gt;Linked Services Overview&lt;/a&gt;&lt;/p&gt;

### Example

```javascript
import OnSchedConsumerApi from 'on_sched_consumer_api';
let defaultClient = OnSchedConsumerApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: oauth2
let oauth2 = defaultClient.authentications['oauth2'];
oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new OnSchedConsumerApi.ResourcesApi();
let id = 56; // Number | id of resource object
let opts = {
  'offset': 56, // Number | Starting row of page, default 0
  'limit': 56 // Number | Page limit default 20, max 100
};
apiInstance.consumerV1ResourcesIdServicesGet(id, opts, (error, data, response) => {
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
 **id** | **Number**| id of resource object | 
 **offset** | **Number**| Starting row of page, default 0 | [optional] 
 **limit** | **Number**| Page limit default 20, max 100 | [optional] 

### Return type

[**ResourceServiceListViewModel**](ResourceServiceListViewModel.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

