# GeodesystemsCom443.TypeColoradoWaterRightsApi

All URIs are relative to *https://geodesystems.com:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**searchColoradoWaterRights**](TypeColoradoWaterRightsApi.md#searchColoradoWaterRights) | **GET** /repository/search/type/colorado_water_rights | Search API for &#39;Colorado Water Rights&#39; entry type



## searchColoradoWaterRights

> searchColoradoWaterRights(opts)

Search API for &#39;Colorado Water Rights&#39; entry type

API to search for entries of type Colorado Water Rights

### Example

```javascript
import GeodesystemsCom443 from 'geodesystems_com443';

let apiInstance = new GeodesystemsCom443.TypeColoradoWaterRightsApi();
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
  'searchDbColoradoWaterRightsStructureName': "searchDbColoradoWaterRightsStructureName_example", // String | Structure Name
  'searchDbColoradoWaterRightsStructureType': "searchDbColoradoWaterRightsStructureType_example", // String | Structure Type
  'searchDbColoradoWaterRightsWaterSource': "searchDbColoradoWaterRightsWaterSource_example", // String | Water Source
  'searchDbColoradoWaterRightsCounty': "searchDbColoradoWaterRightsCounty_example", // String | County
  'searchDbColoradoWaterRightsAdjudicationDate': "searchDbColoradoWaterRightsAdjudicationDate_example", // String | Adjudication Date
  'searchDbColoradoWaterRightsAppropriationDate': "searchDbColoradoWaterRightsAppropriationDate_example", // String | Appropriation Date
  'searchDbColoradoWaterRightsPriorityNo': "searchDbColoradoWaterRightsPriorityNo_example", // String | Priority No
  'searchDbColoradoWaterRightsDecreedUses': "searchDbColoradoWaterRightsDecreedUses_example", // String | Decreed Uses
  'searchDbColoradoWaterRightsNetAbsolute': 3.4, // Number | Net Absolute
  'searchDbColoradoWaterRightsNetConditional': 3.4, // Number | Net Conditional
  'searchDbColoradoWaterRightsNetApexAbsolute': 3.4, // Number | Net Apex Absolute
  'searchDbColoradoWaterRightsNetApexConditional': 3.4, // Number | Net Apex Conditional
  'searchDbColoradoWaterRightsDecreedUnits': "searchDbColoradoWaterRightsDecreedUnits_example", // String | Decreed Units
  'searchDbColoradoWaterRightsSeasonalLimits': "searchDbColoradoWaterRightsSeasonalLimits_example", // String | Seasonal Limits
  'searchDbColoradoWaterRightsComments': "searchDbColoradoWaterRightsComments_example", // String | Comments
  'searchDbColoradoWaterRightsMoreInformation': "searchDbColoradoWaterRightsMoreInformation_example", // String | More Information
  'searchDbColoradoWaterRightsLocation': "searchDbColoradoWaterRightsLocation_example" // String | Location
};
apiInstance.searchColoradoWaterRights(opts, (error, data, response) => {
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
 **searchDbColoradoWaterRightsStructureName** | **String**| Structure Name | [optional] 
 **searchDbColoradoWaterRightsStructureType** | **String**| Structure Type | [optional] 
 **searchDbColoradoWaterRightsWaterSource** | **String**| Water Source | [optional] 
 **searchDbColoradoWaterRightsCounty** | **String**| County | [optional] 
 **searchDbColoradoWaterRightsAdjudicationDate** | **String**| Adjudication Date | [optional] 
 **searchDbColoradoWaterRightsAppropriationDate** | **String**| Appropriation Date | [optional] 
 **searchDbColoradoWaterRightsPriorityNo** | **String**| Priority No | [optional] 
 **searchDbColoradoWaterRightsDecreedUses** | **String**| Decreed Uses | [optional] 
 **searchDbColoradoWaterRightsNetAbsolute** | **Number**| Net Absolute | [optional] 
 **searchDbColoradoWaterRightsNetConditional** | **Number**| Net Conditional | [optional] 
 **searchDbColoradoWaterRightsNetApexAbsolute** | **Number**| Net Apex Absolute | [optional] 
 **searchDbColoradoWaterRightsNetApexConditional** | **Number**| Net Apex Conditional | [optional] 
 **searchDbColoradoWaterRightsDecreedUnits** | **String**| Decreed Units | [optional] 
 **searchDbColoradoWaterRightsSeasonalLimits** | **String**| Seasonal Limits | [optional] 
 **searchDbColoradoWaterRightsComments** | **String**| Comments | [optional] 
 **searchDbColoradoWaterRightsMoreInformation** | **String**| More Information | [optional] 
 **searchDbColoradoWaterRightsLocation** | **String**| Location | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

