# AwsMarketplaceEntitlementService.DefaultApi

All URIs are relative to *http://entitlement.marketplace.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getEntitlements**](DefaultApi.md#getEntitlements) | **POST** /#X-Amz-Target&#x3D;AWSMPEntitlementService.GetEntitlements | 



## getEntitlements

> GetEntitlementsResult getEntitlements(xAmzTarget, getEntitlementsRequest, opts)



GetEntitlements retrieves entitlement values for a given product. The results can be filtered based on customer identifier or product dimensions.

### Example

```javascript
import AwsMarketplaceEntitlementService from 'aws_marketplace_entitlement_service';
let defaultClient = AwsMarketplaceEntitlementService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsMarketplaceEntitlementService.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getEntitlementsRequest = new AwsMarketplaceEntitlementService.GetEntitlementsRequest(); // GetEntitlementsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEntitlements(xAmzTarget, getEntitlementsRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **getEntitlementsRequest** | [**GetEntitlementsRequest**](GetEntitlementsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEntitlementsResult**](GetEntitlementsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

