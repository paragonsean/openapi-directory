# TwilioFlex.FlexV1InsightsQuestionnairesCategoryApi

All URIs are relative to *https://flex-api.twilio.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**createInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#createInsightsQuestionnairesCategory) | **POST** /v1/Insights/QualityManagement/Categories | 
[**deleteInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#deleteInsightsQuestionnairesCategory) | **DELETE** /v1/Insights/QualityManagement/Categories/{CategorySid} | 
[**listInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#listInsightsQuestionnairesCategory) | **GET** /v1/Insights/QualityManagement/Categories | 
[**updateInsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategoryApi.md#updateInsightsQuestionnairesCategory) | **POST** /v1/Insights/QualityManagement/Categories/{CategorySid} | 



## createInsightsQuestionnairesCategory

> FlexV1InsightsQuestionnairesCategory createInsightsQuestionnairesCategory(name, opts)



To create a category for Questions

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesCategoryApi();
let name = "name_example"; // String | The name of this category.
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.createInsightsQuestionnairesCategory(name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **String**| The name of this category. | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategory.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json


## deleteInsightsQuestionnairesCategory

> deleteInsightsQuestionnairesCategory(categorySid, opts)





### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesCategoryApi();
let categorySid = "categorySid_example"; // String | The SID of the category to be deleted
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.deleteInsightsQuestionnairesCategory(categorySid, opts, (error, data, response) => {
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
 **categorySid** | **String**| The SID of the category to be deleted | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

null (empty response body)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## listInsightsQuestionnairesCategory

> ListInsightsQuestionnairesCategoryResponse listInsightsQuestionnairesCategory(opts)



To get all the categories

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesCategoryApi();
let opts = {
  'authorization': "authorization_example", // String | The Authorization HTTP request header
  'pageSize': 56, // Number | How many resources to return in each list page. The default is 50, and the maximum is 1000.
  'page': 56, // Number | The page index. This value is simply for client state.
  'pageToken': "pageToken_example" // String | The page token. This is provided by the API.
};
apiInstance.listInsightsQuestionnairesCategory(opts, (error, data, response) => {
  if (error) {
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
 **pageSize** | **Number**| How many resources to return in each list page. The default is 50, and the maximum is 1000. | [optional] 
 **page** | **Number**| The page index. This value is simply for client state. | [optional] 
 **pageToken** | **String**| The page token. This is provided by the API. | [optional] 

### Return type

[**ListInsightsQuestionnairesCategoryResponse**](ListInsightsQuestionnairesCategoryResponse.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## updateInsightsQuestionnairesCategory

> FlexV1InsightsQuestionnairesCategory updateInsightsQuestionnairesCategory(categorySid, name, opts)



To update the category for Questions

### Example

```javascript
import TwilioFlex from 'twilio_flex';
let defaultClient = TwilioFlex.ApiClient.instance;
// Configure HTTP basic authorization: accountSid_authToken
let accountSid_authToken = defaultClient.authentications['accountSid_authToken'];
accountSid_authToken.username = 'YOUR USERNAME';
accountSid_authToken.password = 'YOUR PASSWORD';

let apiInstance = new TwilioFlex.FlexV1InsightsQuestionnairesCategoryApi();
let categorySid = "categorySid_example"; // String | The SID of the category to be updated
let name = "name_example"; // String | The name of this category.
let opts = {
  'authorization': "authorization_example" // String | The Authorization HTTP request header
};
apiInstance.updateInsightsQuestionnairesCategory(categorySid, name, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **categorySid** | **String**| The SID of the category to be updated | 
 **name** | **String**| The name of this category. | 
 **authorization** | **String**| The Authorization HTTP request header | [optional] 

### Return type

[**FlexV1InsightsQuestionnairesCategory**](FlexV1InsightsQuestionnairesCategory.md)

### Authorization

[accountSid_authToken](../README.md#accountSid_authToken)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

