# SeveraPublicRestApiDocumentation.ProjectsDeleteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywordsDeleteProjectKeyword**](ProjectsDeleteApi.md#keywordsDeleteProjectKeyword) | **DELETE** /v1/projects/{projectGuid}/keywords/{guid} | Delete a keyword from the project
[**phaseMembersDeletePhaseMember**](ProjectsDeleteApi.md#phaseMembersDeletePhaseMember) | **DELETE** /v1/phasemembers/{userGuid} | Deletes a phase member
[**phasesDeletePhase**](ProjectsDeleteApi.md#phasesDeletePhase) | **DELETE** /v1/phases/{guid} | Deletes a phase
[**projectCustomValuesDeleteProjectCustomValue**](ProjectsDeleteApi.md#projectCustomValuesDeleteProjectCustomValue) | **DELETE** /v1/projects/customvalues/{guid} | Deletes a project custom value.
[**projectForecastsDeleteForecast**](ProjectsDeleteApi.md#projectForecastsDeleteForecast) | **DELETE** /v1/projectforecasts/{guid} | Delete a project forecast
[**projectForecastsDeleteForecasts**](ProjectsDeleteApi.md#projectForecastsDeleteForecasts) | **DELETE** /v1/projects/{projectGuid}/projectforecasts | Delete the project forecasts from a month onward, including the given month.
[**projectInvoiceSettingsDeleteProjectInvoiceSettings_0**](ProjectsDeleteApi.md#projectInvoiceSettingsDeleteProjectInvoiceSettings_0) | **DELETE** /v1/projectinvoicesettings/{guid} | Delete an project invoice settings.
[**projectProductsDeleteAllProjectProducts**](ProjectsDeleteApi.md#projectProductsDeleteAllProjectProducts) | **DELETE** /v1/projects/{projectGuid}/projectproducts | Deletes all project products of a project.
[**projectProductsDeleteProjectProduct**](ProjectsDeleteApi.md#projectProductsDeleteProjectProduct) | **DELETE** /v1/projectproducts/{guid} | Deletes a project product.
[**projectWorkHourPricesDeleteProjectWorkHourPrice**](ProjectsDeleteApi.md#projectWorkHourPricesDeleteProjectWorkHourPrice) | **DELETE** /v1/projectworkhourprices/{guid} | Deletes a work hour price
[**projectWorkTypesDeleteProjectWorktype**](ProjectsDeleteApi.md#projectWorkTypesDeleteProjectWorktype) | **DELETE** /v1/projectworktypes/{guid} | Deletes a project work type.
[**projectsDeleteProject**](ProjectsDeleteApi.md#projectsDeleteProject) | **DELETE** /v1/projects/{guid} | Delete a project
[**proposalFeesDeleteProposalFee**](ProjectsDeleteApi.md#proposalFeesDeleteProposalFee) | **DELETE** /v1/proposalfeerows/{guid} | Delete a proposal fee row
[**proposalSubtotalsDeleteProposalSubtotal**](ProjectsDeleteApi.md#proposalSubtotalsDeleteProposalSubtotal) | **DELETE** /v1/proposalsubtotals/{guid} | Delete a proposal subtotal
[**proposalWorkhoursDeleteProposalWorkhour**](ProjectsDeleteApi.md#proposalWorkhoursDeleteProposalWorkhour) | **DELETE** /v1/proposalworkrows/{guid} | Delete a proposal work row.
[**proposalsDeleteProposal**](ProjectsDeleteApi.md#proposalsDeleteProposal) | **DELETE** /v1/proposals/{guid} | Delete a proposal
[**salesNotesDeleteProjectSalesNote**](ProjectsDeleteApi.md#salesNotesDeleteProjectSalesNote) | **DELETE** /v1/projectsalesnotes/{guid} | Deletes a project sales note.



## keywordsDeleteProjectKeyword

> keywordsDeleteProjectKeyword(projectGuid, guid)

Delete a keyword from the project

Returns: No Content (204) if succeeded. Not found (404) if the keyword or the link can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let projectGuid = "projectGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsDeleteProjectKeyword(projectGuid, guid, (error, data, response) => {
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
 **projectGuid** | **String**|  | 
 **guid** | **String**|  | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseMembersDeletePhaseMember

> phaseMembersDeletePhaseMember(userGuid, opts)

Deletes a phase member

Returns: No Content (204) if succeeded. Only one of transferToRoleGuid and transferToUserGuid can be provided. Use root phase to delete a project member.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let userGuid = "userGuid_example"; // String | GUID of the phase member to remove
let opts = {
  'resourceAllocationAction': new SeveraPublicRestApiDocumentation.ResourceAllocationAction(), // ResourceAllocationAction | Optional: The action to be applied to the user's resource allocations
  'transferToUserGuid': "transferToUserGuid_example", // String | Optional: GUID of the user to whom the resource allocations are transferred.
  'phaseMemberModel': new SeveraPublicRestApiDocumentation.PhaseMemberModel() // PhaseMemberModel | 
};
apiInstance.phaseMembersDeletePhaseMember(userGuid, opts, (error, data, response) => {
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
 **userGuid** | **String**| GUID of the phase member to remove | 
 **resourceAllocationAction** | [**ResourceAllocationAction**](.md)| Optional: The action to be applied to the user&#39;s resource allocations | [optional] 
 **transferToUserGuid** | **String**| Optional: GUID of the user to whom the resource allocations are transferred. | [optional] 
 **phaseMemberModel** | [**PhaseMemberModel**](PhaseMemberModel.md)|  | [optional] 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phasesDeletePhase

> phasesDeletePhase(guid)

Deletes a phase

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the phase.
apiInstance.phasesDeletePhase(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the phase. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomValuesDeleteProjectCustomValue

> projectCustomValuesDeleteProjectCustomValue(guid)

Deletes a project custom value.

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the project custom value.
apiInstance.projectCustomValuesDeleteProjectCustomValue(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the project custom value. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectForecastsDeleteForecast

> projectForecastsDeleteForecast(guid)

Delete a project forecast

Returns: No Content (204) if succeeded. Not found (404) if product can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | ID for the project forecast to delete
apiInstance.projectForecastsDeleteForecast(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the project forecast to delete | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectForecastsDeleteForecasts

> projectForecastsDeleteForecasts(projectGuid, opts)

Delete the project forecasts from a month onward, including the given month.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let projectGuid = "projectGuid_example"; // String | Project for the forecasts to delete
let opts = {
  'year': 56, // Number | Year where to start deleting the forecasts
  'month': 56 // Number | Month where to start deleting the forecasts
};
apiInstance.projectForecastsDeleteForecasts(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Project for the forecasts to delete | 
 **year** | **Number**| Year where to start deleting the forecasts | [optional] 
 **month** | **Number**| Month where to start deleting the forecasts | [optional] 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectInvoiceSettingsDeleteProjectInvoiceSettings_0

> projectInvoiceSettingsDeleteProjectInvoiceSettings_0(guid)

Delete an project invoice settings.

Returns: No Content (204) if succeeded. Not found (404) if project invoice settings can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | ID for the project invoice settings to delete.
apiInstance.projectInvoiceSettingsDeleteProjectInvoiceSettings_0(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the project invoice settings to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectProductsDeleteAllProjectProducts

> projectProductsDeleteAllProjectProducts(projectGuid)

Deletes all project products of a project.

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let projectGuid = "projectGuid_example"; // String | GUID of the project from where project products to remove.
apiInstance.projectProductsDeleteAllProjectProducts(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**| GUID of the project from where project products to remove. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectProductsDeleteProjectProduct

> projectProductsDeleteProjectProduct(guid)

Deletes a project product.

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | GUID of the project product to remove.
apiInstance.projectProductsDeleteProjectProduct(guid, (error, data, response) => {
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
 **guid** | **String**| GUID of the project product to remove. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectWorkHourPricesDeleteProjectWorkHourPrice

> projectWorkHourPricesDeleteProjectWorkHourPrice(guid)

Deletes a work hour price

Returns: No Content (204) if succeeded.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the work hour price.
apiInstance.projectWorkHourPricesDeleteProjectWorkHourPrice(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the work hour price. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectWorkTypesDeleteProjectWorktype

> projectWorkTypesDeleteProjectWorktype(guid)

Deletes a project work type.

Returns: No Content (204) if succeeded. The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | GUID of the project work type to remove.
apiInstance.projectWorkTypesDeleteProjectWorktype(guid, (error, data, response) => {
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
 **guid** | **String**| GUID of the project work type to remove. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsDeleteProject

> projectsDeleteProject(guid)

Delete a project

Returns: No Content (204) if succeeded. Not found (404) if project can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | ID for the project to delete
apiInstance.projectsDeleteProject(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the project to delete | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalFeesDeleteProposalFee

> proposalFeesDeleteProposalFee(guid)

Delete a proposal fee row

Returns: No Content (204) if succeeded. Not found (404) if proposal fee row can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | ID for the proposal fee row to delete
apiInstance.proposalFeesDeleteProposalFee(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the proposal fee row to delete | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalSubtotalsDeleteProposalSubtotal

> proposalSubtotalsDeleteProposalSubtotal(guid)

Delete a proposal subtotal

Returns: No Content (204) if succeeded. Not found (404) if proposal subtotal can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | ID for the proposal subtotal to delete.
apiInstance.proposalSubtotalsDeleteProposalSubtotal(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the proposal subtotal to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalWorkhoursDeleteProposalWorkhour

> proposalWorkhoursDeleteProposalWorkhour(guid)

Delete a proposal work row.

Returns: No Content (204) if succeeded. Not found (404) if proposal work row can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | ID for the proposal work row to delete.
apiInstance.proposalWorkhoursDeleteProposalWorkhour(guid, (error, data, response) => {
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
 **guid** | **String**| ID for the proposal work row to delete. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalsDeleteProposal

> proposalsDeleteProposal(guid)

Delete a proposal

Returns: No Content (204) if succeeded. Not found (404) if proposal can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | Guid for the proposal to delete
apiInstance.proposalsDeleteProposal(guid, (error, data, response) => {
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
 **guid** | **String**| Guid for the proposal to delete | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesDeleteProjectSalesNote

> salesNotesDeleteProjectSalesNote(guid)

Deletes a project sales note.

Returns: No Content (204) if succeeded. OK (200) if note has child notes and can&#39;t be deleted. It is marked as IsDeleted &#x3D; true. Not found (404) if note can&#39;t be found.

### Example

```javascript
import SeveraPublicRestApiDocumentation from 'severa_public_rest_api_documentation';
let defaultClient = SeveraPublicRestApiDocumentation.ApiClient.instance;
// Configure API key authorization: ClientIdAuth
let ClientIdAuth = defaultClient.authentications['ClientIdAuth'];
ClientIdAuth.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//ClientIdAuth.apiKeyPrefix = 'Token';
// Configure OAuth2 access token for authorization: OAuth2
let OAuth2 = defaultClient.authentications['OAuth2'];
OAuth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsDeleteApi();
let guid = "guid_example"; // String | GUID used to delete the project sales note.
apiInstance.salesNotesDeleteProjectSalesNote(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to delete the project sales note. | 

### Return type

null (empty response body)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

