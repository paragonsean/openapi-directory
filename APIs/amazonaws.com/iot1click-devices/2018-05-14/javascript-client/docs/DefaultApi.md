# AwsIoT1ClickDevicesService.DefaultApi

All URIs are relative to *http://devices.iot1click.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**claimDevicesByClaimCode**](DefaultApi.md#claimDevicesByClaimCode) | **PUT** /claims/{claimCode} | 
[**describeDevice**](DefaultApi.md#describeDevice) | **GET** /devices/{deviceId} | 
[**finalizeDeviceClaim**](DefaultApi.md#finalizeDeviceClaim) | **PUT** /devices/{deviceId}/finalize-claim | 
[**getDeviceMethods**](DefaultApi.md#getDeviceMethods) | **GET** /devices/{deviceId}/methods | 
[**initiateDeviceClaim**](DefaultApi.md#initiateDeviceClaim) | **PUT** /devices/{deviceId}/initiate-claim | 
[**invokeDeviceMethod**](DefaultApi.md#invokeDeviceMethod) | **POST** /devices/{deviceId}/methods | 
[**listDeviceEvents**](DefaultApi.md#listDeviceEvents) | **GET** /devices/{deviceId}/events#fromTimeStamp&amp;toTimeStamp | 
[**listDevices**](DefaultApi.md#listDevices) | **GET** /devices | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resource-arn} | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resource-arn} | 
[**unclaimDevice**](DefaultApi.md#unclaimDevice) | **PUT** /devices/{deviceId}/unclaim | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resource-arn}#tagKeys | 
[**updateDeviceState**](DefaultApi.md#updateDeviceState) | **PUT** /devices/{deviceId}/state | 



## claimDevicesByClaimCode

> ClaimDevicesByClaimCodeResponse claimDevicesByClaimCode(claimCode, opts)



Adds device(s) to your account (i.e., claim one or more devices) if and only if you  received a claim code with the device(s).

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let claimCode = "claimCode_example"; // String | The claim code, starting with \"C-\", as provided by the device manufacturer.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.claimDevicesByClaimCode(claimCode, opts, (error, data, response) => {
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
 **claimCode** | **String**| The claim code, starting with \&quot;C-\&quot;, as provided by the device manufacturer. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**ClaimDevicesByClaimCodeResponse**](ClaimDevicesByClaimCodeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeDevice

> DescribeDeviceResponse describeDevice(deviceId, opts)



Given a device ID, returns a DescribeDeviceResponse object describing the  details of the device.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeDevice(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeDeviceResponse**](DescribeDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## finalizeDeviceClaim

> FinalizeDeviceClaimResponse finalizeDeviceClaim(deviceId, finalizeDeviceClaimRequest, opts)



&lt;p&gt;Given a device ID, finalizes the claim request for the associated device.&lt;/p&gt;&lt;note&gt;  &lt;p&gt;Claiming a device consists of initiating a claim, then publishing a device event,  and finalizing the claim. For a device of type button, a device event can  be published by simply clicking the device.&lt;/p&gt;  &lt;/note&gt;

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let finalizeDeviceClaimRequest = new AwsIoT1ClickDevicesService.FinalizeDeviceClaimRequest(); // FinalizeDeviceClaimRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.finalizeDeviceClaim(deviceId, finalizeDeviceClaimRequest, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **finalizeDeviceClaimRequest** | [**FinalizeDeviceClaimRequest**](FinalizeDeviceClaimRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**FinalizeDeviceClaimResponse**](FinalizeDeviceClaimResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getDeviceMethods

> GetDeviceMethodsResponse getDeviceMethods(deviceId, opts)



Given a device ID, returns the invokable methods associated with the device.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeviceMethods(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDeviceMethodsResponse**](GetDeviceMethodsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## initiateDeviceClaim

> InitiateDeviceClaimResponse initiateDeviceClaim(deviceId, opts)



&lt;p&gt;Given a device ID, initiates a claim request for the associated device.&lt;/p&gt;&lt;note&gt;  &lt;p&gt;Claiming a device consists of initiating a claim, then publishing a device event,  and finalizing the claim. For a device of type button, a device event can  be published by simply clicking the device.&lt;/p&gt;  &lt;/note&gt;

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.initiateDeviceClaim(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InitiateDeviceClaimResponse**](InitiateDeviceClaimResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## invokeDeviceMethod

> InvokeDeviceMethodResponse invokeDeviceMethod(deviceId, invokeDeviceMethodRequest, opts)



Given a device ID, issues a request to invoke a named device method (with possible  parameters). See the \&quot;Example POST\&quot; code snippet below.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let invokeDeviceMethodRequest = new AwsIoT1ClickDevicesService.InvokeDeviceMethodRequest(); // InvokeDeviceMethodRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.invokeDeviceMethod(deviceId, invokeDeviceMethodRequest, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **invokeDeviceMethodRequest** | [**InvokeDeviceMethodRequest**](InvokeDeviceMethodRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**InvokeDeviceMethodResponse**](InvokeDeviceMethodResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listDeviceEvents

> ListDeviceEventsResponse listDeviceEvents(deviceId, fromTimeStamp, toTimeStamp, opts)



Using a device ID, returns a DeviceEventsResponse object containing an  array of events for the device.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let fromTimeStamp = new Date("2013-10-20T19:20:30+01:00"); // Date | The start date for the device event query, in ISO8061 format. For example,  2018-03-28T15:45:12.880Z  
let toTimeStamp = new Date("2013-10-20T19:20:30+01:00"); // Date | The end date for the device event query, in ISO8061 format. For example,  2018-03-28T15:45:12.880Z  
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of results to return per request. If not set, a default value of  100 is used.
  'nextToken': "nextToken_example" // String | The token to retrieve the next set of results.
};
apiInstance.listDeviceEvents(deviceId, fromTimeStamp, toTimeStamp, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **fromTimeStamp** | **Date**| The start date for the device event query, in ISO8061 format. For example,  2018-03-28T15:45:12.880Z   | 
 **toTimeStamp** | **Date**| The end date for the device event query, in ISO8061 format. For example,  2018-03-28T15:45:12.880Z   | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per request. If not set, a default value of  100 is used. | [optional] 
 **nextToken** | **String**| The token to retrieve the next set of results. | [optional] 

### Return type

[**ListDeviceEventsResponse**](ListDeviceEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDevices

> ListDevicesResponse listDevices(opts)



Lists the 1-Click compatible devices associated with your AWS account.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'deviceType': "deviceType_example", // String | The type of the device, such as \"button\".
  'maxResults': 56, // Number | The maximum number of results to return per request. If not set, a default value of  100 is used.
  'nextToken': "nextToken_example" // String | The token to retrieve the next set of results.
};
apiInstance.listDevices(opts, (error, data, response) => {
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
 **deviceType** | **String**| The type of the device, such as \&quot;button\&quot;. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per request. If not set, a default value of  100 is used. | [optional] 
 **nextToken** | **String**| The token to retrieve the next set of results. | [optional] 

### Return type

[**ListDevicesResponse**](ListDevicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Lists the tags associated with the specified resource ARN.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource.
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
 **resourceArn** | **String**| The ARN of the resource. | 
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

- **Content-Type**: Not defined
- **Accept**: application/json


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



Adds or updates the tags associated with the resource ARN. See &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/iot-1-click/latest/developerguide/1click-appendix.html#1click-limits\&quot;&gt;AWS IoT 1-Click Service Limits&lt;/a&gt; for the maximum number of tags allowed per  resource.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource.
let tagResourceRequest = new AwsIoT1ClickDevicesService.TagResourceRequest(); // TagResourceRequest | 
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The ARN of the resource. | 
 **tagResourceRequest** | [**TagResourceRequest**](TagResourceRequest.md)|  | 
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


## unclaimDevice

> UnclaimDeviceResponse unclaimDevice(deviceId, opts)



Disassociates a device from your AWS account using its device ID.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.unclaimDevice(deviceId, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UnclaimDeviceResponse**](UnclaimDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Using tag keys, deletes the tags (key/value pairs) associated with the specified  resource ARN.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource.
let tagKeys = ["null"]; // [String] | A collections of tag keys. For example, {\"key1\",\"key2\"}
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
    console.log('API called successfully.');
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resourceArn** | **String**| The ARN of the resource. | 
 **tagKeys** | [**[String]**](String.md)| A collections of tag keys. For example, {\&quot;key1\&quot;,\&quot;key2\&quot;} | 
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


## updateDeviceState

> Object updateDeviceState(deviceId, updateDeviceStateRequest, opts)



Using a Boolean value (true or false), this operation  enables or disables the device given a device ID.

### Example

```javascript
import AwsIoT1ClickDevicesService from 'aws_io_t_1_click_devices_service';
let defaultClient = AwsIoT1ClickDevicesService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsIoT1ClickDevicesService.DefaultApi();
let deviceId = "deviceId_example"; // String | The unique identifier of the device.
let updateDeviceStateRequest = new AwsIoT1ClickDevicesService.UpdateDeviceStateRequest(); // UpdateDeviceStateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDeviceState(deviceId, updateDeviceStateRequest, opts, (error, data, response) => {
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
 **deviceId** | **String**| The unique identifier of the device. | 
 **updateDeviceStateRequest** | [**UpdateDeviceStateRequest**](UpdateDeviceStateRequest.md)|  | 
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

