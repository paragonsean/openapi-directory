# DaniWebConnectApi.GroupsApi

All URIs are relative to *https://www.daniweb.com/connect/api/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groupsGet**](GroupsApi.md#groupsGet) | **GET** /groups | 
[**groupsIDGet**](GroupsApi.md#groupsIDGet) | **GET** /groups/{ID} | 
[**groupsIDMembershipsDelete**](GroupsApi.md#groupsIDMembershipsDelete) | **DELETE** /groups/{ID}/memberships | 
[**groupsIDMembershipsGet**](GroupsApi.md#groupsIDMembershipsGet) | **GET** /groups/{ID}/memberships | 
[**groupsIDMembershipsPatch**](GroupsApi.md#groupsIDMembershipsPatch) | **PATCH** /groups/{ID}/memberships | 
[**groupsIDMembershipsPost**](GroupsApi.md#groupsIDMembershipsPost) | **POST** /groups/{ID}/memberships | 
[**groupsIDMessagesGet**](GroupsApi.md#groupsIDMessagesGet) | **GET** /groups/{ID}/messages | 
[**groupsIDMessagesPost**](GroupsApi.md#groupsIDMessagesPost) | **POST** /groups/{ID}/messages | 
[**groupsIDPatch**](GroupsApi.md#groupsIDPatch) | **PATCH** /groups/{ID} | 
[**groupsIDSchedulesPost**](GroupsApi.md#groupsIDSchedulesPost) | **POST** /groups/{ID}/schedules | 
[**groupsIDStatusesGet**](GroupsApi.md#groupsIDStatusesGet) | **GET** /groups/{ID}/statuses | 
[**groupsMessagesIDDelete**](GroupsApi.md#groupsMessagesIDDelete) | **DELETE** /groups/messages/{ID} | 
[**groupsMessagesIDGet**](GroupsApi.md#groupsMessagesIDGet) | **GET** /groups/messages/{ID} | 
[**groupsMessagesIDMetadataCollectionsGet**](GroupsApi.md#groupsMessagesIDMetadataCollectionsGet) | **GET** /groups/messages/{ID}/metadata/collections | 
[**groupsMessagesIDMetadataGet**](GroupsApi.md#groupsMessagesIDMetadataGet) | **GET** /groups/messages/{ID}/metadata | 
[**groupsMessagesIDMetadataPost**](GroupsApi.md#groupsMessagesIDMetadataPost) | **POST** /groups/messages/{ID}/metadata | 
[**groupsMessagesMetadataFiltersPost**](GroupsApi.md#groupsMessagesMetadataFiltersPost) | **POST** /groups/messages/metadata/filters | 
[**groupsPost**](GroupsApi.md#groupsPost) | **POST** /groups | 
[**groupsSchedulesPost**](GroupsApi.md#groupsSchedulesPost) | **POST** /groups/schedules | 
[**groupsStatusesGet**](GroupsApi.md#groupsStatusesGet) | **GET** /groups/statuses | 



## groupsGet

> EndpointGetGroups groupsGet(opts)



Fetch an array of all groups that were created by users existing within the current access token&#39;s bubble. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let opts = {
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.groupsGet(opts, (error, data, response) => {
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
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetGroups**](EndpointGetGroups.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsIDGet

> EndpointGetGroupsID groupsIDGet(ID)



Fetch an array of groups. You can only retrieve groups created by users existing within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = [null]; // [Number] | 
apiInstance.groupsIDGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetGroupsID**](EndpointGetGroupsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsIDMembershipsDelete

> EndpointDeleteGroupsIDMemberships groupsIDMembershipsDelete(ID)



Leave a group that you are a member of and that was created by a user who exists within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
apiInstance.groupsIDMembershipsDelete(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointDeleteGroupsIDMemberships**](EndpointDeleteGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsIDMembershipsGet

> EndpointGetGroupsIDMemberships groupsIDMembershipsGet(ID, opts)



Fetch an array of users who are members of specific groups that you are also a member of. You can only retrieve users existing within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = [null]; // [Number] | 
let opts = {
  'moderatorsOnly': false, // Boolean | 
  'offset': 0 // Number | 
};
apiInstance.groupsIDMembershipsGet(ID, opts, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 
 **moderatorsOnly** | **Boolean**|  | [optional] [default to false]
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**EndpointGetGroupsIDMemberships**](EndpointGetGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsIDMembershipsPatch

> EndpointPatchGroupsIDMemberships groupsIDMembershipsPatch(ID, userId, opts)



Promote or demote a member&#39;s privileges within a group that you created. The user must exist within the current access token&#39;s bubble and be an existing member of the group.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let userId = 56; // Number | 
let opts = {
  'moderator': false // Boolean | 
};
apiInstance.groupsIDMembershipsPatch(ID, userId, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **userId** | **Number**|  | 
 **moderator** | **Boolean**|  | [optional] [default to false]

### Return type

[**EndpointPatchGroupsIDMemberships**](EndpointPatchGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsIDMembershipsPost

> EndpointPostGroupsIDMemberships groupsIDMembershipsPost(ID, opts)



Join a group that was created by a user who exists within the current access token&#39;s bubble, or join other users into a group that you created. If you are the group owner, you can pass in a user_id to create membership records for a user you are in a conversation with. The user must exist within the current access token&#39;s bubble. If the group is private, you must successfully pass in its passphrase in order to join. You can obtain the passphrase from the group&#39;s owner.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let opts = {
  'passphrase': "passphrase_example", // String | 
  'userId': 56 // Number | 
};
apiInstance.groupsIDMembershipsPost(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **passphrase** | **String**|  | [optional] 
 **userId** | **Number**|  | [optional] 

### Return type

[**EndpointPostGroupsIDMemberships**](EndpointPostGroupsIDMemberships.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsIDMessagesGet

> EndpointGetGroupsIDMessages groupsIDMessagesGet(ID, opts)



Retrieve the last {limit} messages in the group, for messages authored by users within the current access token&#39;s bubble. If a timeout is 0 or greater, the batch is sorted oldest first. Otherwise, if timeout is a negative number, the transcript is paginated and sorted newest first. Specify a timeout for long polling (which delays the server sending back results for up to n seconds or until results are available, whichever comes first), or default to 0 for immediate results. Optionally record your status as online along with sharing the latest message you&#39;ve seen with other group members. Optionally specify a gt_message_id to retrieve only messages with an ID greater than that specified (such as greater than the latest message ID received in the last poll). Optionally only poll for messages authored by other members of the group, and echo messages authored by you when sending, for a perceived increase in performance. Optionally only retrieve messages that were posted from within the current access token&#39;s bubble. Optionally specify a date formatted as YYYY-MM-DD to retrieve a transcript of messages from a single day. When record_seen is set to true, the new message count for the group is reset to zero.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let opts = {
  'gtMessageId': 56, // Number | 
  'excludeSelf': false, // Boolean | 
  'includeDeleted': false, // Boolean | 
  'date': "date_example", // String | 
  'bubbled': false, // Boolean | 
  'recordSeen': false, // Boolean | 
  'timeout': 0, // Number | 
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.groupsIDMessagesGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **gtMessageId** | **Number**|  | [optional] 
 **excludeSelf** | **Boolean**|  | [optional] [default to false]
 **includeDeleted** | **Boolean**|  | [optional] [default to false]
 **date** | **String**|  | [optional] 
 **bubbled** | **Boolean**|  | [optional] [default to false]
 **recordSeen** | **Boolean**|  | [optional] [default to false]
 **timeout** | **Number**|  | [optional] [default to 0]
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetGroupsIDMessages**](EndpointGetGroupsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsIDMessagesPost

> EndpointPostGroupsIDMessages groupsIDMessagesPost(ID, textRaw, opts)



Post a message to a group that you are a member of and that was created by a user who exists within the current access token&#39;s bubble. Optionally specify whether emoticons should be parsed into smiley images. Additionally, optionally attach a single metadata key/value pair to the group message upon submission.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let textRaw = "textRaw_example"; // String | 
let opts = {
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Privacy': "metadata0Privacy_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Privacy': "metadata1Privacy_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Privacy': "metadata2Privacy_example", // String | 
  'metadata2Values': ["null"], // [String] | 
  'textEmoticons': false // Boolean | 
};
apiInstance.groupsIDMessagesPost(ID, textRaw, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **textRaw** | **String**|  | 
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Privacy** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Privacy** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Privacy** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 
 **textEmoticons** | **Boolean**|  | [optional] [default to false]

### Return type

[**EndpointPostGroupsIDMessages**](EndpointPostGroupsIDMessages.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsIDPatch

> EndpointPatchGroupsID groupsIDPatch(ID, opts)



Modify a group you previously created.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let opts = {
  'description': "description_example", // String | 
  'name': "name_example", // String | 
  'passphrase': "passphrase_example", // String | 
  'privacy': "privacy_example", // String | 
  'slug': "slug_example" // String | 
};
apiInstance.groupsIDPatch(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **description** | **String**|  | [optional] 
 **name** | **String**|  | [optional] 
 **passphrase** | **String**|  | [optional] 
 **privacy** | **String**|  | [optional] 
 **slug** | **String**|  | [optional] 

### Return type

[**EndpointPatchGroupsID**](EndpointPatchGroupsID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsIDSchedulesPost

> EndpointPostGroupsIDSchedules groupsIDSchedulesPost(ID, opts)



Paginated report of information about group messages contributed by conversation and date. Only groups you&#39;re a member of and group messages authored by users existing within the current access token&#39;s bubble are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages within the group discussion(s).

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = [null]; // [Number] | 
let opts = {
  'date': "date_example", // String | 
  'limit': 50, // Number | 
  'offset': 0, // Number | 
  'rollUp': false, // Boolean | 
  'sort': "'desc'" // String | 
};
apiInstance.groupsIDSchedulesPost(ID, opts, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 
 **date** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **offset** | **Number**|  | [optional] [default to 0]
 **rollUp** | **Boolean**|  | [optional] [default to false]
 **sort** | **String**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**EndpointPostGroupsIDSchedules**](EndpointPostGroupsIDSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsIDStatusesGet

> EndpointGetGroupsIDStatuses groupsIDStatusesGet(ID)



Status information about your current relationship with one or more groups you are a member of, provided the users who created the groups exist within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = [null]; // [Number] | 
apiInstance.groupsIDStatusesGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetGroupsIDStatuses**](EndpointGetGroupsIDStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsMessagesIDDelete

> EndpointDeleteGroupsMessagesID groupsMessagesIDDelete(ID)



Delete an array of group messages. You must be the owner or moderator of the group.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = [null]; // [Number] | 
apiInstance.groupsMessagesIDDelete(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointDeleteGroupsMessagesID**](EndpointDeleteGroupsMessagesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsMessagesIDGet

> EndpointGetGroupsMessagesID groupsMessagesIDGet(ID)



Fetch an array of group messages. You can only retrieve messages authored by you or by users existing within the current access token&#39;s bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = [null]; // [Number] | 
apiInstance.groupsMessagesIDGet(ID, (error, data, response) => {
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
 **ID** | [**[Number]**](Number.md)|  | 

### Return type

[**EndpointGetGroupsMessagesID**](EndpointGetGroupsMessagesID.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsMessagesIDMetadataCollectionsGet

> EndpointGetGroupsMessagesIDMetadataCollections groupsMessagesIDMetadataCollectionsGet(ID)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
apiInstance.groupsMessagesIDMetadataCollectionsGet(ID, (error, data, response) => {
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
 **ID** | **Number**|  | 

### Return type

[**EndpointGetGroupsMessagesIDMetadataCollections**](EndpointGetGroupsMessagesIDMetadataCollections.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsMessagesIDMetadataGet

> EndpointGetGroupsMessagesIDMetadata groupsMessagesIDMetadataGet(ID, opts)



Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who created the group exists within the current access token&#39;s bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let opts = {
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.groupsMessagesIDMetadataGet(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetGroupsMessagesIDMetadata**](EndpointGetGroupsMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## groupsMessagesIDMetadataPost

> EndpointPostGroupsMessagesIDMetadata groupsMessagesIDMetadataPost(ID, opts)



Attach one-to-many key/value pairs of metadata to a group message, so long as the user who authored the message exists within the current access token&#39;s bubble and you are a member of their group. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by anyone using an access token which grants them access to the user who authored the message and who is also a member of the group the message belongs to; Bubbled metadata by anyone using an access token existing within the current bubble who is also a member of the group the message belongs to; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message and you remain a member of the group; Private metadata by you, so long as you are using an access token existing within the current bubble and you remain a member of the group.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let ID = 56; // Number | 
let opts = {
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Privacy': "metadata0Privacy_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Privacy': "metadata1Privacy_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Privacy': "metadata2Privacy_example", // String | 
  'metadata2Values': ["null"] // [String] | 
};
apiInstance.groupsMessagesIDMetadataPost(ID, opts, (error, data, response) => {
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
 **ID** | **Number**|  | 
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Privacy** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Privacy** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Privacy** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 

### Return type

[**EndpointPostGroupsMessagesIDMetadata**](EndpointPostGroupsMessagesIDMetadata.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsMessagesMetadataFiltersPost

> EndpointPostGroupsMessagesMetadataFilters groupsMessagesMetadataFiltersPost(opts)



Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let opts = {
  'limit': 50, // Number | 
  'metadata0Key': "metadata0Key_example", // String | 
  'metadata0Values': ["null"], // [String] | 
  'metadata1Key': "metadata1Key_example", // String | 
  'metadata1Values': ["null"], // [String] | 
  'metadata2Key': "metadata2Key_example", // String | 
  'metadata2Values': ["null"], // [String] | 
  'offset': 0 // Number | 
};
apiInstance.groupsMessagesMetadataFiltersPost(opts, (error, data, response) => {
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
 **limit** | **Number**|  | [optional] [default to 50]
 **metadata0Key** | **String**|  | [optional] 
 **metadata0Values** | [**[String]**](String.md)|  | [optional] 
 **metadata1Key** | **String**|  | [optional] 
 **metadata1Values** | [**[String]**](String.md)|  | [optional] 
 **metadata2Key** | **String**|  | [optional] 
 **metadata2Values** | [**[String]**](String.md)|  | [optional] 
 **offset** | **Number**|  | [optional] [default to 0]

### Return type

[**EndpointPostGroupsMessagesMetadataFilters**](EndpointPostGroupsMessagesMetadataFilters.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsPost

> EndpointPostGroups groupsPost(description, name, privacy, slug, opts)



Create a new group for other members to join. Any user who is using an access token whose bubble you exist in can join your group provided it is not a private group. Private groups can only be joined by members who know its passphrase. Unlisted groups can be joined by anybody as long as they know the Group ID, but they are not referenced anywhere to non-members. Public groups can be joined by anybody, are discoverable, and anyone can see the public groups a user is a member of, provided the group owner exists in their access token&#39;s bubble. Groups each have their own discussions, transcripts, schedules, and ability to list and search their members.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let description = "description_example"; // String | 
let name = "name_example"; // String | 
let privacy = "privacy_example"; // String | 
let slug = "slug_example"; // String | 
let opts = {
  'passphrase': "passphrase_example" // String | 
};
apiInstance.groupsPost(description, name, privacy, slug, opts, (error, data, response) => {
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
 **description** | **String**|  | 
 **name** | **String**|  | 
 **privacy** | **String**|  | 
 **slug** | **String**|  | 
 **passphrase** | **String**|  | [optional] 

### Return type

[**EndpointPostGroups**](EndpointPostGroups.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsSchedulesPost

> EndpointPostGroupsSchedules groupsSchedulesPost(opts)



Paginated report of information about messages contributed by group and date. Only groups you&#39;re a member of and group messages authored by users the current access token has access to are considered in the calculations. Optionally roll up all groups to retrieve one record per date. Optionally specify a date formatted as YYYY-MM-DD to retrieve information just from the single date, along with additional navigational information, which is useful when generating a transcript for a single day and wanting to reference the previous and next days there were messages.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let opts = {
  'date': "date_example", // String | 
  'limit': 50, // Number | 
  'offset': 0, // Number | 
  'rollUp': false, // Boolean | 
  'sort': "'desc'" // String | 
};
apiInstance.groupsSchedulesPost(opts, (error, data, response) => {
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
 **date** | **String**|  | [optional] 
 **limit** | **Number**|  | [optional] [default to 50]
 **offset** | **Number**|  | [optional] [default to 0]
 **rollUp** | **Boolean**|  | [optional] [default to false]
 **sort** | **String**|  | [optional] [default to &#39;desc&#39;]

### Return type

[**EndpointPostGroupsSchedules**](EndpointPostGroupsSchedules.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: multipart/form-data
- **Accept**: application/json


## groupsStatusesGet

> EndpointGetGroupsStatuses groupsStatusesGet(opts)



Retrieve groups that were created by users within the current access token&#39;s bubble, along with your current relationship with the groups. The groups must be either Public or you must be a member of them. Unlisted and Private groups that you are not a member of are not listed. Optionally only retrieve groups that you are a member of.

### Example

```javascript
import DaniWebConnectApi from 'dani_web_connect_api';
let defaultClient = DaniWebConnectApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: implicit_flow
let implicit_flow = defaultClient.authentications['implicit_flow'];
implicit_flow.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: explicit_flow
let explicit_flow = defaultClient.authentications['explicit_flow'];
explicit_flow.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DaniWebConnectApi.GroupsApi();
let opts = {
  'existingMembership': false, // Boolean | 
  'offset': 0, // Number | 
  'limit': 50 // Number | 
};
apiInstance.groupsStatusesGet(opts, (error, data, response) => {
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
 **existingMembership** | **Boolean**|  | [optional] [default to false]
 **offset** | **Number**|  | [optional] [default to 0]
 **limit** | **Number**|  | [optional] [default to 50]

### Return type

[**EndpointGetGroupsStatuses**](EndpointGetGroupsStatuses.md)

### Authorization

[implicit_flow](../README.md#implicit_flow), [explicit_flow](../README.md#explicit_flow)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

