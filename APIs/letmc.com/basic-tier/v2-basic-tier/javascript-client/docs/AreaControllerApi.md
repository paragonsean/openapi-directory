# LetMcApiV2BasicTier2.AreaControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier2ShortNameAreaAreasAreaIDGet**](AreaControllerApi.md#v2Tier2ShortNameAreaAreasAreaIDGet) | **GET** /v2/tier2/{shortName}/area/areas/{areaID} | Get a specific area given its unique Object ID (OID)
[**v2Tier2ShortNameAreaAreasGet**](AreaControllerApi.md#v2Tier2ShortNameAreaAreasGet) | **GET** /v2/tier2/{shortName}/area/areas | A collection of all the areas for a company



## v2Tier2ShortNameAreaAreasAreaIDGet

> AreaModel v2Tier2ShortNameAreaAreasAreaIDGet(shortName, areaID)

Get a specific area given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.AreaControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let areaID = "areaID_example"; // String | The unique ID of the Area
apiInstance.v2Tier2ShortNameAreaAreasAreaIDGet(shortName, areaID, (error, data, response) => {
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


## v2Tier2ShortNameAreaAreasGet

> AreaModelResults v2Tier2ShortNameAreaAreasGet(shortName, offset, count)

A collection of all the areas for a company

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.AreaControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier2ShortNameAreaAreasGet(shortName, offset, count, (error, data, response) => {
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

