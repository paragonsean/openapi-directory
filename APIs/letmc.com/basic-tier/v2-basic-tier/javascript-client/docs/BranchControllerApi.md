# LetMcApiV2BasicTier2.BranchControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v2Tier2ShortNameBranchBranchesBranchIDGet**](BranchControllerApi.md#v2Tier2ShortNameBranchBranchesBranchIDGet) | **GET** /v2/tier2/{shortName}/branch/branches/{branchID} | Get a specific branch given its unique Object ID (OID)
[**v2Tier2ShortNameBranchBranchesGet**](BranchControllerApi.md#v2Tier2ShortNameBranchBranchesGet) | **GET** /v2/tier2/{shortName}/branch/branches | All branches defined for a company



## v2Tier2ShortNameBranchBranchesBranchIDGet

> BranchModel v2Tier2ShortNameBranchBranchesBranchIDGet(shortName, branchID)

Get a specific branch given its unique Object ID (OID)

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.BranchControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
apiInstance.v2Tier2ShortNameBranchBranchesBranchIDGet(shortName, branchID, (error, data, response) => {
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


## v2Tier2ShortNameBranchBranchesGet

> BranchModelResults v2Tier2ShortNameBranchBranchesGet(shortName, offset, count)

All branches defined for a company

### Example

```javascript
import LetMcApiV2BasicTier2 from 'let_mc_api_v2_basic__tier_2';

let apiInstance = new LetMcApiV2BasicTier2.BranchControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.v2Tier2ShortNameBranchBranchesGet(shortName, offset, count, (error, data, response) => {
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

