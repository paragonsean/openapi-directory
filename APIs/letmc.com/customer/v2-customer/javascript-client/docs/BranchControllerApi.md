# AgentOsApiV2CustomerLoginCallGroup.BranchControllerApi

All URIs are relative to *https://live-api.letmc.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**branchControllerGetBranches**](BranchControllerApi.md#branchControllerGetBranches) | **GET** /v2/customer/{shortName}/branch/branches | All branches defined for a company
[**v2CustomerShortNameBranchBranchesBranchIDGet**](BranchControllerApi.md#v2CustomerShortNameBranchBranchesBranchIDGet) | **GET** /v2/customer/{shortName}/branch/branches/{branchID} | Get a specific branch given its unique Object ID (OID)



## branchControllerGetBranches

> BranchModelResults branchControllerGetBranches(shortName, offset, count)

All branches defined for a company

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.BranchControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let offset = 56; // Number | The index of the first item to return
let count = 56; // Number | The maximum number of items to return (up to 1000 per request)
apiInstance.branchControllerGetBranches(shortName, offset, count, (error, data, response) => {
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
- **Accept**: application/json, application/xml, text/json, text/xml


## v2CustomerShortNameBranchBranchesBranchIDGet

> BranchModel v2CustomerShortNameBranchBranchesBranchIDGet(shortName, branchID)

Get a specific branch given its unique Object ID (OID)

### Example

```javascript
import AgentOsApiV2CustomerLoginCallGroup from 'agent_os_api_v2_customer_login_call_group';

let apiInstance = new AgentOsApiV2CustomerLoginCallGroup.BranchControllerApi();
let shortName = "shortName_example"; // String | The unique client short-name
let branchID = "branchID_example"; // String | The unique ID of the Branch
apiInstance.v2CustomerShortNameBranchBranchesBranchIDGet(shortName, branchID, (error, data, response) => {
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
- **Accept**: application/json, application/xml, text/json, text/xml

