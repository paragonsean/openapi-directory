# ConversationApi.MemberApi

All URIs are relative to *https://api.nexmo.com/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createMember**](MemberApi.md#createMember) | **POST** /conversations/{conversation_id}/members | Create a member
[**deleteMember**](MemberApi.md#deleteMember) | **DELETE** /conversations/{conversation_id}/members/{member_id} | Delete a member
[**getMember**](MemberApi.md#getMember) | **GET** /conversations/{conversation_id}/members/{member_id} | Retrieve a member
[**getMembers**](MemberApi.md#getMembers) | **GET** /conversations/{conversation_id}/members | List members
[**updateMember**](MemberApi.md#updateMember) | **PUT** /conversations/{conversation_id}/members/{member_id} | Update a member



## createMember

> CreateMember201Response createMember(conversationId, opts)

Create a member

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.MemberApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let opts = {
  'createMemberRequest': new ConversationApi.CreateMemberRequest() // CreateMemberRequest | 
};
apiInstance.createMember(conversationId, opts, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **createMemberRequest** | [**CreateMemberRequest**](CreateMemberRequest.md)|  | [optional] 

### Return type

[**CreateMember201Response**](CreateMember201Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteMember

> Object deleteMember(conversationId, memberId)

Delete a member

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.MemberApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let memberId = "memberId_example"; // String | Member ID
apiInstance.deleteMember(conversationId, memberId, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **memberId** | **String**| Member ID | 

### Return type

**Object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMember

> GetMember200Response getMember(conversationId, memberId)

Retrieve a member

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.MemberApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let memberId = "memberId_example"; // String | Member ID
apiInstance.getMember(conversationId, memberId, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **memberId** | **String**| Member ID | 

### Return type

[**GetMember200Response**](GetMember200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getMembers

> [GetMembers200ResponseInner] getMembers(conversationId)

List members

This endpoint is **DEPRECATED**. Please use [/v0.2/members](/api/conversation.v2#get-members).

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.MemberApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
apiInstance.getMembers(conversationId, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 

### Return type

[**[GetMembers200ResponseInner]**](GetMembers200ResponseInner.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateMember

> GetMember200Response updateMember(conversationId, memberId, opts)

Update a member

### Example

```javascript
import ConversationApi from 'conversation_api';
let defaultClient = ConversationApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: bearerAuth
let bearerAuth = defaultClient.authentications['bearerAuth'];
bearerAuth.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new ConversationApi.MemberApi();
let conversationId = "CON-f972836a-550f-45fa-956c-12a2ab5b7d22"; // String | Conversation ID
let memberId = "memberId_example"; // String | Member ID
let opts = {
  'updateMemberRequest': new ConversationApi.UpdateMemberRequest() // UpdateMemberRequest | 
};
apiInstance.updateMember(conversationId, memberId, opts, (error, data, response) => {
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
 **conversationId** | **String**| Conversation ID | 
 **memberId** | **String**| Member ID | 
 **updateMemberRequest** | [**UpdateMemberRequest**](UpdateMemberRequest.md)|  | [optional] 

### Return type

[**GetMember200Response**](GetMember200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

