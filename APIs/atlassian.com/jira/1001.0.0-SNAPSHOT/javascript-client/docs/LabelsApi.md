# TheJiraCloudPlatformRestApi.LabelsApi

All URIs are relative to *https://your-domain.atlassian.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getAllLabels**](LabelsApi.md#getAllLabels) | **GET** /rest/api/3/label | Get all labels



## getAllLabels

> PageBeanString getAllLabels(opts)

Get all labels

Returns a [paginated](#pagination) list of labels.

### Example

```javascript
import TheJiraCloudPlatformRestApi from 'the_jira_cloud_platform_rest_api';
let defaultClient = TheJiraCloudPlatformRestApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';
// Configure HTTP basic authorization: basicAuth
let basicAuth = defaultClient.authentications['basicAuth'];
basicAuth.username = 'YOUR USERNAME';
basicAuth.password = 'YOUR PASSWORD';

let apiInstance = new TheJiraCloudPlatformRestApi.LabelsApi();
let opts = {
  'startAt': 0, // Number | The index of the first item to return in a page of results (page offset).
  'maxResults': 1000 // Number | The maximum number of items to return per page.
};
apiInstance.getAllLabels(opts, (error, data, response) => {
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
 **startAt** | **Number**| The index of the first item to return in a page of results (page offset). | [optional] [default to 0]
 **maxResults** | **Number**| The maximum number of items to return per page. | [optional] [default to 1000]

### Return type

[**PageBeanString**](PageBeanString.md)

### Authorization

[OAuth2](../README.md#OAuth2), [basicAuth](../README.md#basicAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

