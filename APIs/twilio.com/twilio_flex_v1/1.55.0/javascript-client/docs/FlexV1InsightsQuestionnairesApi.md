# TwilioFlex.FlexV1InsightsQuestionnairesApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#createInsightsQuestionnaires) | **POST** /v1/Insights/QualityManagement/Questionnaires | 
[**deleteInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#deleteInsightsQuestionnaires) | **DELETE** /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid} | 
[**fetchInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#fetchInsightsQuestionnaires) | **GET** /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid} | 
[**listInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#listInsightsQuestionnaires) | **GET** /v1/Insights/QualityManagement/Questionnaires | 
[**updateInsightsQuestionnaires**](FlexV1InsightsQuestionnairesApi.md#updateInsightsQuestionnaires) | **POST** /v1/Insights/QualityManagement/Questionnaires/{QuestionnaireSid} | 



## createInsightsQuestionnaires

> FlexV1InsightsQuestionnaires createInsightsQuestionnaires(name, opts)



To create a Questionnaire

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesApi();
let name = "name_example"; // String | The name of this questionnaire
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'active': true, // Boolean | The flag to enable or disable questionnaire
  'description': "description_example", // String | The description of this questionnaire
  'questionSids': ["null"] // [String] | The list of questions sids under a questionnaire
};
apiInstance.createInsightsQuestionnaires(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of this questionnaire | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 
 **active** | **Boolean**| The flag to enable or disable questionnaire | [optional] 
 **description** | **String**| The description of this questionnaire | [optional] 
 **questionSids** | [**[String]**](String.md)| The list of questions sids under a questionnaire | [optional] 

### Return type

[**FlexV1InsightsQuestionnaires**](FlexV1InsightsQuestionnaires.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteInsightsQuestionnaires

> deleteInsightsQuestionnaires(questionnaireSid, opts)



To delete the questionnaire

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesApi();
let questionnaireSid = "questionnaireSid_example"; // String | The SID of the questionnaire
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.deleteInsightsQuestionnaires(questionnaireSid, opts, (error, data, response) => {
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
 **questionnaireSid** | **String**| The SID of the questionnaire | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## fetchInsightsQuestionnaires

> FlexV1InsightsQuestionnaires fetchInsightsQuestionnaires(questionnaireSid, opts)



To get the Questionnaire Detail

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesApi();
let questionnaireSid = "questionnaireSid_example"; // String | The SID of the questionnaire
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.fetchInsightsQuestionnaires(questionnaireSid, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaireSid** | **String**| The SID of the questionnaire | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsQuestionnaires**](FlexV1InsightsQuestionnaires.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listInsightsQuestionnaires

> ListInsightsQuestionnairesResponse listInsightsQuestionnaires(opts)



To get all questionnaires with questions

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesApi();
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'includeInactive': true, // Boolean | Flag indicating whether to include inactive questionnaires or not
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInsightsQuestionnaires(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **String**| The Authorization HTTP request header | [optional] 
 **includeInactive** | **Boolean**| Flag indicating whether to include inactive questionnaires or not | [optional] 
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInsightsQuestionnairesResponse**](ListInsightsQuestionnairesResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInsightsQuestionnaires

> FlexV1InsightsQuestionnaires updateInsightsQuestionnaires(questionnaireSid, active, opts)



To update the questionnaire

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesApi();
let questionnaireSid = "questionnaireSid_example"; // String | The SID of the questionnaire
let active = true; // Boolean | The flag to enable or disable questionnaire
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'description': "description_example", // String | The description of this questionnaire
  'name': "name_example", // String | The name of this questionnaire
  'questionSids': ["null"] // [String] | The list of questions sids under a questionnaire
};
apiInstance.updateInsightsQuestionnaires(questionnaireSid, active, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **questionnaireSid** | **String**| The SID of the questionnaire | 
 **active** | **Boolean**| The flag to enable or disable questionnaire | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 
 **description** | **String**| The description of this questionnaire | [optional] 
 **name** | **String**| The name of this questionnaire | [optional] 
 **questionSids** | [**[String]**](String.md)| The list of questions sids under a questionnaire | [optional] 

### Return type

[**FlexV1InsightsQuestionnaires**](FlexV1InsightsQuestionnaires.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

