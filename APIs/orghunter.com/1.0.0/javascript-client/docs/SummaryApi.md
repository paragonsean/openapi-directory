# OrgHunter.SummaryApi

All URIs are relative to *http://data.orghunter.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getSummary**](SummaryApi.md#getSummary) | **POST** /v1/charitysearch | Get summary data!



## getSummary

> getSummary(opts)

Get summary data!

&lt;p&gt;This operation provides summary data.&lt;/p&gt;

### Example

```javascript
import OrgHunter from 'org_hunter';
let defaultClient = OrgHunter.ApiClient.instance;
// Configure API key authorization: user_key
let user_key = defaultClient.authentications['user_key'];
user_key.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//user_key.apiKeyPrefix = 'Token';

let apiInstance = new OrgHunter.SummaryApi();
let opts = {
  'ein': "ein_example", // String | Employer Identification Number (EIN)
  'searchTerm': "searchTerm_example", // String | Charity Name or Keyword. Example: humane society or cancer
  'city': "city_example", // String | City Name. Example: Miami
  'state': "state_example", // String | State Name - Two letter state abbreviation
  'zipCode': "zipCode_example", // String | Zipcode Value - 5 digit zipcode value
  'category': "category_example", // String | Category Value Selected from Categories API
  'eligible': "eligible_example", // String | eligible=1 will return only organizations that are tax deductible and in good standing with the IRS
  'start': "start_example", // String | Record Set Start Position
  'rows': "rows_example" // String | Records Per Page. Default Value = 20
};
apiInstance.getSummary(opts, (error, data, response) => {
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
 **ein** | **String**| Employer Identification Number (EIN) | [optional] 
 **searchTerm** | **String**| Charity Name or Keyword. Example: humane society or cancer | [optional] 
 **city** | **String**| City Name. Example: Miami | [optional] 
 **state** | **String**| State Name - Two letter state abbreviation | [optional] 
 **zipCode** | **String**| Zipcode Value - 5 digit zipcode value | [optional] 
 **category** | **String**| Category Value Selected from Categories API | [optional] 
 **eligible** | **String**| eligible&#x3D;1 will return only organizations that are tax deductible and in good standing with the IRS | [optional] 
 **start** | **String**| Record Set Start Position | [optional] 
 **rows** | **String**| Records Per Page. Default Value &#x3D; 20 | [optional] 

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

