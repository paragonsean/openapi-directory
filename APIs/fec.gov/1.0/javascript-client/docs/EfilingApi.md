# OpenFec.EfilingApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**efileFilingsGet**](EfilingApi.md#efileFilingsGet) | **GET** /efile/filings/ | 
[**efileReportsHouseSenateGet**](EfilingApi.md#efileReportsHouseSenateGet) | **GET** /efile/reports/house-senate/ | 
[**efileReportsPacPartyGet**](EfilingApi.md#efileReportsPacPartyGet) | **GET** /efile/reports/pac-party/ | 
[**efileReportsPresidentialGet**](EfilingApi.md#efileReportsPresidentialGet) | **GET** /efile/reports/presidential/ | 



## efileFilingsGet

> EFilingsPage efileFilingsGet(apiKey, opts)



Basic information about electronic files coming into the FEC, posted as they are received.

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

let apiInstance = new OpenFec.EfilingApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'qFiler': ["null"] // [String] |  Keyword search for filer name or ID 
};
apiInstance.efileFilingsGet(apiKey, opts, (error, data, response) => {
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
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 

### Return type

[**EFilingsPage**](EFilingsPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## efileReportsHouseSenateGet

> BaseF3FilingPage efileReportsHouseSenateGet(apiKey, opts)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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

let apiInstance = new OpenFec.EfilingApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'qFiler': ["null"] // [String] |  Keyword search for filer name or ID 
};
apiInstance.efileReportsHouseSenateGet(apiKey, opts, (error, data, response) => {
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
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 

### Return type

[**BaseF3FilingPage**](BaseF3FilingPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## efileReportsPacPartyGet

> BaseF3XFilingPage efileReportsPacPartyGet(apiKey, opts)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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

let apiInstance = new OpenFec.EfilingApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'qFiler': ["null"] // [String] |  Keyword search for filer name or ID 
};
apiInstance.efileReportsPacPartyGet(apiKey, opts, (error, data, response) => {
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
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 

### Return type

[**BaseF3XFilingPage**](BaseF3XFilingPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## efileReportsPresidentialGet

> BaseF3PFilingPage efileReportsPresidentialGet(apiKey, opts)



 Key financial data reported periodically by committees as they are reported. This feed includes summary information from the the House F3 reports, the presidential F3p reports and the PAC and party F3x reports.  Generally, committees file reports on a quarterly or monthly basis, but some must also submit a report 12 days before primary elections. Therefore, during the primary season, the period covered by this file may be different for different committees. These totals also incorporate any changes made by committees, if any report covering the period is amended.  DISCLAIMER: The field labels contained within this resource are subject to change.  We are attempting to succinctly label these fields while conveying clear meaning to ensure accessibility for all users. 

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

let apiInstance = new OpenFec.EfilingApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'maxReceiptDate': new Date("2013-10-20"), // Date |  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'fileNumber': [null], // [Number] | Filing ID number
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-receipt_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'qFiler': ["null"] // [String] |  Keyword search for filer name or ID 
};
apiInstance.efileReportsPresidentialGet(apiKey, opts, (error, data, response) => {
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
 **minReceiptDate** | **Date**|  Selects all filings received after this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **maxReceiptDate** | **Date**|  Selects all filings received before this date(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **fileNumber** | [**[Number]**](Number.md)| Filing ID number | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-receipt_date&#39;]
 **qFiler** | [**[String]**](String.md)|  Keyword search for filer name or ID  | [optional] 

### Return type

[**BaseF3PFilingPage**](BaseF3PFilingPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

