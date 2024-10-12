# MicrosoftResourceHealth.EmergingIssuesApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**emergingIssuesGet**](EmergingIssuesApi.md#emergingIssuesGet) | **GET** /providers/Microsoft.ResourceHealth/emergingIssues/{issueName} | 
[**emergingIssuesList**](EmergingIssuesApi.md#emergingIssuesList) | **GET** /providers/Microsoft.ResourceHealth/emergingIssues | 



## emergingIssuesGet

> EmergingIssuesGetResult emergingIssuesGet(issueName, apiVersion)



Gets Azure services&#39; emerging issues.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.EmergingIssuesApi();
let issueName = "issueName_example"; // String | The name of the emerging issue.
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.emergingIssuesGet(issueName, apiVersion, (error, data, response) => {
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
 **issueName** | **String**| The name of the emerging issue. | 
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**EmergingIssuesGetResult**](EmergingIssuesGetResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## emergingIssuesList

> EmergingIssueListResult emergingIssuesList(apiVersion)



Lists Azure services&#39; emerging issues.

### Example

```javascript
import MicrosoftResourceHealth from 'microsoft_resource_health';
let defaultClient = MicrosoftResourceHealth.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new MicrosoftResourceHealth.EmergingIssuesApi();
let apiVersion = "apiVersion_example"; // String | Client Api Version.
apiInstance.emergingIssuesList(apiVersion, (error, data, response) => {
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
 **apiVersion** | **String**| Client Api Version. | 

### Return type

[**EmergingIssueListResult**](EmergingIssueListResult.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

