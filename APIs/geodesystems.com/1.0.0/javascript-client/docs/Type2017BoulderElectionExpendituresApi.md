# GeodesystemsCom443.Type2017BoulderElectionExpendituresApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search2017BoulderElectionExpenditures**](Type2017BoulderElectionExpendituresApi.md#search2017BoulderElectionExpenditures) | **GET** /repository/search/type/2017_boulder_election_expenditures | Search API for &#39;2017 Boulder Election Expenditures&#39; entry type



## search2017BoulderElectionExpenditures

> search2017BoulderElectionExpenditures(opts)

Search API for &#39;2017 Boulder Election Expenditures&#39; entry type

API to search for entries of type 2017 Boulder Election Expenditures

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.Type2017BoulderElectionExpendituresApi();
let opts = {
  'text': "text_example", // String | Search text
  'name': "name_example", // String | Search name
  'description': "description_example", // String | Search description
  'fromdate': new Date("2013-10-20T19:20:30+01:00"), // Date | From date
  'todate': new Date("2013-10-20T19:20:30+01:00"), // Date | To date
  'createdateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date from
  'createdateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive create date to
  'changedateFrom': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date from
  'changedateTo': new Date("2013-10-20T19:20:30+01:00"), // Date | Archive change date to
  'group': "group_example", // String | Parent entry
  'filesuffix': "filesuffix_example", // String | File suffix
  'maxlatitude': 3.4, // Number | Northern bounds of search
  'minlongitude': 3.4, // Number | Western bounds of search
  'minlatitude': 3.4, // Number | Southern bounds of search
  'maxlongitude': 3.4, // Number | Eastern bounds of search
  'max': 56, // Number | Max number of results
  'skip': 56, // Number | Number to skip
  'searchDb2017BoulderElectionExpendituresCommittee': "searchDb2017BoulderElectionExpendituresCommittee_example", // String | Committee
  'searchDb2017BoulderElectionExpendituresTransactionDate': "searchDb2017BoulderElectionExpendituresTransactionDate_example", // String | Transaction Date
  'searchDb2017BoulderElectionExpendituresName': "searchDb2017BoulderElectionExpendituresName_example", // String | Name
  'searchDb2017BoulderElectionExpendituresStreet': "searchDb2017BoulderElectionExpendituresStreet_example", // String | Street
  'searchDb2017BoulderElectionExpendituresCity': "searchDb2017BoulderElectionExpendituresCity_example", // String | City
  'searchDb2017BoulderElectionExpendituresState': "searchDb2017BoulderElectionExpendituresState_example", // String | State
  'searchDb2017BoulderElectionExpendituresZip': "searchDb2017BoulderElectionExpendituresZip_example", // String | Zip
  'searchDb2017BoulderElectionExpendituresExpenditure': 3.4, // Number | Expenditure
  'searchDb2017BoulderElectionExpendituresPurpose': "searchDb2017BoulderElectionExpendituresPurpose_example" // String | Purpose
};
apiInstance.search2017BoulderElectionExpenditures(opts, (error, data, response) => {
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
 **text** | **String**| Search text | [optional] 
 **name** | **String**| Search name | [optional] 
 **description** | **String**| Search description | [optional] 
 **fromdate** | **Date**| From date | [optional] 
 **todate** | **Date**| To date | [optional] 
 **createdateFrom** | **Date**| Archive create date from | [optional] 
 **createdateTo** | **Date**| Archive create date to | [optional] 
 **changedateFrom** | **Date**| Archive change date from | [optional] 
 **changedateTo** | **Date**| Archive change date to | [optional] 
 **group** | **String**| Parent entry | [optional] 
 **filesuffix** | **String**| File suffix | [optional] 
 **maxlatitude** | **Number**| Northern bounds of search | [optional] 
 **minlongitude** | **Number**| Western bounds of search | [optional] 
 **minlatitude** | **Number**| Southern bounds of search | [optional] 
 **maxlongitude** | **Number**| Eastern bounds of search | [optional] 
 **max** | **Number**| Max number of results | [optional] 
 **skip** | **Number**| Number to skip | [optional] 
 **searchDb2017BoulderElectionExpendituresCommittee** | **String**| Committee | [optional] 
 **searchDb2017BoulderElectionExpendituresTransactionDate** | **String**| Transaction Date | [optional] 
 **searchDb2017BoulderElectionExpendituresName** | **String**| Name | [optional] 
 **searchDb2017BoulderElectionExpendituresStreet** | **String**| Street | [optional] 
 **searchDb2017BoulderElectionExpendituresCity** | **String**| City | [optional] 
 **searchDb2017BoulderElectionExpendituresState** | **String**| State | [optional] 
 **searchDb2017BoulderElectionExpendituresZip** | **String**| Zip | [optional] 
 **searchDb2017BoulderElectionExpendituresExpenditure** | **Number**| Expenditure | [optional] 
 **searchDb2017BoulderElectionExpendituresPurpose** | **String**| Purpose | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

