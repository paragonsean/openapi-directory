# FirebaseManagementApi.ProjectsApi

All URIs are relative to *https://firebase.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firebaseProjectsAddFirebase**](ProjectsApi.md#firebaseProjectsAddFirebase) | **POST** /v1beta1/{project}:addFirebase | 
[**firebaseProjectsAddGoogleAnalytics**](ProjectsApi.md#firebaseProjectsAddGoogleAnalytics) | **POST** /v1beta1/{parent}:addGoogleAnalytics | 
[**firebaseProjectsAndroidAppsCreate**](ProjectsApi.md#firebaseProjectsAndroidAppsCreate) | **POST** /v1beta1/{parent}/androidApps | 
[**firebaseProjectsAndroidAppsList**](ProjectsApi.md#firebaseProjectsAndroidAppsList) | **GET** /v1beta1/{parent}/androidApps | 
[**firebaseProjectsAndroidAppsShaCreate**](ProjectsApi.md#firebaseProjectsAndroidAppsShaCreate) | **POST** /v1beta1/{parent}/sha | 
[**firebaseProjectsAndroidAppsShaDelete**](ProjectsApi.md#firebaseProjectsAndroidAppsShaDelete) | **DELETE** /v1beta1/{name} | 
[**firebaseProjectsAndroidAppsShaList**](ProjectsApi.md#firebaseProjectsAndroidAppsShaList) | **GET** /v1beta1/{parent}/sha | 
[**firebaseProjectsAvailableLocationsList**](ProjectsApi.md#firebaseProjectsAvailableLocationsList) | **GET** /v1beta1/{parent}/availableLocations | 
[**firebaseProjectsDefaultLocationFinalize**](ProjectsApi.md#firebaseProjectsDefaultLocationFinalize) | **POST** /v1beta1/{parent}/defaultLocation:finalize | 
[**firebaseProjectsIosAppsCreate**](ProjectsApi.md#firebaseProjectsIosAppsCreate) | **POST** /v1beta1/{parent}/iosApps | 
[**firebaseProjectsIosAppsList**](ProjectsApi.md#firebaseProjectsIosAppsList) | **GET** /v1beta1/{parent}/iosApps | 
[**firebaseProjectsList**](ProjectsApi.md#firebaseProjectsList) | **GET** /v1beta1/projects | 
[**firebaseProjectsRemoveAnalytics**](ProjectsApi.md#firebaseProjectsRemoveAnalytics) | **POST** /v1beta1/{parent}:removeAnalytics | 
[**firebaseProjectsSearchApps**](ProjectsApi.md#firebaseProjectsSearchApps) | **GET** /v1beta1/{parent}:searchApps | 
[**firebaseProjectsWebAppsCreate**](ProjectsApi.md#firebaseProjectsWebAppsCreate) | **POST** /v1beta1/{parent}/webApps | 
[**firebaseProjectsWebAppsGetConfig**](ProjectsApi.md#firebaseProjectsWebAppsGetConfig) | **GET** /v1beta1/{name} | 
[**firebaseProjectsWebAppsList**](ProjectsApi.md#firebaseProjectsWebAppsList) | **GET** /v1beta1/{parent}/webApps | 
[**firebaseProjectsWebAppsPatch**](ProjectsApi.md#firebaseProjectsWebAppsPatch) | **PATCH** /v1beta1/{name} | 
[**firebaseProjectsWebAppsRemove**](ProjectsApi.md#firebaseProjectsWebAppsRemove) | **POST** /v1beta1/{name}:remove | 
[**firebaseProjectsWebAppsUndelete**](ProjectsApi.md#firebaseProjectsWebAppsUndelete) | **POST** /v1beta1/{name}:undelete | 



## firebaseProjectsAddFirebase

> Operation firebaseProjectsAddFirebase(project, opts)



Adds Firebase resources to the specified existing [Google Cloud Platform (GCP) &#x60;Project&#x60;] (https://cloud.google.com/resource-manager/reference/rest/v1/projects). Since a FirebaseProject is actually also a GCP &#x60;Project&#x60;, a &#x60;FirebaseProject&#x60; has the same underlying GCP identifiers (&#x60;projectNumber&#x60; and &#x60;projectId&#x60;). This allows for easy interop with Google APIs. The result of this call is an [&#x60;Operation&#x60;](../../v1beta1/operations). Poll the &#x60;Operation&#x60; to track the provisioning process by calling GetOperation until [&#x60;done&#x60;](../../v1beta1/operations#Operation.FIELDS.done) is &#x60;true&#x60;. When &#x60;done&#x60; is &#x60;true&#x60;, the &#x60;Operation&#x60; has either succeeded or failed. If the &#x60;Operation&#x60; succeeded, its [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) is set to a FirebaseProject; if the &#x60;Operation&#x60; failed, its [&#x60;error&#x60;](../../v1beta1/operations#Operation.FIELDS.error) is set to a google.rpc.Status. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call DeleteOperation. This method does not modify any billing account information on the underlying GCP &#x60;Project&#x60;. To call &#x60;AddFirebase&#x60;, a project member or service account must have the following permissions (the IAM roles of Editor and Owner contain these permissions): &#x60;firebase.projects.update&#x60;, &#x60;resourcemanager.projects.get&#x60;, &#x60;serviceusage.services.enable&#x60;, and &#x60;serviceusage.services.get&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let project = "project_example"; // String | The resource name of the GCP `Project` to which Firebase resources will be added, in the format: projects/PROJECT_IDENTIFIER Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. After calling `AddFirebase`, the unique Project identifiers ( [`projectNumber`](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_number) and [`projectId`](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_id)) of the underlying GCP `Project` are also the identifiers of the FirebaseProject.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'addFirebaseRequest': new FirebaseManagementApi.AddFirebaseRequest() // AddFirebaseRequest | 
};
apiInstance.firebaseProjectsAddFirebase(project, opts, (error, data, response) => {
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
 **project** | **String**| The resource name of the GCP &#x60;Project&#x60; to which Firebase resources will be added, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. After calling &#x60;AddFirebase&#x60;, the unique Project identifiers ( [&#x60;projectNumber&#x60;](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_number) and [&#x60;projectId&#x60;](https://cloud.google.com/resource-manager/reference/rest/v1/projects#Project.FIELDS.project_id)) of the underlying GCP &#x60;Project&#x60; are also the identifiers of the FirebaseProject. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **addFirebaseRequest** | [**AddFirebaseRequest**](AddFirebaseRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsAddGoogleAnalytics

> Operation firebaseProjectsAddGoogleAnalytics(parent, opts)



Links the specified FirebaseProject with an existing [Google Analytics account](http://www.google.com/analytics/). Using this call, you can either: - Specify an &#x60;analyticsAccountId&#x60; to provision a new Google Analytics property within the specified account and associate the new property with the &#x60;FirebaseProject&#x60;. - Specify an existing &#x60;analyticsPropertyId&#x60; to associate the property with the &#x60;FirebaseProject&#x60;. Note that when you call &#x60;AddGoogleAnalytics&#x60;: 1. The first check determines if any existing data streams in the Google Analytics property correspond to any existing Firebase Apps in the &#x60;FirebaseProject&#x60; (based on the &#x60;packageName&#x60; or &#x60;bundleId&#x60; associated with the data stream). Then, as applicable, the data streams and apps are linked. Note that this auto-linking only applies to &#x60;AndroidApps&#x60; and &#x60;IosApps&#x60;. 2. If no corresponding data streams are found for the Firebase Apps, new data streams are provisioned in the Google Analytics property for each of the Firebase Apps. Note that a new data stream is always provisioned for a Web App even if it was previously associated with a data stream in the Analytics property. Learn more about the hierarchy and structure of Google Analytics accounts in the [Analytics documentation](https://support.google.com/analytics/answer/9303323). The result of this call is an [&#x60;Operation&#x60;](../../v1beta1/operations). Poll the &#x60;Operation&#x60; to track the provisioning process by calling GetOperation until [&#x60;done&#x60;](../../v1beta1/operations#Operation.FIELDS.done) is &#x60;true&#x60;. When &#x60;done&#x60; is &#x60;true&#x60;, the &#x60;Operation&#x60; has either succeeded or failed. If the &#x60;Operation&#x60; succeeded, its [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) is set to an AnalyticsDetails; if the &#x60;Operation&#x60; failed, its [&#x60;error&#x60;](../../v1beta1/operations#Operation.FIELDS.error) is set to a google.rpc.Status. To call &#x60;AddGoogleAnalytics&#x60;, a project member must be an Owner for the existing &#x60;FirebaseProject&#x60; and have the [&#x60;Edit&#x60; permission](https://support.google.com/analytics/answer/2884495) for the Google Analytics account. If the &#x60;FirebaseProject&#x60; already has Google Analytics enabled, and you call &#x60;AddGoogleAnalytics&#x60; using an &#x60;analyticsPropertyId&#x60; that&#39;s different from the currently associated property, then the call will fail. Analytics may have already been enabled in the Firebase console or by specifying &#x60;timeZone&#x60; and &#x60;regionCode&#x60; in the call to [&#x60;AddFirebase&#x60;](../../v1beta1/projects/addFirebase).

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the FirebaseProject to link to an existing Google Analytics account, in the format: projects/PROJECT_IDENTIFIER Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'addGoogleAnalyticsRequest': new FirebaseManagementApi.AddGoogleAnalyticsRequest() // AddGoogleAnalyticsRequest | 
};
apiInstance.firebaseProjectsAddGoogleAnalytics(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the FirebaseProject to link to an existing Google Analytics account, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **addGoogleAnalyticsRequest** | [**AddGoogleAnalyticsRequest**](AddGoogleAnalyticsRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsAndroidAppsCreate

> Operation firebaseProjectsAndroidAppsCreate(parent, opts)



Requests the creation of a new AndroidApp in the specified FirebaseProject. The result of this call is an &#x60;Operation&#x60; which can be used to track the provisioning process. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call &#x60;DeleteOperation&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent FirebaseProject in which to create an AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'androidApp': new FirebaseManagementApi.AndroidApp() // AndroidApp | 
};
apiInstance.firebaseProjectsAndroidAppsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent FirebaseProject in which to create an AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **androidApp** | [**AndroidApp**](AndroidApp.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsAndroidAppsList

> ListAndroidAppsResponse firebaseProjectsAndroidAppsList(parent, opts)



Lists each AndroidApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a &#x60;pageToken&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent FirebaseProject for which to list each associated AndroidApp, in the format: projects/PROJECT_IDENTIFIER /androidApps Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of Apps to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit.
  'pageToken': "pageToken_example", // String | Token returned from a previous call to `ListAndroidApps` indicating where in the set of Apps to resume listing.
  'showDeleted': true // Boolean | Controls whether Apps in the DELETED state should be returned in the response. If not specified, only `ACTIVE` Apps will be returned.
};
apiInstance.firebaseProjectsAndroidAppsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent FirebaseProject for which to list each associated AndroidApp, in the format: projects/PROJECT_IDENTIFIER /androidApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of Apps to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. | [optional] 
 **pageToken** | **String**| Token returned from a previous call to &#x60;ListAndroidApps&#x60; indicating where in the set of Apps to resume listing. | [optional] 
 **showDeleted** | **Boolean**| Controls whether Apps in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned. | [optional] 

### Return type

[**ListAndroidAppsResponse**](ListAndroidAppsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsAndroidAppsShaCreate

> ShaCertificate firebaseProjectsAndroidAppsShaCreate(parent, opts)



Adds a ShaCertificate to the specified AndroidApp.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent AndroidApp to which to add a ShaCertificate, in the format: projects/PROJECT_IDENTIFIER/androidApps/ APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/androidApps/APP_ID Refer to the `AndroidApp` [`name`](../projects.androidApps#AndroidApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'shaCertificate': new FirebaseManagementApi.ShaCertificate() // ShaCertificate | 
};
apiInstance.firebaseProjectsAndroidAppsShaCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent AndroidApp to which to add a ShaCertificate, in the format: projects/PROJECT_IDENTIFIER/androidApps/ APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/androidApps/APP_ID Refer to the &#x60;AndroidApp&#x60; [&#x60;name&#x60;](../projects.androidApps#AndroidApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **shaCertificate** | [**ShaCertificate**](ShaCertificate.md)|  | [optional] 

### Return type

[**ShaCertificate**](ShaCertificate.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsAndroidAppsShaDelete

> Object firebaseProjectsAndroidAppsShaDelete(name, opts)



Removes a ShaCertificate from the specified AndroidApp.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let name = "name_example"; // String | The resource name of the ShaCertificate to remove from the parent AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps/APP_ID /sha/SHA_HASH Refer to the `ShaCertificate` [`name`](../projects.androidApps.sha#ShaCertificate.FIELDS.name) field for details about PROJECT_IDENTIFIER, APP_ID, and SHA_HASH values. You can obtain the full resource name of the `ShaCertificate` from the response of [`ListShaCertificates`](../projects.androidApps.sha/list) or the original [`CreateShaCertificate`](../projects.androidApps.sha/create).
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firebaseProjectsAndroidAppsShaDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the ShaCertificate to remove from the parent AndroidApp, in the format: projects/PROJECT_IDENTIFIER/androidApps/APP_ID /sha/SHA_HASH Refer to the &#x60;ShaCertificate&#x60; [&#x60;name&#x60;](../projects.androidApps.sha#ShaCertificate.FIELDS.name) field for details about PROJECT_IDENTIFIER, APP_ID, and SHA_HASH values. You can obtain the full resource name of the &#x60;ShaCertificate&#x60; from the response of [&#x60;ListShaCertificates&#x60;](../projects.androidApps.sha/list) or the original [&#x60;CreateShaCertificate&#x60;](../projects.androidApps.sha/create). | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsAndroidAppsShaList

> ListShaCertificatesResponse firebaseProjectsAndroidAppsShaList(parent, opts)



Lists the SHA-1 and SHA-256 certificates for the specified AndroidApp.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent AndroidApp for which to list each associated ShaCertificate, in the format: projects/PROJECT_IDENTIFIER /androidApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/androidApps/APP_ID Refer to the `AndroidApp` [`name`](../projects.androidApps#AndroidApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firebaseProjectsAndroidAppsShaList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent AndroidApp for which to list each associated ShaCertificate, in the format: projects/PROJECT_IDENTIFIER /androidApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/androidApps/APP_ID Refer to the &#x60;AndroidApp&#x60; [&#x60;name&#x60;](../projects.androidApps#AndroidApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**ListShaCertificatesResponse**](ListShaCertificatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsAvailableLocationsList

> ListAvailableLocationsResponse firebaseProjectsAvailableLocationsList(parent, opts)



**DEPRECATED.** _Instead, use the applicable resource-specific REST API (or associated documentation, as needed) to determine valid locations for each resource used in your Project._ Lists the valid Google Cloud Platform (GCP) resource locations for the specified Project (including a FirebaseProject). One of these locations can be selected as the Project&#39;s [_default_ GCP resource location](https://firebase.google.com/docs/projects/locations), which is the geographical location where the Project&#39;s resources, such as Cloud Firestore, will be provisioned by default. However, if the default GCP resource location has already been set for the Project, then this setting cannot be changed. This call checks for any possible [location restrictions](https://cloud.google.com/resource-manager/docs/organization-policy/defining-locations) for the specified Project and, thus, might return a subset of all possible GCP resource locations. To list all GCP resource locations (regardless of any restrictions), call the endpoint without specifying a unique project identifier (that is, &#x60;/v1beta1/{parent&#x3D;projects/-}/listAvailableLocations&#x60;). To call &#x60;ListAvailableLocations&#x60; with a specified project, a member must be at minimum a Viewer of the Project. Calls without a specified project do not require any specific project permissions.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The FirebaseProject for which to list GCP resource locations, in the format: projects/PROJECT_IDENTIFIER Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. If no unique project identifier is specified (that is, `projects/-`), the returned list does not take into account org-specific or project-specific location restrictions.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of locations to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative.
  'pageToken': "pageToken_example" // String | Token returned from a previous call to `ListAvailableLocations` indicating where in the list of locations to resume listing.
};
apiInstance.firebaseProjectsAvailableLocationsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The FirebaseProject for which to list GCP resource locations, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. If no unique project identifier is specified (that is, &#x60;projects/-&#x60;), the returned list does not take into account org-specific or project-specific location restrictions. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of locations to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative. | [optional] 
 **pageToken** | **String**| Token returned from a previous call to &#x60;ListAvailableLocations&#x60; indicating where in the list of locations to resume listing. | [optional] 

### Return type

[**ListAvailableLocationsResponse**](ListAvailableLocationsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsDefaultLocationFinalize

> Operation firebaseProjectsDefaultLocationFinalize(parent, opts)



**DEPRECATED.** _Instead, use the applicable resource-specific REST API to set the location for each resource used in your Project._ Sets the default Google Cloud Platform (GCP) resource location for the specified FirebaseProject. This method creates an App Engine application with a [default Cloud Storage bucket](https://cloud.google.com/appengine/docs/standard/python/googlecloudstorageclient/setting-up-cloud-storage#activating_a_cloud_storage_bucket), located in the specified [&#x60;locationId&#x60;](#body.request_body.FIELDS.location_id). This location must be one of the available [GCP resource locations](https://firebase.google.com/docs/projects/locations). After the default GCP resource location is finalized, or if it was already set, it cannot be changed. The default GCP resource location for the specified &#x60;FirebaseProject&#x60; might already be set because either the underlying GCP &#x60;Project&#x60; already has an App Engine application or &#x60;FinalizeDefaultLocation&#x60; was previously called with a specified &#x60;locationId&#x60;. Any new calls to &#x60;FinalizeDefaultLocation&#x60; with a *different* specified &#x60;locationId&#x60; will return a 409 error. The result of this call is an [&#x60;Operation&#x60;](../../v1beta1/operations), which can be used to track the provisioning process. The [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) type of the &#x60;Operation&#x60; is google.protobuf.Empty. The &#x60;Operation&#x60; can be polled by its &#x60;name&#x60; using GetOperation until &#x60;done&#x60; is true. When &#x60;done&#x60; is true, the &#x60;Operation&#x60; has either succeeded or failed. If the &#x60;Operation&#x60; has succeeded, its [&#x60;response&#x60;](../../v1beta1/operations#Operation.FIELDS.response) will be set to a google.protobuf.Empty; if the &#x60;Operation&#x60; has failed, its &#x60;error&#x60; will be set to a google.rpc.Status. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call DeleteOperation. All fields listed in the [request body](#request-body) are required. To call &#x60;FinalizeDefaultLocation&#x60;, a member must be an Owner of the Project.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the FirebaseProject for which the default GCP resource location will be set, in the format: projects/PROJECT_IDENTIFIER Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'finalizeDefaultLocationRequest': new FirebaseManagementApi.FinalizeDefaultLocationRequest() // FinalizeDefaultLocationRequest | 
};
apiInstance.firebaseProjectsDefaultLocationFinalize(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the FirebaseProject for which the default GCP resource location will be set, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **finalizeDefaultLocationRequest** | [**FinalizeDefaultLocationRequest**](FinalizeDefaultLocationRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsIosAppsCreate

> Operation firebaseProjectsIosAppsCreate(parent, opts)



Requests the creation of a new IosApp in the specified FirebaseProject. The result of this call is an &#x60;Operation&#x60; which can be used to track the provisioning process. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call &#x60;DeleteOperation&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent FirebaseProject in which to create an IosApp, in the format: projects/PROJECT_IDENTIFIER/iosApps Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'iosApp': new FirebaseManagementApi.IosApp() // IosApp | 
};
apiInstance.firebaseProjectsIosAppsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent FirebaseProject in which to create an IosApp, in the format: projects/PROJECT_IDENTIFIER/iosApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **iosApp** | [**IosApp**](IosApp.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsIosAppsList

> ListIosAppsResponse firebaseProjectsIosAppsList(parent, opts)



Lists each IosApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a &#x60;pageToken&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent FirebaseProject for which to list each associated IosApp, in the format: projects/PROJECT_IDENTIFIER/iosApps Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of Apps to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit.
  'pageToken': "pageToken_example", // String | Token returned from a previous call to `ListIosApps` indicating where in the set of Apps to resume listing.
  'showDeleted': true // Boolean | Controls whether Apps in the DELETED state should be returned in the response. If not specified, only `ACTIVE` Apps will be returned.
};
apiInstance.firebaseProjectsIosAppsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent FirebaseProject for which to list each associated IosApp, in the format: projects/PROJECT_IDENTIFIER/iosApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of Apps to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. | [optional] 
 **pageToken** | **String**| Token returned from a previous call to &#x60;ListIosApps&#x60; indicating where in the set of Apps to resume listing. | [optional] 
 **showDeleted** | **Boolean**| Controls whether Apps in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned. | [optional] 

### Return type

[**ListIosAppsResponse**](ListIosAppsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsList

> ListFirebaseProjectsResponse firebaseProjectsList(opts)



Lists each FirebaseProject accessible to the caller. The elements are returned in no particular order, but they will be a consistent view of the Projects when additional requests are made with a &#x60;pageToken&#x60;. This method is eventually consistent with Project mutations, which means newly provisioned Projects and recent modifications to existing Projects might not be reflected in the set of Projects. The list will include only ACTIVE Projects. Use GetFirebaseProject for consistent reads as well as for additional Project details.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of Projects to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. This value cannot be negative.
  'pageToken': "pageToken_example", // String | Token returned from a previous call to `ListFirebaseProjects` indicating where in the set of Projects to resume listing.
  'showDeleted': true // Boolean | Optional. Controls whether Projects in the DELETED state should be returned in the response. If not specified, only `ACTIVE` Projects will be returned.
};
apiInstance.firebaseProjectsList(opts, (error, data, response) => {
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
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of Projects to return in the response. The server may return fewer than this at its discretion. If no value is specified (or too large a value is specified), the server will impose its own limit. This value cannot be negative. | [optional] 
 **pageToken** | **String**| Token returned from a previous call to &#x60;ListFirebaseProjects&#x60; indicating where in the set of Projects to resume listing. | [optional] 
 **showDeleted** | **Boolean**| Optional. Controls whether Projects in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Projects will be returned. | [optional] 

### Return type

[**ListFirebaseProjectsResponse**](ListFirebaseProjectsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsRemoveAnalytics

> Object firebaseProjectsRemoveAnalytics(parent, opts)



Unlinks the specified FirebaseProject from its Google Analytics account. This call removes the association of the specified &#x60;FirebaseProject&#x60; with its current Google Analytics property. However, this call does not delete the Google Analytics resources, such as the Google Analytics property or any data streams. These resources may be re-associated later to the &#x60;FirebaseProject&#x60; by calling [&#x60;AddGoogleAnalytics&#x60;](../../v1beta1/projects/addGoogleAnalytics) and specifying the same &#x60;analyticsPropertyId&#x60;. For Android Apps and iOS Apps, this call re-links data streams with their corresponding apps. However, for Web Apps, this call provisions a *new* data stream for each Web App. To call &#x60;RemoveAnalytics&#x60;, a project member must be an Owner for the &#x60;FirebaseProject&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the FirebaseProject to unlink from its Google Analytics account, in the format: projects/PROJECT_IDENTIFIER Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'removeAnalyticsRequest': new FirebaseManagementApi.RemoveAnalyticsRequest() // RemoveAnalyticsRequest | 
};
apiInstance.firebaseProjectsRemoveAnalytics(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the FirebaseProject to unlink from its Google Analytics account, in the format: projects/PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **removeAnalyticsRequest** | [**RemoveAnalyticsRequest**](RemoveAnalyticsRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsSearchApps

> SearchFirebaseAppsResponse firebaseProjectsSearchApps(parent, opts)



Lists all available Apps for the specified FirebaseProject. This is a convenience method. Typically, interaction with an App should be done using the platform-specific service, but some tool use-cases require a summary of all known Apps (such as for App selector interfaces).

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The parent FirebaseProject for which to list Apps, in the format: projects/ PROJECT_IDENTIFIER Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'filter': "filter_example", // String | A query string compatible with Google's [AIP-160 standard](https://google.aip.dev/160). Use any of the following fields in a query: * [`app_id`](../projects/searchApps#FirebaseAppInfo.FIELDS.app_id) * [`namespace`](../projects/searchApps#FirebaseAppInfo.FIELDS.namespace) * [`platform`](../projects/searchApps#FirebaseAppInfo.FIELDS.platform) This query also supports the following \"virtual\" fields. These are fields which are not actually part of the returned resource object, but they can be queried as if they are pre-populated with specific values. * `sha1_hash` or `sha1_hashes`: This field is considered to be a _repeated_ `string` field, populated with the list of all SHA-1 certificate fingerprints registered with the AndroidApp. This list is empty if the App is not an `AndroidApp`. * `sha256_hash` or `sha256_hashes`: This field is considered to be a _repeated_ `string` field, populated with the list of all SHA-256 certificate fingerprints registered with the AndroidApp. This list is empty if the App is not an `AndroidApp`. * `app_store_id`: This field is considered to be a _singular_ `string` field, populated with the Apple App Store ID registered with the IosApp. This field is empty if the App is not an `IosApp`. * `team_id`: This field is considered to be a _singular_ `string` field, populated with the Apple team ID registered with the IosApp. This field is empty if the App is not an `IosApp`.
  'pageSize': 56, // Number | The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative.
  'pageToken': "pageToken_example", // String | Token returned from a previous call to `SearchFirebaseApps` indicating where in the set of Apps to resume listing.
  'showDeleted': true // Boolean | Controls whether Apps in the DELETED state should be returned. If not specified, only `ACTIVE` Apps will be returned.
};
apiInstance.firebaseProjectsSearchApps(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The parent FirebaseProject for which to list Apps, in the format: projects/ PROJECT_IDENTIFIER Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **filter** | **String**| A query string compatible with Google&#39;s [AIP-160 standard](https://google.aip.dev/160). Use any of the following fields in a query: * [&#x60;app_id&#x60;](../projects/searchApps#FirebaseAppInfo.FIELDS.app_id) * [&#x60;namespace&#x60;](../projects/searchApps#FirebaseAppInfo.FIELDS.namespace) * [&#x60;platform&#x60;](../projects/searchApps#FirebaseAppInfo.FIELDS.platform) This query also supports the following \&quot;virtual\&quot; fields. These are fields which are not actually part of the returned resource object, but they can be queried as if they are pre-populated with specific values. * &#x60;sha1_hash&#x60; or &#x60;sha1_hashes&#x60;: This field is considered to be a _repeated_ &#x60;string&#x60; field, populated with the list of all SHA-1 certificate fingerprints registered with the AndroidApp. This list is empty if the App is not an &#x60;AndroidApp&#x60;. * &#x60;sha256_hash&#x60; or &#x60;sha256_hashes&#x60;: This field is considered to be a _repeated_ &#x60;string&#x60; field, populated with the list of all SHA-256 certificate fingerprints registered with the AndroidApp. This list is empty if the App is not an &#x60;AndroidApp&#x60;. * &#x60;app_store_id&#x60;: This field is considered to be a _singular_ &#x60;string&#x60; field, populated with the Apple App Store ID registered with the IosApp. This field is empty if the App is not an &#x60;IosApp&#x60;. * &#x60;team_id&#x60;: This field is considered to be a _singular_ &#x60;string&#x60; field, populated with the Apple team ID registered with the IosApp. This field is empty if the App is not an &#x60;IosApp&#x60;. | [optional] 
 **pageSize** | **Number**| The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. This value cannot be negative. | [optional] 
 **pageToken** | **String**| Token returned from a previous call to &#x60;SearchFirebaseApps&#x60; indicating where in the set of Apps to resume listing. | [optional] 
 **showDeleted** | **Boolean**| Controls whether Apps in the DELETED state should be returned. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned. | [optional] 

### Return type

[**SearchFirebaseAppsResponse**](SearchFirebaseAppsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsWebAppsCreate

> Operation firebaseProjectsWebAppsCreate(parent, opts)



Requests the creation of a new WebApp in the specified FirebaseProject. The result of this call is an &#x60;Operation&#x60; which can be used to track the provisioning process. The &#x60;Operation&#x60; is automatically deleted after completion, so there is no need to call &#x60;DeleteOperation&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent FirebaseProject in which to create a WebApp, in the format: projects/PROJECT_IDENTIFIER/webApps Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'webApp': new FirebaseManagementApi.WebApp() // WebApp | 
};
apiInstance.firebaseProjectsWebAppsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent FirebaseProject in which to create a WebApp, in the format: projects/PROJECT_IDENTIFIER/webApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **webApp** | [**WebApp**](WebApp.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsWebAppsGetConfig

> WebAppConfig firebaseProjectsWebAppsGetConfig(name, opts)



Gets the configuration artifact associated with the specified WebApp.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let name = "name_example"; // String | The resource name of the WebApp configuration to download, in the format: projects/PROJECT_IDENTIFIER/webApps/APP_ID/config Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the `WebApp` [`name`](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example" // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
};
apiInstance.firebaseProjectsWebAppsGetConfig(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the WebApp configuration to download, in the format: projects/PROJECT_IDENTIFIER/webApps/APP_ID/config Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the &#x60;WebApp&#x60; [&#x60;name&#x60;](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 

### Return type

[**WebAppConfig**](WebAppConfig.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsWebAppsList

> ListWebAppsResponse firebaseProjectsWebAppsList(parent, opts)



Lists each WebApp associated with the specified FirebaseProject. The elements are returned in no particular order, but will be a consistent view of the Apps when additional requests are made with a &#x60;pageToken&#x60;.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let parent = "parent_example"; // String | The resource name of the parent FirebaseProject for which to list each associated WebApp, in the format: projects/PROJECT_IDENTIFIER/webApps Refer to the `FirebaseProject` [`name`](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'pageSize': 56, // Number | The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit.
  'pageToken': "pageToken_example", // String | Token returned from a previous call to `ListWebApps` indicating where in the set of Apps to resume listing.
  'showDeleted': true // Boolean | Controls whether Apps in the DELETED state should be returned in the response. If not specified, only `ACTIVE` Apps will be returned.
};
apiInstance.firebaseProjectsWebAppsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| The resource name of the parent FirebaseProject for which to list each associated WebApp, in the format: projects/PROJECT_IDENTIFIER/webApps Refer to the &#x60;FirebaseProject&#x60; [&#x60;name&#x60;](../projects#FirebaseProject.FIELDS.name) field for details about PROJECT_IDENTIFIER values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **pageSize** | **Number**| The maximum number of Apps to return in the response. The server may return fewer than this value at its discretion. If no value is specified (or too large a value is specified), then the server will impose its own limit. | [optional] 
 **pageToken** | **String**| Token returned from a previous call to &#x60;ListWebApps&#x60; indicating where in the set of Apps to resume listing. | [optional] 
 **showDeleted** | **Boolean**| Controls whether Apps in the DELETED state should be returned in the response. If not specified, only &#x60;ACTIVE&#x60; Apps will be returned. | [optional] 

### Return type

[**ListWebAppsResponse**](ListWebAppsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## firebaseProjectsWebAppsPatch

> WebApp firebaseProjectsWebAppsPatch(name, opts)



Updates the attributes of the specified WebApp.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let name = "name_example"; // String | The resource name of the WebApp, in the format: projects/PROJECT_IDENTIFIER /webApps/APP_ID * PROJECT_IDENTIFIER: the parent Project's [`ProjectNumber`](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [`ProjectId`](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google's [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the `ProjectId`. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [`appId`](../projects.webApps#WebApp.FIELDS.app_id)).
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'updateMask': "updateMask_example", // String | Specifies which fields of the WebApp to update. Note that the following fields are immutable: `name`, `app_id`, and `project_id`. To update `state`, use any of the following endpoints: RemoveWebApp or UndeleteWebApp.
  'webApp': new FirebaseManagementApi.WebApp() // WebApp | 
};
apiInstance.firebaseProjectsWebAppsPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| The resource name of the WebApp, in the format: projects/PROJECT_IDENTIFIER /webApps/APP_ID * PROJECT_IDENTIFIER: the parent Project&#39;s [&#x60;ProjectNumber&#x60;](../projects#FirebaseProject.FIELDS.project_number) ***(recommended)*** or its [&#x60;ProjectId&#x60;](../projects#FirebaseProject.FIELDS.project_id). Learn more about using project identifiers in Google&#39;s [AIP 2510 standard](https://google.aip.dev/cloud/2510). Note that the value for PROJECT_IDENTIFIER in any response body will be the &#x60;ProjectId&#x60;. * APP_ID: the globally unique, Firebase-assigned identifier for the App (see [&#x60;appId&#x60;](../projects.webApps#WebApp.FIELDS.app_id)). | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **updateMask** | **String**| Specifies which fields of the WebApp to update. Note that the following fields are immutable: &#x60;name&#x60;, &#x60;app_id&#x60;, and &#x60;project_id&#x60;. To update &#x60;state&#x60;, use any of the following endpoints: RemoveWebApp or UndeleteWebApp. | [optional] 
 **webApp** | [**WebApp**](WebApp.md)|  | [optional] 

### Return type

[**WebApp**](WebApp.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsWebAppsRemove

> Operation firebaseProjectsWebAppsRemove(name, opts)



Removes the specified WebApp from the FirebaseProject.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let name = "name_example"; // String | Required. The resource name of the WebApp, in the format: projects/ PROJECT_IDENTIFIER/webApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the WebApp [name](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'removeWebAppRequest': new FirebaseManagementApi.RemoveWebAppRequest() // RemoveWebAppRequest | 
};
apiInstance.firebaseProjectsWebAppsRemove(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name of the WebApp, in the format: projects/ PROJECT_IDENTIFIER/webApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the WebApp [name](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **removeWebAppRequest** | [**RemoveWebAppRequest**](RemoveWebAppRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## firebaseProjectsWebAppsUndelete

> Operation firebaseProjectsWebAppsUndelete(name, opts)



Restores the specified WebApp to the FirebaseProject.

### Example

```javascript
import FirebaseManagementApi from 'firebase_management_api';
let defaultClient = FirebaseManagementApi.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new FirebaseManagementApi.ProjectsApi();
let name = "name_example"; // String | Required. The resource name of the WebApp, in the format: projects/ PROJECT_IDENTIFIER/webApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the WebApp [name](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values.
let opts = {
  'xgafv': "xgafv_example", // String | V1 error format.
  'accessToken': "accessToken_example", // String | OAuth access token.
  'alt': "alt_example", // String | Data format for response.
  'callback': "callback_example", // String | JSONP
  'fields': "fields_example", // String | Selector specifying which fields to include in a partial response.
  'key': "key_example", // String | API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
  'oauthToken': "oauthToken_example", // String | OAuth 2.0 token for the current user.
  'prettyPrint': true, // Boolean | Returns response with indentations and line breaks.
  'quotaUser': "quotaUser_example", // String | Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
  'uploadProtocol': "uploadProtocol_example", // String | Upload protocol for media (e.g. \"raw\", \"multipart\").
  'uploadType': "uploadType_example", // String | Legacy upload protocol for media (e.g. \"media\", \"multipart\").
  'undeleteWebAppRequest': new FirebaseManagementApi.UndeleteWebAppRequest() // UndeleteWebAppRequest | 
};
apiInstance.firebaseProjectsWebAppsUndelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The resource name of the WebApp, in the format: projects/ PROJECT_IDENTIFIER/webApps/APP_ID Since an APP_ID is a unique identifier, the Unique Resource from Sub-Collection access pattern may be used here, in the format: projects/-/webApps/APP_ID Refer to the WebApp [name](../projects.webApps#WebApp.FIELDS.name) field for details about PROJECT_IDENTIFIER and APP_ID values. | 
 **xgafv** | **String**| V1 error format. | [optional] 
 **accessToken** | **String**| OAuth access token. | [optional] 
 **alt** | **String**| Data format for response. | [optional] 
 **callback** | **String**| JSONP | [optional] 
 **fields** | **String**| Selector specifying which fields to include in a partial response. | [optional] 
 **key** | **String**| API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token. | [optional] 
 **oauthToken** | **String**| OAuth 2.0 token for the current user. | [optional] 
 **prettyPrint** | **Boolean**| Returns response with indentations and line breaks. | [optional] 
 **quotaUser** | **String**| Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters. | [optional] 
 **uploadProtocol** | **String**| Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;). | [optional] 
 **uploadType** | **String**| Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;). | [optional] 
 **undeleteWebAppRequest** | [**UndeleteWebAppRequest**](UndeleteWebAppRequest.md)|  | [optional] 

### Return type

[**Operation**](Operation.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

