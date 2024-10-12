# TwilioInsights.InsightsV1ConferenceApi

All URIs are relative to *https://insights.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchConference**](InsightsV1ConferenceApi.md#fetchConference) | **GET** /v1/Conferences/{ConferenceSid} | 
[**listConference**](InsightsV1ConferenceApi.md#listConference) | **GET** /v1/Conferences | 



## fetchConference

> InsightsV1Conference fetchConference(conferenceSid)



Get a specific Conference Summary.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1ConferenceApi();
let conferenceSid = "conferenceSid_example"; // String | The unique SID identifier of the Conference.
apiInstance.fetchConference(conferenceSid, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conferenceSid** | **String**| The unique SID identifier of the Conference. | 

### Return type

[**InsightsV1Conference**](InsightsV1Conference.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listConference

> ListConferenceResponse listConference(opts)



Get a list of Conference Summaries.

### Example

```javascript
import TwilioInsights from 'twilio_insights';
let defaultClient = TwilioInsights.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioInsights.InsightsV1ConferenceApi();
let opts = {
  'conferenceSid': "conferenceSid_example", // String | The SID of the conference.
  'friendlyName': "friendlyName_example", // String | Custom label for the conference resource, up to 64 characters.
  'status': "status_example", // String | Conference status.
  'createdAfter': "createdAfter_example", // String | Conferences created after the provided timestamp specified in ISO 8601 format
  'createdBefore': "createdBefore_example", // String | Conferences created before the provided timestamp specified in ISO 8601 format.
  'mixerRegion': "mixerRegion_example", // String | Twilio region where the conference media was mixed.
  'tags': "tags_example", // String | Tags applied by Twilio for common potential configuration, quality, or performance issues.
  'subaccount': "subaccount_example", // String | Account SID for the subaccount whose resources you wish to retrieve.
  'detectedIssues': "detectedIssues_example", // String | Potential configuration, behavior, or performance issues detected during the conference.
  'endReason': "endReason_example", // String | Conference end reason; e.g. last participant left, modified by API, etc.
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listConference(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conferenceSid** | **String**| The SID of the conference. | [optional] 
 **friendlyName** | **String**| Custom label for the conference resource, up to 64 characters. | [optional] 
 **status** | **String**| Conference status. | [optional] 
 **createdAfter** | **String**| Conferences created after the provided timestamp specified in ISO 8601 format | [optional] 
 **createdBefore** | **String**| Conferences created before the provided timestamp specified in ISO 8601 format. | [optional] 
 **mixerRegion** | **String**| Twilio region where the conference media was mixed. | [optional] 
 **tags** | **String**| Tags applied by Twilio for common potential configuration, quality, or performance issues. | [optional] 
 **subaccount** | **String**| Account SID for the subaccount whose resources you wish to retrieve. | [optional] 
 **detectedIssues** | **String**| Potential configuration, behavior, or performance issues detected during the conference. | [optional] 
 **endReason** | **String**| Conference end reason; e.g. last participant left, modified by API, etc. | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListConferenceResponse**](ListConferenceResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

