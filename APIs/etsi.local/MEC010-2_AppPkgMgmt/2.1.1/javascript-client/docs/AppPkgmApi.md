# EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi

All URIs are relative to *http://etsi.local*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appDGET**](AppPkgmApi.md#appDGET) | **GET** /onboarded_app_packages/{appDId}/appd | Reads the content of the AppD of on-boarded individual application package resources.
[**appDIdGET**](AppPkgmApi.md#appDIdGET) | **GET** /onboarded_app_packages/{appDId}/package_content | Fetch the onboarded application package content identified by appPkgId or appDId.
[**appDIdPUT**](AppPkgmApi.md#appDIdPUT) | **PUT** /onboarded_app_packages/{appDId}/package_content | Uploads the content of application package.
[**appPackageDELETE**](AppPkgmApi.md#appPackageDELETE) | **DELETE** /app_packages/{appPkgId} | Deletes an individual application package resources
[**appPackageGET**](AppPkgmApi.md#appPackageGET) | **GET** /app_packages/{appPkgId} | Queries the information related to individual application package resources
[**appPackagePATCH**](AppPkgmApi.md#appPackagePATCH) | **PATCH** /app_packages/{appPkgId} | Updates the operational state of an individual application package resource
[**appPackagesGET**](AppPkgmApi.md#appPackagesGET) | **GET** /app_packages | Queries information relating to on-boarded application packages in the MEO
[**appPackagesPOST**](AppPkgmApi.md#appPackagesPOST) | **POST** /app_packages | Create a resource for on-boarding an application package to a MEO
[**appPkgGET**](AppPkgmApi.md#appPkgGET) | **GET** /app_packages/{appPkgId}/package_content | Fetch the onboarded application package content identified by appPkgId or appDId.
[**appPkgIdGET**](AppPkgmApi.md#appPkgIdGET) | **GET** /app_packages/{appPkgId}/appd | Reads the content of the AppD of on-boarded individual application package resources.
[**appPkgPUT**](AppPkgmApi.md#appPkgPUT) | **PUT** /app_packages/{appPkgId}/package_content | Uploads the content of application package.
[**individualSubscriptionDELETE**](AppPkgmApi.md#individualSubscriptionDELETE) | **DELETE** /subscriptions/{subscriptionId} | Deletes the individual subscription to notifications about application package changes in MEO.
[**individualSubscriptionGET**](AppPkgmApi.md#individualSubscriptionGET) | **GET** /subscriptions/{subscriptionId} | Used to represent an individual subscription to notifications about application package changes.
[**subscriptionsGET**](AppPkgmApi.md#subscriptionsGET) | **GET** /subscriptions | used to retrieve the information of subscriptions to individual application package resource in MEO
[**subscriptionsPOST**](AppPkgmApi.md#subscriptionsPOST) | **POST** /subscriptions | Subscribe to notifications about on-boarding an application package



## appDGET

> AppD appDGET(appDId, opts)

Reads the content of the AppD of on-boarded individual application package resources.

Reads the content of the AppD of on-boarded individual application package resources.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appDId = "appDId_example"; // String | Identifier of an application descriptor
let opts = {
  'filter': "filter_example", // String | Attribute-based filtering parameters according to ETSI GS MEC 009
  'allFields': "allFields_example", // String | Include all complex attributes in the response.
  'fields': "fields_example", // String | Complex attributes of AppPkgInfo to be included into the response
  'excludeFields': "excludeFields_example", // String | Complex attributes of AppPkgInfo to be excluded from the response.
  'excludeDefault': "excludeDefault_example" // String | Indicates to exclude the following complex attributes of AppPkgInfo from the response.
};
apiInstance.appDGET(appDId, opts, (error, data, response) => {
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
 **appDId** | **String**| Identifier of an application descriptor | 
 **filter** | **String**| Attribute-based filtering parameters according to ETSI GS MEC 009 | [optional] 
 **allFields** | **String**| Include all complex attributes in the response. | [optional] 
 **fields** | **String**| Complex attributes of AppPkgInfo to be included into the response | [optional] 
 **excludeFields** | **String**| Complex attributes of AppPkgInfo to be excluded from the response. | [optional] 
 **excludeDefault** | **String**| Indicates to exclude the following complex attributes of AppPkgInfo from the response. | [optional] 

### Return type

[**AppD**](AppD.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip, text/plain, application/json


## appDIdGET

> appDIdGET(appDId)

Fetch the onboarded application package content identified by appPkgId or appDId.

Fetch the onboarded application package content identified by appPkgId or appDId.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appDId = "appDId_example"; // String | Identifier of an application descriptor
apiInstance.appDIdGET(appDId, (error, data, response) => {
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
 **appDId** | **String**| Identifier of an application descriptor | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appDIdPUT

> appDIdPUT(appDId, opts)

Uploads the content of application package.

Uploads the content of application package.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appDId = "appDId_example"; // String | Identifier of an application descriptor
let opts = {
  'body': "/path/to/file" // File | 
};
apiInstance.appDIdPUT(appDId, opts, (error, data, response) => {
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
 **appDId** | **String**| Identifier of an application descriptor | 
 **body** | **File**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/zip
- **Accept**: application/json


## appPackageDELETE

> appPackageDELETE(appPkgId)

Deletes an individual application package resources

Deletes an individual application package resources

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgId = "appPkgId_example"; // String | Identifier of an individual application package resource
apiInstance.appPackageDELETE(appPkgId, (error, data, response) => {
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
 **appPkgId** | **String**| Identifier of an individual application package resource | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPackageGET

> AppPkgInfo appPackageGET(appPkgId)

Queries the information related to individual application package resources

Queries the information related to individual application package resources

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgId = "appPkgId_example"; // String | Identifier of an individual application package resource
apiInstance.appPackageGET(appPkgId, (error, data, response) => {
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
 **appPkgId** | **String**| Identifier of an individual application package resource | 

### Return type

[**AppPkgInfo**](AppPkgInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPackagePATCH

> AppPkgInfoModifications appPackagePATCH(appPkgId, appPkgInfoModifications)

Updates the operational state of an individual application package resource

Updates the operational state of an individual application package resources

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgId = "appPkgId_example"; // String | Identifier of an individual application package resource
let appPkgInfoModifications = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgInfoModifications(); // AppPkgInfoModifications | Operational state to be set
apiInstance.appPackagePATCH(appPkgId, appPkgInfoModifications, (error, data, response) => {
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
 **appPkgId** | **String**| Identifier of an individual application package resource | 
 **appPkgInfoModifications** | [**AppPkgInfoModifications**](AppPkgInfoModifications.md)| Operational state to be set | 

### Return type

[**AppPkgInfoModifications**](AppPkgInfoModifications.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appPackagesGET

> [AppPkgInfo] appPackagesGET(opts)

Queries information relating to on-boarded application packages in the MEO

queries information relating to on-boarded application packages in the MEO

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let opts = {
  'filter': "filter_example", // String | Attribute-based filtering parameters according to ETSI GS MEC 009
  'allFields': "allFields_example", // String | Include all complex attributes in the response.
  'fields': "fields_example", // String | Complex attributes of AppPkgInfo to be included into the response
  'excludeFields': "excludeFields_example", // String | Complex attributes of AppPkgInfo to be excluded from the response.
  'excludeDefault': "excludeDefault_example" // String | Indicates to exclude the following complex attributes of AppPkgInfo from the response.
};
apiInstance.appPackagesGET(opts, (error, data, response) => {
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
 **filter** | **String**| Attribute-based filtering parameters according to ETSI GS MEC 009 | [optional] 
 **allFields** | **String**| Include all complex attributes in the response. | [optional] 
 **fields** | **String**| Complex attributes of AppPkgInfo to be included into the response | [optional] 
 **excludeFields** | **String**| Complex attributes of AppPkgInfo to be excluded from the response. | [optional] 
 **excludeDefault** | **String**| Indicates to exclude the following complex attributes of AppPkgInfo from the response. | [optional] 

### Return type

[**[AppPkgInfo]**](AppPkgInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPackagesPOST

> [AppPkgInfo] appPackagesPOST(createAppPkg)

Create a resource for on-boarding an application package to a MEO

Create a resource for on-boarding an application package to a MEO

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let createAppPkg = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.CreateAppPkg(); // CreateAppPkg | Resource to be created
apiInstance.appPackagesPOST(createAppPkg, (error, data, response) => {
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
 **createAppPkg** | [**CreateAppPkg**](CreateAppPkg.md)| Resource to be created | 

### Return type

[**[AppPkgInfo]**](AppPkgInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appPkgGET

> appPkgGET(appPkgId)

Fetch the onboarded application package content identified by appPkgId or appDId.

Fetch the onboarded application package content identified by appPkgId or appDId.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgId = "appPkgId_example"; // String | Identifier of an on-boarded individual application package
apiInstance.appPkgGET(appPkgId, (error, data, response) => {
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
 **appPkgId** | **String**| Identifier of an on-boarded individual application package | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appPkgIdGET

> AppD appPkgIdGET(appPkgId, opts)

Reads the content of the AppD of on-boarded individual application package resources.

Reads the content of the AppD of on-boarded individual application package resources.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgId = "appPkgId_example"; // String | Identifier of an on-boarded individual application package
let opts = {
  'filter': "filter_example", // String | Attribute-based filtering parameters according to ETSI GS MEC 009
  'allFields': "allFields_example", // String | Include all complex attributes in the response.
  'fields': "fields_example", // String | Complex attributes of AppPkgInfo to be included into the response
  'excludeFields': "excludeFields_example", // String | Complex attributes of AppPkgInfo to be excluded from the response.
  'excludeDefault': "excludeDefault_example" // String | Indicates to exclude the following complex attributes of AppPkgInfo from the response.
};
apiInstance.appPkgIdGET(appPkgId, opts, (error, data, response) => {
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
 **appPkgId** | **String**| Identifier of an on-boarded individual application package | 
 **filter** | **String**| Attribute-based filtering parameters according to ETSI GS MEC 009 | [optional] 
 **allFields** | **String**| Include all complex attributes in the response. | [optional] 
 **fields** | **String**| Complex attributes of AppPkgInfo to be included into the response | [optional] 
 **excludeFields** | **String**| Complex attributes of AppPkgInfo to be excluded from the response. | [optional] 
 **excludeDefault** | **String**| Indicates to exclude the following complex attributes of AppPkgInfo from the response. | [optional] 

### Return type

[**AppD**](AppD.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/zip, text/plain, application/json


## appPkgPUT

> appPkgPUT(appPkgId, opts)

Uploads the content of application package.

Uploads the content of application package.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgId = "appPkgId_example"; // String | Identifier of an on-boarded individual application package
let opts = {
  'body': "/path/to/file" // File | 
};
apiInstance.appPkgPUT(appPkgId, opts, (error, data, response) => {
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
 **appPkgId** | **String**| Identifier of an on-boarded individual application package | 
 **body** | **File**|  | [optional] 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/zip
- **Accept**: application/json


## individualSubscriptionDELETE

> individualSubscriptionDELETE(subscriptionId)

Deletes the individual subscription to notifications about application package changes in MEO.

Deletes the individual subscription to notifications about application package changes in MEO.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of an individual subscription to notifications about application package changes
apiInstance.individualSubscriptionDELETE(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of an individual subscription to notifications about application package changes | 

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## individualSubscriptionGET

> AppPkgSubscriptionInfo individualSubscriptionGET(subscriptionId)

Used to represent an individual subscription to notifications about application package changes.

Used to represent an individual subscription to notifications about application package changes.

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let subscriptionId = "subscriptionId_example"; // String | Identifier of an individual subscription to notifications about application package changes
apiInstance.individualSubscriptionGET(subscriptionId, (error, data, response) => {
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
 **subscriptionId** | **String**| Identifier of an individual subscription to notifications about application package changes | 

### Return type

[**AppPkgSubscriptionInfo**](AppPkgSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsGET

> AppPkgSubscriptionLinkList subscriptionsGET()

used to retrieve the information of subscriptions to individual application package resource in MEO

used to retrieve the information of subscriptions to individual application package resource in MEO package

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
apiInstance.subscriptionsGET((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AppPkgSubscriptionLinkList**](AppPkgSubscriptionLinkList.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## subscriptionsPOST

> AppPkgSubscriptionInfo subscriptionsPOST(appPkgSubscription)

Subscribe to notifications about on-boarding an application package

Subscribe to notifications about on-boarding an application package

### Example

```javascript
import EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement from 'etsi_gs_mec_010_2_part_2_application_lifecycle_rules_and_requirements_management';

let apiInstance = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgmApi();
let appPkgSubscription = new EtsiGsMec0102Part2ApplicationLifecycleRulesAndRequirementsManagement.AppPkgSubscription(); // AppPkgSubscription | The input parameters of subscribe operation to notifications
apiInstance.subscriptionsPOST(appPkgSubscription, (error, data, response) => {
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
 **appPkgSubscription** | [**AppPkgSubscription**](AppPkgSubscription.md)| The input parameters of subscribe operation to notifications | 

### Return type

[**AppPkgSubscriptionInfo**](AppPkgSubscriptionInfo.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

