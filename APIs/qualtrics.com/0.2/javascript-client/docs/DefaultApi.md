# QualtricsApi.DefaultApi

All URIs are relative to *https://fra1.qualtrics.com/API/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createContactInMailinglist**](DefaultApi.md#createContactInMailinglist) | **POST** /directories/{DirectoryId}/mailinglists/{MailingListId}/contacts | Create contact in mailing list
[**generateDistributionLinks**](DefaultApi.md#generateDistributionLinks) | **POST** /distributions | Generate distribution links
[**getDistributions**](DefaultApi.md#getDistributions) | **GET** /distributions | Get distributions for survey
[**getEventSubscriptions**](DefaultApi.md#getEventSubscriptions) | **GET** /eventsubscriptions/{SubscriptionId} | Get event subscriptions
[**getSurvey**](DefaultApi.md#getSurvey) | **GET** /survey-definitions/{SurveyId} | Get survey
[**retrievedistributionlinks**](DefaultApi.md#retrievedistributionlinks) | **GET** /distributions/{DistributionId}/links | Retrieve distribution links
[**webhookDelete**](DefaultApi.md#webhookDelete) | **DELETE** /eventsubscriptions/ | Remove subscription to response event
[**whenAResponseIsReceived**](DefaultApi.md#whenAResponseIsReceived) | **POST** /eventsubscriptions/ | Triggers when a response is submitted to a qualtrics survey



## createContactInMailinglist

> createContactInMailinglist(directoryId, mailingListId, createContactInMailingList)

Create contact in mailing list

Creates a contact in a given mailing list

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let directoryId = "directoryId_example"; // String | ID of the qualtrics directory to create the contact to
let mailingListId = "mailingListId_example"; // String | ID of the mailing list
let createContactInMailingList = new QualtricsApi.CreateContactInMailingList(); // CreateContactInMailingList | Contact data
apiInstance.createContactInMailinglist(directoryId, mailingListId, createContactInMailingList, (error, data, response) => {
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
 **directoryId** | **String**| ID of the qualtrics directory to create the contact to | 
 **mailingListId** | **String**| ID of the mailing list | 
 **createContactInMailingList** | [**CreateContactInMailingList**](CreateContactInMailingList.md)| Contact data | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## generateDistributionLinks

> generateDistributionLinks(createDistributionLinks)

Generate distribution links

Geneates links for individual distribution

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let createDistributionLinks = new QualtricsApi.CreateDistributionLinks(); // CreateDistributionLinks | Parameters for the link generation
apiInstance.generateDistributionLinks(createDistributionLinks, (error, data, response) => {
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
 **createDistributionLinks** | [**CreateDistributionLinks**](CreateDistributionLinks.md)| Parameters for the link generation | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## getDistributions

> DistributionsResponse getDistributions(surveyId)

Get distributions for survey

Gets all distributions for a given survey

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let surveyId = "surveyId_example"; // String | The survey for which to load the distributions
apiInstance.getDistributions(surveyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | **String**| The survey for which to load the distributions | 

### Return type

[**DistributionsResponse**](DistributionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getEventSubscriptions

> EventSubscriptionsResponse getEventSubscriptions(subscriptionId)

Get event subscriptions

Get event subscriptions

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let subscriptionId = "subscriptionId_example"; // String | ID of event subscription - can be obtained from web hook response
apiInstance.getEventSubscriptions(subscriptionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriptionId** | **String**| ID of event subscription - can be obtained from web hook response | 

### Return type

[**EventSubscriptionsResponse**](EventSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getSurvey

> Object getSurvey(surveyId)

Get survey

Gets a single Qualtrics survey speficied by its ID

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let surveyId = "surveyId_example"; // String | ID of survey (eg. SV_123)
apiInstance.getSurvey(surveyId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | **String**| ID of survey (eg. SV_123) | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## retrievedistributionlinks

> RetrieveDistributionLinksResponse retrievedistributionlinks(surveyId, distributionId)

Retrieve distribution links

Retrieves all the individual links for a given distribution

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let surveyId = "surveyId_example"; // String | ID of the survey (eg: SV_123)
let distributionId = "distributionId_example"; // String | ID of the distribution list
apiInstance.retrievedistributionlinks(surveyId, distributionId, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **surveyId** | **String**| ID of the survey (eg: SV_123) | 
 **distributionId** | **String**| ID of the distribution list | 

### Return type

[**RetrieveDistributionLinksResponse**](RetrieveDistributionLinksResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## webhookDelete

> EventSubscriptionsResponse webhookDelete(subscribeToEventBody)

Remove subscription to response event

Remove event subscription

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let subscribeToEventBody = new QualtricsApi.SubscribeToEventBody(); // SubscribeToEventBody | This is the request body of the webhook
apiInstance.webhookDelete(subscribeToEventBody, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribeToEventBody** | [**SubscribeToEventBody**](SubscribeToEventBody.md)| This is the request body of the webhook | 

### Return type

[**EventSubscriptionsResponse**](EventSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## whenAResponseIsReceived

> EventSubscriptionsResponse whenAResponseIsReceived(subscribeToEventBody)

Triggers when a response is submitted to a qualtrics survey

Subscribe to response event

### Example

```javascript
import QualtricsApi from 'qualtrics_api';

let apiInstance = new QualtricsApi.DefaultApi();
let subscribeToEventBody = new QualtricsApi.SubscribeToEventBody(); // SubscribeToEventBody | This is the request body of the webhook
apiInstance.whenAResponseIsReceived(subscribeToEventBody, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscribeToEventBody** | [**SubscribeToEventBody**](SubscribeToEventBody.md)| This is the request body of the webhook | 

### Return type

[**EventSubscriptionsResponse**](EventSubscriptionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

