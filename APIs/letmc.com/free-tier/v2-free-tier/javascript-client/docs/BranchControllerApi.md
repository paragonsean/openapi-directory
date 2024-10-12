# LetMcApiV2FreeTier1.BranchControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier1ShortNameBranchBranchesBranchIDGet**](BranchControllerApi.md#v2Tier1ShortNameBranchBranchesBranchIDGet) | **GET** /v2/tier1/{shortName}/branch/branches/{branchID} | Get a specific branch given its unique Object ID (OID)
[**v2Tier1ShortNameBranchBranchesGet**](BranchControllerApi.md#v2Tier1ShortNameBranchBranchesGet) | **GET** /v2/tier1/{shortName}/branch/branches | All branches defined for a company



## v2Tier1ShortNameBranchBranchesBranchIDGet

> BranchModel v2Tier1ShortNameBranchBranchesBranchIDGet(shortName, branchID)

Get a specific branch given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.BranchControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
apiInstance.v2Tier1ShortNameBranchBranchesBranchIDGet(shortName, branchID, (error, data, response) => {
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

### Return type

[**BranchModel**](BranchModel.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml


## v2Tier1ShortNameBranchBranchesGet

> BranchModelResults v2Tier1ShortNameBranchBranchesGet(shortName, offset, count)

All branches defined for a company

### Example

```javascript
import LetMcApiV2FreeTier1 from 'let_mc_api_v2_free__tier_1';

let apiInstance = new LetMcApiV2FreeTier1.BranchControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier1ShortNameBranchBranchesGet(shortName, offset, count, (error, data, response) => {
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

[**BranchModelResults**](BranchModelResults.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/json, application/xml, text/xml

