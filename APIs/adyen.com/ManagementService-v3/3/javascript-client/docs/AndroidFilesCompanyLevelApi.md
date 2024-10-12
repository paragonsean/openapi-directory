# ManagementApi.AndroidFilesCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

Method | HTTP request | Description
------------- | ------------- | -------------
[**getCompaniesCompanyIdAndroidApps**](AndroidFilesCompanyLevelApi.md#getCompaniesCompanyIdAndroidApps) | **GET** /companies/{companyId}/androidApps | Get a list of Android apps
[**getCompaniesCompanyIdAndroidAppsId**](AndroidFilesCompanyLevelApi.md#getCompaniesCompanyIdAndroidAppsId) | **GET** /companies/{companyId}/androidApps/{id} | Get Android app
[**getCompaniesCompanyIdAndroidCertificates**](AndroidFilesCompanyLevelApi.md#getCompaniesCompanyIdAndroidCertificates) | **GET** /companies/{companyId}/androidCertificates | Get a list of Android certificates
[**postCompaniesCompanyIdAndroidApps**](AndroidFilesCompanyLevelApi.md#postCompaniesCompanyIdAndroidApps) | **POST** /companies/{companyId}/androidApps | Upload Android App



## getCompaniesCompanyIdAndroidApps

> AndroidAppsResponse getCompaniesCompanyIdAndroidApps(companyId, opts)

Get a list of Android apps

Returns a list of the Android apps that are available for the company identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write * Management API—Terminal actions read * Management API—Terminal actions read and write

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

let apiInstance = new ManagementApi.AndroidFilesCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56, // Number | The number of items to have on a page, maximum 100. The default is 20 items on a page.
  'packageName': "packageName_example", // String | The package name that uniquely identifies the Android app.
  'versionCode': 56 // Number | The version number of the app.
};
apiInstance.getCompaniesCompanyIdAndroidApps(companyId, opts, (error, data, response) => {
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
 **packageName** | **String**| The package name that uniquely identifies the Android app. | [optional] 
 **versionCode** | **Number**| The version number of the app. | [optional] 

### Return type

[**AndroidAppsResponse**](AndroidAppsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdAndroidAppsId

> AndroidApp getCompaniesCompanyIdAndroidAppsId(companyId, id)

Get Android app

Returns the details of the Android app identified in the path.  These apps have been uploaded to Adyen and can be installed or uninstalled on Android payment terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write

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

let apiInstance = new ManagementApi.AndroidFilesCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let id = "id_example"; // String | The unique identifier of the app.
apiInstance.getCompaniesCompanyIdAndroidAppsId(companyId, id, (error, data, response) => {
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
 **id** | **String**| The unique identifier of the app. | 

### Return type

[**AndroidApp**](AndroidApp.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## getCompaniesCompanyIdAndroidCertificates

> AndroidCertificatesResponse getCompaniesCompanyIdAndroidCertificates(companyId, opts)

Get a list of Android certificates

Returns a list of the Android certificates that are available for the company identified in the path. Typically, these certificates enable running apps on Android payment terminals. The certifcates in the list have been uploaded to Adyen and can be installed or uninstalled on Android terminals through [terminal actions](https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api).  To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read * Management API—Android files read and write * Management API—Terminal actions read * Management API—Terminal actions read and write

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

let apiInstance = new ManagementApi.AndroidFilesCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
let opts = {
  'pageNumber': 56, // Number | The number of the page to fetch.
  'pageSize': 56, // Number | The number of items to have on a page, maximum 100. The default is 20 items on a page.
  'certificateName': "certificateName_example" // String | The name of the certificate.
};
apiInstance.getCompaniesCompanyIdAndroidCertificates(companyId, opts, (error, data, response) => {
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
 **certificateName** | **String**| The name of the certificate. | [optional] 

### Return type

[**AndroidCertificatesResponse**](AndroidCertificatesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## postCompaniesCompanyIdAndroidApps

> UploadAndroidAppResponse postCompaniesCompanyIdAndroidApps(companyId)

Upload Android App

Uploads an Android APK file to Adyen. The maximum APK file size is 200 MB. To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Android files read and write  &gt;By choosing to upload, install, or run any third-party applications on an Adyen payment terminal, you accept full responsibility and liability for any consequences of uploading, installing, or running any such applications.

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

let apiInstance = new ManagementApi.AndroidFilesCompanyLevelApi();
let companyId = "companyId_example"; // String | The unique identifier of the company account.
apiInstance.postCompaniesCompanyIdAndroidApps(companyId, (error, data, response) => {
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

### Return type

[**UploadAndroidAppResponse**](UploadAndroidAppResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

