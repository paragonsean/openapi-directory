# AgcoApi.UpdateGroupClientRelationshipsApi

All URIs are relative to *https://secure.agco-ats.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**updateGroupClientRelationshipsGetSubscription**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsGetSubscription) | **GET** /api/v2/UpdateGroupClientRelationships/{RelationshipID} | Get a subscription by RelationshipID
[**updateGroupClientRelationshipsGetSubscriptions**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsGetSubscriptions) | **GET** /api/v2/UpdateGroupClientRelationships | Get a list of current Client Subscriptions.
[**updateGroupClientRelationshipsPostSubscription**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsPostSubscription) | **POST** /api/v2/UpdateGroupClientRelationships | Add a subscription
[**updateGroupClientRelationshipsPutSubscription**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsPutSubscription) | **PUT** /api/v2/UpdateGroupClientRelationships/{RelationshipID} | Updates a Subscription
[**updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID**](UpdateGroupClientRelationshipsApi.md#updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID) | **PUT** /api/v2/UpdateGroupClientRelationships | DEPRECATED. Set client subscription status for an update group.



## updateGroupClientRelationshipsGetSubscription

> UpdateSystemModelsUpdateGroupClientRelationship updateGroupClientRelationshipsGetSubscription(relationshipID)

Get a subscription by RelationshipID

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupClientRelationshipsApi();
let relationshipID = "relationshipID_example"; // String | The RelationshipID.
apiInstance.updateGroupClientRelationshipsGetSubscription(relationshipID, (error, data, response) => {
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
 **relationshipID** | **String**| The RelationshipID. | 

### Return type

[**UpdateSystemModelsUpdateGroupClientRelationship**](UpdateSystemModelsUpdateGroupClientRelationship.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, application/xml, text/json, text/xml


## updateGroupClientRelationshipsGetSubscriptions

> APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship updateGroupClientRelationshipsGetSubscriptions(opts)

Get a list of current Client Subscriptions.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupClientRelationshipsApi();
let opts = {
  'clientID': "clientID_example", // String | Optional. Filter by Client ID
  'updateGroupID': "updateGroupID_example", // String | Optional. Filter by Update Group ID
  'limit': 56, // Number | Optional. The page limit. The default page limit is 10.
  'offset': 56, // Number | Optional. The page offset. The default page offset is 0.
  'active': true // Boolean | Optional. Filter by Active
};
apiInstance.updateGroupClientRelationshipsGetSubscriptions(opts, (error, data, response) => {
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
 **clientID** | **String**| Optional. Filter by Client ID | [optional] 
 **updateGroupID** | **String**| Optional. Filter by Update Group ID | [optional] 
 **limit** | **Number**| Optional. The page limit. The default page limit is 10. | [optional] 
 **offset** | **Number**| Optional. The page offset. The default page offset is 0. | [optional] 
 **active** | **Boolean**| Optional. Filter by Active | [optional] 

### Return type

[**APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship**](APIPagedResponseUpdateSystemModelsUpdateGroupClientRelationship.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json


## updateGroupClientRelationshipsPostSubscription

> String updateGroupClientRelationshipsPostSubscription(updateSystemModelsUpdateGroupClientRelationship)

Add a subscription

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupClientRelationshipsApi();
let updateSystemModelsUpdateGroupClientRelationship = new AgcoApi.UpdateSystemModelsUpdateGroupClientRelationship(); // UpdateSystemModelsUpdateGroupClientRelationship | The UpdateGroupClientRelationship to add.
apiInstance.updateGroupClientRelationshipsPostSubscription(updateSystemModelsUpdateGroupClientRelationship, (error, data, response) => {
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
 **updateSystemModelsUpdateGroupClientRelationship** | [**UpdateSystemModelsUpdateGroupClientRelationship**](UpdateSystemModelsUpdateGroupClientRelationship.md)| The UpdateGroupClientRelationship to add. | 

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: application/json, application/xml, text/json, text/xml


## updateGroupClientRelationshipsPutSubscription

> updateGroupClientRelationshipsPutSubscription(relationshipID, updateSystemModelsUpdateGroupClientRelationship)

Updates a Subscription

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupClientRelationshipsApi();
let relationshipID = "relationshipID_example"; // String | The relationship id of the UpdateGroupClientRelationship
let updateSystemModelsUpdateGroupClientRelationship = new AgcoApi.UpdateSystemModelsUpdateGroupClientRelationship(); // UpdateSystemModelsUpdateGroupClientRelationship | The updated UpdateGroupClientRelationship
apiInstance.updateGroupClientRelationshipsPutSubscription(relationshipID, updateSystemModelsUpdateGroupClientRelationship, (error, data, response) => {
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
 **relationshipID** | **String**| The relationship id of the UpdateGroupClientRelationship | 
 **updateSystemModelsUpdateGroupClientRelationship** | [**UpdateSystemModelsUpdateGroupClientRelationship**](UpdateSystemModelsUpdateGroupClientRelationship.md)| The updated UpdateGroupClientRelationship | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
- **Accept**: */*


## updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID

> updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID(clientID, updateGroupID, active)

DEPRECATED. Set client subscription status for an update group.

No Documentation Found.

### Example

```javascript
import AgcoApi from 'agco_api';

let apiInstance = new AgcoApi.UpdateGroupClientRelationshipsApi();
let clientID = "clientID_example"; // String | The Client ID.  This can be a client ID that has not been registered yet.
let updateGroupID = "updateGroupID_example"; // String | The Update Group ID
let active = true; // Boolean | Subscribe the client to the Update Group.
apiInstance.updateGroupClientRelationshipsPutSubscriptionByClientIDUpdateGroupID(clientID, updateGroupID, active, (error, data, response) => {
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
 **clientID** | **String**| The Client ID.  This can be a client ID that has not been registered yet. | 
 **updateGroupID** | **String**| The Update Group ID | 
 **active** | **Boolean**| Subscribe the client to the Update Group. | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: */*

