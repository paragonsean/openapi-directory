# AwsSystemsManagerIncidentManagerContacts.DefaultApi

All URIs are relative to *http://ssm-contacts.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**acceptPage**](DefaultApi.md#acceptPage) | **POST** /#X-Amz-Target&#x3D;SSMContacts.AcceptPage | 
[**activateContactChannel**](DefaultApi.md#activateContactChannel) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ActivateContactChannel | 
[**createContact**](DefaultApi.md#createContact) | **POST** /#X-Amz-Target&#x3D;SSMContacts.CreateContact | 
[**createContactChannel**](DefaultApi.md#createContactChannel) | **POST** /#X-Amz-Target&#x3D;SSMContacts.CreateContactChannel | 
[**createRotation**](DefaultApi.md#createRotation) | **POST** /#X-Amz-Target&#x3D;SSMContacts.CreateRotation | 
[**createRotationOverride**](DefaultApi.md#createRotationOverride) | **POST** /#X-Amz-Target&#x3D;SSMContacts.CreateRotationOverride | 
[**deactivateContactChannel**](DefaultApi.md#deactivateContactChannel) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DeactivateContactChannel | 
[**deleteContact**](DefaultApi.md#deleteContact) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DeleteContact | 
[**deleteContactChannel**](DefaultApi.md#deleteContactChannel) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DeleteContactChannel | 
[**deleteRotation**](DefaultApi.md#deleteRotation) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DeleteRotation | 
[**deleteRotationOverride**](DefaultApi.md#deleteRotationOverride) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DeleteRotationOverride | 
[**describeEngagement**](DefaultApi.md#describeEngagement) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DescribeEngagement | 
[**describePage**](DefaultApi.md#describePage) | **POST** /#X-Amz-Target&#x3D;SSMContacts.DescribePage | 
[**getContact**](DefaultApi.md#getContact) | **POST** /#X-Amz-Target&#x3D;SSMContacts.GetContact | 
[**getContactChannel**](DefaultApi.md#getContactChannel) | **POST** /#X-Amz-Target&#x3D;SSMContacts.GetContactChannel | 
[**getContactPolicy**](DefaultApi.md#getContactPolicy) | **POST** /#X-Amz-Target&#x3D;SSMContacts.GetContactPolicy | 
[**getRotation**](DefaultApi.md#getRotation) | **POST** /#X-Amz-Target&#x3D;SSMContacts.GetRotation | 
[**getRotationOverride**](DefaultApi.md#getRotationOverride) | **POST** /#X-Amz-Target&#x3D;SSMContacts.GetRotationOverride | 
[**listContactChannels**](DefaultApi.md#listContactChannels) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListContactChannels | 
[**listContacts**](DefaultApi.md#listContacts) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListContacts | 
[**listEngagements**](DefaultApi.md#listEngagements) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListEngagements | 
[**listPageReceipts**](DefaultApi.md#listPageReceipts) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListPageReceipts | 
[**listPageResolutions**](DefaultApi.md#listPageResolutions) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListPageResolutions | 
[**listPagesByContact**](DefaultApi.md#listPagesByContact) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListPagesByContact | 
[**listPagesByEngagement**](DefaultApi.md#listPagesByEngagement) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListPagesByEngagement | 
[**listPreviewRotationShifts**](DefaultApi.md#listPreviewRotationShifts) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListPreviewRotationShifts | 
[**listRotationOverrides**](DefaultApi.md#listRotationOverrides) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListRotationOverrides | 
[**listRotationShifts**](DefaultApi.md#listRotationShifts) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListRotationShifts | 
[**listRotations**](DefaultApi.md#listRotations) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListRotations | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **POST** /#X-Amz-Target&#x3D;SSMContacts.ListTagsForResource | 
[**putContactPolicy**](DefaultApi.md#putContactPolicy) | **POST** /#X-Amz-Target&#x3D;SSMContacts.PutContactPolicy | 
[**sendActivationCode**](DefaultApi.md#sendActivationCode) | **POST** /#X-Amz-Target&#x3D;SSMContacts.SendActivationCode | 
[**startEngagement**](DefaultApi.md#startEngagement) | **POST** /#X-Amz-Target&#x3D;SSMContacts.StartEngagement | 
[**stopEngagement**](DefaultApi.md#stopEngagement) | **POST** /#X-Amz-Target&#x3D;SSMContacts.StopEngagement | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /#X-Amz-Target&#x3D;SSMContacts.TagResource | 
[**untagResource**](DefaultApi.md#untagResource) | **POST** /#X-Amz-Target&#x3D;SSMContacts.UntagResource | 
[**updateContact**](DefaultApi.md#updateContact) | **POST** /#X-Amz-Target&#x3D;SSMContacts.UpdateContact | 
[**updateContactChannel**](DefaultApi.md#updateContactChannel) | **POST** /#X-Amz-Target&#x3D;SSMContacts.UpdateContactChannel | 
[**updateRotation**](DefaultApi.md#updateRotation) | **POST** /#X-Amz-Target&#x3D;SSMContacts.UpdateRotation | 



## acceptPage

> Object acceptPage(xAmzTarget, acceptPageRequest, opts)



Used to acknowledge an engagement to a contact channel during an incident.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let acceptPageRequest = new AwsSystemsManagerIncidentManagerContacts.AcceptPageRequest(); // AcceptPageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.acceptPage(xAmzTarget, acceptPageRequest, opts, (error, data, response) => {
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
 **acceptPageRequest** | [**AcceptPageRequest**](AcceptPageRequest.md)|  | 
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


## activateContactChannel

> Object activateContactChannel(xAmzTarget, activateContactChannelRequest, opts)



Activates a contact&#39;s contact channel. Incident Manager can&#39;t engage a contact until the contact channel has been activated.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let activateContactChannelRequest = new AwsSystemsManagerIncidentManagerContacts.ActivateContactChannelRequest(); // ActivateContactChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.activateContactChannel(xAmzTarget, activateContactChannelRequest, opts, (error, data, response) => {
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
 **activateContactChannelRequest** | [**ActivateContactChannelRequest**](ActivateContactChannelRequest.md)|  | 
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


## createContact

> CreateContactResult createContact(xAmzTarget, createContactRequest, opts)



Contacts are either the contacts that Incident Manager engages during an incident or the escalation plans that Incident Manager uses to engage contacts in phases during an incident.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createContactRequest = new AwsSystemsManagerIncidentManagerContacts.CreateContactRequest(); // CreateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContact(xAmzTarget, createContactRequest, opts, (error, data, response) => {
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
 **createContactRequest** | [**CreateContactRequest**](CreateContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContactResult**](CreateContactResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createContactChannel

> CreateContactChannelResult createContactChannel(xAmzTarget, createContactChannelRequest, opts)



A contact channel is the method that Incident Manager uses to engage your contact.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createContactChannelRequest = new AwsSystemsManagerIncidentManagerContacts.CreateContactChannelRequest(); // CreateContactChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContactChannel(xAmzTarget, createContactChannelRequest, opts, (error, data, response) => {
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
 **createContactChannelRequest** | [**CreateContactChannelRequest**](CreateContactChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateContactChannelResult**](CreateContactChannelResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRotation

> CreateRotationResult createRotation(xAmzTarget, createRotationRequest, opts)



Creates a rotation in an on-call schedule.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createRotationRequest = new AwsSystemsManagerIncidentManagerContacts.CreateRotationRequest(); // CreateRotationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRotation(xAmzTarget, createRotationRequest, opts, (error, data, response) => {
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
 **createRotationRequest** | [**CreateRotationRequest**](CreateRotationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRotationResult**](CreateRotationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRotationOverride

> CreateRotationOverrideResult createRotationOverride(xAmzTarget, createRotationOverrideRequest, opts)



Creates an override for a rotation in an on-call schedule.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let createRotationOverrideRequest = new AwsSystemsManagerIncidentManagerContacts.CreateRotationOverrideRequest(); // CreateRotationOverrideRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRotationOverride(xAmzTarget, createRotationOverrideRequest, opts, (error, data, response) => {
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
 **createRotationOverrideRequest** | [**CreateRotationOverrideRequest**](CreateRotationOverrideRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRotationOverrideResult**](CreateRotationOverrideResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deactivateContactChannel

> Object deactivateContactChannel(xAmzTarget, deactivateContactChannelRequest, opts)



To no longer receive Incident Manager engagements to a contact channel, you can deactivate the channel.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deactivateContactChannelRequest = new AwsSystemsManagerIncidentManagerContacts.DeactivateContactChannelRequest(); // DeactivateContactChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deactivateContactChannel(xAmzTarget, deactivateContactChannelRequest, opts, (error, data, response) => {
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
 **deactivateContactChannelRequest** | [**DeactivateContactChannelRequest**](DeactivateContactChannelRequest.md)|  | 
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


## deleteContact

> Object deleteContact(xAmzTarget, deleteContactRequest, opts)



To remove a contact from Incident Manager, you can delete the contact. Deleting a contact removes them from all escalation plans and related response plans. Deleting an escalation plan removes it from all related response plans. You will have to recreate the contact and its contact channels before you can use it again.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteContactRequest = new AwsSystemsManagerIncidentManagerContacts.DeleteContactRequest(); // DeleteContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContact(xAmzTarget, deleteContactRequest, opts, (error, data, response) => {
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
 **deleteContactRequest** | [**DeleteContactRequest**](DeleteContactRequest.md)|  | 
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


## deleteContactChannel

> Object deleteContactChannel(xAmzTarget, deleteContactChannelRequest, opts)



To no longer receive engagements on a contact channel, you can delete the channel from a contact. Deleting the contact channel removes it from the contact&#39;s engagement plan. If you delete the only contact channel for a contact, you won&#39;t be able to engage that contact during an incident.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteContactChannelRequest = new AwsSystemsManagerIncidentManagerContacts.DeleteContactChannelRequest(); // DeleteContactChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContactChannel(xAmzTarget, deleteContactChannelRequest, opts, (error, data, response) => {
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
 **deleteContactChannelRequest** | [**DeleteContactChannelRequest**](DeleteContactChannelRequest.md)|  | 
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


## deleteRotation

> Object deleteRotation(xAmzTarget, deleteRotationRequest, opts)



Deletes a rotation from the system. If a rotation belongs to more than one on-call schedule, this operation deletes it from all of them.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteRotationRequest = new AwsSystemsManagerIncidentManagerContacts.DeleteRotationRequest(); // DeleteRotationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRotation(xAmzTarget, deleteRotationRequest, opts, (error, data, response) => {
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
 **deleteRotationRequest** | [**DeleteRotationRequest**](DeleteRotationRequest.md)|  | 
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


## deleteRotationOverride

> Object deleteRotationOverride(xAmzTarget, deleteRotationOverrideRequest, opts)



Deletes an existing override for an on-call rotation.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let deleteRotationOverrideRequest = new AwsSystemsManagerIncidentManagerContacts.DeleteRotationOverrideRequest(); // DeleteRotationOverrideRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRotationOverride(xAmzTarget, deleteRotationOverrideRequest, opts, (error, data, response) => {
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
 **deleteRotationOverrideRequest** | [**DeleteRotationOverrideRequest**](DeleteRotationOverrideRequest.md)|  | 
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


## describeEngagement

> DescribeEngagementResult describeEngagement(xAmzTarget, describeEngagementRequest, opts)



Incident Manager uses engagements to engage contacts and escalation plans during an incident. Use this command to describe the engagement that occurred during an incident.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describeEngagementRequest = new AwsSystemsManagerIncidentManagerContacts.DescribeEngagementRequest(); // DescribeEngagementRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describeEngagement(xAmzTarget, describeEngagementRequest, opts, (error, data, response) => {
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
 **describeEngagementRequest** | [**DescribeEngagementRequest**](DescribeEngagementRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribeEngagementResult**](DescribeEngagementResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## describePage

> DescribePageResult describePage(xAmzTarget, describePageRequest, opts)



Lists details of the engagement to a contact channel.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let describePageRequest = new AwsSystemsManagerIncidentManagerContacts.DescribePageRequest(); // DescribePageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.describePage(xAmzTarget, describePageRequest, opts, (error, data, response) => {
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
 **describePageRequest** | [**DescribePageRequest**](DescribePageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DescribePageResult**](DescribePageResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContact

> GetContactResult getContact(xAmzTarget, getContactRequest, opts)



Retrieves information about the specified contact or escalation plan.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getContactRequest = new AwsSystemsManagerIncidentManagerContacts.GetContactRequest(); // GetContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContact(xAmzTarget, getContactRequest, opts, (error, data, response) => {
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
 **getContactRequest** | [**GetContactRequest**](GetContactRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactResult**](GetContactResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContactChannel

> GetContactChannelResult getContactChannel(xAmzTarget, getContactChannelRequest, opts)



List details about a specific contact channel.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getContactChannelRequest = new AwsSystemsManagerIncidentManagerContacts.GetContactChannelRequest(); // GetContactChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContactChannel(xAmzTarget, getContactChannelRequest, opts, (error, data, response) => {
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
 **getContactChannelRequest** | [**GetContactChannelRequest**](GetContactChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactChannelResult**](GetContactChannelResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getContactPolicy

> GetContactPolicyResult getContactPolicy(xAmzTarget, getContactPolicyRequest, opts)



Retrieves the resource policies attached to the specified contact or escalation plan.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getContactPolicyRequest = new AwsSystemsManagerIncidentManagerContacts.GetContactPolicyRequest(); // GetContactPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContactPolicy(xAmzTarget, getContactPolicyRequest, opts, (error, data, response) => {
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
 **getContactPolicyRequest** | [**GetContactPolicyRequest**](GetContactPolicyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactPolicyResult**](GetContactPolicyResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRotation

> GetRotationResult getRotation(xAmzTarget, getRotationRequest, opts)



Retrieves information about an on-call rotation.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getRotationRequest = new AwsSystemsManagerIncidentManagerContacts.GetRotationRequest(); // GetRotationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRotation(xAmzTarget, getRotationRequest, opts, (error, data, response) => {
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
 **getRotationRequest** | [**GetRotationRequest**](GetRotationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRotationResult**](GetRotationResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getRotationOverride

> GetRotationOverrideResult getRotationOverride(xAmzTarget, getRotationOverrideRequest, opts)



Retrieves information about an override to an on-call rotation.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let getRotationOverrideRequest = new AwsSystemsManagerIncidentManagerContacts.GetRotationOverrideRequest(); // GetRotationOverrideRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRotationOverride(xAmzTarget, getRotationOverrideRequest, opts, (error, data, response) => {
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
 **getRotationOverrideRequest** | [**GetRotationOverrideRequest**](GetRotationOverrideRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRotationOverrideResult**](GetRotationOverrideResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listContactChannels

> ListContactChannelsResult listContactChannels(xAmzTarget, listContactChannelsRequest, opts)



Lists all contact channels for the specified contact.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listContactChannelsRequest = new AwsSystemsManagerIncidentManagerContacts.ListContactChannelsRequest(); // ListContactChannelsRequest | 
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
apiInstance.listContactChannels(xAmzTarget, listContactChannelsRequest, opts, (error, data, response) => {
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
 **listContactChannelsRequest** | [**ListContactChannelsRequest**](ListContactChannelsRequest.md)|  | 
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

[**ListContactChannelsResult**](ListContactChannelsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listContacts

> ListContactsResult listContacts(xAmzTarget, listContactsRequest, opts)



Lists all contacts and escalation plans in Incident Manager.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listContactsRequest = new AwsSystemsManagerIncidentManagerContacts.ListContactsRequest(); // ListContactsRequest | 
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
apiInstance.listContacts(xAmzTarget, listContactsRequest, opts, (error, data, response) => {
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
 **listContactsRequest** | [**ListContactsRequest**](ListContactsRequest.md)|  | 
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

[**ListContactsResult**](ListContactsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listEngagements

> ListEngagementsResult listEngagements(xAmzTarget, listEngagementsRequest, opts)



Lists all engagements that have happened in an incident.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listEngagementsRequest = new AwsSystemsManagerIncidentManagerContacts.ListEngagementsRequest(); // ListEngagementsRequest | 
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
apiInstance.listEngagements(xAmzTarget, listEngagementsRequest, opts, (error, data, response) => {
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
 **listEngagementsRequest** | [**ListEngagementsRequest**](ListEngagementsRequest.md)|  | 
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

[**ListEngagementsResult**](ListEngagementsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPageReceipts

> ListPageReceiptsResult listPageReceipts(xAmzTarget, listPageReceiptsRequest, opts)



Lists all of the engagements to contact channels that have been acknowledged.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPageReceiptsRequest = new AwsSystemsManagerIncidentManagerContacts.ListPageReceiptsRequest(); // ListPageReceiptsRequest | 
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
apiInstance.listPageReceipts(xAmzTarget, listPageReceiptsRequest, opts, (error, data, response) => {
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
 **listPageReceiptsRequest** | [**ListPageReceiptsRequest**](ListPageReceiptsRequest.md)|  | 
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

[**ListPageReceiptsResult**](ListPageReceiptsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPageResolutions

> ListPageResolutionsResult listPageResolutions(xAmzTarget, listPageResolutionsRequest, opts)



Returns the resolution path of an engagement. For example, the escalation plan engaged in an incident might target an on-call schedule that includes several contacts in a rotation, but just one contact on-call when the incident starts. The resolution path indicates the hierarchy of &lt;i&gt;escalation plan &amp;gt; on-call schedule &amp;gt; contact&lt;/i&gt;.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPageResolutionsRequest = new AwsSystemsManagerIncidentManagerContacts.ListPageResolutionsRequest(); // ListPageResolutionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listPageResolutions(xAmzTarget, listPageResolutionsRequest, opts, (error, data, response) => {
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
 **listPageResolutionsRequest** | [**ListPageResolutionsRequest**](ListPageResolutionsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListPageResolutionsResult**](ListPageResolutionsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPagesByContact

> ListPagesByContactResult listPagesByContact(xAmzTarget, listPagesByContactRequest, opts)



Lists the engagements to a contact&#39;s contact channels.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPagesByContactRequest = new AwsSystemsManagerIncidentManagerContacts.ListPagesByContactRequest(); // ListPagesByContactRequest | 
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
apiInstance.listPagesByContact(xAmzTarget, listPagesByContactRequest, opts, (error, data, response) => {
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
 **listPagesByContactRequest** | [**ListPagesByContactRequest**](ListPagesByContactRequest.md)|  | 
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

[**ListPagesByContactResult**](ListPagesByContactResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPagesByEngagement

> ListPagesByEngagementResult listPagesByEngagement(xAmzTarget, listPagesByEngagementRequest, opts)



Lists the engagements to contact channels that occurred by engaging a contact.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPagesByEngagementRequest = new AwsSystemsManagerIncidentManagerContacts.ListPagesByEngagementRequest(); // ListPagesByEngagementRequest | 
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
apiInstance.listPagesByEngagement(xAmzTarget, listPagesByEngagementRequest, opts, (error, data, response) => {
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
 **listPagesByEngagementRequest** | [**ListPagesByEngagementRequest**](ListPagesByEngagementRequest.md)|  | 
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

[**ListPagesByEngagementResult**](ListPagesByEngagementResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listPreviewRotationShifts

> ListPreviewRotationShiftsResult listPreviewRotationShifts(xAmzTarget, listPreviewRotationShiftsRequest, opts)



&lt;p&gt;Returns a list of shifts based on rotation configuration parameters.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The Incident Manager primarily uses this operation to populate the &lt;b&gt;Preview&lt;/b&gt; calendar. It is not typically run by end users.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listPreviewRotationShiftsRequest = new AwsSystemsManagerIncidentManagerContacts.ListPreviewRotationShiftsRequest(); // ListPreviewRotationShiftsRequest | 
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
apiInstance.listPreviewRotationShifts(xAmzTarget, listPreviewRotationShiftsRequest, opts, (error, data, response) => {
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
 **listPreviewRotationShiftsRequest** | [**ListPreviewRotationShiftsRequest**](ListPreviewRotationShiftsRequest.md)|  | 
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

[**ListPreviewRotationShiftsResult**](ListPreviewRotationShiftsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRotationOverrides

> ListRotationOverridesResult listRotationOverrides(xAmzTarget, listRotationOverridesRequest, opts)



Retrieves a list of overrides currently specified for an on-call rotation.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRotationOverridesRequest = new AwsSystemsManagerIncidentManagerContacts.ListRotationOverridesRequest(); // ListRotationOverridesRequest | 
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
apiInstance.listRotationOverrides(xAmzTarget, listRotationOverridesRequest, opts, (error, data, response) => {
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
 **listRotationOverridesRequest** | [**ListRotationOverridesRequest**](ListRotationOverridesRequest.md)|  | 
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

[**ListRotationOverridesResult**](ListRotationOverridesResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRotationShifts

> ListRotationShiftsResult listRotationShifts(xAmzTarget, listRotationShiftsRequest, opts)



Returns a list of shifts generated by an existing rotation in the system.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRotationShiftsRequest = new AwsSystemsManagerIncidentManagerContacts.ListRotationShiftsRequest(); // ListRotationShiftsRequest | 
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
apiInstance.listRotationShifts(xAmzTarget, listRotationShiftsRequest, opts, (error, data, response) => {
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
 **listRotationShiftsRequest** | [**ListRotationShiftsRequest**](ListRotationShiftsRequest.md)|  | 
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

[**ListRotationShiftsResult**](ListRotationShiftsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRotations

> ListRotationsResult listRotations(xAmzTarget, listRotationsRequest, opts)



Retrieves a list of on-call rotations.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listRotationsRequest = new AwsSystemsManagerIncidentManagerContacts.ListRotationsRequest(); // ListRotationsRequest | 
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
apiInstance.listRotations(xAmzTarget, listRotationsRequest, opts, (error, data, response) => {
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
 **listRotationsRequest** | [**ListRotationsRequest**](ListRotationsRequest.md)|  | 
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

[**ListRotationsResult**](ListRotationsResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResult listTagsForResource(xAmzTarget, listTagsForResourceRequest, opts)



Lists the tags of an escalation plan or contact.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let listTagsForResourceRequest = new AwsSystemsManagerIncidentManagerContacts.ListTagsForResourceRequest(); // ListTagsForResourceRequest | 
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

[**ListTagsForResourceResult**](ListTagsForResourceResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putContactPolicy

> Object putContactPolicy(xAmzTarget, putContactPolicyRequest, opts)



Adds a resource policy to the specified contact or escalation plan. The resource policy is used to share the contact or escalation plan using Resource Access Manager (RAM). For more information about cross-account sharing, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/incident-manager/latest/userguide/xa.html\&quot;&gt;Setting up cross-account functionality&lt;/a&gt;.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let putContactPolicyRequest = new AwsSystemsManagerIncidentManagerContacts.PutContactPolicyRequest(); // PutContactPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putContactPolicy(xAmzTarget, putContactPolicyRequest, opts, (error, data, response) => {
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
 **putContactPolicyRequest** | [**PutContactPolicyRequest**](PutContactPolicyRequest.md)|  | 
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


## sendActivationCode

> Object sendActivationCode(xAmzTarget, sendActivationCodeRequest, opts)



Sends an activation code to a contact channel. The contact can use this code to activate the contact channel in the console or with the &lt;code&gt;ActivateChannel&lt;/code&gt; operation. Incident Manager can&#39;t engage a contact channel until it has been activated.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let sendActivationCodeRequest = new AwsSystemsManagerIncidentManagerContacts.SendActivationCodeRequest(); // SendActivationCodeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendActivationCode(xAmzTarget, sendActivationCodeRequest, opts, (error, data, response) => {
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
 **sendActivationCodeRequest** | [**SendActivationCodeRequest**](SendActivationCodeRequest.md)|  | 
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


## startEngagement

> StartEngagementResult startEngagement(xAmzTarget, startEngagementRequest, opts)



Starts an engagement to a contact or escalation plan. The engagement engages each contact specified in the incident.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let startEngagementRequest = new AwsSystemsManagerIncidentManagerContacts.StartEngagementRequest(); // StartEngagementRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.startEngagement(xAmzTarget, startEngagementRequest, opts, (error, data, response) => {
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
 **startEngagementRequest** | [**StartEngagementRequest**](StartEngagementRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**StartEngagementResult**](StartEngagementResult.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## stopEngagement

> Object stopEngagement(xAmzTarget, stopEngagementRequest, opts)



Stops an engagement before it finishes the final stage of the escalation plan or engagement plan. Further contacts aren&#39;t engaged.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let stopEngagementRequest = new AwsSystemsManagerIncidentManagerContacts.StopEngagementRequest(); // StopEngagementRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.stopEngagement(xAmzTarget, stopEngagementRequest, opts, (error, data, response) => {
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
 **stopEngagementRequest** | [**StopEngagementRequest**](StopEngagementRequest.md)|  | 
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


## tagResource

> Object tagResource(xAmzTarget, tagResourceRequest, opts)



Tags a contact or escalation plan. You can tag only contacts and escalation plans in the first region of your replication set.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let tagResourceRequest = new AwsSystemsManagerIncidentManagerContacts.TagResourceRequest(); // TagResourceRequest | 
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



Removes tags from the specified resource.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let untagResourceRequest = new AwsSystemsManagerIncidentManagerContacts.UntagResourceRequest(); // UntagResourceRequest | 
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


## updateContact

> Object updateContact(xAmzTarget, updateContactRequest, opts)



Updates the contact or escalation plan specified.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateContactRequest = new AwsSystemsManagerIncidentManagerContacts.UpdateContactRequest(); // UpdateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContact(xAmzTarget, updateContactRequest, opts, (error, data, response) => {
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
 **updateContactRequest** | [**UpdateContactRequest**](UpdateContactRequest.md)|  | 
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


## updateContactChannel

> Object updateContactChannel(xAmzTarget, updateContactChannelRequest, opts)



Updates a contact&#39;s contact channel.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateContactChannelRequest = new AwsSystemsManagerIncidentManagerContacts.UpdateContactChannelRequest(); // UpdateContactChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactChannel(xAmzTarget, updateContactChannelRequest, opts, (error, data, response) => {
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
 **updateContactChannelRequest** | [**UpdateContactChannelRequest**](UpdateContactChannelRequest.md)|  | 
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


## updateRotation

> Object updateRotation(xAmzTarget, updateRotationRequest, opts)



Updates the information specified for an on-call rotation.

### Example

```javascript
import AwsSystemsManagerIncidentManagerContacts from 'aws_systems_manager_incident_manager_contacts';
let defaultClient = AwsSystemsManagerIncidentManagerContacts.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AwsSystemsManagerIncidentManagerContacts.DefaultApi();
let xAmzTarget = "xAmzTarget_example"; // String | 
let updateRotationRequest = new AwsSystemsManagerIncidentManagerContacts.UpdateRotationRequest(); // UpdateRotationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRotation(xAmzTarget, updateRotationRequest, opts, (error, data, response) => {
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
 **updateRotationRequest** | [**UpdateRotationRequest**](UpdateRotationRequest.md)|  | 
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

