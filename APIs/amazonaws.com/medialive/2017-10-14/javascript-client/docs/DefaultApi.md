# AwsElementalMediaLive.DefaultApi

All URIs are relative to *http://medialive.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptInputDeviceTransfer**](DefaultApi.md#acceptInputDeviceTransfer) | **POST** /prod/inputDevices/{inputDeviceId}/accept | 
[**batchDelete**](DefaultApi.md#batchDelete) | **POST** /prod/batch/delete | 
[**batchStart**](DefaultApi.md#batchStart) | **POST** /prod/batch/start | 
[**batchStop**](DefaultApi.md#batchStop) | **POST** /prod/batch/stop | 
[**batchUpdateSchedule**](DefaultApi.md#batchUpdateSchedule) | **PUT** /prod/channels/{channelId}/schedule | 
[**cancelInputDeviceTransfer**](DefaultApi.md#cancelInputDeviceTransfer) | **POST** /prod/inputDevices/{inputDeviceId}/cancel | 
[**claimDevice**](DefaultApi.md#claimDevice) | **POST** /prod/claimDevice | 
[**createChannel**](DefaultApi.md#createChannel) | **POST** /prod/channels | 
[**createInput**](DefaultApi.md#createInput) | **POST** /prod/inputs | 
[**createInputSecurityGroup**](DefaultApi.md#createInputSecurityGroup) | **POST** /prod/inputSecurityGroups | 
[**createMultiplex**](DefaultApi.md#createMultiplex) | **POST** /prod/multiplexes | 
[**createMultiplexProgram**](DefaultApi.md#createMultiplexProgram) | **POST** /prod/multiplexes/{multiplexId}/programs | 
[**createPartnerInput**](DefaultApi.md#createPartnerInput) | **POST** /prod/inputs/{inputId}/partners | 
[**createTags**](DefaultApi.md#createTags) | **POST** /prod/tags/{resource-arn} | 
[**deleteChannel**](DefaultApi.md#deleteChannel) | **DELETE** /prod/channels/{channelId} | 
[**deleteInput**](DefaultApi.md#deleteInput) | **DELETE** /prod/inputs/{inputId} | 
[**deleteInputSecurityGroup**](DefaultApi.md#deleteInputSecurityGroup) | **DELETE** /prod/inputSecurityGroups/{inputSecurityGroupId} | 
[**deleteMultiplex**](DefaultApi.md#deleteMultiplex) | **DELETE** /prod/multiplexes/{multiplexId} | 
[**deleteMultiplexProgram**](DefaultApi.md#deleteMultiplexProgram) | **DELETE** /prod/multiplexes/{multiplexId}/programs/{programName} | 
[**deleteReservation**](DefaultApi.md#deleteReservation) | **DELETE** /prod/reservations/{reservationId} | 
[**deleteSchedule**](DefaultApi.md#deleteSchedule) | **DELETE** /prod/channels/{channelId}/schedule | 
[**deleteTags**](DefaultApi.md#deleteTags) | **DELETE** /prod/tags/{resource-arn}#tagKeys | 
[**describeAccountConfiguration**](DefaultApi.md#describeAccountConfiguration) | **GET** /prod/accountConfiguration | 
[**describeChannel**](DefaultApi.md#describeChannel) | **GET** /prod/channels/{channelId} | 
[**describeInput**](DefaultApi.md#describeInput) | **GET** /prod/inputs/{inputId} | 
[**describeInputDevice**](DefaultApi.md#describeInputDevice) | **GET** /prod/inputDevices/{inputDeviceId} | 
[**describeInputDeviceThumbnail**](DefaultApi.md#describeInputDeviceThumbnail) | **GET** /prod/inputDevices/{inputDeviceId}/thumbnailData#accept | 
[**describeInputSecurityGroup**](DefaultApi.md#describeInputSecurityGroup) | **GET** /prod/inputSecurityGroups/{inputSecurityGroupId} | 
[**describeMultiplex**](DefaultApi.md#describeMultiplex) | **GET** /prod/multiplexes/{multiplexId} | 
[**describeMultiplexProgram**](DefaultApi.md#describeMultiplexProgram) | **GET** /prod/multiplexes/{multiplexId}/programs/{programName} | 
[**describeOffering**](DefaultApi.md#describeOffering) | **GET** /prod/offerings/{offeringId} | 
[**describeReservation**](DefaultApi.md#describeReservation) | **GET** /prod/reservations/{reservationId} | 
[**describeSchedule**](DefaultApi.md#describeSchedule) | **GET** /prod/channels/{channelId}/schedule | 
[**describeThumbnails**](DefaultApi.md#describeThumbnails) | **GET** /prod/channels/{channelId}/thumbnails#pipelineId&amp;thumbnailType | 
[**listChannels**](DefaultApi.md#listChannels) | **GET** /prod/channels | 
[**listInputDeviceTransfers**](DefaultApi.md#listInputDeviceTransfers) | **GET** /prod/inputDeviceTransfers#transferType | 
[**listInputDevices**](DefaultApi.md#listInputDevices) | **GET** /prod/inputDevices | 
[**listInputSecurityGroups**](DefaultApi.md#listInputSecurityGroups) | **GET** /prod/inputSecurityGroups | 
[**listInputs**](DefaultApi.md#listInputs) | **GET** /prod/inputs | 
[**listMultiplexPrograms**](DefaultApi.md#listMultiplexPrograms) | **GET** /prod/multiplexes/{multiplexId}/programs | 
[**listMultiplexes**](DefaultApi.md#listMultiplexes) | **GET** /prod/multiplexes | 
[**listOfferings**](DefaultApi.md#listOfferings) | **GET** /prod/offerings | 
[**listReservations**](DefaultApi.md#listReservations) | **GET** /prod/reservations | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /prod/tags/{resource-arn} | 
[**purchaseOffering**](DefaultApi.md#purchaseOffering) | **POST** /prod/offerings/{offeringId}/purchase | 
[**rebootInputDevice**](DefaultApi.md#rebootInputDevice) | **POST** /prod/inputDevices/{inputDeviceId}/reboot | 
[**rejectInputDeviceTransfer**](DefaultApi.md#rejectInputDeviceTransfer) | **POST** /prod/inputDevices/{inputDeviceId}/reject | 
[**startChannel**](DefaultApi.md#startChannel) | **POST** /prod/channels/{channelId}/start | 
[**startInputDeviceMaintenanceWindow**](DefaultApi.md#startInputDeviceMaintenanceWindow) | **POST** /prod/inputDevices/{inputDeviceId}/startInputDeviceMaintenanceWindow | 
[**startMultiplex**](DefaultApi.md#startMultiplex) | **POST** /prod/multiplexes/{multiplexId}/start | 
[**stopChannel**](DefaultApi.md#stopChannel) | **POST** /prod/channels/{channelId}/stop | 
[**stopMultiplex**](DefaultApi.md#stopMultiplex) | **POST** /prod/multiplexes/{multiplexId}/stop | 
[**transferInputDevice**](DefaultApi.md#transferInputDevice) | **POST** /prod/inputDevices/{inputDeviceId}/transfer | 
[**updateAccountConfiguration**](DefaultApi.md#updateAccountConfiguration) | **PUT** /prod/accountConfiguration | 
[**updateChannel**](DefaultApi.md#updateChannel) | **PUT** /prod/channels/{channelId} | 
[**updateChannelClass**](DefaultApi.md#updateChannelClass) | **PUT** /prod/channels/{channelId}/channelClass | 
[**updateInput**](DefaultApi.md#updateInput) | **PUT** /prod/inputs/{inputId} | 
[**updateInputDevice**](DefaultApi.md#updateInputDevice) | **PUT** /prod/inputDevices/{inputDeviceId} | 
[**updateInputSecurityGroup**](DefaultApi.md#updateInputSecurityGroup) | **PUT** /prod/inputSecurityGroups/{inputSecurityGroupId} | 
[**updateMultiplex**](DefaultApi.md#updateMultiplex) | **PUT** /prod/multiplexes/{multiplexId} | 
[**updateMultiplexProgram**](DefaultApi.md#updateMultiplexProgram) | **PUT** /prod/multiplexes/{multiplexId}/programs/{programName} | 
[**updateReservation**](DefaultApi.md#updateReservation) | **PUT** /prod/reservations/{reservationId} | 



## acceptInputDeviceTransfer

> Object acceptInputDeviceTransfer(inputDeviceId, opts)



Accept an incoming input device transfer. The ownership of the device will transfer to your AWS account.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of the input device to accept. For example, hd-123456789abcdef.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acceptInputDeviceTransfer(inputDeviceId, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of the input device to accept. For example, hd-123456789abcdef. | 
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


## batchDelete

> BatchDeleteResponse batchDelete(batchDeleteRequest, opts)



Starts delete of resources.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let batchDeleteRequest = new AwsElementalMediaLive.BatchDeleteRequest(); // BatchDeleteRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchDelete(batchDeleteRequest, opts, (error, data, response) => {
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
 **batchDeleteRequest** | [**BatchDeleteRequest**](BatchDeleteRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchDeleteResponse**](BatchDeleteResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchStart

> BatchStartResponse batchStart(batchStartRequest, opts)



Starts existing resources

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let batchStartRequest = new AwsElementalMediaLive.BatchStartRequest(); // BatchStartRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchStart(batchStartRequest, opts, (error, data, response) => {
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
 **batchStartRequest** | [**BatchStartRequest**](BatchStartRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchStartResponse**](BatchStartResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchStop

> BatchStopResponse batchStop(batchStartRequest, opts)



Stops running resources

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let batchStartRequest = new AwsElementalMediaLive.BatchStartRequest(); // BatchStartRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchStop(batchStartRequest, opts, (error, data, response) => {
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
 **batchStartRequest** | [**BatchStartRequest**](BatchStartRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchStopResponse**](BatchStopResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## batchUpdateSchedule

> BatchUpdateScheduleResponse batchUpdateSchedule(channelId, batchUpdateScheduleRequest, opts)



Update a channel schedule

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | Id of the channel whose schedule is being updated.
let batchUpdateScheduleRequest = new AwsElementalMediaLive.BatchUpdateScheduleRequest(); // BatchUpdateScheduleRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchUpdateSchedule(channelId, batchUpdateScheduleRequest, opts, (error, data, response) => {
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
 **channelId** | **String**| Id of the channel whose schedule is being updated. | 
 **batchUpdateScheduleRequest** | [**BatchUpdateScheduleRequest**](BatchUpdateScheduleRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchUpdateScheduleResponse**](BatchUpdateScheduleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## cancelInputDeviceTransfer

> Object cancelInputDeviceTransfer(inputDeviceId, opts)



Cancel an input device transfer that you have requested.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of the input device to cancel. For example, hd-123456789abcdef.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.cancelInputDeviceTransfer(inputDeviceId, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of the input device to cancel. For example, hd-123456789abcdef. | 
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


## claimDevice

> Object claimDevice(claimDeviceRequest, opts)



Send a request to claim an AWS Elemental device that you have purchased from a third-party vendor. After the request succeeds, you will own the device.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let claimDeviceRequest = new AwsElementalMediaLive.ClaimDeviceRequest(); // ClaimDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.claimDevice(claimDeviceRequest, opts, (error, data, response) => {
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
 **claimDeviceRequest** | [**ClaimDeviceRequest**](ClaimDeviceRequest.md)|  | 
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


## createChannel

> CreateChannelResponse createChannel(createChannelRequest, opts)



Creates a new channel

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let createChannelRequest = new AwsElementalMediaLive.CreateChannelRequest(); // CreateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createChannel(createChannelRequest, opts, (error, data, response) => {
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
 **createChannelRequest** | [**CreateChannelRequest**](CreateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateChannelResponse**](CreateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInput

> CreateInputResponse createInput(createInputRequest, opts)



Create an input

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let createInputRequest = new AwsElementalMediaLive.CreateInputRequest(); // CreateInputRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInput(createInputRequest, opts, (error, data, response) => {
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
 **createInputRequest** | [**CreateInputRequest**](CreateInputRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateInputResponse**](CreateInputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createInputSecurityGroup

> CreateInputSecurityGroupResponse createInputSecurityGroup(createInputSecurityGroupRequest, opts)



Creates a Input Security Group

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let createInputSecurityGroupRequest = new AwsElementalMediaLive.CreateInputSecurityGroupRequest(); // CreateInputSecurityGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInputSecurityGroup(createInputSecurityGroupRequest, opts, (error, data, response) => {
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
 **createInputSecurityGroupRequest** | [**CreateInputSecurityGroupRequest**](CreateInputSecurityGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateInputSecurityGroupResponse**](CreateInputSecurityGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMultiplex

> CreateMultiplexResponse createMultiplex(createMultiplexRequest, opts)



Create a new multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let createMultiplexRequest = new AwsElementalMediaLive.CreateMultiplexRequest(); // CreateMultiplexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMultiplex(createMultiplexRequest, opts, (error, data, response) => {
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
 **createMultiplexRequest** | [**CreateMultiplexRequest**](CreateMultiplexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMultiplexResponse**](CreateMultiplexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createMultiplexProgram

> CreateMultiplexProgramResponse createMultiplexProgram(multiplexId, createMultiplexProgramRequest, opts)



Create a new program in the multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | ID of the multiplex where the program is to be created.
let createMultiplexProgramRequest = new AwsElementalMediaLive.CreateMultiplexProgramRequest(); // CreateMultiplexProgramRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createMultiplexProgram(multiplexId, createMultiplexProgramRequest, opts, (error, data, response) => {
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
 **multiplexId** | **String**| ID of the multiplex where the program is to be created. | 
 **createMultiplexProgramRequest** | [**CreateMultiplexProgramRequest**](CreateMultiplexProgramRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateMultiplexProgramResponse**](CreateMultiplexProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPartnerInput

> CreatePartnerInputResponse createPartnerInput(inputId, createPartnerInputRequest, opts)



Create a partner input

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputId = "inputId_example"; // String | Unique ID of the input.
let createPartnerInputRequest = new AwsElementalMediaLive.CreatePartnerInputRequest(); // CreatePartnerInputRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPartnerInput(inputId, createPartnerInputRequest, opts, (error, data, response) => {
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
 **inputId** | **String**| Unique ID of the input. | 
 **createPartnerInputRequest** | [**CreatePartnerInputRequest**](CreatePartnerInputRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePartnerInputResponse**](CreatePartnerInputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createTags

> createTags(resourceArn, createTagsRequest, opts)



Create tags for a resource

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let resourceArn = "resourceArn_example"; // String | 
let createTagsRequest = new AwsElementalMediaLive.CreateTagsRequest(); // CreateTagsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createTags(resourceArn, createTagsRequest, opts, (error, data, response) => {
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
 **resourceArn** | **String**|  | 
 **createTagsRequest** | [**CreateTagsRequest**](CreateTagsRequest.md)|  | 
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


## deleteChannel

> DeleteChannelResponse deleteChannel(channelId, opts)



Starts deletion of channel. The associated outputs are also deleted.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | Unique ID of the channel.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| Unique ID of the channel. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteChannelResponse**](DeleteChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteInput

> Object deleteInput(inputId, opts)



Deletes the input end point

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputId = "inputId_example"; // String | Unique ID of the input
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteInput(inputId, opts, (error, data, response) => {
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
 **inputId** | **String**| Unique ID of the input | 
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


## deleteInputSecurityGroup

> Object deleteInputSecurityGroup(inputSecurityGroupId, opts)



Deletes an Input Security Group

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputSecurityGroupId = "inputSecurityGroupId_example"; // String | The Input Security Group to delete
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteInputSecurityGroup(inputSecurityGroupId, opts, (error, data, response) => {
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
 **inputSecurityGroupId** | **String**| The Input Security Group to delete | 
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


## deleteMultiplex

> DeleteMultiplexResponse deleteMultiplex(multiplexId, opts)



Delete a multiplex. The multiplex must be idle.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMultiplex(multiplexId, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMultiplexResponse**](DeleteMultiplexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteMultiplexProgram

> DeleteMultiplexProgramResponse deleteMultiplexProgram(multiplexId, programName, opts)



Delete a program from a multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex that the program belongs to.
let programName = "programName_example"; // String | The multiplex program name.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteMultiplexProgram(multiplexId, programName, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex that the program belongs to. | 
 **programName** | **String**| The multiplex program name. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteMultiplexProgramResponse**](DeleteMultiplexProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteReservation

> DeleteReservationResponse deleteReservation(reservationId, opts)



Delete an expired reservation.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let reservationId = "reservationId_example"; // String | Unique reservation ID, e.g. '1234567'
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteReservation(reservationId, opts, (error, data, response) => {
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
 **reservationId** | **String**| Unique reservation ID, e.g. &#39;1234567&#39; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteReservationResponse**](DeleteReservationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSchedule

> Object deleteSchedule(channelId, opts)



Delete all schedule actions on a channel.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | Id of the channel whose schedule is being deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSchedule(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| Id of the channel whose schedule is being deleted. | 
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


## deleteTags

> deleteTags(resourceArn, tagKeys, opts)



Removes tags for a resource

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let resourceArn = "resourceArn_example"; // String | 
let tagKeys = ["null"]; // [String] | An array of tag keys to delete
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteTags(resourceArn, tagKeys, opts, (error, data, response) => {
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
 **resourceArn** | **String**|  | 
 **tagKeys** | [**[String]**](String.md)| An array of tag keys to delete | 
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


## describeAccountConfiguration

> DescribeAccountConfigurationResponse describeAccountConfiguration(opts)



Get account configuration

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeAccountConfiguration(opts, (error, data, response) => {
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

### Return type

[**DescribeAccountConfigurationResponse**](DescribeAccountConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeChannel

> DescribeChannelResponse describeChannel(channelId, opts)



Gets details about a channel

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | channel ID
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| channel ID | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeChannelResponse**](DescribeChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInput

> DescribeInputResponse describeInput(inputId, opts)



Produces details about an input

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputId = "inputId_example"; // String | Unique ID of the input
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInput(inputId, opts, (error, data, response) => {
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
 **inputId** | **String**| Unique ID of the input | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInputResponse**](DescribeInputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInputDevice

> DescribeInputDeviceResponse describeInputDevice(inputDeviceId, opts)



Gets the details for the input device

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of this input device. For example, hd-123456789abcdef.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInputDevice(inputDeviceId, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of this input device. For example, hd-123456789abcdef. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInputDeviceResponse**](DescribeInputDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInputDeviceThumbnail

> DescribeInputDeviceThumbnailResponse describeInputDeviceThumbnail(inputDeviceId, accept, opts)



Get the latest thumbnail data for the input device.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of this input device. For example, hd-123456789abcdef.
let accept = "accept_example"; // String | The HTTP Accept header. Indicates the requested type for the thumbnail.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInputDeviceThumbnail(inputDeviceId, accept, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of this input device. For example, hd-123456789abcdef. | 
 **accept** | **String**| The HTTP Accept header. Indicates the requested type for the thumbnail. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInputDeviceThumbnailResponse**](DescribeInputDeviceThumbnailResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeInputSecurityGroup

> DescribeInputSecurityGroupResponse describeInputSecurityGroup(inputSecurityGroupId, opts)



Produces a summary of an Input Security Group

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputSecurityGroupId = "inputSecurityGroupId_example"; // String | The id of the Input Security Group to describe
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeInputSecurityGroup(inputSecurityGroupId, opts, (error, data, response) => {
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
 **inputSecurityGroupId** | **String**| The id of the Input Security Group to describe | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeInputSecurityGroupResponse**](DescribeInputSecurityGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeMultiplex

> DescribeMultiplexResponse describeMultiplex(multiplexId, opts)



Gets details about a multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMultiplex(multiplexId, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMultiplexResponse**](DescribeMultiplexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeMultiplexProgram

> DescribeMultiplexProgramResponse describeMultiplexProgram(multiplexId, programName, opts)



Get the details for a program in a multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex that the program belongs to.
let programName = "programName_example"; // String | The name of the program.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeMultiplexProgram(multiplexId, programName, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex that the program belongs to. | 
 **programName** | **String**| The name of the program. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeMultiplexProgramResponse**](DescribeMultiplexProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeOffering

> DescribeOfferingResponse describeOffering(offeringId, opts)



Get details for an offering.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let offeringId = "offeringId_example"; // String | Unique offering ID, e.g. '87654321'
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeOffering(offeringId, opts, (error, data, response) => {
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
 **offeringId** | **String**| Unique offering ID, e.g. &#39;87654321&#39; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeOfferingResponse**](DescribeOfferingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeReservation

> DescribeReservationResponse describeReservation(reservationId, opts)



Get details for a reservation.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let reservationId = "reservationId_example"; // String | Unique reservation ID, e.g. '1234567'
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeReservation(reservationId, opts, (error, data, response) => {
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
 **reservationId** | **String**| Unique reservation ID, e.g. &#39;1234567&#39; | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeReservationResponse**](DescribeReservationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeSchedule

> DescribeScheduleResponse describeSchedule(channelId, opts)



Get a channel schedule

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | Id of the channel whose schedule is being updated.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.describeSchedule(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| Id of the channel whose schedule is being updated. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**DescribeScheduleResponse**](DescribeScheduleResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## describeThumbnails

> DescribeThumbnailsResponse describeThumbnails(channelId, pipelineId, thumbnailType, opts)



Describe the latest thumbnails data.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | Unique ID of the channel
let pipelineId = "pipelineId_example"; // String | Pipeline ID (\"0\" or \"1\")
let thumbnailType = "thumbnailType_example"; // String | thumbnail type
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeThumbnails(channelId, pipelineId, thumbnailType, opts, (error, data, response) => {
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
 **channelId** | **String**| Unique ID of the channel | 
 **pipelineId** | **String**| Pipeline ID (\&quot;0\&quot; or \&quot;1\&quot;) | 
 **thumbnailType** | **String**| thumbnail type | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeThumbnailsResponse**](DescribeThumbnailsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listChannels

> ListChannelsResponse listChannels(opts)



Produces list of channels that have been created

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listChannels(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListChannelsResponse**](ListChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInputDeviceTransfers

> ListInputDeviceTransfersResponse listInputDeviceTransfers(transferType, opts)



List input devices that are currently being transferred. List input devices that you are transferring from your AWS account or input devices that another AWS account is transferring to you.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let transferType = "transferType_example"; // String | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInputDeviceTransfers(transferType, opts, (error, data, response) => {
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
 **transferType** | **String**|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInputDeviceTransfersResponse**](ListInputDeviceTransfersResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInputDevices

> ListInputDevicesResponse listInputDevices(opts)



List input devices

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInputDevices(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInputDevicesResponse**](ListInputDevicesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInputSecurityGroups

> ListInputSecurityGroupsResponse listInputSecurityGroups(opts)



Produces a list of Input Security Groups for an account

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInputSecurityGroups(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInputSecurityGroupsResponse**](ListInputSecurityGroupsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInputs

> ListInputsResponse listInputs(opts)



Produces list of inputs that have been created

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | 
  'nextToken': "nextToken_example", // String | 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listInputs(opts, (error, data, response) => {
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
 **maxResults** | **Number**|  | [optional] 
 **nextToken** | **String**|  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListInputsResponse**](ListInputsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMultiplexPrograms

> ListMultiplexProgramsResponse listMultiplexPrograms(multiplexId, opts)



List the programs that currently exist for a specific multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex that the programs belong to.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return.
  'nextToken': "nextToken_example", // String | The token to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMultiplexPrograms(multiplexId, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex that the programs belong to. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **maxResults** | **Number**| The maximum number of items to return. | [optional] 
 **nextToken** | **String**| The token to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMultiplexProgramsResponse**](ListMultiplexProgramsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listMultiplexes

> ListMultiplexesResponse listMultiplexes(opts)



Retrieve a list of the existing multiplexes.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'maxResults': 56, // Number | The maximum number of items to return.
  'nextToken': "nextToken_example", // String | The token to retrieve the next page of results.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listMultiplexes(opts, (error, data, response) => {
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
 **maxResults** | **Number**| The maximum number of items to return. | [optional] 
 **nextToken** | **String**| The token to retrieve the next page of results. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListMultiplexesResponse**](ListMultiplexesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listOfferings

> ListOfferingsResponse listOfferings(opts)



List offerings available for purchase.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'channelClass': "channelClass_example", // String | Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE' 
  'channelConfiguration': "channelConfiguration_example", // String | Filter to offerings that match the configuration of an existing channel, e.g. '2345678' (a channel ID) 
  'codec': "codec_example", // String | Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', or 'LINK'
  'duration': "duration_example", // String | Filter by offering duration, e.g. '12'
  'maxResults': 56, // Number | 
  'maximumBitrate': "maximumBitrate_example", // String | Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS' 
  'maximumFramerate': "maximumFramerate_example", // String | Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
  'nextToken': "nextToken_example", // String | 
  'resolution': "resolution_example", // String | Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'
  'resourceType': "resourceType_example", // String | Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
  'specialFeature': "specialFeature_example", // String | Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION' 
  'videoQuality': "videoQuality_example", // String | Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM' 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listOfferings(opts, (error, data, response) => {
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
 **channelClass** | **String**| Filter by channel class, &#39;STANDARD&#39; or &#39;SINGLE_PIPELINE&#39;  | [optional] 
 **channelConfiguration** | **String**| Filter to offerings that match the configuration of an existing channel, e.g. &#39;2345678&#39; (a channel ID)  | [optional] 
 **codec** | **String**| Filter by codec, &#39;AVC&#39;, &#39;HEVC&#39;, &#39;MPEG2&#39;, &#39;AUDIO&#39;, or &#39;LINK&#39; | [optional] 
 **duration** | **String**| Filter by offering duration, e.g. &#39;12&#39; | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **maximumBitrate** | **String**| Filter by bitrate, &#39;MAX_10_MBPS&#39;, &#39;MAX_20_MBPS&#39;, or &#39;MAX_50_MBPS&#39;  | [optional] 
 **maximumFramerate** | **String**| Filter by framerate, &#39;MAX_30_FPS&#39; or &#39;MAX_60_FPS&#39; | [optional] 
 **nextToken** | **String**|  | [optional] 
 **resolution** | **String**| Filter by resolution, &#39;SD&#39;, &#39;HD&#39;, &#39;FHD&#39;, or &#39;UHD&#39; | [optional] 
 **resourceType** | **String**| Filter by resource type, &#39;INPUT&#39;, &#39;OUTPUT&#39;, &#39;MULTIPLEX&#39;, or &#39;CHANNEL&#39; | [optional] 
 **specialFeature** | **String**| Filter by special feature, &#39;ADVANCED_AUDIO&#39; or &#39;AUDIO_NORMALIZATION&#39;  | [optional] 
 **videoQuality** | **String**| Filter by video quality, &#39;STANDARD&#39;, &#39;ENHANCED&#39;, or &#39;PREMIUM&#39;  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListOfferingsResponse**](ListOfferingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listReservations

> ListReservationsResponse listReservations(opts)



List purchased reservations.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'channelClass': "channelClass_example", // String | Filter by channel class, 'STANDARD' or 'SINGLE_PIPELINE' 
  'codec': "codec_example", // String | Filter by codec, 'AVC', 'HEVC', 'MPEG2', 'AUDIO', or 'LINK'
  'maxResults': 56, // Number | 
  'maximumBitrate': "maximumBitrate_example", // String | Filter by bitrate, 'MAX_10_MBPS', 'MAX_20_MBPS', or 'MAX_50_MBPS' 
  'maximumFramerate': "maximumFramerate_example", // String | Filter by framerate, 'MAX_30_FPS' or 'MAX_60_FPS'
  'nextToken': "nextToken_example", // String | 
  'resolution': "resolution_example", // String | Filter by resolution, 'SD', 'HD', 'FHD', or 'UHD'
  'resourceType': "resourceType_example", // String | Filter by resource type, 'INPUT', 'OUTPUT', 'MULTIPLEX', or 'CHANNEL'
  'specialFeature': "specialFeature_example", // String | Filter by special feature, 'ADVANCED_AUDIO' or 'AUDIO_NORMALIZATION' 
  'videoQuality': "videoQuality_example", // String | Filter by video quality, 'STANDARD', 'ENHANCED', or 'PREMIUM' 
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listReservations(opts, (error, data, response) => {
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
 **channelClass** | **String**| Filter by channel class, &#39;STANDARD&#39; or &#39;SINGLE_PIPELINE&#39;  | [optional] 
 **codec** | **String**| Filter by codec, &#39;AVC&#39;, &#39;HEVC&#39;, &#39;MPEG2&#39;, &#39;AUDIO&#39;, or &#39;LINK&#39; | [optional] 
 **maxResults** | **Number**|  | [optional] 
 **maximumBitrate** | **String**| Filter by bitrate, &#39;MAX_10_MBPS&#39;, &#39;MAX_20_MBPS&#39;, or &#39;MAX_50_MBPS&#39;  | [optional] 
 **maximumFramerate** | **String**| Filter by framerate, &#39;MAX_30_FPS&#39; or &#39;MAX_60_FPS&#39; | [optional] 
 **nextToken** | **String**|  | [optional] 
 **resolution** | **String**| Filter by resolution, &#39;SD&#39;, &#39;HD&#39;, &#39;FHD&#39;, or &#39;UHD&#39; | [optional] 
 **resourceType** | **String**| Filter by resource type, &#39;INPUT&#39;, &#39;OUTPUT&#39;, &#39;MULTIPLEX&#39;, or &#39;CHANNEL&#39; | [optional] 
 **specialFeature** | **String**| Filter by special feature, &#39;ADVANCED_AUDIO&#39; or &#39;AUDIO_NORMALIZATION&#39;  | [optional] 
 **videoQuality** | **String**| Filter by video quality, &#39;STANDARD&#39;, &#39;ENHANCED&#39;, or &#39;PREMIUM&#39;  | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListReservationsResponse**](ListReservationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Produces list of tags that have been created for a resource

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let resourceArn = "resourceArn_example"; // String | 
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
 **resourceArn** | **String**|  | 
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


## purchaseOffering

> PurchaseOfferingResponse purchaseOffering(offeringId, purchaseOfferingRequest, opts)



Purchase an offering and create a reservation.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let offeringId = "offeringId_example"; // String | Offering to purchase, e.g. '87654321'
let purchaseOfferingRequest = new AwsElementalMediaLive.PurchaseOfferingRequest(); // PurchaseOfferingRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.purchaseOffering(offeringId, purchaseOfferingRequest, opts, (error, data, response) => {
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
 **offeringId** | **String**| Offering to purchase, e.g. &#39;87654321&#39; | 
 **purchaseOfferingRequest** | [**PurchaseOfferingRequest**](PurchaseOfferingRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PurchaseOfferingResponse**](PurchaseOfferingResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## rebootInputDevice

> Object rebootInputDevice(inputDeviceId, rebootInputDeviceRequest, opts)



Send a reboot command to the specified input device. The device will begin rebooting within a few seconds of sending the command. When the reboot is complete, the device’s connection status will change to connected.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of the input device to reboot. For example, hd-123456789abcdef.
let rebootInputDeviceRequest = new AwsElementalMediaLive.RebootInputDeviceRequest(); // RebootInputDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rebootInputDevice(inputDeviceId, rebootInputDeviceRequest, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of the input device to reboot. For example, hd-123456789abcdef. | 
 **rebootInputDeviceRequest** | [**RebootInputDeviceRequest**](RebootInputDeviceRequest.md)|  | 
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


## rejectInputDeviceTransfer

> Object rejectInputDeviceTransfer(inputDeviceId, opts)



Reject the transfer of the specified input device to your AWS account.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of the input device to reject. For example, hd-123456789abcdef.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.rejectInputDeviceTransfer(inputDeviceId, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of the input device to reject. For example, hd-123456789abcdef. | 
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


## startChannel

> StartChannelResponse startChannel(channelId, opts)



Starts an existing channel

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | A request to start a channel
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| A request to start a channel | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartChannelResponse**](StartChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## startInputDeviceMaintenanceWindow

> Object startInputDeviceMaintenanceWindow(inputDeviceId, opts)



Start a maintenance window for the specified input device. Starting a maintenance window will give the device up to two hours to install software. If the device was streaming prior to the maintenance, it will resume streaming when the software is fully installed. Devices automatically install updates while they are powered on and their MediaLive channels are stopped. A maintenance window allows you to update a device without having to stop MediaLive channels that use the device. The device must remain powered on and connected to the internet for the duration of the maintenance.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of the input device to start a maintenance window for. For example, hd-123456789abcdef.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startInputDeviceMaintenanceWindow(inputDeviceId, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of the input device to start a maintenance window for. For example, hd-123456789abcdef. | 
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


## startMultiplex

> StartMultiplexResponse startMultiplex(multiplexId, opts)



Start (run) the multiplex. Starting the multiplex does not start the channels. You must explicitly start each channel.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startMultiplex(multiplexId, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartMultiplexResponse**](StartMultiplexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopChannel

> StopChannelResponse stopChannel(channelId, opts)



Stops a running channel

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | A request to stop a running channel
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopChannel(channelId, opts, (error, data, response) => {
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
 **channelId** | **String**| A request to stop a running channel | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopChannelResponse**](StopChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stopMultiplex

> StopMultiplexResponse stopMultiplex(multiplexId, opts)



Stops a running multiplex. If the multiplex isn&#39;t running, this action has no effect.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopMultiplex(multiplexId, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StopMultiplexResponse**](StopMultiplexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## transferInputDevice

> Object transferInputDevice(inputDeviceId, transferInputDeviceRequest, opts)



Start an input device transfer to another AWS account. After you make the request, the other account must accept or reject the transfer.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of this input device. For example, hd-123456789abcdef.
let transferInputDeviceRequest = new AwsElementalMediaLive.TransferInputDeviceRequest(); // TransferInputDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.transferInputDevice(inputDeviceId, transferInputDeviceRequest, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of this input device. For example, hd-123456789abcdef. | 
 **transferInputDeviceRequest** | [**TransferInputDeviceRequest**](TransferInputDeviceRequest.md)|  | 
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


## updateAccountConfiguration

> UpdateAccountConfigurationResponse updateAccountConfiguration(updateAccountConfigurationRequest, opts)



Update account configuration

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let updateAccountConfigurationRequest = new AwsElementalMediaLive.UpdateAccountConfigurationRequest(); // UpdateAccountConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAccountConfiguration(updateAccountConfigurationRequest, opts, (error, data, response) => {
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
 **updateAccountConfigurationRequest** | [**UpdateAccountConfigurationRequest**](UpdateAccountConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAccountConfigurationResponse**](UpdateAccountConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannel

> UpdateChannelResponse updateChannel(channelId, updateChannelRequest, opts)



Updates a channel.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | channel ID
let updateChannelRequest = new AwsElementalMediaLive.UpdateChannelRequest(); // UpdateChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannel(channelId, updateChannelRequest, opts, (error, data, response) => {
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
 **channelId** | **String**| channel ID | 
 **updateChannelRequest** | [**UpdateChannelRequest**](UpdateChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelResponse**](UpdateChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateChannelClass

> UpdateChannelClassResponse updateChannelClass(channelId, updateChannelClassRequest, opts)



Changes the class of the channel.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let channelId = "channelId_example"; // String | Channel Id of the channel whose class should be updated.
let updateChannelClassRequest = new AwsElementalMediaLive.UpdateChannelClassRequest(); // UpdateChannelClassRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateChannelClass(channelId, updateChannelClassRequest, opts, (error, data, response) => {
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
 **channelId** | **String**| Channel Id of the channel whose class should be updated. | 
 **updateChannelClassRequest** | [**UpdateChannelClassRequest**](UpdateChannelClassRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateChannelClassResponse**](UpdateChannelClassResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInput

> UpdateInputResponse updateInput(inputId, updateInputRequest, opts)



Updates an input.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputId = "inputId_example"; // String | Unique ID of the input.
let updateInputRequest = new AwsElementalMediaLive.UpdateInputRequest(); // UpdateInputRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateInput(inputId, updateInputRequest, opts, (error, data, response) => {
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
 **inputId** | **String**| Unique ID of the input. | 
 **updateInputRequest** | [**UpdateInputRequest**](UpdateInputRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateInputResponse**](UpdateInputResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInputDevice

> UpdateInputDeviceResponse updateInputDevice(inputDeviceId, updateInputDeviceRequest, opts)



Updates the parameters for the input device.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputDeviceId = "inputDeviceId_example"; // String | The unique ID of the input device. For example, hd-123456789abcdef.
let updateInputDeviceRequest = new AwsElementalMediaLive.UpdateInputDeviceRequest(); // UpdateInputDeviceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateInputDevice(inputDeviceId, updateInputDeviceRequest, opts, (error, data, response) => {
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
 **inputDeviceId** | **String**| The unique ID of the input device. For example, hd-123456789abcdef. | 
 **updateInputDeviceRequest** | [**UpdateInputDeviceRequest**](UpdateInputDeviceRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateInputDeviceResponse**](UpdateInputDeviceResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInputSecurityGroup

> UpdateInputSecurityGroupResponse updateInputSecurityGroup(inputSecurityGroupId, createInputSecurityGroupRequest, opts)



Update an Input Security Group&#39;s Whilelists.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let inputSecurityGroupId = "inputSecurityGroupId_example"; // String | The id of the Input Security Group to update.
let createInputSecurityGroupRequest = new AwsElementalMediaLive.CreateInputSecurityGroupRequest(); // CreateInputSecurityGroupRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateInputSecurityGroup(inputSecurityGroupId, createInputSecurityGroupRequest, opts, (error, data, response) => {
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
 **inputSecurityGroupId** | **String**| The id of the Input Security Group to update. | 
 **createInputSecurityGroupRequest** | [**CreateInputSecurityGroupRequest**](CreateInputSecurityGroupRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateInputSecurityGroupResponse**](UpdateInputSecurityGroupResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMultiplex

> UpdateMultiplexResponse updateMultiplex(multiplexId, updateMultiplexRequest, opts)



Updates a multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | ID of the multiplex to update.
let updateMultiplexRequest = new AwsElementalMediaLive.UpdateMultiplexRequest(); // UpdateMultiplexRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMultiplex(multiplexId, updateMultiplexRequest, opts, (error, data, response) => {
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
 **multiplexId** | **String**| ID of the multiplex to update. | 
 **updateMultiplexRequest** | [**UpdateMultiplexRequest**](UpdateMultiplexRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMultiplexResponse**](UpdateMultiplexResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateMultiplexProgram

> UpdateMultiplexProgramResponse updateMultiplexProgram(multiplexId, programName, updateMultiplexProgramRequest, opts)



Update a program in a multiplex.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let multiplexId = "multiplexId_example"; // String | The ID of the multiplex of the program to update.
let programName = "programName_example"; // String | The name of the program to update.
let updateMultiplexProgramRequest = new AwsElementalMediaLive.UpdateMultiplexProgramRequest(); // UpdateMultiplexProgramRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateMultiplexProgram(multiplexId, programName, updateMultiplexProgramRequest, opts, (error, data, response) => {
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
 **multiplexId** | **String**| The ID of the multiplex of the program to update. | 
 **programName** | **String**| The name of the program to update. | 
 **updateMultiplexProgramRequest** | [**UpdateMultiplexProgramRequest**](UpdateMultiplexProgramRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateMultiplexProgramResponse**](UpdateMultiplexProgramResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateReservation

> UpdateReservationResponse updateReservation(reservationId, updateReservationRequest, opts)



Update reservation.

### Example

```javascript
import AwsElementalMediaLive from 'aws_elemental_media_live';
let defaultClient = AwsElementalMediaLive.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsElementalMediaLive.DefaultApi();
let reservationId = "reservationId_example"; // String | Unique reservation ID, e.g. '1234567'
let updateReservationRequest = new AwsElementalMediaLive.UpdateReservationRequest(); // UpdateReservationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateReservation(reservationId, updateReservationRequest, opts, (error, data, response) => {
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
 **reservationId** | **String**| Unique reservation ID, e.g. &#39;1234567&#39; | 
 **updateReservationRequest** | [**UpdateReservationRequest**](UpdateReservationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateReservationResponse**](UpdateReservationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

