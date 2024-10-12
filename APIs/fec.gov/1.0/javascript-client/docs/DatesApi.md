# OpenFec.DatesApi

All URIs are relative to */v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calendarDatesExportGet**](DatesApi.md#calendarDatesExportGet) | **GET** /calendar-dates/export/ | 
[**calendarDatesGet**](DatesApi.md#calendarDatesGet) | **GET** /calendar-dates/ | 
[**electionDatesGet**](DatesApi.md#electionDatesGet) | **GET** /election-dates/ | 
[**reportingDatesGet**](DatesApi.md#reportingDatesGet) | **GET** /reporting-dates/ | 



## calendarDatesExportGet

> CalendarDatePage calendarDatesExportGet(apiKey, opts)



 Returns CSV or ICS for downloading directly into calendar applications like Google, Outlook or other applications.  Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State filtering now applies to elections, reports and reporting periods.  Presidential pre-primary report due dates are not shown on even years. Filers generally opt to file monthly rather than submit over 50 pre-primary election reports. All reporting deadlines are available at /reporting-dates/ for reference.  This is [the sql function](https://github.com/fecgov/openFEC/blob/develop/data/migrations/V40__omnibus_dates.sql) that creates the calendar.  

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

let apiInstance = new OpenFec.DatesApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'calendarCategoryId': [null], // [Number] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
  'description': ["null"], // [String] | Brief description of event
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'maxEndDate': new Date("2013-10-20"), // Date |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
  'summary': ["null"], // [String] | Longer description of event
  'minEndDate': new Date("2013-10-20"), // Date |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'minStartDate': new Date("2013-10-20"), // Date |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'maxStartDate': new Date("2013-10-20"), // Date |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
  'renderer': "'ics'", // String | 
  'sort': "'-start_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'eventId': 56 // Number | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
};
apiInstance.calendarDatesExportGet(apiKey, opts, (error, data, response) => {
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
 **calendarCategoryId** | [**[Number]**](Number.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
 **description** | [**[String]**](String.md)| Brief description of event | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **maxEndDate** | **Date**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **summary** | [**[String]**](String.md)| Longer description of event | [optional] 
 **minEndDate** | **Date**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **minStartDate** | **Date**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **maxStartDate** | **Date**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **renderer** | **String**|  | [optional] [default to &#39;ics&#39;]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-start_date&#39;]
 **eventId** | **Number**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## calendarDatesGet

> CalendarDatePage calendarDatesGet(apiKey, opts)



 Combines the election and reporting dates with Commission meetings, conferences, outreach, Advisory Opinions, rules, litigation dates and other events into one calendar.  State and report type filtering is no longer available. 

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

let apiInstance = new OpenFec.DatesApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'calendarCategoryId': [null], // [Number] |  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29 
  'description': ["null"], // [String] | Brief description of event
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'maxEndDate': new Date("2013-10-20"), // Date |  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD) 
  'summary': ["null"], // [String] | Longer description of event
  'minEndDate': new Date("2013-10-20"), // Date |  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD) 
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'minStartDate': new Date("2013-10-20"), // Date |  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD) 
  'maxStartDate': new Date("2013-10-20"), // Date |  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD) 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sort': "'-start_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'eventId': 56 // Number | An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID.
};
apiInstance.calendarDatesGet(apiKey, opts, (error, data, response) => {
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
 **calendarCategoryId** | [**[Number]**](Number.md)|  Each type of event has a calendar category with an integer id. Options are: Open Meetings: 32, Executive Sessions: 39, Public Hearings: 40, Conferences: 33, Roundtables: 34, Election Dates: 36, Federal Holidays: 37, FEA Periods: 38, Commission Meetings: 20, Reporting Deadlines: 21, Conferences and Outreach: 22, AOs and Rules: 23, Other: 24, Quarterly: 25, Monthly: 26, Pre and Post-Elections: 27, EC Periods:28, and IE Periods: 29  | [optional] 
 **description** | [**[String]**](String.md)| Brief description of event | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **maxEndDate** | **Date**|  The maximum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **summary** | [**[String]**](String.md)| Longer description of event | [optional] 
 **minEndDate** | **Date**|  The minimum end date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **minStartDate** | **Date**|  The minimum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **maxStartDate** | **Date**|  The maximum start date.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-start_date&#39;]
 **eventId** | **Number**| An unique ID for an event. Useful for downloading a single event to your calendar. This ID is not a permanent, persistent ID. | [optional] 

### Return type

[**CalendarDatePage**](CalendarDatePage.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## electionDatesGet

> ElectionDatesGetDefaultResponse electionDatesGet(apiKey, opts)



 FEC election dates since 1995. 

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

let apiInstance = new OpenFec.DatesApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'electionState': ["null"], // [String] |  State or territory of the office sought. 
  'maxElectionDate': new Date("2013-10-20"), // Date |  The maximum date of election. 
  'electionDistrict': ["null"], // [String] |  House district of the office sought, if applicable. 
  'minUpdateDate': new Date("2013-10-20"), // Date |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'maxCreateDate': new Date("2013-10-20"), // Date |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'electionYear': ["null"], // [String] | Year of election
  'sort': "'-election_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'minCreateDate': new Date("2013-10-20"), // Date |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
  'electionParty': ["null"], // [String] |  Party, if applicable. 
  'officeSought': ["null"], // [String] |  House, Senate or presidential office. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'page': 1, // Number | For paginating through results, starting at page 1
  'maxUpdateDate': new Date("2013-10-20"), // Date |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
  'electionTypeId': ["null"], // [String] |  Election type id 
  'maxPrimaryGeneralDate': new Date("2013-10-20"), // Date |  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
  'minElectionDate': new Date("2013-10-20"), // Date |  The minimum date of election. 
  'minPrimaryGeneralDate': new Date("2013-10-20") // Date |  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD) 
};
apiInstance.electionDatesGet(apiKey, opts, (error, data, response) => {
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
 **electionState** | [**[String]**](String.md)|  State or territory of the office sought.  | [optional] 
 **maxElectionDate** | **Date**|  The maximum date of election.  | [optional] 
 **electionDistrict** | [**[String]**](String.md)|  House district of the office sought, if applicable.  | [optional] 
 **minUpdateDate** | **Date**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **maxCreateDate** | **Date**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **electionYear** | [**[String]**](String.md)| Year of election | [optional] 
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-election_date&#39;]
 **minCreateDate** | **Date**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **electionParty** | [**[String]**](String.md)|  Party, if applicable.  | [optional] 
 **officeSought** | [**[String]**](String.md)|  House, Senate or presidential office.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **maxUpdateDate** | **Date**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **electionTypeId** | [**[String]**](String.md)|  Election type id  | [optional] 
 **maxPrimaryGeneralDate** | **Date**|  The maximum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **minElectionDate** | **Date**|  The minimum date of election.  | [optional] 
 **minPrimaryGeneralDate** | **Date**|  The minimum date of primary or general election.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 

### Return type

[**ElectionDatesGetDefaultResponse**](ElectionDatesGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## reportingDatesGet

> ReportingDatesGetDefaultResponse reportingDatesGet(apiKey, opts)



 FEC election dates since 1995. 

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

let apiInstance = new OpenFec.DatesApi();
let apiKey = "'DEMO_KEY'"; // String |  API key for https://api.data.gov. Get one at https://api.data.gov/signup. 
let opts = {
  'minUpdateDate': new Date("2013-10-20"), // Date |  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
  'reportType': ["null"], // [String] | Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE) 
  'minDueDate': new Date("2013-10-20"), // Date |  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
  'sortNullOnly': false, // Boolean | Toggle that filters out all rows having sort column that is non-null
  'page': 1, // Number | For paginating through results, starting at page 1
  'maxDueDate': new Date("2013-10-20"), // Date |  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD) 
  'reportYear': [null], // [Number] |  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 
  'sortNullsLast': false, // Boolean | Toggle that sorts null values last
  'maxCreateDate': new Date("2013-10-20"), // Date |  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
  'maxUpdateDate': new Date("2013-10-20"), // Date |  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD) 
  'perPage': 20, // Number | The number of results returned per page. Defaults to 20.
  'sortHideNull': false, // Boolean | Hide null values on sorted column(s).
  'sort': "'-due_date'", // String | Provide a field to sort by. Use `-` for descending order. 
  'minCreateDate': new Date("2013-10-20") // Date |  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD) 
};
apiInstance.reportingDatesGet(apiKey, opts, (error, data, response) => {
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
 **minUpdateDate** | **Date**|  The minimum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **reportType** | [**[String]**](String.md)| Name of report where the underlying data comes from:     - 10D Pre-Election     - 10G Pre-General     - 10P Pre-Primary     - 10R Pre-Run-Off     - 10S Pre-Special     - 12C Pre-Convention     - 12G Pre-General     - 12P Pre-Primary     - 12R Pre-Run-Off     - 12S Pre-Special     - 30D Post-Election     - 30G Post-General     - 30P Post-Primary     - 30R Post-Run-Off     - 30S Post-Special     - 60D Post-Convention     - M1  January Monthly     - M10 October Monthly     - M11 November Monthly     - M12 December Monthly     - M2  February Monthly     - M3  March Monthly     - M4  April Monthly     - M5  May Monthly     - M6  June Monthly     - M7  July Monthly     - M8  August Monthly     - M9  September Monthly     - MY  Mid-Year Report     - Q1  April Quarterly     - Q2  July Quarterly     - Q3  October Quarterly     - TER Termination Report     - YE  Year-End     - ADJ COMP ADJUST AMEND     - CA  COMPREHENSIVE AMEND     - 90S Post Inaugural Supplement     - 90D Post Inaugural     - 48  48 Hour Notification     - 24  24 Hour Notification     - M7S July Monthly/Semi-Annual     - MSA Monthly Semi-Annual (MY)     - MYS Monthly Year End/Semi-Annual     - Q2S July Quarterly/Semi-Annual     - QSA Quarterly Semi-Annual (MY)     - QYS Quarterly Year End/Semi-Annual     - QYE Quarterly Semi-Annual (YE)     - QMS Quarterly Mid-Year/ Semi-Annual     - MSY Monthly Semi-Annual (YE)  | [optional] 
 **minDueDate** | **Date**|  The minimum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **sortNullOnly** | **Boolean**| Toggle that filters out all rows having sort column that is non-null | [optional] [default to false]
 **page** | **Number**| For paginating through results, starting at page 1 | [optional] [default to 1]
 **maxDueDate** | **Date**|  The maximum date the report is due.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **reportYear** | [**[Number]**](Number.md)|  Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date.  | [optional] 
 **sortNullsLast** | **Boolean**| Toggle that sorts null values last | [optional] [default to false]
 **maxCreateDate** | **Date**|  The maximum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **maxUpdateDate** | **Date**|  The maximum date this record was last updated.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 
 **perPage** | **Number**| The number of results returned per page. Defaults to 20. | [optional] [default to 20]
 **sortHideNull** | **Boolean**| Hide null values on sorted column(s). | [optional] [default to false]
 **sort** | **String**| Provide a field to sort by. Use &#x60;-&#x60; for descending order.  | [optional] [default to &#39;-due_date&#39;]
 **minCreateDate** | **Date**|  The minimum date this record was added to the system.(MM/DD/YYYY or YYYY-MM-DD)  | [optional] 

### Return type

[**ReportingDatesGetDefaultResponse**](ReportingDatesGetDefaultResponse.md)

### Authorization

[ApiKeyHeaderAuth](../README.md#ApiKeyHeaderAuth), [ApiKeyQueryAuth](../README.md#ApiKeyQueryAuth), [apiKey](../README.md#apiKey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

