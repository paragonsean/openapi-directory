# AmazonCloudHsm.DefaultApi

All URIs are relative to *http://cloudhsm.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTagsToResource**](DefaultApi.md#addTagsToResource) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.AddTagsToResource | 
[**createHapg**](DefaultApi.md#createHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.CreateHapg | 
[**createHsm**](DefaultApi.md#createHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.CreateHsm | 
[**createLunaClient**](DefaultApi.md#createLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.CreateLunaClient | 
[**deleteHapg**](DefaultApi.md#deleteHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DeleteHapg | 
[**deleteHsm**](DefaultApi.md#deleteHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DeleteHsm | 
[**deleteLunaClient**](DefaultApi.md#deleteLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DeleteLunaClient | 
[**describeHapg**](DefaultApi.md#describeHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DescribeHapg | 
[**describeHsm**](DefaultApi.md#describeHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DescribeHsm | 
[**describeLunaClient**](DefaultApi.md#describeLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.DescribeLunaClient | 
[**getConfig**](DefaultApi.md#getConfig) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.GetConfig | 
[**listAvailableZones**](DefaultApi.md#listAvailableZones) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListAvailableZones | 
[**listHapgs**](DefaultApi.md#listHapgs) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListHapgs | 
[**listHsms**](DefaultApi.md#listHsms) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListHsms | 
[**listLunaClients**](DefaultApi.md#listLunaClients) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListLunaClients | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ListTagsForResource | 
[**modifyHapg**](DefaultApi.md#modifyHapg) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ModifyHapg | 
[**modifyHsm**](DefaultApi.md#modifyHsm) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ModifyHsm | 
[**modifyLunaClient**](DefaultApi.md#modifyLunaClient) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.ModifyLunaClient | 
[**removeTagsFromResource**](DefaultApi.md#removeTagsFromResource) | **POST** /#X-Amz-Target&#x3D;CloudHsmFrontendService.RemoveTagsFromResource | 



## addTagsToResource

> AddTagsToResourceResponse addTagsToResource(xAmzTarget, addTagsToResourceRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Adds or overwrites one or more tags for the specified AWS CloudHSM resource.&lt;/p&gt; &lt;p&gt;Each tag consists of a key and a value. Tag keys must be unique to each resource.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let addTagsToResourceRequest = new AmazonCloudHsm.AddTagsToResourceRequest(); // AddTagsToResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addTagsToResource(xAmzTarget, addTagsToResourceRequest, opts, (error, data, response) => {
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
 **addTagsToResourceRequest** | [**AddTagsToResourceRequest**](AddTagsToResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddTagsToResourceResponse**](AddTagsToResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHapg

> CreateHapgResponse createHapg(xAmzTarget, createHapgRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates a high-availability partition group. A high-availability partition group is a group of partitions that spans multiple physical HSMs.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createHapgRequest = new AmazonCloudHsm.CreateHapgRequest(); // CreateHapgRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createHapg(xAmzTarget, createHapgRequest, opts, (error, data, response) => {
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
 **createHapgRequest** | [**CreateHapgRequest**](CreateHapgRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateHapgResponse**](CreateHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createHsm

> CreateHsmResponse createHsm(xAmzTarget, createHsmRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates an uninitialized HSM instance.&lt;/p&gt; &lt;p&gt;There is an upfront fee charged for each HSM instance that you create with the &lt;code&gt;CreateHsm&lt;/code&gt; operation. If you accidentally provision an HSM and want to request a refund, delete the instance using the &lt;a&gt;DeleteHsm&lt;/a&gt; operation, go to the &lt;a href&#x3D;\&quot;https://console.aws.amazon.com/support/home\&quot;&gt;AWS Support Center&lt;/a&gt;, create a new case, and select &lt;b&gt;Account and Billing Support&lt;/b&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;It can take up to 20 minutes to create and provision an HSM. You can monitor the status of the HSM with the &lt;a&gt;DescribeHsm&lt;/a&gt; operation. The HSM is ready to be initialized when the status changes to &lt;code&gt;RUNNING&lt;/code&gt;.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createHsmRequest = new AmazonCloudHsm.CreateHsmRequest(); // CreateHsmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createHsm(xAmzTarget, createHsmRequest, opts, (error, data, response) => {
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
 **createHsmRequest** | [**CreateHsmRequest**](CreateHsmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateHsmResponse**](CreateHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLunaClient

> CreateLunaClientResponse createLunaClient(xAmzTarget, createLunaClientRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Creates an HSM client.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createLunaClientRequest = new AmazonCloudHsm.CreateLunaClientRequest(); // CreateLunaClientRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLunaClient(xAmzTarget, createLunaClientRequest, opts, (error, data, response) => {
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
 **createLunaClientRequest** | [**CreateLunaClientRequest**](CreateLunaClientRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLunaClientResponse**](CreateLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteHapg

> DeleteHapgResponse deleteHapg(xAmzTarget, deleteHapgRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes a high-availability partition group.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteHapgRequest = new AmazonCloudHsm.DeleteHapgRequest(); // DeleteHapgRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteHapg(xAmzTarget, deleteHapgRequest, opts, (error, data, response) => {
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
 **deleteHapgRequest** | [**DeleteHapgRequest**](DeleteHapgRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteHapgResponse**](DeleteHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteHsm

> DeleteHsmResponse deleteHsm(xAmzTarget, deleteHsmRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes an HSM. After completion, this operation cannot be undone and your key material cannot be recovered.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteHsmRequest = new AmazonCloudHsm.DeleteHsmRequest(); // DeleteHsmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteHsm(xAmzTarget, deleteHsmRequest, opts, (error, data, response) => {
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
 **deleteHsmRequest** | [**DeleteHsmRequest**](DeleteHsmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteHsmResponse**](DeleteHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteLunaClient

> DeleteLunaClientResponse deleteLunaClient(xAmzTarget, deleteLunaClientRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Deletes a client.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteLunaClientRequest = new AmazonCloudHsm.DeleteLunaClientRequest(); // DeleteLunaClientRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteLunaClient(xAmzTarget, deleteLunaClientRequest, opts, (error, data, response) => {
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
 **deleteLunaClientRequest** | [**DeleteLunaClientRequest**](DeleteLunaClientRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteLunaClientResponse**](DeleteLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeHapg

> DescribeHapgResponse describeHapg(xAmzTarget, describeHapgRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about a high-availability partition group.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeHapgRequest = new AmazonCloudHsm.DescribeHapgRequest(); // DescribeHapgRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeHapg(xAmzTarget, describeHapgRequest, opts, (error, data, response) => {
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
 **describeHapgRequest** | [**DescribeHapgRequest**](DescribeHapgRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeHapgResponse**](DescribeHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeHsm

> DescribeHsmResponse describeHsm(xAmzTarget, describeHsmRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about an HSM. You can identify the HSM by its ARN or its serial number.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeHsmRequest = new AmazonCloudHsm.DescribeHsmRequest(); // DescribeHsmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeHsm(xAmzTarget, describeHsmRequest, opts, (error, data, response) => {
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
 **describeHsmRequest** | [**DescribeHsmRequest**](DescribeHsmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeHsmResponse**](DescribeHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeLunaClient

> DescribeLunaClientResponse describeLunaClient(xAmzTarget, describeLunaClientRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves information about an HSM client.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeLunaClientRequest = new AmazonCloudHsm.DescribeLunaClientRequest(); // DescribeLunaClientRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeLunaClient(xAmzTarget, describeLunaClientRequest, opts, (error, data, response) => {
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
 **describeLunaClientRequest** | [**DescribeLunaClientRequest**](DescribeLunaClientRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeLunaClientResponse**](DescribeLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getConfig

> GetConfigResponse getConfig(xAmzTarget, getConfigRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Gets the configuration files necessary to connect to all high availability partition groups the client is associated with.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getConfigRequest = new AmazonCloudHsm.GetConfigRequest(); // GetConfigRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfig(xAmzTarget, getConfigRequest, opts, (error, data, response) => {
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
 **getConfigRequest** | [**GetConfigRequest**](GetConfigRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConfigResponse**](GetConfigResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listAvailableZones

> ListAvailableZonesResponse listAvailableZones(xAmzTarget, body, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists the Availability Zones that have available AWS CloudHSM capacity.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let body = {key: null}; // Object | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listAvailableZones(xAmzTarget, body, opts, (error, data, response) => {
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
 **body** | **Object**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListAvailableZonesResponse**](ListAvailableZonesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listHapgs

> ListHapgsResponse listHapgs(xAmzTarget, listHapgsRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists the high-availability partition groups for the account.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListHapgs&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listHapgsRequest = new AmazonCloudHsm.ListHapgsRequest(); // ListHapgsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listHapgs(xAmzTarget, listHapgsRequest, opts, (error, data, response) => {
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
 **listHapgsRequest** | [**ListHapgsRequest**](ListHapgsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListHapgsResponse**](ListHapgsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listHsms

> ListHsmsResponse listHsms(xAmzTarget, listHsmsRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Retrieves the identifiers of all of the HSMs provisioned for the current customer.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListHsms&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listHsmsRequest = new AmazonCloudHsm.ListHsmsRequest(); // ListHsmsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listHsms(xAmzTarget, listHsmsRequest, opts, (error, data, response) => {
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
 **listHsmsRequest** | [**ListHsmsRequest**](ListHsmsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListHsmsResponse**](ListHsmsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLunaClients

> ListLunaClientsResponse listLunaClients(xAmzTarget, listLunaClientsRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Lists all of the clients.&lt;/p&gt; &lt;p&gt;This operation supports pagination with the use of the &lt;code&gt;NextToken&lt;/code&gt; member. If more results are available, the &lt;code&gt;NextToken&lt;/code&gt; member of the response contains a token that you pass in the next call to &lt;code&gt;ListLunaClients&lt;/code&gt; to retrieve the next set of items.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listLunaClientsRequest = new AmazonCloudHsm.ListLunaClientsRequest(); // ListLunaClientsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listLunaClients(xAmzTarget, listLunaClientsRequest, opts, (error, data, response) => {
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
 **listLunaClientsRequest** | [**ListLunaClientsRequest**](ListLunaClientsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListLunaClientsResponse**](ListLunaClientsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Returns a list of all tags for the specified AWS CloudHSM resource.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AmazonCloudHsm.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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


## modifyHapg

> ModifyHapgResponse modifyHapg(xAmzTarget, modifyHapgRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies an existing high-availability partition group.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let modifyHapgRequest = new AmazonCloudHsm.ModifyHapgRequest(); // ModifyHapgRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.modifyHapg(xAmzTarget, modifyHapgRequest, opts, (error, data, response) => {
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
 **modifyHapgRequest** | [**ModifyHapgRequest**](ModifyHapgRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ModifyHapgResponse**](ModifyHapgResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modifyHsm

> ModifyHsmResponse modifyHsm(xAmzTarget, modifyHsmRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies an HSM.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This operation can result in the HSM being offline for up to 15 minutes while the AWS CloudHSM service is reconfigured. If you are modifying a production HSM, you should ensure that your AWS CloudHSM service is configured for high availability, and consider executing this operation during a maintenance window.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let modifyHsmRequest = new AmazonCloudHsm.ModifyHsmRequest(); // ModifyHsmRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.modifyHsm(xAmzTarget, modifyHsmRequest, opts, (error, data, response) => {
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
 **modifyHsmRequest** | [**ModifyHsmRequest**](ModifyHsmRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ModifyHsmResponse**](ModifyHsmResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## modifyLunaClient

> ModifyLunaClientResponse modifyLunaClient(xAmzTarget, modifyLunaClientRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Modifies the certificate used by the client.&lt;/p&gt; &lt;p&gt;This action can potentially start a workflow to install the new certificate on the client&#39;s HSMs.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let modifyLunaClientRequest = new AmazonCloudHsm.ModifyLunaClientRequest(); // ModifyLunaClientRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.modifyLunaClient(xAmzTarget, modifyLunaClientRequest, opts, (error, data, response) => {
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
 **modifyLunaClientRequest** | [**ModifyLunaClientRequest**](ModifyLunaClientRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ModifyLunaClientResponse**](ModifyLunaClientResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeTagsFromResource

> RemoveTagsFromResourceResponse removeTagsFromResource(xAmzTarget, removeTagsFromResourceRequest, opts)



&lt;p&gt;This is documentation for &lt;b&gt;AWS CloudHSM Classic&lt;/b&gt;. For more information, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/faqs-classic/\&quot;&gt;AWS CloudHSM Classic FAQs&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/userguide/\&quot;&gt;AWS CloudHSM Classic User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/classic/APIReference/\&quot;&gt;AWS CloudHSM Classic API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;b&gt;For information about the current version of AWS CloudHSM&lt;/b&gt;, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/cloudhsm/\&quot;&gt;AWS CloudHSM&lt;/a&gt;, the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/userguide/\&quot;&gt;AWS CloudHSM User Guide&lt;/a&gt;, and the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/cloudhsm/latest/APIReference/\&quot;&gt;AWS CloudHSM API Reference&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Removes one or more tags from the specified AWS CloudHSM resource.&lt;/p&gt; &lt;p&gt;To remove a tag, specify only the tag key to remove (not the value). To overwrite the value for an existing tag, use &lt;a&gt;AddTagsToResource&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonCloudHsm from 'amazon_cloud_hsm';
let defaultClient = AmazonCloudHsm.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonCloudHsm.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let removeTagsFromResourceRequest = new AmazonCloudHsm.RemoveTagsFromResourceRequest(); // RemoveTagsFromResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeTagsFromResource(xAmzTarget, removeTagsFromResourceRequest, opts, (error, data, response) => {
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
 **removeTagsFromResourceRequest** | [**RemoveTagsFromResourceRequest**](RemoveTagsFromResourceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveTagsFromResourceResponse**](RemoveTagsFromResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

