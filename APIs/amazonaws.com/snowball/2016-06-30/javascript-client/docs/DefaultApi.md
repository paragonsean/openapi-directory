# AmazonImportExportSnowball.DefaultApi

All URIs are relative to *http://snowball.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelCluster**](DefaultApi.md#cancelCluster) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CancelCluster | 
[**cancelJob**](DefaultApi.md#cancelJob) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CancelJob | 
[**createAddress**](DefaultApi.md#createAddress) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CreateAddress | 
[**createCluster**](DefaultApi.md#createCluster) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CreateCluster | 
[**createJob**](DefaultApi.md#createJob) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CreateJob | 
[**createLongTermPricing**](DefaultApi.md#createLongTermPricing) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CreateLongTermPricing | 
[**createReturnShippingLabel**](DefaultApi.md#createReturnShippingLabel) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.CreateReturnShippingLabel | 
[**describeAddress**](DefaultApi.md#describeAddress) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.DescribeAddress | 
[**describeAddresses**](DefaultApi.md#describeAddresses) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.DescribeAddresses | 
[**describeCluster**](DefaultApi.md#describeCluster) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.DescribeCluster | 
[**describeJob**](DefaultApi.md#describeJob) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.DescribeJob | 
[**describeReturnShippingLabel**](DefaultApi.md#describeReturnShippingLabel) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.DescribeReturnShippingLabel | 
[**getJobManifest**](DefaultApi.md#getJobManifest) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.GetJobManifest | 
[**getJobUnlockCode**](DefaultApi.md#getJobUnlockCode) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.GetJobUnlockCode | 
[**getSnowballUsage**](DefaultApi.md#getSnowballUsage) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.GetSnowballUsage | 
[**getSoftwareUpdates**](DefaultApi.md#getSoftwareUpdates) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.GetSoftwareUpdates | 
[**listClusterJobs**](DefaultApi.md#listClusterJobs) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListClusterJobs | 
[**listClusters**](DefaultApi.md#listClusters) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListClusters | 
[**listCompatibleImages**](DefaultApi.md#listCompatibleImages) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListCompatibleImages | 
[**listJobs**](DefaultApi.md#listJobs) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListJobs | 
[**listLongTermPricing**](DefaultApi.md#listLongTermPricing) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListLongTermPricing | 
[**listPickupLocations**](DefaultApi.md#listPickupLocations) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListPickupLocations | 
[**listServiceVersions**](DefaultApi.md#listServiceVersions) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.ListServiceVersions | 
[**updateCluster**](DefaultApi.md#updateCluster) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.UpdateCluster | 
[**updateJob**](DefaultApi.md#updateJob) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.UpdateJob | 
[**updateJobShipmentState**](DefaultApi.md#updateJobShipmentState) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.UpdateJobShipmentState | 
[**updateLongTermPricing**](DefaultApi.md#updateLongTermPricing) | **POST** /#X-Amz-Target&#x3D;AWSIESnowballJobManagementService.UpdateLongTermPricing | 



## cancelCluster

> Object cancelCluster(xAmzTarget, cancelClusterRequest, opts)



Cancels a cluster job. You can only cancel a cluster job while it&#39;s in the &lt;code&gt;AwaitingQuorum&lt;/code&gt; status. You&#39;ll have at least an hour after creating a cluster job to cancel it.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let cancelClusterRequest = new AmazonImportExportSnowball.CancelClusterRequest(); // CancelClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelCluster(xAmzTarget, cancelClusterRequest, opts, (error, data, response) => {
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
 **cancelClusterRequest** | [**CancelClusterRequest**](CancelClusterRequest.md)|  | 
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


## cancelJob

> Object cancelJob(xAmzTarget, cancelJobRequest, opts)



Cancels the specified job. You can only cancel a job before its &lt;code&gt;JobState&lt;/code&gt; value changes to &lt;code&gt;PreparingAppliance&lt;/code&gt;. Requesting the &lt;code&gt;ListJobs&lt;/code&gt; or &lt;code&gt;DescribeJob&lt;/code&gt; action returns a job&#39;s &lt;code&gt;JobState&lt;/code&gt; as part of the response element data returned.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let cancelJobRequest = new AmazonImportExportSnowball.CancelJobRequest(); // CancelJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelJob(xAmzTarget, cancelJobRequest, opts, (error, data, response) => {
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
 **cancelJobRequest** | [**CancelJobRequest**](CancelJobRequest.md)|  | 
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


## createAddress

> CreateAddressResult createAddress(xAmzTarget, createAddressRequest, opts)



Creates an address for a Snow device to be shipped to. In most regions, addresses are validated at the time of creation. The address you provide must be located within the serviceable area of your region. If the address is invalid or unsupported, then an exception is thrown.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createAddressRequest = new AmazonImportExportSnowball.CreateAddressRequest(); // CreateAddressRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createAddress(xAmzTarget, createAddressRequest, opts, (error, data, response) => {
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
 **createAddressRequest** | [**CreateAddressRequest**](CreateAddressRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAddressResult**](CreateAddressResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCluster

> CreateClusterResult createCluster(xAmzTarget, createClusterRequest, opts)



Creates an empty cluster. Each cluster supports five nodes. You use the &lt;a&gt;CreateJob&lt;/a&gt; action separately to create the jobs for each of these nodes. The cluster does not ship until these five node jobs have been created.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createClusterRequest = new AmazonImportExportSnowball.CreateClusterRequest(); // CreateClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCluster(xAmzTarget, createClusterRequest, opts, (error, data, response) => {
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
 **createClusterRequest** | [**CreateClusterRequest**](CreateClusterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateClusterResult**](CreateClusterResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createJob

> CreateJobResult createJob(xAmzTarget, createJobRequest, opts)



&lt;p&gt;Creates a job to import or export data between Amazon S3 and your on-premises data center. Your Amazon Web Services account must have the right trust policies and permissions in place to create a job for a Snow device. If you&#39;re creating a job for a node in a cluster, you only need to provide the &lt;code&gt;clusterId&lt;/code&gt; value; the other job attributes are inherited from the cluster. &lt;/p&gt; &lt;note&gt; &lt;p&gt;Only the Snowball; Edge device type is supported when ordering clustered jobs.&lt;/p&gt; &lt;p&gt;The device capacity is optional.&lt;/p&gt; &lt;p&gt;Availability of device types differ by Amazon Web Services Region. For more information about Region availability, see &lt;a href&#x3D;\&quot;https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/?p&#x3D;ngi&amp;amp;loc&#x3D;4\&quot;&gt;Amazon Web Services Regional Services&lt;/a&gt;.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;p class&#x3D;\&quot;title\&quot;&gt; &lt;b&gt;Snow Family devices and their capacities.&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;SNC1_SSD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T14&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowcone &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;SNC1_HDD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T8&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowcone &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE_S&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T98&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Storage Optimized for data transfer only &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE_CG&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T42&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Compute Optimized with GPU&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE_C&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T42&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Compute Optimized without GPU&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;EDGE&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T100&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Storage Optimized with EC2 Compute&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;note&gt; &lt;p&gt;This device is replaced with T98.&lt;/p&gt; &lt;/note&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;STANDARD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T50&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Original Snowball device&lt;/p&gt; &lt;note&gt; &lt;p&gt;This device is only available in the Ningxia, Beijing, and Singapore Amazon Web Services Region &lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;STANDARD&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T80&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Original Snowball device&lt;/p&gt; &lt;note&gt; &lt;p&gt;This device is only available in the Ningxia, Beijing, and Singapore Amazon Web Services Region. &lt;/p&gt; &lt;/note&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p/&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Snow Family device type: &lt;b&gt;RACK_5U_C&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T13 &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowblade.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Device type: &lt;b&gt;V3_5S&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Capacity: T240&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Description: Snowball Edge Storage Optimized 210TB&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createJobRequest = new AmazonImportExportSnowball.CreateJobRequest(); // CreateJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createJob(xAmzTarget, createJobRequest, opts, (error, data, response) => {
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
 **createJobRequest** | [**CreateJobRequest**](CreateJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateJobResult**](CreateJobResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createLongTermPricing

> CreateLongTermPricingResult createLongTermPricing(xAmzTarget, createLongTermPricingRequest, opts)



Creates a job with the long-term usage option for a device. The long-term usage is a 1-year or 3-year long-term pricing type for the device. You are billed upfront, and Amazon Web Services provides discounts for long-term pricing. 

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createLongTermPricingRequest = new AmazonImportExportSnowball.CreateLongTermPricingRequest(); // CreateLongTermPricingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createLongTermPricing(xAmzTarget, createLongTermPricingRequest, opts, (error, data, response) => {
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
 **createLongTermPricingRequest** | [**CreateLongTermPricingRequest**](CreateLongTermPricingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateLongTermPricingResult**](CreateLongTermPricingResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createReturnShippingLabel

> CreateReturnShippingLabelResult createReturnShippingLabel(xAmzTarget, createReturnShippingLabelRequest, opts)



Creates a shipping label that will be used to return the Snow device to Amazon Web Services.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createReturnShippingLabelRequest = new AmazonImportExportSnowball.CreateReturnShippingLabelRequest(); // CreateReturnShippingLabelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createReturnShippingLabel(xAmzTarget, createReturnShippingLabelRequest, opts, (error, data, response) => {
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
 **createReturnShippingLabelRequest** | [**CreateReturnShippingLabelRequest**](CreateReturnShippingLabelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateReturnShippingLabelResult**](CreateReturnShippingLabelResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAddress

> DescribeAddressResult describeAddress(xAmzTarget, describeAddressRequest, opts)



Takes an &lt;code&gt;AddressId&lt;/code&gt; and returns specific details about that address in the form of an &lt;code&gt;Address&lt;/code&gt; object.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAddressRequest = new AmazonImportExportSnowball.DescribeAddressRequest(); // DescribeAddressRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAddress(xAmzTarget, describeAddressRequest, opts, (error, data, response) => {
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
 **describeAddressRequest** | [**DescribeAddressRequest**](DescribeAddressRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeAddressResult**](DescribeAddressResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeAddresses

> DescribeAddressesResult describeAddresses(xAmzTarget, describeAddressesRequest, opts)



Returns a specified number of &lt;code&gt;ADDRESS&lt;/code&gt; objects. Calling this API in one of the US regions will return addresses from the list of all addresses associated with this account in all US regions.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeAddressesRequest = new AmazonImportExportSnowball.DescribeAddressesRequest(); // DescribeAddressesRequest | 
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
apiInstance.describeAddresses(xAmzTarget, describeAddressesRequest, opts, (error, data, response) => {
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
 **describeAddressesRequest** | [**DescribeAddressesRequest**](DescribeAddressesRequest.md)|  | 
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

[**DescribeAddressesResult**](DescribeAddressesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeCluster

> DescribeClusterResult describeCluster(xAmzTarget, describeClusterRequest, opts)



Returns information about a specific cluster including shipping information, cluster status, and other important metadata.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeClusterRequest = new AmazonImportExportSnowball.DescribeClusterRequest(); // DescribeClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeCluster(xAmzTarget, describeClusterRequest, opts, (error, data, response) => {
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
 **describeClusterRequest** | [**DescribeClusterRequest**](DescribeClusterRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeClusterResult**](DescribeClusterResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeJob

> DescribeJobResult describeJob(xAmzTarget, describeJobRequest, opts)



Returns information about a specific job including shipping information, job status, and other important metadata. 

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeJobRequest = new AmazonImportExportSnowball.DescribeJobRequest(); // DescribeJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeJob(xAmzTarget, describeJobRequest, opts, (error, data, response) => {
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
 **describeJobRequest** | [**DescribeJobRequest**](DescribeJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeJobResult**](DescribeJobResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describeReturnShippingLabel

> DescribeReturnShippingLabelResult describeReturnShippingLabel(xAmzTarget, describeReturnShippingLabelRequest, opts)



Information on the shipping label of a Snow device that is being returned to Amazon Web Services.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeReturnShippingLabelRequest = new AmazonImportExportSnowball.DescribeReturnShippingLabelRequest(); // DescribeReturnShippingLabelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeReturnShippingLabel(xAmzTarget, describeReturnShippingLabelRequest, opts, (error, data, response) => {
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
 **describeReturnShippingLabelRequest** | [**DescribeReturnShippingLabelRequest**](DescribeReturnShippingLabelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeReturnShippingLabelResult**](DescribeReturnShippingLabelResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getJobManifest

> GetJobManifestResult getJobManifest(xAmzTarget, getJobManifestRequest, opts)



&lt;p&gt;Returns a link to an Amazon S3 presigned URL for the manifest file associated with the specified &lt;code&gt;JobId&lt;/code&gt; value. You can access the manifest file for up to 60 minutes after this request has been made. To access the manifest file after 60 minutes have passed, you&#39;ll have to make another call to the &lt;code&gt;GetJobManifest&lt;/code&gt; action.&lt;/p&gt; &lt;p&gt;The manifest is an encrypted file that you can download after your job enters the &lt;code&gt;WithCustomer&lt;/code&gt; status. This is the only valid status for calling this API as the manifest and &lt;code&gt;UnlockCode&lt;/code&gt; code value are used for securing your device and should only be used when you have the device. The manifest is decrypted by using the &lt;code&gt;UnlockCode&lt;/code&gt; code value, when you pass both values to the Snow device through the Snowball client when the client is started for the first time. &lt;/p&gt; &lt;p&gt;As a best practice, we recommend that you don&#39;t save a copy of an &lt;code&gt;UnlockCode&lt;/code&gt; value in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.&lt;/p&gt; &lt;p&gt;The credentials of a given job, including its manifest file and unlock code, expire 360 days after the job is created.&lt;/p&gt;

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getJobManifestRequest = new AmazonImportExportSnowball.GetJobManifestRequest(); // GetJobManifestRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getJobManifest(xAmzTarget, getJobManifestRequest, opts, (error, data, response) => {
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
 **getJobManifestRequest** | [**GetJobManifestRequest**](GetJobManifestRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetJobManifestResult**](GetJobManifestResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getJobUnlockCode

> GetJobUnlockCodeResult getJobUnlockCode(xAmzTarget, getJobUnlockCodeRequest, opts)



&lt;p&gt;Returns the &lt;code&gt;UnlockCode&lt;/code&gt; code value for the specified job. A particular &lt;code&gt;UnlockCode&lt;/code&gt; value can be accessed for up to 360 days after the associated job has been created.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;UnlockCode&lt;/code&gt; value is a 29-character code with 25 alphanumeric characters and 4 hyphens. This code is used to decrypt the manifest file when it is passed along with the manifest to the Snow device through the Snowball client when the client is started for the first time. The only valid status for calling this API is &lt;code&gt;WithCustomer&lt;/code&gt; as the manifest and &lt;code&gt;Unlock&lt;/code&gt; code values are used for securing your device and should only be used when you have the device.&lt;/p&gt; &lt;p&gt;As a best practice, we recommend that you don&#39;t save a copy of the &lt;code&gt;UnlockCode&lt;/code&gt; in the same location as the manifest file for that job. Saving these separately helps prevent unauthorized parties from gaining access to the Snow device associated with that job.&lt;/p&gt;

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getJobUnlockCodeRequest = new AmazonImportExportSnowball.GetJobUnlockCodeRequest(); // GetJobUnlockCodeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getJobUnlockCode(xAmzTarget, getJobUnlockCodeRequest, opts, (error, data, response) => {
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
 **getJobUnlockCodeRequest** | [**GetJobUnlockCodeRequest**](GetJobUnlockCodeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetJobUnlockCodeResult**](GetJobUnlockCodeResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSnowballUsage

> GetSnowballUsageResult getSnowballUsage(xAmzTarget, body, opts)



&lt;p&gt;Returns information about the Snow Family service limit for your account, and also the number of Snow devices your account has in use.&lt;/p&gt; &lt;p&gt;The default service limit for the number of Snow devices that you can have at one time is 1. If you want to increase your service limit, contact Amazon Web Services Support.&lt;/p&gt;

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
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
apiInstance.getSnowballUsage(xAmzTarget, body, opts, (error, data, response) => {
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

[**GetSnowballUsageResult**](GetSnowballUsageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getSoftwareUpdates

> GetSoftwareUpdatesResult getSoftwareUpdates(xAmzTarget, getSoftwareUpdatesRequest, opts)



Returns an Amazon S3 presigned URL for an update file associated with a specified &lt;code&gt;JobId&lt;/code&gt;.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getSoftwareUpdatesRequest = new AmazonImportExportSnowball.GetSoftwareUpdatesRequest(); // GetSoftwareUpdatesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSoftwareUpdates(xAmzTarget, getSoftwareUpdatesRequest, opts, (error, data, response) => {
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
 **getSoftwareUpdatesRequest** | [**GetSoftwareUpdatesRequest**](GetSoftwareUpdatesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSoftwareUpdatesResult**](GetSoftwareUpdatesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listClusterJobs

> ListClusterJobsResult listClusterJobs(xAmzTarget, listClusterJobsRequest, opts)



Returns an array of &lt;code&gt;JobListEntry&lt;/code&gt; objects of the specified length. Each &lt;code&gt;JobListEntry&lt;/code&gt; object is for a job in the specified cluster and contains a job&#39;s state, a job&#39;s ID, and other information.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listClusterJobsRequest = new AmazonImportExportSnowball.ListClusterJobsRequest(); // ListClusterJobsRequest | 
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
apiInstance.listClusterJobs(xAmzTarget, listClusterJobsRequest, opts, (error, data, response) => {
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
 **listClusterJobsRequest** | [**ListClusterJobsRequest**](ListClusterJobsRequest.md)|  | 
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

[**ListClusterJobsResult**](ListClusterJobsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listClusters

> ListClustersResult listClusters(xAmzTarget, listClustersRequest, opts)



Returns an array of &lt;code&gt;ClusterListEntry&lt;/code&gt; objects of the specified length. Each &lt;code&gt;ClusterListEntry&lt;/code&gt; object contains a cluster&#39;s state, a cluster&#39;s ID, and other important status information.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listClustersRequest = new AmazonImportExportSnowball.ListClustersRequest(); // ListClustersRequest | 
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
apiInstance.listClusters(xAmzTarget, listClustersRequest, opts, (error, data, response) => {
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
 **listClustersRequest** | [**ListClustersRequest**](ListClustersRequest.md)|  | 
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

[**ListClustersResult**](ListClustersResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCompatibleImages

> ListCompatibleImagesResult listCompatibleImages(xAmzTarget, listCompatibleImagesRequest, opts)



This action returns a list of the different Amazon EC2-compatible Amazon Machine Images (AMIs) that are owned by your Amazon Web Services accountthat would be supported for use on a Snow device. Currently, supported AMIs are based on the Amazon Linux-2, Ubuntu 20.04 LTS - Focal, or Ubuntu 22.04 LTS - Jammy images, available on the Amazon Web Services Marketplace. Ubuntu 16.04 LTS - Xenial (HVM) images are no longer supported in the Market, but still supported for use on devices through Amazon EC2 VM Import/Export and running locally in AMIs.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listCompatibleImagesRequest = new AmazonImportExportSnowball.ListCompatibleImagesRequest(); // ListCompatibleImagesRequest | 
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
apiInstance.listCompatibleImages(xAmzTarget, listCompatibleImagesRequest, opts, (error, data, response) => {
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
 **listCompatibleImagesRequest** | [**ListCompatibleImagesRequest**](ListCompatibleImagesRequest.md)|  | 
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

[**ListCompatibleImagesResult**](ListCompatibleImagesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listJobs

> ListJobsResult listJobs(xAmzTarget, listJobsRequest, opts)



Returns an array of &lt;code&gt;JobListEntry&lt;/code&gt; objects of the specified length. Each &lt;code&gt;JobListEntry&lt;/code&gt; object contains a job&#39;s state, a job&#39;s ID, and a value that indicates whether the job is a job part, in the case of export jobs. Calling this API action in one of the US regions will return jobs from the list of all jobs associated with this account in all US regions.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listJobsRequest = new AmazonImportExportSnowball.ListJobsRequest(); // ListJobsRequest | 
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
apiInstance.listJobs(xAmzTarget, listJobsRequest, opts, (error, data, response) => {
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
 **listJobsRequest** | [**ListJobsRequest**](ListJobsRequest.md)|  | 
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

[**ListJobsResult**](ListJobsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listLongTermPricing

> ListLongTermPricingResult listLongTermPricing(xAmzTarget, listLongTermPricingRequest, opts)



Lists all long-term pricing types.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listLongTermPricingRequest = new AmazonImportExportSnowball.ListLongTermPricingRequest(); // ListLongTermPricingRequest | 
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
apiInstance.listLongTermPricing(xAmzTarget, listLongTermPricingRequest, opts, (error, data, response) => {
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
 **listLongTermPricingRequest** | [**ListLongTermPricingRequest**](ListLongTermPricingRequest.md)|  | 
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

[**ListLongTermPricingResult**](ListLongTermPricingResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPickupLocations

> ListPickupLocationsResult listPickupLocations(xAmzTarget, listPickupLocationsRequest, opts)



A list of locations from which the customer can choose to pickup a device.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPickupLocationsRequest = new AmazonImportExportSnowball.ListPickupLocationsRequest(); // ListPickupLocationsRequest | 
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
apiInstance.listPickupLocations(xAmzTarget, listPickupLocationsRequest, opts, (error, data, response) => {
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
 **listPickupLocationsRequest** | [**ListPickupLocationsRequest**](ListPickupLocationsRequest.md)|  | 
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

[**ListPickupLocationsResult**](ListPickupLocationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listServiceVersions

> ListServiceVersionsResult listServiceVersions(xAmzTarget, listServiceVersionsRequest, opts)



Lists all supported versions for Snow on-device services. Returns an array of &lt;code&gt;ServiceVersion&lt;/code&gt; object containing the supported versions for a particular service.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listServiceVersionsRequest = new AmazonImportExportSnowball.ListServiceVersionsRequest(); // ListServiceVersionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.listServiceVersions(xAmzTarget, listServiceVersionsRequest, opts, (error, data, response) => {
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
 **listServiceVersionsRequest** | [**ListServiceVersionsRequest**](ListServiceVersionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ListServiceVersionsResult**](ListServiceVersionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCluster

> Object updateCluster(xAmzTarget, updateClusterRequest, opts)



While a cluster&#39;s &lt;code&gt;ClusterState&lt;/code&gt; value is in the &lt;code&gt;AwaitingQuorum&lt;/code&gt; state, you can update some of the information associated with a cluster. Once the cluster changes to a different job state, usually 60 minutes after the cluster being created, this action is no longer available.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateClusterRequest = new AmazonImportExportSnowball.UpdateClusterRequest(); // UpdateClusterRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCluster(xAmzTarget, updateClusterRequest, opts, (error, data, response) => {
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
 **updateClusterRequest** | [**UpdateClusterRequest**](UpdateClusterRequest.md)|  | 
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


## updateJob

> Object updateJob(xAmzTarget, updateJobRequest, opts)



While a job&#39;s &lt;code&gt;JobState&lt;/code&gt; value is &lt;code&gt;New&lt;/code&gt;, you can update some of the information associated with a job. Once the job changes to a different job state, usually within 60 minutes of the job being created, this action is no longer available.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateJobRequest = new AmazonImportExportSnowball.UpdateJobRequest(); // UpdateJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJob(xAmzTarget, updateJobRequest, opts, (error, data, response) => {
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
 **updateJobRequest** | [**UpdateJobRequest**](UpdateJobRequest.md)|  | 
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


## updateJobShipmentState

> Object updateJobShipmentState(xAmzTarget, updateJobShipmentStateRequest, opts)



Updates the state when a shipment state changes to a different state.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateJobShipmentStateRequest = new AmazonImportExportSnowball.UpdateJobShipmentStateRequest(); // UpdateJobShipmentStateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJobShipmentState(xAmzTarget, updateJobShipmentStateRequest, opts, (error, data, response) => {
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
 **updateJobShipmentStateRequest** | [**UpdateJobShipmentStateRequest**](UpdateJobShipmentStateRequest.md)|  | 
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


## updateLongTermPricing

> Object updateLongTermPricing(xAmzTarget, updateLongTermPricingRequest, opts)



Updates the long-term pricing type.

### Example

```javascript
import AmazonImportExportSnowball from 'amazon_import_export_snowball';
let defaultClient = AmazonImportExportSnowball.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonImportExportSnowball.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateLongTermPricingRequest = new AmazonImportExportSnowball.UpdateLongTermPricingRequest(); // UpdateLongTermPricingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateLongTermPricing(xAmzTarget, updateLongTermPricingRequest, opts, (error, data, response) => {
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
 **updateLongTermPricingRequest** | [**UpdateLongTermPricingRequest**](UpdateLongTermPricingRequest.md)|  | 
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

