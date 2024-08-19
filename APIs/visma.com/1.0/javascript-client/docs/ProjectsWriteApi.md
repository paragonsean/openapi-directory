# SeveraPublicRestApiDocumentation.ProjectsWriteApi

All URIs are relative to *https://api.severa.visma.com/rest-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**filesPostProjectLink**](ProjectsWriteApi.md#filesPostProjectLink) | **POST** /v1/projectlinks | Add a link to a project.
[**keywordsLinkKeywordToProject**](ProjectsWriteApi.md#keywordsLinkKeywordToProject) | **POST** /v1/projects/{projectGuid}/keywords/{guid} | Link existing keyword to project
[**phaseMembersPostPhaseMember**](ProjectsWriteApi.md#phaseMembersPostPhaseMember) | **POST** /v1/phasemembers | Adds a phase member.
[**phaseMembersPostPhaseMembersFromBusinessUnitUsers**](ProjectsWriteApi.md#phaseMembersPostPhaseMembersFromBusinessUnitUsers) | **POST** /v1/phasemembersfrombusinessunitusers | Adds business unit users to phase members.
[**phasesPatchPhase**](ProjectsWriteApi.md#phasesPatchPhase) | **PATCH** /v1/phases/{guid} | Update (Patch) a phase or a part of it
[**phasesPostPhase**](ProjectsWriteApi.md#phasesPostPhase) | **POST** /v1/phases | Insert a phase
[**priceListsPostCustomPricelist**](ProjectsWriteApi.md#priceListsPostCustomPricelist) | **POST** /v1/projects/{projectGuid}/pricelists/custom | Create custom price list for a project. If project already has a custom price list returns existing price list. Creates a new price list if project doesn&#39;t have a custom price list. Project can only have one custom price list. Note that project&#39;s price list will be changed to the custom price list created here and also existing prices are copied to the new price list.
[**projectCustomValuesPatchProjectCustomValue**](ProjectsWriteApi.md#projectCustomValuesPatchProjectCustomValue) | **PATCH** /v1/projects/customvalues/{guid} | Update (Patch) a project custom value or a part of it.
[**projectCustomValuesPostProjectCustomValue**](ProjectsWriteApi.md#projectCustomValuesPostProjectCustomValue) | **POST** /v1/projects/customvalues | Insert a project custom value.
[**projectForecastsPatchForecast**](ProjectsWriteApi.md#projectForecastsPatchForecast) | **PATCH** /v1/projectforecasts/{guid} | Update (Patch) an project forecast or a part of it
[**projectForecastsPostForecast**](ProjectsWriteApi.md#projectForecastsPostForecast) | **POST** /v1/projectforecasts | Insert a project forecast
[**projectInvoiceSettingsPatchProjectInvoiceSettings_0**](ProjectsWriteApi.md#projectInvoiceSettingsPatchProjectInvoiceSettings_0) | **PATCH** /v1/projectinvoicesettings/{guid} | Update (Patch) project invoice settings.
[**projectInvoiceSettingsPostProjectInvoiceSettings_0**](ProjectsWriteApi.md#projectInvoiceSettingsPostProjectInvoiceSettings_0) | **POST** /v1/projectinvoicesettings | Create a new project invoice settings.
[**projectProductsPostProjectProduct**](ProjectsWriteApi.md#projectProductsPostProjectProduct) | **POST** /v1/projectproducts | Adds a product to a project.
[**projectWorkHourPricesPatchProjectWorkHourPrice**](ProjectsWriteApi.md#projectWorkHourPricesPatchProjectWorkHourPrice) | **PATCH** /v1/projectworkhourprices/{guid} | Update (Patch) a work hour price or a part of it
[**projectWorkHourPricesPostProjectWorkHourPrice**](ProjectsWriteApi.md#projectWorkHourPricesPostProjectWorkHourPrice) | **POST** /v1/projectworkhourprices | Insert a work hour price
[**projectWorkTypesPatchProjectWorktype**](ProjectsWriteApi.md#projectWorkTypesPatchProjectWorktype) | **PATCH** /v1/projectworktypes/{guid} | Update (patch) a project work type.
[**projectWorkTypesPostProjectWorktype**](ProjectsWriteApi.md#projectWorkTypesPostProjectWorktype) | **POST** /v1/projectworktypes | Adds a work type to a project.
[**projectsPatchProject**](ProjectsWriteApi.md#projectsPatchProject) | **PATCH** /v1/projects/{guid} | Update (Patch) a project or a part of it
[**projectsPostProject**](ProjectsWriteApi.md#projectsPostProject) | **POST** /v1/projects | Insert a project
[**proposalFeesPatchProposalFee**](ProjectsWriteApi.md#proposalFeesPatchProposalFee) | **PATCH** /v1/proposalfeerows/{guid} | Update (Patch) a proposal fee row or a part of it
[**proposalFeesPostProposalFee**](ProjectsWriteApi.md#proposalFeesPostProposalFee) | **POST** /v1/proposalfeerows | Insert a proposal fee row.
[**proposalSettingsPatchProposalSettings**](ProjectsWriteApi.md#proposalSettingsPatchProposalSettings) | **PATCH** /v1/proposals/{guid}/proposalsettings | Update (Patch) proposal settings
[**proposalSubtotalsPatchProposalSubtotal**](ProjectsWriteApi.md#proposalSubtotalsPatchProposalSubtotal) | **PATCH** /v1/proposalsubtotals/{guid} | Update (Patch) a Proposal subtotal or a part of it
[**proposalSubtotalsPostProposalSubtotal**](ProjectsWriteApi.md#proposalSubtotalsPostProposalSubtotal) | **POST** /v1/proposalsubtotals | Insert a proposal subtotal
[**proposalWorkhoursPatchProposalWorkhour**](ProjectsWriteApi.md#proposalWorkhoursPatchProposalWorkhour) | **PATCH** /v1/proposalworkrows/{guid} | Update (Patch) a proposal work row or a part of it.
[**proposalWorkhoursPostProposalWorkhour**](ProjectsWriteApi.md#proposalWorkhoursPostProposalWorkhour) | **POST** /v1/proposalworkrows | Insert a proposal work row.
[**proposalsPatchProposal**](ProjectsWriteApi.md#proposalsPatchProposal) | **PATCH** /v1/proposals/{guid} | Update (Patch) a Proposal or a part of it
[**proposalsPostProposal**](ProjectsWriteApi.md#proposalsPostProposal) | **POST** /v1/proposals | Insert a proposal.
[**salesNotesPatchProjectSalesNote**](ProjectsWriteApi.md#salesNotesPatchProjectSalesNote) | **PATCH** /v1/projectsalesnotes/{guid} | Update (Patch) a project sales note or a part of it.
[**salesNotesPostProjectSalesNotes**](ProjectsWriteApi.md#salesNotesPostProjectSalesNotes) | **POST** /v1/projectsalesnotes | Insert a project sales note.



## filesPostProjectLink

> ProjectFileModel filesPostProjectLink(opts)

Add a link to a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectFileModel': new SeveraPublicRestApiDocumentation.ProjectFileModel() // ProjectFileModel | ProjectFileModel.
};
apiInstance.filesPostProjectLink(opts, (error, data, response) => {
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
 **projectFileModel** | [**ProjectFileModel**](ProjectFileModel.md)| ProjectFileModel. | [optional] 

### Return type

[**ProjectFileModel**](ProjectFileModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## keywordsLinkKeywordToProject

> ProjectKeywordModel keywordsLinkKeywordToProject(projectGuid, guid)

Link existing keyword to project

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let projectGuid = "projectGuid_example"; // String | 
let guid = "guid_example"; // String | 
apiInstance.keywordsLinkKeywordToProject(projectGuid, guid, (error, data, response) => {
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
 **guid** | **String**|  | 

### Return type

[**ProjectKeywordModel**](ProjectKeywordModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## phaseMembersPostPhaseMember

> PhaseMemberModel phaseMembersPostPhaseMember(opts)

Adds a phase member.

User is always added as a root phase (project) member also.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'addToAllSubPhases': true, // Boolean | Optional: Add member to all sub phases. Default true.
  'phaseMemberModel': new SeveraPublicRestApiDocumentation.PhaseMemberModel() // PhaseMemberModel | PhaseMemberModel.
};
apiInstance.phaseMembersPostPhaseMember(opts, (error, data, response) => {
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
 **addToAllSubPhases** | **Boolean**| Optional: Add member to all sub phases. Default true. | [optional] [default to true]
 **phaseMemberModel** | [**PhaseMemberModel**](PhaseMemberModel.md)| PhaseMemberModel. | [optional] 

### Return type

[**PhaseMemberModel**](PhaseMemberModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phaseMembersPostPhaseMembersFromBusinessUnitUsers

> [PhaseMemberModel] phaseMembersPostPhaseMembersFromBusinessUnitUsers(opts)

Adds business unit users to phase members.

Users are always added as a root phase (project) member also.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'addToAllSubPhases': true, // Boolean | Optional: Add member to all sub phases. Default true.
  'phaseMembersFromBusinessUnitUsersModel': new SeveraPublicRestApiDocumentation.PhaseMembersFromBusinessUnitUsersModel() // PhaseMembersFromBusinessUnitUsersModel | PhaseMemberModel.
};
apiInstance.phaseMembersPostPhaseMembersFromBusinessUnitUsers(opts, (error, data, response) => {
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
 **addToAllSubPhases** | **Boolean**| Optional: Add member to all sub phases. Default true. | [optional] [default to true]
 **phaseMembersFromBusinessUnitUsersModel** | [**PhaseMembersFromBusinessUnitUsersModel**](PhaseMembersFromBusinessUnitUsersModel.md)| PhaseMemberModel. | [optional] 

### Return type

[**[PhaseMemberModel]**](PhaseMemberModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phasesPatchPhase

> [PhaseOutputModel] phasesPatchPhase(guid, opts)

Update (Patch) a phase or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the phase
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of PhaseInputModel
};
apiInstance.phasesPatchPhase(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the phase | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of PhaseInputModel | [optional] 

### Return type

[**[PhaseOutputModel]**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## phasesPostPhase

> PhaseOutputModel phasesPostPhase(opts)

Insert a phase

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'phaseInputModel': new SeveraPublicRestApiDocumentation.PhaseInputModel() // PhaseInputModel | PhaseOutputModel
};
apiInstance.phasesPostPhase(opts, (error, data, response) => {
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
 **phaseInputModel** | [**PhaseInputModel**](PhaseInputModel.md)| PhaseOutputModel | [optional] 

### Return type

[**PhaseOutputModel**](PhaseOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## priceListsPostCustomPricelist

> CustomPriceListOutputModel priceListsPostCustomPricelist(projectGuid, opts)

Create custom price list for a project. If project already has a custom price list returns existing price list. Creates a new price list if project doesn&#39;t have a custom price list. Project can only have one custom price list. Note that project&#39;s price list will be changed to the custom price list created here and also existing prices are copied to the new price list.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let projectGuid = "projectGuid_example"; // String | ID of the project.
let opts = {
  'isVolumePricing': false // Boolean | Get the custom volume pricing price list or regular custom price list. Default is false.
};
apiInstance.priceListsPostCustomPricelist(projectGuid, opts, (error, data, response) => {
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
 **isVolumePricing** | **Boolean**| Get the custom volume pricing price list or regular custom price list. Default is false. | [optional] [default to false]

### Return type

[**CustomPriceListOutputModel**](CustomPriceListOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## projectCustomValuesPatchProjectCustomValue

> [ProjectCustomValueModel] projectCustomValuesPatchProjectCustomValue(guid, opts)

Update (Patch) a project custom value or a part of it.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the project custom value Can also be comma separate list of IDs to patch multiple project custom values with one call. When multiple IDs are given, returns model which has list of succeeded project custom values and list of errors.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ProjectCustomValueModel.
};
apiInstance.projectCustomValuesPatchProjectCustomValue(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project custom value Can also be comma separate list of IDs to patch multiple project custom values with one call. When multiple IDs are given, returns model which has list of succeeded project custom values and list of errors. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ProjectCustomValueModel. | [optional] 

### Return type

[**[ProjectCustomValueModel]**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectCustomValuesPostProjectCustomValue

> [ProjectCustomValueModel] projectCustomValuesPostProjectCustomValue(opts)

Insert a project custom value.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectCustomValueModel': new SeveraPublicRestApiDocumentation.ProjectCustomValueModel() // ProjectCustomValueModel | ProjectCustomValueModel.
};
apiInstance.projectCustomValuesPostProjectCustomValue(opts, (error, data, response) => {
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
 **projectCustomValueModel** | [**ProjectCustomValueModel**](ProjectCustomValueModel.md)| ProjectCustomValueModel. | [optional] 

### Return type

[**[ProjectCustomValueModel]**](ProjectCustomValueModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectForecastsPatchForecast

> [ProjectForecastOutputModel] projectForecastsPatchForecast(guid, opts)

Update (Patch) an project forecast or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the project forecast
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProjectForecastInputModel
};
apiInstance.projectForecastsPatchForecast(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project forecast | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProjectForecastInputModel | [optional] 

### Return type

[**[ProjectForecastOutputModel]**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectForecastsPostForecast

> ProjectForecastOutputModel projectForecastsPostForecast(opts)

Insert a project forecast

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectForecastInputModel': new SeveraPublicRestApiDocumentation.ProjectForecastInputModel() // ProjectForecastInputModel | ProjectForecastOutputInputModel
};
apiInstance.projectForecastsPostForecast(opts, (error, data, response) => {
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
 **projectForecastInputModel** | [**ProjectForecastInputModel**](ProjectForecastInputModel.md)| ProjectForecastOutputInputModel | [optional] 

### Return type

[**ProjectForecastOutputModel**](ProjectForecastOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectInvoiceSettingsPatchProjectInvoiceSettings_0

> [ProjectInvoiceSettingsOutputModel] projectInvoiceSettingsPatchProjectInvoiceSettings_0(guid, opts)

Update (Patch) project invoice settings.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the project invoice settings.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProjectInvoiceSettingsInputModel.
};
apiInstance.projectInvoiceSettingsPatchProjectInvoiceSettings_0(guid, opts, (error, data, response) => {
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
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProjectInvoiceSettingsInputModel. | [optional] 

### Return type

[**[ProjectInvoiceSettingsOutputModel]**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectInvoiceSettingsPostProjectInvoiceSettings_0

> ProjectInvoiceSettingsOutputModel projectInvoiceSettingsPostProjectInvoiceSettings_0(opts)

Create a new project invoice settings.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectInvoiceSettingsInputModel': new SeveraPublicRestApiDocumentation.ProjectInvoiceSettingsInputModel() // ProjectInvoiceSettingsInputModel | Project invoice settings.
};
apiInstance.projectInvoiceSettingsPostProjectInvoiceSettings_0(opts, (error, data, response) => {
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
 **projectInvoiceSettingsInputModel** | [**ProjectInvoiceSettingsInputModel**](ProjectInvoiceSettingsInputModel.md)| Project invoice settings. | [optional] 

### Return type

[**ProjectInvoiceSettingsOutputModel**](ProjectInvoiceSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectProductsPostProjectProduct

> ProjectProductOutputModel projectProductsPostProjectProduct(opts)

Adds a product to a project.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectProductInputModel': new SeveraPublicRestApiDocumentation.ProjectProductInputModel() // ProjectProductInputModel | projectProductModel
};
apiInstance.projectProductsPostProjectProduct(opts, (error, data, response) => {
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
 **projectProductInputModel** | [**ProjectProductInputModel**](ProjectProductInputModel.md)| projectProductModel | [optional] 

### Return type

[**ProjectProductOutputModel**](ProjectProductOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectWorkHourPricesPatchProjectWorkHourPrice

> [ProjectWorkHourPriceOutputModel] projectWorkHourPricesPatchProjectWorkHourPrice(guid, opts)

Update (Patch) a work hour price or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the work hour price
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProjectWorkHourPriceInputModel
};
apiInstance.projectWorkHourPricesPatchProjectWorkHourPrice(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the work hour price | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProjectWorkHourPriceInputModel | [optional] 

### Return type

[**[ProjectWorkHourPriceOutputModel]**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectWorkHourPricesPostProjectWorkHourPrice

> ProjectWorkHourPriceOutputModel projectWorkHourPricesPostProjectWorkHourPrice(opts)

Insert a work hour price

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectWorkHourPriceInputModel': new SeveraPublicRestApiDocumentation.ProjectWorkHourPriceInputModel() // ProjectWorkHourPriceInputModel | ProjectWorkHourPriceInputModel
};
apiInstance.projectWorkHourPricesPostProjectWorkHourPrice(opts, (error, data, response) => {
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
 **projectWorkHourPriceInputModel** | [**ProjectWorkHourPriceInputModel**](ProjectWorkHourPriceInputModel.md)| ProjectWorkHourPriceInputModel | [optional] 

### Return type

[**ProjectWorkHourPriceOutputModel**](ProjectWorkHourPriceOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectWorkTypesPatchProjectWorktype

> [ProjectWorkTypeModel] projectWorkTypesPatchProjectWorktype(guid, opts)

Update (patch) a project work type.

This currently can be used only to change the default work type in a project. The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the project work type.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProjectWorkTypeModel.
};
apiInstance.projectWorkTypesPatchProjectWorktype(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project work type. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProjectWorkTypeModel. | [optional] 

### Return type

[**[ProjectWorkTypeModel]**](ProjectWorkTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectWorkTypesPostProjectWorktype

> ProjectWorkTypeModel projectWorkTypesPostProjectWorktype(opts)

Adds a work type to a project.

The \&quot;UseWorktypesFromSetting\&quot; flag for the Project should be false (the project should not use the organization list of work types).

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectWorkTypeModel': new SeveraPublicRestApiDocumentation.ProjectWorkTypeModel() // ProjectWorkTypeModel | ProjectWorkTypeModel.
};
apiInstance.projectWorkTypesPostProjectWorktype(opts, (error, data, response) => {
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
 **projectWorkTypeModel** | [**ProjectWorkTypeModel**](ProjectWorkTypeModel.md)| ProjectWorkTypeModel. | [optional] 

### Return type

[**ProjectWorkTypeModel**](ProjectWorkTypeModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsPatchProject

> [ProjectOutputModel] projectsPatchProject(guid, opts)

Update (Patch) a project or a part of it

To update current project status, give ProjectStatusTypeGuid and possibly Description. To update current sales status, give SalesStatusTypeGuid (

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the project
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON Patch document of ProjectInputModel
};
apiInstance.projectsPatchProject(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON Patch document of ProjectInputModel | [optional] 

### Return type

[**[ProjectOutputModel]**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## projectsPostProject

> ProjectOutputModel projectsPostProject(opts)

Insert a project

When creating a new project, the price list property will be ignored, as it is chosen by default.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectInputModelBase': new SeveraPublicRestApiDocumentation.ProjectInputModelBase() // ProjectInputModelBase | ProjectInputModelBase
};
apiInstance.projectsPostProject(opts, (error, data, response) => {
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
 **projectInputModelBase** | [**ProjectInputModelBase**](ProjectInputModelBase.md)| ProjectInputModelBase | [optional] 

### Return type

[**ProjectOutputModel**](ProjectOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalFeesPatchProposalFee

> [ProposalFeeRowOutputModel] proposalFeesPatchProposalFee(guid, opts)

Update (Patch) a proposal fee row or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the proposal fee row
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProposalFeeModel
};
apiInstance.proposalFeesPatchProposalFee(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the proposal fee row | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProposalFeeModel | [optional] 

### Return type

[**[ProposalFeeRowOutputModel]**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalFeesPostProposalFee

> ProposalFeeRowOutputModel proposalFeesPostProposalFee(opts)

Insert a proposal fee row.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'proposalFeeRowInputModel': new SeveraPublicRestApiDocumentation.ProposalFeeRowInputModel() // ProposalFeeRowInputModel | ProposalFeeModel
};
apiInstance.proposalFeesPostProposalFee(opts, (error, data, response) => {
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
 **proposalFeeRowInputModel** | [**ProposalFeeRowInputModel**](ProposalFeeRowInputModel.md)| ProposalFeeModel | [optional] 

### Return type

[**ProposalFeeRowOutputModel**](ProposalFeeRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalSettingsPatchProposalSettings

> [ProposalSettingsOutputModel] proposalSettingsPatchProposalSettings(guid, opts)

Update (Patch) proposal settings

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | Guid of the Proposal
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProposalSettingsInputModel
};
apiInstance.proposalSettingsPatchProposalSettings(guid, opts, (error, data, response) => {
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
 **guid** | **String**| Guid of the Proposal | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProposalSettingsInputModel | [optional] 

### Return type

[**[ProposalSettingsOutputModel]**](ProposalSettingsOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalSubtotalsPatchProposalSubtotal

> [ProposalSubtotalOutputModel] proposalSubtotalsPatchProposalSubtotal(guid, opts)

Update (Patch) a Proposal subtotal or a part of it

It is not possible to changed the proposalGuid for an existing proposal subtotal. Also, when a proposal subtotal is connected to a phase, the connection can only be broken if the phase is deleted.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the Proposal subtotal
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProposalSubtotalModel
};
apiInstance.proposalSubtotalsPatchProposalSubtotal(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the Proposal subtotal | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProposalSubtotalModel | [optional] 

### Return type

[**[ProposalSubtotalOutputModel]**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalSubtotalsPostProposalSubtotal

> ProposalSubtotalOutputModel proposalSubtotalsPostProposalSubtotal(opts)

Insert a proposal subtotal

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'proposalSubtotalInputModel': new SeveraPublicRestApiDocumentation.ProposalSubtotalInputModel() // ProposalSubtotalInputModel | ProposalSubtotalModel
};
apiInstance.proposalSubtotalsPostProposalSubtotal(opts, (error, data, response) => {
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
 **proposalSubtotalInputModel** | [**ProposalSubtotalInputModel**](ProposalSubtotalInputModel.md)| ProposalSubtotalModel | [optional] 

### Return type

[**ProposalSubtotalOutputModel**](ProposalSubtotalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalWorkhoursPatchProposalWorkhour

> [ProposalWorkhourRowOutputModel] proposalWorkhoursPatchProposalWorkhour(guid, opts)

Update (Patch) a proposal work row or a part of it.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the proposal work row.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProposalWorkhourModel.
};
apiInstance.proposalWorkhoursPatchProposalWorkhour(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the proposal work row. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProposalWorkhourModel. | [optional] 

### Return type

[**[ProposalWorkhourRowOutputModel]**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalWorkhoursPostProposalWorkhour

> ProposalWorkhourRowOutputModel proposalWorkhoursPostProposalWorkhour(opts)

Insert a proposal work row.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'proposalWorkhourRowInputModel': new SeveraPublicRestApiDocumentation.ProposalWorkhourRowInputModel() // ProposalWorkhourRowInputModel | ProposalWorkhourModel
};
apiInstance.proposalWorkhoursPostProposalWorkhour(opts, (error, data, response) => {
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
 **proposalWorkhourRowInputModel** | [**ProposalWorkhourRowInputModel**](ProposalWorkhourRowInputModel.md)| ProposalWorkhourModel | [optional] 

### Return type

[**ProposalWorkhourRowOutputModel**](ProposalWorkhourRowOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalsPatchProposal

> [ProposalOutputModel] proposalsPatchProposal(guid, opts)

Update (Patch) a Proposal or a part of it

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | Guid of the Proposal
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of ProposalInputModel
};
apiInstance.proposalsPatchProposal(guid, opts, (error, data, response) => {
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
 **guid** | **String**| Guid of the Proposal | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of ProposalInputModel | [optional] 

### Return type

[**[ProposalOutputModel]**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## proposalsPostProposal

> ProposalOutputModel proposalsPostProposal(opts)

Insert a proposal.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'proposalInputModel': new SeveraPublicRestApiDocumentation.ProposalInputModel() // ProposalInputModel | ProposalInputModel
};
apiInstance.proposalsPostProposal(opts, (error, data, response) => {
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
 **proposalInputModel** | [**ProposalInputModel**](ProposalInputModel.md)| ProposalInputModel | [optional] 

### Return type

[**ProposalOutputModel**](ProposalOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesNotesPatchProjectSalesNote

> [ProjectSalesNoteOutputModel] salesNotesPatchProjectSalesNote(guid, opts)

Update (Patch) a project sales note or a part of it.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let guid = "guid_example"; // String | ID of the project sales note.
let opts = {
  'patchOperation': [new SeveraPublicRestApiDocumentation.PatchOperation()] // [PatchOperation] | JSON patch document of project sales note model.
};
apiInstance.salesNotesPatchProjectSalesNote(guid, opts, (error, data, response) => {
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
 **guid** | **String**| ID of the project sales note. | 
 **patchOperation** | [**[PatchOperation]**](PatchOperation.md)| JSON patch document of project sales note model. | [optional] 

### Return type

[**[ProjectSalesNoteOutputModel]**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## salesNotesPostProjectSalesNotes

> ProjectSalesNoteOutputModel salesNotesPostProjectSalesNotes(opts)

Insert a project sales note.

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

let apiInstance = new SeveraPublicRestApiDocumentation.ProjectsWriteApi();
let opts = {
  'projectSalesNoteInputModel': new SeveraPublicRestApiDocumentation.ProjectSalesNoteInputModel() // ProjectSalesNoteInputModel | SalesNoteOutputModel
};
apiInstance.salesNotesPostProjectSalesNotes(opts, (error, data, response) => {
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
 **projectSalesNoteInputModel** | [**ProjectSalesNoteInputModel**](ProjectSalesNoteInputModel.md)| SalesNoteOutputModel | [optional] 

### Return type

[**ProjectSalesNoteOutputModel**](ProjectSalesNoteOutputModel.md)

### Authorization

[ClientIdAuth](../README.md#ClientIdAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

