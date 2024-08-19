# AmazonElasticContainerRegistryPublic.DefaultApi

All URIs are relative to *http://api.ecr-public.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchCheckLayerAvailability**](DefaultApi.md#batchCheckLayerAvailability) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.BatchCheckLayerAvailability | 
[**batchDeleteImage**](DefaultApi.md#batchDeleteImage) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.BatchDeleteImage | 
[**completeLayerUpload**](DefaultApi.md#completeLayerUpload) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.CompleteLayerUpload | 
[**createRepository**](DefaultApi.md#createRepository) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.CreateRepository | 
[**deleteRepository**](DefaultApi.md#deleteRepository) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.DeleteRepository | 
[**deleteRepositoryPolicy**](DefaultApi.md#deleteRepositoryPolicy) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.DeleteRepositoryPolicy | 
[**describeImageTags**](DefaultApi.md#describeImageTags) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.DescribeImageTags | 
[**describeImages**](DefaultApi.md#describeImages) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.DescribeImages | 
[**describeRegistries**](DefaultApi.md#describeRegistries) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.DescribeRegistries | 
[**describeRepositories**](DefaultApi.md#describeRepositories) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.DescribeRepositories | 
[**getAuthorizationToken**](DefaultApi.md#getAuthorizationToken) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.GetAuthorizationToken | 
[**getRegistryCatalogData**](DefaultApi.md#getRegistryCatalogData) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.GetRegistryCatalogData | 
[**getRepositoryCatalogData**](DefaultApi.md#getRepositoryCatalogData) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.GetRepositoryCatalogData | 
[**getRepositoryPolicy**](DefaultApi.md#getRepositoryPolicy) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.GetRepositoryPolicy | 
[**initiateLayerUpload**](DefaultApi.md#initiateLayerUpload) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.InitiateLayerUpload | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.ListTagsForResource | 
[**putImage**](DefaultApi.md#putImage) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.PutImage | 
[**putRegistryCatalogData**](DefaultApi.md#putRegistryCatalogData) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.PutRegistryCatalogData | 
[**putRepositoryCatalogData**](DefaultApi.md#putRepositoryCatalogData) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.PutRepositoryCatalogData | 
[**setRepositoryPolicy**](DefaultApi.md#setRepositoryPolicy) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.SetRepositoryPolicy | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.UntagResource | 
[**uploadLayerPart**](DefaultApi.md#uploadLayerPart) | **POST** /#X-Amz-Target&#x3D;SpencerFrontendService.UploadLayerPart | 



## batchCheckLayerAvailability

> BatchCheckLayerAvailabilityResponse batchCheckLayerAvailability(xAmzTarget, batchCheckLayerAvailabilityRequest, opts)



&lt;p&gt;Checks the availability of one or more image layers that are within a repository in a public registry. When an image is pushed to a repository, each image layer is checked to verify if it has been uploaded before. If it has been uploaded, then the image layer is skipped.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the &lt;code&gt;docker&lt;/code&gt; CLI to pull, tag, and push images.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchCheckLayerAvailabilityRequest = new AmazonElasticContainerRegistryPublic.BatchCheckLayerAvailabilityRequest(); // BatchCheckLayerAvailabilityRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchCheckLayerAvailability(xAmzTarget, batchCheckLayerAvailabilityRequest, opts, (error, data, response) => {
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
 **batchCheckLayerAvailabilityRequest** | [**BatchCheckLayerAvailabilityRequest**](BatchCheckLayerAvailabilityRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchCheckLayerAvailabilityResponse**](BatchCheckLayerAvailabilityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchDeleteImage

> BatchDeleteImageResponse batchDeleteImage(xAmzTarget, batchDeleteImageRequest, opts)



&lt;p&gt;Deletes a list of specified images that are within a repository in a public registry. Images are specified with either an &lt;code&gt;imageTag&lt;/code&gt; or &lt;code&gt;imageDigest&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;You can remove a tag from an image by specifying the image&#39;s tag in your request. When you remove the last tag from an image, the image is deleted from your repository.&lt;/p&gt; &lt;p&gt;You can completely delete an image (and all of its tags) by specifying the digest of the image in your request.&lt;/p&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let batchDeleteImageRequest = new AmazonElasticContainerRegistryPublic.BatchDeleteImageRequest(); // BatchDeleteImageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDeleteImage(xAmzTarget, batchDeleteImageRequest, opts, (error, data, response) => {
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
 **batchDeleteImageRequest** | [**BatchDeleteImageRequest**](BatchDeleteImageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteImageResponse**](BatchDeleteImageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## completeLayerUpload

> CompleteLayerUploadResponse completeLayerUpload(xAmzTarget, completeLayerUploadRequest, opts)



&lt;p&gt;Informs Amazon ECR that the image layer upload is complete for a specified public registry, repository name, and upload ID. You can optionally provide a &lt;code&gt;sha256&lt;/code&gt; digest of the image layer for data validation purposes.&lt;/p&gt; &lt;p&gt;When an image is pushed, the CompleteLayerUpload API is called once for each new image layer to verify that the upload is complete.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the &lt;code&gt;docker&lt;/code&gt; CLI to pull, tag, and push images.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let completeLayerUploadRequest = new AmazonElasticContainerRegistryPublic.CompleteLayerUploadRequest(); // CompleteLayerUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.completeLayerUpload(xAmzTarget, completeLayerUploadRequest, opts, (error, data, response) => {
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
 **completeLayerUploadRequest** | [**CompleteLayerUploadRequest**](CompleteLayerUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CompleteLayerUploadResponse**](CompleteLayerUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRepository

> CreateRepositoryResponse createRepository(xAmzTarget, createRepositoryRequest, opts)



Creates a repository in a public registry. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html\&quot;&gt;Amazon ECR repositories&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Registry User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createRepositoryRequest = new AmazonElasticContainerRegistryPublic.CreateRepositoryRequest(); // CreateRepositoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRepository(xAmzTarget, createRepositoryRequest, opts, (error, data, response) => {
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
 **createRepositoryRequest** | [**CreateRepositoryRequest**](CreateRepositoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRepositoryResponse**](CreateRepositoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRepository

> DeleteRepositoryResponse deleteRepository(xAmzTarget, deleteRepositoryRequest, opts)



Deletes a repository in a public registry. If the repository contains images, you must either manually delete all images in the repository or use the &lt;code&gt;force&lt;/code&gt; option. This option deletes all images on your behalf before deleting the repository.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteRepositoryRequest = new AmazonElasticContainerRegistryPublic.DeleteRepositoryRequest(); // DeleteRepositoryRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRepository(xAmzTarget, deleteRepositoryRequest, opts, (error, data, response) => {
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
 **deleteRepositoryRequest** | [**DeleteRepositoryRequest**](DeleteRepositoryRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRepositoryResponse**](DeleteRepositoryResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteRepositoryPolicy

> DeleteRepositoryPolicyResponse deleteRepositoryPolicy(xAmzTarget, deleteRepositoryPolicyRequest, opts)



Deletes the repository policy that&#39;s associated with the specified repository.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteRepositoryPolicyRequest = new AmazonElasticContainerRegistryPublic.DeleteRepositoryPolicyRequest(); // DeleteRepositoryPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRepositoryPolicy(xAmzTarget, deleteRepositoryPolicyRequest, opts, (error, data, response) => {
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
 **deleteRepositoryPolicyRequest** | [**DeleteRepositoryPolicyRequest**](DeleteRepositoryPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRepositoryPolicyResponse**](DeleteRepositoryPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeImageTags

> DescribeImageTagsResponse describeImageTags(xAmzTarget, describeImageTagsRequest, opts)



Returns the image tag details for a repository in a public registry.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeImageTagsRequest = new AmazonElasticContainerRegistryPublic.DescribeImageTagsRequest(); // DescribeImageTagsRequest | 
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
apiInstance.describeImageTags(xAmzTarget, describeImageTagsRequest, opts, (error, data, response) => {
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
 **describeImageTagsRequest** | [**DescribeImageTagsRequest**](DescribeImageTagsRequest.md)|  | 
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

[**DescribeImageTagsResponse**](DescribeImageTagsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeImages

> DescribeImagesResponse describeImages(xAmzTarget, describeImagesRequest, opts)



&lt;p&gt;Returns metadata that&#39;s related to the images in a repository in a public registry.&lt;/p&gt; &lt;note&gt; &lt;p&gt;Beginning with Docker version 1.9, the Docker client compresses image layers before pushing them to a V2 Docker registry. The output of the &lt;code&gt;docker images&lt;/code&gt; command shows the uncompressed image size. Therefore, it might return a larger image size than the image sizes that are returned by &lt;a&gt;DescribeImages&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeImagesRequest = new AmazonElasticContainerRegistryPublic.DescribeImagesRequest(); // DescribeImagesRequest | 
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
apiInstance.describeImages(xAmzTarget, describeImagesRequest, opts, (error, data, response) => {
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
 **describeImagesRequest** | [**DescribeImagesRequest**](DescribeImagesRequest.md)|  | 
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

[**DescribeImagesResponse**](DescribeImagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeRegistries

> DescribeRegistriesResponse describeRegistries(xAmzTarget, describeRegistriesRequest, opts)



Returns details for a public registry.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeRegistriesRequest = new AmazonElasticContainerRegistryPublic.DescribeRegistriesRequest(); // DescribeRegistriesRequest | 
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
apiInstance.describeRegistries(xAmzTarget, describeRegistriesRequest, opts, (error, data, response) => {
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
 **describeRegistriesRequest** | [**DescribeRegistriesRequest**](DescribeRegistriesRequest.md)|  | 
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

[**DescribeRegistriesResponse**](DescribeRegistriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeRepositories

> DescribeRepositoriesResponse describeRepositories(xAmzTarget, describeRepositoriesRequest, opts)



Describes repositories that are in a public registry.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeRepositoriesRequest = new AmazonElasticContainerRegistryPublic.DescribeRepositoriesRequest(); // DescribeRepositoriesRequest | 
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
apiInstance.describeRepositories(xAmzTarget, describeRepositoriesRequest, opts, (error, data, response) => {
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
 **describeRepositoriesRequest** | [**DescribeRepositoriesRequest**](DescribeRepositoriesRequest.md)|  | 
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

[**DescribeRepositoriesResponse**](DescribeRepositoriesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getAuthorizationToken

> GetAuthorizationTokenResponse getAuthorizationToken(xAmzTarget, body, opts)



Retrieves an authorization token. An authorization token represents your IAM authentication credentials. You can use it to access any Amazon ECR registry that your IAM principal has access to. The authorization token is valid for 12 hours. This API requires the &lt;code&gt;ecr-public:GetAuthorizationToken&lt;/code&gt; and &lt;code&gt;sts:GetServiceBearerToken&lt;/code&gt; permissions.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
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
apiInstance.getAuthorizationToken(xAmzTarget, body, opts, (error, data, response) => {
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

[**GetAuthorizationTokenResponse**](GetAuthorizationTokenResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRegistryCatalogData

> GetRegistryCatalogDataResponse getRegistryCatalogData(xAmzTarget, body, opts)



Retrieves catalog metadata for a public registry.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
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
apiInstance.getRegistryCatalogData(xAmzTarget, body, opts, (error, data, response) => {
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

[**GetRegistryCatalogDataResponse**](GetRegistryCatalogDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRepositoryCatalogData

> GetRepositoryCatalogDataResponse getRepositoryCatalogData(xAmzTarget, getRepositoryCatalogDataRequest, opts)



Retrieve catalog metadata for a repository in a public registry. This metadata is displayed publicly in the Amazon ECR Public Gallery.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getRepositoryCatalogDataRequest = new AmazonElasticContainerRegistryPublic.GetRepositoryCatalogDataRequest(); // GetRepositoryCatalogDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRepositoryCatalogData(xAmzTarget, getRepositoryCatalogDataRequest, opts, (error, data, response) => {
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
 **getRepositoryCatalogDataRequest** | [**GetRepositoryCatalogDataRequest**](GetRepositoryCatalogDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRepositoryCatalogDataResponse**](GetRepositoryCatalogDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRepositoryPolicy

> GetRepositoryPolicyResponse getRepositoryPolicy(xAmzTarget, getRepositoryPolicyRequest, opts)



Retrieves the repository policy for the specified repository.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getRepositoryPolicyRequest = new AmazonElasticContainerRegistryPublic.GetRepositoryPolicyRequest(); // GetRepositoryPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRepositoryPolicy(xAmzTarget, getRepositoryPolicyRequest, opts, (error, data, response) => {
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
 **getRepositoryPolicyRequest** | [**GetRepositoryPolicyRequest**](GetRepositoryPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRepositoryPolicyResponse**](GetRepositoryPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## initiateLayerUpload

> InitiateLayerUploadResponse initiateLayerUpload(xAmzTarget, initiateLayerUploadRequest, opts)



&lt;p&gt;Notifies Amazon ECR that you intend to upload an image layer.&lt;/p&gt; &lt;p&gt;When an image is pushed, the InitiateLayerUpload API is called once for each image layer that hasn&#39;t already been uploaded. Whether an image layer uploads is determined by the BatchCheckLayerAvailability API action.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the &lt;code&gt;docker&lt;/code&gt; CLI to pull, tag, and push images.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let initiateLayerUploadRequest = new AmazonElasticContainerRegistryPublic.InitiateLayerUploadRequest(); // InitiateLayerUploadRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.initiateLayerUpload(xAmzTarget, initiateLayerUploadRequest, opts, (error, data, response) => {
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
 **initiateLayerUploadRequest** | [**InitiateLayerUploadRequest**](InitiateLayerUploadRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InitiateLayerUploadResponse**](InitiateLayerUploadResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



List the tags for an Amazon ECR Public resource.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AmazonElasticContainerRegistryPublic.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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


## putImage

> PutImageResponse putImage(xAmzTarget, putImageRequest, opts)



&lt;p&gt;Creates or updates the image manifest and tags that are associated with an image.&lt;/p&gt; &lt;p&gt;When an image is pushed and all new image layers have been uploaded, the PutImage API is called once to create or update the image manifest and the tags that are associated with the image.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the &lt;code&gt;docker&lt;/code&gt; CLI to pull, tag, and push images.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putImageRequest = new AmazonElasticContainerRegistryPublic.PutImageRequest(); // PutImageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putImage(xAmzTarget, putImageRequest, opts, (error, data, response) => {
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
 **putImageRequest** | [**PutImageRequest**](PutImageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutImageResponse**](PutImageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putRegistryCatalogData

> PutRegistryCatalogDataResponse putRegistryCatalogData(xAmzTarget, putRegistryCatalogDataRequest, opts)



Create or update the catalog data for a public registry.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putRegistryCatalogDataRequest = new AmazonElasticContainerRegistryPublic.PutRegistryCatalogDataRequest(); // PutRegistryCatalogDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRegistryCatalogData(xAmzTarget, putRegistryCatalogDataRequest, opts, (error, data, response) => {
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
 **putRegistryCatalogDataRequest** | [**PutRegistryCatalogDataRequest**](PutRegistryCatalogDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutRegistryCatalogDataResponse**](PutRegistryCatalogDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putRepositoryCatalogData

> PutRepositoryCatalogDataResponse putRepositoryCatalogData(xAmzTarget, putRepositoryCatalogDataRequest, opts)



Creates or updates the catalog data for a repository in a public registry.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putRepositoryCatalogDataRequest = new AmazonElasticContainerRegistryPublic.PutRepositoryCatalogDataRequest(); // PutRepositoryCatalogDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putRepositoryCatalogData(xAmzTarget, putRepositoryCatalogDataRequest, opts, (error, data, response) => {
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
 **putRepositoryCatalogDataRequest** | [**PutRepositoryCatalogDataRequest**](PutRepositoryCatalogDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutRepositoryCatalogDataResponse**](PutRepositoryCatalogDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## setRepositoryPolicy

> SetRepositoryPolicyResponse setRepositoryPolicy(xAmzTarget, setRepositoryPolicyRequest, opts)



Applies a repository policy to the specified public repository to control access permissions. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html\&quot;&gt;Amazon ECR Repository Policies&lt;/a&gt; in the &lt;i&gt;Amazon Elastic Container Registry User Guide&lt;/i&gt;.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let setRepositoryPolicyRequest = new AmazonElasticContainerRegistryPublic.SetRepositoryPolicyRequest(); // SetRepositoryPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.setRepositoryPolicy(xAmzTarget, setRepositoryPolicyRequest, opts, (error, data, response) => {
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
 **setRepositoryPolicyRequest** | [**SetRepositoryPolicyRequest**](SetRepositoryPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SetRepositoryPolicyResponse**](SetRepositoryPolicyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Associates the specified tags to a resource with the specified &lt;code&gt;resourceArn&lt;/code&gt;. If existing tags on a resource aren&#39;t specified in the request parameters, they aren&#39;t changed. When a resource is deleted, the tags associated with that resource are also deleted.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AmazonElasticContainerRegistryPublic.TagResourceRequest(); // TagResourceRequest | 
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


## untagResource

> Object untagResource(xAmzTarget, untagResourceRequest, opts)



Deletes specified tags from a resource.

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AmazonElasticContainerRegistryPublic.UntagResourceRequest(); // UntagResourceRequest | 
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


## uploadLayerPart

> UploadLayerPartResponse uploadLayerPart(xAmzTarget, uploadLayerPartRequest, opts)



&lt;p&gt;Uploads an image layer part to Amazon ECR.&lt;/p&gt; &lt;p&gt;When an image is pushed, each new image layer is uploaded in parts. The maximum size of each image layer part can be 20971520 bytes (about 20MB). The UploadLayerPart API is called once for each new image layer part.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This operation is used by the Amazon ECR proxy and is not generally used by customers for pulling and pushing images. In most cases, you should use the &lt;code&gt;docker&lt;/code&gt; CLI to pull, tag, and push images.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonElasticContainerRegistryPublic from 'amazon_elastic_container_registry_public';
let defaultClient = AmazonElasticContainerRegistryPublic.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonElasticContainerRegistryPublic.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let uploadLayerPartRequest = new AmazonElasticContainerRegistryPublic.UploadLayerPartRequest(); // UploadLayerPartRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.uploadLayerPart(xAmzTarget, uploadLayerPartRequest, opts, (error, data, response) => {
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
 **uploadLayerPartRequest** | [**UploadLayerPartRequest**](UploadLayerPartRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UploadLayerPartResponse**](UploadLayerPartResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

