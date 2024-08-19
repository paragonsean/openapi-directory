# SchoolDiggerApiV20.RankingsApi

All URIs are relative to *https://api.schooldigger.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**rankingsGetRankDistrict**](RankingsApi.md#rankingsGetRankDistrict) | **GET** /v2.0/rankings/districts/{st} | Returns a SchoolDigger district ranking list
[**rankingsGetSchoolRank2**](RankingsApi.md#rankingsGetSchoolRank2) | **GET** /v2.0/rankings/schools/{st} | Returns a SchoolDigger school ranking list



## rankingsGetRankDistrict

> APIDistrictListRank2 rankingsGetRankDistrict(st, appID, appKey, opts)

Returns a SchoolDigger district ranking list

### Example

```javascript
import SchoolDiggerApiV20 from 'school_digger_api_v2_0';

let apiInstance = new SchoolDiggerApiV20.RankingsApi();
let st = "st_example"; // String | Two character state (e.g. 'CA')
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
let opts = {
  'year': 56, // Number | The ranking year (leave blank for most recent year)
  'page': 56, // Number | Page number to retrieve (optional, default: 1)
  'perPage': 56 // Number | Number of districts to retrieve on a page (50 max) (optional, default: 10)
};
apiInstance.rankingsGetRankDistrict(st, appID, appKey, opts, (error, data, response) => {
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
 **st** | **String**| Two character state (e.g. &#39;CA&#39;) | 
 **appID** | **String**| Your API app id | 
 **appKey** | **String**| Your API app key | 
 **year** | **Number**| The ranking year (leave blank for most recent year) | [optional] 
 **page** | **Number**| Page number to retrieve (optional, default: 1) | [optional] 
 **perPage** | **Number**| Number of districts to retrieve on a page (50 max) (optional, default: 10) | [optional] 

### Return type

[**APIDistrictListRank2**](APIDistrictListRank2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## rankingsGetSchoolRank2

> APISchoolListRank2 rankingsGetSchoolRank2(st, appID, appKey, opts)

Returns a SchoolDigger school ranking list

### Example

```javascript
import SchoolDiggerApiV20 from 'school_digger_api_v2_0';

let apiInstance = new SchoolDiggerApiV20.RankingsApi();
let st = "st_example"; // String | Two character state (e.g. 'CA')
let appID = "appID_example"; // String | Your API app id
let appKey = "appKey_example"; // String | Your API app key
let opts = {
  'year': 56, // Number | The ranking year (leave blank for most recent year)
  'level': "level_example", // String | Level of ranking: 'Elementary', 'Middle', or 'High'
  'page': 56, // Number | Page number to retrieve (optional, default: 1)
  'perPage': 56 // Number | Number of schools to retrieve on a page (50 max) (optional, default: 10)
};
apiInstance.rankingsGetSchoolRank2(st, appID, appKey, opts, (error, data, response) => {
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
 **st** | **String**| Two character state (e.g. &#39;CA&#39;) | 
 **appID** | **String**| Your API app id | 
 **appKey** | **String**| Your API app key | 
 **year** | **Number**| The ranking year (leave blank for most recent year) | [optional] 
 **level** | **String**| Level of ranking: &#39;Elementary&#39;, &#39;Middle&#39;, or &#39;High&#39; | [optional] 
 **page** | **Number**| Page number to retrieve (optional, default: 1) | [optional] 
 **perPage** | **Number**| Number of schools to retrieve on a page (50 max) (optional, default: 10) | [optional] 

### Return type

[**APISchoolListRank2**](APISchoolListRank2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

