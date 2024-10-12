# AmazonPinpointSmsAndVoiceService.DefaultApi

All URIs are relative to *http://sms-voice.pinpoint.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConfigurationSet**](DefaultApi.md#createConfigurationSet) | **POST** /v1/sms-voice/configuration-sets | 
[**createConfigurationSetEventDestination**](DefaultApi.md#createConfigurationSetEventDestination) | **POST** /v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations | 
[**deleteConfigurationSet**](DefaultApi.md#deleteConfigurationSet) | **DELETE** /v1/sms-voice/configuration-sets/{ConfigurationSetName} | 
[**deleteConfigurationSetEventDestination**](DefaultApi.md#deleteConfigurationSetEventDestination) | **DELETE** /v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName} | 
[**getConfigurationSetEventDestinations**](DefaultApi.md#getConfigurationSetEventDestinations) | **GET** /v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations | 
[**listConfigurationSets**](DefaultApi.md#listConfigurationSets) | **GET** /v1/sms-voice/configuration-sets | 
[**sendVoiceMessage**](DefaultApi.md#sendVoiceMessage) | **POST** /v1/sms-voice/voice/message | 
[**updateConfigurationSetEventDestination**](DefaultApi.md#updateConfigurationSetEventDestination) | **PUT** /v1/sms-voice/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName} | 



## createConfigurationSet

> Object createConfigurationSet(createConfigurationSetRequest, opts)



Create a new configuration set. After you create the configuration set, you can add one or more event destinations to it.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let createConfigurationSetRequest = new AmazonPinpointSmsAndVoiceService.CreateConfigurationSetRequest(); // CreateConfigurationSetRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfigurationSet(createConfigurationSetRequest, opts, (error, data, response) => {
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
 **createConfigurationSetRequest** | [**CreateConfigurationSetRequest**](CreateConfigurationSetRequest.md)|  | 
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


## createConfigurationSetEventDestination

> Object createConfigurationSetEventDestination(configurationSetName, createConfigurationSetEventDestinationRequest, opts)



Create a new event destination in a configuration set.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | ConfigurationSetName
let createConfigurationSetEventDestinationRequest = new AmazonPinpointSmsAndVoiceService.CreateConfigurationSetEventDestinationRequest(); // CreateConfigurationSetEventDestinationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createConfigurationSetEventDestination(configurationSetName, createConfigurationSetEventDestinationRequest, opts, (error, data, response) => {
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
 **configurationSetName** | **String**| ConfigurationSetName | 
 **createConfigurationSetEventDestinationRequest** | [**CreateConfigurationSetEventDestinationRequest**](CreateConfigurationSetEventDestinationRequest.md)|  | 
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


## deleteConfigurationSet

> Object deleteConfigurationSet(configurationSetName, opts)



Deletes an existing configuration set.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | ConfigurationSetName
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfigurationSet(configurationSetName, opts, (error, data, response) => {
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
 **configurationSetName** | **String**| ConfigurationSetName | 
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


## deleteConfigurationSetEventDestination

> Object deleteConfigurationSetEventDestination(configurationSetName, eventDestinationName, opts)



Deletes an event destination in a configuration set.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | ConfigurationSetName
let eventDestinationName = "eventDestinationName_example"; // String | EventDestinationName
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteConfigurationSetEventDestination(configurationSetName, eventDestinationName, opts, (error, data, response) => {
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
 **configurationSetName** | **String**| ConfigurationSetName | 
 **eventDestinationName** | **String**| EventDestinationName | 
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


## getConfigurationSetEventDestinations

> GetConfigurationSetEventDestinationsResponse getConfigurationSetEventDestinations(configurationSetName, opts)



Obtain information about an event destination, including the types of events it reports, the Amazon Resource Name (ARN) of the destination, and the name of the event destination.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | ConfigurationSetName
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfigurationSetEventDestinations(configurationSetName, opts, (error, data, response) => {
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
 **configurationSetName** | **String**| ConfigurationSetName | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConfigurationSetEventDestinationsResponse**](GetConfigurationSetEventDestinationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationSets

> ListConfigurationSetsResponse listConfigurationSets(opts)



List all of the configuration sets associated with your Amazon Pinpoint account in the current region.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to the API that indicates the position in the list of results.
  'pageSize': "pageSize_example" // String | Used to specify the number of items that should be returned in the response.
};
apiInstance.listConfigurationSets(opts, (error, data, response) => {
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
 **nextToken** | **String**| A token returned from a previous call to the API that indicates the position in the list of results. | [optional] 
 **pageSize** | **String**| Used to specify the number of items that should be returned in the response. | [optional] 

### Return type

[**ListConfigurationSetsResponse**](ListConfigurationSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## sendVoiceMessage

> SendVoiceMessageResponse sendVoiceMessage(sendVoiceMessageRequest, opts)



Create a new voice message and send it to a recipient&#39;s phone number.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let sendVoiceMessageRequest = new AmazonPinpointSmsAndVoiceService.SendVoiceMessageRequest(); // SendVoiceMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendVoiceMessage(sendVoiceMessageRequest, opts, (error, data, response) => {
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
 **sendVoiceMessageRequest** | [**SendVoiceMessageRequest**](SendVoiceMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendVoiceMessageResponse**](SendVoiceMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateConfigurationSetEventDestination

> Object updateConfigurationSetEventDestination(configurationSetName, eventDestinationName, updateConfigurationSetEventDestinationRequest, opts)



Update an event destination in a configuration set. An event destination is a location that you publish information about your voice calls to. For example, you can log an event to an Amazon CloudWatch destination when a call fails.

### Example

```javascript
import AmazonPinpointSmsAndVoiceService from 'amazon_pinpoint_sms_and_voice_service';
let defaultClient = AmazonPinpointSmsAndVoiceService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointSmsAndVoiceService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | ConfigurationSetName
let eventDestinationName = "eventDestinationName_example"; // String | EventDestinationName
let updateConfigurationSetEventDestinationRequest = new AmazonPinpointSmsAndVoiceService.UpdateConfigurationSetEventDestinationRequest(); // UpdateConfigurationSetEventDestinationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateConfigurationSetEventDestination(configurationSetName, eventDestinationName, updateConfigurationSetEventDestinationRequest, opts, (error, data, response) => {
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
 **configurationSetName** | **String**| ConfigurationSetName | 
 **eventDestinationName** | **String**| EventDestinationName | 
 **updateConfigurationSetEventDestinationRequest** | [**UpdateConfigurationSetEventDestinationRequest**](UpdateConfigurationSetEventDestinationRequest.md)|  | 
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

