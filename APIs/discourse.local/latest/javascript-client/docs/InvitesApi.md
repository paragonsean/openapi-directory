# DiscourseApiDocumentation.InvitesApi

All URIs are relative to *http://discourse.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInvite**](InvitesApi.md#createInvite) | **POST** /invites.json | Create an invite
[**inviteToTopic_0**](InvitesApi.md#inviteToTopic_0) | **POST** /t/{id}/invite.json | Invite to topic



## createInvite

> CreateInvite200Response createInvite(apiKey, apiUsername, opts)

Create an invite

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.InvitesApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let opts = {
  'createInviteRequest': new DiscourseApiDocumentation.CreateInviteRequest() // CreateInviteRequest | 
};
apiInstance.createInvite(apiKey, apiUsername, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **createInviteRequest** | [**CreateInviteRequest**](CreateInviteRequest.md)|  | [optional] 

### Return type

[**CreateInvite200Response**](CreateInvite200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## inviteToTopic_0

> InviteToTopic200Response inviteToTopic_0(apiKey, apiUsername, id, opts)

Invite to topic

### Example

```javascript
import DiscourseApiDocumentation from 'discourse_api_documentation';

let apiInstance = new DiscourseApiDocumentation.InvitesApi();
let apiKey = "apiKey_example"; // String | 
let apiUsername = "apiUsername_example"; // String | 
let id = "id_example"; // String | 
let opts = {
  'inviteToTopicRequest': new DiscourseApiDocumentation.InviteToTopicRequest() // InviteToTopicRequest | 
};
apiInstance.inviteToTopic_0(apiKey, apiUsername, id, opts, (error, data, response) => {
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
 **apiKey** | **String**|  | 
 **apiUsername** | **String**|  | 
 **id** | **String**|  | 
 **inviteToTopicRequest** | [**InviteToTopicRequest**](InviteToTopicRequest.md)|  | [optional] 

### Return type

[**InviteToTopic200Response**](InviteToTopic200Response.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

