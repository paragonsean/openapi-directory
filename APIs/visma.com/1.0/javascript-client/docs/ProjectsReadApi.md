# SeveraPublicRestApiDocumentation.ProjectsReadApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywordsGetProjectKeywords**](ProjectsReadApi.md#keywordsGetProjectKeywords) | **GET** /v1/projects/{projectGuid}/keywords | Get all the keywords for project.
[**overtimePricesGetOvertimePricesForProject**](ProjectsReadApi.md#overtimePricesGetOvertimePricesForProject) | **GET** /v1/projects/{projectGuid}/overtimeprices | Get all the overtimePrices for a project.
[**phaseMembersGetAllDeletedPhaseMembers**](ProjectsReadApi.md#phaseMembersGetAllDeletedPhaseMembers) | **GET** /v1/deletedphasemembers | Get all deleted phase members
[**phaseMembersGetAllPhaseMembers**](ProjectsReadApi.md#phaseMembersGetAllPhaseMembers) | **GET** /v1/phasemembers | Get all active phase members
[**phaseMembersGetPhaseMembers**](ProjectsReadApi.md#phaseMembersGetPhaseMembers) | **GET** /v1/phases/{phaseGuid}/phasemembers | Get phase members
[**phasesGetPhase**](ProjectsReadApi.md#phasesGetPhase) | **GET** /v1/phases/{guid} | Get phase by ID
[**phasesGetPhases**](ProjectsReadApi.md#phasesGetPhases) | **GET** /v1/phases | Get the phases.
[**phasesGetProjectPhases**](ProjectsReadApi.md#phasesGetProjectPhases) | **GET** /v1/projects/{guid}/phaseswithhierarchy | Get project&#39;s phases as flat list
[**phasesGetRootPhases**](ProjectsReadApi.md#phasesGetRootPhases) | **GET** /v1/rootphaseswithhierarchy | Get a list of root phases with information about hierarchy.
[**productPricesGetProductPricesForProject**](ProjectsReadApi.md#productPricesGetProductPricesForProject) | **GET** /v1/projects/{projectGuid}/productprices | Get all the productPrices for a project.
[**productsGetSearchedProducts**](ProjectsReadApi.md#productsGetSearchedProducts) | **GET** /v1/projects/{projectGuid}/productsforproject | Gets available products for the given project where price information comes from projects price list
[**projectBillingCustomersGetWorkHourPricesForProject**](ProjectsReadApi.md#projectBillingCustomersGetWorkHourPricesForProject) | **GET** /v1/projects/{projectGuid}/projectbillingcustomers | Get all the billing customers for a project
[**projectCustomValuesGetProjectCustomValue**](ProjectsReadApi.md#projectCustomValuesGetProjectCustomValue) | **GET** /v1/projects/customvalues/{guid} | Get project custom value by ID.
[**projectCustomValuesGetProjectCustomValues**](ProjectsReadApi.md#projectCustomValuesGetProjectCustomValues) | **GET** /v1/projects/{projectGuid}/customvalues | Get the project custom values.
[**projectForecastsGetForecast**](ProjectsReadApi.md#projectForecastsGetForecast) | **GET** /v1/projectforecasts/{guid} | Get project forecast by ID
[**projectForecastsGetForecasts**](ProjectsReadApi.md#projectForecastsGetForecasts) | **GET** /v1/projects/{projectGuid}/projectforecasts | Get the project forecasts
[**projectInvoiceSettingsGetProjectInvoiceSetting_0**](ProjectsReadApi.md#projectInvoiceSettingsGetProjectInvoiceSetting_0) | **GET** /v1/projectinvoicesettings/{guid} | Get project invoice settings by ID.
[**projectInvoiceSettingsGetProjectInvoiceSettings_0**](ProjectsReadApi.md#projectInvoiceSettingsGetProjectInvoiceSettings_0) | **GET** /v1/projects/{projectGuid}/projectinvoicesettings | Get project invoice settings by project ID.
[**projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject**](ProjectsReadApi.md#projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject) | **GET** /v1/projects/{projectGuid}/projectmembercostexceptions | Get all cost exceptions of project members for a project.
[**projectProductsGetProjectProducts**](ProjectsReadApi.md#projectProductsGetProjectProducts) | **GET** /v1/projects/{projectGuid}/projectproducts | Get project products
[**projectWorkHourPricesGetProjectWorkHourPrice**](ProjectsReadApi.md#projectWorkHourPricesGetProjectWorkHourPrice) | **GET** /v1/projectworkhourprices/{guid} | Get project work hour price by ID
[**projectWorkHourPricesGetWorkHourPricesForProject**](ProjectsReadApi.md#projectWorkHourPricesGetWorkHourPricesForProject) | **GET** /v1/projects/{projectGuid}/projectworkhourprices | Get all the work hour prices for a project
[**projectWorkTypesGetProjectWorktypes**](ProjectsReadApi.md#projectWorkTypesGetProjectWorktypes) | **GET** /v1/projects/{projectGuid}/projectworktypes | Get project work types.
[**projectsGetCustomerProjects**](ProjectsReadApi.md#projectsGetCustomerProjects) | **GET** /v1/customers/{customerGuid}/projects | Get customer&#39;s projects
[**projectsGetProject**](ProjectsReadApi.md#projectsGetProject) | **GET** /v1/projects/{guid} | Get project by ID
[**projectsGetProjects**](ProjectsReadApi.md#projectsGetProjects) | **GET** /v1/projects | Get all the projects
[**projectsGetSalesCases**](ProjectsReadApi.md#projectsGetSalesCases) | **GET** /v1/salescases | Gets the sales cases (sales status is in progress)
[**proposalFeesGetProposalFee**](ProjectsReadApi.md#proposalFeesGetProposalFee) | **GET** /v1/proposalfeerows/{guid} | Get the proposal fee rows by guid
[**proposalFeesGetProposalFees**](ProjectsReadApi.md#proposalFeesGetProposalFees) | **GET** /v1/proposalfeerows | Get the proposal fee rows.
[**proposalFeesGetProposalFeesForProposal**](ProjectsReadApi.md#proposalFeesGetProposalFeesForProposal) | **GET** /v1/proposals/{proposalGuid}/proposalfeerows | Get all the proposal fee rows for a proposal
[**proposalSettingsGetProposalSettings**](ProjectsReadApi.md#proposalSettingsGetProposalSettings) | **GET** /v1/proposals/{guid}/proposalsettings | Get settings for a proposal
[**proposalSubtotalsGetProposalSubtotal**](ProjectsReadApi.md#proposalSubtotalsGetProposalSubtotal) | **GET** /v1/proposalsubtotals/{guid} | Get Proposal subtotal by ID
[**proposalSubtotalsGetProposalSubtotals**](ProjectsReadApi.md#proposalSubtotalsGetProposalSubtotals) | **GET** /v1/proposalsubtotals | Get the proposal subtotals.
[**proposalSubtotalsGetProposalSubtotalsForProposal**](ProjectsReadApi.md#proposalSubtotalsGetProposalSubtotalsForProposal) | **GET** /v1/proposals/{proposalGuid}/proposalsubtotals | Get all the proposal subtotals for a proposal
[**proposalWorkhoursGetProposalWorkHours**](ProjectsReadApi.md#proposalWorkhoursGetProposalWorkHours) | **GET** /v1/proposalworkrows | Get the proposal work rows.
[**proposalWorkhoursGetProposalWorkHoursForProposal**](ProjectsReadApi.md#proposalWorkhoursGetProposalWorkHoursForProposal) | **GET** /v1/proposals/{proposalGuid}/proposalworkrows | Get all the proposal work rows.
[**proposalWorkhoursGetProposalWorkhour**](ProjectsReadApi.md#proposalWorkhoursGetProposalWorkhour) | **GET** /v1/proposalworkrows/{guid} | Get the proposal work row by guid.
[**proposalsGetProposal**](ProjectsReadApi.md#proposalsGetProposal) | **GET** /v1/proposals/{guid} | Get Proposal by ID
[**proposalsGetProposals**](ProjectsReadApi.md#proposalsGetProposals) | **GET** /v1/proposals | Get all the proposals
[**proposalsGetProposalsForProject**](ProjectsReadApi.md#proposalsGetProposalsForProject) | **GET** /v1/projects/{projectGuid}/proposals | Get all the proposals for a project
[**salesNotesGetAllCustomerSalesNotes**](ProjectsReadApi.md#salesNotesGetAllCustomerSalesNotes) | **GET** /v1/customers/{customerGuid}/salesnotes | Get the sales notes by customer guid.
[**salesNotesGetProjectSalesNote**](ProjectsReadApi.md#salesNotesGetProjectSalesNote) | **GET** /v1/projectsalesnotes/{guid} | Get project sales note by ID.
[**salesNotesGetProjectSalesNotes**](ProjectsReadApi.md#salesNotesGetProjectSalesNotes) | **GET** /v1/projects/{projectGuid}/projectsalesnotes | Get the sales notes of a case.
[**salesStatusHistoryGetSalesStatusHistory**](ProjectsReadApi.md#salesStatusHistoryGetSalesStatusHistory) | **GET** /v1/projects/{projectGuid}/salesstatushistory | Get the sales status history for a project
[**teamProductivityGetTeamProductivity**](ProjectsReadApi.md#teamProductivityGetTeamProductivity) | **GET** /v1/projects/{projectGuid}/teamproductivity | Get team productivity of a project.
[**travelExpenseTypesGetSearchedTravelExpenseTypes**](ProjectsReadApi.md#travelExpenseTypesGetSearchedTravelExpenseTypes) | **GET** /v1/projects/{projectGuid}/travelexpensetypes | Search active travel expense types of project by part of the name or code.
[**travelPricesGetTravelPricesForProject**](ProjectsReadApi.md#travelPricesGetTravelPricesForProject) | **GET** /v1/projects/{projectGuid}/travelprices | Get all the travel prices for a project.
[**workTypesGetPhaseWorkTypes**](ProjectsReadApi.md#workTypesGetPhaseWorkTypes) | **GET** /v1/phases/{phaseGuid}/worktypes | Get all work types that are available for a phase (for work hour entry)
[**workTypesGetSearchedWorktypes**](ProjectsReadApi.md#workTypesGetSearchedWorktypes) | **GET** /v1/projects/{projectGuid}/worktypesforproject | Search active work types by part of the name or code.



## keywordsGetProjectKeywords

> [ProjectKeywordModel] keywordsGetProjectKeywords(projectGuid, opts)

Get all the keywords for project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project for which keywords are requested.
let opts = {
  'active': true, // Boolean | If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Keyword&sortings[0].value=Desc\".
};
apiInstance.keywordsGetProjectKeywords(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project for which keywords are requested. | 
 **active** | **Boolean**| If not given, return all Keywords, if given as true return only active Keywords, if given as false returns only inactive Keywords. | [optional] 
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (submodel fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Keyword&amp;sortings[0].value&#x3D;Desc\&quot;. | [optional] 

### Return type

[**[ProjectKeywordModel]**](ProjectKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## overtimePricesGetOvertimePricesForProject

> [OvertimePriceModel] overtimePricesGetOvertimePricesForProject(projectGuid)

Get all the overtimePrices for a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | 
apiInstance.overtimePricesGetOvertimePricesForProject(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**|  | 

### Return type

[**[OvertimePriceModel]**](OvertimePriceModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseMembersGetAllDeletedPhaseMembers

> [DeletedPhaseMemberOutputModel] phaseMembersGetAllDeletedPhaseMembers(opts)

Get all deleted phase members

Use root phase to get project members.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'deletedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get phase members that have been added or changed after this date time (greater or equal).
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'isUserActive': true // Boolean | Optional: Is the user active. Default nothing = all.
};
apiInstance.phaseMembersGetAllDeletedPhaseMembers(opts, (error, data, response) => {
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
 **deletedSince** | **Date**| Optional: Get phase members that have been added or changed after this date time (greater or equal). | [optional] 
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **isUserActive** | **Boolean**| Optional: Is the user active. Default nothing &#x3D; all. | [optional] 

### Return type

[**[DeletedPhaseMemberOutputModel]**](DeletedPhaseMemberOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseMembersGetAllPhaseMembers

> [PhaseMemberOutputModel] phaseMembersGetAllPhaseMembers(opts)

Get all active phase members

Use root phase to get project members.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get phase members that have been added or changed after this date time (greater or equal).
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'isUserActive': true // Boolean | Optional: Is the user active. Default nothing = all.
};
apiInstance.phaseMembersGetAllPhaseMembers(opts, (error, data, response) => {
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
 **changedSince** | **Date**| Optional: Get phase members that have been added or changed after this date time (greater or equal). | [optional] 
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **isUserActive** | **Boolean**| Optional: Is the user active. Default nothing &#x3D; all. | [optional] 

### Return type

[**[PhaseMemberOutputModel]**](PhaseMemberOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseMembersGetPhaseMembers

> [PhaseMemberOutputModel] phaseMembersGetPhaseMembers(phaseGuid, opts)

Get phase members

Use root phase to get project members.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let phaseGuid = "phaseGuid_example"; // String | GUID of the phase.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch.
  'isActive': true, // Boolean | Optional: Is the member active on the phase. Filters only root phase members. Default nothing = all.
  'isUserActive': true // Boolean | Optional: Is the user active. Default nothing = all.
};
apiInstance.phaseMembersGetPhaseMembers(phaseGuid, opts, (error, data, response) => {
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
 **phaseGuid** | **String**| GUID of the phase. | 
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch. | [optional] 
 **isActive** | **Boolean**| Optional: Is the member active on the phase. Filters only root phase members. Default nothing &#x3D; all. | [optional] 
 **isUserActive** | **Boolean**| Optional: Is the user active. Default nothing &#x3D; all. | [optional] 

### Return type

[**[PhaseMemberOutputModel]**](PhaseMemberOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phasesGetPhase

> PhaseOutputModel phasesGetPhase(guid)

Get phase by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | Id used to get the phase.
apiInstance.phasesGetPhase(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the phase. | 

### Return type

[**PhaseOutputModel**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phasesGetPhases

> [PhaseOutputModel] phasesGetPhases(opts)

Get the phases.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get phases that have been added or changed after this date time (greater or equal).
  'code': "''", // String | Optional: Code of the phase.
  'projectGuids': ["null"] // [String] | Optional: List of project ids.
};
apiInstance.phasesGetPhases(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get phases that have been added or changed after this date time (greater or equal). | [optional] 
 **code** | **String**| Optional: Code of the phase. | [optional] [default to &#39;&#39;]
 **projectGuids** | [**[String]**](String.md)| Optional: List of project ids. | [optional] 

### Return type

[**[PhaseOutputModel]**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phasesGetProjectPhases

> [PhaseModelWithHierarchyInfo] phasesGetProjectPhases(guid)

Get project&#39;s phases as flat list

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | Id of the project.
apiInstance.phasesGetProjectPhases(guid, (error, data, response) => {
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
 **guid** | **String**| Id of the project. | 

### Return type

[**[PhaseModelWithHierarchyInfo]**](PhaseModelWithHierarchyInfo.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phasesGetRootPhases

> [PhaseOutputModel] phasesGetRootPhases(opts)

Get a list of root phases with information about hierarchy.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'customerGuids': ["null"], // [String] | 
  'projectGuids': ["null"], // [String] | 
  'projectKeywordGuids': ["null"], // [String] | 
  'projectStatusTypeGuids': ["null"], // [String] | 
  'salesPersonGuids': ["null"], // [String] | 
  'projectOwnerGuids': ["null"], // [String] | 
  'businessUnitGuids': ["null"], // [String] | 
  'customerOwnerGuids': ["null"], // [String] | 
  'salesStatusTypeGuids': ["null"], // [String] | 
  'openProjects': true, // Boolean | 
  'projectMemberUserGuids': ["null"] // [String] | 
};
apiInstance.phasesGetRootPhases(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **customerGuids** | [**[String]**](String.md)|  | [optional] 
 **projectGuids** | [**[String]**](String.md)|  | [optional] 
 **projectKeywordGuids** | [**[String]**](String.md)|  | [optional] 
 **projectStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **salesPersonGuids** | [**[String]**](String.md)|  | [optional] 
 **projectOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **businessUnitGuids** | [**[String]**](String.md)|  | [optional] 
 **customerOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **salesStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **openProjects** | **Boolean**|  | [optional] 
 **projectMemberUserGuids** | [**[String]**](String.md)|  | [optional] 

### Return type

[**[PhaseOutputModel]**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productPricesGetProductPricesForProject

> [ProductPriceOutputModel] productPricesGetProductPricesForProject(projectGuid, opts)

Get all the productPrices for a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'fromPricelistOnly': false, // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from Product name.
  'calculateRowCount': false, // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
  'isAvailable': true, // Boolean | Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all.
  'productCode': "''", // String | Optional: Absolute search for products with specified product code.
  'productGuids': ["null"], // [String] | Optional: Search all product price(s) by products guid(s).
  'isVolumePriced': true, // Boolean | Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products.
  'productCategoryGuids': ["null"], // [String] | Optional: Search product prices according to product category / categories by product category guid(s).
  'productTypes': [new SeveraPublicRestApiDocumentation.ProductType()] // [ProductType] | Optional: Search product prices according to product type / types.
};
apiInstance.productPricesGetProductPricesForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 
 **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false]
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false]
 **isAvailable** | **Boolean**| Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all. | [optional] 
 **productCode** | **String**| Optional: Absolute search for products with specified product code. | [optional] [default to &#39;&#39;]
 **productGuids** | [**[String]**](String.md)| Optional: Search all product price(s) by products guid(s). | [optional] 
 **isVolumePriced** | **Boolean**| Optional: If true, return only volume priced products. If false, return all non volume priced products. Default is null, which means return all products. | [optional] 
 **productCategoryGuids** | [**[String]**](String.md)| Optional: Search product prices according to product category / categories by product category guid(s). | [optional] 
 **productTypes** | [**[ProductType]**](ProductType.md)| Optional: Search product prices according to product type / types. | [optional] 

### Return type

[**[ProductPriceOutputModel]**](ProductPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## productsGetSearchedProducts

> [ProductForProjectOutputModel] productsGetSearchedProducts(projectGuid, opts)

Gets available products for the given project where price information comes from projects price list

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Id of the project
let opts = {
  'rowCount': 56, // Number | Optional: Number of rows to fetch
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'type': new SeveraPublicRestApiDocumentation.ProductType(), // ProductType | Product type. if given, it filters the products by the given type
  'includeProductsFromRegistry': false // Boolean | Optional: If true returns all the products from registry with project specific prices. If false returns only products specified for the project with project specific prices. Default false.
};
apiInstance.productsGetSearchedProducts(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Id of the project | 
 **rowCount** | **Number**| Optional: Number of rows to fetch | [optional] 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **type** | [**ProductType**](.md)| Product type. if given, it filters the products by the given type | [optional] 
 **includeProductsFromRegistry** | **Boolean**| Optional: If true returns all the products from registry with project specific prices. If false returns only products specified for the project with project specific prices. Default false. | [optional] [default to false]

### Return type

[**[ProductForProjectOutputModel]**](ProductForProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectBillingCustomersGetWorkHourPricesForProject

> [ProjectBillingCustomerModel] projectBillingCustomersGetWorkHourPricesForProject(projectGuid)

Get all the billing customers for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | 
apiInstance.projectBillingCustomersGetWorkHourPricesForProject(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**|  | 

### Return type

[**[ProjectBillingCustomerModel]**](ProjectBillingCustomerModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomValuesGetProjectCustomValue

> ProjectCustomValueModel projectCustomValuesGetProjectCustomValue(guid)

Get project custom value by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | Id used to get the project custom value.
apiInstance.projectCustomValuesGetProjectCustomValue(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the project custom value. | 

### Return type

[**ProjectCustomValueModel**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomValuesGetProjectCustomValues

> [ProjectCustomValueModel] projectCustomValuesGetProjectCustomValues(projectGuid, opts)

Get the project custom values.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'active': true, // Boolean | Optional: Get only values of active or inactive project custom properties.
  'target': ["null"], // [String] | List of target for which to get the values.
  'calculateRowCount': false, // Boolean | Optional: Calculate total number of rows.
  'sortings': [new SeveraPublicRestApiDocumentation.KeyValuePairOfStringAndSortDirection()] // [KeyValuePairOfStringAndSortDirection] | Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \"Desc\" or \"Asc\". Example: \"?sortings[0].key=Name&sortings[0].value=Desc&sortings[1].key=Number&sortings[1].value=Asc\".
};
apiInstance.projectCustomValuesGetProjectCustomValues(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **active** | **Boolean**| Optional: Get only values of active or inactive project custom properties. | [optional] 
 **target** | [**[String]**](String.md)| List of target for which to get the values. | [optional] 
 **calculateRowCount** | **Boolean**| Optional: Calculate total number of rows. | [optional] [default to false]
 **sortings** | [**[KeyValuePairOfStringAndSortDirection]**](KeyValuePairOfStringAndSortDirection.md)| Optional: A list of Key-Value pairs, containing names of fields and directions by which the results should be sorted. Any sortable field name (sub-model fields not supported) in the model can be used, while value can be \&quot;Desc\&quot; or \&quot;Asc\&quot;. Example: \&quot;?sortings[0].key&#x3D;Name&amp;sortings[0].value&#x3D;Desc&amp;sortings[1].key&#x3D;Number&amp;sortings[1].value&#x3D;Asc\&quot;. | [optional] 

### Return type

[**[ProjectCustomValueModel]**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectForecastsGetForecast

> ProjectForecastOutputModel projectForecastsGetForecast(guid)

Get project forecast by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | GUID used to get the project forecast.
apiInstance.projectForecastsGetForecast(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the project forecast. | 

### Return type

[**ProjectForecastOutputModel**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectForecastsGetForecasts

> [ProjectForecastOutputModel] projectForecastsGetForecasts(projectGuid, opts)

Get the project forecasts

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | project for the forecasts
let opts = {
  'startDate': new Date("2013-10-20T19:20:30+01:00"), // Date | Start date of the date range for the forecasts
  'endDate': new Date("2013-10-20T19:20:30+01:00") // Date | End date of the date range for the forecasts
};
apiInstance.projectForecastsGetForecasts(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| project for the forecasts | 
 **startDate** | **Date**| Start date of the date range for the forecasts | [optional] 
 **endDate** | **Date**| End date of the date range for the forecasts | [optional] 

### Return type

[**[ProjectForecastOutputModel]**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectInvoiceSettingsGetProjectInvoiceSetting_0

> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsGetProjectInvoiceSetting_0(guid)

Get project invoice settings by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | ID of the project invoice settings.
apiInstance.projectInvoiceSettingsGetProjectInvoiceSetting_0(guid, (error, data, response) => {
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
 **guid** | **String**| ID of the project invoice settings. | 

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectInvoiceSettingsGetProjectInvoiceSettings_0

> [ProjectInvoiceSettingsOutputModel] projectInvoiceSettingsGetProjectInvoiceSettings_0(projectGuid)

Get project invoice settings by project ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
apiInstance.projectInvoiceSettingsGetProjectInvoiceSettings_0(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 

### Return type

[**[ProjectInvoiceSettingsOutputModel]**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject

> [ProjectMemberCostExceptionOutputModel] projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject(projectGuid, opts)

Get all cost exceptions of project members for a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Guid of the project.
let opts = {
  'userGuid': "userGuid_example", // String | Optional: Guid of the user.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default 20, maximum 100.
};
apiInstance.projectMemberCostExceptionsGetProjectMemberCostExceptionsForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Guid of the project. | 
 **userGuid** | **String**| Optional: Guid of the user. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 

### Return type

[**[ProjectMemberCostExceptionOutputModel]**](ProjectMemberCostExceptionOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectProductsGetProjectProducts

> [ProjectProductOutputModel] projectProductsGetProjectProducts(projectGuid, opts)

Get project products

This is the same as organization&#39;s list of products, unless the project has some specific products and UseProductsFromSetting in project model is set to false.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | GUID of the project.
let opts = {
  'includeProductsFromRegistry': false, // Boolean | Optional: Includes products available from product registry
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'active': true // Boolean | Fetch only active
};
apiInstance.projectProductsGetProjectProducts(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| GUID of the project. | 
 **includeProductsFromRegistry** | **Boolean**| Optional: Includes products available from product registry | [optional] [default to false]
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **active** | **Boolean**| Fetch only active | [optional] 

### Return type

[**[ProjectProductOutputModel]**](ProjectProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectWorkHourPricesGetProjectWorkHourPrice

> ProjectWorkHourPriceOutputModel projectWorkHourPricesGetProjectWorkHourPrice(guid)

Get project work hour price by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | Id used to get the work hour price.
apiInstance.projectWorkHourPricesGetProjectWorkHourPrice(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the work hour price. | 

### Return type

[**ProjectWorkHourPriceOutputModel**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectWorkHourPricesGetWorkHourPricesForProject

> [ProjectWorkHourPriceOutputModel] projectWorkHourPricesGetWorkHourPricesForProject(projectGuid, opts)

Get all the work hour prices for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Guid of the project.
let opts = {
  'fromPricelistOnly': false, // Boolean | If true return only prices from the price list, if false also returns prices from the products. Default is false.
  'isAvailable': true, // Boolean | Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get project work hour prices that have been added or changed after this date time (greater or equal).
};
apiInstance.projectWorkHourPricesGetWorkHourPricesForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Guid of the project. | 
 **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the products. Default is false. | [optional] [default to false]
 **isAvailable** | **Boolean**| Optional: If true, returns only prices that are available for the project, false returns price that are not available. Default all. | [optional] 
 **changedSince** | **Date**| Optional: Get project work hour prices that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectWorkHourPriceOutputModel]**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectWorkTypesGetProjectWorktypes

> [ProjectWorkTypeModel] projectWorkTypesGetProjectWorktypes(projectGuid, opts)

Get project work types.

This is the same as organization&#39;s list of work types, unless the project has some specific work types and \&quot;UseWorktypesFromSetting\&quot; in project model is set to false.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | GUID of the project.
let opts = {
  'includeWorktypesFromRegistry': false, // Boolean | Include work types also from registry. If false, returns only project specific work types. Default false.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'active': true, // Boolean | If not given, return all work types, if given as true return only active work types, if given as false returns only inactive work types.
  'textToSearch': "''", // String | Optional: Text to search from work type name.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get project work types that have been added or changed after this date time (greater or equal).
};
apiInstance.projectWorkTypesGetProjectWorktypes(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| GUID of the project. | 
 **includeWorktypesFromRegistry** | **Boolean**| Include work types also from registry. If false, returns only project specific work types. Default false. | [optional] [default to false]
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **active** | **Boolean**| If not given, return all work types, if given as true return only active work types, if given as false returns only inactive work types. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from work type name. | [optional] [default to &#39;&#39;]
 **changedSince** | **Date**| Optional: Get project work types that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectWorkTypeModel]**](ProjectWorkTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetCustomerProjects

> [ProjectOutputModel] projectsGetCustomerProjects(customerGuid, opts)

Get customer&#39;s projects

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let customerGuid = "customerGuid_example"; // String | Id of the customer.
let opts = {
  'pageToken': "pageToken_example", // String | 
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'isBillable': true, // Boolean | Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing = all.
  'currencyGuids': ["null"], // [String] | 
  'projectGuids': ["null"], // [String] | 
  'projectKeywordGuids': ["null"], // [String] | 
  'projectStatusTypeGuids': ["null"], // [String] | 
  'salesPersonGuids': ["null"], // [String] | 
  'projectOwnerGuids': ["null"], // [String] | 
  'businessUnitGuids': ["null"], // [String] | 
  'minimumBillableAmount': 3.4, // Number | 
  'customerOwnerGuids': ["null"], // [String] | 
  'invoiceableDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'marketSegmentationGuids': ["null"], // [String] | 
  'salesStatusTypeGuids': ["null"], // [String] | 
  'isClosed': true, // Boolean | 
  'hasRecurringFees': true, // Boolean | 
  'companyCurrencyGuids': ["null"], // [String] | 
  'projectMemberUserGuids': ["null"], // [String] | 
  'numbers': [null] // [Number] | 
};
apiInstance.projectsGetCustomerProjects(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| Id of the customer. | 
 **pageToken** | **String**|  | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **isBillable** | **Boolean**| Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing &#x3D; all. | [optional] 
 **currencyGuids** | [**[String]**](String.md)|  | [optional] 
 **projectGuids** | [**[String]**](String.md)|  | [optional] 
 **projectKeywordGuids** | [**[String]**](String.md)|  | [optional] 
 **projectStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **salesPersonGuids** | [**[String]**](String.md)|  | [optional] 
 **projectOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **businessUnitGuids** | [**[String]**](String.md)|  | [optional] 
 **minimumBillableAmount** | **Number**|  | [optional] 
 **customerOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **invoiceableDate** | **Date**|  | [optional] 
 **marketSegmentationGuids** | [**[String]**](String.md)|  | [optional] 
 **salesStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **isClosed** | **Boolean**|  | [optional] 
 **hasRecurringFees** | **Boolean**|  | [optional] 
 **companyCurrencyGuids** | [**[String]**](String.md)|  | [optional] 
 **projectMemberUserGuids** | [**[String]**](String.md)|  | [optional] 
 **numbers** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**[ProjectOutputModel]**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetProject

> ProjectOutputModel projectsGetProject(guid)

Get project by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | Id used to get the project.
apiInstance.projectsGetProject(guid, (error, data, response) => {
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
 **guid** | **String**| Id used to get the project. | 

### Return type

[**ProjectOutputModel**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetProjects

> [ProjectOutputModel] projectsGetProjects(opts)

Get all the projects

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | 
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'currencyGuid': "currencyGuid_example", // String | Optional: ID of project currency.
  'changedSince': new Date("2013-10-20T19:20:30+01:00"), // Date | Optional: Get projects that have been added or changed after this date time (greater or equal).
  'isBillable': true, // Boolean | Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing = all.
  'customerGuids': ["null"], // [String] | 
  'projectGuids': ["null"], // [String] | 
  'projectKeywordGuids': ["null"], // [String] | 
  'projectStatusTypeGuids': ["null"], // [String] | 
  'salesPersonGuids': ["null"], // [String] | 
  'projectOwnerGuids': ["null"], // [String] | 
  'businessUnitGuids': ["null"], // [String] | 
  'minimumBillableAmount': 3.4, // Number | 
  'customerOwnerGuids': ["null"], // [String] | 
  'invoiceableDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'marketSegmentationGuids': ["null"], // [String] | 
  'salesStatusTypeGuids': ["null"], // [String] | 
  'isClosed': true, // Boolean | 
  'hasRecurringFees': true, // Boolean | 
  'companyCurrencyGuids': ["null"], // [String] | 
  'projectMemberUserGuids': ["null"], // [String] | 
  'numbers': [null], // [Number] | 
  'internal': true // Boolean | Optional: Get internal / non-internal projects.
};
apiInstance.projectsGetProjects(opts, (error, data, response) => {
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
 **pageToken** | **String**|  | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **currencyGuid** | **String**| Optional: ID of project currency. | [optional] 
 **changedSince** | **Date**| Optional: Get projects that have been added or changed after this date time (greater or equal). | [optional] 
 **isBillable** | **Boolean**| Optional: When true fetch projects that have something to bill, when false nothing to bill. Default nothing &#x3D; all. | [optional] 
 **customerGuids** | [**[String]**](String.md)|  | [optional] 
 **projectGuids** | [**[String]**](String.md)|  | [optional] 
 **projectKeywordGuids** | [**[String]**](String.md)|  | [optional] 
 **projectStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **salesPersonGuids** | [**[String]**](String.md)|  | [optional] 
 **projectOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **businessUnitGuids** | [**[String]**](String.md)|  | [optional] 
 **minimumBillableAmount** | **Number**|  | [optional] 
 **customerOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **invoiceableDate** | **Date**|  | [optional] 
 **marketSegmentationGuids** | [**[String]**](String.md)|  | [optional] 
 **salesStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **isClosed** | **Boolean**|  | [optional] 
 **hasRecurringFees** | **Boolean**|  | [optional] 
 **companyCurrencyGuids** | [**[String]**](String.md)|  | [optional] 
 **projectMemberUserGuids** | [**[String]**](String.md)|  | [optional] 
 **numbers** | [**[Number]**](Number.md)|  | [optional] 
 **internal** | **Boolean**| Optional: Get internal / non-internal projects. | [optional] 

### Return type

[**[ProjectOutputModel]**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectsGetSalesCases

> [ProjectOutputModel] projectsGetSalesCases(opts)

Gets the sales cases (sales status is in progress)

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | 
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'customerGuids': ["null"], // [String] | 
  'currencyGuids': ["null"], // [String] | 
  'projectGuids': ["null"], // [String] | 
  'projectKeywordGuids': ["null"], // [String] | 
  'projectStatusTypeGuids': ["null"], // [String] | 
  'salesPersonGuids': ["null"], // [String] | 
  'projectOwnerGuids': ["null"], // [String] | 
  'businessUnitGuids': ["null"], // [String] | 
  'minimumBillableAmount': 3.4, // Number | 
  'customerOwnerGuids': ["null"], // [String] | 
  'invoiceableDate': new Date("2013-10-20T19:20:30+01:00"), // Date | 
  'marketSegmentationGuids': ["null"], // [String] | 
  'salesStatusTypeGuids': ["null"], // [String] | 
  'isClosed': true, // Boolean | 
  'hasRecurringFees': true, // Boolean | 
  'companyCurrencyGuids': ["null"], // [String] | 
  'projectMemberUserGuids': ["null"], // [String] | 
  'numbers': [null] // [Number] | 
};
apiInstance.projectsGetSalesCases(opts, (error, data, response) => {
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
 **pageToken** | **String**|  | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **customerGuids** | [**[String]**](String.md)|  | [optional] 
 **currencyGuids** | [**[String]**](String.md)|  | [optional] 
 **projectGuids** | [**[String]**](String.md)|  | [optional] 
 **projectKeywordGuids** | [**[String]**](String.md)|  | [optional] 
 **projectStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **salesPersonGuids** | [**[String]**](String.md)|  | [optional] 
 **projectOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **businessUnitGuids** | [**[String]**](String.md)|  | [optional] 
 **minimumBillableAmount** | **Number**|  | [optional] 
 **customerOwnerGuids** | [**[String]**](String.md)|  | [optional] 
 **invoiceableDate** | **Date**|  | [optional] 
 **marketSegmentationGuids** | [**[String]**](String.md)|  | [optional] 
 **salesStatusTypeGuids** | [**[String]**](String.md)|  | [optional] 
 **isClosed** | **Boolean**|  | [optional] 
 **hasRecurringFees** | **Boolean**|  | [optional] 
 **companyCurrencyGuids** | [**[String]**](String.md)|  | [optional] 
 **projectMemberUserGuids** | [**[String]**](String.md)|  | [optional] 
 **numbers** | [**[Number]**](Number.md)|  | [optional] 

### Return type

[**[ProjectOutputModel]**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalFeesGetProposalFee

> ProposalFeeRowOutputModel proposalFeesGetProposalFee(guid)

Get the proposal fee rows by guid

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | proposal fee row id to get
apiInstance.proposalFeesGetProposalFee(guid, (error, data, response) => {
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
 **guid** | **String**| proposal fee row id to get | 

### Return type

[**ProposalFeeRowOutputModel**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalFeesGetProposalFees

> [ProposalFeeRowOutputModel] proposalFeesGetProposalFees(opts)

Get the proposal fee rows.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get proposal fee rows that have been added or changed after this date time (greater or equal).
};
apiInstance.proposalFeesGetProposalFees(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get proposal fee rows that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProposalFeeRowOutputModel]**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalFeesGetProposalFeesForProposal

> [ProposalFeeRowOutputModel] proposalFeesGetProposalFeesForProposal(proposalGuid, opts)

Get all the proposal fee rows for a proposal

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let proposalGuid = "proposalGuid_example"; // String | proposal id for which to get proposal fees rows.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default all.
};
apiInstance.proposalFeesGetProposalFeesForProposal(proposalGuid, opts, (error, data, response) => {
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
 **proposalGuid** | **String**| proposal id for which to get proposal fees rows. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 

### Return type

[**[ProposalFeeRowOutputModel]**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalSettingsGetProposalSettings

> ProposalSettingsOutputModel proposalSettingsGetProposalSettings(guid)

Get settings for a proposal

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | GUID used to get the Proposal.
apiInstance.proposalSettingsGetProposalSettings(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the Proposal. | 

### Return type

[**ProposalSettingsOutputModel**](ProposalSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalSubtotalsGetProposalSubtotal

> ProposalSubtotalOutputModel proposalSubtotalsGetProposalSubtotal(guid)

Get Proposal subtotal by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | GUID used to get the Proposal subtotal.
apiInstance.proposalSubtotalsGetProposalSubtotal(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the Proposal subtotal. | 

### Return type

[**ProposalSubtotalOutputModel**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalSubtotalsGetProposalSubtotals

> [ProposalSubtotalOutputModel] proposalSubtotalsGetProposalSubtotals(opts)

Get the proposal subtotals.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get proposal subtotals that have been added or changed after this date time (greater or equal).
};
apiInstance.proposalSubtotalsGetProposalSubtotals(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get proposal subtotals that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProposalSubtotalOutputModel]**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalSubtotalsGetProposalSubtotalsForProposal

> [ProposalSubtotalOutputModel] proposalSubtotalsGetProposalSubtotalsForProposal(proposalGuid, opts)

Get all the proposal subtotals for a proposal

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let proposalGuid = "proposalGuid_example"; // String | proposal id for which to get proposal subtotals.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: Page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default all.
};
apiInstance.proposalSubtotalsGetProposalSubtotalsForProposal(proposalGuid, opts, (error, data, response) => {
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
 **proposalGuid** | **String**| proposal id for which to get proposal subtotals. | 
 **pageToken** | **String**| Optional: Page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 

### Return type

[**[ProposalSubtotalOutputModel]**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalWorkhoursGetProposalWorkHours

> [ProposalWorkhourRowOutputModel] proposalWorkhoursGetProposalWorkHours(opts)

Get the proposal work rows.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get proposal work rows that have been added or changed after this date time (greater or equal).
};
apiInstance.proposalWorkhoursGetProposalWorkHours(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get proposal work rows that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProposalWorkhourRowOutputModel]**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalWorkhoursGetProposalWorkHoursForProposal

> [ProposalWorkhourRowOutputModel] proposalWorkhoursGetProposalWorkHoursForProposal(proposalGuid, opts)

Get all the proposal work rows.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let proposalGuid = "proposalGuid_example"; // String | proposal id for which to get proposal work rows.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56 // Number | Optional: How many rows to fetch, Default all.
};
apiInstance.proposalWorkhoursGetProposalWorkHoursForProposal(proposalGuid, opts, (error, data, response) => {
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
 **proposalGuid** | **String**| proposal id for which to get proposal work rows. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 

### Return type

[**[ProposalWorkhourRowOutputModel]**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalWorkhoursGetProposalWorkhour

> ProposalWorkhourRowOutputModel proposalWorkhoursGetProposalWorkhour(guid)

Get the proposal work row by guid.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | proposal work row id to get.
apiInstance.proposalWorkhoursGetProposalWorkhour(guid, (error, data, response) => {
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
 **guid** | **String**| proposal work row id to get. | 

### Return type

[**ProposalWorkhourRowOutputModel**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalsGetProposal

> ProposalOutputModel proposalsGetProposal(guid)

Get Proposal by ID

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | GUID used to get the Proposal.
apiInstance.proposalsGetProposal(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the Proposal. | 

### Return type

[**ProposalOutputModel**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalsGetProposals

> [ProposalOutputModel] proposalsGetProposals(opts)

Get all the proposals

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get proposals that have been added or changed after this date time (greater or equal).
};
apiInstance.proposalsGetProposals(opts, (error, data, response) => {
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
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get proposals that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProposalOutputModel]**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## proposalsGetProposalsForProject

> [ProposalOutputModel] proposalsGetProposalsForProject(projectGuid, opts)

Get all the proposals for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Project id for which to get proposals.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get proposals that have been added or changed after this date time (greater or equal).
};
apiInstance.proposalsGetProposalsForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Project id for which to get proposals. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **changedSince** | **Date**| Optional: Get proposals that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProposalOutputModel]**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesGetAllCustomerSalesNotes

> [SalesNoteOutputModel] salesNotesGetAllCustomerSalesNotes(customerGuid, opts)

Get the sales notes by customer guid.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let customerGuid = "customerGuid_example"; // String | Customer guid used to get the notes.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
};
apiInstance.salesNotesGetAllCustomerSalesNotes(customerGuid, opts, (error, data, response) => {
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
 **customerGuid** | **String**| Customer guid used to get the notes. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[SalesNoteOutputModel]**](SalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesGetProjectSalesNote

> ProjectSalesNoteOutputModel salesNotesGetProjectSalesNote(guid)

Get project sales note by ID.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let guid = "guid_example"; // String | GUID used to get the project sales note.
apiInstance.salesNotesGetProjectSalesNote(guid, (error, data, response) => {
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
 **guid** | **String**| GUID used to get the project sales note. | 

### Return type

[**ProjectSalesNoteOutputModel**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesNotesGetProjectSalesNotes

> [ProjectSalesNoteOutputModel] salesNotesGetProjectSalesNotes(projectGuid, opts)

Get the sales notes of a case.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Project guid used to get the notes.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'changedSince': new Date("2013-10-20T19:20:30+01:00") // Date | Optional: Get sales notes that have been added or changed after this date time (greater or equal).
};
apiInstance.salesNotesGetProjectSalesNotes(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Project guid used to get the notes. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **changedSince** | **Date**| Optional: Get sales notes that have been added or changed after this date time (greater or equal). | [optional] 

### Return type

[**[ProjectSalesNoteOutputModel]**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## salesStatusHistoryGetSalesStatusHistory

> [SalesStatusHistoryOutputModel] salesStatusHistoryGetSalesStatusHistory(projectGuid)

Get the sales status history for a project

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | The project for which the sales status history is fetched.
apiInstance.salesStatusHistoryGetSalesStatusHistory(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**| The project for which the sales status history is fetched. | 

### Return type

[**[SalesStatusHistoryOutputModel]**](SalesStatusHistoryOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## teamProductivityGetTeamProductivity

> [TeamProductivityOutputModel] teamProductivityGetTeamProductivity(projectGuid)

Get team productivity of a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | GUID of the project.
apiInstance.teamProductivityGetTeamProductivity(projectGuid, (error, data, response) => {
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
 **projectGuid** | **String**| GUID of the project. | 

### Return type

[**[TeamProductivityOutputModel]**](TeamProductivityOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelExpenseTypesGetSearchedTravelExpenseTypes

> [TravelExpenseTypeOutputModel] travelExpenseTypesGetSearchedTravelExpenseTypes(projectGuid, opts)

Search active travel expense types of project by part of the name or code.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Id of the project.
let opts = {
  'textToSearch': "''", // String | Searched string: part of name or code.
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default all.
  'userGuid': "userGuid_example", // String | Optional: Id of the user to fetch travels for.
  'expenseClass': new SeveraPublicRestApiDocumentation.ExpensesClass() // ExpensesClass | Optional: Expense class of the travel. Mileage/DailyAllowance/OtherTravelExpense.
};
apiInstance.travelExpenseTypesGetSearchedTravelExpenseTypes(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Id of the project. | 
 **textToSearch** | **String**| Searched string: part of name or code. | [optional] [default to &#39;&#39;]
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default all. | [optional] 
 **userGuid** | **String**| Optional: Id of the user to fetch travels for. | [optional] 
 **expenseClass** | [**ExpensesClass**](.md)| Optional: Expense class of the travel. Mileage/DailyAllowance/OtherTravelExpense. | [optional] 

### Return type

[**[TravelExpenseTypeOutputModel]**](TravelExpenseTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## travelPricesGetTravelPricesForProject

> [TravelPriceOutputModel] travelPricesGetTravelPricesForProject(projectGuid, opts)

Get all the travel prices for a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'fromPricelistOnly': false, // Boolean | If true return only prices from the price list, if false also returns prices from the settings. Default is false.
  'expenseClasses': [new SeveraPublicRestApiDocumentation.ExpensesClass()], // [ExpensesClass] | Optional: List of expense classes to search by, defaults to all travel categories.
  'firstRow': 0, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''", // String | Optional: Text to search from Product name.
  'calculateRowCount': false // Boolean | Optional: Calculate the number of total rows. Default false = total row count is returned as zero.
};
apiInstance.travelPricesGetTravelPricesForProject(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| ID of the project. | 
 **fromPricelistOnly** | **Boolean**| If true return only prices from the price list, if false also returns prices from the settings. Default is false. | [optional] [default to false]
 **expenseClasses** | [**[ExpensesClass]**](ExpensesClass.md)| Optional: List of expense classes to search by, defaults to all travel categories. | [optional] 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] [default to 0]
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Optional: Text to search from Product name. | [optional] [default to &#39;&#39;]
 **calculateRowCount** | **Boolean**| Optional: Calculate the number of total rows. Default false &#x3D; total row count is returned as zero. | [optional] [default to false]

### Return type

[**[TravelPriceOutputModel]**](TravelPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workTypesGetPhaseWorkTypes

> [WorkTypeOutputModel] workTypesGetPhaseWorkTypes(phaseGuid, opts)

Get all work types that are available for a phase (for work hour entry)

Only the active work types are included in the list, whether they come from organization settings or project specific work types.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let phaseGuid = "phaseGuid_example"; // String | Id of the phase.
let opts = {
  'pageToken': "pageToken_example", // String | Optional: page token to fetch the next page.
  'rowCount': 56, // Number | Optional: number of rows to fetch
  'userGuid': "userGuid_example" // String | Id of the user for whom the work types are retrieved. Default is current user.
};
apiInstance.workTypesGetPhaseWorkTypes(phaseGuid, opts, (error, data, response) => {
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
 **phaseGuid** | **String**| Id of the phase. | 
 **pageToken** | **String**| Optional: page token to fetch the next page. | [optional] 
 **rowCount** | **Number**| Optional: number of rows to fetch | [optional] 
 **userGuid** | **String**| Id of the user for whom the work types are retrieved. Default is current user. | [optional] 

### Return type

[**[WorkTypeOutputModel]**](WorkTypeOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## workTypesGetSearchedWorktypes

> [WorktypeForProjectOutputModel] workTypesGetSearchedWorktypes(projectGuid, opts)

Search active work types by part of the name or code.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsReadApi();
let projectGuid = "projectGuid_example"; // String | Id of the case to which proposal is connected.
let opts = {
  'firstRow': 56, // Number | Optional: first row to fetch. Default 0 = first row.
  'rowCount': 56, // Number | Optional: How many rows to fetch, Default 20, maximum 100.
  'textToSearch': "''" // String | Searched string: part of name or code.
};
apiInstance.workTypesGetSearchedWorktypes(projectGuid, opts, (error, data, response) => {
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
 **projectGuid** | **String**| Id of the case to which proposal is connected. | 
 **firstRow** | **Number**| Optional: first row to fetch. Default 0 &#x3D; first row. | [optional] 
 **rowCount** | **Number**| Optional: How many rows to fetch, Default 20, maximum 100. | [optional] 
 **textToSearch** | **String**| Searched string: part of name or code. | [optional] [default to &#39;&#39;]

### Return type

[**[WorktypeForProjectOutputModel]**](WorktypeForProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

