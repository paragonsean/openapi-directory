# AwsTelcoNetworkBuilder.DefaultApi

All URIs are relative to *http://tnb.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelSolNetworkOperation**](DefaultApi.md#cancelSolNetworkOperation) | **POST** /sol/nslcm/v1/ns_lcm_op_occs/{nsLcmOpOccId}/cancel | 
[**createSolFunctionPackage**](DefaultApi.md#createSolFunctionPackage) | **POST** /sol/vnfpkgm/v1/vnf_packages | 
[**createSolNetworkInstance**](DefaultApi.md#createSolNetworkInstance) | **POST** /sol/nslcm/v1/ns_instances | 
[**createSolNetworkPackage**](DefaultApi.md#createSolNetworkPackage) | **POST** /sol/nsd/v1/ns_descriptors | 
[**deleteSolFunctionPackage**](DefaultApi.md#deleteSolFunctionPackage) | **DELETE** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId} | 
[**deleteSolNetworkInstance**](DefaultApi.md#deleteSolNetworkInstance) | **DELETE** /sol/nslcm/v1/ns_instances/{nsInstanceId} | 
[**deleteSolNetworkPackage**](DefaultApi.md#deleteSolNetworkPackage) | **DELETE** /sol/nsd/v1/ns_descriptors/{nsdInfoId} | 
[**getSolFunctionInstance**](DefaultApi.md#getSolFunctionInstance) | **GET** /sol/vnflcm/v1/vnf_instances/{vnfInstanceId} | 
[**getSolFunctionPackage**](DefaultApi.md#getSolFunctionPackage) | **GET** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId} | 
[**getSolFunctionPackageContent**](DefaultApi.md#getSolFunctionPackageContent) | **GET** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId}/package_content#Accept | 
[**getSolFunctionPackageDescriptor**](DefaultApi.md#getSolFunctionPackageDescriptor) | **GET** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId}/vnfd#Accept | 
[**getSolNetworkInstance**](DefaultApi.md#getSolNetworkInstance) | **GET** /sol/nslcm/v1/ns_instances/{nsInstanceId} | 
[**getSolNetworkOperation**](DefaultApi.md#getSolNetworkOperation) | **GET** /sol/nslcm/v1/ns_lcm_op_occs/{nsLcmOpOccId} | 
[**getSolNetworkPackage**](DefaultApi.md#getSolNetworkPackage) | **GET** /sol/nsd/v1/ns_descriptors/{nsdInfoId} | 
[**getSolNetworkPackageContent**](DefaultApi.md#getSolNetworkPackageContent) | **GET** /sol/nsd/v1/ns_descriptors/{nsdInfoId}/nsd_content#Accept | 
[**getSolNetworkPackageDescriptor**](DefaultApi.md#getSolNetworkPackageDescriptor) | **GET** /sol/nsd/v1/ns_descriptors/{nsdInfoId}/nsd | 
[**instantiateSolNetworkInstance**](DefaultApi.md#instantiateSolNetworkInstance) | **POST** /sol/nslcm/v1/ns_instances/{nsInstanceId}/instantiate | 
[**listSolFunctionInstances**](DefaultApi.md#listSolFunctionInstances) | **GET** /sol/vnflcm/v1/vnf_instances | 
[**listSolFunctionPackages**](DefaultApi.md#listSolFunctionPackages) | **GET** /sol/vnfpkgm/v1/vnf_packages | 
[**listSolNetworkInstances**](DefaultApi.md#listSolNetworkInstances) | **GET** /sol/nslcm/v1/ns_instances | 
[**listSolNetworkOperations**](DefaultApi.md#listSolNetworkOperations) | **GET** /sol/nslcm/v1/ns_lcm_op_occs | 
[**listSolNetworkPackages**](DefaultApi.md#listSolNetworkPackages) | **GET** /sol/nsd/v1/ns_descriptors | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**putSolFunctionPackageContent**](DefaultApi.md#putSolFunctionPackageContent) | **PUT** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId}/package_content | 
[**putSolNetworkPackageContent**](DefaultApi.md#putSolNetworkPackageContent) | **PUT** /sol/nsd/v1/ns_descriptors/{nsdInfoId}/nsd_content | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**terminateSolNetworkInstance**](DefaultApi.md#terminateSolNetworkInstance) | **POST** /sol/nslcm/v1/ns_instances/{nsInstanceId}/terminate | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateSolFunctionPackage**](DefaultApi.md#updateSolFunctionPackage) | **PATCH** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId} | 
[**updateSolNetworkInstance**](DefaultApi.md#updateSolNetworkInstance) | **POST** /sol/nslcm/v1/ns_instances/{nsInstanceId}/update | 
[**updateSolNetworkPackage**](DefaultApi.md#updateSolNetworkPackage) | **PATCH** /sol/nsd/v1/ns_descriptors/{nsdInfoId} | 
[**validateSolFunctionPackageContent**](DefaultApi.md#validateSolFunctionPackageContent) | **PUT** /sol/vnfpkgm/v1/vnf_packages/{vnfPkgId}/package_content/validate | 
[**validateSolNetworkPackageContent**](DefaultApi.md#validateSolNetworkPackageContent) | **PUT** /sol/nsd/v1/ns_descriptors/{nsdInfoId}/nsd_content/validate | 



## cancelSolNetworkOperation

> cancelSolNetworkOperation(nsLcmOpOccId, opts)



&lt;p&gt;Cancels a network operation.&lt;/p&gt; &lt;p&gt;A network operation is any operation that is done to your network, such as network instance instantiation or termination.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsLcmOpOccId = "nsLcmOpOccId_example"; // String | The identifier of the network operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelSolNetworkOperation(nsLcmOpOccId, opts, (error, data, response) => {
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
 **nsLcmOpOccId** | **String**| The identifier of the network operation. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## createSolFunctionPackage

> CreateSolFunctionPackageOutput createSolFunctionPackage(createSolFunctionPackageRequest, opts)



&lt;p&gt;Creates a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/ug/function-packages.html\&quot;&gt;Function packages&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Telco Network Builder User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;Creating a function package is the first step for creating a network in AWS TNB. This request creates an empty container with an ID. The next step is to upload the actual CSAR zip file into that empty container. To upload function package content, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html\&quot;&gt;PutSolFunctionPackageContent&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let createSolFunctionPackageRequest = new AwsTelcoNetworkBuilder.CreateSolFunctionPackageRequest(); // CreateSolFunctionPackageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSolFunctionPackage(createSolFunctionPackageRequest, opts, (error, data, response) => {
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
 **createSolFunctionPackageRequest** | [**CreateSolFunctionPackageRequest**](CreateSolFunctionPackageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSolFunctionPackageOutput**](CreateSolFunctionPackageOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSolNetworkInstance

> CreateSolNetworkInstanceOutput createSolNetworkInstance(createSolNetworkInstanceRequest, opts)



&lt;p&gt;Creates a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed. Creating a network instance is the third step after creating a network package. For more information about network instances, &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html\&quot;&gt;Network instances&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Telco Network Builder User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;Once you create a network instance, you can instantiate it. To instantiate a network, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_InstantiateSolNetworkInstance.html\&quot;&gt;InstantiateSolNetworkInstance&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let createSolNetworkInstanceRequest = new AwsTelcoNetworkBuilder.CreateSolNetworkInstanceRequest(); // CreateSolNetworkInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSolNetworkInstance(createSolNetworkInstanceRequest, opts, (error, data, response) => {
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
 **createSolNetworkInstanceRequest** | [**CreateSolNetworkInstanceRequest**](CreateSolNetworkInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSolNetworkInstanceOutput**](CreateSolNetworkInstanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSolNetworkPackage

> CreateSolNetworkPackageOutput createSolNetworkPackage(createSolFunctionPackageRequest, opts)



&lt;p&gt;Creates a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/ug/network-instances.html\&quot;&gt;Network instances&lt;/a&gt; in the &lt;i&gt;Amazon Web Services Telco Network Builder User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;A network package consists of a network service descriptor (NSD) file (required) and any additional files (optional), such as scripts specific to your needs. For example, if you have multiple function packages in your network package, you can use the NSD to define which network functions should run in certain VPCs, subnets, or EKS clusters.&lt;/p&gt; &lt;p&gt;This request creates an empty network package container with an ID. Once you create a network package, you can upload the network package content using &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html\&quot;&gt;PutSolNetworkPackageContent&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let createSolFunctionPackageRequest = new AwsTelcoNetworkBuilder.CreateSolFunctionPackageRequest(); // CreateSolFunctionPackageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSolNetworkPackage(createSolFunctionPackageRequest, opts, (error, data, response) => {
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
 **createSolFunctionPackageRequest** | [**CreateSolFunctionPackageRequest**](CreateSolFunctionPackageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSolNetworkPackageOutput**](CreateSolNetworkPackageOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteSolFunctionPackage

> deleteSolFunctionPackage(vnfPkgId, opts)



&lt;p&gt;Deletes a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt; &lt;p&gt;To delete a function package, the package must be in a disabled state. To disable a function package, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolFunctionPackage.html\&quot;&gt;UpdateSolFunctionPackage&lt;/a&gt;. &lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let vnfPkgId = "vnfPkgId_example"; // String | ID of the function package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSolFunctionPackage(vnfPkgId, opts, (error, data, response) => {
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
 **vnfPkgId** | **String**| ID of the function package. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSolNetworkInstance

> deleteSolNetworkInstance(nsInstanceId, opts)



&lt;p&gt;Deletes a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt; &lt;p&gt;To delete a network instance, the instance must be in a stopped or terminated state. To terminate a network instance, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_TerminateSolNetworkInstance.html\&quot;&gt;TerminateSolNetworkInstance&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsInstanceId = "nsInstanceId_example"; // String | Network instance ID.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSolNetworkInstance(nsInstanceId, opts, (error, data, response) => {
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
 **nsInstanceId** | **String**| Network instance ID. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSolNetworkPackage

> deleteSolNetworkPackage(nsdInfoId, opts)



&lt;p&gt;Deletes network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt; &lt;p&gt;To delete a network package, the package must be in a disable state. To disable a network package, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_UpdateSolNetworkPackage.html\&quot;&gt;UpdateSolNetworkPackage&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsdInfoId = "nsdInfoId_example"; // String | ID of the network service descriptor in the network package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSolNetworkPackage(nsdInfoId, opts, (error, data, response) => {
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
 **nsdInfoId** | **String**| ID of the network service descriptor in the network package. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolFunctionInstance

> GetSolFunctionInstanceOutput getSolFunctionInstance(vnfInstanceId, opts)



&lt;p&gt;Gets the details of a network function instance, including the instantation state and metadata from the function package descriptor in the network function package.&lt;/p&gt; &lt;p&gt;A network function instance is a function in a function package .&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let vnfInstanceId = "vnfInstanceId_example"; // String | ID of the network function.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolFunctionInstance(vnfInstanceId, opts, (error, data, response) => {
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
 **vnfInstanceId** | **String**| ID of the network function. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolFunctionInstanceOutput**](GetSolFunctionInstanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolFunctionPackage

> GetSolFunctionPackageOutput getSolFunctionPackage(vnfPkgId, opts)



&lt;p&gt;Gets the details of an individual function package, such as the operational state and whether the package is in use.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network..&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let vnfPkgId = "vnfPkgId_example"; // String | ID of the function package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolFunctionPackage(vnfPkgId, opts, (error, data, response) => {
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
 **vnfPkgId** | **String**| ID of the function package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolFunctionPackageOutput**](GetSolFunctionPackageOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolFunctionPackageContent

> GetSolFunctionPackageContentOutput getSolFunctionPackageContent(accept, vnfPkgId, opts)



&lt;p&gt;Gets the contents of a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let accept = "accept_example"; // String | The format of the package that you want to download from the function packages.
let vnfPkgId = "vnfPkgId_example"; // String | ID of the function package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolFunctionPackageContent(accept, vnfPkgId, opts, (error, data, response) => {
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
 **accept** | **String**| The format of the package that you want to download from the function packages. | 
 **vnfPkgId** | **String**| ID of the function package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolFunctionPackageContentOutput**](GetSolFunctionPackageContentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolFunctionPackageDescriptor

> GetSolFunctionPackageDescriptorOutput getSolFunctionPackageDescriptor(accept, vnfPkgId, opts)



&lt;p&gt;Gets a function package descriptor in a function package.&lt;/p&gt; &lt;p&gt;A function package descriptor is a .yaml file in a function package that uses the TOSCA standard to describe how the network function in the function package should run on your network.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let accept = "accept_example"; // String | Indicates which content types, expressed as MIME types, the client is able to understand.
let vnfPkgId = "vnfPkgId_example"; // String | ID of the function package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolFunctionPackageDescriptor(accept, vnfPkgId, opts, (error, data, response) => {
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
 **accept** | **String**| Indicates which content types, expressed as MIME types, the client is able to understand. | 
 **vnfPkgId** | **String**| ID of the function package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolFunctionPackageDescriptorOutput**](GetSolFunctionPackageDescriptorOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolNetworkInstance

> GetSolNetworkInstanceOutput getSolNetworkInstance(nsInstanceId, opts)



&lt;p&gt;Gets the details of the network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsInstanceId = "nsInstanceId_example"; // String | ID of the network instance.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolNetworkInstance(nsInstanceId, opts, (error, data, response) => {
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
 **nsInstanceId** | **String**| ID of the network instance. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolNetworkInstanceOutput**](GetSolNetworkInstanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolNetworkOperation

> GetSolNetworkOperationOutput getSolNetworkOperation(nsLcmOpOccId, opts)



&lt;p&gt;Gets the details of a network operation, including the tasks involved in the network operation and the status of the tasks.&lt;/p&gt; &lt;p&gt;A network operation is any operation that is done to your network, such as network instance instantiation or termination.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsLcmOpOccId = "nsLcmOpOccId_example"; // String | The identifier of the network operation.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolNetworkOperation(nsLcmOpOccId, opts, (error, data, response) => {
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
 **nsLcmOpOccId** | **String**| The identifier of the network operation. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolNetworkOperationOutput**](GetSolNetworkOperationOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolNetworkPackage

> GetSolNetworkPackageOutput getSolNetworkPackage(nsdInfoId, opts)



&lt;p&gt;Gets the details of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsdInfoId = "nsdInfoId_example"; // String | ID of the network service descriptor in the network package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolNetworkPackage(nsdInfoId, opts, (error, data, response) => {
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
 **nsdInfoId** | **String**| ID of the network service descriptor in the network package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolNetworkPackageOutput**](GetSolNetworkPackageOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolNetworkPackageContent

> GetSolNetworkPackageContentOutput getSolNetworkPackageContent(accept, nsdInfoId, opts)



&lt;p&gt;Gets the contents of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let accept = "accept_example"; // String | The format of the package you want to download from the network package.
let nsdInfoId = "nsdInfoId_example"; // String | ID of the network service descriptor in the network package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolNetworkPackageContent(accept, nsdInfoId, opts, (error, data, response) => {
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
 **accept** | **String**| The format of the package you want to download from the network package. | 
 **nsdInfoId** | **String**| ID of the network service descriptor in the network package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolNetworkPackageContentOutput**](GetSolNetworkPackageContentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSolNetworkPackageDescriptor

> GetSolNetworkPackageDescriptorOutput getSolNetworkPackageDescriptor(nsdInfoId, opts)



&lt;p&gt;Gets the content of the network service descriptor.&lt;/p&gt; &lt;p&gt;A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the Amazon Web Services infrastructure you want to deploy the network functions on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsdInfoId = "nsdInfoId_example"; // String | ID of the network service descriptor in the network package.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSolNetworkPackageDescriptor(nsdInfoId, opts, (error, data, response) => {
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
 **nsdInfoId** | **String**| ID of the network service descriptor in the network package. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSolNetworkPackageDescriptorOutput**](GetSolNetworkPackageDescriptorOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## instantiateSolNetworkInstance

> InstantiateSolNetworkInstanceOutput instantiateSolNetworkInstance(nsInstanceId, instantiateSolNetworkInstanceRequest, opts)



&lt;p&gt;Instantiates a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt; &lt;p&gt;Before you can instantiate a network instance, you have to create a network instance. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_CreateSolNetworkInstance.html\&quot;&gt;CreateSolNetworkInstance&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsInstanceId = "nsInstanceId_example"; // String | ID of the network instance.
let instantiateSolNetworkInstanceRequest = new AwsTelcoNetworkBuilder.InstantiateSolNetworkInstanceRequest(); // InstantiateSolNetworkInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'dryRun': true // Boolean | A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.
};
apiInstance.instantiateSolNetworkInstance(nsInstanceId, instantiateSolNetworkInstanceRequest, opts, (error, data, response) => {
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
 **nsInstanceId** | **String**| ID of the network instance. | 
 **instantiateSolNetworkInstanceRequest** | [**InstantiateSolNetworkInstanceRequest**](InstantiateSolNetworkInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **dryRun** | **Boolean**| A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is &lt;code&gt;DryRunOperation&lt;/code&gt;. Otherwise, it is &lt;code&gt;UnauthorizedOperation&lt;/code&gt;. | [optional] 

### Return type

[**InstantiateSolNetworkInstanceOutput**](InstantiateSolNetworkInstanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSolFunctionInstances

> ListSolFunctionInstancesOutput listSolFunctionInstances(opts)



&lt;p&gt;Lists network function instances.&lt;/p&gt; &lt;p&gt;A network function instance is a function in a function package .&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextpageOpaqueMarker': "nextpageOpaqueMarker_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listSolFunctionInstances(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextpageOpaqueMarker** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSolFunctionInstancesOutput**](ListSolFunctionInstancesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSolFunctionPackages

> ListSolFunctionPackagesOutput listSolFunctionPackages(opts)



&lt;p&gt;Lists information about function packages.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextpageOpaqueMarker': "nextpageOpaqueMarker_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listSolFunctionPackages(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextpageOpaqueMarker** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSolFunctionPackagesOutput**](ListSolFunctionPackagesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSolNetworkInstances

> ListSolNetworkInstancesOutput listSolNetworkInstances(opts)



&lt;p&gt;Lists your network instances.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextpageOpaqueMarker': "nextpageOpaqueMarker_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listSolNetworkInstances(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextpageOpaqueMarker** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSolNetworkInstancesOutput**](ListSolNetworkInstancesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSolNetworkOperations

> ListSolNetworkOperationsOutput listSolNetworkOperations(opts)



&lt;p&gt;Lists details for a network operation, including when the operation started and the status of the operation.&lt;/p&gt; &lt;p&gt;A network operation is any operation that is done to your network, such as network instance instantiation or termination.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextpageOpaqueMarker': "nextpageOpaqueMarker_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listSolNetworkOperations(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextpageOpaqueMarker** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSolNetworkOperationsOutput**](ListSolNetworkOperationsOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSolNetworkPackages

> ListSolNetworkPackagesOutput listSolNetworkPackages(opts)



&lt;p&gt;Lists network packages.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to include in the response.
  'nextpageOpaqueMarker': "nextpageOpaqueMarker_example", // String | The token for the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listSolNetworkPackages(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of results to include in the response. | [optional] 
 **nextpageOpaqueMarker** | **String**| The token for the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListSolNetworkPackagesOutput**](ListSolNetworkPackagesOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceOutput listTagsForResource(resourceArn, opts)



Lists tags for AWS TNB resources.

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let resourceArn = "resourceArn_example"; // String | Resource ARN.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listTagsForResource(resourceArn, opts, (error, data, response) => {
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
 **resourceArn** | **String**| Resource ARN. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListTagsForResourceOutput**](ListTagsForResourceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## putSolFunctionPackageContent

> PutSolFunctionPackageContentOutput putSolFunctionPackageContent(vnfPkgId, putSolFunctionPackageContentRequest, opts)



&lt;p&gt;Uploads the contents of a function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let vnfPkgId = "vnfPkgId_example"; // String | Function package ID.
let putSolFunctionPackageContentRequest = new AwsTelcoNetworkBuilder.PutSolFunctionPackageContentRequest(); // PutSolFunctionPackageContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'contentType': "contentType_example" // String | Function package content type.
};
apiInstance.putSolFunctionPackageContent(vnfPkgId, putSolFunctionPackageContentRequest, opts, (error, data, response) => {
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
 **vnfPkgId** | **String**| Function package ID. | 
 **putSolFunctionPackageContentRequest** | [**PutSolFunctionPackageContentRequest**](PutSolFunctionPackageContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **contentType** | **String**| Function package content type. | [optional] 

### Return type

[**PutSolFunctionPackageContentOutput**](PutSolFunctionPackageContentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putSolNetworkPackageContent

> PutSolNetworkPackageContentOutput putSolNetworkPackageContent(nsdInfoId, putSolNetworkPackageContentRequest, opts)



&lt;p&gt;Uploads the contents of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsdInfoId = "nsdInfoId_example"; // String | Network service descriptor info ID.
let putSolNetworkPackageContentRequest = new AwsTelcoNetworkBuilder.PutSolNetworkPackageContentRequest(); // PutSolNetworkPackageContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'contentType': "contentType_example" // String | Network package content type.
};
apiInstance.putSolNetworkPackageContent(nsdInfoId, putSolNetworkPackageContentRequest, opts, (error, data, response) => {
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
 **nsdInfoId** | **String**| Network service descriptor info ID. | 
 **putSolNetworkPackageContentRequest** | [**PutSolNetworkPackageContentRequest**](PutSolNetworkPackageContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **contentType** | **String**| Network package content type. | [optional] 

### Return type

[**PutSolNetworkPackageContentOutput**](PutSolNetworkPackageContentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Tags an AWS TNB resource.&lt;/p&gt; &lt;p&gt;A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let resourceArn = "resourceArn_example"; // String | Resource ARN.
let tagResourceRequest = new AwsTelcoNetworkBuilder.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(resourceArn, tagResourceRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**| Resource ARN. | 
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


## terminateSolNetworkInstance

> TerminateSolNetworkInstanceOutput terminateSolNetworkInstance(nsInstanceId, terminateSolNetworkInstanceRequest, opts)



&lt;p&gt;Terminates a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt; &lt;p&gt;You must terminate a network instance before you can delete it.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsInstanceId = "nsInstanceId_example"; // String | ID of the network instance.
let terminateSolNetworkInstanceRequest = new AwsTelcoNetworkBuilder.TerminateSolNetworkInstanceRequest(); // TerminateSolNetworkInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.terminateSolNetworkInstance(nsInstanceId, terminateSolNetworkInstanceRequest, opts, (error, data, response) => {
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
 **nsInstanceId** | **String**| ID of the network instance. | 
 **terminateSolNetworkInstanceRequest** | [**TerminateSolNetworkInstanceRequest**](TerminateSolNetworkInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TerminateSolNetworkInstanceOutput**](TerminateSolNetworkInstanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## untagResource

> Object untagResource(resourceArn, tagKeys, opts)



&lt;p&gt;Untags an AWS TNB resource.&lt;/p&gt; &lt;p&gt;A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let resourceArn = "resourceArn_example"; // String | Resource ARN.
let tagKeys = ["null"]; // [String] | Tag keys.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.untagResource(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**| Resource ARN. | 
 **tagKeys** | [**[String]**](String.md)| Tag keys. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## updateSolFunctionPackage

> UpdateSolFunctionPackageOutput updateSolFunctionPackage(vnfPkgId, updateSolFunctionPackageRequest, opts)



&lt;p&gt;Updates the operational state of function package.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let vnfPkgId = "vnfPkgId_example"; // String | ID of the function package.
let updateSolFunctionPackageRequest = new AwsTelcoNetworkBuilder.UpdateSolFunctionPackageRequest(); // UpdateSolFunctionPackageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSolFunctionPackage(vnfPkgId, updateSolFunctionPackageRequest, opts, (error, data, response) => {
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
 **vnfPkgId** | **String**| ID of the function package. | 
 **updateSolFunctionPackageRequest** | [**UpdateSolFunctionPackageRequest**](UpdateSolFunctionPackageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSolFunctionPackageOutput**](UpdateSolFunctionPackageOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSolNetworkInstance

> UpdateSolNetworkInstanceOutput updateSolNetworkInstance(nsInstanceId, updateSolNetworkInstanceRequest, opts)



&lt;p&gt;Update a network instance.&lt;/p&gt; &lt;p&gt;A network instance is a single network created in Amazon Web Services TNB that can be deployed and on which life-cycle operations (like terminate, update, and delete) can be performed.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsInstanceId = "nsInstanceId_example"; // String | ID of the network instance.
let updateSolNetworkInstanceRequest = new AwsTelcoNetworkBuilder.UpdateSolNetworkInstanceRequest(); // UpdateSolNetworkInstanceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSolNetworkInstance(nsInstanceId, updateSolNetworkInstanceRequest, opts, (error, data, response) => {
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
 **nsInstanceId** | **String**| ID of the network instance. | 
 **updateSolNetworkInstanceRequest** | [**UpdateSolNetworkInstanceRequest**](UpdateSolNetworkInstanceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSolNetworkInstanceOutput**](UpdateSolNetworkInstanceOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSolNetworkPackage

> UpdateSolNetworkPackageOutput updateSolNetworkPackage(nsdInfoId, updateSolNetworkPackageRequest, opts)



&lt;p&gt;Updates the operational state of a network package.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt; &lt;p&gt;A network service descriptor is a .yaml file in a network package that uses the TOSCA standard to describe the network functions you want to deploy and the Amazon Web Services infrastructure you want to deploy the network functions on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsdInfoId = "nsdInfoId_example"; // String | ID of the network service descriptor in the network package.
let updateSolNetworkPackageRequest = new AwsTelcoNetworkBuilder.UpdateSolNetworkPackageRequest(); // UpdateSolNetworkPackageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSolNetworkPackage(nsdInfoId, updateSolNetworkPackageRequest, opts, (error, data, response) => {
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
 **nsdInfoId** | **String**| ID of the network service descriptor in the network package. | 
 **updateSolNetworkPackageRequest** | [**UpdateSolNetworkPackageRequest**](UpdateSolNetworkPackageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSolNetworkPackageOutput**](UpdateSolNetworkPackageOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateSolFunctionPackageContent

> ValidateSolFunctionPackageContentOutput validateSolFunctionPackageContent(vnfPkgId, putSolFunctionPackageContentRequest, opts)



&lt;p&gt;Validates function package content. This can be used as a dry run before uploading function package content with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolFunctionPackageContent.html\&quot;&gt;PutSolFunctionPackageContent&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A function package is a .zip file in CSAR (Cloud Service Archive) format that contains a network function (an ETSI standard telecommunication application) and function package descriptor that uses the TOSCA standard to describe how the network functions should run on your network.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let vnfPkgId = "vnfPkgId_example"; // String | Function package ID.
let putSolFunctionPackageContentRequest = new AwsTelcoNetworkBuilder.PutSolFunctionPackageContentRequest(); // PutSolFunctionPackageContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'contentType': "contentType_example" // String | Function package content type.
};
apiInstance.validateSolFunctionPackageContent(vnfPkgId, putSolFunctionPackageContentRequest, opts, (error, data, response) => {
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
 **vnfPkgId** | **String**| Function package ID. | 
 **putSolFunctionPackageContentRequest** | [**PutSolFunctionPackageContentRequest**](PutSolFunctionPackageContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **contentType** | **String**| Function package content type. | [optional] 

### Return type

[**ValidateSolFunctionPackageContentOutput**](ValidateSolFunctionPackageContentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## validateSolNetworkPackageContent

> ValidateSolNetworkPackageContentOutput validateSolNetworkPackageContent(nsdInfoId, putSolNetworkPackageContentRequest, opts)



&lt;p&gt;Validates network package content. This can be used as a dry run before uploading network package content with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/tnb/latest/APIReference/API_PutSolNetworkPackageContent.html\&quot;&gt;PutSolNetworkPackageContent&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;A network package is a .zip file in CSAR (Cloud Service Archive) format defines the function packages you want to deploy and the Amazon Web Services infrastructure you want to deploy them on.&lt;/p&gt;

### Example

```javascript
import AwsTelcoNetworkBuilder from 'aws_telco_network_builder';
let defaultClient = AwsTelcoNetworkBuilder.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsTelcoNetworkBuilder.DefaultApi();
let nsdInfoId = "nsdInfoId_example"; // String | Network service descriptor file.
let putSolNetworkPackageContentRequest = new AwsTelcoNetworkBuilder.PutSolNetworkPackageContentRequest(); // PutSolNetworkPackageContentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'contentType': "contentType_example" // String | Network package content type.
};
apiInstance.validateSolNetworkPackageContent(nsdInfoId, putSolNetworkPackageContentRequest, opts, (error, data, response) => {
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
 **nsdInfoId** | **String**| Network service descriptor file. | 
 **putSolNetworkPackageContentRequest** | [**PutSolNetworkPackageContentRequest**](PutSolNetworkPackageContentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **contentType** | **String**| Network package content type. | [optional] 

### Return type

[**ValidateSolNetworkPackageContentOutput**](ValidateSolNetworkPackageContentOutput.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

