# PatchmanEngineApi.DefaultApi

All URIs are relative to *http://redhat.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletesystem**](DefaultApi.md#deletesystem) | **DELETE** /api/patch/v1/systems/{inventory_id} | Delete system by inventory id
[**detailAdvisory**](DefaultApi.md#detailAdvisory) | **GET** /api/patch/v1/advisories/{advisory_id} | Show me details an advisory by given advisory name
[**detailSystem**](DefaultApi.md#detailSystem) | **GET** /api/patch/v1/systems/{inventory_id} | Show me details about a system by given inventory id
[**exportAdvisories**](DefaultApi.md#exportAdvisories) | **GET** /api/patch/v1/export/advisories | Export applicable advisories for all my systems
[**exportAdvisorySystems**](DefaultApi.md#exportAdvisorySystems) | **GET** /api/patch/v1/export/advisories/{advisory_id}/systems | Export systems for my account
[**exportPackageSystems**](DefaultApi.md#exportPackageSystems) | **GET** /api/patch/v1/export/packages/{package_name}/systems | Show me all my systems which have a package installed
[**exportPackages**](DefaultApi.md#exportPackages) | **GET** /api/patch/v1/export/packages | Show me all installed packages across my systems
[**exportSystemAdvisories**](DefaultApi.md#exportSystemAdvisories) | **GET** /api/patch/v1/export/systems/{inventory_id}/advisories | Export applicable advisories for all my systems
[**exportSystemPackages**](DefaultApi.md#exportSystemPackages) | **GET** /api/patch/v1/export/systems/{inventory_id}/packages | Show me details about a system packages by given inventory id
[**exportSystems**](DefaultApi.md#exportSystems) | **GET** /api/patch/v1/export/systems | Export systems for my account
[**latestPackage**](DefaultApi.md#latestPackage) | **GET** /api/patch/v1/packages/{package_name} | Show me metadata of selected package
[**listAdvisories**](DefaultApi.md#listAdvisories) | **GET** /api/patch/v1/advisories | Show me all applicable advisories for all my systems
[**listAdvisorySystems**](DefaultApi.md#listAdvisorySystems) | **GET** /api/patch/v1/advisories/{advisory_id}/systems | Show me systems on which the given advisory is applicable
[**listPackages**](DefaultApi.md#listPackages) | **GET** /api/patch/v1/packages/ | Show me all installed packages across my systems
[**listSystemAdvisories**](DefaultApi.md#listSystemAdvisories) | **GET** /api/patch/v1/systems/{inventory_id}/advisories | Show me advisories for a system by given inventory id
[**listSystems**](DefaultApi.md#listSystems) | **GET** /api/patch/v1/systems | Show me all my systems
[**packageSystems**](DefaultApi.md#packageSystems) | **GET** /api/patch/v1/packages/{package_name}/systems | Show me all my systems which have a package installed
[**packageVersions**](DefaultApi.md#packageVersions) | **GET** /api/patch/v1/packages/{package_name}/versions | Show me all package versions installed on some system
[**systemPackages**](DefaultApi.md#systemPackages) | **GET** /api/patch/v1/systems/{inventory_id}/packages | Show me details about a system packages by given inventory id
[**viewAdvisoriesSystems**](DefaultApi.md#viewAdvisoriesSystems) | **POST** /api/patch/v1/views/advisories/systems | View advisory-system pairs for selected systems and advisories
[**viewSystemsAdvisories**](DefaultApi.md#viewSystemsAdvisories) | **POST** /api/patch/v1/views/systems/advisories | View system-advisory pairs for selected systems and advisories



## deletesystem

> deletesystem(inventoryId)

Delete system by inventory id

Delete system by inventory id

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let inventoryId = "inventoryId_example"; // String | Inventory ID
apiInstance.deletesystem(inventoryId, (error, data, response) => {
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
 **inventoryId** | **String**| Inventory ID | 

### Return type

null (empty response body)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## detailAdvisory

> ControllersAdvisoryDetailResponse detailAdvisory(advisoryId)

Show me details an advisory by given advisory name

Show me details an advisory by given advisory name

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let advisoryId = "advisoryId_example"; // String | Advisory ID
apiInstance.detailAdvisory(advisoryId, (error, data, response) => {
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
 **advisoryId** | **String**| Advisory ID | 

### Return type

[**ControllersAdvisoryDetailResponse**](ControllersAdvisoryDetailResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## detailSystem

> ControllersSystemDetailResponse detailSystem(inventoryId)

Show me details about a system by given inventory id

Show me details about a system by given inventory id

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let inventoryId = "inventoryId_example"; // String | Inventory ID
apiInstance.detailSystem(inventoryId, (error, data, response) => {
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
 **inventoryId** | **String**| Inventory ID | 

### Return type

[**ControllersSystemDetailResponse**](ControllersSystemDetailResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportAdvisories

> [ControllersAdvisoryInlineItem] exportAdvisories(opts)

Export applicable advisories for all my systems

Export applicable advisories for all my systems

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let opts = {
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter
  'filterDescription': "filterDescription_example", // String | Filter
  'filterPublicDate': "filterPublicDate_example", // String | Filter
  'filterSynopsis': "filterSynopsis_example", // String | Filter
  'filterAdvisoryType': "filterAdvisoryType_example", // String | Filter
  'filterSeverity': "filterSeverity_example", // String | Filter
  'filterApplicableSystems': "filterApplicableSystems_example" // String | Filter
};
apiInstance.exportAdvisories(opts, (error, data, response) => {
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
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterDescription** | **String**| Filter | [optional] 
 **filterPublicDate** | **String**| Filter | [optional] 
 **filterSynopsis** | **String**| Filter | [optional] 
 **filterAdvisoryType** | **String**| Filter | [optional] 
 **filterSeverity** | **String**| Filter | [optional] 
 **filterApplicableSystems** | **String**| Filter | [optional] 

### Return type

[**[ControllersAdvisoryInlineItem]**](ControllersAdvisoryInlineItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## exportAdvisorySystems

> [ControllersSystemInlineItem] exportAdvisorySystems(advisoryId, opts)

Export systems for my account

Export systems for my account

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let advisoryId = "advisoryId_example"; // String | Advisory ID
let opts = {
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter
  'filterDisplayName': "filterDisplayName_example", // String | Filter
  'filterLastEvaluation': "filterLastEvaluation_example", // String | Filter
  'filterLastUpload': "filterLastUpload_example", // String | Filter
  'filterRhsaCount': "filterRhsaCount_example", // String | Filter
  'filterRhbaCount': "filterRhbaCount_example", // String | Filter
  'filterRheaCount': "filterRheaCount_example", // String | Filter
  'filterOtherCount': "filterOtherCount_example", // String | Filter
  'filterStale': "filterStale_example", // String | Filter
  'filterPackagesInstalled': "filterPackagesInstalled_example", // String | Filter
  'filterPackagesUpdatable': "filterPackagesUpdatable_example", // String | Filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"], // [String] | Filter systems by their SAP SIDs
  'tags': ["null"] // [String] | Tag filter
};
apiInstance.exportAdvisorySystems(advisoryId, opts, (error, data, response) => {
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
 **advisoryId** | **String**| Advisory ID | 
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterDisplayName** | **String**| Filter | [optional] 
 **filterLastEvaluation** | **String**| Filter | [optional] 
 **filterLastUpload** | **String**| Filter | [optional] 
 **filterRhsaCount** | **String**| Filter | [optional] 
 **filterRhbaCount** | **String**| Filter | [optional] 
 **filterRheaCount** | **String**| Filter | [optional] 
 **filterOtherCount** | **String**| Filter | [optional] 
 **filterStale** | **String**| Filter | [optional] 
 **filterPackagesInstalled** | **String**| Filter | [optional] 
 **filterPackagesUpdatable** | **String**| Filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 

### Return type

[**[ControllersSystemInlineItem]**](ControllersSystemInlineItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## exportPackageSystems

> [ControllersPackageSystemItem] exportPackageSystems(packageName, opts)

Show me all my systems which have a package installed

Show me all my systems which have a package installed

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let packageName = "packageName_example"; // String | Package name
let opts = {
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"], // [String] | Filter systems by their SAP SIDs
  'tags': ["null"] // [String] | Tag filter
};
apiInstance.exportPackageSystems(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| Package name | 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 

### Return type

[**[ControllersPackageSystemItem]**](ControllersPackageSystemItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportPackages

> [ControllersPackageItem] exportPackages(opts)

Show me all installed packages across my systems

Show me all installed packages across my systems

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let opts = {
  'sort': "sort_example", // String | Sort field
  'search': "search_example", // String | Find matching text
  'filterName': "filterName_example", // String | Filter
  'filterSystemsInstalled': "filterSystemsInstalled_example", // String | Filter
  'filterSystemsUpdatable': "filterSystemsUpdatable_example", // String | Filter
  'filterSummary': "filterSummary_example" // String | Filter
};
apiInstance.exportPackages(opts, (error, data, response) => {
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
 **sort** | **String**| Sort field | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterName** | **String**| Filter | [optional] 
 **filterSystemsInstalled** | **String**| Filter | [optional] 
 **filterSystemsUpdatable** | **String**| Filter | [optional] 
 **filterSummary** | **String**| Filter | [optional] 

### Return type

[**[ControllersPackageItem]**](ControllersPackageItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## exportSystemAdvisories

> [ControllersSystemAdvisoriesDBLookup] exportSystemAdvisories(inventoryId, opts)

Export applicable advisories for all my systems

Export applicable advisories for all my systems

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let inventoryId = "inventoryId_example"; // String | Inventory ID
let opts = {
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter
  'filterDescription': "filterDescription_example", // String | Filter
  'filterPublicDate': "filterPublicDate_example", // String | Filter
  'filterSynopsis': "filterSynopsis_example", // String | Filter
  'filterAdvisoryType': "filterAdvisoryType_example", // String | Filter
  'filterSeverity': "filterSeverity_example" // String | Filter
};
apiInstance.exportSystemAdvisories(inventoryId, opts, (error, data, response) => {
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
 **inventoryId** | **String**| Inventory ID | 
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterDescription** | **String**| Filter | [optional] 
 **filterPublicDate** | **String**| Filter | [optional] 
 **filterSynopsis** | **String**| Filter | [optional] 
 **filterAdvisoryType** | **String**| Filter | [optional] 
 **filterSeverity** | **String**| Filter | [optional] 

### Return type

[**[ControllersSystemAdvisoriesDBLookup]**](ControllersSystemAdvisoriesDBLookup.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## exportSystemPackages

> [ControllersSystemPackageInline] exportSystemPackages(inventoryId, opts)

Show me details about a system packages by given inventory id

Show me details about a system packages by given inventory id

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let inventoryId = "inventoryId_example"; // String | Inventory ID
let opts = {
  'search': "search_example", // String | Find matching text
  'filterName': "filterName_example", // String | Filter
  'filterDescription': "filterDescription_example", // String | Filter
  'filterEvra': "filterEvra_example", // String | Filter
  'filterSummary': "filterSummary_example", // String | Filter
  'filterUpdatable': true // Boolean | Filter
};
apiInstance.exportSystemPackages(inventoryId, opts, (error, data, response) => {
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
 **inventoryId** | **String**| Inventory ID | 
 **search** | **String**| Find matching text | [optional] 
 **filterName** | **String**| Filter | [optional] 
 **filterDescription** | **String**| Filter | [optional] 
 **filterEvra** | **String**| Filter | [optional] 
 **filterSummary** | **String**| Filter | [optional] 
 **filterUpdatable** | **Boolean**| Filter | [optional] 

### Return type

[**[ControllersSystemPackageInline]**](ControllersSystemPackageInline.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## exportSystems

> [ControllersSystemInlineItem] exportSystems(opts)

Export systems for my account

Export systems for my account

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let opts = {
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter
  'filterDisplayName': "filterDisplayName_example", // String | Filter
  'filterLastEvaluation': "filterLastEvaluation_example", // String | Filter
  'filterLastUpload': "filterLastUpload_example", // String | Filter
  'filterRhsaCount': "filterRhsaCount_example", // String | Filter
  'filterRhbaCount': "filterRhbaCount_example", // String | Filter
  'filterRheaCount': "filterRheaCount_example", // String | Filter
  'filterOtherCount': "filterOtherCount_example", // String | Filter
  'filterStale': "filterStale_example", // String | Filter
  'filterPackagesInstalled': "filterPackagesInstalled_example", // String | Filter
  'filterPackagesUpdatable': "filterPackagesUpdatable_example", // String | Filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"], // [String] | Filter systems by their SAP SIDs
  'tags': ["null"] // [String] | Tag filter
};
apiInstance.exportSystems(opts, (error, data, response) => {
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
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterDisplayName** | **String**| Filter | [optional] 
 **filterLastEvaluation** | **String**| Filter | [optional] 
 **filterLastUpload** | **String**| Filter | [optional] 
 **filterRhsaCount** | **String**| Filter | [optional] 
 **filterRhbaCount** | **String**| Filter | [optional] 
 **filterRheaCount** | **String**| Filter | [optional] 
 **filterOtherCount** | **String**| Filter | [optional] 
 **filterStale** | **String**| Filter | [optional] 
 **filterPackagesInstalled** | **String**| Filter | [optional] 
 **filterPackagesUpdatable** | **String**| Filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 

### Return type

[**[ControllersSystemInlineItem]**](ControllersSystemInlineItem.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json, text/csv


## latestPackage

> ControllersPackageDetailResponse latestPackage(packageName)

Show me metadata of selected package

Show me metadata of selected package

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let packageName = "packageName_example"; // String | package_name - latest, nevra - exact version
apiInstance.latestPackage(packageName, (error, data, response) => {
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
 **packageName** | **String**| package_name - latest, nevra - exact version | 

### Return type

[**ControllersPackageDetailResponse**](ControllersPackageDetailResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAdvisories

> ControllersAdvisoriesResponse listAdvisories(opts)

Show me all applicable advisories for all my systems

Show me all applicable advisories for all my systems

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'sort': "sort_example", // String | Sort field
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter 
  'filterDescription': "filterDescription_example", // String | Filter
  'filterPublicDate': "filterPublicDate_example", // String | Filter
  'filterSynopsis': "filterSynopsis_example", // String | Filter
  'filterAdvisoryType': "filterAdvisoryType_example", // String | Filter
  'filterSeverity': "filterSeverity_example", // String | Filter
  'filterApplicableSystems': "filterApplicableSystems_example", // String | Filter
  'tags': ["null"], // [String] | Tag filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"] // [String] | Filter systems by their SAP SIDs
};
apiInstance.listAdvisories(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **sort** | **String**| Sort field | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter  | [optional] 
 **filterDescription** | **String**| Filter | [optional] 
 **filterPublicDate** | **String**| Filter | [optional] 
 **filterSynopsis** | **String**| Filter | [optional] 
 **filterAdvisoryType** | **String**| Filter | [optional] 
 **filterSeverity** | **String**| Filter | [optional] 
 **filterApplicableSystems** | **String**| Filter | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 

### Return type

[**ControllersAdvisoriesResponse**](ControllersAdvisoriesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listAdvisorySystems

> ControllersAdvisorySystemsResponse listAdvisorySystems(advisoryId, opts)

Show me systems on which the given advisory is applicable

Show me systems on which the given advisory is applicable

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let advisoryId = "advisoryId_example"; // String | Advisory ID
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'sort': "sort_example", // String | Sort field
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter
  'filterInsightsId': "filterInsightsId_example", // String | Filter
  'filterDisplayName': "filterDisplayName_example", // String | Filter
  'filterLastEvaluation': "filterLastEvaluation_example", // String | Filter
  'filterLastUpload': "filterLastUpload_example", // String | Filter
  'filterRhsaCount': "filterRhsaCount_example", // String | Filter
  'filterRhbaCount': "filterRhbaCount_example", // String | Filter
  'filterRheaCount': "filterRheaCount_example", // String | Filter
  'filterOtherCount': "filterOtherCount_example", // String | Filter
  'filterStale': "filterStale_example", // String | Filter
  'filterStaleTimestamp': "filterStaleTimestamp_example", // String | Filter
  'filterStaleWarningTimestamp': "filterStaleWarningTimestamp_example", // String | Filter
  'filterCulledTimestamp': "filterCulledTimestamp_example", // String | Filter
  'filterCreated': "filterCreated_example", // String | Filter
  'tags': ["null"], // [String] | Tag filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"] // [String] | Filter systems by their SAP SIDs
};
apiInstance.listAdvisorySystems(advisoryId, opts, (error, data, response) => {
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
 **advisoryId** | **String**| Advisory ID | 
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **sort** | **String**| Sort field | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterInsightsId** | **String**| Filter | [optional] 
 **filterDisplayName** | **String**| Filter | [optional] 
 **filterLastEvaluation** | **String**| Filter | [optional] 
 **filterLastUpload** | **String**| Filter | [optional] 
 **filterRhsaCount** | **String**| Filter | [optional] 
 **filterRhbaCount** | **String**| Filter | [optional] 
 **filterRheaCount** | **String**| Filter | [optional] 
 **filterOtherCount** | **String**| Filter | [optional] 
 **filterStale** | **String**| Filter | [optional] 
 **filterStaleTimestamp** | **String**| Filter | [optional] 
 **filterStaleWarningTimestamp** | **String**| Filter | [optional] 
 **filterCulledTimestamp** | **String**| Filter | [optional] 
 **filterCreated** | **String**| Filter | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 

### Return type

[**ControllersAdvisorySystemsResponse**](ControllersAdvisorySystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listPackages

> ControllersPackagesResponse listPackages(opts)

Show me all installed packages across my systems

Show me all installed packages across my systems

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'sort': "sort_example", // String | Sort field
  'search': "search_example", // String | Find matching text
  'filterName': "filterName_example", // String | Filter
  'filterSystemsInstalled': "filterSystemsInstalled_example", // String | Filter
  'filterSystemsUpdatable': "filterSystemsUpdatable_example", // String | Filter
  'filterSummary': "filterSummary_example", // String | Filter
  'tags': ["null"], // [String] | Tag filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"] // [String] | Filter systems by their SAP SIDs
};
apiInstance.listPackages(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **sort** | **String**| Sort field | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterName** | **String**| Filter | [optional] 
 **filterSystemsInstalled** | **String**| Filter | [optional] 
 **filterSystemsUpdatable** | **String**| Filter | [optional] 
 **filterSummary** | **String**| Filter | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 

### Return type

[**ControllersPackagesResponse**](ControllersPackagesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSystemAdvisories

> ControllersSystemAdvisoriesResponse listSystemAdvisories(inventoryId, opts)

Show me advisories for a system by given inventory id

Show me advisories for a system by given inventory id

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let inventoryId = "inventoryId_example"; // String | Inventory ID
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'sort': "sort_example", // String | Sort field
  'search': "search_example", // String | Find matching text
  'filterId': "filterId_example", // String | Filter
  'filterDescription': "filterDescription_example", // String | Filter
  'filterPublicDate': "filterPublicDate_example", // String | Filter
  'filterSynopsis': "filterSynopsis_example", // String | Filter
  'filterAdvisoryType': "filterAdvisoryType_example", // String | Filter
  'filterSeverity': "filterSeverity_example" // String | Filter
};
apiInstance.listSystemAdvisories(inventoryId, opts, (error, data, response) => {
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
 **inventoryId** | **String**| Inventory ID | 
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **sort** | **String**| Sort field | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterDescription** | **String**| Filter | [optional] 
 **filterPublicDate** | **String**| Filter | [optional] 
 **filterSynopsis** | **String**| Filter | [optional] 
 **filterAdvisoryType** | **String**| Filter | [optional] 
 **filterSeverity** | **String**| Filter | [optional] 

### Return type

[**ControllersSystemAdvisoriesResponse**](ControllersSystemAdvisoriesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## listSystems

> ControllersSystemsResponse listSystems(opts)

Show me all my systems

Show me all my systems

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'sort': "sort_example", // String | Sort field
  'search': "search_example", // String | Find matching text
  'filterInsightsId': "filterInsightsId_example", // String | Filter
  'filterId': "filterId_example", // String | Filter
  'filterDisplayName': "filterDisplayName_example", // String | Filter
  'filterLastEvaluation': "filterLastEvaluation_example", // String | Filter
  'filterLastUpload': "filterLastUpload_example", // String | Filter
  'filterRhsaCount': "filterRhsaCount_example", // String | Filter
  'filterRhbaCount': "filterRhbaCount_example", // String | Filter
  'filterRheaCount': "filterRheaCount_example", // String | Filter
  'filterOtherCount': "filterOtherCount_example", // String | Filter
  'filterStale': "filterStale_example", // String | Filter
  'filterPackagesInstalled': "filterPackagesInstalled_example", // String | Filter
  'filterPackagesUpdatable': "filterPackagesUpdatable_example", // String | Filter
  'filterStaleTimestamp': "filterStaleTimestamp_example", // String | Filter
  'filterStaleWarningTimestamp': "filterStaleWarningTimestamp_example", // String | Filter
  'filterCulledTimestamp': "filterCulledTimestamp_example", // String | Filter
  'filterCreated': "filterCreated_example", // String | Filter
  'tags': ["null"], // [String] | Tag filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"] // [String] | Filter systems by their SAP SIDs
};
apiInstance.listSystems(opts, (error, data, response) => {
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
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **sort** | **String**| Sort field | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterInsightsId** | **String**| Filter | [optional] 
 **filterId** | **String**| Filter | [optional] 
 **filterDisplayName** | **String**| Filter | [optional] 
 **filterLastEvaluation** | **String**| Filter | [optional] 
 **filterLastUpload** | **String**| Filter | [optional] 
 **filterRhsaCount** | **String**| Filter | [optional] 
 **filterRhbaCount** | **String**| Filter | [optional] 
 **filterRheaCount** | **String**| Filter | [optional] 
 **filterOtherCount** | **String**| Filter | [optional] 
 **filterStale** | **String**| Filter | [optional] 
 **filterPackagesInstalled** | **String**| Filter | [optional] 
 **filterPackagesUpdatable** | **String**| Filter | [optional] 
 **filterStaleTimestamp** | **String**| Filter | [optional] 
 **filterStaleWarningTimestamp** | **String**| Filter | [optional] 
 **filterCulledTimestamp** | **String**| Filter | [optional] 
 **filterCreated** | **String**| Filter | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 

### Return type

[**ControllersSystemsResponse**](ControllersSystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageSystems

> ControllersPackageSystemsResponse packageSystems(packageName, opts)

Show me all my systems which have a package installed

Show me all my systems which have a package installed

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let packageName = "packageName_example"; // String | Package name
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'tags': ["null"], // [String] | Tag filter
  'filterSystemProfileSapSystem': "filterSystemProfileSapSystem_example", // String | Filter only SAP systems
  'filterSystemProfileSapSidsIn': ["null"] // [String] | Filter systems by their SAP SIDs
};
apiInstance.packageSystems(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| Package name | 
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **tags** | [**[String]**](String.md)| Tag filter | [optional] 
 **filterSystemProfileSapSystem** | **String**| Filter only SAP systems | [optional] 
 **filterSystemProfileSapSidsIn** | [**[String]**](String.md)| Filter systems by their SAP SIDs | [optional] 

### Return type

[**ControllersPackageSystemsResponse**](ControllersPackageSystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## packageVersions

> ControllersPackageVersionsResponse packageVersions(packageName, opts)

Show me all package versions installed on some system

Show me all package versions installed on some system

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let packageName = "packageName_example"; // String | Package name
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56 // Number | Offset for paging
};
apiInstance.packageVersions(packageName, opts, (error, data, response) => {
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
 **packageName** | **String**| Package name | 
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 

### Return type

[**ControllersPackageVersionsResponse**](ControllersPackageVersionsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## systemPackages

> ControllersSystemPackageResponse systemPackages(inventoryId, opts)

Show me details about a system packages by given inventory id

Show me details about a system packages by given inventory id

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let inventoryId = "inventoryId_example"; // String | Inventory ID
let opts = {
  'limit': 56, // Number | Limit for paging, set -1 to return all
  'offset': 56, // Number | Offset for paging
  'search': "search_example", // String | Find matching text
  'filterName': "filterName_example", // String | Filter
  'filterDescription': "filterDescription_example", // String | Filter
  'filterEvra': "filterEvra_example", // String | Filter
  'filterSummary': "filterSummary_example", // String | Filter
  'filterUpdatable': true // Boolean | Filter
};
apiInstance.systemPackages(inventoryId, opts, (error, data, response) => {
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
 **inventoryId** | **String**| Inventory ID | 
 **limit** | **Number**| Limit for paging, set -1 to return all | [optional] 
 **offset** | **Number**| Offset for paging | [optional] 
 **search** | **String**| Find matching text | [optional] 
 **filterName** | **String**| Filter | [optional] 
 **filterDescription** | **String**| Filter | [optional] 
 **filterEvra** | **String**| Filter | [optional] 
 **filterSummary** | **String**| Filter | [optional] 
 **filterUpdatable** | **Boolean**| Filter | [optional] 

### Return type

[**ControllersSystemPackageResponse**](ControllersSystemPackageResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## viewAdvisoriesSystems

> ControllersAdvisoriesSystemsResponse viewAdvisoriesSystems(body)

View advisory-system pairs for selected systems and advisories

View advisory-system pairs for selected systems and advisories

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let body = new PatchmanEngineApi.ControllersSystemsAdvisoriesRequest(); // ControllersSystemsAdvisoriesRequest | Request body
apiInstance.viewAdvisoriesSystems(body, (error, data, response) => {
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
 **body** | [**ControllersSystemsAdvisoriesRequest**](ControllersSystemsAdvisoriesRequest.md)| Request body | 

### Return type

[**ControllersAdvisoriesSystemsResponse**](ControllersAdvisoriesSystemsResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## viewSystemsAdvisories

> ControllersSystemsAdvisoriesResponse viewSystemsAdvisories(body)

View system-advisory pairs for selected systems and advisories

View system-advisory pairs for selected systems and advisories

### Example

```javascript
import PatchmanEngineApi from 'patchman_engine_api';
let defaultClient = PatchmanEngineApi.ApiClient.instance;
// Configure API key authorization: RhIdentity
let RhIdentity = defaultClient.authentications['RhIdentity'];
RhIdentity.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//RhIdentity.apiKeyPrefix = 'Token';

let apiInstance = new PatchmanEngineApi.DefaultApi();
let body = new PatchmanEngineApi.ControllersSystemsAdvisoriesRequest(); // ControllersSystemsAdvisoriesRequest | Request body
apiInstance.viewSystemsAdvisories(body, (error, data, response) => {
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
 **body** | [**ControllersSystemsAdvisoriesRequest**](ControllersSystemsAdvisoriesRequest.md)| Request body | 

### Return type

[**ControllersSystemsAdvisoriesResponse**](ControllersSystemsAdvisoriesResponse.md)

### Authorization

[RhIdentity](../README.md#RhIdentity)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

