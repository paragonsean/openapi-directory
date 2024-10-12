# AwsArcZonalShift.DefaultApi

All URIs are relative to *http://arc-zonal-shift.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancelZonalShift**](DefaultApi.md#cancelZonalShift) | **DELETE** /zonalshifts/{zonalShiftId} | 
[**getManagedResource**](DefaultApi.md#getManagedResource) | **GET** /managedresources/{resourceIdentifier} | 
[**listManagedResources**](DefaultApi.md#listManagedResources) | **GET** /managedresources | 
[**listZonalShifts**](DefaultApi.md#listZonalShifts) | **GET** /zonalshifts | 
[**startZonalShift**](DefaultApi.md#startZonalShift) | **POST** /zonalshifts | 
[**updateZonalShift**](DefaultApi.md#updateZonalShift) | **PATCH** /zonalshifts/{zonalShiftId} | 



## cancelZonalShift

> ZonalShift cancelZonalShift(zonalShiftId, opts)



Cancel a zonal shift in Amazon Route 53 Application Recovery Controller that you&#39;ve started for a resource in your AWS account in an AWS Region. 

### Example

```javascript
import AwsArcZonalShift from 'aws_arc_zonal_shift';
let defaultClient = AwsArcZonalShift.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsArcZonalShift.DefaultApi();
let zonalShiftId = "zonalShiftId_example"; // String | The internally-generated identifier of a zonal shift.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelZonalShift(zonalShiftId, opts, (error, data, response) => {
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
 **zonalShiftId** | **String**| The internally-generated identifier of a zonal shift. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ZonalShift**](ZonalShift.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getManagedResource

> GetManagedResourceResponse getManagedResource(resourceIdentifier, opts)



&lt;p&gt;Get information about a resource that&#39;s been registered for zonal shifts with Amazon Route 53 Application Recovery Controller in this AWS Region. Resources that are registered for zonal shifts are managed resources in Route 53 ARC.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt;

### Example

```javascript
import AwsArcZonalShift from 'aws_arc_zonal_shift';
let defaultClient = AwsArcZonalShift.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsArcZonalShift.DefaultApi();
let resourceIdentifier = "resourceIdentifier_example"; // String | <p>The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.</p> <p>At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getManagedResource(resourceIdentifier, opts, (error, data, response) => {
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
 **resourceIdentifier** | **String**| &lt;p&gt;The identifier for the resource to include in a zonal shift. The identifier is the Amazon Resource Name (ARN) for the resource.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetManagedResourceResponse**](GetManagedResourceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listManagedResources

> ListManagedResourcesResponse listManagedResources(opts)



Lists all the resources in your AWS account in this AWS Region that are managed for zonal shifts in Amazon Route 53 Application Recovery Controller, and information about them. The information includes their Amazon Resource Names (ARNs), the Availability Zones the resources are deployed in, and the resource name.

### Example

```javascript
import AwsArcZonalShift from 'aws_arc_zonal_shift';
let defaultClient = AwsArcZonalShift.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsArcZonalShift.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The number of objects that you want to return with this call.
  'nextToken': "nextToken_example" // String | Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.
};
apiInstance.listManagedResources(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The number of objects that you want to return with this call. | [optional] 
 **nextToken** | **String**| Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 

### Return type

[**ListManagedResourcesResponse**](ListManagedResourcesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listZonalShifts

> ListZonalShiftsResponse listZonalShifts(opts)



Lists all the active zonal shifts in Amazon Route 53 Application Recovery Controller in your AWS account in this AWS Region.

### Example

```javascript
import AwsArcZonalShift from 'aws_arc_zonal_shift';
let defaultClient = AwsArcZonalShift.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsArcZonalShift.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The number of objects that you want to return with this call.
  'nextToken': "nextToken_example", // String | Specifies that you want to receive the next page of results. Valid only if you received a <code>NextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>NextToken</code> response to request the next page of results.
  'status': "status_example" // String | <p>A status for a zonal shift.</p> <p>The <code>Status</code> for a zonal shift can have one of the following values:</p> <ul> <li> <p> <b>ACTIVE</b>: The zonal shift is started and active.</p> </li> <li> <p> <b>EXPIRED</b>: The zonal shift has expired (the expiry time was exceeded).</p> </li> <li> <p> <b>CANCELED</b>: The zonal shift was canceled.</p> </li> </ul>
};
apiInstance.listZonalShifts(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The number of objects that you want to return with this call. | [optional] 
 **nextToken** | **String**| Specifies that you want to receive the next page of results. Valid only if you received a &lt;code&gt;NextToken&lt;/code&gt; response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call&#39;s &lt;code&gt;NextToken&lt;/code&gt; response to request the next page of results. | [optional] 
 **status** | **String**| &lt;p&gt;A status for a zonal shift.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;Status&lt;/code&gt; for a zonal shift can have one of the following values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;ACTIVE&lt;/b&gt;: The zonal shift is started and active.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;EXPIRED&lt;/b&gt;: The zonal shift has expired (the expiry time was exceeded).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;CANCELED&lt;/b&gt;: The zonal shift was canceled.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; | [optional] 

### Return type

[**ListZonalShiftsResponse**](ListZonalShiftsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startZonalShift

> ZonalShift startZonalShift(startZonalShiftRequest, opts)



&lt;p&gt;You start a zonal shift to temporarily move load balancer traffic away from an Availability Zone in a AWS Region, to help your application recover immediately, for example, from a developer&#39;s bad code deployment or from an AWS infrastructure failure in a single Availability Zone. You can start a zonal shift in Route 53 ARC only for managed resources in your account in an AWS Region. Resources are automatically registered with Route 53 ARC by AWS services.&lt;/p&gt; &lt;p&gt;At this time, you can only start a zonal shift for Network Load Balancers and Application Load Balancers with cross-zone load balancing turned off.&lt;/p&gt; &lt;p&gt;When you start a zonal shift, traffic for the resource is no longer routed to the Availability Zone. The zonal shift is created immediately in Route 53 ARC. However, it can take a short time, typically up to a few minutes, for existing, in-progress connections in the Availability Zone to complete.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html\&quot;&gt;Zonal shift&lt;/a&gt; in the Amazon Route 53 Application Recovery Controller Developer Guide.&lt;/p&gt;

### Example

```javascript
import AwsArcZonalShift from 'aws_arc_zonal_shift';
let defaultClient = AwsArcZonalShift.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsArcZonalShift.DefaultApi();
let startZonalShiftRequest = new AwsArcZonalShift.StartZonalShiftRequest(); // StartZonalShiftRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startZonalShift(startZonalShiftRequest, opts, (error, data, response) => {
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
 **startZonalShiftRequest** | [**StartZonalShiftRequest**](StartZonalShiftRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ZonalShift**](ZonalShift.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateZonalShift

> ZonalShift updateZonalShift(zonalShiftId, updateZonalShiftRequest, opts)



Update an active zonal shift in Amazon Route 53 Application Recovery Controller in your AWS account. You can update a zonal shift to set a new expiration, or edit or replace the comment for the zonal shift. 

### Example

```javascript
import AwsArcZonalShift from 'aws_arc_zonal_shift';
let defaultClient = AwsArcZonalShift.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsArcZonalShift.DefaultApi();
let zonalShiftId = "zonalShiftId_example"; // String | The identifier of a zonal shift.
let updateZonalShiftRequest = new AwsArcZonalShift.UpdateZonalShiftRequest(); // UpdateZonalShiftRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateZonalShift(zonalShiftId, updateZonalShiftRequest, opts, (error, data, response) => {
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
 **zonalShiftId** | **String**| The identifier of a zonal shift. | 
 **updateZonalShiftRequest** | [**UpdateZonalShiftRequest**](UpdateZonalShiftRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ZonalShift**](ZonalShift.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

