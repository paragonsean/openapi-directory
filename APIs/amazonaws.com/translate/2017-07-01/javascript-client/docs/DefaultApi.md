# AmazonTranslate.DefaultApi

All URIs are relative to *http://translate.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createParallelData**](DefaultApi.md#createParallelData) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.CreateParallelData | 
[**deleteParallelData**](DefaultApi.md#deleteParallelData) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.DeleteParallelData | 
[**deleteTerminology**](DefaultApi.md#deleteTerminology) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.DeleteTerminology | 
[**describeTextTranslationJob**](DefaultApi.md#describeTextTranslationJob) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.DescribeTextTranslationJob | 
[**getParallelData**](DefaultApi.md#getParallelData) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.GetParallelData | 
[**getTerminology**](DefaultApi.md#getTerminology) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.GetTerminology | 
[**importTerminology**](DefaultApi.md#importTerminology) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.ImportTerminology | 
[**listLanguages**](DefaultApi.md#listLanguages) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.ListLanguages | 
[**listParallelData**](DefaultApi.md#listParallelData) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.ListParallelData | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.ListTagsForResource | 
[**listTerminologies**](DefaultApi.md#listTerminologies) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.ListTerminologies | 
[**listTextTranslationJobs**](DefaultApi.md#listTextTranslationJobs) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.ListTextTranslationJobs | 
[**startTextTranslationJob**](DefaultApi.md#startTextTranslationJob) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.StartTextTranslationJob | 
[**stopTextTranslationJob**](DefaultApi.md#stopTextTranslationJob) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.StopTextTranslationJob | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.TagResource | 
[**translateDocument**](DefaultApi.md#translateDocument) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.TranslateDocument | 
[**translateText**](DefaultApi.md#translateText) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.TranslateText | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.UntagResource | 
[**updateParallelData**](DefaultApi.md#updateParallelData) | **POST** /#X-Amz-Target&#x3D;AWSShineFrontendService_20170701.UpdateParallelData | 



## createParallelData

> CreateParallelDataResponse createParallelData(xAmzTarget, createParallelDataRequest, opts)



Creates a parallel data resource in Amazon Translate by importing an input file from Amazon S3. Parallel data files contain examples that show how you want segments of text to be translated. By adding parallel data, you can influence the style, tone, and word choice in your translation output.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createParallelDataRequest = new AmazonTranslate.CreateParallelDataRequest(); // CreateParallelDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createParallelData(xAmzTarget, createParallelDataRequest, opts, (error, data, response) => {
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
 **createParallelDataRequest** | [**CreateParallelDataRequest**](CreateParallelDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateParallelDataResponse**](CreateParallelDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteParallelData

> DeleteParallelDataResponse deleteParallelData(xAmzTarget, deleteParallelDataRequest, opts)



Deletes a parallel data resource in Amazon Translate.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteParallelDataRequest = new AmazonTranslate.DeleteParallelDataRequest(); // DeleteParallelDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteParallelData(xAmzTarget, deleteParallelDataRequest, opts, (error, data, response) => {
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
 **deleteParallelDataRequest** | [**DeleteParallelDataRequest**](DeleteParallelDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteParallelDataResponse**](DeleteParallelDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteTerminology

> deleteTerminology(xAmzTarget, deleteTerminologyRequest, opts)



A synchronous action that deletes a custom terminology.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteTerminologyRequest = new AmazonTranslate.DeleteTerminologyRequest(); // DeleteTerminologyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTerminology(xAmzTarget, deleteTerminologyRequest, opts, (error, data, response) => {
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
 **deleteTerminologyRequest** | [**DeleteTerminologyRequest**](DeleteTerminologyRequest.md)|  | 
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


## describeTextTranslationJob

> DescribeTextTranslationJobResponse describeTextTranslationJob(xAmzTarget, describeTextTranslationJobRequest, opts)



Gets the properties associated with an asynchronous batch translation job including name, ID, status, source and target languages, input/output S3 buckets, and so on.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeTextTranslationJobRequest = new AmazonTranslate.DescribeTextTranslationJobRequest(); // DescribeTextTranslationJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeTextTranslationJob(xAmzTarget, describeTextTranslationJobRequest, opts, (error, data, response) => {
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
 **describeTextTranslationJobRequest** | [**DescribeTextTranslationJobRequest**](DescribeTextTranslationJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeTextTranslationJobResponse**](DescribeTextTranslationJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getParallelData

> GetParallelDataResponse getParallelData(xAmzTarget, getParallelDataRequest, opts)



Provides information about a parallel data resource.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getParallelDataRequest = new AmazonTranslate.GetParallelDataRequest(); // GetParallelDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getParallelData(xAmzTarget, getParallelDataRequest, opts, (error, data, response) => {
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
 **getParallelDataRequest** | [**GetParallelDataRequest**](GetParallelDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetParallelDataResponse**](GetParallelDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getTerminology

> GetTerminologyResponse getTerminology(xAmzTarget, getTerminologyRequest, opts)



Retrieves a custom terminology.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getTerminologyRequest = new AmazonTranslate.GetTerminologyRequest(); // GetTerminologyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getTerminology(xAmzTarget, getTerminologyRequest, opts, (error, data, response) => {
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
 **getTerminologyRequest** | [**GetTerminologyRequest**](GetTerminologyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetTerminologyResponse**](GetTerminologyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## importTerminology

> ImportTerminologyResponse importTerminology(xAmzTarget, importTerminologyRequest, opts)



&lt;p&gt;Creates or updates a custom terminology, depending on whether one already exists for the given terminology name. Importing a terminology with the same name as an existing one will merge the terminologies based on the chosen merge strategy. The only supported merge strategy is OVERWRITE, where the imported terminology overwrites the existing terminology of the same name.&lt;/p&gt; &lt;p&gt;If you import a terminology that overwrites an existing one, the new terminology takes up to 10 minutes to fully propagate. After that, translations have access to the new terminology.&lt;/p&gt;

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let importTerminologyRequest = new AmazonTranslate.ImportTerminologyRequest(); // ImportTerminologyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.importTerminology(xAmzTarget, importTerminologyRequest, opts, (error, data, response) => {
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
 **importTerminologyRequest** | [**ImportTerminologyRequest**](ImportTerminologyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ImportTerminologyResponse**](ImportTerminologyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLanguages

> ListLanguagesResponse listLanguages(xAmzTarget, listLanguagesRequest, opts)



Provides a list of languages (RFC-5646 codes and names) that Amazon Translate supports.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listLanguagesRequest = new AmazonTranslate.ListLanguagesRequest(); // ListLanguagesRequest | 
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
apiInstance.listLanguages(xAmzTarget, listLanguagesRequest, opts, (error, data, response) => {
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
 **listLanguagesRequest** | [**ListLanguagesRequest**](ListLanguagesRequest.md)|  | 
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

[**ListLanguagesResponse**](ListLanguagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listParallelData

> ListParallelDataResponse listParallelData(xAmzTarget, listParallelDataRequest, opts)



Provides a list of your parallel data resources in Amazon Translate.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listParallelDataRequest = new AmazonTranslate.ListParallelDataRequest(); // ListParallelDataRequest | 
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
apiInstance.listParallelData(xAmzTarget, listParallelDataRequest, opts, (error, data, response) => {
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
 **listParallelDataRequest** | [**ListParallelDataRequest**](ListParallelDataRequest.md)|  | 
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

[**ListParallelDataResponse**](ListParallelDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Lists all tags associated with a given Amazon Translate resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/translate/latest/dg/tagging.html\&quot;&gt; Tagging your resources&lt;/a&gt;.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AmazonTranslate.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts, (error, data, response) => {
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
 **listTagsForResourceRequest** | [**ListTagsForResourceRequest**](ListTagsForResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceResponse**](ListTagsForResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTerminologies

> ListTerminologiesResponse listTerminologies(xAmzTarget, listTerminologiesRequest, opts)



Provides a list of custom terminologies associated with your account.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTerminologiesRequest = new AmazonTranslate.ListTerminologiesRequest(); // ListTerminologiesRequest | 
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
apiInstance.listTerminologies(xAmzTarget, listTerminologiesRequest, opts, (error, data, response) => {
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
 **listTerminologiesRequest** | [**ListTerminologiesRequest**](ListTerminologiesRequest.md)|  | 
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

[**ListTerminologiesResponse**](ListTerminologiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTextTranslationJobs

> ListTextTranslationJobsResponse listTextTranslationJobs(xAmzTarget, listTextTranslationJobsRequest, opts)



Gets a list of the batch translation jobs that you have submitted.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTextTranslationJobsRequest = new AmazonTranslate.ListTextTranslationJobsRequest(); // ListTextTranslationJobsRequest | 
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
apiInstance.listTextTranslationJobs(xAmzTarget, listTextTranslationJobsRequest, opts, (error, data, response) => {
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
 **listTextTranslationJobsRequest** | [**ListTextTranslationJobsRequest**](ListTextTranslationJobsRequest.md)|  | 
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

[**ListTextTranslationJobsResponse**](ListTextTranslationJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## startTextTranslationJob

> StartTextTranslationJobResponse startTextTranslationJob(xAmzTarget, startTextTranslationJobRequest, opts)



&lt;p&gt;Starts an asynchronous batch translation job. Use batch translation jobs to translate large volumes of text across multiple documents at once. For batch translation, you can input documents with different source languages (specify &lt;code&gt;auto&lt;/code&gt; as the source language). You can specify one or more target languages. Batch translation translates each input document into each of the target languages. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/translate/latest/dg/async.html\&quot;&gt;Asynchronous batch processing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Batch translation jobs can be described with the &lt;a&gt;DescribeTextTranslationJob&lt;/a&gt; operation, listed with the &lt;a&gt;ListTextTranslationJobs&lt;/a&gt; operation, and stopped with the &lt;a&gt;StopTextTranslationJob&lt;/a&gt; operation.&lt;/p&gt;

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startTextTranslationJobRequest = new AmazonTranslate.StartTextTranslationJobRequest(); // StartTextTranslationJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startTextTranslationJob(xAmzTarget, startTextTranslationJobRequest, opts, (error, data, response) => {
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
 **startTextTranslationJobRequest** | [**StartTextTranslationJobRequest**](StartTextTranslationJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartTextTranslationJobResponse**](StartTextTranslationJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopTextTranslationJob

> StopTextTranslationJobResponse stopTextTranslationJob(xAmzTarget, stopTextTranslationJobRequest, opts)



&lt;p&gt;Stops an asynchronous batch translation job that is in progress.&lt;/p&gt; &lt;p&gt;If the job&#39;s state is &lt;code&gt;IN_PROGRESS&lt;/code&gt;, the job will be marked for termination and put into the &lt;code&gt;STOP_REQUESTED&lt;/code&gt; state. If the job completes before it can be stopped, it is put into the &lt;code&gt;COMPLETED&lt;/code&gt; state. Otherwise, the job is put into the &lt;code&gt;STOPPED&lt;/code&gt; state.&lt;/p&gt; &lt;p&gt;Asynchronous batch translation jobs are started with the &lt;a&gt;StartTextTranslationJob&lt;/a&gt; operation. You can use the &lt;a&gt;DescribeTextTranslationJob&lt;/a&gt; or &lt;a&gt;ListTextTranslationJobs&lt;/a&gt; operations to get a batch translation job&#39;s &lt;code&gt;JobId&lt;/code&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopTextTranslationJobRequest = new AmazonTranslate.StopTextTranslationJobRequest(); // StopTextTranslationJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopTextTranslationJob(xAmzTarget, stopTextTranslationJobRequest, opts, (error, data, response) => {
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
 **stopTextTranslationJobRequest** | [**StopTextTranslationJobRequest**](StopTextTranslationJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopTextTranslationJobResponse**](StopTextTranslationJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Associates a specific tag with a resource. A tag is a key-value pair that adds as a metadata to a resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/translate/latest/dg/tagging.html\&quot;&gt; Tagging your resources&lt;/a&gt;.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AmazonTranslate.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(xAmzTarget, tagResourceRequest, opts, (error, data, response) => {
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
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## translateDocument

> TranslateDocumentResponse translateDocument(xAmzTarget, translateDocumentRequest, opts)



&lt;p&gt;Translates the input document from the source language to the target language. This synchronous operation supports plain text or HTML for the input document. &lt;code&gt;TranslateDocument&lt;/code&gt; supports translations from English to any supported language, and from any supported language to English. Therefore, specify either the source language code or the target language code as “en” (English). &lt;/p&gt; &lt;p&gt; &lt;code&gt;TranslateDocument&lt;/code&gt; does not support language auto-detection. &lt;/p&gt; &lt;p&gt; If you set the &lt;code&gt;Formality&lt;/code&gt; parameter, the request will fail if the target language does not support formality. For a list of target languages that support formality, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/translate/latest/dg/customizing-translations-formality.html\&quot;&gt;Setting formality&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let translateDocumentRequest = new AmazonTranslate.TranslateDocumentRequest(); // TranslateDocumentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.translateDocument(xAmzTarget, translateDocumentRequest, opts, (error, data, response) => {
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
 **translateDocumentRequest** | [**TranslateDocumentRequest**](TranslateDocumentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TranslateDocumentResponse**](TranslateDocumentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## translateText

> TranslateTextResponse translateText(xAmzTarget, translateTextRequest, opts)



Translates input text from the source language to the target language. For a list of available languages and language codes, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/translate/latest/dg/what-is-languages.html\&quot;&gt;Supported languages&lt;/a&gt;.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let translateTextRequest = new AmazonTranslate.TranslateTextRequest(); // TranslateTextRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.translateText(xAmzTarget, translateTextRequest, opts, (error, data, response) => {
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
 **translateTextRequest** | [**TranslateTextRequest**](TranslateTextRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TranslateTextResponse**](TranslateTextResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Removes a specific tag associated with an Amazon Translate resource. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/translate/latest/dg/tagging.html\&quot;&gt; Tagging your resources&lt;/a&gt;.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AmazonTranslate.UntagResourceRequest(); // UntagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(xAmzTarget, untagResourceRequest, opts, (error, data, response) => {
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
 **untagResourceRequest** | [**UntagResourceRequest**](UntagResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

**Object**

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateParallelData

> UpdateParallelDataResponse updateParallelData(xAmzTarget, updateParallelDataRequest, opts)



Updates a previously created parallel data resource by importing a new input file from Amazon S3.

### Example

```javascript
import AmazonTranslate from 'amazon_translate';
let defaultClient = AmazonTranslate.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonTranslate.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateParallelDataRequest = new AmazonTranslate.UpdateParallelDataRequest(); // UpdateParallelDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateParallelData(xAmzTarget, updateParallelDataRequest, opts, (error, data, response) => {
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
 **updateParallelDataRequest** | [**UpdateParallelDataRequest**](UpdateParallelDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateParallelDataResponse**](UpdateParallelDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

