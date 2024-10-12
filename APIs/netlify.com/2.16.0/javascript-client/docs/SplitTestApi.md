# NetlifysApiDocumentation.SplitTestApi

All URIs are relative to *https://api.netlify.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createSplitTest**](SplitTestApi.md#createSplitTest) | **POST** /sites/{site_id}/traffic_splits | 
[**disableSplitTest**](SplitTestApi.md#disableSplitTest) | **POST** /sites/{site_id}/traffic_splits/{split_test_id}/unpublish | 
[**enableSplitTest**](SplitTestApi.md#enableSplitTest) | **POST** /sites/{site_id}/traffic_splits/{split_test_id}/publish | 
[**getSplitTest**](SplitTestApi.md#getSplitTest) | **GET** /sites/{site_id}/traffic_splits/{split_test_id} | 
[**getSplitTests**](SplitTestApi.md#getSplitTests) | **GET** /sites/{site_id}/traffic_splits | 
[**updateSplitTest**](SplitTestApi.md#updateSplitTest) | **PUT** /sites/{site_id}/traffic_splits/{split_test_id} | 



## createSplitTest

> SplitTest createSplitTest(siteId, branchTests)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SplitTestApi();
let siteId = "siteId_example"; // String | 
let branchTests = new NetlifysApiDocumentation.SplitTestSetup(); // SplitTestSetup | 
apiInstance.createSplitTest(siteId, branchTests, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **branchTests** | [**SplitTestSetup**](SplitTestSetup.md)|  | 

### Return type

[**SplitTest**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableSplitTest

> disableSplitTest(siteId, splitTestId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SplitTestApi();
let siteId = "siteId_example"; // String | 
let splitTestId = "splitTestId_example"; // String | 
apiInstance.disableSplitTest(siteId, splitTestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteId** | **String**|  | 
 **splitTestId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## enableSplitTest

> enableSplitTest(siteId, splitTestId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SplitTestApi();
let siteId = "siteId_example"; // String | 
let splitTestId = "splitTestId_example"; // String | 
apiInstance.enableSplitTest(siteId, splitTestId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **siteId** | **String**|  | 
 **splitTestId** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSplitTest

> SplitTest getSplitTest(siteId, splitTestId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SplitTestApi();
let siteId = "siteId_example"; // String | 
let splitTestId = "splitTestId_example"; // String | 
apiInstance.getSplitTest(siteId, splitTestId, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **splitTestId** | **String**|  | 

### Return type

[**SplitTest**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSplitTests

> [SplitTest] getSplitTests(siteId)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SplitTestApi();
let siteId = "siteId_example"; // String | 
apiInstance.getSplitTests(siteId, (error, data, response) => {
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
 **siteId** | **String**|  | 

### Return type

[**[SplitTest]**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSplitTest

> SplitTest updateSplitTest(siteId, splitTestId, branchTests)



### Example

```javascript
import NetlifysApiDocumentation from 'netlifys_api_documentation';
let defaultClient = NetlifysApiDocumentation.ApiClient.instance;
// Configure OAuth2 access token for authorization: netlifyAuth
let netlifyAuth = defaultClient.authentications['netlifyAuth'];
netlifyAuth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new NetlifysApiDocumentation.SplitTestApi();
let siteId = "siteId_example"; // String | 
let splitTestId = "splitTestId_example"; // String | 
let branchTests = new NetlifysApiDocumentation.SplitTestSetup(); // SplitTestSetup | 
apiInstance.updateSplitTest(siteId, splitTestId, branchTests, (error, data, response) => {
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
 **siteId** | **String**|  | 
 **splitTestId** | **String**|  | 
 **branchTests** | [**SplitTestSetup**](SplitTestSetup.md)|  | 

### Return type

[**SplitTest**](SplitTest.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

