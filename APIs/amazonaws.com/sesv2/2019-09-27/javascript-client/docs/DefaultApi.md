# AmazonSimpleEmailService.DefaultApi

All URIs are relative to *http://email.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batchGetMetricData**](DefaultApi.md#batchGetMetricData) | **POST** /v2/email/metrics/batch | 
[**createConfigurationSet**](DefaultApi.md#createConfigurationSet) | **POST** /v2/email/configuration-sets | 
[**createConfigurationSetEventDestination**](DefaultApi.md#createConfigurationSetEventDestination) | **POST** /v2/email/configuration-sets/{ConfigurationSetName}/event-destinations | 
[**createContact**](DefaultApi.md#createContact) | **POST** /v2/email/contact-lists/{ContactListName}/contacts | 
[**createContactList**](DefaultApi.md#createContactList) | **POST** /v2/email/contact-lists | 
[**createCustomVerificationEmailTemplate**](DefaultApi.md#createCustomVerificationEmailTemplate) | **POST** /v2/email/custom-verification-email-templates | 
[**createDedicatedIpPool**](DefaultApi.md#createDedicatedIpPool) | **POST** /v2/email/dedicated-ip-pools | 
[**createDeliverabilityTestReport**](DefaultApi.md#createDeliverabilityTestReport) | **POST** /v2/email/deliverability-dashboard/test | 
[**createEmailIdentity**](DefaultApi.md#createEmailIdentity) | **POST** /v2/email/identities | 
[**createEmailIdentityPolicy**](DefaultApi.md#createEmailIdentityPolicy) | **POST** /v2/email/identities/{EmailIdentity}/policies/{PolicyName} | 
[**createEmailTemplate**](DefaultApi.md#createEmailTemplate) | **POST** /v2/email/templates | 
[**createImportJob**](DefaultApi.md#createImportJob) | **POST** /v2/email/import-jobs | 
[**deleteConfigurationSet**](DefaultApi.md#deleteConfigurationSet) | **DELETE** /v2/email/configuration-sets/{ConfigurationSetName} | 
[**deleteConfigurationSetEventDestination**](DefaultApi.md#deleteConfigurationSetEventDestination) | **DELETE** /v2/email/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName} | 
[**deleteContact**](DefaultApi.md#deleteContact) | **DELETE** /v2/email/contact-lists/{ContactListName}/contacts/{EmailAddress} | 
[**deleteContactList**](DefaultApi.md#deleteContactList) | **DELETE** /v2/email/contact-lists/{ContactListName} | 
[**deleteCustomVerificationEmailTemplate**](DefaultApi.md#deleteCustomVerificationEmailTemplate) | **DELETE** /v2/email/custom-verification-email-templates/{TemplateName} | 
[**deleteDedicatedIpPool**](DefaultApi.md#deleteDedicatedIpPool) | **DELETE** /v2/email/dedicated-ip-pools/{PoolName} | 
[**deleteEmailIdentity**](DefaultApi.md#deleteEmailIdentity) | **DELETE** /v2/email/identities/{EmailIdentity} | 
[**deleteEmailIdentityPolicy**](DefaultApi.md#deleteEmailIdentityPolicy) | **DELETE** /v2/email/identities/{EmailIdentity}/policies/{PolicyName} | 
[**deleteEmailTemplate**](DefaultApi.md#deleteEmailTemplate) | **DELETE** /v2/email/templates/{TemplateName} | 
[**deleteSuppressedDestination**](DefaultApi.md#deleteSuppressedDestination) | **DELETE** /v2/email/suppression/addresses/{EmailAddress} | 
[**getAccount**](DefaultApi.md#getAccount) | **GET** /v2/email/account | 
[**getBlacklistReports**](DefaultApi.md#getBlacklistReports) | **GET** /v2/email/deliverability-dashboard/blacklist-report#BlacklistItemNames | 
[**getConfigurationSet**](DefaultApi.md#getConfigurationSet) | **GET** /v2/email/configuration-sets/{ConfigurationSetName} | 
[**getConfigurationSetEventDestinations**](DefaultApi.md#getConfigurationSetEventDestinations) | **GET** /v2/email/configuration-sets/{ConfigurationSetName}/event-destinations | 
[**getContact**](DefaultApi.md#getContact) | **GET** /v2/email/contact-lists/{ContactListName}/contacts/{EmailAddress} | 
[**getContactList**](DefaultApi.md#getContactList) | **GET** /v2/email/contact-lists/{ContactListName} | 
[**getCustomVerificationEmailTemplate**](DefaultApi.md#getCustomVerificationEmailTemplate) | **GET** /v2/email/custom-verification-email-templates/{TemplateName} | 
[**getDedicatedIp**](DefaultApi.md#getDedicatedIp) | **GET** /v2/email/dedicated-ips/{IP} | 
[**getDedicatedIpPool**](DefaultApi.md#getDedicatedIpPool) | **GET** /v2/email/dedicated-ip-pools/{PoolName} | 
[**getDedicatedIps**](DefaultApi.md#getDedicatedIps) | **GET** /v2/email/dedicated-ips | 
[**getDeliverabilityDashboardOptions**](DefaultApi.md#getDeliverabilityDashboardOptions) | **GET** /v2/email/deliverability-dashboard | 
[**getDeliverabilityTestReport**](DefaultApi.md#getDeliverabilityTestReport) | **GET** /v2/email/deliverability-dashboard/test-reports/{ReportId} | 
[**getDomainDeliverabilityCampaign**](DefaultApi.md#getDomainDeliverabilityCampaign) | **GET** /v2/email/deliverability-dashboard/campaigns/{CampaignId} | 
[**getDomainStatisticsReport**](DefaultApi.md#getDomainStatisticsReport) | **GET** /v2/email/deliverability-dashboard/statistics-report/{Domain}#StartDate&amp;EndDate | 
[**getEmailIdentity**](DefaultApi.md#getEmailIdentity) | **GET** /v2/email/identities/{EmailIdentity} | 
[**getEmailIdentityPolicies**](DefaultApi.md#getEmailIdentityPolicies) | **GET** /v2/email/identities/{EmailIdentity}/policies | 
[**getEmailTemplate**](DefaultApi.md#getEmailTemplate) | **GET** /v2/email/templates/{TemplateName} | 
[**getImportJob**](DefaultApi.md#getImportJob) | **GET** /v2/email/import-jobs/{JobId} | 
[**getSuppressedDestination**](DefaultApi.md#getSuppressedDestination) | **GET** /v2/email/suppression/addresses/{EmailAddress} | 
[**listConfigurationSets**](DefaultApi.md#listConfigurationSets) | **GET** /v2/email/configuration-sets | 
[**listContactLists**](DefaultApi.md#listContactLists) | **GET** /v2/email/contact-lists | 
[**listContacts**](DefaultApi.md#listContacts) | **GET** /v2/email/contact-lists/{ContactListName}/contacts | 
[**listCustomVerificationEmailTemplates**](DefaultApi.md#listCustomVerificationEmailTemplates) | **GET** /v2/email/custom-verification-email-templates | 
[**listDedicatedIpPools**](DefaultApi.md#listDedicatedIpPools) | **GET** /v2/email/dedicated-ip-pools | 
[**listDeliverabilityTestReports**](DefaultApi.md#listDeliverabilityTestReports) | **GET** /v2/email/deliverability-dashboard/test-reports | 
[**listDomainDeliverabilityCampaigns**](DefaultApi.md#listDomainDeliverabilityCampaigns) | **GET** /v2/email/deliverability-dashboard/domains/{SubscribedDomain}/campaigns#StartDate&amp;EndDate | 
[**listEmailIdentities**](DefaultApi.md#listEmailIdentities) | **GET** /v2/email/identities | 
[**listEmailTemplates**](DefaultApi.md#listEmailTemplates) | **GET** /v2/email/templates | 
[**listImportJobs**](DefaultApi.md#listImportJobs) | **GET** /v2/email/import-jobs | 
[**listRecommendations**](DefaultApi.md#listRecommendations) | **POST** /v2/email/vdm/recommendations | 
[**listSuppressedDestinations**](DefaultApi.md#listSuppressedDestinations) | **GET** /v2/email/suppression/addresses | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /v2/email/tags#ResourceArn | 
[**putAccountDedicatedIpWarmupAttributes**](DefaultApi.md#putAccountDedicatedIpWarmupAttributes) | **PUT** /v2/email/account/dedicated-ips/warmup | 
[**putAccountDetails**](DefaultApi.md#putAccountDetails) | **POST** /v2/email/account/details | 
[**putAccountSendingAttributes**](DefaultApi.md#putAccountSendingAttributes) | **PUT** /v2/email/account/sending | 
[**putAccountSuppressionAttributes**](DefaultApi.md#putAccountSuppressionAttributes) | **PUT** /v2/email/account/suppression | 
[**putAccountVdmAttributes**](DefaultApi.md#putAccountVdmAttributes) | **PUT** /v2/email/account/vdm | 
[**putConfigurationSetDeliveryOptions**](DefaultApi.md#putConfigurationSetDeliveryOptions) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/delivery-options | 
[**putConfigurationSetReputationOptions**](DefaultApi.md#putConfigurationSetReputationOptions) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/reputation-options | 
[**putConfigurationSetSendingOptions**](DefaultApi.md#putConfigurationSetSendingOptions) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/sending | 
[**putConfigurationSetSuppressionOptions**](DefaultApi.md#putConfigurationSetSuppressionOptions) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/suppression-options | 
[**putConfigurationSetTrackingOptions**](DefaultApi.md#putConfigurationSetTrackingOptions) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/tracking-options | 
[**putConfigurationSetVdmOptions**](DefaultApi.md#putConfigurationSetVdmOptions) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/vdm-options | 
[**putDedicatedIpInPool**](DefaultApi.md#putDedicatedIpInPool) | **PUT** /v2/email/dedicated-ips/{IP}/pool | 
[**putDedicatedIpPoolScalingAttributes**](DefaultApi.md#putDedicatedIpPoolScalingAttributes) | **PUT** /v2/email/dedicated-ip-pools/{PoolName}/scaling | 
[**putDedicatedIpWarmupAttributes**](DefaultApi.md#putDedicatedIpWarmupAttributes) | **PUT** /v2/email/dedicated-ips/{IP}/warmup | 
[**putDeliverabilityDashboardOption**](DefaultApi.md#putDeliverabilityDashboardOption) | **PUT** /v2/email/deliverability-dashboard | 
[**putEmailIdentityConfigurationSetAttributes**](DefaultApi.md#putEmailIdentityConfigurationSetAttributes) | **PUT** /v2/email/identities/{EmailIdentity}/configuration-set | 
[**putEmailIdentityDkimAttributes**](DefaultApi.md#putEmailIdentityDkimAttributes) | **PUT** /v2/email/identities/{EmailIdentity}/dkim | 
[**putEmailIdentityDkimSigningAttributes**](DefaultApi.md#putEmailIdentityDkimSigningAttributes) | **PUT** /v1/email/identities/{EmailIdentity}/dkim/signing | 
[**putEmailIdentityFeedbackAttributes**](DefaultApi.md#putEmailIdentityFeedbackAttributes) | **PUT** /v2/email/identities/{EmailIdentity}/feedback | 
[**putEmailIdentityMailFromAttributes**](DefaultApi.md#putEmailIdentityMailFromAttributes) | **PUT** /v2/email/identities/{EmailIdentity}/mail-from | 
[**putSuppressedDestination**](DefaultApi.md#putSuppressedDestination) | **PUT** /v2/email/suppression/addresses | 
[**sendBulkEmail**](DefaultApi.md#sendBulkEmail) | **POST** /v2/email/outbound-bulk-emails | 
[**sendCustomVerificationEmail**](DefaultApi.md#sendCustomVerificationEmail) | **POST** /v2/email/outbound-custom-verification-emails | 
[**sendEmail**](DefaultApi.md#sendEmail) | **POST** /v2/email/outbound-emails | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /v2/email/tags | 
[**testRenderEmailTemplate**](DefaultApi.md#testRenderEmailTemplate) | **POST** /v2/email/templates/{TemplateName}/render | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /v2/email/tags#ResourceArn&amp;TagKeys | 
[**updateConfigurationSetEventDestination**](DefaultApi.md#updateConfigurationSetEventDestination) | **PUT** /v2/email/configuration-sets/{ConfigurationSetName}/event-destinations/{EventDestinationName} | 
[**updateContact**](DefaultApi.md#updateContact) | **PUT** /v2/email/contact-lists/{ContactListName}/contacts/{EmailAddress} | 
[**updateContactList**](DefaultApi.md#updateContactList) | **PUT** /v2/email/contact-lists/{ContactListName} | 
[**updateCustomVerificationEmailTemplate**](DefaultApi.md#updateCustomVerificationEmailTemplate) | **PUT** /v2/email/custom-verification-email-templates/{TemplateName} | 
[**updateEmailIdentityPolicy**](DefaultApi.md#updateEmailIdentityPolicy) | **PUT** /v2/email/identities/{EmailIdentity}/policies/{PolicyName} | 
[**updateEmailTemplate**](DefaultApi.md#updateEmailTemplate) | **PUT** /v2/email/templates/{TemplateName} | 



## batchGetMetricData

> BatchGetMetricDataResponse batchGetMetricData(batchGetMetricDataRequest, opts)



&lt;p&gt;Retrieves batches of metric data collected based on your sending activity.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than 16 times per second, and with at most 160 queries from the batches per second (cumulative).&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let batchGetMetricDataRequest = new AmazonSimpleEmailService.BatchGetMetricDataRequest(); // BatchGetMetricDataRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.batchGetMetricData(batchGetMetricDataRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batchGetMetricDataRequest** | [**BatchGetMetricDataRequest**](BatchGetMetricDataRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**BatchGetMetricDataResponse**](BatchGetMetricDataResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createConfigurationSet

> Object createConfigurationSet(createConfigurationSetRequest, opts)



Create a configuration set. &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails that you send. You apply a configuration set to an email by specifying the name of the configuration set when you call the Amazon SES API v2. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email. 

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createConfigurationSetRequest = new AmazonSimpleEmailService.CreateConfigurationSetRequest(); // CreateConfigurationSetRequest | 
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



&lt;p&gt;Create an event destination. &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt; &lt;p&gt;A single configuration set can include more than one event destination.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set .
let createConfigurationSetEventDestinationRequest = new AmazonSimpleEmailService.CreateConfigurationSetEventDestinationRequest(); // CreateConfigurationSetEventDestinationRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set . | 
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


## createContact

> Object createContact(contactListName, createContactRequest, opts)



Creates a contact, which is an end-user who is receiving the email, and adds them to a contact list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list to which the contact should be added.
let createContactRequest = new AmazonSimpleEmailService.CreateContactRequest(); // CreateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContact(contactListName, createContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list to which the contact should be added. | 
 **createContactRequest** | [**CreateContactRequest**](CreateContactRequest.md)|  | 
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


## createContactList

> Object createContactList(createContactListRequest, opts)



Creates a contact list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createContactListRequest = new AmazonSimpleEmailService.CreateContactListRequest(); // CreateContactListRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createContactList(createContactListRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createContactListRequest** | [**CreateContactListRequest**](CreateContactListRequest.md)|  | 
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


## createCustomVerificationEmailTemplate

> Object createCustomVerificationEmailTemplate(createCustomVerificationEmailTemplateRequest, opts)



&lt;p&gt;Creates a new custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createCustomVerificationEmailTemplateRequest = new AmazonSimpleEmailService.CreateCustomVerificationEmailTemplateRequest(); // CreateCustomVerificationEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCustomVerificationEmailTemplate(createCustomVerificationEmailTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createCustomVerificationEmailTemplateRequest** | [**CreateCustomVerificationEmailTemplateRequest**](CreateCustomVerificationEmailTemplateRequest.md)|  | 
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



Create a new pool of dedicated IP addresses. A pool can include one or more dedicated IP addresses that are associated with your Amazon Web Services account. You can associate a pool with a configuration set. When you send an email that uses that configuration set, the message is sent from one of the addresses in the associated pool.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createDedicatedIpPoolRequest = new AmazonSimpleEmailService.CreateDedicatedIpPoolRequest(); // CreateDedicatedIpPoolRequest | 
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



Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon SES then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the &lt;code&gt;GetDeliverabilityTestReport&lt;/code&gt; operation to view the results of the test.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createDeliverabilityTestReportRequest = new AmazonSimpleEmailService.CreateDeliverabilityTestReportRequest(); // CreateDeliverabilityTestReportRequest | 
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



&lt;p&gt;Starts the process of verifying an email identity. An &lt;i&gt;identity&lt;/i&gt; is an email address or domain that you use when you send email. Before you can use an identity to send email, you first have to verify it. By verifying an identity, you demonstrate that you&#39;re the owner of the identity, and that you&#39;ve given Amazon SES API v2 permission to send email from the identity.&lt;/p&gt; &lt;p&gt;When you verify an email address, Amazon SES sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. &lt;/p&gt; &lt;p&gt;When you verify a domain without specifying the &lt;code&gt;DkimSigningAttributes&lt;/code&gt; object, this operation provides a set of DKIM tokens. You can convert these tokens into CNAME records, which you then add to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. This verification method is known as &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/easy-dkim.html\&quot;&gt;Easy DKIM&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;Alternatively, you can perform the verification process by providing your own public-private key pair. This verification method is known as Bring Your Own DKIM (BYODKIM). To use BYODKIM, your call to the &lt;code&gt;CreateEmailIdentity&lt;/code&gt; operation has to include the &lt;code&gt;DkimSigningAttributes&lt;/code&gt; object. When you specify this object, you provide a selector (a component of the DNS record name that identifies the public key to use for DKIM authentication) and a private key.&lt;/p&gt; &lt;p&gt;When you verify a domain, this operation provides a set of DKIM tokens, which you can convert into CNAME tokens. You add these CNAME tokens to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. For some DNS providers, it can take 72 hours or more to complete the domain verification process.&lt;/p&gt; &lt;p&gt;Additionally, you can associate an existing configuration set with the email identity that you&#39;re verifying.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createEmailIdentityRequest = new AmazonSimpleEmailService.CreateEmailIdentityRequest(); // CreateEmailIdentityRequest | 
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


## createEmailIdentityPolicy

> Object createEmailIdentityPolicy(emailIdentity, policyName, updateEmailIdentityPolicyRequest, opts)



&lt;p&gt;Creates the specified sending authorization policy for the given identity (an email address or a domain).&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let policyName = "policyName_example"; // String | <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>
let updateEmailIdentityPolicyRequest = new AmazonSimpleEmailService.UpdateEmailIdentityPolicyRequest(); // UpdateEmailIdentityPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEmailIdentityPolicy(emailIdentity, policyName, updateEmailIdentityPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity. | 
 **policyName** | **String**| &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt; | 
 **updateEmailIdentityPolicyRequest** | [**UpdateEmailIdentityPolicyRequest**](UpdateEmailIdentityPolicyRequest.md)|  | 
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


## createEmailTemplate

> Object createEmailTemplate(createEmailTemplateRequest, opts)



&lt;p&gt;Creates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createEmailTemplateRequest = new AmazonSimpleEmailService.CreateEmailTemplateRequest(); // CreateEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEmailTemplate(createEmailTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createEmailTemplateRequest** | [**CreateEmailTemplateRequest**](CreateEmailTemplateRequest.md)|  | 
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


## createImportJob

> CreateImportJobResponse createImportJob(createImportJobRequest, opts)



Creates an import job for a data destination.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let createImportJobRequest = new AmazonSimpleEmailService.CreateImportJobRequest(); // CreateImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createImportJob(createImportJobRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createImportJobRequest** | [**CreateImportJobRequest**](CreateImportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateImportJobResponse**](CreateImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteConfigurationSet

> Object deleteConfigurationSet(configurationSetName, opts)



&lt;p&gt;Delete an existing configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set.
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
 **configurationSetName** | **String**| The name of the configuration set. | 
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



&lt;p&gt;Delete an event destination.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that contains the event destination to delete.
let eventDestinationName = "eventDestinationName_example"; // String | The name of the event destination to delete.
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
 **configurationSetName** | **String**| The name of the configuration set that contains the event destination to delete. | 
 **eventDestinationName** | **String**| The name of the event destination to delete. | 
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


## deleteContact

> Object deleteContact(contactListName, emailAddress, opts)



Removes a contact from a contact list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list from which the contact should be removed.
let emailAddress = "emailAddress_example"; // String | The contact's email address.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContact(contactListName, emailAddress, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list from which the contact should be removed. | 
 **emailAddress** | **String**| The contact&#39;s email address. | 
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


## deleteContactList

> Object deleteContactList(contactListName, opts)



Deletes a contact list and all of the contacts on that list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteContactList(contactListName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list. | 
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


## deleteCustomVerificationEmailTemplate

> Object deleteCustomVerificationEmailTemplate(templateName, opts)



&lt;p&gt;Deletes an existing custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the custom verification email template that you want to delete.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCustomVerificationEmailTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the custom verification email template that you want to delete. | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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



Deletes an email identity. An identity can be either an email address or a domain name.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The identity (that is, the email address or domain) to delete.
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
 **emailIdentity** | **String**| The identity (that is, the email address or domain) to delete. | 
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


## deleteEmailIdentityPolicy

> Object deleteEmailIdentityPolicy(emailIdentity, policyName, opts)



&lt;p&gt;Deletes the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let policyName = "policyName_example"; // String | <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEmailIdentityPolicy(emailIdentity, policyName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity. | 
 **policyName** | **String**| &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt; | 
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


## deleteEmailTemplate

> Object deleteEmailTemplate(templateName, opts)



&lt;p&gt;Deletes an email template.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the template to be deleted.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEmailTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the template to be deleted. | 
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


## deleteSuppressedDestination

> Object deleteSuppressedDestination(emailAddress, opts)



Removes an email address from the suppression list for your account.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailAddress = "emailAddress_example"; // String | The suppressed email destination to remove from the account suppression list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSuppressedDestination(emailAddress, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailAddress** | **String**| The suppressed email destination to remove from the account suppression list. | 
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



Obtain information about the email-sending status and capabilities of your Amazon SES account in the current Amazon Web Services Region.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let blacklistItemNames = ["null"]; // [String] | A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon SES or Amazon Pinpoint.
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
 **blacklistItemNames** | [**[String]**](String.md)| A list of IP addresses that you want to retrieve blacklist information about. You can only specify the dedicated IP addresses that you use to send email using Amazon SES or Amazon Pinpoint. | 
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



&lt;p&gt;Get information about an existing configuration set, including the dedicated IP pool that it&#39;s associated with, whether or not it&#39;s enabled for sending email, and more.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set.
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
 **configurationSetName** | **String**| The name of the configuration set. | 
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



&lt;p&gt;Retrieve a list of event destinations that are associated with a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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


## getContact

> GetContactResponse getContact(contactListName, emailAddress, opts)



Returns a contact from a contact list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list to which the contact belongs.
let emailAddress = "emailAddress_example"; // String | The contact's email address.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContact(contactListName, emailAddress, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list to which the contact belongs. | 
 **emailAddress** | **String**| The contact&#39;s email address. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactResponse**](GetContactResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getContactList

> GetContactListResponse getContactList(contactListName, opts)



Returns contact list metadata. It does not return any information about the contacts present in the list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getContactList(contactListName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetContactListResponse**](GetContactListResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCustomVerificationEmailTemplate

> GetCustomVerificationEmailTemplateResponse getCustomVerificationEmailTemplate(templateName, opts)



&lt;p&gt;Returns the custom email verification template for the template name you specify.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the custom verification email template that you want to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCustomVerificationEmailTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the custom verification email template that you want to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCustomVerificationEmailTemplateResponse**](GetCustomVerificationEmailTemplateResponse.md)

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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let IP = "IP_example"; // String | The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that's assocaited with your Amazon Web Services account.
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
 **IP** | **String**| The IP address that you want to obtain more information about. The value you specify has to be a dedicated IP address that&#39;s assocaited with your Amazon Web Services account. | 
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


## getDedicatedIpPool

> GetDedicatedIpPoolResponse getDedicatedIpPool(poolName, opts)



Retrieve information about the dedicated pool.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let poolName = "poolName_example"; // String | The name of the dedicated IP pool to retrieve.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getDedicatedIpPool(poolName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolName** | **String**| The name of the dedicated IP pool to retrieve. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetDedicatedIpPoolResponse**](GetDedicatedIpPoolResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getDedicatedIps

> GetDedicatedIpsResponse getDedicatedIps(opts)



List the dedicated IP addresses that are associated with your Amazon Web Services account.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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



&lt;p&gt;Retrieve information about the status of the Deliverability dashboard for your account. When the Deliverability dashboard is enabled, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other Amazon Web Services services. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/ses/pricing/\&quot;&gt;Amazon SES Pricing&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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



Retrieve all the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.
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
 **campaignId** | **String**| The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign. | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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



Provides information about a specific identity, including the identity&#39;s verification status, sending authorization policies, its DKIM authentication status, and its custom Mail-From settings.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
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
 **emailIdentity** | **String**| The email identity. | 
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


## getEmailIdentityPolicies

> GetEmailIdentityPoliciesResponse getEmailIdentityPolicies(emailIdentity, opts)



&lt;p&gt;Returns the requested sending authorization policies for the given identity (an email address or a domain). The policies are returned as a map of policy names to policy contents. You can retrieve a maximum of 20 policies at a time.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEmailIdentityPolicies(emailIdentity, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEmailIdentityPoliciesResponse**](GetEmailIdentityPoliciesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmailTemplate

> GetEmailTemplateResponse getEmailTemplate(templateName, opts)



&lt;p&gt;Displays the template object (which includes the subject line, HTML part and text part) for the template you specify.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the template.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEmailTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the template. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEmailTemplateResponse**](GetEmailTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImportJob

> GetImportJobResponse getImportJob(jobId, opts)



Provides information about an import job.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let jobId = "jobId_example"; // String | The ID of the import job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getImportJob(jobId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **jobId** | **String**| The ID of the import job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetImportJobResponse**](GetImportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSuppressedDestination

> GetSuppressedDestinationResponse getSuppressedDestination(emailAddress, opts)



Retrieves information about a specific email address that&#39;s on the suppression list for your account.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailAddress = "emailAddress_example"; // String | The email address that's on the account suppression list.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSuppressedDestination(emailAddress, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailAddress** | **String**| The email address that&#39;s on the account suppression list. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSuppressedDestinationResponse**](GetSuppressedDestinationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConfigurationSets

> ListConfigurationSetsResponse listConfigurationSets(opts)



&lt;p&gt;List all of the configuration sets associated with your account in the current region.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Configuration sets&lt;/i&gt; are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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


## listContactLists

> ListContactListsResponse listContactLists(opts)



Lists all of the contact lists available.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': 56, // Number | Maximum number of contact lists to return at once. Use this parameter to paginate results. If additional contact lists exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional lists.
  'nextToken': "nextToken_example" // String | A string token indicating that there might be additional contact lists available to be listed. Use the token provided in the Response to use in the subsequent call to ListContactLists with the same parameters to retrieve the next page of contact lists.
};
apiInstance.listContactLists(opts, (error, data, response) => {
  if (error) {
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
 **pageSize** | **Number**| Maximum number of contact lists to return at once. Use this parameter to paginate results. If additional contact lists exist beyond the specified limit, the &lt;code&gt;NextToken&lt;/code&gt; element is sent in the response. Use the &lt;code&gt;NextToken&lt;/code&gt; value in subsequent requests to retrieve additional lists. | [optional] 
 **nextToken** | **String**| A string token indicating that there might be additional contact lists available to be listed. Use the token provided in the Response to use in the subsequent call to ListContactLists with the same parameters to retrieve the next page of contact lists. | [optional] 

### Return type

[**ListContactListsResponse**](ListContactListsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listContacts

> ListContactsResponse listContacts(contactListName, listContactsRequest, opts)



Lists the contacts present in a specific contact list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list.
let listContactsRequest = new AmazonSimpleEmailService.ListContactsRequest(); // ListContactsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': 56, // Number | The number of contacts that may be returned at once, which is dependent on if there are more or less contacts than the value of the PageSize. Use this parameter to paginate results. If additional contacts exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional contacts.
  'nextToken': "nextToken_example" // String | A string token indicating that there might be additional contacts available to be listed. Use the token provided in the Response to use in the subsequent call to ListContacts with the same parameters to retrieve the next page of contacts.
};
apiInstance.listContacts(contactListName, listContactsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list. | 
 **listContactsRequest** | [**ListContactsRequest**](ListContactsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **Number**| The number of contacts that may be returned at once, which is dependent on if there are more or less contacts than the value of the PageSize. Use this parameter to paginate results. If additional contacts exist beyond the specified limit, the &lt;code&gt;NextToken&lt;/code&gt; element is sent in the response. Use the &lt;code&gt;NextToken&lt;/code&gt; value in subsequent requests to retrieve additional contacts. | [optional] 
 **nextToken** | **String**| A string token indicating that there might be additional contacts available to be listed. Use the token provided in the Response to use in the subsequent call to ListContacts with the same parameters to retrieve the next page of contacts. | [optional] 

### Return type

[**ListContactsResponse**](ListContactsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listCustomVerificationEmailTemplates

> ListCustomVerificationEmailTemplatesResponse listCustomVerificationEmailTemplates(opts)



&lt;p&gt;Lists the existing custom verification email templates for your account in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListCustomVerificationEmailTemplates</code> to indicate the position in the list of custom verification email templates.
  'pageSize': 56 // Number | <p>The number of results to show in a single call to <code>ListCustomVerificationEmailTemplates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 50.</p>
};
apiInstance.listCustomVerificationEmailTemplates(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListCustomVerificationEmailTemplates&lt;/code&gt; to indicate the position in the list of custom verification email templates. | [optional] 
 **pageSize** | **Number**| &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListCustomVerificationEmailTemplates&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 1, and can be no more than 50.&lt;/p&gt; | [optional] 

### Return type

[**ListCustomVerificationEmailTemplatesResponse**](ListCustomVerificationEmailTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listDedicatedIpPools

> ListDedicatedIpPoolsResponse listDedicatedIpPools(opts)



List all of the dedicated IP pools that exist in your Amazon Web Services account in the current Region.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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



Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard for the domain.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let startDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The first day that you want to obtain deliverability data for.
let endDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The last day that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the <code>StartDate</code> parameter.
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
 **startDate** | **Date**| The first day that you want to obtain deliverability data for. | 
 **endDate** | **Date**| The last day that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the &lt;code&gt;StartDate&lt;/code&gt; parameter. | 
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



Returns a list of all of the email identities that are associated with your Amazon Web Services account. An identity can be either an email address or a domain. This operation returns identities that are verified as well as those that aren&#39;t. This operation returns identities that are associated with Amazon SES and Amazon Pinpoint.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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


## listEmailTemplates

> ListEmailTemplatesResponse listEmailTemplates(opts)



&lt;p&gt;Lists the email templates present in your Amazon SES account in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListEmailTemplates</code> to indicate the position in the list of email templates.
  'pageSize': 56 // Number | <p>The number of results to show in a single call to <code>ListEmailTemplates</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p> <p>The value you specify has to be at least 1, and can be no more than 10.</p>
};
apiInstance.listEmailTemplates(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListEmailTemplates&lt;/code&gt; to indicate the position in the list of email templates. | [optional] 
 **pageSize** | **Number**| &lt;p&gt;The number of results to show in a single call to &lt;code&gt;ListEmailTemplates&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results.&lt;/p&gt; &lt;p&gt;The value you specify has to be at least 1, and can be no more than 10.&lt;/p&gt; | [optional] 

### Return type

[**ListEmailTemplatesResponse**](ListEmailTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listImportJobs

> ListImportJobsResponse listImportJobs(listImportJobsRequest, opts)



Lists all of the import jobs.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let listImportJobsRequest = new AmazonSimpleEmailService.ListImportJobsRequest(); // ListImportJobsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to <code>ListImportJobs</code> with the same parameters to retrieve the next page of import jobs.
  'pageSize': 56 // Number | Maximum number of import jobs to return at once. Use this parameter to paginate results. If additional import jobs exist beyond the specified limit, the <code>NextToken</code> element is sent in the response. Use the <code>NextToken</code> value in subsequent requests to retrieve additional addresses.
};
apiInstance.listImportJobs(listImportJobsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listImportJobsRequest** | [**ListImportJobsRequest**](ListImportJobsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| A string token indicating that there might be additional import jobs available to be listed. Copy this token to a subsequent call to &lt;code&gt;ListImportJobs&lt;/code&gt; with the same parameters to retrieve the next page of import jobs. | [optional] 
 **pageSize** | **Number**| Maximum number of import jobs to return at once. Use this parameter to paginate results. If additional import jobs exist beyond the specified limit, the &lt;code&gt;NextToken&lt;/code&gt; element is sent in the response. Use the &lt;code&gt;NextToken&lt;/code&gt; value in subsequent requests to retrieve additional addresses. | [optional] 

### Return type

[**ListImportJobsResponse**](ListImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listRecommendations

> ListRecommendationsResponse listRecommendations(listRecommendationsRequest, opts)



&lt;p&gt;Lists the recommendations present in your Amazon SES account in the current Amazon Web Services Region.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let listRecommendationsRequest = new AmazonSimpleEmailService.ListRecommendationsRequest(); // ListRecommendationsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | Pagination limit
  'nextToken': "nextToken_example" // String | Pagination token
};
apiInstance.listRecommendations(listRecommendationsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **listRecommendationsRequest** | [**ListRecommendationsRequest**](ListRecommendationsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| Pagination limit | [optional] 
 **nextToken** | **String**| Pagination token | [optional] 

### Return type

[**ListRecommendationsResponse**](ListRecommendationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## listSuppressedDestinations

> ListSuppressedDestinationsResponse listSuppressedDestinations(opts)



Retrieves a list of email addresses that are on the suppression list for your account.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'reason': [new AmazonSimpleEmailService.SuppressionListReason()], // [SuppressionListReason] | The factors that caused the email address to be added to .
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list after a specific date.
  'endDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list before a specific date.
  'nextToken': "nextToken_example", // String | A token returned from a previous call to <code>ListSuppressedDestinations</code> to indicate the position in the list of suppressed email addresses.
  'pageSize': 56 // Number | The number of results to show in a single call to <code>ListSuppressedDestinations</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.
};
apiInstance.listSuppressedDestinations(opts, (error, data, response) => {
  if (error) {
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
 **reason** | [**[SuppressionListReason]**](SuppressionListReason.md)| The factors that caused the email address to be added to . | [optional] 
 **startDate** | **Date**| Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list after a specific date. | [optional] 
 **endDate** | **Date**| Used to filter the list of suppressed email destinations so that it only includes addresses that were added to the list before a specific date. | [optional] 
 **nextToken** | **String**| A token returned from a previous call to &lt;code&gt;ListSuppressedDestinations&lt;/code&gt; to indicate the position in the list of suppressed email addresses. | [optional] 
 **pageSize** | **Number**| The number of results to show in a single call to &lt;code&gt;ListSuppressedDestinations&lt;/code&gt;. If the number of results is larger than the number you specified in this parameter, then the response includes a &lt;code&gt;NextToken&lt;/code&gt; element, which you can use to obtain additional results. | [optional] 

### Return type

[**ListSuppressedDestinationsResponse**](ListSuppressedDestinationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Retrieve a list of the tags (keys and values) that are associated with a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource. Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an optional associated &lt;i&gt;tag value&lt;/i&gt;. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putAccountDedicatedIpWarmupAttributesRequest = new AmazonSimpleEmailService.PutAccountDedicatedIpWarmupAttributesRequest(); // PutAccountDedicatedIpWarmupAttributesRequest | 
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


## putAccountDetails

> Object putAccountDetails(putAccountDetailsRequest, opts)



Update your Amazon SES account details.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putAccountDetailsRequest = new AmazonSimpleEmailService.PutAccountDetailsRequest(); // PutAccountDetailsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccountDetails(putAccountDetailsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putAccountDetailsRequest** | [**PutAccountDetailsRequest**](PutAccountDetailsRequest.md)|  | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putAccountSendingAttributesRequest = new AmazonSimpleEmailService.PutAccountSendingAttributesRequest(); // PutAccountSendingAttributesRequest | 
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


## putAccountSuppressionAttributes

> Object putAccountSuppressionAttributes(putAccountSuppressionAttributesRequest, opts)



Change the settings for the account-level suppression list.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putAccountSuppressionAttributesRequest = new AmazonSimpleEmailService.PutAccountSuppressionAttributesRequest(); // PutAccountSuppressionAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccountSuppressionAttributes(putAccountSuppressionAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putAccountSuppressionAttributesRequest** | [**PutAccountSuppressionAttributesRequest**](PutAccountSuppressionAttributesRequest.md)|  | 
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


## putAccountVdmAttributes

> Object putAccountVdmAttributes(putAccountVdmAttributesRequest, opts)



&lt;p&gt;Update your Amazon SES account VDM attributes.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putAccountVdmAttributesRequest = new AmazonSimpleEmailService.PutAccountVdmAttributesRequest(); // PutAccountVdmAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putAccountVdmAttributes(putAccountVdmAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putAccountVdmAttributesRequest** | [**PutAccountVdmAttributesRequest**](PutAccountVdmAttributesRequest.md)|  | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set to associate with a dedicated IP pool.
let putConfigurationSetDeliveryOptionsRequest = new AmazonSimpleEmailService.PutConfigurationSetDeliveryOptionsRequest(); // PutConfigurationSetDeliveryOptionsRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set to associate with a dedicated IP pool. | 
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



Enable or disable collection of reputation metrics for emails that you send using a particular configuration set in a specific Amazon Web Services Region.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set.
let putConfigurationSetReputationOptionsRequest = new AmazonSimpleEmailService.PutConfigurationSetReputationOptionsRequest(); // PutConfigurationSetReputationOptionsRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set. | 
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



Enable or disable email sending for messages that use a particular configuration set in a specific Amazon Web Services Region.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set to enable or disable email sending for.
let putConfigurationSetSendingOptionsRequest = new AmazonSimpleEmailService.PutConfigurationSetSendingOptionsRequest(); // PutConfigurationSetSendingOptionsRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set to enable or disable email sending for. | 
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


## putConfigurationSetSuppressionOptions

> Object putConfigurationSetSuppressionOptions(configurationSetName, putConfigurationSetSuppressionOptionsRequest, opts)



Specify the account suppression list preferences for a configuration set.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set to change the suppression list preferences for.
let putConfigurationSetSuppressionOptionsRequest = new AmazonSimpleEmailService.PutConfigurationSetSuppressionOptionsRequest(); // PutConfigurationSetSuppressionOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfigurationSetSuppressionOptions(configurationSetName, putConfigurationSetSuppressionOptionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set to change the suppression list preferences for. | 
 **putConfigurationSetSuppressionOptionsRequest** | [**PutConfigurationSetSuppressionOptionsRequest**](PutConfigurationSetSuppressionOptionsRequest.md)|  | 
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



Specify a custom domain to use for open and click tracking elements in email that you send.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set.
let putConfigurationSetTrackingOptionsRequest = new AmazonSimpleEmailService.PutConfigurationSetTrackingOptionsRequest(); // PutConfigurationSetTrackingOptionsRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set. | 
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


## putConfigurationSetVdmOptions

> Object putConfigurationSetVdmOptions(configurationSetName, putConfigurationSetVdmOptionsRequest, opts)



&lt;p&gt;Specify VDM preferences for email that you send using the configuration set.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set.
let putConfigurationSetVdmOptionsRequest = new AmazonSimpleEmailService.PutConfigurationSetVdmOptionsRequest(); // PutConfigurationSetVdmOptionsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putConfigurationSetVdmOptions(configurationSetName, putConfigurationSetVdmOptionsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **configurationSetName** | **String**| The name of the configuration set. | 
 **putConfigurationSetVdmOptionsRequest** | [**PutConfigurationSetVdmOptionsRequest**](PutConfigurationSetVdmOptionsRequest.md)|  | 
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



&lt;p&gt;Move a dedicated IP address to an existing dedicated IP pool.&lt;/p&gt; &lt;note&gt; &lt;p&gt;The dedicated IP address that you specify must already exist, and must be associated with your Amazon Web Services account. &lt;/p&gt; &lt;p&gt;The dedicated IP pool you specify must already exist. You can create a new pool by using the &lt;code&gt;CreateDedicatedIpPool&lt;/code&gt; operation.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let IP = "IP_example"; // String | The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that's associated with your Amazon Web Services account.
let putDedicatedIpInPoolRequest = new AmazonSimpleEmailService.PutDedicatedIpInPoolRequest(); // PutDedicatedIpInPoolRequest | 
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
 **IP** | **String**| The IP address that you want to move to the dedicated IP pool. The value you specify has to be a dedicated IP address that&#39;s associated with your Amazon Web Services account. | 
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


## putDedicatedIpPoolScalingAttributes

> Object putDedicatedIpPoolScalingAttributes(poolName, putDedicatedIpPoolScalingAttributesRequest, opts)



&lt;p&gt;Used to convert a dedicated IP pool to a different scaling mode.&lt;/p&gt; &lt;note&gt; &lt;p&gt; &lt;code&gt;MANAGED&lt;/code&gt; pools cannot be converted to &lt;code&gt;STANDARD&lt;/code&gt; scaling mode.&lt;/p&gt; &lt;/note&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let poolName = "poolName_example"; // String | The name of the dedicated IP pool.
let putDedicatedIpPoolScalingAttributesRequest = new AmazonSimpleEmailService.PutDedicatedIpPoolScalingAttributesRequest(); // PutDedicatedIpPoolScalingAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putDedicatedIpPoolScalingAttributes(poolName, putDedicatedIpPoolScalingAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **poolName** | **String**| The name of the dedicated IP pool. | 
 **putDedicatedIpPoolScalingAttributesRequest** | [**PutDedicatedIpPoolScalingAttributesRequest**](PutDedicatedIpPoolScalingAttributesRequest.md)|  | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let IP = "IP_example"; // String | The dedicated IP address that you want to update the warm-up attributes for.
let putDedicatedIpWarmupAttributesRequest = new AmazonSimpleEmailService.PutDedicatedIpWarmupAttributesRequest(); // PutDedicatedIpWarmupAttributesRequest | 
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



&lt;p&gt;Enable or disable the Deliverability dashboard. When you enable the Deliverability dashboard, you gain access to reputation, deliverability, and other metrics for the domains that you use to send email. You also gain the ability to perform predictive inbox placement tests.&lt;/p&gt; &lt;p&gt;When you use the Deliverability dashboard, you pay a monthly subscription charge, in addition to any other fees that you accrue by using Amazon SES and other Amazon Web Services services. For more information about the features and cost of a Deliverability dashboard subscription, see &lt;a href&#x3D;\&quot;http://aws.amazon.com/ses/pricing/\&quot;&gt;Amazon SES Pricing&lt;/a&gt;.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putDeliverabilityDashboardOptionRequest = new AmazonSimpleEmailService.PutDeliverabilityDashboardOptionRequest(); // PutDeliverabilityDashboardOptionRequest | 
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


## putEmailIdentityConfigurationSetAttributes

> Object putEmailIdentityConfigurationSetAttributes(emailIdentity, putEmailIdentityConfigurationSetAttributesRequest, opts)



Used to associate a configuration set with an email identity.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email address or domain to associate with a configuration set.
let putEmailIdentityConfigurationSetAttributesRequest = new AmazonSimpleEmailService.PutEmailIdentityConfigurationSetAttributesRequest(); // PutEmailIdentityConfigurationSetAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEmailIdentityConfigurationSetAttributes(emailIdentity, putEmailIdentityConfigurationSetAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email address or domain to associate with a configuration set. | 
 **putEmailIdentityConfigurationSetAttributesRequest** | [**PutEmailIdentityConfigurationSetAttributesRequest**](PutEmailIdentityConfigurationSetAttributesRequest.md)|  | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let putEmailIdentityDkimAttributesRequest = new AmazonSimpleEmailService.PutEmailIdentityDkimAttributesRequest(); // PutEmailIdentityDkimAttributesRequest | 
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
 **emailIdentity** | **String**| The email identity. | 
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


## putEmailIdentityDkimSigningAttributes

> PutEmailIdentityDkimSigningAttributesResponse putEmailIdentityDkimSigningAttributes(emailIdentity, putEmailIdentityDkimSigningAttributesRequest, opts)



&lt;p&gt;Used to configure or change the DKIM authentication settings for an email domain identity. You can use this operation to do any of the following:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Update the signing attributes for an identity that uses Bring Your Own DKIM (BYODKIM).&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Update the key length that should be used for Easy DKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using no DKIM authentication to using Easy DKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using no DKIM authentication to using BYODKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using Easy DKIM to using BYODKIM.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Change from using BYODKIM to using Easy DKIM.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let putEmailIdentityDkimSigningAttributesRequest = new AmazonSimpleEmailService.PutEmailIdentityDkimSigningAttributesRequest(); // PutEmailIdentityDkimSigningAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEmailIdentityDkimSigningAttributes(emailIdentity, putEmailIdentityDkimSigningAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity. | 
 **putEmailIdentityDkimSigningAttributesRequest** | [**PutEmailIdentityDkimSigningAttributesRequest**](PutEmailIdentityDkimSigningAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutEmailIdentityDkimSigningAttributesResponse**](PutEmailIdentityDkimSigningAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putEmailIdentityFeedbackAttributes

> Object putEmailIdentityFeedbackAttributes(emailIdentity, putEmailIdentityFeedbackAttributesRequest, opts)



&lt;p&gt;Used to enable or disable feedback forwarding for an identity. This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.&lt;/p&gt; &lt;p&gt;If the value is &lt;code&gt;true&lt;/code&gt;, you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the &lt;code&gt;Return-Path&lt;/code&gt; header of the original email.&lt;/p&gt; &lt;p&gt;You&#39;re required to have a method of tracking bounces and complaints. If you haven&#39;t set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let putEmailIdentityFeedbackAttributesRequest = new AmazonSimpleEmailService.PutEmailIdentityFeedbackAttributesRequest(); // PutEmailIdentityFeedbackAttributesRequest | 
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
 **emailIdentity** | **String**| The email identity. | 
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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The verified email identity.
let putEmailIdentityMailFromAttributesRequest = new AmazonSimpleEmailService.PutEmailIdentityMailFromAttributesRequest(); // PutEmailIdentityMailFromAttributesRequest | 
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
 **emailIdentity** | **String**| The verified email identity. | 
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


## putSuppressedDestination

> Object putSuppressedDestination(putSuppressedDestinationRequest, opts)



Adds an email address to the suppression list for your account.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let putSuppressedDestinationRequest = new AmazonSimpleEmailService.PutSuppressedDestinationRequest(); // PutSuppressedDestinationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putSuppressedDestination(putSuppressedDestinationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **putSuppressedDestinationRequest** | [**PutSuppressedDestinationRequest**](PutSuppressedDestinationRequest.md)|  | 
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


## sendBulkEmail

> SendBulkEmailResponse sendBulkEmail(sendBulkEmailRequest, opts)



Composes an email message to multiple destinations.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let sendBulkEmailRequest = new AmazonSimpleEmailService.SendBulkEmailRequest(); // SendBulkEmailRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendBulkEmail(sendBulkEmailRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sendBulkEmailRequest** | [**SendBulkEmailRequest**](SendBulkEmailRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendBulkEmailResponse**](SendBulkEmailResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendCustomVerificationEmail

> SendCustomVerificationEmailResponse sendCustomVerificationEmail(sendCustomVerificationEmailRequest, opts)



&lt;p&gt;Adds an email address to the list of identities for your Amazon SES account in the current Amazon Web Services Region and attempts to verify it. As a result of executing this operation, a customized verification email is sent to the specified address.&lt;/p&gt; &lt;p&gt;To use this operation, you must first create a custom verification email template. For more information about creating and using custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let sendCustomVerificationEmailRequest = new AmazonSimpleEmailService.SendCustomVerificationEmailRequest(); // SendCustomVerificationEmailRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendCustomVerificationEmail(sendCustomVerificationEmailRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sendCustomVerificationEmailRequest** | [**SendCustomVerificationEmailRequest**](SendCustomVerificationEmailRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendCustomVerificationEmailResponse**](SendCustomVerificationEmailResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendEmail

> SendEmailResponse sendEmail(sendEmailRequest, opts)



&lt;p&gt;Sends an email message. You can use the Amazon SES API v2 to send the following types of messages:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Simple&lt;/b&gt; – A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon SES assembles the message for you.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Raw&lt;/b&gt; – A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;b&gt;Templated&lt;/b&gt; – A message that contains personalization tags. When you send this type of email, Amazon SES API v2 automatically replaces the tags with values that you specify.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let sendEmailRequest = new AmazonSimpleEmailService.SendEmailRequest(); // SendEmailRequest | 
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



&lt;p&gt;Add one or more tags (keys and values) to a specified resource. A &lt;i&gt;tag&lt;/i&gt; is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.&lt;/p&gt; &lt;p&gt;Each tag consists of a required &lt;i&gt;tag key&lt;/i&gt; and an associated &lt;i&gt;tag value&lt;/i&gt;, both of which you define. A tag key is a general label that acts as a category for more specific tag values. A tag value acts as a descriptor within a tag key.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let tagResourceRequest = new AmazonSimpleEmailService.TagResourceRequest(); // TagResourceRequest | 
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


## testRenderEmailTemplate

> TestRenderEmailTemplateResponse testRenderEmailTemplate(templateName, testRenderEmailTemplateRequest, opts)



&lt;p&gt;Creates a preview of the MIME content of an email when provided with a template and a set of replacement data.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the template.
let testRenderEmailTemplateRequest = new AmazonSimpleEmailService.TestRenderEmailTemplateRequest(); // TestRenderEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.testRenderEmailTemplate(templateName, testRenderEmailTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the template. | 
 **testRenderEmailTemplateRequest** | [**TestRenderEmailTemplateRequest**](TestRenderEmailTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**TestRenderEmailTemplateResponse**](TestRenderEmailTemplateResponse.md)

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
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource that you want to remove one or more tags from.
let tagKeys = ["null"]; // [String] | <p>The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.</p> <p>To remove more than one tag from the resource, append the <code>TagKeys</code> parameter and argument for each additional tag to remove, separated by an ampersand. For example: <code>/v2/email/tags?ResourceArn=ResourceArn&amp;TagKeys=Key1&amp;TagKeys=Key2</code> </p>
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
 **tagKeys** | [**[String]**](String.md)| &lt;p&gt;The tags (tag keys) that you want to remove from the resource. When you specify a tag key, the action removes both that key and its associated tag value.&lt;/p&gt; &lt;p&gt;To remove more than one tag from the resource, append the &lt;code&gt;TagKeys&lt;/code&gt; parameter and argument for each additional tag to remove, separated by an ampersand. For example: &lt;code&gt;/v2/email/tags?ResourceArn&#x3D;ResourceArn&amp;amp;TagKeys&#x3D;Key1&amp;amp;TagKeys&#x3D;Key2&lt;/code&gt; &lt;/p&gt; | 
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



&lt;p&gt;Update the configuration of an event destination for a configuration set.&lt;/p&gt; &lt;p&gt; &lt;i&gt;Events&lt;/i&gt; include message sends, deliveries, opens, clicks, bounces, and complaints. &lt;i&gt;Event destinations&lt;/i&gt; are places that you can send information about these events to. For example, you can send event data to Amazon SNS to receive notifications when you receive bounces or complaints, or you can use Amazon Kinesis Data Firehose to stream data to Amazon S3 for long-term storage.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let configurationSetName = "configurationSetName_example"; // String | The name of the configuration set that contains the event destination to modify.
let eventDestinationName = "eventDestinationName_example"; // String | The name of the event destination.
let updateConfigurationSetEventDestinationRequest = new AmazonSimpleEmailService.UpdateConfigurationSetEventDestinationRequest(); // UpdateConfigurationSetEventDestinationRequest | 
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
 **configurationSetName** | **String**| The name of the configuration set that contains the event destination to modify. | 
 **eventDestinationName** | **String**| The name of the event destination. | 
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


## updateContact

> Object updateContact(contactListName, emailAddress, updateContactRequest, opts)



Updates a contact&#39;s preferences for a list. It is not necessary to specify all existing topic preferences in the TopicPreferences object, just the ones that need updating.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list.
let emailAddress = "emailAddress_example"; // String | The contact's email address.
let updateContactRequest = new AmazonSimpleEmailService.UpdateContactRequest(); // UpdateContactRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContact(contactListName, emailAddress, updateContactRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list. | 
 **emailAddress** | **String**| The contact&#39;s email address. | 
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


## updateContactList

> Object updateContactList(contactListName, updateContactListRequest, opts)



Updates contact list metadata. This operation does a complete replacement.

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let contactListName = "contactListName_example"; // String | The name of the contact list.
let updateContactListRequest = new AmazonSimpleEmailService.UpdateContactListRequest(); // UpdateContactListRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateContactList(contactListName, updateContactListRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contactListName** | **String**| The name of the contact list. | 
 **updateContactListRequest** | [**UpdateContactListRequest**](UpdateContactListRequest.md)|  | 
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


## updateCustomVerificationEmailTemplate

> Object updateCustomVerificationEmailTemplate(templateName, updateCustomVerificationEmailTemplateRequest, opts)



&lt;p&gt;Updates an existing custom verification email template.&lt;/p&gt; &lt;p&gt;For more information about custom verification email templates, see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html#send-email-verify-address-custom\&quot;&gt;Using custom verification email templates&lt;/a&gt; in the &lt;i&gt;Amazon SES Developer Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the custom verification email template that you want to update.
let updateCustomVerificationEmailTemplateRequest = new AmazonSimpleEmailService.UpdateCustomVerificationEmailTemplateRequest(); // UpdateCustomVerificationEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCustomVerificationEmailTemplate(templateName, updateCustomVerificationEmailTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the custom verification email template that you want to update. | 
 **updateCustomVerificationEmailTemplateRequest** | [**UpdateCustomVerificationEmailTemplateRequest**](UpdateCustomVerificationEmailTemplateRequest.md)|  | 
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


## updateEmailIdentityPolicy

> Object updateEmailIdentityPolicy(emailIdentity, policyName, updateEmailIdentityPolicyRequest, opts)



&lt;p&gt;Updates the specified sending authorization policy for the given identity (an email address or a domain). This API returns successfully even if a policy with the specified name does not exist.&lt;/p&gt; &lt;note&gt; &lt;p&gt;This API is for the identity owner only. If you have not verified the identity, this API will return an error.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;Sending authorization is a feature that enables an identity owner to authorize other senders to use its identities. For information about using sending authorization, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let emailIdentity = "emailIdentity_example"; // String | The email identity.
let policyName = "policyName_example"; // String | <p>The name of the policy.</p> <p>The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.</p>
let updateEmailIdentityPolicyRequest = new AmazonSimpleEmailService.UpdateEmailIdentityPolicyRequest(); // UpdateEmailIdentityPolicyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEmailIdentityPolicy(emailIdentity, policyName, updateEmailIdentityPolicyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emailIdentity** | **String**| The email identity. | 
 **policyName** | **String**| &lt;p&gt;The name of the policy.&lt;/p&gt; &lt;p&gt;The policy name cannot exceed 64 characters and can only include alphanumeric characters, dashes, and underscores.&lt;/p&gt; | 
 **updateEmailIdentityPolicyRequest** | [**UpdateEmailIdentityPolicyRequest**](UpdateEmailIdentityPolicyRequest.md)|  | 
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


## updateEmailTemplate

> Object updateEmailTemplate(templateName, updateEmailTemplateRequest, opts)



&lt;p&gt;Updates an email template. Email templates enable you to send personalized email to one or more destinations in a single API operation. For more information, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-personalized-email-api.html\&quot;&gt;Amazon SES Developer Guide&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;You can execute this operation no more than once per second.&lt;/p&gt;

### Example

```javascript
import AmazonSimpleEmailService from 'amazon_simple_email_service';
let defaultClient = AmazonSimpleEmailService.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonSimpleEmailService.DefaultApi();
let templateName = "templateName_example"; // String | The name of the template.
let updateEmailTemplateRequest = new AmazonSimpleEmailService.UpdateEmailTemplateRequest(); // UpdateEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEmailTemplate(templateName, updateEmailTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the template. | 
 **updateEmailTemplateRequest** | [**UpdateEmailTemplateRequest**](UpdateEmailTemplateRequest.md)|  | 
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

