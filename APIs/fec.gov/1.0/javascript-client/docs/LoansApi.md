# OpenFec.LoansApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedulesScheduleCGet**](LoansApi.md#schedulesScheduleCGet) | **GET** /schedules/schedule_c/ | 
[**schedulesScheduleCSubIdGet**](LoansApi.md#schedulesScheduleCSubIdGet) | **GET** /schedules/schedule_c/{sub_id}/ | 



## schedulesScheduleCGet

> SchedulesScheduleCGetDefaultResponse schedulesScheduleCGet(apiKey, opts)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

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

let apiInstance = new OpenFec.LoansApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minPaymentToDate': 56, // Number |  Minimum payment to date 
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'maxIncurredDate': new Date("2013-10-20"), // Date |  Maximum incurred date 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'lastIndex': 56, // Number | Index of last result from previous page
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'minAmount': "minAmount_example", // String |  Filter for all amounts greater than a value. 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'loanSourceName': ["null"], // [String] | Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate
  'lineNumber': "lineNumber_example", // String |  Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`. 
  'sort': "'-incurred_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'maxPaymentToDate': 56, // Number |  Maximum payment to date 
  'candidateName': ["null"], // [String] | Name of candidate running for office
  'sortNullsLast': true, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'minIncurredDate': new Date("2013-10-20"), // Date |  Minimum incurred date 
  'maxAmount': "maxAmount_example" // String |  Filter for all amounts less than a value. 
};
apiInstance.schedulesScheduleCGet(apiKey, opts, (error, data, response) => {
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
 **minPaymentToDate** | **Number**|  Minimum payment to date  | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **maxIncurredDate** | **Date**|  Maximum incurred date  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **lastIndex** | **Number**| Index of last result from previous page | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **minAmount** | **String**|  Filter for all amounts greater than a value.  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **loanSourceName** | [**[String]**](String.md)| Source of the loan (i.e., bank loan, brokerage account, credit card, home equity line of credit,               other line of credit, or personal funds of the candidate | [optional] 
 **lineNumber** | **String**|  Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;.  | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-incurred_date&#39;]
 **maxPaymentToDate** | **Number**|  Maximum payment to date  | [optional] 
 **candidateName** | [**[String]**](String.md)| Name of candidate running for office | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to true]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **minIncurredDate** | **Date**|  Minimum incurred date  | [optional] 
 **maxAmount** | **String**|  Filter for all amounts less than a value.  | [optional] 

### Return type

[**SchedulesScheduleCGetDefaultResponse**](SchedulesScheduleCGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleCSubIdGet

> SchedulesScheduleCGetDefaultResponse schedulesScheduleCSubIdGet(apiKey, subId, opts)



 Schedule C shows all loans, endorsements and loan guarantees a committee receives or makes.  The committee continues to report the loan until it is repaid. 

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

let apiInstance = new OpenFec.LoansApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let subId = "subId_example"; // String | 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "sort_example", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.schedulesScheduleCSubIdGet(apiKey, subId, opts, (error, data, response) => {
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
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**SchedulesScheduleCGetDefaultResponse**](SchedulesScheduleCGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

