# SlackWebApi.SearchApi

All URIs are relative to *https://slack.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchMessages**](SearchApi.md#searchMessages) | **GET** /search.messages | 



## searchMessages

> DefaultSuccessTemplate searchMessages(token, query, opts)



Searches for messages matching a query.

### Example

```javascript
import SlackWebApi from 'slack_web_api';
let defaultClient = SlackWebApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: slackAuth
let slackAuth = defaultClient.authentications['slackAuth'];
slackAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SlackWebApi.SearchApi();
let token = "token_example"; // String | Authentication token. Requires scope: `search:read`
let query = "query_example"; // String | Search query.
let opts = {
  'count': 56, // Number | Pass the number of results you want per \"page\". Maximum of `100`.
  'highlight': true, // Boolean | Pass a value of `true` to enable query highlight markers (see below).
  'page': 56, // Number | 
  'sort': "sort_example", // String | Return matches sorted by either `score` or `timestamp`.
  'sortDir': "sortDir_example" // String | Change sort direction to ascending (`asc`) or descending (`desc`).
};
apiInstance.searchMessages(token, query, opts, (error, data, response) => {
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
 **token** | **String**| Authentication token. Requires scope: &#x60;search:read&#x60; | 
 **query** | **String**| Search query. | 
 **count** | **Number**| Pass the number of results you want per \&quot;page\&quot;. Maximum of &#x60;100&#x60;. | [optional] 
 **highlight** | **Boolean**| Pass a value of &#x60;true&#x60; to enable query highlight markers (see below). | [optional] 
 **page** | **Number**|  | [optional] 
 **sort** | **String**| Return matches sorted by either &#x60;score&#x60; or &#x60;timestamp&#x60;. | [optional] 
 **sortDir** | **String**| Change sort direction to ascending (&#x60;asc&#x60;) or descending (&#x60;desc&#x60;). | [optional] 

### Return type

[**DefaultSuccessTemplate**](DefaultSuccessTemplate.md)

### Authorization

[slackAuth](../README.md#slackAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

