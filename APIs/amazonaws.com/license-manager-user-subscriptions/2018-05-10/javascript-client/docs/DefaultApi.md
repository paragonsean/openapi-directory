# AwsLicenseManagerUserSubscriptions.DefaultApi

All URIs are relative to *http://license-manager-user-subscriptions.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateUser**](DefaultApi.md#associateUser) | **POST** /user/AssociateUser | 
[**deregisterIdentityProvider**](DefaultApi.md#deregisterIdentityProvider) | **POST** /identity-provider/DeregisterIdentityProvider | 
[**disassociateUser**](DefaultApi.md#disassociateUser) | **POST** /user/DisassociateUser | 
[**listIdentityProviders**](DefaultApi.md#listIdentityProviders) | **POST** /identity-provider/ListIdentityProviders | 
[**listInstances**](DefaultApi.md#listInstances) | **POST** /instance/ListInstances | 
[**listProductSubscriptions**](DefaultApi.md#listProductSubscriptions) | **POST** /user/ListProductSubscriptions | 
[**listUserAssociations**](DefaultApi.md#listUserAssociations) | **POST** /user/ListUserAssociations | 
[**registerIdentityProvider**](DefaultApi.md#registerIdentityProvider) | **POST** /identity-provider/RegisterIdentityProvider | 
[**startProductSubscription**](DefaultApi.md#startProductSubscription) | **POST** /user/StartProductSubscription | 
[**stopProductSubscription**](DefaultApi.md#stopProductSubscription) | **POST** /user/StopProductSubscription | 
[**updateIdentityProviderSettings**](DefaultApi.md#updateIdentityProviderSettings) | **POST** /identity-provider/UpdateIdentityProviderSettings | 



## associateUser

> AssociateUserResponse associateUser(associateUserRequest, opts)



&lt;p&gt;Associates the user to an EC2 instance to utilize user-based subscriptions.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Your estimated bill for charges on the number of users and related costs will take 48 hours to appear for billing periods that haven&#39;t closed (marked as &lt;b&gt;Pending&lt;/b&gt; billing status) in Amazon Web Services Billing. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html\&quot;&gt;Viewing your monthly charges&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let associateUserRequest = new AwsLicenseManagerUserSubscriptions.AssociateUserRequest(); // AssociateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateUser(associateUserRequest, opts, (error, data, response) => {
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
 **associateUserRequest** | [**AssociateUserRequest**](AssociateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateUserResponse**](AssociateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deregisterIdentityProvider

> DeregisterIdentityProviderResponse deregisterIdentityProvider(deregisterIdentityProviderRequest, opts)



Deregisters the identity provider from providing user-based subscriptions.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let deregisterIdentityProviderRequest = new AwsLicenseManagerUserSubscriptions.DeregisterIdentityProviderRequest(); // DeregisterIdentityProviderRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deregisterIdentityProvider(deregisterIdentityProviderRequest, opts, (error, data, response) => {
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
 **deregisterIdentityProviderRequest** | [**DeregisterIdentityProviderRequest**](DeregisterIdentityProviderRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeregisterIdentityProviderResponse**](DeregisterIdentityProviderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateUser

> DisassociateUserResponse disassociateUser(associateUserRequest, opts)



Disassociates the user from an EC2 instance providing user-based subscriptions.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let associateUserRequest = new AwsLicenseManagerUserSubscriptions.AssociateUserRequest(); // AssociateUserRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateUser(associateUserRequest, opts, (error, data, response) => {
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
 **associateUserRequest** | [**AssociateUserRequest**](AssociateUserRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateUserResponse**](DisassociateUserResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listIdentityProviders

> ListIdentityProvidersResponse listIdentityProviders(listIdentityProvidersRequest, opts)



Lists the identity providers for user-based subscriptions.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let listIdentityProvidersRequest = new AwsLicenseManagerUserSubscriptions.ListIdentityProvidersRequest(); // ListIdentityProvidersRequest | 
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
apiInstance.listIdentityProviders(listIdentityProvidersRequest, opts, (error, data, response) => {
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
 **listIdentityProvidersRequest** | [**ListIdentityProvidersRequest**](ListIdentityProvidersRequest.md)|  | 
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

[**ListIdentityProvidersResponse**](ListIdentityProvidersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listInstances

> ListInstancesResponse listInstances(listInstancesRequest, opts)



Lists the EC2 instances providing user-based subscriptions.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let listInstancesRequest = new AwsLicenseManagerUserSubscriptions.ListInstancesRequest(); // ListInstancesRequest | 
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
apiInstance.listInstances(listInstancesRequest, opts, (error, data, response) => {
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
 **listInstancesRequest** | [**ListInstancesRequest**](ListInstancesRequest.md)|  | 
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

[**ListInstancesResponse**](ListInstancesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listProductSubscriptions

> ListProductSubscriptionsResponse listProductSubscriptions(listProductSubscriptionsRequest, opts)



Lists the user-based subscription products available from an identity provider.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let listProductSubscriptionsRequest = new AwsLicenseManagerUserSubscriptions.ListProductSubscriptionsRequest(); // ListProductSubscriptionsRequest | 
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
apiInstance.listProductSubscriptions(listProductSubscriptionsRequest, opts, (error, data, response) => {
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
 **listProductSubscriptionsRequest** | [**ListProductSubscriptionsRequest**](ListProductSubscriptionsRequest.md)|  | 
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

[**ListProductSubscriptionsResponse**](ListProductSubscriptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listUserAssociations

> ListUserAssociationsResponse listUserAssociations(listUserAssociationsRequest, opts)



Lists user associations for an identity provider.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let listUserAssociationsRequest = new AwsLicenseManagerUserSubscriptions.ListUserAssociationsRequest(); // ListUserAssociationsRequest | 
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
apiInstance.listUserAssociations(listUserAssociationsRequest, opts, (error, data, response) => {
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
 **listUserAssociationsRequest** | [**ListUserAssociationsRequest**](ListUserAssociationsRequest.md)|  | 
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

[**ListUserAssociationsResponse**](ListUserAssociationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## registerIdentityProvider

> RegisterIdentityProviderResponse registerIdentityProvider(registerIdentityProviderRequest, opts)



Registers an identity provider for user-based subscriptions.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let registerIdentityProviderRequest = new AwsLicenseManagerUserSubscriptions.RegisterIdentityProviderRequest(); // RegisterIdentityProviderRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.registerIdentityProvider(registerIdentityProviderRequest, opts, (error, data, response) => {
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
 **registerIdentityProviderRequest** | [**RegisterIdentityProviderRequest**](RegisterIdentityProviderRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RegisterIdentityProviderResponse**](RegisterIdentityProviderResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startProductSubscription

> StartProductSubscriptionResponse startProductSubscription(startProductSubscriptionRequest, opts)



&lt;p&gt;Starts a product subscription for a user with the specified identity provider.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Your estimated bill for charges on the number of users and related costs will take 48 hours to appear for billing periods that haven&#39;t closed (marked as &lt;b&gt;Pending&lt;/b&gt; billing status) in Amazon Web Services Billing. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/invoice.html\&quot;&gt;Viewing your monthly charges&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Billing User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let startProductSubscriptionRequest = new AwsLicenseManagerUserSubscriptions.StartProductSubscriptionRequest(); // StartProductSubscriptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startProductSubscription(startProductSubscriptionRequest, opts, (error, data, response) => {
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
 **startProductSubscriptionRequest** | [**StartProductSubscriptionRequest**](StartProductSubscriptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartProductSubscriptionResponse**](StartProductSubscriptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopProductSubscription

> StopProductSubscriptionResponse stopProductSubscription(stopProductSubscriptionRequest, opts)



Stops a product subscription for a user with the specified identity provider.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let stopProductSubscriptionRequest = new AwsLicenseManagerUserSubscriptions.StopProductSubscriptionRequest(); // StopProductSubscriptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopProductSubscription(stopProductSubscriptionRequest, opts, (error, data, response) => {
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
 **stopProductSubscriptionRequest** | [**StopProductSubscriptionRequest**](StopProductSubscriptionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopProductSubscriptionResponse**](StopProductSubscriptionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateIdentityProviderSettings

> UpdateIdentityProviderSettingsResponse updateIdentityProviderSettings(updateIdentityProviderSettingsRequest, opts)



Updates additional product configuration settings for the registered identity provider.

### Example

```javascript
import AwsLicenseManagerUserSubscriptions from 'aws_license_manager_user_subscriptions';
let defaultClient = AwsLicenseManagerUserSubscriptions.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsLicenseManagerUserSubscriptions.DefaultApi();
let updateIdentityProviderSettingsRequest = new AwsLicenseManagerUserSubscriptions.UpdateIdentityProviderSettingsRequest(); // UpdateIdentityProviderSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateIdentityProviderSettings(updateIdentityProviderSettingsRequest, opts, (error, data, response) => {
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
 **updateIdentityProviderSettingsRequest** | [**UpdateIdentityProviderSettingsRequest**](UpdateIdentityProviderSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateIdentityProviderSettingsResponse**](UpdateIdentityProviderSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

