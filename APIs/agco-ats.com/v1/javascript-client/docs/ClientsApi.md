# AgcoApi.ClientsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apiV2ClientsIDGet**](ClientsApi.md#apiV2ClientsIDGet) | **GET** /api/v2/Clients/{ID} | Get a Client in the Update System.
[**clientsGet**](ClientsApi.md#clientsGet) | **GET** /api/v2/Clients | Get a List of Clients in the Update System.
[**clientsGetAvailableSubscriptions**](ClientsApi.md#clientsGetAvailableSubscriptions) | **GET** /api/v2/Clients/{ID}/AvailableUpdateGroupSubscriptions | Get a Client&#39;s Available Update Group Subscriptions
[**clientsGetSubscriptions**](ClientsApi.md#clientsGetSubscriptions) | **GET** /api/v2/Clients/{ID}/UpdateGroupSubscriptions | Get a Client&#39;s Current Update Group Subscriptions
[**clientsPut**](ClientsApi.md#clientsPut) | **PUT** /api/v2/Clients/{ID} | Update a Client.



## apiV2ClientsIDGet

> UpdateSystemModelsClient apiV2ClientsIDGet(ID)

Get a Client in the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ClientsApi();
let ID = "ID_example"; // String | The Client ID
apiInstance.apiV2ClientsIDGet(ID, (error, data, response) => {
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
 **ID** | **String**| The Client ID | 

### Return type

[**UpdateSystemModelsClient**](UpdateSystemModelsClient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## clientsGet

> APIPagedResponseUpdateSystemModelsClient clientsGet(opts)

Get a List of Clients in the Update System.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ClientsApi();
let opts = {
  'tag': "tag_example", // String | Optional. Filter clients by Tag. Wildcards are supported (*).
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.clientsGet(opts, (error, data, response) => {
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
 **tag** | **String**| Optional. Filter clients by Tag. Wildcards are supported (*). | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsClient**](APIPagedResponseUpdateSystemModelsClient.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## clientsGetAvailableSubscriptions

> APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription clientsGetAvailableSubscriptions(ID, opts)

Get a Client&#39;s Available Update Group Subscriptions

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ClientsApi();
let ID = "ID_example"; // String | The Client ID
let opts = {
  'updateGroupID': "updateGroupID_example", // String | Optional. Filter by Update Group.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.clientsGetAvailableSubscriptions(ID, opts, (error, data, response) => {
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
 **ID** | **String**| The Client ID | 
 **updateGroupID** | **String**| Optional. Filter by Update Group. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription**](APIPagedResponseUpdateSystemModelsAvailableUpdateGroupSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## clientsGetSubscriptions

> APIPagedResponseUpdateSystemModelsUpdateGroupSubscription clientsGetSubscriptions(ID, opts)

Get a Client&#39;s Current Update Group Subscriptions

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ClientsApi();
let ID = "ID_example"; // String | The Client ID
let opts = {
  'updateGroupID': "updateGroupID_example", // String | Optional. Filter by Update Group.
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56 // Number | Optional. The page offset. The default page offset is 0.
};
apiInstance.clientsGetSubscriptions(ID, opts, (error, data, response) => {
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
 **ID** | **String**| The Client ID | 
 **updateGroupID** | **String**| Optional. Filter by Update Group. | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupSubscription**](APIPagedResponseUpdateSystemModelsUpdateGroupSubscription.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## clientsPut

> clientsPut(ID, updateSystemModelsClient)

Update a Client.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.ClientsApi();
let ID = "ID_example"; // String | The Client ID
let updateSystemModelsClient = new AgcoApi.UpdateSystemModelsClient(); // UpdateSystemModelsClient | Updated Client Object.
apiInstance.clientsPut(ID, updateSystemModelsClient, (error, data, response) => {
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
 **ID** | **String**| The Client ID | 
 **updateSystemModelsClient** | [**UpdateSystemModelsClient**](UpdateSystemModelsClient.md)| Updated Client Object. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*

