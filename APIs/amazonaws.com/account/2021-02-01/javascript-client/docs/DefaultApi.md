# AwsAccount.DefaultApi

All URIs are relative to *http://account.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deleteAlternateContact**](DefaultApi.md#deleteAlternateContact) | **POST** /deleteAlternateContact | 
[**disableRegion**](DefaultApi.md#disableRegion) | **POST** /disableRegion | 
[**enableRegion**](DefaultApi.md#enableRegion) | **POST** /enableRegion | 
[**getAlternateContact**](DefaultApi.md#getAlternateContact) | **POST** /getAlternateContact | 
[**getContactInformation**](DefaultApi.md#getContactInformation) | **POST** /getContactInformation | 
[**getRegionOptStatus**](DefaultApi.md#getRegionOptStatus) | **POST** /getRegionOptStatus | 
[**listRegions**](DefaultApi.md#listRegions) | **POST** /listRegions | 
[**putAlternateContact**](DefaultApi.md#putAlternateContact) | **POST** /putAlternateContact | 
[**putContactInformation**](DefaultApi.md#putContactInformation) | **POST** /putContactInformation | 



## deleteAlternateContact

> deleteAlternateContact(deleteAlternateContactRequest, opts)



&lt;p&gt;Deletes the specified alternate contact from an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the alternate contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Access or updating the alternate contacts&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html\&quot;&gt;Enabling trusted access for Amazon Web Services Account Management&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let deleteAlternateContactRequest = new AwsAccount.DeleteAlternateContactRequest(); // DeleteAlternateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAlternateContact(deleteAlternateContactRequest, opts, (error, data, response) => {
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
 **deleteAlternateContactRequest** | [**DeleteAlternateContactRequest**](DeleteAlternateContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disableRegion

> disableRegion(disableRegionRequest, opts)



Disables (opts-out) a particular Region for an account.

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let disableRegionRequest = new AwsAccount.DisableRegionRequest(); // DisableRegionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disableRegion(disableRegionRequest, opts, (error, data, response) => {
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
 **disableRegionRequest** | [**DisableRegionRequest**](DisableRegionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## enableRegion

> enableRegion(enableRegionRequest, opts)



Enables (opts-in) a particular Region for an account.

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let enableRegionRequest = new AwsAccount.EnableRegionRequest(); // EnableRegionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.enableRegion(enableRegionRequest, opts, (error, data, response) => {
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
 **enableRegionRequest** | [**EnableRegionRequest**](EnableRegionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAlternateContact

> GetAlternateContactResponse getAlternateContact(getAlternateContactRequest, opts)



&lt;p&gt;Retrieves the specified alternate contact attached to an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the alternate contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Access or updating the alternate contacts&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html\&quot;&gt;Enabling trusted access for Amazon Web Services Account Management&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let getAlternateContactRequest = new AwsAccount.GetAlternateContactRequest(); // GetAlternateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAlternateContact(getAlternateContactRequest, opts, (error, data, response) => {
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
 **getAlternateContactRequest** | [**GetAlternateContactRequest**](GetAlternateContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAlternateContactResponse**](GetAlternateContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContactInformation

> GetContactInformationResponse getContactInformation(getContactInformationRequest, opts)



&lt;p&gt;Retrieves the primary contact information of an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the primary contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Update the primary and alternate contact information&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let getContactInformationRequest = new AwsAccount.GetContactInformationRequest(); // GetContactInformationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContactInformation(getContactInformationRequest, opts, (error, data, response) => {
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
 **getContactInformationRequest** | [**GetContactInformationRequest**](GetContactInformationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactInformationResponse**](GetContactInformationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRegionOptStatus

> GetRegionOptStatusResponse getRegionOptStatus(getRegionOptStatusRequest, opts)



Retrieves the opt-in status of a particular Region.

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let getRegionOptStatusRequest = new AwsAccount.GetRegionOptStatusRequest(); // GetRegionOptStatusRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRegionOptStatus(getRegionOptStatusRequest, opts, (error, data, response) => {
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
 **getRegionOptStatusRequest** | [**GetRegionOptStatusRequest**](GetRegionOptStatusRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRegionOptStatusResponse**](GetRegionOptStatusResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRegions

> ListRegionsResponse listRegions(listRegionsRequest, opts)



Lists all the Regions for a given account and their respective opt-in statuses. Optionally, this list can be filtered by the &lt;code&gt;region-opt-status-contains&lt;/code&gt; parameter. 

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let listRegionsRequest = new AwsAccount.ListRegionsRequest(); // ListRegionsRequest | 
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
apiInstance.listRegions(listRegionsRequest, opts, (error, data, response) => {
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
 **listRegionsRequest** | [**ListRegionsRequest**](ListRegionsRequest.md)|  | 
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

[**ListRegionsResponse**](ListRegionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putAlternateContact

> putAlternateContact(putAlternateContactRequest, opts)



&lt;p&gt;Modifies the specified alternate contact attached to an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the alternate contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Access or updating the alternate contacts&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Before you can update the alternate contact information for an Amazon Web Services account that is managed by Organizations, you must first enable integration between Amazon Web Services Account Management and Organizations. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/using-orgs-trusted-access.html\&quot;&gt;Enabling trusted access for Amazon Web Services Account Management&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let putAlternateContactRequest = new AwsAccount.PutAlternateContactRequest(); // PutAlternateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAlternateContact(putAlternateContactRequest, opts, (error, data, response) => {
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
 **putAlternateContactRequest** | [**PutAlternateContactRequest**](PutAlternateContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putContactInformation

> putContactInformation(putContactInformationRequest, opts)



&lt;p&gt;Updates the primary contact information of an Amazon Web Services account.&lt;/p&gt; &lt;p&gt;For complete details about how to use the primary contact operations, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html\&quot;&gt;Update the primary and alternate contact information&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsAccount from 'aws_account';
let defaultClient = AwsAccount.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsAccount.DefaultApi();
let putContactInformationRequest = new AwsAccount.PutContactInformationRequest(); // PutContactInformationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putContactInformation(putContactInformationRequest, opts, (error, data, response) => {
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
 **putContactInformationRequest** | [**PutContactInformationRequest**](PutContactInformationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

null (empty response body)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

