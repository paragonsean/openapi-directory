# ChecksApi.BehaviorApi

All URIs are relative to *https://api.truora.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reportBehavior**](BehaviorApi.md#reportBehavior) | **POST** /v1/behavior | Report Behavior



## reportBehavior

> BehaviourOutput reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, opts)

Report Behavior

Creates a behavior item to report employee conducts that do not or might not be included in their background check. This report includes both possitive and negative behaviors and sorts them by severity.  ### Reasons to report a person  &lt;table&gt;   &lt;tr&gt;     &lt;td style&#x3D;\&quot;width: 100px\&quot;&gt;&lt;center&gt;&lt;b&gt;Very High&lt;/b&gt;&lt;br&gt;(Score: 1)&lt;/td&gt;     &lt;td&gt;Rape, Drug Dealing, Sexual Harassment&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;High&lt;/b&gt;&lt;br&gt;(Score: 0.8)&lt;/td&gt;     &lt;td&gt;Theft, Fights, Aggressive Behaviour, Identity Fraud, Drunk, Drug Possession&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Medium&lt;/b&gt;&lt;br&gt;(Score: 0.6)&lt;/td&gt;     &lt;td&gt;Absences&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Low&lt;/b&gt;&lt;br&gt;(Score: 0.4)&lt;/td&gt;     &lt;td&gt;Tardiness, Confidentiality Breach&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;None&lt;/b&gt;&lt;br&gt;(Score: 0)&lt;/td&gt;     &lt;td&gt;Good Reputation&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;&lt;center&gt;&lt;b&gt;Unknown&lt;/b&gt;&lt;/td&gt;     &lt;td&gt;No information&lt;/td&gt;   &lt;/tr&gt; &lt;/table&gt;  **NOTE:** If the reason of your report is not here, please contact Truora support team. 

### Example

```javascript
import ChecksApi from 'checks_api';
let defaultClient = ChecksApi.ApiClient.instance;
// Configure API key authorization: api-key
let api-key = defaultClient.authentications['api-key'];
api-key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//api-key.apiKeyPrefix = 'Token';

let apiInstance = new ChecksApi.BehaviorApi();
let birthDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Birth date of reported person
let country = "country_example"; // String | Document country
let documentId = "documentId_example"; // String | Person document ID
let documentType = "documentType_example"; // String | Document type associated with the background check
let email = "email_example"; // String | Reported person e-mail
let feedbackDate = new Date("2013-10-20T19:20:30+01:00"); // Date | Behavior report date
let firstName = "firstName_example"; // String | Person first name
let lastName = "lastName_example"; // String | Person last name
let reason = "reason_example"; // String | Report reason
let opts = {
  'phoneNumber': "phoneNumber_example" // String | Phone number of the reported person
};
apiInstance.reportBehavior(birthDate, country, documentId, documentType, email, feedbackDate, firstName, lastName, reason, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **birthDate** | **Date**| Birth date of reported person | 
 **country** | **String**| Document country | 
 **documentId** | **String**| Person document ID | 
 **documentType** | **String**| Document type associated with the background check | 
 **email** | **String**| Reported person e-mail | 
 **feedbackDate** | **Date**| Behavior report date | 
 **firstName** | **String**| Person first name | 
 **lastName** | **String**| Person last name | 
 **reason** | **String**| Report reason | 
 **phoneNumber** | **String**| Phone number of the reported person | [optional] 

### Return type

[**BehaviourOutput**](BehaviourOutput.md)

### Authorization

[api-key](../README.md#api-key)

### HTTP request headers

- **Content-Type**: application/x-www-form-urlencoded
- **Accept**: application/json

