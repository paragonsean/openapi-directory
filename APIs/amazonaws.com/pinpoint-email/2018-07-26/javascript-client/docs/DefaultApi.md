# AmazonPinpointEmailService.DefaultApi

All URIs are relative to *http://email.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createConfigurationSet**](DefaultApi.md#createConfigurationSet) | **POST** /v1/email/configuration-sets | 
[**createConfigurationSetEventDestination**](DefaultApi.md#createConfigurationSetEventDestination) | **POST** /v1/email/configuration-sets/{ConfigurationSetName}/event-destinations | 
[**createDedicatedIpPool**](DefaultApi.md#createDedicatedIpPool) | **POST** /v1/email/dedicated-ip-pools | 
[**createDeliverabilityTestReport**](DefaultApi.md#createDeliverabilityTestReport) | **POST** /v1/email/deliverability-dashboard/test | 
[**createEmailIdentity**](DefaultApi.md#createEmailIdentity) | **POST** /v1/email/identities | 
[**deleteConfigurationSet**](DefaultApi.md#deleteConfigurationSet) | **DELETE** /v1/email/configuration-sets/{ConfigurationSetName} | 
[**deleteConfigurationSetEventDestination**](DefaultApi.md#deleteConfigurationSetEventDestination) | **DELETE** /v1/email/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName} | 
[**deleteDedicatedIpPool**](DefaultApi.md#deleteDedicatedIpPool) | **DELETE** /v1/email/dedicated-ip-pools/{PoolName} | 
[**deleteEmailIdentity**](DefaultApi.md#deleteEmailIdentity) | **DELETE** /v1/email/identities/{EmailIdentity} | 
[**getAccount**](DefaultApi.md#getAccount) | **GET** /v1/email/account | 
[**getBlacklistReports**](DefaultApi.md#getBlacklistReports) | **GET** /v1/email/deliverability-dashboard/blacklist-report#BlacklistItemNames | 
[**getConfigurationSet**](DefaultApi.md#getConfigurationSet) | **GET** /v1/email/configuration-sets/{ConfigurationSetName} | 
[**getConfigurationSetEventDestinations**](DefaultApi.md#getConfigurationSetEventDestinations) | **GET** /v1/email/configuration-sets/{ConfigurationSetName}/event-destinations | 
[**getDedicatedIp**](DefaultApi.md#getDedicatedIp) | **GET** /v1/email/dedicated-ips/{IP} | 
[**getDedicatedIps**](DefaultApi.md#getDedicatedIps) | **GET** /v1/email/dedicated-ips | 
[**getDeliverabilityDashboardOptions**](DefaultApi.md#getDeliverabilityDashboardOptions) | **GET** /v1/email/deliverability-dashboard | 
[**getDeliverabilityTestReport**](DefaultApi.md#getDeliverabilityTestReport) | **GET** /v1/email/deliverability-dashboard/test-reports/{ReportId} | 
[**getDomainDeliverabilityCampaign**](DefaultApi.md#getDomainDeliverabilityCampaign) | **GET** /v1/email/deliverability-dashboard/campaigns/{CampaignId} | 
[**getDomainStatisticsReport**](DefaultApi.md#getDomainStatisticsReport) | **GET** /v1/email/deliverability-dashboard/statistics-report/{Domain}#StartDate&amp;EndDate | 
[**getEmailIdentity**](DefaultApi.md#getEmailIdentity) | **GET** /v1/email/identities/{EmailIdentity} | 
[**listConfigurationSets**](DefaultApi.md#listConfigurationSets) | **GET** /v1/email/configuration-sets | 
[**listDedicatedIpPools**](DefaultApi.md#listDedicatedIpPools) | **GET** /v1/email/dedicated-ip-pools | 
[**listDeliverabilityTestReports**](DefaultApi.md#listDeliverabilityTestReports) | **GET** /v1/email/deliverability-dashboard/test-reports | 
[**listDomainDeliverabilityCampaigns**](DefaultApi.md#listDomainDeliverabilityCampaigns) | **GET** /v1/email/deliverability-dashboard/domains/{SubscribedDomain}/campaigns#StartDate&amp;EndDate | 
[**listEmailIdentities**](DefaultApi.md#listEmailIdentities) | **GET** /v1/email/identities | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /v1/email/tags#ResourceArn | 
[**putAccountDedicatedIpWarmupAttributes**](DefaultApi.md#putAccountDedicatedIpWarmupAttributes) | **PUT** /v1/email/account/dedicated-ips/warmup | 
[**putAccountSendingAttributes**](DefaultApi.md#putAccountSendingAttributes) | **PUT** /v1/email/account/sending | 
[**putConfigurationSetDeliveryOptions**](DefaultApi.md#putConfigurationSetDeliveryOptions) | **PUT** /v1/email/configuration-sets/{ConfigurationSetName}/delivery-options | 
[**putConfigurationSetReputationOptions**](DefaultApi.md#putConfigurationSetReputationOptions) | **PUT** /v1/email/configuration-sets/{ConfigurationSetName}/reputation-options | 
[**putConfigurationSetSendingOptions**](DefaultApi.md#putConfigurationSetSendingOptions) | **PUT** /v1/email/configuration-sets/{ConfigurationSetName}/sending | 
[**putConfigurationSetTrackingOptions**](DefaultApi.md#putConfigurationSetTrackingOptions) | **PUT** /v1/email/configuration-sets/{ConfigurationSetName}/tracking-options | 
[**putDedicatedIpInPool**](DefaultApi.md#putDedicatedIpInPool) | **PUT** /v1/email/dedicated-ips/{IP}/pool | 
[**putDedicatedIpWarmupAttributes**](DefaultApi.md#putDedicatedIpWarmupAttributes) | **PUT** /v1/email/dedicated-ips/{IP}/warmup | 
[**putDeliverabilityDashboardOption**](DefaultApi.md#putDeliverabilityDashboardOption) | **PUT** /v1/email/deliverability-dashboard | 
[**putEmailIdentityDkimAttributes**](DefaultApi.md#putEmailIdentityDkimAttributes) | **PUT** /v1/email/identities/{EmailIdentity}/dkim | 
[**putEmailIdentityFeedbackAttributes**](DefaultApi.md#putEmailIdentityFeedbackAttributes) | **PUT** /v1/email/identities/{EmailIdentity}/feedback | 
[**putEmailIdentityMailFromAttributes**](DefaultApi.md#putEmailIdentityMailFromAttributes) | **PUT** /v1/email/identities/{EmailIdentity}/mail-from | 
[**sendEmail**](DefaultApi.md#sendEmail) | **POST** /v1/email/outbound-emails | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /v1/email/tags | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /v1/email/tags#ResourceArn&amp;TagKeys | 
[**updateConfigurationSetEventDestination**](DefaultApi.md#updateConfigurationSetEventDestination) | **PUT** /v1/email/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName} | 



## createConfigurationSet

> Object createConfigurationSet(createConfigurationSetRequest, opts)



Create a configuration set. &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send using Amazon Pinpoint. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. 

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let createConfigurationSetRequest = new AmazonPinpointEmailService.CreateConfigurationSetRequest(); // CreateConfigurationSetRequest | 
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



&lt;p&gt;Create an event destination. In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt; &lt;p&gt;A single configuration set can include more than one event destination.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to add an event destination to.
let createConfigurationSetEventDestinationRequest = new AmazonPinpointEmailService.CreateConfigurationSetEventDestinationRequest(); // CreateConfigurationSetEventDestinationRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set that you want to add an event destination to. | 
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


## createDedicatedIpPool

> Object createDedicatedIpPool(createDedicatedIpPoolRequest, opts)



Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Pinpoint account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, Amazon Pinpoint sends it using only the IP addresses in the associated pool.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let createDedicatedIpPoolRequest = new AmazonPinpointEmailService.CreateDedicatedIpPoolRequest(); // CreateDedicatedIpPoolRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDedicatedIpPool(createDedicatedIpPoolRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDedicatedIpPoolRequest** | [**CreateDedicatedIpPoolRequest**](CreateDedicatedIpPoolRequest.md)|  | 
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


## createDeliverabilityTestReport

> CreateDeliverabilityTestReportResponse createDeliverabilityTestReport(createDeliverabilityTestReportRequest, opts)



Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon Pinpoint then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the &lt;code&gt;GetDeliverabilityTestReport&lt;/code&gt; operation to view the results of the test.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let createDeliverabilityTestReportRequest = new AmazonPinpointEmailService.CreateDeliverabilityTestReportRequest(); // CreateDeliverabilityTestReportRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createDeliverabilityTestReport(createDeliverabilityTestReportRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createDeliverabilityTestReportRequest** | [**CreateDeliverabilityTestReportRequest**](CreateDeliverabilityTestReportRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateDeliverabilityTestReportResponse**](CreateDeliverabilityTestReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEmailIdentity

> CreateEmailIdentityResponse createEmailIdentity(createEmailIdentityRequest, opts)



&lt;p&gt;Verifies an email identity for use with Amazon Pinpoint. In Amazon Pinpoint, an identity is an email address or domain that you use when you send email. Before you can use an identity to send email with Amazon Pinpoint, you first have to verify it. By verifying an address, you demonstrate that you&#39;re the owner of the address, and that you&#39;ve given Amazon Pinpoint permission to send email from the address.&lt;/p&gt; &lt;p&gt;When you verify an email address, Amazon Pinpoint sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. &lt;/p&gt; &lt;p&gt;When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon Pinpoint detects these records in the DNS configuration for your domain. It usually takes around 72 hours to complete the domain verification process.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let createEmailIdentityRequest = new AmazonPinpointEmailService.CreateEmailIdentityRequest(); // CreateEmailIdentityRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEmailIdentity(createEmailIdentityRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createEmailIdentityRequest** | [**CreateEmailIdentityRequest**](CreateEmailIdentityRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEmailIdentityResponse**](CreateEmailIdentityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteConfigurationSet

> Object deleteConfigurationSet(configurationSetName, opts)



&lt;p&gt;Delete an existing configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to delete.
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
 **configurationSetName** | **String**| The name of the configuration set that you want to delete. | 
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



&lt;p&gt;Delete an event destination.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that contains the event destination that you want to delete.
let eventDestinationName = "eventDestinationName_example"; // String | The name of the event destination that you want to delete.
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
 **configurationSetName** | **String**| The name of the configuration set that contains the event destination that you want to delete. | 
 **eventDestinationName** | **String**| The name of the event destination that you want to delete. | 
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


## deleteDedicatedIpPool

> Object deleteDedicatedIpPool(poolName, opts)



Delete a dedicated IP pool.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let poolName = "poolName_example"; // String | The name of the dedicated IP pool that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteDedicatedIpPool(poolName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolName** | **String**| The name of the dedicated IP pool that you want to delete. | 
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


## deleteEmailIdentity

> Object deleteEmailIdentity(emailIdentity, opts)



Deletes an email identity that you previously verified for use with Amazon Pinpoint. An identity can be either an email address or a domain name.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEmailIdentity(emailIdentity, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The identity (that is, the email address or domain) that you want to delete from your Amazon Pinpoint account. | 
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


## getAccount

> GetAccountResponse getAccount(opts)



Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAccount(opts, (error, data, response) => {
  if (error) {
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

[**GetAccountResponse**](GetAccountResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBlacklistReports

> GetBlacklistReportsResponse getBlacklistReports(blacklistItemNames, opts)



Retrieve a list of the blacklists that your dedicated IP addresses appear on.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let blacklistItemNames = ["null"]; // [String] | A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon Pinpoint or Amazon SES.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBlacklistReports(blacklistItemNames, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **blacklistItemNames** | [**[String]**](String.md)| A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon Pinpoint or Amazon SES. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBlacklistReportsResponse**](GetBlacklistReportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfigurationSet

> GetConfigurationSetResponse getConfigurationSet(configurationSetName, opts)



&lt;p&gt;Get information about an existing configuration set, including the dedicated IP pool that it&#39;s associated with, whether or not it&#39;s enabled for sending email, and more.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to obtain more information about.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getConfigurationSet(configurationSetName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set that you want to obtain more information about. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetConfigurationSetResponse**](GetConfigurationSetResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getConfigurationSetEventDestinations

> GetConfigurationSetEventDestinationsResponse getConfigurationSetEventDestinations(configurationSetName, opts)



&lt;p&gt;Retrieve a list of event destinations that are associated with a configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that contains the event destination.
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
 **configurationSetName** | **String**| The name of the configuration set that contains the event destination. | 
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


## getDedicatedIp

> GetDedicatedIpResponse getDedicatedIp(IP, opts)



Get information about a dedicated IP address, including the name of the dedicated IP pool that it&#39;s associated with, as well information about the automatic warm-up process for the address.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let IP = "IP_example"; // String | The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Pinpoint account.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDedicatedIp(IP, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **IP** | **String**| The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that&#39;s assocaited with your Amazon Pinpoint account. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDedicatedIpResponse**](GetDedicatedIpResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDedicatedIps

> GetDedicatedIpsResponse getDedicatedIps(opts)



List the dedicated IP addresses that are associated with your Amazon Pinpoint account.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'poolName': "poolName_example", // String | The name of the IP pool that the dedicated IP address is associated with.
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>GetDedicatedIps</code> to indicate the position of the dedicated IP pool in the list of IP pools.
  'pageSize': 56 // Number | The number of results to show in a single call to <code>GetDedicatedIpsRequest</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.
};
apiInstance.getDedicatedIps(opts, (error, data, response) => {
  if (error) {
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
 **poolName** | **String**| The name of the IP pool that the dedicated IP address is associated with. | [optional] 
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;GetDedicatedIps&lt;/code&gt; to indicate the position of the dedicated IP pool in the list of IP pools. | [optional] 
 **pageSize** | **Number**| The number of results to show in a single call to &lt;code&gt;GetDedicatedIpsRequest&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results. | [optional] 

### Return type

[**GetDedicatedIpsResponse**](GetDedicatedIpsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeliverabilityDashboardOptions

> GetDeliverabilityDashboardOptionsResponse getDeliverabilityDashboardOptions(opts)



&lt;p&gt;Retrieve information about the status of the Deliverability dashboard for your Amazon Pinpoint account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon Pinpoint. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/pinpoint/pricing/\&quot;&gt;Amazon Pinpoint Pricing&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeliverabilityDashboardOptions(opts, (error, data, response) => {
  if (error) {
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

[**GetDeliverabilityDashboardOptionsResponse**](GetDeliverabilityDashboardOptionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDeliverabilityTestReport

> GetDeliverabilityTestReportResponse getDeliverabilityTestReport(reportId, opts)



Retrieve the results of a predictive inbox placement test.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let reportId = "reportId_example"; // String | A unique string that identifies the predictive inbox placement test.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDeliverabilityTestReport(reportId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reportId** | **String**| A unique string that identifies the predictive inbox placement test. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDeliverabilityTestReportResponse**](GetDeliverabilityTestReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainDeliverabilityCampaign

> GetDomainDeliverabilityCampaignResponse getDomainDeliverabilityCampaign(campaignId, opts)



Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (&lt;code&gt;PutDeliverabilityDashboardOption&lt;/code&gt; operation).

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDomainDeliverabilityCampaign(campaignId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **campaignId** | **String**| The unique identifier for the campaign. Amazon Pinpoint automatically generates and assigns this identifier to a campaign. This value is not the same as the campaign identifier that Amazon Pinpoint assigns to campaigns that you create and manage by using the Amazon Pinpoint API or the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDomainDeliverabilityCampaignResponse**](GetDomainDeliverabilityCampaignResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDomainStatisticsReport

> GetDomainStatisticsReportResponse getDomainStatisticsReport(domain, startDate, endDate, opts)



Retrieve inbox placement and engagement rates for the domains that you use to send email.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let domain = "domain_example"; // String | The domain that you want to obtain deliverability metrics for.
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The first day (in Unix time) that you want to obtain domain deliverability metrics for.
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The last day (in Unix time) that you want to obtain domain deliverability metrics for. The <code>EndDate</code> that you specify has to be less than or equal to 30 days after the <code>StartDate</code>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDomainStatisticsReport(domain, startDate, endDate, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | **String**| The domain that you want to obtain deliverability metrics for. | 
 **startDate** | **Date**| The first day (in Unix time) that you want to obtain domain deliverability metrics for. | 
 **endDate** | **Date**| The last day (in Unix time) that you want to obtain domain deliverability metrics for. The &lt;code&gt;EndDate&lt;/code&gt; that you specify has to be less than or equal to 30 days after the &lt;code&gt;StartDate&lt;/code&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDomainStatisticsReportResponse**](GetDomainStatisticsReportResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmailIdentity

> GetEmailIdentityResponse getEmailIdentity(emailIdentity, opts)



Provides information about a specific identity associated with your Amazon Pinpoint account, including the identity&#39;s verification status, its DKIM authentication status, and its custom Mail-From settings.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity that you want to retrieve details for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEmailIdentity(emailIdentity, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity that you want to retrieve details for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEmailIdentityResponse**](GetEmailIdentityResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationSets

> ListConfigurationSetsResponse listConfigurationSets(opts)



&lt;p&gt;List all of the configuration sets associated with your Amazon Pinpoint account in the current region.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListConfigurationSets</code> to indicate the position in the list of configuration sets.
  'pageSize': 56 // Number | The number of results to show in a single call to <code>ListConfigurationSets</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.
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
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListConfigurationSets&lt;/code&gt; to indicate the position in the list of configuration sets. | [optional] 
 **pageSize** | **Number**| The number of results to show in a single call to &lt;code&gt;ListConfigurationSets&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results. | [optional] 

### Return type

[**ListConfigurationSetsResponse**](ListConfigurationSetsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDedicatedIpPools

> ListDedicatedIpPoolsResponse listDedicatedIpPools(opts)



List all of the dedicated IP pools that exist in your Amazon Pinpoint account in the current AWS Region.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListDedicatedIpPools</code> to indicate the position in the list of dedicated IP pools.
  'pageSize': 56 // Number | The number of results to show in a single call to <code>ListDedicatedIpPools</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.
};
apiInstance.listDedicatedIpPools(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListDedicatedIpPools&lt;/code&gt; to indicate the position in the list of dedicated IP pools. | [optional] 
 **pageSize** | **Number**| The number of results to show in a single call to &lt;code&gt;ListDedicatedIpPools&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results. | [optional] 

### Return type

[**ListDedicatedIpPoolsResponse**](ListDedicatedIpPoolsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDeliverabilityTestReports

> ListDeliverabilityTestReportsResponse listDeliverabilityTestReports(opts)



Show a list of the predictive inbox placement tests that you&#39;ve performed, regardless of their statuses. For predictive inbox placement tests that are complete, you can use the &lt;code&gt;GetDeliverabilityTestReport&lt;/code&gt; operation to view the results.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListDeliverabilityTestReports</code> to indicate the position in the list of predictive inbox placement tests.
  'pageSize': 56 // Number | <p>The number of results to show in a single call to <code>ListDeliverabilityTestReports</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>
};
apiInstance.listDeliverabilityTestReports(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListDeliverabilityTestReports&lt;/code&gt; to indicate the position in the list of predictive inbox placement tests. | [optional] 
 **pageSize** | **Number**| &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListDeliverabilityTestReports&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 0, and can be no more than 1000.&lt;/p&gt; | [optional] 

### Return type

[**ListDeliverabilityTestReportsResponse**](ListDeliverabilityTestReportsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDomainDeliverabilityCampaigns

> ListDomainDeliverabilityCampaignsResponse listDomainDeliverabilityCampaigns(startDate, endDate, subscribedDomain, opts)



Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard (&lt;code&gt;PutDeliverabilityDashboardOption&lt;/code&gt; operation) for the domain.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The first day, in Unix time format, that you want to obtain deliverability data for.
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The last day, in Unix time format, that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the <code>StartDate</code> parameter.
let subscribedDomain = "subscribedDomain_example"; // String | The domain to obtain deliverability data for.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token that’s returned from a previous call to the <code>ListDomainDeliverabilityCampaigns</code> operation. This token indicates the position of a campaign in the list of campaigns.
  'pageSize': 56 // Number | The maximum number of results to include in response to a single call to the <code>ListDomainDeliverabilityCampaigns</code> operation. If the number of results is larger than the number that you specify in this parameter, the response includes a <code>NextToken</code> element, which you can use to obtain additional results.
};
apiInstance.listDomainDeliverabilityCampaigns(startDate, endDate, subscribedDomain, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **startDate** | **Date**| The first day, in Unix time format, that you want to obtain deliverability data for. | 
 **endDate** | **Date**| The last day, in Unix time format, that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the &lt;code&gt;StartDate&lt;/code&gt; parameter. | 
 **subscribedDomain** | **String**| The domain to obtain deliverability data for. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A token that’s returned from a previous call to the &lt;code&gt;ListDomainDeliverabilityCampaigns&lt;/code&gt; operation. This token indicates the position of a campaign in the list of campaigns. | [optional] 
 **pageSize** | **Number**| The maximum number of results to include in response to a single call to the &lt;code&gt;ListDomainDeliverabilityCampaigns&lt;/code&gt; operation. If the number of results is larger than the number that you specify in this parameter, the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results. | [optional] 

### Return type

[**ListDomainDeliverabilityCampaignsResponse**](ListDomainDeliverabilityCampaignsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listEmailIdentities

> ListEmailIdentitiesResponse listEmailIdentities(opts)



Returns a list of all of the email identities that are associated with your Amazon Pinpoint account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren&#39;t.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListEmailIdentities</code> to indicate the position in the list of identities.
  'pageSize': 56 // Number | <p>The number of results to show in a single call to <code>ListEmailIdentities</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 0, and can be no more than 1000.</p>
};
apiInstance.listEmailIdentities(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListEmailIdentities&lt;/code&gt; to indicate the position in the list of identities. | [optional] 
 **pageSize** | **Number**| &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListEmailIdentities&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 0, and can be no more than 1000.&lt;/p&gt; | [optional] 

### Return type

[**ListEmailIdentitiesResponse**](ListEmailIdentitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Retrieve a list of the tags (keys and values) that are associated with a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource in Amazon Pinpoint. Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an optional associated &lt;i&gt;tag value&lt;/i&gt;. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource that you want to retrieve tag information for. | 
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


## putAccountDedicatedIpWarmupAttributes

> Object putAccountDedicatedIpWarmupAttributes(putAccountDedicatedIpWarmupAttributesRequest, opts)



Enable or disable the automatic warm-up feature for dedicated IP addresses.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let putAccountDedicatedIpWarmupAttributesRequest = new AmazonPinpointEmailService.PutAccountDedicatedIpWarmupAttributesRequest(); // PutAccountDedicatedIpWarmupAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccountDedicatedIpWarmupAttributes(putAccountDedicatedIpWarmupAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putAccountDedicatedIpWarmupAttributesRequest** | [**PutAccountDedicatedIpWarmupAttributesRequest**](PutAccountDedicatedIpWarmupAttributesRequest.md)|  | 
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


## putAccountSendingAttributes

> Object putAccountSendingAttributes(putAccountSendingAttributesRequest, opts)



Enable or disable the ability of your account to send email.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let putAccountSendingAttributesRequest = new AmazonPinpointEmailService.PutAccountSendingAttributesRequest(); // PutAccountSendingAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccountSendingAttributes(putAccountSendingAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putAccountSendingAttributesRequest** | [**PutAccountSendingAttributesRequest**](PutAccountSendingAttributesRequest.md)|  | 
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


## putConfigurationSetDeliveryOptions

> Object putConfigurationSetDeliveryOptions(configurationSetName, putConfigurationSetDeliveryOptionsRequest, opts)



Associate a configuration set with a dedicated IP pool. You can use dedicated IP pools to create groups of dedicated IP addresses for sending specific types of email.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to associate with a dedicated IP pool.
let putConfigurationSetDeliveryOptionsRequest = new AmazonPinpointEmailService.PutConfigurationSetDeliveryOptionsRequest(); // PutConfigurationSetDeliveryOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfigurationSetDeliveryOptions(configurationSetName, putConfigurationSetDeliveryOptionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set that you want to associate with a dedicated IP pool. | 
 **putConfigurationSetDeliveryOptionsRequest** | [**PutConfigurationSetDeliveryOptionsRequest**](PutConfigurationSetDeliveryOptionsRequest.md)|  | 
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


## putConfigurationSetReputationOptions

> Object putConfigurationSetReputationOptions(configurationSetName, putConfigurationSetReputationOptionsRequest, opts)



Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific AWS Region.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to enable or disable reputation metric tracking for.
let putConfigurationSetReputationOptionsRequest = new AmazonPinpointEmailService.PutConfigurationSetReputationOptionsRequest(); // PutConfigurationSetReputationOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfigurationSetReputationOptions(configurationSetName, putConfigurationSetReputationOptionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set that you want to enable or disable reputation metric tracking for. | 
 **putConfigurationSetReputationOptionsRequest** | [**PutConfigurationSetReputationOptionsRequest**](PutConfigurationSetReputationOptionsRequest.md)|  | 
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


## putConfigurationSetSendingOptions

> Object putConfigurationSetSendingOptions(configurationSetName, putConfigurationSetSendingOptionsRequest, opts)



Enable or disable email sending for messages that use a particular configuration set in a specific AWS Region.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to enable or disable email sending for.
let putConfigurationSetSendingOptionsRequest = new AmazonPinpointEmailService.PutConfigurationSetSendingOptionsRequest(); // PutConfigurationSetSendingOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfigurationSetSendingOptions(configurationSetName, putConfigurationSetSendingOptionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set that you want to enable or disable email sending for. | 
 **putConfigurationSetSendingOptionsRequest** | [**PutConfigurationSetSendingOptionsRequest**](PutConfigurationSetSendingOptionsRequest.md)|  | 
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


## putConfigurationSetTrackingOptions

> Object putConfigurationSetTrackingOptions(configurationSetName, putConfigurationSetTrackingOptionsRequest, opts)



Specify a custom domain to use for open and click tracking elements in email that you send using Amazon Pinpoint.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that you want to add a custom tracking domain to.
let putConfigurationSetTrackingOptionsRequest = new AmazonPinpointEmailService.PutConfigurationSetTrackingOptionsRequest(); // PutConfigurationSetTrackingOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfigurationSetTrackingOptions(configurationSetName, putConfigurationSetTrackingOptionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set that you want to add a custom tracking domain to. | 
 **putConfigurationSetTrackingOptionsRequest** | [**PutConfigurationSetTrackingOptionsRequest**](PutConfigurationSetTrackingOptionsRequest.md)|  | 
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


## putDedicatedIpInPool

> Object putDedicatedIpInPool(IP, putDedicatedIpInPoolRequest, opts)



&lt;p&gt;Move a dedicated IP address to an existing dedicated IP pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The dedicated IP address that you specify must already exist, and must be associated with your Amazon Pinpoint account. &lt;/p&gt; &lt;p&gt;The dedicated IP pool you specify must already exist. You can create a new pool by using the &lt;code&gt;CreateDedicatedIpPool&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let IP = "IP_example"; // String | The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Pinpoint account.
let putDedicatedIpInPoolRequest = new AmazonPinpointEmailService.PutDedicatedIpInPoolRequest(); // PutDedicatedIpInPoolRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDedicatedIpInPool(IP, putDedicatedIpInPoolRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **IP** | **String**| The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that&#39;s associated with your Amazon Pinpoint account. | 
 **putDedicatedIpInPoolRequest** | [**PutDedicatedIpInPoolRequest**](PutDedicatedIpInPoolRequest.md)|  | 
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


## putDedicatedIpWarmupAttributes

> Object putDedicatedIpWarmupAttributes(IP, putDedicatedIpWarmupAttributesRequest, opts)



&lt;p/&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let IP = "IP_example"; // String | The dedicated IP address that you want to update the warm-up attributes for.
let putDedicatedIpWarmupAttributesRequest = new AmazonPinpointEmailService.PutDedicatedIpWarmupAttributesRequest(); // PutDedicatedIpWarmupAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDedicatedIpWarmupAttributes(IP, putDedicatedIpWarmupAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **IP** | **String**| The dedicated IP address that you want to update the warm-up attributes for. | 
 **putDedicatedIpWarmupAttributesRequest** | [**PutDedicatedIpWarmupAttributesRequest**](PutDedicatedIpWarmupAttributesRequest.md)|  | 
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


## putDeliverabilityDashboardOption

> Object putDeliverabilityDashboardOption(putDeliverabilityDashboardOptionRequest, opts)



&lt;p&gt;Enable or disable the Deliverability dashboard for your Amazon Pinpoint account. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email using Amazon Pinpoint. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon Pinpoint. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/pinpoint/pricing/\&quot;&gt;Amazon Pinpoint Pricing&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let putDeliverabilityDashboardOptionRequest = new AmazonPinpointEmailService.PutDeliverabilityDashboardOptionRequest(); // PutDeliverabilityDashboardOptionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDeliverabilityDashboardOption(putDeliverabilityDashboardOptionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putDeliverabilityDashboardOptionRequest** | [**PutDeliverabilityDashboardOptionRequest**](PutDeliverabilityDashboardOptionRequest.md)|  | 
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


## putEmailIdentityDkimAttributes

> Object putEmailIdentityDkimAttributes(emailIdentity, putEmailIdentityDkimAttributesRequest, opts)



Used to enable or disable DKIM authentication for an email identity.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity that you want to change the DKIM settings for.
let putEmailIdentityDkimAttributesRequest = new AmazonPinpointEmailService.PutEmailIdentityDkimAttributesRequest(); // PutEmailIdentityDkimAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEmailIdentityDkimAttributes(emailIdentity, putEmailIdentityDkimAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity that you want to change the DKIM settings for. | 
 **putEmailIdentityDkimAttributesRequest** | [**PutEmailIdentityDkimAttributesRequest**](PutEmailIdentityDkimAttributesRequest.md)|  | 
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


## putEmailIdentityFeedbackAttributes

> Object putEmailIdentityFeedbackAttributes(emailIdentity, putEmailIdentityFeedbackAttributesRequest, opts)



&lt;p&gt;Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.&lt;/p&gt; &lt;p&gt;When you enable feedback forwarding, Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.&lt;/p&gt; &lt;p&gt;When you disable feedback forwarding, Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic. You&#39;re required to have a method of tracking bounces and complaints. If you haven&#39;t set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity that you want to configure bounce and complaint feedback forwarding for.
let putEmailIdentityFeedbackAttributesRequest = new AmazonPinpointEmailService.PutEmailIdentityFeedbackAttributesRequest(); // PutEmailIdentityFeedbackAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEmailIdentityFeedbackAttributes(emailIdentity, putEmailIdentityFeedbackAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity that you want to configure bounce and complaint feedback forwarding for. | 
 **putEmailIdentityFeedbackAttributesRequest** | [**PutEmailIdentityFeedbackAttributesRequest**](PutEmailIdentityFeedbackAttributesRequest.md)|  | 
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


## putEmailIdentityMailFromAttributes

> Object putEmailIdentityMailFromAttributes(emailIdentity, putEmailIdentityMailFromAttributesRequest, opts)



Used to enable or disable the custom Mail-From domain configuration for an email identity.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The verified email identity that you want to set up the custom MAIL FROM domain for.
let putEmailIdentityMailFromAttributesRequest = new AmazonPinpointEmailService.PutEmailIdentityMailFromAttributesRequest(); // PutEmailIdentityMailFromAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEmailIdentityMailFromAttributes(emailIdentity, putEmailIdentityMailFromAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The verified email identity that you want to set up the custom MAIL FROM domain for. | 
 **putEmailIdentityMailFromAttributesRequest** | [**PutEmailIdentityMailFromAttributesRequest**](PutEmailIdentityMailFromAttributesRequest.md)|  | 
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


## sendEmail

> SendEmailResponse sendEmail(sendEmailRequest, opts)



&lt;p&gt;Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Simple&lt;/b&gt; – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon Pinpoint assembles the message for you.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Raw&lt;/b&gt; – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let sendEmailRequest = new AmazonPinpointEmailService.SendEmailRequest(); // SendEmailRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendEmail(sendEmailRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sendEmailRequest** | [**SendEmailRequest**](SendEmailRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendEmailResponse**](SendEmailResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> Object tagResource(tagResourceRequest, opts)



&lt;p&gt;Add one or more tags (keys and values) to a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.&lt;/p&gt; &lt;p&gt;Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an associated &lt;i&gt;tag value&lt;/i&gt;, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let tagResourceRequest = new AmazonPinpointEmailService.TagResourceRequest(); // TagResourceRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.tagResource(tagResourceRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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



Remove one or more tags (keys and values) from a specified resource.

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.
let tagKeys = ["null"]; // [String] | <p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the resource, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. For example: <code>/v1/email/tags?ResourceArn=ResourceArn&amp;TagKeys=Key1&amp;TagKeys=Key2</code> </p>
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from. | 
 **tagKeys** | [**[String]**](String.md)| &lt;p&gt;The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.&lt;/p&gt; &lt;p&gt;To remove more than one tag from the resource, append the &lt;code&gt;TagKeys&lt;/code&gt; parameter and argument for each additional tag to remove, separated by an ampersand. For example: &lt;code&gt;/v1/email/tags?ResourceArn&#x3D;ResourceArn&amp;amp;TagKeys&#x3D;Key1&amp;amp;TagKeys&#x3D;Key2&lt;/code&gt; &lt;/p&gt; | 
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


## updateConfigurationSetEventDestination

> Object updateConfigurationSetEventDestination(configurationSetName, eventDestinationName, updateConfigurationSetEventDestinationRequest, opts)



&lt;p&gt;Update the configuration of an event destination for a configuration set.&lt;/p&gt; &lt;p&gt;In Amazon Pinpoint, &lt;i&gt;events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

### Example

```javascript
import AmazonPinpointEmailService from 'amazon_pinpoint_email_service';
let defaultClient = AmazonPinpointEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpointEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that contains the event destination that you want to modify.
let eventDestinationName = "eventDestinationName_example"; // String | The name of the event destination that you want to modify.
let updateConfigurationSetEventDestinationRequest = new AmazonPinpointEmailService.UpdateConfigurationSetEventDestinationRequest(); // UpdateConfigurationSetEventDestinationRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set that contains the event destination that you want to modify. | 
 **eventDestinationName** | **String**| The name of the event destination that you want to modify. | 
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

