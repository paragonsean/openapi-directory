# CallControlApi.ReputationApi

All URIs are relative to *https://api.callcontrol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reputationReport**](ReputationApi.md#reputationReport) | **POST** /api/2015-11-01/Report | Report: report spam calls received to better tune our algorithms based upon spam calls you receive
[**reputationReputation**](ReputationApi.md#reputationReputation) | **GET** /api/2015-11-01/Reputation/{phoneNumber} | Reputation:  Premium service which returns a reputation informaiton of a phone number via API.



## reputationReport

> reputationReport(callReport)

Report: report spam calls received to better tune our algorithms based upon spam calls you receive

This returns information required to perform basic call blocking behaviors&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example

```javascript
import CallControlApi from 'call_control_api';

let apiInstance = new CallControlApi.ReputationApi();
let callReport = new CallControlApi.CallReport(); // CallReport | [FromBody] Call Report              PhoneNumber,               Caller name(optional),               Call category(optional),               Comment or tags(free text) (optional),               Unwanted call  - yes/no(optional),
apiInstance.reputationReport(callReport, (error, data, response) => {
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
 **callReport** | [**CallReport**](CallReport.md)| [FromBody] Call Report              PhoneNumber,               Caller name(optional),               Call category(optional),               Comment or tags(free text) (optional),               Unwanted call  - yes/no(optional), | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json, text/json
- **Accept**: Not defined


## reputationReputation

> Reputation reputationReputation(phoneNumber)

Reputation:  Premium service which returns a reputation informaiton of a phone number via API.

This returns information required to perform basic call blocking behaviors&lt;br /&gt;              Try with api_key &#39;demo&#39; and phone numbers 18008472911, 13157244022, 17275567300, 18008276655, and 12061231234 (last one not spam)

### Example

```javascript
import CallControlApi from 'call_control_api';

let apiInstance = new CallControlApi.ReputationApi();
let phoneNumber = "phoneNumber_example"; // String | phone number to search
apiInstance.reputationReputation(phoneNumber, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **phoneNumber** | **String**| phone number to search | 

### Return type

[**Reputation**](Reputation.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json

