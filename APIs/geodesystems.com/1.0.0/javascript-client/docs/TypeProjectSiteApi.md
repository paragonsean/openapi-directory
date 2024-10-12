# GeodesystemsCom443.TypeProjectSiteApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchProjectSite**](TypeProjectSiteApi.md#searchProjectSite) | **GET** /repository/search/type/project_site | Search API for &#39;Site&#39; entry type



## searchProjectSite

> searchProjectSite(opts)

Search API for &#39;Site&#39; entry type

API to search for entries of type Site

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeProjectSiteApi();
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
  'searchProjectSiteShortName': "searchProjectSiteShortName_example", // String | Short Name
  'searchProjectSiteSiteType': "searchProjectSiteSiteType_example", // String | Site Type
  'searchProjectSiteStatus': "searchProjectSiteStatus_example", // String | Status
  'searchProjectSiteNetwork': "searchProjectSiteNetwork_example", // String | Network
  'searchProjectSiteCountry': "searchProjectSiteCountry_example", // String | Country
  'searchProjectSiteState': "searchProjectSiteState_example", // String | State/Province
  'searchProjectSiteCounty': "searchProjectSiteCounty_example" // String | County
};
apiInstance.searchProjectSite(opts, (error, data, response) => {
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
 **searchProjectSiteShortName** | **String**| Short Name | [optional] 
 **searchProjectSiteSiteType** | **String**| Site Type | [optional] 
 **searchProjectSiteStatus** | **String**| Status | [optional] 
 **searchProjectSiteNetwork** | **String**| Network | [optional] 
 **searchProjectSiteCountry** | **String**| Country | [optional] 
 **searchProjectSiteState** | **String**| State/Province | [optional] 
 **searchProjectSiteCounty** | **String**| County | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

