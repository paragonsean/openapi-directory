# LetMcApiV2FreeTier1.LettingsControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**lettingsControllerGetAdvertised**](LettingsControllerApi.md#lettingsControllerGetAdvertised) | **GET** /v2/tier1/{shortName}/lettings/advertised | Search all properties available for rent given a range of search criteria.
[**lettingsControllerGetAdvertisedBetweenDates**](LettingsControllerApi.md#lettingsControllerGetAdvertisedBetweenDates) | **GET** /v2/tier1/{shortName}/lettings/advertisedbetweendates | Search all properties available for rent given a range of search criteria and dates.
[**lettingsControllerGetTenancyBrochure**](LettingsControllerApi.md#lettingsControllerGetTenancyBrochure) | **GET** /v2/tier1/{shortName}/lettings/tenancies/{tenancyID}/brochure | Downloads the brochure relating to the latest advertised rental of a property
[**v2Tier1ShortNameLettingsTenanciesGet**](LettingsControllerApi.md#v2Tier1ShortNameLettingsTenanciesGet) | **GET** /v2/tier1/{shortName}/lettings/tenancies | A collection of all the company&#39;s tenancies
[**v2Tier1ShortNameLettingsTenanciesTenancyIDGet**](LettingsControllerApi.md#v2Tier1ShortNameLettingsTenanciesTenancyIDGet) | **GET** /v2/tier1/{shortName}/lettings/tenancies/{tenancyID} | Get a specific tenancy given its unique Object ID (OID)



## lettingsControllerGetAdvertised

> TenancyModelResults lettingsControllerGetAdvertised(shortName, branchID, offset, count, opts)

Search all properties available for rent given a range of search criteria.

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.LettingsControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
let opts = {
  'areaID': "areaID_example", // String | The unique ID of the Area
  'rentMinimum': 3.4, // Number | The minimum advertised rent to search for
  'rentMaximum': 3.4, // Number | The maximum advertised rent to search for
  'maximumTenants': 56, // Number | The maximum number of tenants a property can accommodate
  'wantSharedProperties': true, // Boolean | Search for shared properties?
  'wantStudentProperties': true // Boolean | Search for student properties?
};
apiInstance.lettingsControllerGetAdvertised(shortName, branchID, offset, count, opts, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 
 **areaID** | **String**| The unique ID of the Area | [optional] 
 **rentMinimum** | **Number**| The minimum advertised rent to search for | [optional] 
 **rentMaximum** | **Number**| The maximum advertised rent to search for | [optional] 
 **maximumTenants** | **Number**| The maximum number of tenants a property can accommodate | [optional] 
 **wantSharedProperties** | **Boolean**| Search for shared properties? | [optional] 
 **wantStudentProperties** | **Boolean**| Search for student properties? | [optional] 

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## lettingsControllerGetAdvertisedBetweenDates

> TenancyModelResults lettingsControllerGetAdvertisedBetweenDates(shortName, branchID, offset, count, rangeStartDate, rangeEndDate, opts)

Search all properties available for rent given a range of search criteria and dates.

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.LettingsControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
let rangeStartDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search from
let rangeEndDate = new Date("2013-10-20T19:20:30+01:00"); // Date | The date to search to
let opts = {
  'areaID': "areaID_example", // String | The unique ID of the Area
  'rentMinimum': 3.4, // Number | The minimum advertised rent to search for
  'rentMaximum': 3.4, // Number | The maximum advertised rent to search for
  'maximumTenants': 56, // Number | The maximum number of tenants a property can accommodate
  'wantSharedProperties': true, // Boolean | Search for shared properties?
  'wantStudentProperties': true // Boolean | Search for student properties?
};
apiInstance.lettingsControllerGetAdvertisedBetweenDates(shortName, branchID, offset, count, rangeStartDate, rangeEndDate, opts, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **branchID** | **String**| The unique ID of the Branch | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 
 **rangeStartDate** | **Date**| The date to search from | 
 **rangeEndDate** | **Date**| The date to search to | 
 **areaID** | **String**| The unique ID of the Area | [optional] 
 **rentMinimum** | **Number**| The minimum advertised rent to search for | [optional] 
 **rentMaximum** | **Number**| The maximum advertised rent to search for | [optional] 
 **maximumTenants** | **Number**| The maximum number of tenants a property can accommodate | [optional] 
 **wantSharedProperties** | **Boolean**| Search for shared properties? | [optional] 
 **wantStudentProperties** | **Boolean**| Search for student properties? | [optional] 

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## lettingsControllerGetTenancyBrochure

> Object lettingsControllerGetTenancyBrochure(shortName, tenancyID)

Downloads the brochure relating to the latest advertised rental of a property

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.LettingsControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let tenancyID = "tenancyID_example"; // String | The unique ID of the tenancy
apiInstance.lettingsControllerGetTenancyBrochure(shortName, tenancyID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **tenancyID** | **String**| The unique ID of the tenancy | 

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameLettingsTenanciesGet

> TenancyModelResults v2Tier1ShortNameLettingsTenanciesGet(shortName, offset, count)

A collection of all the company&#39;s tenancies

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.LettingsControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameLettingsTenanciesGet(shortName, offset, count, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**TenancyModelResults**](TenancyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameLettingsTenanciesTenancyIDGet

> TenancyModel v2Tier1ShortNameLettingsTenanciesTenancyIDGet(shortName, tenancyID)

Get a specific tenancy given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.LettingsControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let tenancyID = "tenancyID_example"; // String | The unique ID of the Tenancy
apiInstance.v2Tier1ShortNameLettingsTenanciesTenancyIDGet(shortName, tenancyID, (error, data, response) => {
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
 **shortName** | **String**| The unique client short-name | 
 **tenancyID** | **String**| The unique ID of the Tenancy | 

### Return type

[**TenancyModel**](TenancyModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

