# DracoonApi.ResourcesApi

All URIs are relative to */api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**requestSubscriptionScopes**](ResourcesApi.md#requestSubscriptionScopes) | **GET** /v4/resources/user/notifications/scopes | Request list of subscription scopes
[**requestUserAvatar**](ResourcesApi.md#requestUserAvatar) | **GET** /v4/resources/users/{user_id}/avatar/{uuid} | Request user avatar



## requestSubscriptionScopes

> NotificationScopeList requestSubscriptionScopes()

Request list of subscription scopes

&lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.20.0&lt;/h3&gt;  ### Description: Retrieve a list of subscription scopes.  ### Precondition: Authenticated user.  ### Postcondition: List of scopes is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.ResourcesApi();
apiInstance.requestSubscriptionScopes((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**NotificationScopeList**](NotificationScopeList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## requestUserAvatar

> Avatar requestUserAvatar(uuid, userId)

Request user avatar

### Description: Get user avatar.  ### Precondition: Valid user ID and avatar UUID  ### Postcondition: Avatar is returned.  ### Further Information: None.

### Example

```javascript
import DracoonApi from 'dracoon_api';

let apiInstance = new DracoonApi.ResourcesApi();
let uuid = "uuid_example"; // String | UUID of the avatar
let userId = 789; // Number | User ID
apiInstance.requestUserAvatar(uuid, userId, (error, data, response) => {
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
 **uuid** | **String**| UUID of the avatar | 
 **userId** | **Number**| User ID | 

### Return type

[**Avatar**](Avatar.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

