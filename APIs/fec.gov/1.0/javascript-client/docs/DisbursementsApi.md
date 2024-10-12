# OpenFec.DisbursementsApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**schedulesScheduleBByPurposeGet**](DisbursementsApi.md#schedulesScheduleBByPurposeGet) | **GET** /schedules/schedule_b/by_purpose/ | 
[**schedulesScheduleBByRecipientGet**](DisbursementsApi.md#schedulesScheduleBByRecipientGet) | **GET** /schedules/schedule_b/by_recipient/ | 
[**schedulesScheduleBByRecipientIdGet**](DisbursementsApi.md#schedulesScheduleBByRecipientIdGet) | **GET** /schedules/schedule_b/by_recipient_id/ | 
[**schedulesScheduleBEfileGet**](DisbursementsApi.md#schedulesScheduleBEfileGet) | **GET** /schedules/schedule_b/efile/ | 
[**schedulesScheduleBGet**](DisbursementsApi.md#schedulesScheduleBGet) | **GET** /schedules/schedule_b/ | 
[**schedulesScheduleBSubIdGet**](DisbursementsApi.md#schedulesScheduleBSubIdGet) | **GET** /schedules/schedule_b/{sub_id}/ | 



## schedulesScheduleBByPurposeGet

> ScheduleBByPurposePage schedulesScheduleBByPurposeGet(apiKey, opts)



 Schedule B disbursements aggregated by disbursement purpose category. To avoid double counting, memoed items are not included. Purpose is a combination of transaction codes, category codes and disbursement description. Inspect the &#x60;disbursement_purpose&#x60; sql function within the migrations for more details. 

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

let apiInstance = new OpenFec.DisbursementsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'purpose': ["null"], // [String] | Disbursement purpose category
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleBByPurposeGet(apiKey, opts, (error, data, response) => {
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
 **purpose** | [**[String]**](String.md)| Disbursement purpose category | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleBByPurposePage**](ScheduleBByPurposePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleBByRecipientGet

> ScheduleBByRecipientPage schedulesScheduleBByRecipientGet(apiKey, opts)



 Schedule B disbursements aggregated by recipient name. To avoid double counting, memoed items are not included. 

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

let apiInstance = new OpenFec.DisbursementsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'recipientName': ["null"], // [String] | Name of the entity receiving the disbursement
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleBByRecipientGet(apiKey, opts, (error, data, response) => {
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
 **recipientName** | [**[String]**](String.md)| Name of the entity receiving the disbursement | [optional] 
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleBByRecipientPage**](ScheduleBByRecipientPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleBByRecipientIdGet

> ScheduleBByRecipientIDPage schedulesScheduleBByRecipientIdGet(apiKey, opts)



 Schedule B disbursements aggregated by recipient committee ID, if applicable. To avoid double counting, memoed items are not included. 

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

let apiInstance = new OpenFec.DisbursementsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'cycle': [null], // [Number] |  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'recipientId': ["null"], // [String] | The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "sort_example" // String | Provide a field to sort by. Use `-` for descending order. 
};
apiInstance.schedulesScheduleBByRecipientIdGet(apiKey, opts, (error, data, response) => {
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
 **cycle** | [**[Number]**](Number.md)|  Filter records to only those that were applicable to a given two-year period.The cycle begins with an odd year and is named for its ending, even year.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **recipientId** | [**[String]**](String.md)| The FEC identifier should be represented here if the entity receiving the disbursement is registered with the FEC. | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] 

### Return type

[**ScheduleBByRecipientIDPage**](ScheduleBByRecipientIDPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleBEfileGet

> ScheduleBEfilePage schedulesScheduleBEfileGet(apiKey, opts)



 Efiling endpoints provide real-time campaign finance data received from electronic filers. Efiling endpoints only contain the most recent four months of data and don&#39;t contain the processed and coded data that you can find on other endpoints. 

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

let apiInstance = new OpenFec.DisbursementsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minDate': new Date("2013-10-20"), // Date | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
  'disbursementDescription': ["null"], // [String] | Description of disbursement
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'maxDate': new Date("2013-10-20"), // Date | When sorting by `disbursement_date`, this is populated with the         `disbursement_date` of the last result. However, you will need to pass the index         of that last result to `last_index` to get the next page.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'minAmount': "minAmount_example", // String | Filter for all amounts less than a value.
  'maxAmount': "maxAmount_example", // String | Filter for all amounts less than a value.
  'sort': "'-disbursement_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'recipientCity': ["null"], // [String] | City of recipient
  'recipientState': ["null"] // [String] | State of recipient
};
apiInstance.schedulesScheduleBEfileGet(apiKey, opts, (error, data, response) => {
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
 **minDate** | **Date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **disbursementDescription** | [**[String]**](String.md)| Description of disbursement | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **maxDate** | **Date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the         &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index         of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **minAmount** | **String**| Filter for all amounts less than a value. | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **recipientCity** | [**[String]**](String.md)| City of recipient | [optional] 
 **recipientState** | [**[String]**](String.md)| State of recipient | [optional] 

### Return type

[**ScheduleBEfilePage**](ScheduleBEfilePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleBGet

> ScheduleBPage schedulesScheduleBGet(apiKey, opts)



 Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called &#x60;two_year_transaction_period&#x60;, which is derived from the &#x60;report_year&#x60; submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;disbursement_date&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60; pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \&quot;230906248\&quot;,         last_disbursement_date: \&quot;2014-07-04\&quot;     } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;230906248&#x60; and &#x60;last_disbursement_date&#x3D;2014-07-04&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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

let apiInstance = new OpenFec.DisbursementsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minDate': new Date("2013-10-20"), // Date | Minimum date
  'spenderCommitteeDesignation': ["null"], // [String] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
  'recipientCommitteeId': ["null"], // [String] | The FEC identifier should be represented here if the contributor is registered with the FEC.
  'lastDisbursementDate': new Date("2013-10-20"), // Date | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'disbursementDescription': ["null"], // [String] | Description of disbursement
  'disbursementPurposeCategory': ["null"], // [String] | Disbursement purpose category
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'lastIndex': 56, // Number | Index of last result from previous page
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'minAmount': "minAmount_example", // String | Filter for all amounts greater than a value.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'lineNumber': "lineNumber_example", // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
  'sort': "'-disbursement_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'recipientCity': ["null"], // [String] | City of recipient
  'spenderCommitteeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'lastDisbursementAmount': 3.4, // Number | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page.
  'spenderCommitteeOrgType': ["null"], // [String] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
  'twoYearTransactionPeriod': [null], // [Number] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum date
  'recipientName': ["null"], // [String] | Name of the entity receiving the disbursement
  'maxAmount': "maxAmount_example", // String | Filter for all amounts less than a value.
  'recipientState': ["null"] // [String] | State of recipient
};
apiInstance.schedulesScheduleBGet(apiKey, opts, (error, data, response) => {
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
 **minDate** | **Date**| Minimum date | [optional] 
 **spenderCommitteeDesignation** | [**[String]**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **recipientCommitteeId** | [**[String]**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **lastDisbursementDate** | **Date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **disbursementDescription** | [**[String]**](String.md)| Description of disbursement | [optional] 
 **disbursementPurposeCategory** | [**[String]**](String.md)| Disbursement purpose category | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **lastIndex** | **Number**| Index of last result from previous page | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **recipientCity** | [**[String]**](String.md)| City of recipient | [optional] 
 **spenderCommitteeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **lastDisbursementAmount** | **Number**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **spenderCommitteeOrgType** | [**[String]**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **twoYearTransactionPeriod** | [**[Number]**](Number.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum date | [optional] 
 **recipientName** | [**[String]**](String.md)| Name of the entity receiving the disbursement | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 
 **recipientState** | [**[String]**](String.md)| State of recipient | [optional] 

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## schedulesScheduleBSubIdGet

> ScheduleBPage schedulesScheduleBSubIdGet(apiKey, subId, opts)



 Schedule B filings describe itemized disbursements. This data explains how committees and other filers spend their money. These figures are reported as part of forms F3, F3X and F3P.  The data is divided in two-year periods, called &#x60;two_year_transaction_period&#x60;, which is derived from the &#x60;report_year&#x60; submitted of the corresponding form. If no value is supplied, the results will default to the most recent two-year period that is named after the ending, even-numbered year.  Due to the large quantity of Schedule B filings, this endpoint is not paginated by page number. Instead, you can request the next page of results by adding the values in the &#x60;last_indexes&#x60; object from &#x60;pagination&#x60; to the URL of your last request. For example, when sorting by &#x60;disbursement_date&#x60;, you might receive a page of results with the following pagination information:  &#x60;&#x60;&#x60; pagination: {     pages: 965191,     per_page: 20,     count: 19303814,     last_indexes: {         last_index: \&quot;230906248\&quot;,         last_disbursement_date: \&quot;2014-07-04\&quot;     } } &#x60;&#x60;&#x60;  To fetch the next page of sorted results, append &#x60;last_index&#x3D;230906248&#x60; and &#x60;last_disbursement_date&#x3D;2014-07-04&#x60; to the URL.  We strongly advise paging through these results by using the sort indices (defaults to sort by disbursement date, e.g. &#x60;last_disbursement_date&#x60;), otherwise some resources may be unintentionally filtered out. This resource uses keyset pagination to improve query performance and these indices are required to properly page through this large dataset.  Note: because the Schedule B data includes many records, counts for large result sets are approximate; you will want to page through the records until no records are returned. 

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

let apiInstance = new OpenFec.DisbursementsApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let subId = "subId_example"; // String | 
let opts = {
  'minDate': new Date("2013-10-20"), // Date | Minimum date
  'spenderCommitteeDesignation': ["null"], // [String] | The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC 
  'recipientCommitteeId': ["null"], // [String] | The FEC identifier should be represented here if the contributor is registered with the FEC.
  'lastDisbursementDate': new Date("2013-10-20"), // Date | When sorting by `disbursement_date`, this is populated with the `disbursement_date` of the last result. However, you will need to pass the index of that last result to `last_index` to get the next page.
  'maxImageNumber': "maxImageNumber_example", // String | Maxium image number of the page where the schedule item is reported
  'disbursementDescription': ["null"], // [String] | Description of disbursement
  'disbursementPurposeCategory': ["null"], // [String] | Disbursement purpose category
  'minImageNumber': "minImageNumber_example", // String | Minium image number of the page where the schedule item is reported
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'lastIndex': 56, // Number | Index of last result from previous page
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'minAmount': "minAmount_example", // String | Filter for all amounts greater than a value.
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'lineNumber': "lineNumber_example", // String | Filter for form and line number using the following format: `FORM-LINENUMBER`.  For example an argument such as `F3X-16` would filter down to all entries from form `F3X` line number `16`.
  'sort': "'-disbursement_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'recipientCity': ["null"], // [String] | City of recipient
  'spenderCommitteeType': ["null"], // [String] | The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account 
  'lastDisbursementAmount': 3.4, // Number | When sorting by `disbursement_amount`, this is populated with the `disbursement_amount` of the last result.  However, you will need to pass the index of that last result to `last_index` to get the next page.
  'spenderCommitteeOrgType': ["null"], // [String] | The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock 
  'twoYearTransactionPeriod': [null], // [Number] |  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle. 
  'committeeId': ["null"], // [String] |  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id's begin with the letter C which is followed by eight digits. 
  'imageNumber': ["null"], // [String] |  An unique identifier for each page where the electronic or paper filing is reported. 
  'maxDate': new Date("2013-10-20"), // Date | Maximum date
  'recipientName': ["null"], // [String] | Name of the entity receiving the disbursement
  'maxAmount': "maxAmount_example", // String | Filter for all amounts less than a value.
  'recipientState': ["null"] // [String] | State of recipient
};
apiInstance.schedulesScheduleBSubIdGet(apiKey, subId, opts, (error, data, response) => {
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
 **minDate** | **Date**| Minimum date | [optional] 
 **spenderCommitteeDesignation** | [**[String]**](String.md)| The one-letter designation code of the organization:          - A authorized by a candidate          - J joint fundraising committee          - P principal campaign committee of a candidate          - U unauthorized          - B lobbyist/registrant PAC          - D leadership PAC  | [optional] 
 **recipientCommitteeId** | [**[String]**](String.md)| The FEC identifier should be represented here if the contributor is registered with the FEC. | [optional] 
 **lastDisbursementDate** | **Date**| When sorting by &#x60;disbursement_date&#x60;, this is populated with the &#x60;disbursement_date&#x60; of the last result. However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **maxImageNumber** | **String**| Maxium image number of the page where the schedule item is reported | [optional] 
 **disbursementDescription** | [**[String]**](String.md)| Description of disbursement | [optional] 
 **disbursementPurposeCategory** | [**[String]**](String.md)| Disbursement purpose category | [optional] 
 **minImageNumber** | **String**| Minium image number of the page where the schedule item is reported | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **lastIndex** | **Number**| Index of last result from previous page | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **minAmount** | **String**| Filter for all amounts greater than a value. | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **lineNumber** | **String**| Filter for form and line number using the following format: &#x60;FORM-LINENUMBER&#x60;.  For example an argument such as &#x60;F3X-16&#x60; would filter down to all entries from form &#x60;F3X&#x60; line number &#x60;16&#x60;. | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-disbursement_date&#39;]
 **recipientCity** | [**[String]**](String.md)| City of recipient | [optional] 
 **spenderCommitteeType** | [**[String]**](String.md)| The one-letter type code of the organization:         - C communication cost         - D delegate         - E electioneering communication         - H House         - I independent expenditure filer (not a committee)         - N PAC - nonqualified         - O independent expenditure-only (super PACs)         - P presidential         - Q PAC - qualified         - S Senate         - U single candidate independent expenditure         - V PAC with non-contribution account, nonqualified         - W PAC with non-contribution account, qualified         - X party, nonqualified         - Y party, qualified         - Z national party non-federal account  | [optional] 
 **lastDisbursementAmount** | **Number**| When sorting by &#x60;disbursement_amount&#x60;, this is populated with the &#x60;disbursement_amount&#x60; of the last result.  However, you will need to pass the index of that last result to &#x60;last_index&#x60; to get the next page. | [optional] 
 **spenderCommitteeOrgType** | [**[String]**](String.md)| The one-letter code for the kind for organization:         - C corporation         - L labor organization         - M membership organization         - T trade association         - V cooperative         - W corporation without capital stock  | [optional] 
 **twoYearTransactionPeriod** | [**[Number]**](Number.md)|  This is a two-year period that is derived from the year a transaction took place in the Itemized Schedule A and Schedule B tables. In cases where we have the date of the transaction (contribution_receipt_date in schedules/schedule_a, disbursement_date in schedules/schedule_b) the two_year_transaction_period is named after the ending, even-numbered year. If we do not have the date  of the transaction, we fall back to using the report year (report_year in both tables) instead,  making the same cycle adjustment as necessary. If no transaction year is specified, the results default to the most current cycle.  | [optional] 
 **committeeId** | [**[String]**](String.md)|  A unique identifier assigned to each committee or filer registered with the FEC. In general committee id&#39;s begin with the letter C which is followed by eight digits.  | [optional] 
 **imageNumber** | [**[String]**](String.md)|  An unique identifier for each page where the electronic or paper filing is reported.  | [optional] 
 **maxDate** | **Date**| Maximum date | [optional] 
 **recipientName** | [**[String]**](String.md)| Name of the entity receiving the disbursement | [optional] 
 **maxAmount** | **String**| Filter for all amounts less than a value. | [optional] 
 **recipientState** | [**[String]**](String.md)| State of recipient | [optional] 

### Return type

[**ScheduleBPage**](ScheduleBPage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

