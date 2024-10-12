# GeodesystemsCom443.TypeBoulderCountyVoterDetailsApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchBoulderCountyVoterDetails**](TypeBoulderCountyVoterDetailsApi.md#searchBoulderCountyVoterDetails) | **GET** /repository/search/type/boulder_county_voter_details | Search API for &#39;Boulder County Voter Details&#39; entry type



## searchBoulderCountyVoterDetails

> searchBoulderCountyVoterDetails(opts)

Search API for &#39;Boulder County Voter Details&#39; entry type

API to search for entries of type Boulder County Voter Details

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeBoulderCountyVoterDetailsApi();
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
  'searchDbBoulderCountyVoterDetailsFirstName': "searchDbBoulderCountyVoterDetailsFirstName_example", // String | First Name
  'searchDbBoulderCountyVoterDetailsLastName': "searchDbBoulderCountyVoterDetailsLastName_example", // String | Last Name
  'searchDbBoulderCountyVoterDetailsRegistrationDate': "searchDbBoulderCountyVoterDetailsRegistrationDate_example", // String | Registration Date
  'searchDbBoulderCountyVoterDetailsLastUpdatedDate': "searchDbBoulderCountyVoterDetailsLastUpdatedDate_example", // String | Last Updated Date
  'searchDbBoulderCountyVoterDetailsResidentialAddress': "searchDbBoulderCountyVoterDetailsResidentialAddress_example", // String | Residential Address
  'searchDbBoulderCountyVoterDetailsResidentialCity': "searchDbBoulderCountyVoterDetailsResidentialCity_example", // String | Residential City
  'searchDbBoulderCountyVoterDetailsMailingZipCode': "searchDbBoulderCountyVoterDetailsMailingZipCode_example", // String | Mailing Zip Code
  'searchDbBoulderCountyVoterDetailsVoterStatus': "searchDbBoulderCountyVoterDetailsVoterStatus_example", // String | Voter Status
  'searchDbBoulderCountyVoterDetailsParty': "searchDbBoulderCountyVoterDetailsParty_example", // String | Party
  'searchDbBoulderCountyVoterDetailsGender': "searchDbBoulderCountyVoterDetailsGender_example", // String | Gender
  'searchDbBoulderCountyVoterDetailsBirthYear': 56, // Number | Birth Year
  'searchDbBoulderCountyVoterDetailsPrecinctCode': "searchDbBoulderCountyVoterDetailsPrecinctCode_example", // String | Precinct Code
  'searchDbBoulderCountyVoterDetailsCongressional': "searchDbBoulderCountyVoterDetailsCongressional_example", // String | Congressional
  'searchDbBoulderCountyVoterDetailsStateSenate': "searchDbBoulderCountyVoterDetailsStateSenate_example", // String | State Senate
  'searchDbBoulderCountyVoterDetailsStateHouse': "searchDbBoulderCountyVoterDetailsStateHouse_example", // String | State House
  'searchDbBoulderCountyVoterDetailsMunicipality': "searchDbBoulderCountyVoterDetailsMunicipality_example", // String | Municipality
  'searchDbBoulderCountyVoterDetailsCityWardDistrict': "searchDbBoulderCountyVoterDetailsCityWardDistrict_example", // String | City Ward/district
  'searchDbBoulderCountyVoterDetailsSchoolDistrict': "searchDbBoulderCountyVoterDetailsSchoolDistrict_example", // String | School District
  'searchDbBoulderCountyVoterDetailsLocation': "searchDbBoulderCountyVoterDetailsLocation_example" // String | Location
};
apiInstance.searchBoulderCountyVoterDetails(opts, (error, data, response) => {
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
 **searchDbBoulderCountyVoterDetailsFirstName** | **String**| First Name | [optional] 
 **searchDbBoulderCountyVoterDetailsLastName** | **String**| Last Name | [optional] 
 **searchDbBoulderCountyVoterDetailsRegistrationDate** | **String**| Registration Date | [optional] 
 **searchDbBoulderCountyVoterDetailsLastUpdatedDate** | **String**| Last Updated Date | [optional] 
 **searchDbBoulderCountyVoterDetailsResidentialAddress** | **String**| Residential Address | [optional] 
 **searchDbBoulderCountyVoterDetailsResidentialCity** | **String**| Residential City | [optional] 
 **searchDbBoulderCountyVoterDetailsMailingZipCode** | **String**| Mailing Zip Code | [optional] 
 **searchDbBoulderCountyVoterDetailsVoterStatus** | **String**| Voter Status | [optional] 
 **searchDbBoulderCountyVoterDetailsParty** | **String**| Party | [optional] 
 **searchDbBoulderCountyVoterDetailsGender** | **String**| Gender | [optional] 
 **searchDbBoulderCountyVoterDetailsBirthYear** | **Number**| Birth Year | [optional] 
 **searchDbBoulderCountyVoterDetailsPrecinctCode** | **String**| Precinct Code | [optional] 
 **searchDbBoulderCountyVoterDetailsCongressional** | **String**| Congressional | [optional] 
 **searchDbBoulderCountyVoterDetailsStateSenate** | **String**| State Senate | [optional] 
 **searchDbBoulderCountyVoterDetailsStateHouse** | **String**| State House | [optional] 
 **searchDbBoulderCountyVoterDetailsMunicipality** | **String**| Municipality | [optional] 
 **searchDbBoulderCountyVoterDetailsCityWardDistrict** | **String**| City Ward/district | [optional] 
 **searchDbBoulderCountyVoterDetailsSchoolDistrict** | **String**| School District | [optional] 
 **searchDbBoulderCountyVoterDetailsLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

