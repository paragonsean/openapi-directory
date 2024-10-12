# AmazonMobileAnalytics.DefaultApi

All URIs are relative to *http://mobileanalytics.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**putEvents**](DefaultApi.md#putEvents) | **POST** /2014-06-05/events#x-amz-Client-Context | 



## putEvents

> putEvents(xAmzClientContext, putEventsRequest, opts)



The PutEvents operation records one or more events. You can have up to 1,500 unique custom events per app, any combination of up to 40 attributes and metrics per custom event, and any number of attribute or metric values.

### Example

```javascript
import AmazonMobileAnalytics from 'amazon_mobile_analytics';
let defaultClient = AmazonMobileAnalytics.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMobileAnalytics.DefaultApi();
let xAmzClientContext = "xAmzClientContext_example"; // String | The client context including the client ID, app title, app version and package name.
let putEventsRequest = new AmazonMobileAnalytics.PutEventsRequest(); // PutEventsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'xAmzClientContextEncoding': "xAmzClientContextEncoding_example" // String | The encoding used for the client context.
};
apiInstance.putEvents(xAmzClientContext, putEventsRequest, opts, (error, data, response) => {
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
 **xAmzClientContext** | **String**| The client context including the client ID, app title, app version and package name. | 
 **putEventsRequest** | [**PutEventsRequest**](PutEventsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **xAmzClientContextEncoding** | **String**| The encoding used for the client context. | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

