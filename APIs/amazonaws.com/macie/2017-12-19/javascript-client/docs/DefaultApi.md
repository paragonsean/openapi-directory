# AmazonMacie.DefaultApi

All URIs are relative to *http://macie.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**associateMemberAccount**](DefaultApi.md#associateMemberAccount) | **POST** /#X-Amz-Target&#x3D;MacieService.AssociateMemberAccount | 
[**associateS3Resources**](DefaultApi.md#associateS3Resources) | **POST** /#X-Amz-Target&#x3D;MacieService.AssociateS3Resources | 
[**disassociateMemberAccount**](DefaultApi.md#disassociateMemberAccount) | **POST** /#X-Amz-Target&#x3D;MacieService.DisassociateMemberAccount | 
[**disassociateS3Resources**](DefaultApi.md#disassociateS3Resources) | **POST** /#X-Amz-Target&#x3D;MacieService.DisassociateS3Resources | 
[**listMemberAccounts**](DefaultApi.md#listMemberAccounts) | **POST** /#X-Amz-Target&#x3D;MacieService.ListMemberAccounts | 
[**listS3Resources**](DefaultApi.md#listS3Resources) | **POST** /#X-Amz-Target&#x3D;MacieService.ListS3Resources | 
[**updateS3Resources**](DefaultApi.md#updateS3Resources) | **POST** /#X-Amz-Target&#x3D;MacieService.UpdateS3Resources | 



## associateMemberAccount

> associateMemberAccount(xAmzTarget, associateMemberAccountRequest, opts)



(Discontinued) Associates a specified Amazon Web Services account with Amazon Macie Classic as a member account.

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let associateMemberAccountRequest = new AmazonMacie.AssociateMemberAccountRequest(); // AssociateMemberAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateMemberAccount(xAmzTarget, associateMemberAccountRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **associateMemberAccountRequest** | [**AssociateMemberAccountRequest**](AssociateMemberAccountRequest.md)|  | 
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


## associateS3Resources

> AssociateS3ResourcesResult associateS3Resources(xAmzTarget, associateS3ResourcesRequest, opts)



(Discontinued) Associates specified S3 resources with Amazon Macie Classic for monitoring and data classification. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action associates specified S3 resources with Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action associates specified S3 resources with Macie Classic for the specified member account.

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let associateS3ResourcesRequest = new AmazonMacie.AssociateS3ResourcesRequest(); // AssociateS3ResourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.associateS3Resources(xAmzTarget, associateS3ResourcesRequest, opts, (error, data, response) => {
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
 **associateS3ResourcesRequest** | [**AssociateS3ResourcesRequest**](AssociateS3ResourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AssociateS3ResourcesResult**](AssociateS3ResourcesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## disassociateMemberAccount

> disassociateMemberAccount(xAmzTarget, disassociateMemberAccountRequest, opts)



(Discontinued) Removes the specified member account from Amazon Macie Classic.

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let disassociateMemberAccountRequest = new AmazonMacie.DisassociateMemberAccountRequest(); // DisassociateMemberAccountRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateMemberAccount(xAmzTarget, disassociateMemberAccountRequest, opts, (error, data, response) => {
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
 **xAmzTarget** | **String**|  | 
 **disassociateMemberAccountRequest** | [**DisassociateMemberAccountRequest**](DisassociateMemberAccountRequest.md)|  | 
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


## disassociateS3Resources

> DisassociateS3ResourcesResult disassociateS3Resources(xAmzTarget, disassociateS3ResourcesRequest, opts)



(Discontinued) Removes specified S3 resources from being monitored by Amazon Macie Classic. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action removes specified S3 resources from Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action removes specified S3 resources from Macie Classic for the specified member account.

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let disassociateS3ResourcesRequest = new AmazonMacie.DisassociateS3ResourcesRequest(); // DisassociateS3ResourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.disassociateS3Resources(xAmzTarget, disassociateS3ResourcesRequest, opts, (error, data, response) => {
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
 **disassociateS3ResourcesRequest** | [**DisassociateS3ResourcesRequest**](DisassociateS3ResourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DisassociateS3ResourcesResult**](DisassociateS3ResourcesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listMemberAccounts

> ListMemberAccountsResult listMemberAccounts(xAmzTarget, listMemberAccountsRequest, opts)



(Discontinued) Lists all Amazon Macie Classic member accounts for the current Macie Classic administrator account.

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listMemberAccountsRequest = new AmazonMacie.ListMemberAccountsRequest(); // ListMemberAccountsRequest | 
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
apiInstance.listMemberAccounts(xAmzTarget, listMemberAccountsRequest, opts, (error, data, response) => {
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
 **listMemberAccountsRequest** | [**ListMemberAccountsRequest**](ListMemberAccountsRequest.md)|  | 
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

[**ListMemberAccountsResult**](ListMemberAccountsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listS3Resources

> ListS3ResourcesResult listS3Resources(xAmzTarget, listS3ResourcesRequest, opts)



(Discontinued) Lists all the S3 resources associated with Amazon Macie Classic. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action lists the S3 resources associated with Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action lists the S3 resources associated with Macie Classic for the specified member account. 

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listS3ResourcesRequest = new AmazonMacie.ListS3ResourcesRequest(); // ListS3ResourcesRequest | 
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
apiInstance.listS3Resources(xAmzTarget, listS3ResourcesRequest, opts, (error, data, response) => {
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
 **listS3ResourcesRequest** | [**ListS3ResourcesRequest**](ListS3ResourcesRequest.md)|  | 
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

[**ListS3ResourcesResult**](ListS3ResourcesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateS3Resources

> UpdateS3ResourcesResult updateS3Resources(xAmzTarget, updateS3ResourcesRequest, opts)



(Discontinued) Updates the classification types for the specified S3 resources. If &lt;code&gt;memberAccountId&lt;/code&gt; isn&#39;t specified, the action updates the classification types of the S3 resources associated with Amazon Macie Classic for the current Macie Classic administrator account. If &lt;code&gt;memberAccountId&lt;/code&gt; is specified, the action updates the classification types of the S3 resources associated with Macie Classic for the specified member account.

### Example

```javascript
import AmazonMacie from 'amazon_macie';
let defaultClient = AmazonMacie.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonMacie.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateS3ResourcesRequest = new AmazonMacie.UpdateS3ResourcesRequest(); // UpdateS3ResourcesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateS3Resources(xAmzTarget, updateS3ResourcesRequest, opts, (error, data, response) => {
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
 **updateS3ResourcesRequest** | [**UpdateS3ResourcesRequest**](UpdateS3ResourcesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateS3ResourcesResult**](UpdateS3ResourcesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

