# GeodesystemsCom443.TypeBoulderCampaignContributionsApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBoulderCampaignContributions**](TypeBoulderCampaignContributionsApi.md#searchBoulderCampaignContributions) | **GET** /repository/search/type/boulder_campaign_contributions | Search API for &#39;Boulder Campaign Contributions&#39; entry type



## searchBoulderCampaignContributions

> searchBoulderCampaignContributions(opts)

Search API for &#39;Boulder Campaign Contributions&#39; entry type

API to search for entries of type Boulder Campaign Contributions

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeBoulderCampaignContributionsApi();
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
  'searchDbBoulderCampaignContributionsCommittee': "searchDbBoulderCampaignContributionsCommittee_example", // String | Committee
  'searchDbBoulderCampaignContributionsType': "searchDbBoulderCampaignContributionsType_example", // String | Type
  'searchDbBoulderCampaignContributionsCommitteeNum': "searchDbBoulderCampaignContributionsCommitteeNum_example", // String | Committee Num
  'searchDbBoulderCampaignContributionsCandidate': "searchDbBoulderCampaignContributionsCandidate_example", // String | Candidate
  'searchDbBoulderCampaignContributionsFilingDate': "searchDbBoulderCampaignContributionsFilingDate_example", // String | Filing Date
  'searchDbBoulderCampaignContributionsAmendedDate': "searchDbBoulderCampaignContributionsAmendedDate_example", // String | Amended Date
  'searchDbBoulderCampaignContributionsOfficialFiling': "searchDbBoulderCampaignContributionsOfficialFiling_example", // String | Official Filing
  'searchDbBoulderCampaignContributionsTransactionDate': "searchDbBoulderCampaignContributionsTransactionDate_example", // String | Transaction Date
  'searchDbBoulderCampaignContributionsLastName': "searchDbBoulderCampaignContributionsLastName_example", // String | Last Name
  'searchDbBoulderCampaignContributionsFirstName': "searchDbBoulderCampaignContributionsFirstName_example", // String | First Name
  'searchDbBoulderCampaignContributionsStreet': "searchDbBoulderCampaignContributionsStreet_example", // String | Street
  'searchDbBoulderCampaignContributionsCity': "searchDbBoulderCampaignContributionsCity_example", // String | City
  'searchDbBoulderCampaignContributionsState': "searchDbBoulderCampaignContributionsState_example", // String | State
  'searchDbBoulderCampaignContributionsZip': "searchDbBoulderCampaignContributionsZip_example", // String | Zip
  'searchDbBoulderCampaignContributionsContribution': 3.4, // Number | Contribution
  'searchDbBoulderCampaignContributionsContributionType': "searchDbBoulderCampaignContributionsContributionType_example", // String | Contribution Type
  'searchDbBoulderCampaignContributionsAnonymous': "searchDbBoulderCampaignContributionsAnonymous_example", // String | Anonymous
  'searchDbBoulderCampaignContributionsFromCandidate': "searchDbBoulderCampaignContributionsFromCandidate_example", // String | From Candidate
  'searchDbBoulderCampaignContributionsMatch': 3.4 // Number | Match
};
apiInstance.searchBoulderCampaignContributions(opts, (error, data, response) => {
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
 **searchDbBoulderCampaignContributionsCommittee** | **String**| Committee | [optional] 
 **searchDbBoulderCampaignContributionsType** | **String**| Type | [optional] 
 **searchDbBoulderCampaignContributionsCommitteeNum** | **String**| Committee Num | [optional] 
 **searchDbBoulderCampaignContributionsCandidate** | **String**| Candidate | [optional] 
 **searchDbBoulderCampaignContributionsFilingDate** | **String**| Filing Date | [optional] 
 **searchDbBoulderCampaignContributionsAmendedDate** | **String**| Amended Date | [optional] 
 **searchDbBoulderCampaignContributionsOfficialFiling** | **String**| Official Filing | [optional] 
 **searchDbBoulderCampaignContributionsTransactionDate** | **String**| Transaction Date | [optional] 
 **searchDbBoulderCampaignContributionsLastName** | **String**| Last Name | [optional] 
 **searchDbBoulderCampaignContributionsFirstName** | **String**| First Name | [optional] 
 **searchDbBoulderCampaignContributionsStreet** | **String**| Street | [optional] 
 **searchDbBoulderCampaignContributionsCity** | **String**| City | [optional] 
 **searchDbBoulderCampaignContributionsState** | **String**| State | [optional] 
 **searchDbBoulderCampaignContributionsZip** | **String**| Zip | [optional] 
 **searchDbBoulderCampaignContributionsContribution** | **Number**| Contribution | [optional] 
 **searchDbBoulderCampaignContributionsContributionType** | **String**| Contribution Type | [optional] 
 **searchDbBoulderCampaignContributionsAnonymous** | **String**| Anonymous | [optional] 
 **searchDbBoulderCampaignContributionsFromCandidate** | **String**| From Candidate | [optional] 
 **searchDbBoulderCampaignContributionsMatch** | **Number**| Match | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

