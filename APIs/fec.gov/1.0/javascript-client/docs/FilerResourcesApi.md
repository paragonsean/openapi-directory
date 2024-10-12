# OpenFec.FilerResourcesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**radAnalystGet**](FilerResourcesApi.md#radAnalystGet) | **GET** /rad-analyst/ | 
[**stateElectionOfficeGet**](FilerResourcesApi.md#stateElectionOfficeGet) | **GET** /state-election-office/ | 



## radAnalystGet

> RadAnalystPage radAnalystGet(apiKey, opts)



 Use this endpoint to look up the RAD Analyst for a committee.  The mission of the Reports Analysis Division (RAD) is to ensure that campaigns and political committees file timely and accurate reports that fully disclose their financial activities.  RAD is responsible for reviewing statements and financial reports filed by political committees participating in federal elections, providing assistance and guidance to the committees to properly file their reports, and for taking appropriate action to ensure compliance with the Federal Election Campaign Act (FECA). 

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

let apiInstance = new OpenFec.FilerResourcesApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minAssignmentUpdateDate': new Date("2013-10-20"), // Date | Filter results for assignment updates made after this date
  'telephoneExt': [null], // [Number] | Telephone extension of RAD analyst
  'analystId': [null], // [Number] | ID of RAD analyst
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'name': ["null"], // [String] | Name of RAD analyst
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'email': ["null"], // [String] | Email of RAD analyst
  'title': ["null"], // [String] | Title of RAD analyst
  'sort': "sort_example", // String | Provide a field to sort by. Use `-` for descending order. 
  'maxAssignmentUpdateDate': new Date("2013-10-20"), // Date | Filter results for assignment updates made before this date
  'analystShortId': [null] // [Number] | Short ID of RAD analyst
};
apiInstance.radAnalystGet(apiKey, opts, (error, data, response) => {
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
 **minAssignmentUpdateDate** | **Date**| Filter results for assignment updates made after this date | [optional] 
 **telephoneExt** | [**[Number]**](Number.md)| Telephone extension of RAD analyst | [optional] 
 **analystId** | [**[Number]**](Number.md)| ID of RAD analyst | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **name** | [**[String]**](String.md)| Name of RAD analyst | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **email** | [**[String]**](String.md)| Email of RAD analyst | [optional] 
 **title** | [**[String]**](String.md)| Title of RAD analyst | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **maxAssignmentUpdateDate** | **Date**| Filter results for assignment updates made before this date | [optional] 
 **analystShortId** | [**[Number]**](Number.md)| Short ID of RAD analyst | [optional] 

### Return type

[**RadAnalystPage**](RadAnalystPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## stateElectionOfficeGet

> StateElectionOfficeInfoPage stateElectionOfficeGet(state, apiKey, opts)



 State laws and procedures govern elections for state or local offices as well as how candidates appear on election ballots. Contact the appropriate state election office for more information. 

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

let apiInstance = new OpenFec.FilerResourcesApi();
let state = "state_example"; // String |  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.  
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'page': 1, // Number | For paginating through results, starting at page 1
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sort': "sort_example", // String | Provide a field to sort by. Use `-` for descending order. 
  'sortNullsLast': false // Boolean | Toggle that sorts null values last
};
apiInstance.stateElectionOfficeGet(state, apiKey, opts, (error, data, response) => {
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
 **state** | **String**|  Enter a state (Ex: AK, TX, VA etc..) to find the local election offices contact information.   | 
 **apiKey** | **String**|  API key for https://api.data.gov. Get one at https://api.data.gov/signup.  | [default to &#39;DEMO_KEY&#39;]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]

### Return type

[**StateElectionOfficeInfoPage**](StateElectionOfficeInfoPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

