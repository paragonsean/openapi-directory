# DiagnosticsApiClient.DiagnosticsApi

All URIs are relative to *https://management.azure.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**diagnosticsExecuteSiteAnalysis**](DiagnosticsApi.md#diagnosticsExecuteSiteAnalysis) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/analyses/{analysisName}/execute | Execute Analysis
[**diagnosticsExecuteSiteAnalysisSlot**](DiagnosticsApi.md#diagnosticsExecuteSiteAnalysisSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/analyses/{analysisName}/execute | Execute Analysis
[**diagnosticsExecuteSiteDetector**](DiagnosticsApi.md#diagnosticsExecuteSiteDetector) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/detectors/{detectorName}/execute | Execute Detector
[**diagnosticsExecuteSiteDetectorSlot**](DiagnosticsApi.md#diagnosticsExecuteSiteDetectorSlot) | **POST** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/detectors/{detectorName}/execute | Execute Detector
[**diagnosticsGetHostingEnvironmentDetectorResponse**](DiagnosticsApi.md#diagnosticsGetHostingEnvironmentDetectorResponse) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/detectors/{detectorName} | Get Hosting Environment Detector Response
[**diagnosticsGetSiteAnalysis**](DiagnosticsApi.md#diagnosticsGetSiteAnalysis) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/analyses/{analysisName} | Get Site Analysis
[**diagnosticsGetSiteAnalysisSlot**](DiagnosticsApi.md#diagnosticsGetSiteAnalysisSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/analyses/{analysisName} | Get Site Analysis
[**diagnosticsGetSiteDetector**](DiagnosticsApi.md#diagnosticsGetSiteDetector) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/detectors/{detectorName} | Get Detector
[**diagnosticsGetSiteDetectorResponse**](DiagnosticsApi.md#diagnosticsGetSiteDetectorResponse) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/detectors/{detectorName} | Get site detector response
[**diagnosticsGetSiteDetectorResponseSlot**](DiagnosticsApi.md#diagnosticsGetSiteDetectorResponseSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/detectors/{detectorName} | Get site detector response
[**diagnosticsGetSiteDetectorSlot**](DiagnosticsApi.md#diagnosticsGetSiteDetectorSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/detectors/{detectorName} | Get Detector
[**diagnosticsGetSiteDiagnosticCategory**](DiagnosticsApi.md#diagnosticsGetSiteDiagnosticCategory) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory} | Get Diagnostics Category
[**diagnosticsGetSiteDiagnosticCategorySlot**](DiagnosticsApi.md#diagnosticsGetSiteDiagnosticCategorySlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory} | Get Diagnostics Category
[**diagnosticsListHostingEnvironmentDetectorResponses**](DiagnosticsApi.md#diagnosticsListHostingEnvironmentDetectorResponses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/hostingEnvironments/{name}/detectors | List Hosting Environment Detector Responses
[**diagnosticsListSiteAnalyses**](DiagnosticsApi.md#diagnosticsListSiteAnalyses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/analyses | Get Site Analyses
[**diagnosticsListSiteAnalysesSlot**](DiagnosticsApi.md#diagnosticsListSiteAnalysesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/analyses | Get Site Analyses
[**diagnosticsListSiteDetectorResponses**](DiagnosticsApi.md#diagnosticsListSiteDetectorResponses) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/detectors | List Site Detector Responses
[**diagnosticsListSiteDetectorResponsesSlot**](DiagnosticsApi.md#diagnosticsListSiteDetectorResponsesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/detectors | List Site Detector Responses
[**diagnosticsListSiteDetectors**](DiagnosticsApi.md#diagnosticsListSiteDetectors) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics/{diagnosticCategory}/detectors | Get Detectors
[**diagnosticsListSiteDetectorsSlot**](DiagnosticsApi.md#diagnosticsListSiteDetectorsSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics/{diagnosticCategory}/detectors | Get Detectors
[**diagnosticsListSiteDiagnosticCategories**](DiagnosticsApi.md#diagnosticsListSiteDiagnosticCategories) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/diagnostics | Get Diagnostics Categories
[**diagnosticsListSiteDiagnosticCategoriesSlot**](DiagnosticsApi.md#diagnosticsListSiteDiagnosticCategoriesSlot) | **GET** /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slot}/diagnostics | Get Diagnostics Categories



## diagnosticsExecuteSiteAnalysis

> DiagnosticAnalysis diagnosticsExecuteSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion, opts)

Execute Analysis

Description for Execute Analysis

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
let analysisName = "analysisName_example"; // String | Analysis Resource Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsExecuteSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Category Name | 
 **analysisName** | **String**| Analysis Resource Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DiagnosticAnalysis**](DiagnosticAnalysis.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsExecuteSiteAnalysisSlot

> DiagnosticAnalysis diagnosticsExecuteSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion, opts)

Execute Analysis

Description for Execute Analysis

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
let analysisName = "analysisName_example"; // String | Analysis Resource Name
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsExecuteSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Category Name | 
 **analysisName** | **String**| Analysis Resource Name | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DiagnosticAnalysis**](DiagnosticAnalysis.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsExecuteSiteDetector

> DiagnosticDetectorResponse diagnosticsExecuteSiteDetector(resourceGroupName, siteName, detectorName, diagnosticCategory, subscriptionId, apiVersion, opts)

Execute Detector

Description for Execute Detector

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let detectorName = "detectorName_example"; // String | Detector Resource Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsExecuteSiteDetector(resourceGroupName, siteName, detectorName, diagnosticCategory, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **detectorName** | **String**| Detector Resource Name | 
 **diagnosticCategory** | **String**| Category Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DiagnosticDetectorResponse**](DiagnosticDetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsExecuteSiteDetectorSlot

> DiagnosticDetectorResponse diagnosticsExecuteSiteDetectorSlot(resourceGroupName, siteName, detectorName, diagnosticCategory, slot, subscriptionId, apiVersion, opts)

Execute Detector

Description for Execute Detector

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let detectorName = "detectorName_example"; // String | Detector Resource Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Category Name
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsExecuteSiteDetectorSlot(resourceGroupName, siteName, detectorName, diagnosticCategory, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **detectorName** | **String**| Detector Resource Name | 
 **diagnosticCategory** | **String**| Category Name | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DiagnosticDetectorResponse**](DiagnosticDetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetHostingEnvironmentDetectorResponse

> DetectorResponse diagnosticsGetHostingEnvironmentDetectorResponse(resourceGroupName, name, detectorName, subscriptionId, apiVersion, opts)

Get Hosting Environment Detector Response

Description for Get Hosting Environment Detector Response

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | App Service Environment Name
let detectorName = "detectorName_example"; // String | Detector Resource Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsGetHostingEnvironmentDetectorResponse(resourceGroupName, name, detectorName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| App Service Environment Name | 
 **detectorName** | **String**| Detector Resource Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DetectorResponse**](DetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteAnalysis

> AnalysisDefinition diagnosticsGetSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion)

Get Site Analysis

Description for Get Site Analysis

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let analysisName = "analysisName_example"; // String | Analysis Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsGetSiteAnalysis(resourceGroupName, siteName, diagnosticCategory, analysisName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **analysisName** | **String**| Analysis Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteAnalysisSlot

> AnalysisDefinition diagnosticsGetSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion)

Get Site Analysis

Description for Get Site Analysis

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let analysisName = "analysisName_example"; // String | Analysis Name
let slot = "slot_example"; // String | Slot - optional
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsGetSiteAnalysisSlot(resourceGroupName, siteName, diagnosticCategory, analysisName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **analysisName** | **String**| Analysis Name | 
 **slot** | **String**| Slot - optional | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**AnalysisDefinition**](AnalysisDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteDetector

> DetectorDefinition diagnosticsGetSiteDetector(resourceGroupName, siteName, diagnosticCategory, detectorName, subscriptionId, apiVersion)

Get Detector

Description for Get Detector

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let detectorName = "detectorName_example"; // String | Detector Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsGetSiteDetector(resourceGroupName, siteName, diagnosticCategory, detectorName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **detectorName** | **String**| Detector Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DetectorDefinition**](DetectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteDetectorResponse

> DetectorResponse diagnosticsGetSiteDetectorResponse(resourceGroupName, siteName, detectorName, subscriptionId, apiVersion, opts)

Get site detector response

Description for Get site detector response

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let detectorName = "detectorName_example"; // String | Detector Resource Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsGetSiteDetectorResponse(resourceGroupName, siteName, detectorName, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **detectorName** | **String**| Detector Resource Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DetectorResponse**](DetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteDetectorResponseSlot

> DetectorResponse diagnosticsGetSiteDetectorResponseSlot(resourceGroupName, siteName, detectorName, slot, subscriptionId, apiVersion, opts)

Get site detector response

Description for Get site detector response

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let detectorName = "detectorName_example"; // String | Detector Resource Name
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
let opts = {
  'startTime': new Date("2013-10-20T19:20:30+01:00"), // Date | Start Time
  'endTime': new Date("2013-10-20T19:20:30+01:00"), // Date | End Time
  'timeGrain': "timeGrain_example" // String | Time Grain
};
apiInstance.diagnosticsGetSiteDetectorResponseSlot(resourceGroupName, siteName, detectorName, slot, subscriptionId, apiVersion, opts, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **detectorName** | **String**| Detector Resource Name | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 
 **startTime** | **Date**| Start Time | [optional] 
 **endTime** | **Date**| End Time | [optional] 
 **timeGrain** | **String**| Time Grain | [optional] 

### Return type

[**DetectorResponse**](DetectorResponse.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteDetectorSlot

> DetectorDefinition diagnosticsGetSiteDetectorSlot(resourceGroupName, siteName, diagnosticCategory, detectorName, slot, subscriptionId, apiVersion)

Get Detector

Description for Get Detector

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let detectorName = "detectorName_example"; // String | Detector Name
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsGetSiteDetectorSlot(resourceGroupName, siteName, diagnosticCategory, detectorName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **detectorName** | **String**| Detector Name | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DetectorDefinition**](DetectorDefinition.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteDiagnosticCategory

> DiagnosticCategory diagnosticsGetSiteDiagnosticCategory(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion)

Get Diagnostics Category

Description for Get Diagnostics Category

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsGetSiteDiagnosticCategory(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticCategory**](DiagnosticCategory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsGetSiteDiagnosticCategorySlot

> DiagnosticCategory diagnosticsGetSiteDiagnosticCategorySlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion)

Get Diagnostics Category

Description for Get Diagnostics Category

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsGetSiteDiagnosticCategorySlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticCategory**](DiagnosticCategory.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListHostingEnvironmentDetectorResponses

> DetectorResponseCollection diagnosticsListHostingEnvironmentDetectorResponses(resourceGroupName, name, subscriptionId, apiVersion)

List Hosting Environment Detector Responses

Description for List Hosting Environment Detector Responses

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let name = "name_example"; // String | Site Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListHostingEnvironmentDetectorResponses(resourceGroupName, name, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **name** | **String**| Site Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DetectorResponseCollection**](DetectorResponseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteAnalyses

> DiagnosticAnalysisCollection diagnosticsListSiteAnalyses(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion)

Get Site Analyses

Description for Get Site Analyses

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteAnalyses(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticAnalysisCollection**](DiagnosticAnalysisCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteAnalysesSlot

> DiagnosticAnalysisCollection diagnosticsListSiteAnalysesSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion)

Get Site Analyses

Description for Get Site Analyses

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteAnalysesSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticAnalysisCollection**](DiagnosticAnalysisCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteDetectorResponses

> DetectorResponseCollection diagnosticsListSiteDetectorResponses(resourceGroupName, siteName, subscriptionId, apiVersion)

List Site Detector Responses

Description for List Site Detector Responses

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteDetectorResponses(resourceGroupName, siteName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DetectorResponseCollection**](DetectorResponseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteDetectorResponsesSlot

> DetectorResponseCollection diagnosticsListSiteDetectorResponsesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion)

List Site Detector Responses

Description for List Site Detector Responses

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteDetectorResponsesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DetectorResponseCollection**](DetectorResponseCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteDetectors

> DiagnosticDetectorCollection diagnosticsListSiteDetectors(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion)

Get Detectors

Description for Get Detectors

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteDetectors(resourceGroupName, siteName, diagnosticCategory, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticDetectorCollection**](DiagnosticDetectorCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteDetectorsSlot

> DiagnosticDetectorCollection diagnosticsListSiteDetectorsSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion)

Get Detectors

Description for Get Detectors

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let diagnosticCategory = "diagnosticCategory_example"; // String | Diagnostic Category
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteDetectorsSlot(resourceGroupName, siteName, diagnosticCategory, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **diagnosticCategory** | **String**| Diagnostic Category | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticDetectorCollection**](DiagnosticDetectorCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteDiagnosticCategories

> DiagnosticCategoryCollection diagnosticsListSiteDiagnosticCategories(resourceGroupName, siteName, subscriptionId, apiVersion)

Get Diagnostics Categories

Description for Get Diagnostics Categories

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteDiagnosticCategories(resourceGroupName, siteName, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticCategoryCollection**](DiagnosticCategoryCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## diagnosticsListSiteDiagnosticCategoriesSlot

> DiagnosticCategoryCollection diagnosticsListSiteDiagnosticCategoriesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion)

Get Diagnostics Categories

Description for Get Diagnostics Categories

### Example

```javascript
import DiagnosticsApiClient from 'diagnostics_api_client';
let defaultClient = DiagnosticsApiClient.ApiClient.instance;
// Configure OAuth2 access token for authorization: azure_auth
let azure_auth = defaultClient.authentications['azure_auth'];
azure_auth.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new DiagnosticsApiClient.DiagnosticsApi();
let resourceGroupName = "resourceGroupName_example"; // String | Name of the resource group to which the resource belongs.
let siteName = "siteName_example"; // String | Site Name
let slot = "slot_example"; // String | Slot Name
let subscriptionId = "subscriptionId_example"; // String | Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
let apiVersion = "apiVersion_example"; // String | API Version
apiInstance.diagnosticsListSiteDiagnosticCategoriesSlot(resourceGroupName, siteName, slot, subscriptionId, apiVersion, (error, data, response) => {
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
 **resourceGroupName** | **String**| Name of the resource group to which the resource belongs. | 
 **siteName** | **String**| Site Name | 
 **slot** | **String**| Slot Name | 
 **subscriptionId** | **String**| Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000). | 
 **apiVersion** | **String**| API Version | 

### Return type

[**DiagnosticCategoryCollection**](DiagnosticCategoryCollection.md)

### Authorization

[azure_auth](../README.md#azure_auth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

