# LetMcApiV2FreeTier1.AreaControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier1ShortNameAreaAreasAreaIDGet**](AreaControllerApi.md#v2Tier1ShortNameAreaAreasAreaIDGet) | **GET** /v2/tier1/{shortName}/area/areas/{areaID} | Get a specific area given its unique Object ID (OID)
[**v2Tier1ShortNameAreaAreasGet**](AreaControllerApi.md#v2Tier1ShortNameAreaAreasGet) | **GET** /v2/tier1/{shortName}/area/areas | A collection of all the areas for a company



## v2Tier1ShortNameAreaAreasAreaIDGet

> AreaModel v2Tier1ShortNameAreaAreasAreaIDGet(shortName, areaID)

Get a specific area given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.AreaControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let areaID = "areaID_example"; // String | The unique ID of the Area
apiInstance.v2Tier1ShortNameAreaAreasAreaIDGet(shortName, areaID, (error, data, response) => {
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
 **areaID** | **String**| The unique ID of the Area | 

### Return type

[**AreaModel**](AreaModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameAreaAreasGet

> AreaModelResults v2Tier1ShortNameAreaAreasGet(shortName, offset, count)

A collection of all the areas for a company

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.AreaControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameAreaAreasGet(shortName, offset, count, (error, data, response) => {
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

[**AreaModelResults**](AreaModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

