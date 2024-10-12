# OpenFec.DebtsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedulesScheduleDGet**](DebtsApi.md#schedulesScheduleDGet) | **GET** /schedules/schedule_d/ | 
[**schedulesScheduleDSubIdGet**](DebtsApi.md#schedulesScheduleDSubIdGet) | **GET** /schedules/schedule_d/{sub_id}/ | 



## schedulesScheduleDGet

> SchedulesScheduleDGetDefaultResponse schedulesScheduleDGet(apiKey, opts)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.   

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.DebtsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'maxPaymentPeriod': 3.4, // Number | 
  'minDate': new Date("2013-10-20"), // Date | Minimum load date
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'maxAmountOutstandingClose': 3.4, // Number | 
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'minPaymentPeriod': 3.4, // Number | 
  'minAmountIncurred': 3.4, // Number | 
  'creditorDebtorName': ["null"], // [String] | 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'candidateId': ["null"], // [String] |  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don't have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member's district changes during re-districting. Presidential IDs don't have districts. The rest is sequence. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'minAmountOutstandingBeginning': 3.4, // Number | 
  'sort': "'load_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'minAmountOutstandingClose': 3.4, // Number | 
  'natureOfDebt': "natureOfDebt_example", // String | 
  'maxAmountIncurred': 3.4, // Number | 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum load date
  'maxAmountOutstandingBeginning': 3.4 // Number | 
};
apiInstance.schedulesScheduleDGet(apiKey, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **maxPaymentPeriod** | **Number**|  | [optional] 
 **minDate** | **Date**| Minimum load date | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **maxAmountOutstandingClose** | **Number**|  | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **minPaymentPeriod** | **Number**|  | [optional] 
 **minAmountIncurred** | **Number**|  | [optional] 
 **creditorDebtorName** | [**[String]**](String.md)|  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **candidateId** | [**[String]**](String.md)|  A unique identifier assigned to each candidate registered with the FEC. If a person runs for several offices, that person will have separate candidate IDs for each office. First character indicates office - [P]residential, [H]ouse, [S]enate]. Second character is the last digit of the two-year period the ID was created. Third and fourth is the candidate state. Presidential IDs don&#39;t have state. Fifth and sixth is the district when the candidate first ran. This does not change if the candidate/member&#39;s district changes during re-districting. Presidential IDs don&#39;t have districts. The rest is sequence.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **minAmountOutstandingBeginning** | **Number**|  | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;load_date&#39;]
 **minAmountOutstandingClose** | **Number**|  | [optional] 
 **natureOfDebt** | **String**|  | [optional] 
 **maxAmountIncurred** | **Number**|  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum load date | [optional] 
 **maxAmountOutstandingBeginning** | **Number**|  | [optional] 

### Return type

[**SchedulesScheduleDGetDefaultResponse**](SchedulesScheduleDGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleDSubIdGet

> SchedulesScheduleDGetDefaultResponse schedulesScheduleDSubIdGet(apiKey, subId, opts)



 Schedule D, it shows debts and obligations owed to or by the committee that are required to be disclosed.   

### Example

```javascript
import OpenFec from 'open_fec';
let defaultClient = OpenFec.ApiClient.instance;
// Configure API key authorization: ApiKeyHeaderAuth
let ApiKeyHeaderAuth = defaultClient.authentications['ApiKeyHeaderAuth'];
ApiKeyHeaderAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyHeaderAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: ApiKeyQueryAuth
let ApiKeyQueryAuth = defaultClient.authentications['ApiKeyQueryAuth'];
ApiKeyQueryAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyQueryAuth.apiKeyPrefix = 'Token';
// Configure API key authorization: apiKey
let apiKey = defaultClient.authentications['apiKey'];
apiKey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apiKey.apiKeyPrefix = 'Token';

let apiInstance = new OpenFec.DebtsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let subId = "subId_example"; // String | 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "'load_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.schedulesScheduleDSubIdGet(apiKey, subId, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **subId** | **String**|  | 
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;load_date&#39;]
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**SchedulesScheduleDGetDefaultResponse**](SchedulesScheduleDGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

