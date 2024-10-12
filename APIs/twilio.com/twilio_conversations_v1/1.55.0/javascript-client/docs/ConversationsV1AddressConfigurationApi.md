# TwilioConversations.ConversationsV1AddressConfigurationApi

All URIs are relative to *https://conversations.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#createConfigurationAddress) | **POST** /v1/Configuration/Addresses | 
[**deleteConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#deleteConfigurationAddress) | **DELETE** /v1/Configuration/Addresses/{Sid} | 
[**fetchConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#fetchConfigurationAddress) | **GET** /v1/Configuration/Addresses/{Sid} | 
[**listConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#listConfigurationAddress) | **GET** /v1/Configuration/Addresses | 
[**updateConfigurationAddress**](ConversationsV1AddressConfigurationApi.md#updateConfigurationAddress) | **POST** /v1/Configuration/Addresses/{Sid} | 



## createConfigurationAddress

> ConversationsV1ConfigurationAddress createConfigurationAddress(address, type, opts)



Create a new address configuration

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1AddressConfigurationApi();
let address = "address_example"; // String | The unique address to be configured. The address can be a whatsapp address or phone number
let type = "type_example"; // ConfigurationAddressEnumType | 
let opts = {
  'addressCountry': "addressCountry_example", // String | An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses.
  'autoCreationConversationServiceSid': "autoCreationConversationServiceSid_example", // String | Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
  'autoCreationEnabled': true, // Boolean | Enable/Disable auto-creating conversations for messages to this address
  'autoCreationStudioFlowSid': "autoCreationStudioFlowSid_example", // String | For type `studio`, the studio flow SID where the webhook should be sent to.
  'autoCreationStudioRetryCount': 56, // Number | For type `studio`, number of times to retry the webhook request
  'autoCreationType': "autoCreationType_example", // ConfigurationAddressEnumAutoCreationType | 
  'autoCreationWebhookFilters': ["null"], // [String] | The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
  'autoCreationWebhookMethod': "autoCreationWebhookMethod_example", // ConfigurationAddressEnumMethod | 
  'autoCreationWebhookUrl': "autoCreationWebhookUrl_example", // String | For type `webhook`, the url for the webhook request.
  'friendlyName': "friendlyName_example" // String | The human-readable name of this configuration, limited to 256 characters. Optional.
};
apiInstance.createConfigurationAddress(address, type, opts, (error, data, response) => {
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
 **address** | **String**| The unique address to be configured. The address can be a whatsapp address or phone number | 
 **type** | **ConfigurationAddressEnumType**|  | 
 **addressCountry** | **String**| An ISO 3166-1 alpha-2n country code which the address belongs to. This is currently only applicable to short code addresses. | [optional] 
 **autoCreationConversationServiceSid** | **String**| Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service. | [optional] 
 **autoCreationEnabled** | **Boolean**| Enable/Disable auto-creating conversations for messages to this address | [optional] 
 **autoCreationStudioFlowSid** | **String**| For type &#x60;studio&#x60;, the studio flow SID where the webhook should be sent to. | [optional] 
 **autoCreationStudioRetryCount** | **Number**| For type &#x60;studio&#x60;, number of times to retry the webhook request | [optional] 
 **autoCreationType** | **ConfigurationAddressEnumAutoCreationType**|  | [optional] 
 **autoCreationWebhookFilters** | [**[String]**](String.md)| The list of events, firing webhook event for this Conversation. Values can be any of the following: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationStateUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onDeliveryUpdated&#x60; | [optional] 
 **autoCreationWebhookMethod** | **ConfigurationAddressEnumMethod**|  | [optional] 
 **autoCreationWebhookUrl** | **String**| For type &#x60;webhook&#x60;, the url for the webhook request. | [optional] 
 **friendlyName** | **String**| The human-readable name of this configuration, limited to 256 characters. Optional. | [optional] 

### Return type

[**ConversationsV1ConfigurationAddress**](ConversationsV1ConfigurationAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteConfigurationAddress

> deleteConfigurationAddress(sid)



Remove an existing address configuration

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1AddressConfigurationApi();
let sid = "sid_example"; // String | The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
apiInstance.deleteConfigurationAddress(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration | 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchConfigurationAddress

> ConversationsV1ConfigurationAddress fetchConfigurationAddress(sid)



Fetch an address configuration 

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1AddressConfigurationApi();
let sid = "sid_example"; // String | The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
apiInstance.fetchConfigurationAddress(sid, (error, data, response) => {
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
 **sid** | **String**| The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration | 

### Return type

[**ConversationsV1ConfigurationAddress**](ConversationsV1ConfigurationAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationAddress

> ListConfigurationAddressResponse listConfigurationAddress(opts)



Retrieve a list of address configurations for an account

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1AddressConfigurationApi();
let opts = {
  'type': "type_example", // String | Filter the address configurations by its type. This value can be one of: `whatsapp`, `sms`.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConfigurationAddress(opts, (error, data, response) => {
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
 **type** | **String**| Filter the address configurations by its type. This value can be one of: &#x60;whatsapp&#x60;, &#x60;sms&#x60;. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConfigurationAddressResponse**](ListConfigurationAddressResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateConfigurationAddress

> ConversationsV1ConfigurationAddress updateConfigurationAddress(sid, opts)



Update an existing address configuration

### Example

```javascript
import TwilioConversations from 'twilio_conversations';
let defaultClient = TwilioConversations.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioConversations.ConversationsV1AddressConfigurationApi();
let sid = "sid_example"; // String | The SID of the Address Configuration resource. This value can be either the `sid` or the `address` of the configuration
let opts = {
  'autoCreationConversationServiceSid': "autoCreationConversationServiceSid_example", // String | Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service.
  'autoCreationEnabled': true, // Boolean | Enable/Disable auto-creating conversations for messages to this address
  'autoCreationStudioFlowSid': "autoCreationStudioFlowSid_example", // String | For type `studio`, the studio flow SID where the webhook should be sent to.
  'autoCreationStudioRetryCount': 56, // Number | For type `studio`, number of times to retry the webhook request
  'autoCreationType': "autoCreationType_example", // ConfigurationAddressEnumAutoCreationType | 
  'autoCreationWebhookFilters': ["null"], // [String] | The list of events, firing webhook event for this Conversation. Values can be any of the following: `onMessageAdded`, `onMessageUpdated`, `onMessageRemoved`, `onConversationUpdated`, `onConversationStateUpdated`, `onConversationRemoved`, `onParticipantAdded`, `onParticipantUpdated`, `onParticipantRemoved`, `onDeliveryUpdated`
  'autoCreationWebhookMethod': "autoCreationWebhookMethod_example", // ConfigurationAddressEnumMethod | 
  'autoCreationWebhookUrl': "autoCreationWebhookUrl_example", // String | For type `webhook`, the url for the webhook request.
  'friendlyName': "friendlyName_example" // String | The human-readable name of this configuration, limited to 256 characters. Optional.
};
apiInstance.updateConfigurationAddress(sid, opts, (error, data, response) => {
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
 **sid** | **String**| The SID of the Address Configuration resource. This value can be either the &#x60;sid&#x60; or the &#x60;address&#x60; of the configuration | 
 **autoCreationConversationServiceSid** | **String**| Conversation Service for the auto-created conversation. If not set, the conversation is created in the default service. | [optional] 
 **autoCreationEnabled** | **Boolean**| Enable/Disable auto-creating conversations for messages to this address | [optional] 
 **autoCreationStudioFlowSid** | **String**| For type &#x60;studio&#x60;, the studio flow SID where the webhook should be sent to. | [optional] 
 **autoCreationStudioRetryCount** | **Number**| For type &#x60;studio&#x60;, number of times to retry the webhook request | [optional] 
 **autoCreationType** | **ConfigurationAddressEnumAutoCreationType**|  | [optional] 
 **autoCreationWebhookFilters** | [**[String]**](String.md)| The list of events, firing webhook event for this Conversation. Values can be any of the following: &#x60;onMessageAdded&#x60;, &#x60;onMessageUpdated&#x60;, &#x60;onMessageRemoved&#x60;, &#x60;onConversationUpdated&#x60;, &#x60;onConversationStateUpdated&#x60;, &#x60;onConversationRemoved&#x60;, &#x60;onParticipantAdded&#x60;, &#x60;onParticipantUpdated&#x60;, &#x60;onParticipantRemoved&#x60;, &#x60;onDeliveryUpdated&#x60; | [optional] 
 **autoCreationWebhookMethod** | **ConfigurationAddressEnumMethod**|  | [optional] 
 **autoCreationWebhookUrl** | **String**| For type &#x60;webhook&#x60;, the url for the webhook request. | [optional] 
 **friendlyName** | **String**| The human-readable name of this configuration, limited to 256 characters. Optional. | [optional] 

### Return type

[**ConversationsV1ConfigurationAddress**](ConversationsV1ConfigurationAddress.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

