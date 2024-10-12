# AmazonPinpoint.DefaultApi

All URIs are relative to *http://pinpoint.us-east-1.amazonaws.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createApp**](DefaultApi.md#createApp) | **POST** /v1/apps | 
[**createCampaign**](DefaultApi.md#createCampaign) | **POST** /v1/apps/{application-id}/campaigns | 
[**createEmailTemplate**](DefaultApi.md#createEmailTemplate) | **POST** /v1/templates/{template-name}/email | 
[**createExportJob**](DefaultApi.md#createExportJob) | **POST** /v1/apps/{application-id}/jobs/export | 
[**createImportJob**](DefaultApi.md#createImportJob) | **POST** /v1/apps/{application-id}/jobs/import | 
[**createInAppTemplate**](DefaultApi.md#createInAppTemplate) | **POST** /v1/templates/{template-name}/inapp | 
[**createJourney**](DefaultApi.md#createJourney) | **POST** /v1/apps/{application-id}/journeys | 
[**createPushTemplate**](DefaultApi.md#createPushTemplate) | **POST** /v1/templates/{template-name}/push | 
[**createRecommenderConfiguration**](DefaultApi.md#createRecommenderConfiguration) | **POST** /v1/recommenders | 
[**createSegment**](DefaultApi.md#createSegment) | **POST** /v1/apps/{application-id}/segments | 
[**createSmsTemplate**](DefaultApi.md#createSmsTemplate) | **POST** /v1/templates/{template-name}/sms | 
[**createVoiceTemplate**](DefaultApi.md#createVoiceTemplate) | **POST** /v1/templates/{template-name}/voice | 
[**deleteAdmChannel**](DefaultApi.md#deleteAdmChannel) | **DELETE** /v1/apps/{application-id}/channels/adm | 
[**deleteApnsChannel**](DefaultApi.md#deleteApnsChannel) | **DELETE** /v1/apps/{application-id}/channels/apns | 
[**deleteApnsSandboxChannel**](DefaultApi.md#deleteApnsSandboxChannel) | **DELETE** /v1/apps/{application-id}/channels/apns_sandbox | 
[**deleteApnsVoipChannel**](DefaultApi.md#deleteApnsVoipChannel) | **DELETE** /v1/apps/{application-id}/channels/apns_voip | 
[**deleteApnsVoipSandboxChannel**](DefaultApi.md#deleteApnsVoipSandboxChannel) | **DELETE** /v1/apps/{application-id}/channels/apns_voip_sandbox | 
[**deleteApp**](DefaultApi.md#deleteApp) | **DELETE** /v1/apps/{application-id} | 
[**deleteBaiduChannel**](DefaultApi.md#deleteBaiduChannel) | **DELETE** /v1/apps/{application-id}/channels/baidu | 
[**deleteCampaign**](DefaultApi.md#deleteCampaign) | **DELETE** /v1/apps/{application-id}/campaigns/{campaign-id} | 
[**deleteEmailChannel**](DefaultApi.md#deleteEmailChannel) | **DELETE** /v1/apps/{application-id}/channels/email | 
[**deleteEmailTemplate**](DefaultApi.md#deleteEmailTemplate) | **DELETE** /v1/templates/{template-name}/email | 
[**deleteEndpoint**](DefaultApi.md#deleteEndpoint) | **DELETE** /v1/apps/{application-id}/endpoints/{endpoint-id} | 
[**deleteEventStream**](DefaultApi.md#deleteEventStream) | **DELETE** /v1/apps/{application-id}/eventstream | 
[**deleteGcmChannel**](DefaultApi.md#deleteGcmChannel) | **DELETE** /v1/apps/{application-id}/channels/gcm | 
[**deleteInAppTemplate**](DefaultApi.md#deleteInAppTemplate) | **DELETE** /v1/templates/{template-name}/inapp | 
[**deleteJourney**](DefaultApi.md#deleteJourney) | **DELETE** /v1/apps/{application-id}/journeys/{journey-id} | 
[**deletePushTemplate**](DefaultApi.md#deletePushTemplate) | **DELETE** /v1/templates/{template-name}/push | 
[**deleteRecommenderConfiguration**](DefaultApi.md#deleteRecommenderConfiguration) | **DELETE** /v1/recommenders/{recommender-id} | 
[**deleteSegment**](DefaultApi.md#deleteSegment) | **DELETE** /v1/apps/{application-id}/segments/{segment-id} | 
[**deleteSmsChannel**](DefaultApi.md#deleteSmsChannel) | **DELETE** /v1/apps/{application-id}/channels/sms | 
[**deleteSmsTemplate**](DefaultApi.md#deleteSmsTemplate) | **DELETE** /v1/templates/{template-name}/sms | 
[**deleteUserEndpoints**](DefaultApi.md#deleteUserEndpoints) | **DELETE** /v1/apps/{application-id}/users/{user-id} | 
[**deleteVoiceChannel**](DefaultApi.md#deleteVoiceChannel) | **DELETE** /v1/apps/{application-id}/channels/voice | 
[**deleteVoiceTemplate**](DefaultApi.md#deleteVoiceTemplate) | **DELETE** /v1/templates/{template-name}/voice | 
[**getAdmChannel**](DefaultApi.md#getAdmChannel) | **GET** /v1/apps/{application-id}/channels/adm | 
[**getApnsChannel**](DefaultApi.md#getApnsChannel) | **GET** /v1/apps/{application-id}/channels/apns | 
[**getApnsSandboxChannel**](DefaultApi.md#getApnsSandboxChannel) | **GET** /v1/apps/{application-id}/channels/apns_sandbox | 
[**getApnsVoipChannel**](DefaultApi.md#getApnsVoipChannel) | **GET** /v1/apps/{application-id}/channels/apns_voip | 
[**getApnsVoipSandboxChannel**](DefaultApi.md#getApnsVoipSandboxChannel) | **GET** /v1/apps/{application-id}/channels/apns_voip_sandbox | 
[**getApp**](DefaultApi.md#getApp) | **GET** /v1/apps/{application-id} | 
[**getApplicationDateRangeKpi**](DefaultApi.md#getApplicationDateRangeKpi) | **GET** /v1/apps/{application-id}/kpis/daterange/{kpi-name} | 
[**getApplicationSettings**](DefaultApi.md#getApplicationSettings) | **GET** /v1/apps/{application-id}/settings | 
[**getApps**](DefaultApi.md#getApps) | **GET** /v1/apps | 
[**getBaiduChannel**](DefaultApi.md#getBaiduChannel) | **GET** /v1/apps/{application-id}/channels/baidu | 
[**getCampaign**](DefaultApi.md#getCampaign) | **GET** /v1/apps/{application-id}/campaigns/{campaign-id} | 
[**getCampaignActivities**](DefaultApi.md#getCampaignActivities) | **GET** /v1/apps/{application-id}/campaigns/{campaign-id}/activities | 
[**getCampaignDateRangeKpi**](DefaultApi.md#getCampaignDateRangeKpi) | **GET** /v1/apps/{application-id}/campaigns/{campaign-id}/kpis/daterange/{kpi-name} | 
[**getCampaignVersion**](DefaultApi.md#getCampaignVersion) | **GET** /v1/apps/{application-id}/campaigns/{campaign-id}/versions/{version} | 
[**getCampaignVersions**](DefaultApi.md#getCampaignVersions) | **GET** /v1/apps/{application-id}/campaigns/{campaign-id}/versions | 
[**getCampaigns**](DefaultApi.md#getCampaigns) | **GET** /v1/apps/{application-id}/campaigns | 
[**getChannels**](DefaultApi.md#getChannels) | **GET** /v1/apps/{application-id}/channels | 
[**getEmailChannel**](DefaultApi.md#getEmailChannel) | **GET** /v1/apps/{application-id}/channels/email | 
[**getEmailTemplate**](DefaultApi.md#getEmailTemplate) | **GET** /v1/templates/{template-name}/email | 
[**getEndpoint**](DefaultApi.md#getEndpoint) | **GET** /v1/apps/{application-id}/endpoints/{endpoint-id} | 
[**getEventStream**](DefaultApi.md#getEventStream) | **GET** /v1/apps/{application-id}/eventstream | 
[**getExportJob**](DefaultApi.md#getExportJob) | **GET** /v1/apps/{application-id}/jobs/export/{job-id} | 
[**getExportJobs**](DefaultApi.md#getExportJobs) | **GET** /v1/apps/{application-id}/jobs/export | 
[**getGcmChannel**](DefaultApi.md#getGcmChannel) | **GET** /v1/apps/{application-id}/channels/gcm | 
[**getImportJob**](DefaultApi.md#getImportJob) | **GET** /v1/apps/{application-id}/jobs/import/{job-id} | 
[**getImportJobs**](DefaultApi.md#getImportJobs) | **GET** /v1/apps/{application-id}/jobs/import | 
[**getInAppMessages**](DefaultApi.md#getInAppMessages) | **GET** /v1/apps/{application-id}/endpoints/{endpoint-id}/inappmessages | 
[**getInAppTemplate**](DefaultApi.md#getInAppTemplate) | **GET** /v1/templates/{template-name}/inapp | 
[**getJourney**](DefaultApi.md#getJourney) | **GET** /v1/apps/{application-id}/journeys/{journey-id} | 
[**getJourneyDateRangeKpi**](DefaultApi.md#getJourneyDateRangeKpi) | **GET** /v1/apps/{application-id}/journeys/{journey-id}/kpis/daterange/{kpi-name} | 
[**getJourneyExecutionActivityMetrics**](DefaultApi.md#getJourneyExecutionActivityMetrics) | **GET** /v1/apps/{application-id}/journeys/{journey-id}/activities/{journey-activity-id}/execution-metrics | 
[**getJourneyExecutionMetrics**](DefaultApi.md#getJourneyExecutionMetrics) | **GET** /v1/apps/{application-id}/journeys/{journey-id}/execution-metrics | 
[**getJourneyRunExecutionActivityMetrics**](DefaultApi.md#getJourneyRunExecutionActivityMetrics) | **GET** /v1/apps/{application-id}/journeys/{journey-id}/runs/{run-id}/activities/{journey-activity-id}/execution-metrics | 
[**getJourneyRunExecutionMetrics**](DefaultApi.md#getJourneyRunExecutionMetrics) | **GET** /v1/apps/{application-id}/journeys/{journey-id}/runs/{run-id}/execution-metrics | 
[**getJourneyRuns**](DefaultApi.md#getJourneyRuns) | **GET** /v1/apps/{application-id}/journeys/{journey-id}/runs | 
[**getPushTemplate**](DefaultApi.md#getPushTemplate) | **GET** /v1/templates/{template-name}/push | 
[**getRecommenderConfiguration**](DefaultApi.md#getRecommenderConfiguration) | **GET** /v1/recommenders/{recommender-id} | 
[**getRecommenderConfigurations**](DefaultApi.md#getRecommenderConfigurations) | **GET** /v1/recommenders | 
[**getSegment**](DefaultApi.md#getSegment) | **GET** /v1/apps/{application-id}/segments/{segment-id} | 
[**getSegmentExportJobs**](DefaultApi.md#getSegmentExportJobs) | **GET** /v1/apps/{application-id}/segments/{segment-id}/jobs/export | 
[**getSegmentImportJobs**](DefaultApi.md#getSegmentImportJobs) | **GET** /v1/apps/{application-id}/segments/{segment-id}/jobs/import | 
[**getSegmentVersion**](DefaultApi.md#getSegmentVersion) | **GET** /v1/apps/{application-id}/segments/{segment-id}/versions/{version} | 
[**getSegmentVersions**](DefaultApi.md#getSegmentVersions) | **GET** /v1/apps/{application-id}/segments/{segment-id}/versions | 
[**getSegments**](DefaultApi.md#getSegments) | **GET** /v1/apps/{application-id}/segments | 
[**getSmsChannel**](DefaultApi.md#getSmsChannel) | **GET** /v1/apps/{application-id}/channels/sms | 
[**getSmsTemplate**](DefaultApi.md#getSmsTemplate) | **GET** /v1/templates/{template-name}/sms | 
[**getUserEndpoints**](DefaultApi.md#getUserEndpoints) | **GET** /v1/apps/{application-id}/users/{user-id} | 
[**getVoiceChannel**](DefaultApi.md#getVoiceChannel) | **GET** /v1/apps/{application-id}/channels/voice | 
[**getVoiceTemplate**](DefaultApi.md#getVoiceTemplate) | **GET** /v1/templates/{template-name}/voice | 
[**listJourneys**](DefaultApi.md#listJourneys) | **GET** /v1/apps/{application-id}/journeys | 
[**listTagsForResource**](DefaultApi.md#listTagsForResource) | **GET** /v1/tags/{resource-arn} | 
[**listTemplateVersions**](DefaultApi.md#listTemplateVersions) | **GET** /v1/templates/{template-name}/{template-type}/versions | 
[**listTemplates**](DefaultApi.md#listTemplates) | **GET** /v1/templates | 
[**phoneNumberValidate**](DefaultApi.md#phoneNumberValidate) | **POST** /v1/phone/number/validate | 
[**putEventStream**](DefaultApi.md#putEventStream) | **POST** /v1/apps/{application-id}/eventstream | 
[**putEvents**](DefaultApi.md#putEvents) | **POST** /v1/apps/{application-id}/events | 
[**removeAttributes**](DefaultApi.md#removeAttributes) | **PUT** /v1/apps/{application-id}/attributes/{attribute-type} | 
[**sendMessages**](DefaultApi.md#sendMessages) | **POST** /v1/apps/{application-id}/messages | 
[**sendOTPMessage**](DefaultApi.md#sendOTPMessage) | **POST** /v1/apps/{application-id}/otp | 
[**sendUsersMessages**](DefaultApi.md#sendUsersMessages) | **POST** /v1/apps/{application-id}/users-messages | 
[**tagResource**](DefaultApi.md#tagResource) | **POST** /v1/tags/{resource-arn} | 
[**untagResource**](DefaultApi.md#untagResource) | **DELETE** /v1/tags/{resource-arn}#tagKeys | 
[**updateAdmChannel**](DefaultApi.md#updateAdmChannel) | **PUT** /v1/apps/{application-id}/channels/adm | 
[**updateApnsChannel**](DefaultApi.md#updateApnsChannel) | **PUT** /v1/apps/{application-id}/channels/apns | 
[**updateApnsSandboxChannel**](DefaultApi.md#updateApnsSandboxChannel) | **PUT** /v1/apps/{application-id}/channels/apns_sandbox | 
[**updateApnsVoipChannel**](DefaultApi.md#updateApnsVoipChannel) | **PUT** /v1/apps/{application-id}/channels/apns_voip | 
[**updateApnsVoipSandboxChannel**](DefaultApi.md#updateApnsVoipSandboxChannel) | **PUT** /v1/apps/{application-id}/channels/apns_voip_sandbox | 
[**updateApplicationSettings**](DefaultApi.md#updateApplicationSettings) | **PUT** /v1/apps/{application-id}/settings | 
[**updateBaiduChannel**](DefaultApi.md#updateBaiduChannel) | **PUT** /v1/apps/{application-id}/channels/baidu | 
[**updateCampaign**](DefaultApi.md#updateCampaign) | **PUT** /v1/apps/{application-id}/campaigns/{campaign-id} | 
[**updateEmailChannel**](DefaultApi.md#updateEmailChannel) | **PUT** /v1/apps/{application-id}/channels/email | 
[**updateEmailTemplate**](DefaultApi.md#updateEmailTemplate) | **PUT** /v1/templates/{template-name}/email | 
[**updateEndpoint**](DefaultApi.md#updateEndpoint) | **PUT** /v1/apps/{application-id}/endpoints/{endpoint-id} | 
[**updateEndpointsBatch**](DefaultApi.md#updateEndpointsBatch) | **PUT** /v1/apps/{application-id}/endpoints | 
[**updateGcmChannel**](DefaultApi.md#updateGcmChannel) | **PUT** /v1/apps/{application-id}/channels/gcm | 
[**updateInAppTemplate**](DefaultApi.md#updateInAppTemplate) | **PUT** /v1/templates/{template-name}/inapp | 
[**updateJourney**](DefaultApi.md#updateJourney) | **PUT** /v1/apps/{application-id}/journeys/{journey-id} | 
[**updateJourneyState**](DefaultApi.md#updateJourneyState) | **PUT** /v1/apps/{application-id}/journeys/{journey-id}/state | 
[**updatePushTemplate**](DefaultApi.md#updatePushTemplate) | **PUT** /v1/templates/{template-name}/push | 
[**updateRecommenderConfiguration**](DefaultApi.md#updateRecommenderConfiguration) | **PUT** /v1/recommenders/{recommender-id} | 
[**updateSegment**](DefaultApi.md#updateSegment) | **PUT** /v1/apps/{application-id}/segments/{segment-id} | 
[**updateSmsChannel**](DefaultApi.md#updateSmsChannel) | **PUT** /v1/apps/{application-id}/channels/sms | 
[**updateSmsTemplate**](DefaultApi.md#updateSmsTemplate) | **PUT** /v1/templates/{template-name}/sms | 
[**updateTemplateActiveVersion**](DefaultApi.md#updateTemplateActiveVersion) | **PUT** /v1/templates/{template-name}/{template-type}/active-version | 
[**updateVoiceChannel**](DefaultApi.md#updateVoiceChannel) | **PUT** /v1/apps/{application-id}/channels/voice | 
[**updateVoiceTemplate**](DefaultApi.md#updateVoiceTemplate) | **PUT** /v1/templates/{template-name}/voice | 
[**verifyOTPMessage**](DefaultApi.md#verifyOTPMessage) | **POST** /v1/apps/{application-id}/verify-otp | 



## createApp

> CreateAppResponse createApp(createAppRequest, opts)



 &lt;p&gt;Creates an application.&lt;/p&gt;

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let createAppRequest = new AmazonPinpoint.CreateAppRequest(); // CreateAppRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createApp(createAppRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createAppRequest** | [**CreateAppRequest**](CreateAppRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateAppResponse**](CreateAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createCampaign

> CreateCampaignResponse createCampaign(applicationId, createCampaignRequest, opts)



Creates a new campaign for an application or updates the settings of an existing campaign for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let createCampaignRequest = new AmazonPinpoint.CreateCampaignRequest(); // CreateCampaignRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createCampaign(applicationId, createCampaignRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **createCampaignRequest** | [**CreateCampaignRequest**](CreateCampaignRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateCampaignResponse**](CreateCampaignResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createEmailTemplate

> CreateEmailTemplateResponse createEmailTemplate(templateName, updateEmailTemplateRequest, opts)



Creates a message template for messages that are sent through the email channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateEmailTemplateRequest = new AmazonPinpoint.UpdateEmailTemplateRequest(); // UpdateEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createEmailTemplate(templateName, updateEmailTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateEmailTemplateRequest** | [**UpdateEmailTemplateRequest**](UpdateEmailTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateEmailTemplateResponse**](CreateEmailTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createExportJob

> CreateExportJobResponse createExportJob(applicationId, createExportJobRequest, opts)



Creates an export job for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let createExportJobRequest = new AmazonPinpoint.CreateExportJobRequest(); // CreateExportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createExportJob(applicationId, createExportJobRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **createExportJobRequest** | [**CreateExportJobRequest**](CreateExportJobRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateExportJobResponse**](CreateExportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createImportJob

> CreateImportJobResponse createImportJob(applicationId, createImportJobRequest, opts)



Creates an import job for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let createImportJobRequest = new AmazonPinpoint.CreateImportJobRequest(); // CreateImportJobRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createImportJob(applicationId, createImportJobRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
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


## createInAppTemplate

> CreateInAppTemplateResponse createInAppTemplate(templateName, updateInAppTemplateRequest, opts)



Creates a new message template for messages using the in-app message channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateInAppTemplateRequest = new AmazonPinpoint.UpdateInAppTemplateRequest(); // UpdateInAppTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createInAppTemplate(templateName, updateInAppTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateInAppTemplateRequest** | [**UpdateInAppTemplateRequest**](UpdateInAppTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateInAppTemplateResponse**](CreateInAppTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createJourney

> CreateJourneyResponse createJourney(applicationId, createJourneyRequest, opts)



Creates a journey for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let createJourneyRequest = new AmazonPinpoint.CreateJourneyRequest(); // CreateJourneyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createJourney(applicationId, createJourneyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **createJourneyRequest** | [**CreateJourneyRequest**](CreateJourneyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateJourneyResponse**](CreateJourneyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createPushTemplate

> CreatePushTemplateResponse createPushTemplate(templateName, updatePushTemplateRequest, opts)



Creates a message template for messages that are sent through a push notification channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updatePushTemplateRequest = new AmazonPinpoint.UpdatePushTemplateRequest(); // UpdatePushTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createPushTemplate(templateName, updatePushTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updatePushTemplateRequest** | [**UpdatePushTemplateRequest**](UpdatePushTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreatePushTemplateResponse**](CreatePushTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createRecommenderConfiguration

> CreateRecommenderConfigurationResponse createRecommenderConfiguration(createRecommenderConfigurationRequest, opts)



Creates an Amazon Pinpoint configuration for a recommender model.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let createRecommenderConfigurationRequest = new AmazonPinpoint.CreateRecommenderConfigurationRequest(); // CreateRecommenderConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createRecommenderConfiguration(createRecommenderConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **createRecommenderConfigurationRequest** | [**CreateRecommenderConfigurationRequest**](CreateRecommenderConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateRecommenderConfigurationResponse**](CreateRecommenderConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSegment

> CreateSegmentResponse createSegment(applicationId, createSegmentRequest, opts)



Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that&#39;s associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let createSegmentRequest = new AmazonPinpoint.CreateSegmentRequest(); // CreateSegmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSegment(applicationId, createSegmentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **createSegmentRequest** | [**CreateSegmentRequest**](CreateSegmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSegmentResponse**](CreateSegmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createSmsTemplate

> CreateSmsTemplateResponse createSmsTemplate(templateName, updateSmsTemplateRequest, opts)



Creates a message template for messages that are sent through the SMS channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateSmsTemplateRequest = new AmazonPinpoint.UpdateSmsTemplateRequest(); // UpdateSmsTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createSmsTemplate(templateName, updateSmsTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateSmsTemplateRequest** | [**UpdateSmsTemplateRequest**](UpdateSmsTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateSmsTemplateResponse**](CreateSmsTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## createVoiceTemplate

> CreateVoiceTemplateResponse createVoiceTemplate(templateName, updateVoiceTemplateRequest, opts)



Creates a message template for messages that are sent through the voice channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateVoiceTemplateRequest = new AmazonPinpoint.UpdateVoiceTemplateRequest(); // UpdateVoiceTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.createVoiceTemplate(templateName, updateVoiceTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateVoiceTemplateRequest** | [**UpdateVoiceTemplateRequest**](UpdateVoiceTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**CreateVoiceTemplateResponse**](CreateVoiceTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## deleteAdmChannel

> DeleteAdmChannelResponse deleteAdmChannel(applicationId, opts)



Disables the ADM channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteAdmChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAdmChannelResponse**](DeleteAdmChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApnsChannel

> DeleteApnsChannelResponse deleteApnsChannel(applicationId, opts)



Disables the APNs channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApnsChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApnsChannelResponse**](DeleteApnsChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApnsSandboxChannel

> DeleteApnsSandboxChannelResponse deleteApnsSandboxChannel(applicationId, opts)



Disables the APNs sandbox channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApnsSandboxChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApnsSandboxChannelResponse**](DeleteApnsSandboxChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApnsVoipChannel

> DeleteApnsVoipChannelResponse deleteApnsVoipChannel(applicationId, opts)



Disables the APNs VoIP channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApnsVoipChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApnsVoipChannelResponse**](DeleteApnsVoipChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApnsVoipSandboxChannel

> DeleteApnsVoipSandboxChannelResponse deleteApnsVoipSandboxChannel(applicationId, opts)



Disables the APNs VoIP sandbox channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApnsVoipSandboxChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteApnsVoipSandboxChannelResponse**](DeleteApnsVoipSandboxChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteApp

> DeleteAppResponse deleteApp(applicationId, opts)



Deletes an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteApp(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteAppResponse**](DeleteAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteBaiduChannel

> DeleteBaiduChannelResponse deleteBaiduChannel(applicationId, opts)



Disables the Baidu channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteBaiduChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteBaiduChannelResponse**](DeleteBaiduChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteCampaign

> DeleteCampaignResponse deleteCampaign(applicationId, campaignId, opts)



Deletes a campaign from an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteCampaign(applicationId, campaignId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteCampaignResponse**](DeleteCampaignResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEmailChannel

> DeleteEmailChannelResponse deleteEmailChannel(applicationId, opts)



Disables the email channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEmailChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteEmailChannelResponse**](DeleteEmailChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEmailTemplate

> DeleteEmailTemplateResponse deleteEmailTemplate(templateName, opts)



Deletes a message template for messages that were sent through the email channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
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
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**DeleteEmailTemplateResponse**](DeleteEmailTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEndpoint

> DeleteEndpointResponse deleteEndpoint(applicationId, endpointId, opts)



Deletes an endpoint from an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let endpointId = "endpointId_example"; // String | The unique identifier for the endpoint.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEndpoint(applicationId, endpointId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **endpointId** | **String**| The unique identifier for the endpoint. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteEndpointResponse**](DeleteEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteEventStream

> DeleteEventStreamResponse deleteEventStream(applicationId, opts)



Deletes the event stream for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteEventStream(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteEventStreamResponse**](DeleteEventStreamResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteGcmChannel

> DeleteGcmChannelResponse deleteGcmChannel(applicationId, opts)



Disables the GCM channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteGcmChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteGcmChannelResponse**](DeleteGcmChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteInAppTemplate

> DeleteInAppTemplateResponse deleteInAppTemplate(templateName, opts)



Deletes a message template for messages sent using the in-app message channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.deleteInAppTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**DeleteInAppTemplateResponse**](DeleteInAppTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteJourney

> DeleteJourneyResponse deleteJourney(applicationId, journeyId, opts)



Deletes a journey from an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteJourney(applicationId, journeyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteJourneyResponse**](DeleteJourneyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deletePushTemplate

> DeletePushTemplateResponse deletePushTemplate(templateName, opts)



Deletes a message template for messages that were sent through a push notification channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.deletePushTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**DeletePushTemplateResponse**](DeletePushTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteRecommenderConfiguration

> DeleteRecommenderConfigurationResponse deleteRecommenderConfiguration(recommenderId, opts)



Deletes an Amazon Pinpoint configuration for a recommender model.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let recommenderId = "recommenderId_example"; // String | The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteRecommenderConfiguration(recommenderId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommenderId** | **String**| The unique identifier for the recommender model configuration. This identifier is displayed as the &lt;b&gt;Recommender ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteRecommenderConfigurationResponse**](DeleteRecommenderConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSegment

> DeleteSegmentResponse deleteSegment(applicationId, segmentId, opts)



Deletes a segment from an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSegment(applicationId, segmentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSegmentResponse**](DeleteSegmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSmsChannel

> DeleteSmsChannelResponse deleteSmsChannel(applicationId, opts)



Disables the SMS channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteSmsChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteSmsChannelResponse**](DeleteSmsChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteSmsTemplate

> DeleteSmsTemplateResponse deleteSmsTemplate(templateName, opts)



Deletes a message template for messages that were sent through the SMS channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.deleteSmsTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**DeleteSmsTemplateResponse**](DeleteSmsTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteUserEndpoints

> DeleteUserEndpointsResponse deleteUserEndpoints(applicationId, userId, opts)



Deletes all the endpoints that are associated with a specific user ID.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let userId = "userId_example"; // String | The unique identifier for the user.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteUserEndpoints(applicationId, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **userId** | **String**| The unique identifier for the user. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteUserEndpointsResponse**](DeleteUserEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceChannel

> DeleteVoiceChannelResponse deleteVoiceChannel(applicationId, opts)



Disables the voice channel for an application and deletes any existing settings for the channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.deleteVoiceChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**DeleteVoiceChannelResponse**](DeleteVoiceChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## deleteVoiceTemplate

> DeleteVoiceTemplateResponse deleteVoiceTemplate(templateName, opts)



Deletes a message template for messages that were sent through the voice channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.deleteVoiceTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**DeleteVoiceTemplateResponse**](DeleteVoiceTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getAdmChannel

> GetAdmChannelResponse getAdmChannel(applicationId, opts)



Retrieves information about the status and settings of the ADM channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getAdmChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAdmChannelResponse**](GetAdmChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApnsChannel

> GetApnsChannelResponse getApnsChannel(applicationId, opts)



Retrieves information about the status and settings of the APNs channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApnsChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApnsChannelResponse**](GetApnsChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApnsSandboxChannel

> GetApnsSandboxChannelResponse getApnsSandboxChannel(applicationId, opts)



Retrieves information about the status and settings of the APNs sandbox channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApnsSandboxChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApnsSandboxChannelResponse**](GetApnsSandboxChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApnsVoipChannel

> GetApnsVoipChannelResponse getApnsVoipChannel(applicationId, opts)



Retrieves information about the status and settings of the APNs VoIP channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApnsVoipChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApnsVoipChannelResponse**](GetApnsVoipChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApnsVoipSandboxChannel

> GetApnsVoipSandboxChannelResponse getApnsVoipSandboxChannel(applicationId, opts)



Retrieves information about the status and settings of the APNs VoIP sandbox channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApnsVoipSandboxChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApnsVoipSandboxChannelResponse**](GetApnsVoipSandboxChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApp

> GetAppResponse getApp(applicationId, opts)



Retrieves information about an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApp(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetAppResponse**](GetAppResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationDateRangeKpi

> GetApplicationDateRangeKpiResponse getApplicationDateRangeKpi(applicationId, kpiName, opts)



Retrieves (queries) pre-aggregated data for a standard metric that applies to an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let kpiName = "kpiName_example"; // String | The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.
  'nextToken': "nextToken_example", // String | The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'startTime': new Date("2013-10-20T19:20:30+01:00") // Date | The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.
};
apiInstance.getApplicationDateRangeKpi(applicationId, kpiName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **kpiName** | **String**| The name of the metric, also referred to as a &lt;i&gt;key performance indicator (KPI)&lt;/i&gt;, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **endTime** | **Date**| The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019. | [optional] 
 **nextToken** | **String**| The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **startTime** | **Date**| The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day. | [optional] 

### Return type

[**GetApplicationDateRangeKpiResponse**](GetApplicationDateRangeKpiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApplicationSettings

> GetApplicationSettingsResponse getApplicationSettings(applicationId, opts)



Retrieves information about the settings for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getApplicationSettings(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetApplicationSettingsResponse**](GetApplicationSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getApps

> GetAppsResponse getApps(opts)



Retrieves information about all the applications that are associated with your Amazon Pinpoint account.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getApps(opts, (error, data, response) => {
  if (error) {
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
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetAppsResponse**](GetAppsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getBaiduChannel

> GetBaiduChannelResponse getBaiduChannel(applicationId, opts)



Retrieves information about the status and settings of the Baidu channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getBaiduChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetBaiduChannelResponse**](GetBaiduChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaign

> GetCampaignResponse getCampaign(applicationId, campaignId, opts)



Retrieves information about the status, configuration, and other settings for a campaign.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCampaign(applicationId, campaignId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCampaignResponse**](GetCampaignResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignActivities

> GetCampaignActivitiesResponse getCampaignActivities(applicationId, campaignId, opts)



Retrieves information about all the activities for a campaign.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getCampaignActivities(applicationId, campaignId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetCampaignActivitiesResponse**](GetCampaignActivitiesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignDateRangeKpi

> GetCampaignDateRangeKpiResponse getCampaignDateRangeKpi(applicationId, campaignId, kpiName, opts)



Retrieves (queries) pre-aggregated data for a standard metric that applies to a campaign.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let kpiName = "kpiName_example"; // String | The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.
  'nextToken': "nextToken_example", // String | The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'startTime': new Date("2013-10-20T19:20:30+01:00") // Date | The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.
};
apiInstance.getCampaignDateRangeKpi(applicationId, campaignId, kpiName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **kpiName** | **String**| The name of the metric, also referred to as a &lt;i&gt;key performance indicator (KPI)&lt;/i&gt;, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **endTime** | **Date**| The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019. | [optional] 
 **nextToken** | **String**| The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **startTime** | **Date**| The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day. | [optional] 

### Return type

[**GetCampaignDateRangeKpiResponse**](GetCampaignDateRangeKpiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignVersion

> GetCampaignVersionResponse getCampaignVersion(applicationId, campaignId, version, opts)



Retrieves information about the status, configuration, and other settings for a specific version of a campaign.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let version = "version_example"; // String | The unique version number (Version property) for the campaign version.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getCampaignVersion(applicationId, campaignId, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **version** | **String**| The unique version number (Version property) for the campaign version. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetCampaignVersionResponse**](GetCampaignVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaignVersions

> GetCampaignVersionsResponse getCampaignVersions(applicationId, campaignId, opts)



Retrieves information about the status, configuration, and other settings for all versions of a campaign.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getCampaignVersions(applicationId, campaignId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetCampaignVersionsResponse**](GetCampaignVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCampaigns

> GetCampaignsResponse getCampaigns(applicationId, opts)



Retrieves information about the status, configuration, and other settings for all the campaigns that are associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getCampaigns(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetCampaignsResponse**](GetCampaignsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getChannels

> GetChannelsResponse getChannels(applicationId, opts)



Retrieves information about the history and status of each channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getChannels(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetChannelsResponse**](GetChannelsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmailChannel

> GetEmailChannelResponse getEmailChannel(applicationId, opts)



Retrieves information about the status and settings of the email channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEmailChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEmailChannelResponse**](GetEmailChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEmailTemplate

> GetEmailTemplateResponse getEmailTemplate(templateName, opts)



Retrieves the content and settings of a message template for messages that are sent through the email channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
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
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**GetEmailTemplateResponse**](GetEmailTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEndpoint

> GetEndpointResponse getEndpoint(applicationId, endpointId, opts)



Retrieves information about the settings and attributes of a specific endpoint for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let endpointId = "endpointId_example"; // String | The unique identifier for the endpoint.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEndpoint(applicationId, endpointId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **endpointId** | **String**| The unique identifier for the endpoint. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetEndpointResponse**](GetEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventStream

> GetEventStreamResponse getEventStream(applicationId, opts)



Retrieves information about the event stream settings for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getEventStream(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
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


## getExportJob

> GetExportJobResponse getExportJob(applicationId, jobId, opts)



Retrieves information about the status and settings of a specific export job for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let jobId = "jobId_example"; // String | The unique identifier for the job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getExportJob(applicationId, jobId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **jobId** | **String**| The unique identifier for the job. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetExportJobResponse**](GetExportJobResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getExportJobs

> GetExportJobsResponse getExportJobs(applicationId, opts)



Retrieves information about the status and settings of all the export jobs for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getExportJobs(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetExportJobsResponse**](GetExportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getGcmChannel

> GetGcmChannelResponse getGcmChannel(applicationId, opts)



Retrieves information about the status and settings of the GCM channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getGcmChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetGcmChannelResponse**](GetGcmChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getImportJob

> GetImportJobResponse getImportJob(applicationId, jobId, opts)



Retrieves information about the status and settings of a specific import job for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let jobId = "jobId_example"; // String | The unique identifier for the job.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getImportJob(applicationId, jobId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **jobId** | **String**| The unique identifier for the job. | 
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


## getImportJobs

> GetImportJobsResponse getImportJobs(applicationId, opts)



Retrieves information about the status and settings of all the import jobs for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getImportJobs(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetImportJobsResponse**](GetImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInAppMessages

> GetInAppMessagesResponse getInAppMessages(applicationId, endpointId, opts)



Retrieves the in-app messages targeted for the provided endpoint ID.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let endpointId = "endpointId_example"; // String | The unique identifier for the endpoint.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getInAppMessages(applicationId, endpointId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **endpointId** | **String**| The unique identifier for the endpoint. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetInAppMessagesResponse**](GetInAppMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getInAppTemplate

> GetInAppTemplateResponse getInAppTemplate(templateName, opts)



Retrieves the content and settings of a message template for messages sent through the in-app channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.getInAppTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**GetInAppTemplateResponse**](GetInAppTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourney

> GetJourneyResponse getJourney(applicationId, journeyId, opts)



Retrieves information about the status, configuration, and other settings for a journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getJourney(applicationId, journeyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetJourneyResponse**](GetJourneyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourneyDateRangeKpi

> GetJourneyDateRangeKpiResponse getJourneyDateRangeKpi(applicationId, journeyId, kpiName, opts)



Retrieves (queries) pre-aggregated data for a standard engagement metric that applies to a journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let kpiName = "kpiName_example"; // String | The name of the metric, also referred to as a <i>key performance indicator (KPI)</i>, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the <a href=\"https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\">Amazon Pinpoint Developer Guide</a>.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019.
  'nextToken': "nextToken_example", // String | The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'startTime': new Date("2013-10-20T19:20:30+01:00") // Date | The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day.
};
apiInstance.getJourneyDateRangeKpi(applicationId, journeyId, kpiName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **kpiName** | **String**| The name of the metric, also referred to as a &lt;i&gt;key performance indicator (KPI)&lt;/i&gt;, to retrieve data for. This value describes the associated metric and consists of two or more terms, which are comprised of lowercase alphanumeric characters, separated by a hyphen. Examples are email-open-rate and successful-delivery-rate. For a list of valid values, see the &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/pinpoint/latest/developerguide/analytics-standard-metrics.html\&quot;&gt;Amazon Pinpoint Developer Guide&lt;/a&gt;. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **endTime** | **Date**| The last date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-26T20:00:00Z for 8:00 PM UTC July 26, 2019. | [optional] 
 **nextToken** | **String**| The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **startTime** | **Date**| The first date and time to retrieve data for, as part of an inclusive date range that filters the query results. This value should be in extended ISO 8601 format and use Coordinated Universal Time (UTC), for example: 2019-07-19T20:00:00Z for 8:00 PM UTC July 19, 2019. This value should also be fewer than 90 days from the current day. | [optional] 

### Return type

[**GetJourneyDateRangeKpiResponse**](GetJourneyDateRangeKpiResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourneyExecutionActivityMetrics

> GetJourneyExecutionActivityMetricsResponse getJourneyExecutionActivityMetrics(applicationId, journeyActivityId, journeyId, opts)



Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey activity.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyActivityId = "journeyActivityId_example"; // String | The unique identifier for the journey activity.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example" // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
};
apiInstance.getJourneyExecutionActivityMetrics(applicationId, journeyActivityId, journeyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyActivityId** | **String**| The unique identifier for the journey activity. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 

### Return type

[**GetJourneyExecutionActivityMetricsResponse**](GetJourneyExecutionActivityMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourneyExecutionMetrics

> GetJourneyExecutionMetricsResponse getJourneyExecutionMetrics(applicationId, journeyId, opts)



Retrieves (queries) pre-aggregated data for a standard execution metric that applies to a journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example" // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
};
apiInstance.getJourneyExecutionMetrics(applicationId, journeyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 

### Return type

[**GetJourneyExecutionMetricsResponse**](GetJourneyExecutionMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourneyRunExecutionActivityMetrics

> GetJourneyRunExecutionActivityMetricsResponse getJourneyRunExecutionActivityMetrics(applicationId, journeyActivityId, journeyId, runId, opts)



Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey activity.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyActivityId = "journeyActivityId_example"; // String | The unique identifier for the journey activity.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let runId = "runId_example"; // String | The unique identifier for the journey run.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example" // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
};
apiInstance.getJourneyRunExecutionActivityMetrics(applicationId, journeyActivityId, journeyId, runId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyActivityId** | **String**| The unique identifier for the journey activity. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **runId** | **String**| The unique identifier for the journey run. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 

### Return type

[**GetJourneyRunExecutionActivityMetricsResponse**](GetJourneyRunExecutionActivityMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourneyRunExecutionMetrics

> GetJourneyRunExecutionMetricsResponse getJourneyRunExecutionMetrics(applicationId, journeyId, runId, opts)



Retrieves (queries) pre-aggregated data for a standard run execution metric that applies to a journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let runId = "runId_example"; // String | The unique identifier for the journey run.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The <code/> string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example" // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
};
apiInstance.getJourneyRunExecutionMetrics(applicationId, journeyId, runId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **runId** | **String**| The unique identifier for the journey run. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The &lt;code/&gt; string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 

### Return type

[**GetJourneyRunExecutionMetricsResponse**](GetJourneyRunExecutionMetricsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getJourneyRuns

> GetJourneyRunsResponse getJourneyRuns(applicationId, journeyId, opts)



Provides information about the runs of a journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getJourneyRuns(applicationId, journeyId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetJourneyRunsResponse**](GetJourneyRunsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getPushTemplate

> GetPushTemplateResponse getPushTemplate(templateName, opts)



Retrieves the content and settings of a message template for messages that are sent through a push notification channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.getPushTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**GetPushTemplateResponse**](GetPushTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecommenderConfiguration

> GetRecommenderConfigurationResponse getRecommenderConfiguration(recommenderId, opts)



Retrieves information about an Amazon Pinpoint configuration for a recommender model.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let recommenderId = "recommenderId_example"; // String | The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getRecommenderConfiguration(recommenderId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommenderId** | **String**| The unique identifier for the recommender model configuration. This identifier is displayed as the &lt;b&gt;Recommender ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetRecommenderConfigurationResponse**](GetRecommenderConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getRecommenderConfigurations

> GetRecommenderConfigurationsResponse getRecommenderConfigurations(opts)



Retrieves information about all the recommender model configurations that are associated with your Amazon Pinpoint account.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getRecommenderConfigurations(opts, (error, data, response) => {
  if (error) {
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
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetRecommenderConfigurationsResponse**](GetRecommenderConfigurationsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegment

> GetSegmentResponse getSegment(applicationId, segmentId, opts)



Retrieves information about the configuration, dimension, and other settings for a specific segment that&#39;s associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSegment(applicationId, segmentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSegmentResponse**](GetSegmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegmentExportJobs

> GetSegmentExportJobsResponse getSegmentExportJobs(applicationId, segmentId, opts)



Retrieves information about the status and settings of the export jobs for a segment.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getSegmentExportJobs(applicationId, segmentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetSegmentExportJobsResponse**](GetSegmentExportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegmentImportJobs

> GetSegmentImportJobsResponse getSegmentImportJobs(applicationId, segmentId, opts)



Retrieves information about the status and settings of the import jobs for a segment.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getSegmentImportJobs(applicationId, segmentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetSegmentImportJobsResponse**](GetSegmentImportJobsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegmentVersion

> GetSegmentVersionResponse getSegmentVersion(applicationId, segmentId, version, opts)



Retrieves information about the configuration, dimension, and other settings for a specific version of a segment that&#39;s associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let version = "version_example"; // String | The unique version number (Version property) for the campaign version.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSegmentVersion(applicationId, segmentId, version, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **version** | **String**| The unique version number (Version property) for the campaign version. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSegmentVersionResponse**](GetSegmentVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegmentVersions

> GetSegmentVersionsResponse getSegmentVersions(applicationId, segmentId, opts)



Retrieves information about the configuration, dimension, and other settings for all the versions of a specific segment that&#39;s associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getSegmentVersions(applicationId, segmentId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetSegmentVersionsResponse**](GetSegmentVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSegments

> GetSegmentsResponse getSegments(applicationId, opts)



Retrieves information about the configuration, dimension, and other settings for all the segments that are associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.getSegments(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**GetSegmentsResponse**](GetSegmentsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSmsChannel

> GetSmsChannelResponse getSmsChannel(applicationId, opts)



Retrieves information about the status and settings of the SMS channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getSmsChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetSmsChannelResponse**](GetSmsChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSmsTemplate

> GetSmsTemplateResponse getSmsTemplate(templateName, opts)



Retrieves the content and settings of a message template for messages that are sent through the SMS channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.getSmsTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**GetSmsTemplateResponse**](GetSmsTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getUserEndpoints

> GetUserEndpointsResponse getUserEndpoints(applicationId, userId, opts)



Retrieves information about all the endpoints that are associated with a specific user ID.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let userId = "userId_example"; // String | The unique identifier for the user.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getUserEndpoints(applicationId, userId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **userId** | **String**| The unique identifier for the user. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetUserEndpointsResponse**](GetUserEndpointsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceChannel

> GetVoiceChannelResponse getVoiceChannel(applicationId, opts)



Retrieves information about the status and settings of the voice channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.getVoiceChannel(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**GetVoiceChannelResponse**](GetVoiceChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getVoiceTemplate

> GetVoiceTemplateResponse getVoiceTemplate(templateName, opts)



Retrieves the content and settings of a message template for messages that are sent through the voice channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.getVoiceTemplate(templateName, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**GetVoiceTemplateResponse**](GetVoiceTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listJourneys

> ListJourneysResponse listJourneys(applicationId, opts)



Retrieves information about the status, configuration, and other settings for all the journeys that are associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'token': "token_example" // String | The NextToken string that specifies which page of results to return in a paginated response.
};
apiInstance.listJourneys(applicationId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **token** | **String**| The NextToken string that specifies which page of results to return in a paginated response. | [optional] 

### Return type

[**ListJourneysResponse**](ListJourneysResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTagsForResource

> ListTagsForResourceResponse listTagsForResource(resourceArn, opts)



Retrieves all the tags (keys and values) that are associated with an application, campaign, message template, or segment.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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


## listTemplateVersions

> ListTemplateVersionsResponse listTemplateVersions(templateName, templateType, opts)



Retrieves information about all the versions of a specific message template.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let templateType = "templateType_example"; // String | The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example" // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
};
apiInstance.listTemplateVersions(templateName, templateType, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **templateType** | **String**| The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE. | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **nextToken** | **String**| The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 

### Return type

[**ListTemplateVersionsResponse**](ListTemplateVersionsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listTemplates

> ListTemplatesResponse listTemplates(opts)



Retrieves information about all the message templates that are associated with your Amazon Pinpoint account.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'nextToken': "nextToken_example", // String | The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'pageSize': "pageSize_example", // String | The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics.
  'prefix': "prefix_example", // String | The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify.
  'templateType': "templateType_example" // String | The type of message template to include in the results. Valid values are: EMAIL, PUSH, SMS, and VOICE. To include all types of templates in the results, don't include this parameter in your request.
};
apiInstance.listTemplates(opts, (error, data, response) => {
  if (error) {
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
 **nextToken** | **String**| The  string that specifies which page of results to return in a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **pageSize** | **String**| The maximum number of items to include in each page of a paginated response. This parameter is not supported for application, campaign, and journey metrics. | [optional] 
 **prefix** | **String**| The substring to match in the names of the message templates to include in the results. If you specify this value, Amazon Pinpoint returns only those templates whose names begin with the value that you specify. | [optional] 
 **templateType** | **String**| The type of message template to include in the results. Valid values are: EMAIL, PUSH, SMS, and VOICE. To include all types of templates in the results, don&#39;t include this parameter in your request. | [optional] 

### Return type

[**ListTemplatesResponse**](ListTemplatesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phoneNumberValidate

> PhoneNumberValidateResponse phoneNumberValidate(phoneNumberValidateRequest, opts)



Retrieves information about a phone number.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let phoneNumberValidateRequest = new AmazonPinpoint.PhoneNumberValidateRequest(); // PhoneNumberValidateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.phoneNumberValidate(phoneNumberValidateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumberValidateRequest** | [**PhoneNumberValidateRequest**](PhoneNumberValidateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PhoneNumberValidateResponse**](PhoneNumberValidateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putEventStream

> PutEventStreamResponse putEventStream(applicationId, putEventStreamRequest, opts)



Creates a new event stream for an application or updates the settings of an existing event stream for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let putEventStreamRequest = new AmazonPinpoint.PutEventStreamRequest(); // PutEventStreamRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEventStream(applicationId, putEventStreamRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **putEventStreamRequest** | [**PutEventStreamRequest**](PutEventStreamRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutEventStreamResponse**](PutEventStreamResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## putEvents

> PutEventsResponse putEvents(applicationId, putEventsRequest, opts)



Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let putEventsRequest = new AmazonPinpoint.PutEventsRequest(); // PutEventsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.putEvents(applicationId, putEventsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **putEventsRequest** | [**PutEventsRequest**](PutEventsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**PutEventsResponse**](PutEventsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## removeAttributes

> RemoveAttributesResponse removeAttributes(applicationId, attributeType, removeAttributesRequest, opts)



Removes one or more attributes, of the same attribute type, from all the endpoints that are associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let attributeType = "attributeType_example"; // String |  <p>The type of attribute or attributes to remove. Valid values are:</p> <ul><li><p>endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.</p></li> <li><p>endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.</p></li> <li><p>endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.</p></li></ul>
let removeAttributesRequest = new AmazonPinpoint.RemoveAttributesRequest(); // RemoveAttributesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.removeAttributes(applicationId, attributeType, removeAttributesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **attributeType** | **String**|  &lt;p&gt;The type of attribute or attributes to remove. Valid values are:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;endpoint-custom-attributes - Custom attributes that describe endpoints, such as the date when an associated user opted in or out of receiving communications from you through a specific type of channel.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;endpoint-metric-attributes - Custom metrics that your app reports to Amazon Pinpoint for endpoints, such as the number of app sessions or the number of items left in a cart.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;endpoint-user-attributes - Custom attributes that describe users, such as first name, last name, and age.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | 
 **removeAttributesRequest** | [**RemoveAttributesRequest**](RemoveAttributesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**RemoveAttributesResponse**](RemoveAttributesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendMessages

> SendMessagesResponse sendMessages(applicationId, sendMessagesRequest, opts)



Creates and sends a direct message.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let sendMessagesRequest = new AmazonPinpoint.SendMessagesRequest(); // SendMessagesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendMessages(applicationId, sendMessagesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **sendMessagesRequest** | [**SendMessagesRequest**](SendMessagesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendMessagesResponse**](SendMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendOTPMessage

> SendOTPMessageResponse sendOTPMessage(applicationId, sendOTPMessageRequest, opts)



Send an OTP message

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique ID of your Amazon Pinpoint application.
let sendOTPMessageRequest = new AmazonPinpoint.SendOTPMessageRequest(); // SendOTPMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendOTPMessage(applicationId, sendOTPMessageRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique ID of your Amazon Pinpoint application. | 
 **sendOTPMessageRequest** | [**SendOTPMessageRequest**](SendOTPMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendOTPMessageResponse**](SendOTPMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## sendUsersMessages

> SendUsersMessagesResponse sendUsersMessages(applicationId, sendUsersMessagesRequest, opts)



Creates and sends a message to a list of users.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let sendUsersMessagesRequest = new AmazonPinpoint.SendUsersMessagesRequest(); // SendUsersMessagesRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.sendUsersMessages(applicationId, sendUsersMessagesRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **sendUsersMessagesRequest** | [**SendUsersMessagesRequest**](SendUsersMessagesRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**SendUsersMessagesResponse**](SendUsersMessagesResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## tagResource

> tagResource(resourceArn, tagResourceRequest, opts)



Adds one or more tags (keys and values) to an application, campaign, message template, or segment.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagResourceRequest = new AmazonPinpoint.TagResourceRequest(); // TagResourceRequest | 
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
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
- **Accept**: Not defined


## untagResource

> untagResource(resourceArn, tagKeys, opts)



Removes one or more tags (keys and values) from an application, campaign, message template, or segment.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let resourceArn = "resourceArn_example"; // String | The Amazon Resource Name (ARN) of the resource.
let tagKeys = ["null"]; // [String] | The key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&amp;).
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
 **resourceArn** | **String**| The Amazon Resource Name (ARN) of the resource. | 
 **tagKeys** | [**[String]**](String.md)| The key of the tag to remove from the resource. To remove multiple tags, append the tagKeys parameter and argument for each additional tag to remove, separated by an ampersand (&amp;amp;). | 
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
- **Accept**: Not defined


## updateAdmChannel

> UpdateAdmChannelResponse updateAdmChannel(applicationId, updateAdmChannelRequest, opts)



Enables the ADM channel for an application or updates the status and settings of the ADM channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateAdmChannelRequest = new AmazonPinpoint.UpdateAdmChannelRequest(); // UpdateAdmChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateAdmChannel(applicationId, updateAdmChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateAdmChannelRequest** | [**UpdateAdmChannelRequest**](UpdateAdmChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateAdmChannelResponse**](UpdateAdmChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApnsChannel

> UpdateApnsChannelResponse updateApnsChannel(applicationId, updateApnsChannelRequest, opts)



Enables the APNs channel for an application or updates the status and settings of the APNs channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateApnsChannelRequest = new AmazonPinpoint.UpdateApnsChannelRequest(); // UpdateApnsChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApnsChannel(applicationId, updateApnsChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateApnsChannelRequest** | [**UpdateApnsChannelRequest**](UpdateApnsChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApnsChannelResponse**](UpdateApnsChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApnsSandboxChannel

> UpdateApnsSandboxChannelResponse updateApnsSandboxChannel(applicationId, updateApnsSandboxChannelRequest, opts)



Enables the APNs sandbox channel for an application or updates the status and settings of the APNs sandbox channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateApnsSandboxChannelRequest = new AmazonPinpoint.UpdateApnsSandboxChannelRequest(); // UpdateApnsSandboxChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApnsSandboxChannel(applicationId, updateApnsSandboxChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateApnsSandboxChannelRequest** | [**UpdateApnsSandboxChannelRequest**](UpdateApnsSandboxChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApnsSandboxChannelResponse**](UpdateApnsSandboxChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApnsVoipChannel

> UpdateApnsVoipChannelResponse updateApnsVoipChannel(applicationId, updateApnsVoipChannelRequest, opts)



Enables the APNs VoIP channel for an application or updates the status and settings of the APNs VoIP channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateApnsVoipChannelRequest = new AmazonPinpoint.UpdateApnsVoipChannelRequest(); // UpdateApnsVoipChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApnsVoipChannel(applicationId, updateApnsVoipChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateApnsVoipChannelRequest** | [**UpdateApnsVoipChannelRequest**](UpdateApnsVoipChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApnsVoipChannelResponse**](UpdateApnsVoipChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApnsVoipSandboxChannel

> UpdateApnsVoipSandboxChannelResponse updateApnsVoipSandboxChannel(applicationId, updateApnsVoipSandboxChannelRequest, opts)



Enables the APNs VoIP sandbox channel for an application or updates the status and settings of the APNs VoIP sandbox channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateApnsVoipSandboxChannelRequest = new AmazonPinpoint.UpdateApnsVoipSandboxChannelRequest(); // UpdateApnsVoipSandboxChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApnsVoipSandboxChannel(applicationId, updateApnsVoipSandboxChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateApnsVoipSandboxChannelRequest** | [**UpdateApnsVoipSandboxChannelRequest**](UpdateApnsVoipSandboxChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApnsVoipSandboxChannelResponse**](UpdateApnsVoipSandboxChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateApplicationSettings

> UpdateApplicationSettingsResponse updateApplicationSettings(applicationId, updateApplicationSettingsRequest, opts)



Updates the settings for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateApplicationSettingsRequest = new AmazonPinpoint.UpdateApplicationSettingsRequest(); // UpdateApplicationSettingsRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateApplicationSettings(applicationId, updateApplicationSettingsRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateApplicationSettingsRequest** | [**UpdateApplicationSettingsRequest**](UpdateApplicationSettingsRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateApplicationSettingsResponse**](UpdateApplicationSettingsResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateBaiduChannel

> UpdateBaiduChannelResponse updateBaiduChannel(applicationId, updateBaiduChannelRequest, opts)



Enables the Baidu channel for an application or updates the status and settings of the Baidu channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateBaiduChannelRequest = new AmazonPinpoint.UpdateBaiduChannelRequest(); // UpdateBaiduChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateBaiduChannel(applicationId, updateBaiduChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateBaiduChannelRequest** | [**UpdateBaiduChannelRequest**](UpdateBaiduChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateBaiduChannelResponse**](UpdateBaiduChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateCampaign

> UpdateCampaignResponse updateCampaign(applicationId, campaignId, createCampaignRequest, opts)



Updates the configuration and other settings for a campaign.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let campaignId = "campaignId_example"; // String | The unique identifier for the campaign.
let createCampaignRequest = new AmazonPinpoint.CreateCampaignRequest(); // CreateCampaignRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateCampaign(applicationId, campaignId, createCampaignRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **campaignId** | **String**| The unique identifier for the campaign. | 
 **createCampaignRequest** | [**CreateCampaignRequest**](CreateCampaignRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateCampaignResponse**](UpdateCampaignResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEmailChannel

> UpdateEmailChannelResponse updateEmailChannel(applicationId, updateEmailChannelRequest, opts)



Enables the email channel for an application or updates the status and settings of the email channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateEmailChannelRequest = new AmazonPinpoint.UpdateEmailChannelRequest(); // UpdateEmailChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEmailChannel(applicationId, updateEmailChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateEmailChannelRequest** | [**UpdateEmailChannelRequest**](UpdateEmailChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateEmailChannelResponse**](UpdateEmailChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEmailTemplate

> UpdateEmailTemplateResponse updateEmailTemplate(templateName, updateEmailTemplateRequest, opts)



Updates an existing message template for messages that are sent through the email channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateEmailTemplateRequest = new AmazonPinpoint.UpdateEmailTemplateRequest(); // UpdateEmailTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'createNewVersion': true, // Boolean | <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
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
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateEmailTemplateRequest** | [**UpdateEmailTemplateRequest**](UpdateEmailTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **createNewVersion** | **Boolean**| &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt; | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**UpdateEmailTemplateResponse**](UpdateEmailTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEndpoint

> UpdateEndpointResponse updateEndpoint(applicationId, endpointId, updateEndpointRequest, opts)



Creates a new endpoint for an application or updates the settings and attributes of an existing endpoint for an application. You can also use this operation to define custom attributes for an endpoint. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let endpointId = "endpointId_example"; // String | The unique identifier for the endpoint.
let updateEndpointRequest = new AmazonPinpoint.UpdateEndpointRequest(); // UpdateEndpointRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEndpoint(applicationId, endpointId, updateEndpointRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **endpointId** | **String**| The unique identifier for the endpoint. | 
 **updateEndpointRequest** | [**UpdateEndpointRequest**](UpdateEndpointRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateEndpointResponse**](UpdateEndpointResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateEndpointsBatch

> UpdateEndpointsBatchResponse updateEndpointsBatch(applicationId, updateEndpointsBatchRequest, opts)



Creates a new batch of endpoints for an application or updates the settings and attributes of a batch of existing endpoints for an application. You can also use this operation to define custom attributes for a batch of endpoints. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateEndpointsBatchRequest = new AmazonPinpoint.UpdateEndpointsBatchRequest(); // UpdateEndpointsBatchRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateEndpointsBatch(applicationId, updateEndpointsBatchRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateEndpointsBatchRequest** | [**UpdateEndpointsBatchRequest**](UpdateEndpointsBatchRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateEndpointsBatchResponse**](UpdateEndpointsBatchResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateGcmChannel

> UpdateGcmChannelResponse updateGcmChannel(applicationId, updateGcmChannelRequest, opts)



Enables the GCM channel for an application or updates the status and settings of the GCM channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateGcmChannelRequest = new AmazonPinpoint.UpdateGcmChannelRequest(); // UpdateGcmChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateGcmChannel(applicationId, updateGcmChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateGcmChannelRequest** | [**UpdateGcmChannelRequest**](UpdateGcmChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateGcmChannelResponse**](UpdateGcmChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateInAppTemplate

> UpdateInAppTemplateResponse updateInAppTemplate(templateName, updateInAppTemplateRequest, opts)



Updates an existing message template for messages sent through the in-app message channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateInAppTemplateRequest = new AmazonPinpoint.UpdateInAppTemplateRequest(); // UpdateInAppTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'createNewVersion': true, // Boolean | <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.updateInAppTemplate(templateName, updateInAppTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateInAppTemplateRequest** | [**UpdateInAppTemplateRequest**](UpdateInAppTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **createNewVersion** | **Boolean**| &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt; | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**UpdateInAppTemplateResponse**](UpdateInAppTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateJourney

> UpdateJourneyResponse updateJourney(applicationId, journeyId, createJourneyRequest, opts)



Updates the configuration and other settings for a journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let createJourneyRequest = new AmazonPinpoint.CreateJourneyRequest(); // CreateJourneyRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJourney(applicationId, journeyId, createJourneyRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **createJourneyRequest** | [**CreateJourneyRequest**](CreateJourneyRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateJourneyResponse**](UpdateJourneyResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateJourneyState

> UpdateJourneyStateResponse updateJourneyState(applicationId, journeyId, updateJourneyStateRequest, opts)



Cancels (stops) an active journey.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let journeyId = "journeyId_example"; // String | The unique identifier for the journey.
let updateJourneyStateRequest = new AmazonPinpoint.UpdateJourneyStateRequest(); // UpdateJourneyStateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateJourneyState(applicationId, journeyId, updateJourneyStateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **journeyId** | **String**| The unique identifier for the journey. | 
 **updateJourneyStateRequest** | [**UpdateJourneyStateRequest**](UpdateJourneyStateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateJourneyStateResponse**](UpdateJourneyStateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updatePushTemplate

> UpdatePushTemplateResponse updatePushTemplate(templateName, updatePushTemplateRequest, opts)



Updates an existing message template for messages that are sent through a push notification channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updatePushTemplateRequest = new AmazonPinpoint.UpdatePushTemplateRequest(); // UpdatePushTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'createNewVersion': true, // Boolean | <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.updatePushTemplate(templateName, updatePushTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updatePushTemplateRequest** | [**UpdatePushTemplateRequest**](UpdatePushTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **createNewVersion** | **Boolean**| &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt; | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**UpdatePushTemplateResponse**](UpdatePushTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateRecommenderConfiguration

> UpdateRecommenderConfigurationResponse updateRecommenderConfiguration(recommenderId, updateRecommenderConfigurationRequest, opts)



Updates an Amazon Pinpoint configuration for a recommender model.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let recommenderId = "recommenderId_example"; // String | The unique identifier for the recommender model configuration. This identifier is displayed as the <b>Recommender ID</b> on the Amazon Pinpoint console.
let updateRecommenderConfigurationRequest = new AmazonPinpoint.UpdateRecommenderConfigurationRequest(); // UpdateRecommenderConfigurationRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateRecommenderConfiguration(recommenderId, updateRecommenderConfigurationRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recommenderId** | **String**| The unique identifier for the recommender model configuration. This identifier is displayed as the &lt;b&gt;Recommender ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateRecommenderConfigurationRequest** | [**UpdateRecommenderConfigurationRequest**](UpdateRecommenderConfigurationRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateRecommenderConfigurationResponse**](UpdateRecommenderConfigurationResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSegment

> UpdateSegmentResponse updateSegment(applicationId, segmentId, createSegmentRequest, opts)



Creates a new segment for an application or updates the configuration, dimension, and other settings for an existing segment that&#39;s associated with an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let segmentId = "segmentId_example"; // String | The unique identifier for the segment.
let createSegmentRequest = new AmazonPinpoint.CreateSegmentRequest(); // CreateSegmentRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSegment(applicationId, segmentId, createSegmentRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **segmentId** | **String**| The unique identifier for the segment. | 
 **createSegmentRequest** | [**CreateSegmentRequest**](CreateSegmentRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSegmentResponse**](UpdateSegmentResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSmsChannel

> UpdateSmsChannelResponse updateSmsChannel(applicationId, updateSmsChannelRequest, opts)



Enables the SMS channel for an application or updates the status and settings of the SMS channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateSmsChannelRequest = new AmazonPinpoint.UpdateSmsChannelRequest(); // UpdateSmsChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateSmsChannel(applicationId, updateSmsChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateSmsChannelRequest** | [**UpdateSmsChannelRequest**](UpdateSmsChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateSmsChannelResponse**](UpdateSmsChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateSmsTemplate

> UpdateSmsTemplateResponse updateSmsTemplate(templateName, updateSmsTemplateRequest, opts)



Updates an existing message template for messages that are sent through the SMS channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateSmsTemplateRequest = new AmazonPinpoint.UpdateSmsTemplateRequest(); // UpdateSmsTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'createNewVersion': true, // Boolean | <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.updateSmsTemplate(templateName, updateSmsTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateSmsTemplateRequest** | [**UpdateSmsTemplateRequest**](UpdateSmsTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **createNewVersion** | **Boolean**| &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt; | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**UpdateSmsTemplateResponse**](UpdateSmsTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateTemplateActiveVersion

> UpdateTemplateActiveVersionResponse updateTemplateActiveVersion(templateName, templateType, updateTemplateActiveVersionRequest, opts)



Changes the status of a specific version of a message template to &lt;i&gt;active&lt;/i&gt;.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let templateType = "templateType_example"; // String | The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE.
let updateTemplateActiveVersionRequest = new AmazonPinpoint.UpdateTemplateActiveVersionRequest(); // UpdateTemplateActiveVersionRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateTemplateActiveVersion(templateName, templateType, updateTemplateActiveVersionRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **templateType** | **String**| The type of channel that the message template is designed for. Valid values are: EMAIL, PUSH, SMS, and VOICE. | 
 **updateTemplateActiveVersionRequest** | [**UpdateTemplateActiveVersionRequest**](UpdateTemplateActiveVersionRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateTemplateActiveVersionResponse**](UpdateTemplateActiveVersionResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVoiceChannel

> UpdateVoiceChannelResponse updateVoiceChannel(applicationId, updateVoiceChannelRequest, opts)



Enables the voice channel for an application or updates the status and settings of the voice channel for an application.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.
let updateVoiceChannelRequest = new AmazonPinpoint.UpdateVoiceChannelRequest(); // UpdateVoiceChannelRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.updateVoiceChannel(applicationId, updateVoiceChannelRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique identifier for the application. This identifier is displayed as the &lt;b&gt;Project ID&lt;/b&gt; on the Amazon Pinpoint console. | 
 **updateVoiceChannelRequest** | [**UpdateVoiceChannelRequest**](UpdateVoiceChannelRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**UpdateVoiceChannelResponse**](UpdateVoiceChannelResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## updateVoiceTemplate

> UpdateVoiceTemplateResponse updateVoiceTemplate(templateName, updateVoiceTemplateRequest, opts)



Updates an existing message template for messages that are sent through the voice channel.

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let templateName = "templateName_example"; // String | The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.
let updateVoiceTemplateRequest = new AmazonPinpoint.UpdateVoiceTemplateRequest(); // UpdateVoiceTemplateRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example", // String | 
  'createNewVersion': true, // Boolean | <p>Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don't specify a value for the version parameter. Otherwise, an error will occur.</p>
  'version': "version_example" // String | <p>The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the <link  linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don't occur.</p> <p>If you don't specify a value for this parameter, Amazon Pinpoint does the following:</p> <ul><li><p>For a get operation, retrieves information about the active version of the template.</p></li> <li><p>For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn't used or is set to false.</p></li> <li><p>For a delete operation, deletes the template, including all versions of the template.</p></li></ul>
};
apiInstance.updateVoiceTemplate(templateName, updateVoiceTemplateRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **templateName** | **String**| The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive. | 
 **updateVoiceTemplateRequest** | [**UpdateVoiceTemplateRequest**](UpdateVoiceTemplateRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 
 **createNewVersion** | **Boolean**| &lt;p&gt;Specifies whether to save the updates as a new version of the message template. Valid values are: true, save the updates as a new version; and, false, save the updates to (overwrite) the latest existing version of the template.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint saves the updates to (overwrites) the latest existing version of the template. If you specify a value of true for this parameter, don&#39;t specify a value for the version parameter. Otherwise, an error will occur.&lt;/p&gt; | [optional] 
 **version** | **String**| &lt;p&gt;The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the &lt;link  linkend&#x3D;\&quot;templates-template-name-template-type-versions\&quot;&gt;Template Versions&lt;/link&gt; resource.&lt;/p&gt; &lt;p&gt;If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions don&#39;t occur.&lt;/p&gt; &lt;p&gt;If you don&#39;t specify a value for this parameter, Amazon Pinpoint does the following:&lt;/p&gt; &lt;ul&gt;&lt;li&gt;&lt;p&gt;For a get operation, retrieves information about the active version of the template.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isn&#39;t used or is set to false.&lt;/p&gt;&lt;/li&gt; &lt;li&gt;&lt;p&gt;For a delete operation, deletes the template, including all versions of the template.&lt;/p&gt;&lt;/li&gt;&lt;/ul&gt; | [optional] 

### Return type

[**UpdateVoiceTemplateResponse**](UpdateVoiceTemplateResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## verifyOTPMessage

> VerifyOTPMessageResponse verifyOTPMessage(applicationId, verifyOTPMessageRequest, opts)



Verify an OTP

### Example

```javascript
import AmazonPinpoint from 'amazon_pinpoint';
let defaultClient = AmazonPinpoint.ApiClient.instance;
// Configure API key authorization: hmac
let hmac = defaultClient.authentications['hmac'];
hmac.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//hmac.apiKeyPrefix = 'Token';

let apiInstance = new AmazonPinpoint.DefaultApi();
let applicationId = "applicationId_example"; // String | The unique ID of your Amazon Pinpoint application.
let verifyOTPMessageRequest = new AmazonPinpoint.VerifyOTPMessageRequest(); // VerifyOTPMessageRequest | 
let opts = {
  'xAmzContentSha256': "xAmzContentSha256_example", // String | 
  'xAmzDate': "xAmzDate_example", // String | 
  'xAmzAlgorithm': "xAmzAlgorithm_example", // String | 
  'xAmzCredential': "xAmzCredential_example", // String | 
  'xAmzSecurityToken': "xAmzSecurityToken_example", // String | 
  'xAmzSignature': "xAmzSignature_example", // String | 
  'xAmzSignedHeaders': "xAmzSignedHeaders_example" // String | 
};
apiInstance.verifyOTPMessage(applicationId, verifyOTPMessageRequest, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applicationId** | **String**| The unique ID of your Amazon Pinpoint application. | 
 **verifyOTPMessageRequest** | [**VerifyOTPMessageRequest**](VerifyOTPMessageRequest.md)|  | 
 **xAmzContentSha256** | **String**|  | [optional] 
 **xAmzDate** | **String**|  | [optional] 
 **xAmzAlgorithm** | **String**|  | [optional] 
 **xAmzCredential** | **String**|  | [optional] 
 **xAmzSecurityToken** | **String**|  | [optional] 
 **xAmzSignature** | **String**|  | [optional] 
 **xAmzSignedHeaders** | **String**|  | [optional] 

### Return type

[**VerifyOTPMessageResponse**](VerifyOTPMessageResponse.md)

### Authorization

[hmac](../README.md#hmac)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

