# Apacta.TimeEntryRuleGroupsApi

All URIs are relative to *https://app.apacta.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeEntryRuleGroupsGet**](TimeEntryRuleGroupsApi.md#timeEntryRuleGroupsGet) | **GET** /time_entry_rule_groups | List time entry rule groups



## timeEntryRuleGroupsGet

> TimeEntryRuleGroupsGet200Response timeEntryRuleGroupsGet(opts)

List time entry rule groups

### Example

```javascript
import Apacta from 'apacta';
let defaultClient = Apacta.ApiClient.instance;
// Configure API key authorization: api_key
let api_key = defaultClient.authentications['api_key'];
api_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api_key.apiKeyPrefix = 'Token';
// Configure API key authorization: X-Auth-Token
let X-Auth-Token = defaultClient.authentications['X-Auth-Token'];
X-Auth-Token.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//X-Auth-Token.apiKeyPrefix = 'Token';

let apiInstance = new Apacta.TimeEntryRuleGroupsApi();
let opts = {
  'q': "q_example" // String | 
};
apiInstance.timeEntryRuleGroupsGet(opts, (error, data, response) => {
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
 **q** | **String**|  | [optional] 

### Return type

[**TimeEntryRuleGroupsGet200Response**](TimeEntryRuleGroupsGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

