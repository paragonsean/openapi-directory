# FitbitPlusApi.EmailHistoryApi

All URIs are relative to *https://api.twinehealth.com/pub*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fetchEmailHistories**](EmailHistoryApi.md#fetchEmailHistories) | **GET** /email_history | List email histories
[**fetchEmailHistory**](EmailHistoryApi.md#fetchEmailHistory) | **GET** /email_history/{id} | Get an email history



## fetchEmailHistories

> FetchEmailHistoriesResponse fetchEmailHistories(opts)

List email histories

Get a list of email histories

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.EmailHistoryApi();
let opts = {
  'filterReceiver': "filterReceiver_example", // String | Fitbit Plus user id of email recipient. Required if filter[sender] is not defined.
  'filterSender': "filterSender_example", // String | Fitbit Plus user id of email sender. Required if filter[receiver] is not defined.
  'filterEmailType': "filterEmailType_example", // String | Type of email
  'sort': "sort_example" // String | valid sorts:   * send_time - ascending by send_time   * -send_time - descending by send_time 
};
apiInstance.fetchEmailHistories(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filterReceiver** | **String**| Fitbit Plus user id of email recipient. Required if filter[sender] is not defined. | [optional] 
 **filterSender** | **String**| Fitbit Plus user id of email sender. Required if filter[receiver] is not defined. | [optional] 
 **filterEmailType** | **String**| Type of email | [optional] 
 **sort** | **String**| valid sorts:   * send_time - ascending by send_time   * -send_time - descending by send_time  | [optional] 

### Return type

[**FetchEmailHistoriesResponse**](FetchEmailHistoriesResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json


## fetchEmailHistory

> FetchEmailHistoryResponse fetchEmailHistory(id)

Get an email history

Get an email history by id

### Example

```javascript
import FitbitPlusApi from 'fitbit_plus_api';

let apiInstance = new FitbitPlusApi.EmailHistoryApi();
let id = "id_example"; // String | Email history identifier
apiInstance.fetchEmailHistory(id, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **String**| Email history identifier | 

### Return type

[**FetchEmailHistoryResponse**](FetchEmailHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/vnd.api+json

