# AwsLicenseManagerLinuxSubscriptions.DefaultApi

All URIs are relative to *http://license-manager-linux-subscriptions.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getServiceSettings**](DefaultApi.md#getServiceSettings) | **POST** /subscription/GetServiceSettings | 
[**listLinuxSubscriptionInstances**](DefaultApi.md#listLinuxSubscriptionInstances) | **POST** /subscription/ListLinuxSubscriptionInstances | 
[**listLinuxSubscriptions**](DefaultApi.md#listLinuxSubscriptions) | **POST** /subscription/ListLinuxSubscriptions | 
[**updateServiceSettings**](DefaultApi.md#updateServiceSettings) | **POST** /subscription/UpdateServiceSettings | 



## getServiceSettings

> GetServiceSettingsResponse getServiceSettings(opts)



Lists the Linux subscriptions service settings.

### Example

```javascript
import AwsLicenseManagerLinuxSubscriptions from 'aws_license_manager_linux_subscriptions';
let defaultClient = AwsLicenseManagerLinuxSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerLinuxSubscriptions.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getServiceSettings(opts, (error, data, response) => {
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
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetServiceSettingsResponse**](GetServiceSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listLinuxSubscriptionInstances

> ListLinuxSubscriptionInstancesResponse listLinuxSubscriptionInstances(listLinuxSubscriptionInstancesRequest, opts)



Lists the running Amazon EC2 instances that were discovered with commercial Linux subscriptions.

### Example

```javascript
import AwsLicenseManagerLinuxSubscriptions from 'aws_license_manager_linux_subscriptions';
let defaultClient = AwsLicenseManagerLinuxSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerLinuxSubscriptions.DefaultApi();
let listLinuxSubscriptionInstancesRequest = new AwsLicenseManagerLinuxSubscriptions.ListLinuxSubscriptionInstancesRequest(); // ListLinuxSubscriptionInstancesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listLinuxSubscriptionInstances(listLinuxSubscriptionInstancesRequest, opts, (error, data, response) => {
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
 **listLinuxSubscriptionInstancesRequest** | [**ListLinuxSubscriptionInstancesRequest**](ListLinuxSubscriptionInstancesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListLinuxSubscriptionInstancesResponse**](ListLinuxSubscriptionInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLinuxSubscriptions

> ListLinuxSubscriptionsResponse listLinuxSubscriptions(listLinuxSubscriptionsRequest, opts)



Lists the Linux subscriptions that have been discovered. If you have linked your organization, the returned results will include data aggregated across your accounts in Organizations.

### Example

```javascript
import AwsLicenseManagerLinuxSubscriptions from 'aws_license_manager_linux_subscriptions';
let defaultClient = AwsLicenseManagerLinuxSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerLinuxSubscriptions.DefaultApi();
let listLinuxSubscriptionsRequest = new AwsLicenseManagerLinuxSubscriptions.ListLinuxSubscriptionsRequest(); // ListLinuxSubscriptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listLinuxSubscriptions(listLinuxSubscriptionsRequest, opts, (error, data, response) => {
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
 **listLinuxSubscriptionsRequest** | [**ListLinuxSubscriptionsRequest**](ListLinuxSubscriptionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListLinuxSubscriptionsResponse**](ListLinuxSubscriptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateServiceSettings

> UpdateServiceSettingsResponse updateServiceSettings(updateServiceSettingsRequest, opts)



Updates the service settings for Linux subscriptions.

### Example

```javascript
import AwsLicenseManagerLinuxSubscriptions from 'aws_license_manager_linux_subscriptions';
let defaultClient = AwsLicenseManagerLinuxSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerLinuxSubscriptions.DefaultApi();
let updateServiceSettingsRequest = new AwsLicenseManagerLinuxSubscriptions.UpdateServiceSettingsRequest(); // UpdateServiceSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateServiceSettings(updateServiceSettingsRequest, opts, (error, data, response) => {
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
 **updateServiceSettingsRequest** | [**UpdateServiceSettingsRequest**](UpdateServiceSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateServiceSettingsResponse**](UpdateServiceSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

