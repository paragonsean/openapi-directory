# LetMcApiV2FreeTier1.CountyControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**countyControllerGetCountiesBranches**](CountyControllerApi.md#countyControllerGetCountiesBranches) | **GET** /v2/tier1/{shortName}/county/counties/{countyID}/branches | A collection of branches that manage a specific county
[**v2Tier1ShortNameCountyCountiesCountyIDGet**](CountyControllerApi.md#v2Tier1ShortNameCountyCountiesCountyIDGet) | **GET** /v2/tier1/{shortName}/county/counties/{countyID} | Get a specific county given its unique Object ID (OID)
[**v2Tier1ShortNameCountyCountiesGet**](CountyControllerApi.md#v2Tier1ShortNameCountyCountiesGet) | **GET** /v2/tier1/{shortName}/county/counties | A collection of all counties available for a company



## countyControllerGetCountiesBranches

> BranchModelResults countyControllerGetCountiesBranches(shortName, countyID, offset, count)

A collection of branches that manage a specific county

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.CountyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let countyID = "countyID_example"; // String | The unique ID of the County
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.countyControllerGetCountiesBranches(shortName, countyID, offset, count, (error, data, response) => {
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
 **countyID** | **String**| The unique ID of the County | 
 **offset** | **Number**| The index of the first item to return | 
 **count** | **Number**| The maximum number of items to return (up to 1000 per request) | 

### Return type

[**BranchModelResults**](BranchModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameCountyCountiesCountyIDGet

> CountyModel v2Tier1ShortNameCountyCountiesCountyIDGet(shortName, countyID)

Get a specific county given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.CountyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let countyID = "countyID_example"; // String | The unique ID of the County
apiInstance.v2Tier1ShortNameCountyCountiesCountyIDGet(shortName, countyID, (error, data, response) => {
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
 **countyID** | **String**| The unique ID of the County | 

### Return type

[**CountyModel**](CountyModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameCountyCountiesGet

> CountyModelResults v2Tier1ShortNameCountyCountiesGet(shortName, offset, count)

A collection of all counties available for a company

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.CountyControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameCountyCountiesGet(shortName, offset, count, (error, data, response) => {
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

[**CountyModelResults**](CountyModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

