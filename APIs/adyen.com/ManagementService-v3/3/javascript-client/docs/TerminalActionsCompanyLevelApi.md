# ManagementApi.TerminalActionsCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompaniesCompanyIdTerminalActions**](TerminalActionsCompanyLevelApi.md#getCompaniesCompanyIdTerminalActions) | **GET** /companies/{companyId}/terminalActions | Get a list of terminal actions
[**getCompaniesCompanyIdTerminalActionsActionId**](TerminalActionsCompanyLevelApi.md#getCompaniesCompanyIdTerminalActionsActionId) | **GET** /companies/{companyId}/terminalActions/{actionId} | Get terminal action



## getCompaniesCompanyIdTerminalActions

> ListExternalTerminalActionsResponse getCompaniesCompanyIdTerminalActions(companyId, opts)

Get a list of terminal actions

Returns the [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) that have been scheduled for the company identified in the path.The response doesn&#39;t include actions that are scheduled by Adyen. To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalActionsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56, // Number | The number of items to have on a page, maximum 100. The default is 20 items on a page.
  'status': "status_example", // String | Returns terminal actions with the specified status.  Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**.
  'type': "type_example" // String | Returns terminal actions of the specified type.  Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**.
};
apiInstance.getCompaniesCompanyIdTerminalActions(companyId, opts, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **pageNumber** | **Number**| The number of the page to fetch. | [optional] 
 **pageSize** | **Number**| The number of items to have on a page, maximum 100. The default is 20 items on a page. | [optional] 
 **status** | **String**| Returns terminal actions with the specified status.  Allowed values: **pending**, **successful**, **failed**, **cancelled**, **tryLater**. | [optional] 
 **type** | **String**| Returns terminal actions of the specified type.  Allowed values: **InstallAndroidApp**, **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**. | [optional] 

### Return type

[**ListExternalTerminalActionsResponse**](ListExternalTerminalActionsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdTerminalActionsActionId

> ExternalTerminalAction getCompaniesCompanyIdTerminalActionsActionId(companyId, actionId)

Get terminal action

Returns the details of the [terminal action](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api) identified in the path. To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Terminal actions read * Management API—Terminal actions read and write

### Example

```javascript
import ManagementApi from 'management_api';
let defaultClient = ManagementApi.ApiClient.instance;
// Configure HTTP basic authorization: BasicAuth
let BasicAuth = defaultClient.authentications['BasicAuth'];
BasicAuth.username = 'YOUR USERNAME';
BasicAuth.password = 'YOUR PASSWORD';
// Configure API key authorization: ApiKeyAuth
let ApiKeyAuth = defaultClient.authentications['ApiKeyAuth'];
ApiKeyAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ApiKeyAuth.apiKeyPrefix = 'Token';

let apiInstance = new ManagementApi.TerminalActionsCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let actionId = "actionId_example"; // String | The unique identifier of the terminal action.
apiInstance.getCompaniesCompanyIdTerminalActionsActionId(companyId, actionId, (error, data, response) => {
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
 **companyId** | **String**| The unique identifier of the company account. | 
 **actionId** | **String**| The unique identifier of the terminal action. | 

### Return type

[**ExternalTerminalAction**](ExternalTerminalAction.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

