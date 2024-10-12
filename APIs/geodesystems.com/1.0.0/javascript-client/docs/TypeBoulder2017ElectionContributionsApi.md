# GeodesystemsCom443.TypeBoulder2017ElectionContributionsApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBoulder2017ElectionContributions**](TypeBoulder2017ElectionContributionsApi.md#searchBoulder2017ElectionContributions) | **GET** /repository/search/type/boulder_2017_election_contributions | Search API for &#39;Boulder 2017 Election Contributions&#39; entry type



## searchBoulder2017ElectionContributions

> searchBoulder2017ElectionContributions(opts)

Search API for &#39;Boulder 2017 Election Contributions&#39; entry type

API to search for entries of type Boulder 2017 Election Contributions

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeBoulder2017ElectionContributionsApi();
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
  'searchDbBoulder2017ElectionContributionsCommittee': "searchDbBoulder2017ElectionContributionsCommittee_example", // String | Committee
  'searchDbBoulder2017ElectionContributionsLastName': "searchDbBoulder2017ElectionContributionsLastName_example", // String | Last Name
  'searchDbBoulder2017ElectionContributionsFirstName': "searchDbBoulder2017ElectionContributionsFirstName_example", // String | First Name
  'searchDbBoulder2017ElectionContributionsStreet': "searchDbBoulder2017ElectionContributionsStreet_example", // String | Street
  'searchDbBoulder2017ElectionContributionsCity': "searchDbBoulder2017ElectionContributionsCity_example", // String | City
  'searchDbBoulder2017ElectionContributionsState': "searchDbBoulder2017ElectionContributionsState_example", // String | State
  'searchDbBoulder2017ElectionContributionsZip': "searchDbBoulder2017ElectionContributionsZip_example", // String | Zip
  'searchDbBoulder2017ElectionContributionsContributionType': "searchDbBoulder2017ElectionContributionsContributionType_example", // String | Contribution Type
  'searchDbBoulder2017ElectionContributionsFromCandidate': "searchDbBoulder2017ElectionContributionsFromCandidate_example", // String | From Candidate
  'searchDbBoulder2017ElectionContributionsDate': "searchDbBoulder2017ElectionContributionsDate_example", // String | Date
  'searchDbBoulder2017ElectionContributionsAmount': 3.4, // Number | Amount
  'searchDbBoulder2017ElectionContributionsMatchAmount': 3.4, // Number | Match Amount
  'searchDbBoulder2017ElectionContributionsYtdAmount': 3.4, // Number | Ytd Amount
  'searchDbBoulder2017ElectionContributionsLocation': "searchDbBoulder2017ElectionContributionsLocation_example" // String | Location
};
apiInstance.searchBoulder2017ElectionContributions(opts, (error, data, response) => {
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
 **searchDbBoulder2017ElectionContributionsCommittee** | **String**| Committee | [optional] 
 **searchDbBoulder2017ElectionContributionsLastName** | **String**| Last Name | [optional] 
 **searchDbBoulder2017ElectionContributionsFirstName** | **String**| First Name | [optional] 
 **searchDbBoulder2017ElectionContributionsStreet** | **String**| Street | [optional] 
 **searchDbBoulder2017ElectionContributionsCity** | **String**| City | [optional] 
 **searchDbBoulder2017ElectionContributionsState** | **String**| State | [optional] 
 **searchDbBoulder2017ElectionContributionsZip** | **String**| Zip | [optional] 
 **searchDbBoulder2017ElectionContributionsContributionType** | **String**| Contribution Type | [optional] 
 **searchDbBoulder2017ElectionContributionsFromCandidate** | **String**| From Candidate | [optional] 
 **searchDbBoulder2017ElectionContributionsDate** | **String**| Date | [optional] 
 **searchDbBoulder2017ElectionContributionsAmount** | **Number**| Amount | [optional] 
 **searchDbBoulder2017ElectionContributionsMatchAmount** | **Number**| Match Amount | [optional] 
 **searchDbBoulder2017ElectionContributionsYtdAmount** | **Number**| Ytd Amount | [optional] 
 **searchDbBoulder2017ElectionContributionsLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

