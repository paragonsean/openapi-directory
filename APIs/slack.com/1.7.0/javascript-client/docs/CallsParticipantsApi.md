# SlackWebApi.CallsParticipantsApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**callsParticipantsAdd**](CallsParticipantsApi.md#callsParticipantsAdd) | **POST** /calls.participants.add | 
[**callsParticipantsRemove**](CallsParticipantsApi.md#callsParticipantsRemove) | **POST** /calls.participants.remove | 



## callsParticipantsAdd

> DefaultSuccessTemplate callsParticipantsAdd(token, id, users)



Registers new participants added to a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsParticipantsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
let users = "users_example"; // String | The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
apiInstance.callsParticipantsAdd(token, id, users, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 
 **users** | **String**| The list of users to add as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## callsParticipantsRemove

> DefaultSuccessTemplate callsParticipantsRemove(token, id, users)



Registers participants removed from a Call.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.CallsParticipantsApi();
let token = "token_example"; // String | Authentication token. Requires scope: `calls:write`
let id = "id_example"; // String | `id` returned by the [`calls.add`](/methods/calls.add) method.
let users = "users_example"; // String | The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users).
apiInstance.callsParticipantsRemove(token, id, users, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;calls:write&#x60; | 
 **id** | **String**| &#x60;id&#x60; returned by the [&#x60;calls.add&#x60;](/methods/calls.add) method. | 
 **users** | **String**| The list of users to remove as participants in the Call. [Read more on how to specify users here](/apis/calls#users). | 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

