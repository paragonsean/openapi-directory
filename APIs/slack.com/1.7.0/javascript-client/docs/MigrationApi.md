# SlackWebApi.MigrationApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**migrationExchange**](MigrationApi.md#migrationExchange) | **GET** /migration.exchange | 



## migrationExchange

> MigrationExchangeSuccessSchema migrationExchange(token, users, opts)



For Enterprise Grid workspaces, map local user IDs to global user IDs

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.MigrationApi();
let token = "token_example"; // String | Authentication token. Requires scope: `tokens.basic`
let users = "users_example"; // String | A comma-separated list of user ids, up to 400 per request
let opts = {
  'teamId': "teamId_example", // String | Specify team_id starts with `T` in case of Org Token
  'toOld': true // Boolean | Specify `true` to convert `W` global user IDs to workspace-specific `U` IDs. Defaults to `false`.
};
apiInstance.migrationExchange(token, users, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;tokens.basic&#x60; | 
 **users** | **String**| A comma-separated list of user ids, up to 400 per request | 
 **teamId** | **String**| Specify team_id starts with &#x60;T&#x60; in case of Org Token | [optional] 
 **toOld** | **Boolean**| Specify &#x60;true&#x60; to convert &#x60;W&#x60; global user IDs to workspace-specific &#x60;U&#x60; IDs. Defaults to &#x60;false&#x60;. | [optional] 

### Return type

[**MigrationExchangeSuccessSchema**](MigrationExchangeSuccessSchema.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

