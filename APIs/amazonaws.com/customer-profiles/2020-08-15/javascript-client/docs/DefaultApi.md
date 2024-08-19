# AmazonConnectCustomerProfiles.DefaultApi

All URIs are relative to *http://profile.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addProfileKey**](DefaultApi.md#addProfileKey) | **POST** /domains/{DomainName}/profiles/keys | 
[**createCalculatedAttributeDefinition**](DefaultApi.md#createCalculatedAttributeDefinition) | **POST** /domains/{DomainName}/calculated-attributes/{CalculatedAttributeName} | 
[**createDomain**](DefaultApi.md#createDomain) | **POST** /domains/{DomainName} | 
[**createEventStream**](DefaultApi.md#createEventStream) | **POST** /domains/{DomainName}/event-streams/{EventStreamName} | 
[**createIntegrationWorkflow**](DefaultApi.md#createIntegrationWorkflow) | **POST** /domains/{DomainName}/workflows/integrations | 
[**createProfile**](DefaultApi.md#createProfile) | **POST** /domains/{DomainName}/profiles | 
[**deleteCalculatedAttributeDefinition**](DefaultApi.md#deleteCalculatedAttributeDefinition) | **DELETE** /domains/{DomainName}/calculated-attributes/{CalculatedAttributeName} | 
[**deleteDomain**](DefaultApi.md#deleteDomain) | **DELETE** /domains/{DomainName} | 
[**deleteEventStream**](DefaultApi.md#deleteEventStream) | **DELETE** /domains/{DomainName}/event-streams/{EventStreamName} | 
[**deleteIntegration**](DefaultApi.md#deleteIntegration) | **POST** /domains/{DomainName}/integrations/delete | 
[**deleteProfile**](DefaultApi.md#deleteProfile) | **POST** /domains/{DomainName}/profiles/delete | 
[**deleteProfileKey**](DefaultApi.md#deleteProfileKey) | **POST** /domains/{DomainName}/profiles/keys/delete | 
[**deleteProfileObject**](DefaultApi.md#deleteProfileObject) | **POST** /domains/{DomainName}/profiles/objects/delete | 
[**deleteProfileObjectType**](DefaultApi.md#deleteProfileObjectType) | **DELETE** /domains/{DomainName}/object-types/{ObjectTypeName} | 
[**deleteWorkflow**](DefaultApi.md#deleteWorkflow) | **DELETE** /domains/{DomainName}/workflows/{WorkflowId} | 
[**getAutoMergingPreview**](DefaultApi.md#getAutoMergingPreview) | **POST** /domains/{DomainName}/identity-resolution-jobs/auto-merging-preview | 
[**getCalculatedAttributeDefinition**](DefaultApi.md#getCalculatedAttributeDefinition) | **GET** /domains/{DomainName}/calculated-attributes/{CalculatedAttributeName} | 
[**getCalculatedAttributeForProfile**](DefaultApi.md#getCalculatedAttributeForProfile) | **GET** /domains/{DomainName}/profile/{ProfileId}/calculated-attributes/{CalculatedAttributeName} | 
[**getDomain**](DefaultApi.md#getDomain) | **GET** /domains/{DomainName} | 
[**getEventStream**](DefaultApi.md#getEventStream) | **GET** /domains/{DomainName}/event-streams/{EventStreamName} | 
[**getIdentityResolutionJob**](DefaultApi.md#getIdentityResolutionJob) | **GET** /domains/{DomainName}/identity-resolution-jobs/{JobId} | 
[**getIntegration**](DefaultApi.md#getIntegration) | **POST** /domains/{DomainName}/integrations | 
[**getMatches**](DefaultApi.md#getMatches) | **GET** /domains/{DomainName}/matches | 
[**getProfileObjectType**](DefaultApi.md#getProfileObjectType) | **GET** /domains/{DomainName}/object-types/{ObjectTypeName} | 
[**getProfileObjectTypeTemplate**](DefaultApi.md#getProfileObjectTypeTemplate) | **GET** /templates/{TemplateId} | 
[**getSimilarProfiles**](DefaultApi.md#getSimilarProfiles) | **POST** /domains/{DomainName}/matches | 
[**getWorkflow**](DefaultApi.md#getWorkflow) | **GET** /domains/{DomainName}/workflows/{WorkflowId} | 
[**getWorkflowSteps**](DefaultApi.md#getWorkflowSteps) | **GET** /domains/{DomainName}/workflows/{WorkflowId}/steps | 
[**listAccountIntegrations**](DefaultApi.md#listAccountIntegrations) | **POST** /integrations | 
[**listCalculatedAttributeDefinitions**](DefaultApi.md#listCalculatedAttributeDefinitions) | **GET** /domains/{DomainName}/calculated-attributes | 
[**listCalculatedAttributesForProfile**](DefaultApi.md#listCalculatedAttributesForProfile) | **GET** /domains/{DomainName}/profile/{ProfileId}/calculated-attributes | 
[**listDomains**](DefaultApi.md#listDomains) | **GET** /domains | 
[**listEventStreams**](DefaultApi.md#listEventStreams) | **GET** /domains/{DomainName}/event-streams | 
[**listIdentityResolutionJobs**](DefaultApi.md#listIdentityResolutionJobs) | **GET** /domains/{DomainName}/identity-resolution-jobs | 
[**listIntegrations**](DefaultApi.md#listIntegrations) | **GET** /domains/{DomainName}/integrations | 
[**listProfileObjectTypeTemplates**](DefaultApi.md#listProfileObjectTypeTemplates) | **GET** /templates | 
[**listProfileObjectTypes**](DefaultApi.md#listProfileObjectTypes) | **GET** /domains/{DomainName}/object-types | 
[**listProfileObjects**](DefaultApi.md#listProfileObjects) | **POST** /domains/{DomainName}/profiles/objects | 
[**listRuleBasedMatches**](DefaultApi.md#listRuleBasedMatches) | **GET** /domains/{DomainName}/profiles/ruleBasedMatches | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /tags/{resourceArn} | 
[**listWorkflows**](DefaultApi.md#listWorkflows) | **POST** /domains/{DomainName}/workflows | 
[**mergeProfiles**](DefaultApi.md#mergeProfiles) | **POST** /domains/{DomainName}/profiles/objects/merge | 
[**putIntegration**](DefaultApi.md#putIntegration) | **PUT** /domains/{DomainName}/integrations | 
[**putProfileObject**](DefaultApi.md#putProfileObject) | **PUT** /domains/{DomainName}/profiles/objects | 
[**putProfileObjectType**](DefaultApi.md#putProfileObjectType) | **PUT** /domains/{DomainName}/object-types/{ObjectTypeName} | 
[**searchProfiles**](DefaultApi.md#searchProfiles) | **POST** /domains/{DomainName}/profiles/search | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /tags/{resourceArn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /tags/{resourceArn}#tagKeys | 
[**updateCalculatedAttributeDefinition**](DefaultApi.md#updateCalculatedAttributeDefinition) | **PUT** /domains/{DomainName}/calculated-attributes/{CalculatedAttributeName} | 
[**updateDomain**](DefaultApi.md#updateDomain) | **PUT** /domains/{DomainName} | 
[**updateProfile**](DefaultApi.md#updateProfile) | **PUT** /domains/{DomainName}/profiles | 



## addProfileKey

> AddProfileKeyResponse addProfileKey(domainName, addProfileKeyRequest, opts)



&lt;p&gt;Associates a new key value with a specific profile, such as a Contact Record ContactId.&lt;/p&gt; &lt;p&gt;A profile object can have a single unique key and any number of additional keys that can be used to identify the profile that it belongs to.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let addProfileKeyRequest = new AmazonConnectCustomerProfiles.AddProfileKeyRequest(); // AddProfileKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.addProfileKey(domainName, addProfileKeyRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **addProfileKeyRequest** | [**AddProfileKeyRequest**](AddProfileKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**AddProfileKeyResponse**](AddProfileKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCalculatedAttributeDefinition

> CreateCalculatedAttributeDefinitionResponse createCalculatedAttributeDefinition(domainName, calculatedAttributeName, createCalculatedAttributeDefinitionRequest, opts)



Creates a new calculated attribute definition. After creation, new object data ingested into Customer Profiles will be included in the calculated attribute, which can be retrieved for a profile using the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetCalculatedAttributeForProfile.html\&quot;&gt;GetCalculatedAttributeForProfile&lt;/a&gt; API. Defining a calculated attribute makes it available for all profiles within a domain. Each calculated attribute can only reference one &lt;code&gt;ObjectType&lt;/code&gt; and at most, two fields from that &lt;code&gt;ObjectType&lt;/code&gt;.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let calculatedAttributeName = "calculatedAttributeName_example"; // String | The unique name of the calculated attribute.
let createCalculatedAttributeDefinitionRequest = new AmazonConnectCustomerProfiles.CreateCalculatedAttributeDefinitionRequest(); // CreateCalculatedAttributeDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCalculatedAttributeDefinition(domainName, calculatedAttributeName, createCalculatedAttributeDefinitionRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **calculatedAttributeName** | **String**| The unique name of the calculated attribute. | 
 **createCalculatedAttributeDefinitionRequest** | [**CreateCalculatedAttributeDefinitionRequest**](CreateCalculatedAttributeDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCalculatedAttributeDefinitionResponse**](CreateCalculatedAttributeDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createDomain

> CreateDomainResponse createDomain(domainName, createDomainRequest, opts)



&lt;p&gt;Creates a domain, which is a container for all customer data, such as customer profile attributes, object types, profile keys, and encryption keys. You can create multiple domains, and each domain can have multiple third-party integrations.&lt;/p&gt; &lt;p&gt;Each Amazon Connect instance can be associated with only one domain. Multiple Amazon Connect instances can be associated with one domain.&lt;/p&gt; &lt;p&gt;Use this API or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html\&quot;&gt;UpdateDomain&lt;/a&gt; to enable &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;identity resolution&lt;/a&gt;: set &lt;code&gt;Matching&lt;/code&gt; to true.&lt;/p&gt; &lt;p&gt;To prevent cross-service impersonation when you call this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html\&quot;&gt;Cross-service confused deputy prevention&lt;/a&gt; for sample policies that you should apply. &lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let createDomainRequest = new AmazonConnectCustomerProfiles.CreateDomainRequest(); // CreateDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDomain(domainName, createDomainRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **createDomainRequest** | [**CreateDomainRequest**](CreateDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDomainResponse**](CreateDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEventStream

> CreateEventStreamResponse createEventStream(domainName, eventStreamName, createEventStreamRequest, opts)



&lt;p&gt;Creates an event stream, which is a subscription to real-time events, such as when profiles are created and updated through Amazon Connect Customer Profiles.&lt;/p&gt; &lt;p&gt;Each event stream can be associated with only one Kinesis Data Stream destination in the same region and Amazon Web Services account as the customer profiles domain&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let eventStreamName = "eventStreamName_example"; // String | The name of the event stream.
let createEventStreamRequest = new AmazonConnectCustomerProfiles.CreateEventStreamRequest(); // CreateEventStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEventStream(domainName, eventStreamName, createEventStreamRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **eventStreamName** | **String**| The name of the event stream. | 
 **createEventStreamRequest** | [**CreateEventStreamRequest**](CreateEventStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEventStreamResponse**](CreateEventStreamResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createIntegrationWorkflow

> CreateIntegrationWorkflowResponse createIntegrationWorkflow(domainName, createIntegrationWorkflowRequest, opts)



 Creates an integration workflow. An integration workflow is an async process which ingests historic data and sets up an integration for ongoing updates. The supported Amazon AppFlow sources are Salesforce, ServiceNow, and Marketo. 

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let createIntegrationWorkflowRequest = new AmazonConnectCustomerProfiles.CreateIntegrationWorkflowRequest(); // CreateIntegrationWorkflowRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createIntegrationWorkflow(domainName, createIntegrationWorkflowRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **createIntegrationWorkflowRequest** | [**CreateIntegrationWorkflowRequest**](CreateIntegrationWorkflowRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateIntegrationWorkflowResponse**](CreateIntegrationWorkflowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createProfile

> CreateProfileResponse createProfile(domainName, createProfileRequest, opts)



&lt;p&gt;Creates a standard profile.&lt;/p&gt; &lt;p&gt;A standard profile represents the following attributes for a customer profile in a domain.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let createProfileRequest = new AmazonConnectCustomerProfiles.CreateProfileRequest(); // CreateProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createProfile(domainName, createProfileRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **createProfileRequest** | [**CreateProfileRequest**](CreateProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateProfileResponse**](CreateProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteCalculatedAttributeDefinition

> Object deleteCalculatedAttributeDefinition(domainName, calculatedAttributeName, opts)



Deletes an existing calculated attribute definition. Note that deleting a default calculated attribute is possible, however once deleted, you will be unable to undo that action and will need to recreate it on your own using the CreateCalculatedAttributeDefinition API if you want it back.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let calculatedAttributeName = "calculatedAttributeName_example"; // String | The unique name of the calculated attribute.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCalculatedAttributeDefinition(domainName, calculatedAttributeName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **calculatedAttributeName** | **String**| The unique name of the calculated attribute. | 
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


## deleteDomain

> DeleteDomainResponse deleteDomain(domainName, opts)



Deletes a specific domain and all of its customer data, such as customer profile attributes and their related objects.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDomain(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteDomainResponse**](DeleteDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEventStream

> Object deleteEventStream(domainName, eventStreamName, opts)



Disables and deletes the specified event stream.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let eventStreamName = "eventStreamName_example"; // String | The name of the event stream
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEventStream(domainName, eventStreamName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **eventStreamName** | **String**| The name of the event stream | 
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


## deleteIntegration

> DeleteIntegrationResponse deleteIntegration(domainName, deleteIntegrationRequest, opts)



Removes an integration from a specific domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let deleteIntegrationRequest = new AmazonConnectCustomerProfiles.DeleteIntegrationRequest(); // DeleteIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteIntegration(domainName, deleteIntegrationRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **deleteIntegrationRequest** | [**DeleteIntegrationRequest**](DeleteIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteIntegrationResponse**](DeleteIntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProfile

> DeleteProfileResponse deleteProfile(domainName, deleteProfileRequest, opts)



Deletes the standard customer profile and all data pertaining to the profile.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let deleteProfileRequest = new AmazonConnectCustomerProfiles.DeleteProfileRequest(); // DeleteProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProfile(domainName, deleteProfileRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **deleteProfileRequest** | [**DeleteProfileRequest**](DeleteProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteProfileResponse**](DeleteProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProfileKey

> DeleteProfileKeyResponse deleteProfileKey(domainName, deleteProfileKeyRequest, opts)



Removes a searchable key from a customer profile.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let deleteProfileKeyRequest = new AmazonConnectCustomerProfiles.DeleteProfileKeyRequest(); // DeleteProfileKeyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProfileKey(domainName, deleteProfileKeyRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **deleteProfileKeyRequest** | [**DeleteProfileKeyRequest**](DeleteProfileKeyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteProfileKeyResponse**](DeleteProfileKeyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProfileObject

> DeleteProfileObjectResponse deleteProfileObject(domainName, deleteProfileObjectRequest, opts)



Removes an object associated with a profile of a given ProfileObjectType.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let deleteProfileObjectRequest = new AmazonConnectCustomerProfiles.DeleteProfileObjectRequest(); // DeleteProfileObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProfileObject(domainName, deleteProfileObjectRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **deleteProfileObjectRequest** | [**DeleteProfileObjectRequest**](DeleteProfileObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteProfileObjectResponse**](DeleteProfileObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteProfileObjectType

> DeleteProfileObjectTypeResponse deleteProfileObjectType(domainName, objectTypeName, opts)



Removes a ProfileObjectType from a specific domain as well as removes all the ProfileObjects of that type. It also disables integrations from this specific ProfileObjectType. In addition, it scrubs all of the fields of the standard profile that were populated from this ProfileObjectType.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let objectTypeName = "objectTypeName_example"; // String | The name of the profile object type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteProfileObjectType(domainName, objectTypeName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **objectTypeName** | **String**| The name of the profile object type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteProfileObjectTypeResponse**](DeleteProfileObjectTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteWorkflow

> Object deleteWorkflow(domainName, workflowId, opts)



Deletes the specified workflow and all its corresponding resources. This is an async process.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let workflowId = "workflowId_example"; // String | Unique identifier for the workflow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteWorkflow(domainName, workflowId, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **workflowId** | **String**| Unique identifier for the workflow. | 
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


## getAutoMergingPreview

> GetAutoMergingPreviewResponse getAutoMergingPreview(domainName, getAutoMergingPreviewRequest, opts)



&lt;p&gt;Tests the auto-merging settings of your Identity Resolution Job without merging your data. It randomly selects a sample of matching groups from the existing matching results, and applies the automerging settings that you provided. You can then view the number of profiles in the sample, the number of matches, and the number of profiles identified to be merged. This enables you to evaluate the accuracy of the attributes in your matching list. &lt;/p&gt; &lt;p&gt;You can&#39;t view which profiles are matched and would be merged.&lt;/p&gt; &lt;important&gt; &lt;p&gt;We strongly recommend you use this API to do a dry run of the automerging process before running the Identity Resolution Job. Include &lt;b&gt;at least&lt;/b&gt; two matching attributes. If your matching list includes too few attributes (such as only &lt;code&gt;FirstName&lt;/code&gt; or only &lt;code&gt;LastName&lt;/code&gt;), there may be a large number of matches. This increases the chances of erroneous merges.&lt;/p&gt; &lt;/important&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let getAutoMergingPreviewRequest = new AmazonConnectCustomerProfiles.GetAutoMergingPreviewRequest(); // GetAutoMergingPreviewRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAutoMergingPreview(domainName, getAutoMergingPreviewRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **getAutoMergingPreviewRequest** | [**GetAutoMergingPreviewRequest**](GetAutoMergingPreviewRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAutoMergingPreviewResponse**](GetAutoMergingPreviewResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getCalculatedAttributeDefinition

> GetCalculatedAttributeDefinitionResponse getCalculatedAttributeDefinition(domainName, calculatedAttributeName, opts)



Provides more information on a calculated attribute definition for Customer Profiles.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let calculatedAttributeName = "calculatedAttributeName_example"; // String | The unique name of the calculated attribute.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCalculatedAttributeDefinition(domainName, calculatedAttributeName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **calculatedAttributeName** | **String**| The unique name of the calculated attribute. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCalculatedAttributeDefinitionResponse**](GetCalculatedAttributeDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCalculatedAttributeForProfile

> GetCalculatedAttributeForProfileResponse getCalculatedAttributeForProfile(domainName, profileId, calculatedAttributeName, opts)



Retrieve a calculated attribute for a customer profile.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let profileId = "profileId_example"; // String | The unique identifier of a customer profile.
let calculatedAttributeName = "calculatedAttributeName_example"; // String | The unique name of the calculated attribute.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCalculatedAttributeForProfile(domainName, profileId, calculatedAttributeName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **profileId** | **String**| The unique identifier of a customer profile. | 
 **calculatedAttributeName** | **String**| The unique name of the calculated attribute. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCalculatedAttributeForProfileResponse**](GetCalculatedAttributeForProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomain

> GetDomainResponse getDomain(domainName, opts)



Returns information about a specific domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDomain(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDomainResponse**](GetDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventStream

> GetEventStreamResponse getEventStream(domainName, eventStreamName, opts)



Returns information about the specified event stream in a specific domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let eventStreamName = "eventStreamName_example"; // String | The name of the event stream provided during create operations.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEventStream(domainName, eventStreamName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **eventStreamName** | **String**| The name of the event stream provided during create operations. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEventStreamResponse**](GetEventStreamResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIdentityResolutionJob

> GetIdentityResolutionJobResponse getIdentityResolutionJob(domainName, jobId, opts)



&lt;p&gt;Returns information about an Identity Resolution Job in a specific domain. &lt;/p&gt; &lt;p&gt;Identity Resolution Jobs are set up using the Amazon Connect admin console. For more information, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html\&quot;&gt;Use Identity Resolution to consolidate similar profiles&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let jobId = "jobId_example"; // String | The unique identifier of the Identity Resolution Job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIdentityResolutionJob(domainName, jobId, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **jobId** | **String**| The unique identifier of the Identity Resolution Job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIdentityResolutionJobResponse**](GetIdentityResolutionJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getIntegration

> GetIntegrationResponse getIntegration(domainName, deleteIntegrationRequest, opts)



Returns an integration for a domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let deleteIntegrationRequest = new AmazonConnectCustomerProfiles.DeleteIntegrationRequest(); // DeleteIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getIntegration(domainName, deleteIntegrationRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **deleteIntegrationRequest** | [**DeleteIntegrationRequest**](DeleteIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetIntegrationResponse**](GetIntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getMatches

> GetMatchesResponse getMatches(domainName, opts)



&lt;p&gt;Before calling this API, use &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html\&quot;&gt;CreateDomain&lt;/a&gt; or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html\&quot;&gt;UpdateDomain&lt;/a&gt; to enable identity resolution: set &lt;code&gt;Matching&lt;/code&gt; to true.&lt;/p&gt; &lt;p&gt;GetMatches returns potentially matching profiles, based on the results of the latest run of a machine learning process. &lt;/p&gt; &lt;important&gt; &lt;p&gt;The process of matching duplicate profiles. If &lt;code&gt;Matching&lt;/code&gt; &#x3D; &lt;code&gt;true&lt;/code&gt;, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. &lt;/p&gt; &lt;p&gt;After the Identity Resolution Job completes, use the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;GetMatches&lt;/a&gt; API to return and review the results. Or, if you have configured &lt;code&gt;ExportingConfig&lt;/code&gt; in the &lt;code&gt;MatchingRequest&lt;/code&gt;, you can download the results from S3.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;Amazon Connect uses the following profile attributes to identify matches:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;PhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;HomePhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;BusinessPhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;MobilePhoneNumber&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;EmailAddress&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;PersonalEmailAddress&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;BusinessEmailAddress&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;FullName&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;For example, two or more profiles—with spelling mistakes such as &lt;b&gt;John Doe&lt;/b&gt; and &lt;b&gt;Jhn Doe&lt;/b&gt;, or different casing email addresses such as &lt;b&gt;JOHN_DOE@ANYCOMPANY.COM&lt;/b&gt; and &lt;b&gt;johndoe@anycompany.com&lt;/b&gt;, or different phone number formats such as &lt;b&gt;555-010-0000&lt;/b&gt; and &lt;b&gt;+1-555-010-0000&lt;/b&gt;—can be detected as belonging to the same customer &lt;b&gt;John Doe&lt;/b&gt; and merged into a unified profile.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56 // Number | The maximum number of results to return per page.
};
apiInstance.getMatches(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 

### Return type

[**GetMatchesResponse**](GetMatchesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileObjectType

> GetProfileObjectTypeResponse getProfileObjectType(domainName, objectTypeName, opts)



Returns the object types for a specific domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let objectTypeName = "objectTypeName_example"; // String | The name of the profile object type.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getProfileObjectType(domainName, objectTypeName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **objectTypeName** | **String**| The name of the profile object type. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetProfileObjectTypeResponse**](GetProfileObjectTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getProfileObjectTypeTemplate

> GetProfileObjectTypeTemplateResponse getProfileObjectTypeTemplate(templateId, opts)



&lt;p&gt;Returns the template information for a specific object type.&lt;/p&gt; &lt;p&gt;A template is a predefined ProfileObjectType, such as “Salesforce-Account” or “Salesforce-Contact.” When a user sends a ProfileObject, using the PutProfileObject API, with an ObjectTypeName that matches one of the TemplateIds, it uses the mappings from the template.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let templateId = "templateId_example"; // String | A unique identifier for the object template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getProfileObjectTypeTemplate(templateId, opts, (error, data, response) => {
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
 **templateId** | **String**| A unique identifier for the object template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetProfileObjectTypeTemplateResponse**](GetProfileObjectTypeTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSimilarProfiles

> GetSimilarProfilesResponse getSimilarProfiles(domainName, getSimilarProfilesRequest, opts)



Returns a set of profiles that belong to the same matching group using the &lt;code&gt;matchId&lt;/code&gt; or &lt;code&gt;profileId&lt;/code&gt;. You can also specify the type of matching that you want for finding similar profiles using either &lt;code&gt;RULE_BASED_MATCHING&lt;/code&gt; or &lt;code&gt;ML_BASED_MATCHING&lt;/code&gt;.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let getSimilarProfilesRequest = new AmazonConnectCustomerProfiles.GetSimilarProfilesRequest(); // GetSimilarProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous <code>GetSimilarProfiles</code> API call.
  'maxResults': 56 // Number | The maximum number of objects returned per page.
};
apiInstance.getSimilarProfiles(domainName, getSimilarProfilesRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **getSimilarProfilesRequest** | [**GetSimilarProfilesRequest**](GetSimilarProfilesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous &lt;code&gt;GetSimilarProfiles&lt;/code&gt; API call. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 

### Return type

[**GetSimilarProfilesResponse**](GetSimilarProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## getWorkflow

> GetWorkflowResponse getWorkflow(domainName, workflowId, opts)



Get details of specified workflow.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let workflowId = "workflowId_example"; // String | Unique identifier for the workflow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getWorkflow(domainName, workflowId, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **workflowId** | **String**| Unique identifier for the workflow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetWorkflowResponse**](GetWorkflowResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getWorkflowSteps

> GetWorkflowStepsResponse getWorkflowSteps(domainName, workflowId, opts)



Get granular list of steps in workflow.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let workflowId = "workflowId_example"; // String | Unique identifier for the workflow.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56 // Number | The maximum number of results to return per page.
};
apiInstance.getWorkflowSteps(domainName, workflowId, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **workflowId** | **String**| Unique identifier for the workflow. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 

### Return type

[**GetWorkflowStepsResponse**](GetWorkflowStepsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAccountIntegrations

> ListAccountIntegrationsResponse listAccountIntegrations(deleteIntegrationRequest, opts)



Lists all of the integrations associated to a specific URI in the AWS account.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let deleteIntegrationRequest = new AmazonConnectCustomerProfiles.DeleteIntegrationRequest(); // DeleteIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous ListAccountIntegrations API call.
  'maxResults': 56, // Number | The maximum number of objects returned per page.
  'includeHidden': true // Boolean | Boolean to indicate if hidden integration should be returned. Defaults to <code>False</code>.
};
apiInstance.listAccountIntegrations(deleteIntegrationRequest, opts, (error, data, response) => {
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
 **deleteIntegrationRequest** | [**DeleteIntegrationRequest**](DeleteIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous ListAccountIntegrations API call. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 
 **includeHidden** | **Boolean**| Boolean to indicate if hidden integration should be returned. Defaults to &lt;code&gt;False&lt;/code&gt;. | [optional] 

### Return type

[**ListAccountIntegrationsResponse**](ListAccountIntegrationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCalculatedAttributeDefinitions

> ListCalculatedAttributeDefinitionsResponse listCalculatedAttributeDefinitions(domainName, opts)



Lists calculated attribute definitions for Customer Profiles

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous call to ListCalculatedAttributeDefinitions.
  'maxResults': 56 // Number | The maximum number of calculated attribute definitions returned per page.
};
apiInstance.listCalculatedAttributeDefinitions(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous call to ListCalculatedAttributeDefinitions. | [optional] 
 **maxResults** | **Number**| The maximum number of calculated attribute definitions returned per page. | [optional] 

### Return type

[**ListCalculatedAttributeDefinitionsResponse**](ListCalculatedAttributeDefinitionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listCalculatedAttributesForProfile

> ListCalculatedAttributesForProfileResponse listCalculatedAttributesForProfile(domainName, profileId, opts)



Retrieve a list of calculated attributes for a customer profile.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let profileId = "profileId_example"; // String | The unique identifier of a customer profile.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous call to ListCalculatedAttributesForProfile.
  'maxResults': 56 // Number | The maximum number of calculated attributes returned per page.
};
apiInstance.listCalculatedAttributesForProfile(domainName, profileId, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **profileId** | **String**| The unique identifier of a customer profile. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous call to ListCalculatedAttributesForProfile. | [optional] 
 **maxResults** | **Number**| The maximum number of calculated attributes returned per page. | [optional] 

### Return type

[**ListCalculatedAttributesForProfileResponse**](ListCalculatedAttributesForProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDomains

> ListDomainsResponse listDomains(opts)



Returns a list of all the domains for an AWS account that have been created.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous ListDomain API call.
  'maxResults': 56 // Number | The maximum number of objects returned per page.
};
apiInstance.listDomains(opts, (error, data, response) => {
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
 **nextToken** | **String**| The pagination token from the previous ListDomain API call. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 

### Return type

[**ListDomainsResponse**](ListDomainsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEventStreams

> ListEventStreamsResponse listEventStreams(domainName, opts)



Returns a list of all the event streams in a specific domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | Identifies the next page of results to return.
  'maxResults': 56, // Number | The maximum number of objects returned per page.
  'maxResults2': "maxResults_example", // String | Pagination limit
  'nextToken2': "nextToken_example" // String | Pagination token
};
apiInstance.listEventStreams(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Identifies the next page of results to return. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 
 **maxResults2** | **String**| Pagination limit | [optional] 
 **nextToken2** | **String**| Pagination token | [optional] 

### Return type

[**ListEventStreamsResponse**](ListEventStreamsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIdentityResolutionJobs

> ListIdentityResolutionJobsResponse listIdentityResolutionJobs(domainName, opts)



Lists all of the Identity Resolution Jobs in your domain. The response sorts the list by &lt;code&gt;JobStartTime&lt;/code&gt;.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56 // Number | The maximum number of results to return per page.
};
apiInstance.listIdentityResolutionJobs(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 

### Return type

[**ListIdentityResolutionJobsResponse**](ListIdentityResolutionJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listIntegrations

> ListIntegrationsResponse listIntegrations(domainName, opts)



Lists all of the integrations in your domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous ListIntegrations API call.
  'maxResults': 56, // Number | The maximum number of objects returned per page.
  'includeHidden': true // Boolean | Boolean to indicate if hidden integration should be returned. Defaults to <code>False</code>.
};
apiInstance.listIntegrations(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous ListIntegrations API call. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 
 **includeHidden** | **Boolean**| Boolean to indicate if hidden integration should be returned. Defaults to &lt;code&gt;False&lt;/code&gt;. | [optional] 

### Return type

[**ListIntegrationsResponse**](ListIntegrationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProfileObjectTypeTemplates

> ListProfileObjectTypeTemplatesResponse listProfileObjectTypeTemplates(opts)



Lists all of the template information for object types.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous ListObjectTypeTemplates API call.
  'maxResults': 56 // Number | The maximum number of objects returned per page.
};
apiInstance.listProfileObjectTypeTemplates(opts, (error, data, response) => {
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
 **nextToken** | **String**| The pagination token from the previous ListObjectTypeTemplates API call. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 

### Return type

[**ListProfileObjectTypeTemplatesResponse**](ListProfileObjectTypeTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProfileObjectTypes

> ListProfileObjectTypesResponse listProfileObjectTypes(domainName, opts)



Lists all of the templates available within the service.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | Identifies the next page of results to return.
  'maxResults': 56 // Number | The maximum number of objects returned per page.
};
apiInstance.listProfileObjectTypes(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| Identifies the next page of results to return. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 

### Return type

[**ListProfileObjectTypesResponse**](ListProfileObjectTypesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listProfileObjects

> ListProfileObjectsResponse listProfileObjects(domainName, listProfileObjectsRequest, opts)



Returns a list of objects associated with a profile of a given ProfileObjectType.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let listProfileObjectsRequest = new AmazonConnectCustomerProfiles.ListProfileObjectsRequest(); // ListProfileObjectsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous call to ListProfileObjects.
  'maxResults': 56 // Number | The maximum number of objects returned per page.
};
apiInstance.listProfileObjects(domainName, listProfileObjectsRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **listProfileObjectsRequest** | [**ListProfileObjectsRequest**](ListProfileObjectsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous call to ListProfileObjects. | [optional] 
 **maxResults** | **Number**| The maximum number of objects returned per page. | [optional] 

### Return type

[**ListProfileObjectsResponse**](ListProfileObjectsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRuleBasedMatches

> ListRuleBasedMatchesResponse listRuleBasedMatches(domainName, opts)



Returns a set of &lt;code&gt;MatchIds&lt;/code&gt; that belong to the given domain.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous <code>ListRuleBasedMatches</code> API call.
  'maxResults': 56 // Number | The maximum number of <code>MatchIds</code> returned per page.
};
apiInstance.listRuleBasedMatches(domainName, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous &lt;code&gt;ListRuleBasedMatches&lt;/code&gt; API call. | [optional] 
 **maxResults** | **Number**| The maximum number of &lt;code&gt;MatchIds&lt;/code&gt; returned per page. | [optional] 

### Return type

[**ListRuleBasedMatchesResponse**](ListRuleBasedMatchesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Displays the tags associated with an Amazon Connect Customer Profiles resource. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource for which you want to view tags.
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
 **resourceArn** | **String**| The ARN of the resource for which you want to view tags. | 
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


## listWorkflows

> ListWorkflowsResponse listWorkflows(domainName, listWorkflowsRequest, opts)



Query to list all workflows.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let listWorkflowsRequest = new AmazonConnectCustomerProfiles.ListWorkflowsRequest(); // ListWorkflowsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
  'maxResults': 56 // Number | The maximum number of results to return per page.
};
apiInstance.listWorkflows(domainName, listWorkflowsRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **listWorkflowsRequest** | [**ListWorkflowsRequest**](ListWorkflowsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. | [optional] 
 **maxResults** | **Number**| The maximum number of results to return per page. | [optional] 

### Return type

[**ListWorkflowsResponse**](ListWorkflowsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## mergeProfiles

> MergeProfilesResponse mergeProfiles(domainName, mergeProfilesRequest, opts)



&lt;p&gt;Runs an AWS Lambda job that does the following:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;All the profileKeys in the &lt;code&gt;ProfileToBeMerged&lt;/code&gt; will be moved to the main profile.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All the objects in the &lt;code&gt;ProfileToBeMerged&lt;/code&gt; will be moved to the main profile.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All the &lt;code&gt;ProfileToBeMerged&lt;/code&gt; will be deleted at the end.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;All the profileKeys in the &lt;code&gt;ProfileIdsToBeMerged&lt;/code&gt; will be moved to the main profile.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Standard fields are merged as follows:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;Fields are always \&quot;union\&quot;-ed if there are no conflicts in standard fields or attributeKeys.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;When there are conflicting fields:&lt;/p&gt; &lt;ol&gt; &lt;li&gt; &lt;p&gt;If no &lt;code&gt;SourceProfileIds&lt;/code&gt; entry is specified, the main Profile value is always taken. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;If a &lt;code&gt;SourceProfileIds&lt;/code&gt; entry is specified, the specified profileId is always taken, even if it is a NULL value.&lt;/p&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/li&gt; &lt;/ol&gt; &lt;/li&gt; &lt;/ol&gt; &lt;p&gt;You can use MergeProfiles together with &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;GetMatches&lt;/a&gt;, which returns potentially matching profiles, or use it with the results of another matching system. After profiles have been merged, they cannot be separated (unmerged).&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let mergeProfilesRequest = new AmazonConnectCustomerProfiles.MergeProfilesRequest(); // MergeProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.mergeProfiles(domainName, mergeProfilesRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **mergeProfilesRequest** | [**MergeProfilesRequest**](MergeProfilesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**MergeProfilesResponse**](MergeProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putIntegration

> PutIntegrationResponse putIntegration(domainName, putIntegrationRequest, opts)



&lt;p&gt;Adds an integration between the service and a third-party service, which includes Amazon AppFlow and Amazon Connect.&lt;/p&gt; &lt;p&gt;An integration can belong to only one domain.&lt;/p&gt; &lt;p&gt;To add or remove tags on an existing Integration, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html\&quot;&gt; TagResource &lt;/a&gt;/&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html\&quot;&gt; UntagResource&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let putIntegrationRequest = new AmazonConnectCustomerProfiles.PutIntegrationRequest(); // PutIntegrationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putIntegration(domainName, putIntegrationRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **putIntegrationRequest** | [**PutIntegrationRequest**](PutIntegrationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutIntegrationResponse**](PutIntegrationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putProfileObject

> PutProfileObjectResponse putProfileObject(domainName, putProfileObjectRequest, opts)



&lt;p&gt;Adds additional objects to customer profiles of a given ObjectType.&lt;/p&gt; &lt;p&gt;When adding a specific profile object, like a Contact Record, an inferred profile can get created if it is not mapped to an existing profile. The resulting profile will only have a phone number populated in the standard ProfileObject. Any additional Contact Records with the same phone number will be mapped to the same inferred profile.&lt;/p&gt; &lt;p&gt;When a ProfileObject is created and if a ProfileObjectType already exists for the ProfileObject, it will provide data to a standard profile depending on the ProfileObjectType definition.&lt;/p&gt; &lt;p&gt;PutProfileObject needs an ObjectType, which can be created using PutProfileObjectType.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let putProfileObjectRequest = new AmazonConnectCustomerProfiles.PutProfileObjectRequest(); // PutProfileObjectRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putProfileObject(domainName, putProfileObjectRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **putProfileObjectRequest** | [**PutProfileObjectRequest**](PutProfileObjectRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutProfileObjectResponse**](PutProfileObjectResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putProfileObjectType

> PutProfileObjectTypeResponse putProfileObjectType(domainName, objectTypeName, putProfileObjectTypeRequest, opts)



&lt;p&gt;Defines a ProfileObjectType.&lt;/p&gt; &lt;p&gt;To add or remove tags on an existing ObjectType, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html\&quot;&gt; TagResource&lt;/a&gt;/&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let objectTypeName = "objectTypeName_example"; // String | The name of the profile object type.
let putProfileObjectTypeRequest = new AmazonConnectCustomerProfiles.PutProfileObjectTypeRequest(); // PutProfileObjectTypeRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putProfileObjectType(domainName, objectTypeName, putProfileObjectTypeRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **objectTypeName** | **String**| The name of the profile object type. | 
 **putProfileObjectTypeRequest** | [**PutProfileObjectTypeRequest**](PutProfileObjectTypeRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutProfileObjectTypeResponse**](PutProfileObjectTypeResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## searchProfiles

> SearchProfilesResponse searchProfiles(domainName, searchProfilesRequest, opts)



&lt;p&gt;Searches for profiles within a specific domain using one or more predefined search keys (e.g., _fullName, _phone, _email, _account, etc.) and/or custom-defined search keys. A search key is a data type pair that consists of a &lt;code&gt;KeyName&lt;/code&gt; and &lt;code&gt;Values&lt;/code&gt; list.&lt;/p&gt; &lt;p&gt;This operation supports searching for profiles with a minimum of 1 key-value(s) pair and up to 5 key-value(s) pairs using either &lt;code&gt;AND&lt;/code&gt; or &lt;code&gt;OR&lt;/code&gt; logic.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let searchProfilesRequest = new AmazonConnectCustomerProfiles.SearchProfilesRequest(); // SearchProfilesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The pagination token from the previous SearchProfiles API call.
  'maxResults': 56 // Number | <p>The maximum number of objects returned per page.</p> <p>The default is 20 if this parameter is not included in the request.</p>
};
apiInstance.searchProfiles(domainName, searchProfilesRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **searchProfilesRequest** | [**SearchProfilesRequest**](SearchProfilesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The pagination token from the previous SearchProfiles API call. | [optional] 
 **maxResults** | **Number**| &lt;p&gt;The maximum number of objects returned per page.&lt;/p&gt; &lt;p&gt;The default is 20 if this parameter is not included in the request.&lt;/p&gt; | [optional] 

### Return type

[**SearchProfilesResponse**](SearchProfilesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(resourceArn, tagResourceRequest, opts)



&lt;p&gt;Assigns one or more tags (key-value pairs) to the specified Amazon Connect Customer Profiles resource. Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.&lt;/p&gt; &lt;p&gt;Tags don&#39;t have any semantic meaning to AWS and are interpreted strictly as strings of characters.&lt;/p&gt; &lt;p&gt;You can use the TagResource action with a resource that already has tags. If you specify a new tag key, this tag is appended to the list of tags associated with the resource. If you specify a tag key that is already associated with the resource, the new tag value that you specify replaces the previous value for that tag.&lt;/p&gt; &lt;p&gt;You can associate as many as 50 tags with a resource.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource that you're adding tags to.
let tagResourceRequest = new AmazonConnectCustomerProfiles.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The ARN of the resource that you&#39;re adding tags to. | 
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

> Object untagResource(resourceArn, tagKeys, opts)



Removes one or more tags from the specified Amazon Connect Customer Profiles resource. In Connect Customer Profiles, domains, profile object types, and integrations can be tagged.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The ARN of the resource from which you are removing tags.
let tagKeys = ["null"]; // [String] | The list of tag keys to remove from the resource.
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
 **resourceArn** | **String**| The ARN of the resource from which you are removing tags. | 
 **tagKeys** | [**[String]**](String.md)| The list of tag keys to remove from the resource. | 
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


## updateCalculatedAttributeDefinition

> UpdateCalculatedAttributeDefinitionResponse updateCalculatedAttributeDefinition(domainName, calculatedAttributeName, updateCalculatedAttributeDefinitionRequest, opts)



Updates an existing calculated attribute definition. When updating the Conditions, note that increasing the date range of a calculated attribute will not trigger inclusion of historical data greater than the current date range.

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let calculatedAttributeName = "calculatedAttributeName_example"; // String | The unique name of the calculated attribute.
let updateCalculatedAttributeDefinitionRequest = new AmazonConnectCustomerProfiles.UpdateCalculatedAttributeDefinitionRequest(); // UpdateCalculatedAttributeDefinitionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCalculatedAttributeDefinition(domainName, calculatedAttributeName, updateCalculatedAttributeDefinitionRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **calculatedAttributeName** | **String**| The unique name of the calculated attribute. | 
 **updateCalculatedAttributeDefinitionRequest** | [**UpdateCalculatedAttributeDefinitionRequest**](UpdateCalculatedAttributeDefinitionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateCalculatedAttributeDefinitionResponse**](UpdateCalculatedAttributeDefinitionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateDomain

> UpdateDomainResponse updateDomain(domainName, updateDomainRequest, opts)



&lt;p&gt;Updates the properties of a domain, including creating or selecting a dead letter queue or an encryption key.&lt;/p&gt; &lt;p&gt;After a domain is created, the name can’t be changed.&lt;/p&gt; &lt;p&gt;Use this API or &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html\&quot;&gt;CreateDomain&lt;/a&gt; to enable &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html\&quot;&gt;identity resolution&lt;/a&gt;: set &lt;code&gt;Matching&lt;/code&gt; to true.&lt;/p&gt; &lt;p&gt;To prevent cross-service impersonation when you call this API, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/connect/latest/adminguide/cross-service-confused-deputy-prevention.html\&quot;&gt;Cross-service confused deputy prevention&lt;/a&gt; for sample policies that you should apply. &lt;/p&gt; &lt;p&gt;To add or remove tags on an existing Domain, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_TagResource.html\&quot;&gt;TagResource&lt;/a&gt;/&lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UntagResource.html\&quot;&gt;UntagResource&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let updateDomainRequest = new AmazonConnectCustomerProfiles.UpdateDomainRequest(); // UpdateDomainRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateDomain(domainName, updateDomainRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **updateDomainRequest** | [**UpdateDomainRequest**](UpdateDomainRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateDomainResponse**](UpdateDomainResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateProfile

> UpdateProfileResponse updateProfile(domainName, updateProfileRequest, opts)



&lt;p&gt;Updates the properties of a profile. The ProfileId is required for updating a customer profile.&lt;/p&gt; &lt;p&gt;When calling the UpdateProfile API, specifying an empty string value means that any existing value will be removed. Not specifying a string value means that any value already there will be kept.&lt;/p&gt;

### Example

```javascript
import AmazonConnectCustomerProfiles from 'amazon_connect_customer_profiles';
let defaultClient = AmazonConnectCustomerProfiles.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonConnectCustomerProfiles.DefaultApi();
let domainName = "domainName_example"; // String | The unique name of the domain.
let updateProfileRequest = new AmazonConnectCustomerProfiles.UpdateProfileRequest(); // UpdateProfileRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateProfile(domainName, updateProfileRequest, opts, (error, data, response) => {
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
 **domainName** | **String**| The unique name of the domain. | 
 **updateProfileRequest** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateProfileResponse**](UpdateProfileResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

