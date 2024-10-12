# SensitiveDataProtectionDlp.ProjectsApi

All URIs are relative to *https://dlp.googleapis.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dlpProjectsLocationsColumnDataProfilesList**](ProjectsApi.md#dlpProjectsLocationsColumnDataProfilesList) | **GET** /v2/{parent}/columnDataProfiles | 
[**dlpProjectsLocationsContentDeidentify**](ProjectsApi.md#dlpProjectsLocationsContentDeidentify) | **POST** /v2/{parent}/content:deidentify | 
[**dlpProjectsLocationsContentInspect**](ProjectsApi.md#dlpProjectsLocationsContentInspect) | **POST** /v2/{parent}/content:inspect | 
[**dlpProjectsLocationsContentReidentify**](ProjectsApi.md#dlpProjectsLocationsContentReidentify) | **POST** /v2/{parent}/content:reidentify | 
[**dlpProjectsLocationsDeidentifyTemplatesCreate**](ProjectsApi.md#dlpProjectsLocationsDeidentifyTemplatesCreate) | **POST** /v2/{parent}/deidentifyTemplates | 
[**dlpProjectsLocationsDeidentifyTemplatesList**](ProjectsApi.md#dlpProjectsLocationsDeidentifyTemplatesList) | **GET** /v2/{parent}/deidentifyTemplates | 
[**dlpProjectsLocationsDiscoveryConfigsCreate**](ProjectsApi.md#dlpProjectsLocationsDiscoveryConfigsCreate) | **POST** /v2/{parent}/discoveryConfigs | 
[**dlpProjectsLocationsDiscoveryConfigsList**](ProjectsApi.md#dlpProjectsLocationsDiscoveryConfigsList) | **GET** /v2/{parent}/discoveryConfigs | 
[**dlpProjectsLocationsDlpJobsCancel**](ProjectsApi.md#dlpProjectsLocationsDlpJobsCancel) | **POST** /v2/{name}:cancel | 
[**dlpProjectsLocationsDlpJobsCreate**](ProjectsApi.md#dlpProjectsLocationsDlpJobsCreate) | **POST** /v2/{parent}/dlpJobs | 
[**dlpProjectsLocationsDlpJobsFinish**](ProjectsApi.md#dlpProjectsLocationsDlpJobsFinish) | **POST** /v2/{name}:finish | 
[**dlpProjectsLocationsDlpJobsList**](ProjectsApi.md#dlpProjectsLocationsDlpJobsList) | **GET** /v2/{parent}/dlpJobs | 
[**dlpProjectsLocationsImageRedact**](ProjectsApi.md#dlpProjectsLocationsImageRedact) | **POST** /v2/{parent}/image:redact | 
[**dlpProjectsLocationsInspectTemplatesCreate**](ProjectsApi.md#dlpProjectsLocationsInspectTemplatesCreate) | **POST** /v2/{parent}/inspectTemplates | 
[**dlpProjectsLocationsInspectTemplatesList**](ProjectsApi.md#dlpProjectsLocationsInspectTemplatesList) | **GET** /v2/{parent}/inspectTemplates | 
[**dlpProjectsLocationsJobTriggersActivate**](ProjectsApi.md#dlpProjectsLocationsJobTriggersActivate) | **POST** /v2/{name}:activate | 
[**dlpProjectsLocationsJobTriggersCreate**](ProjectsApi.md#dlpProjectsLocationsJobTriggersCreate) | **POST** /v2/{parent}/jobTriggers | 
[**dlpProjectsLocationsJobTriggersHybridInspect**](ProjectsApi.md#dlpProjectsLocationsJobTriggersHybridInspect) | **POST** /v2/{name}:hybridInspect | 
[**dlpProjectsLocationsJobTriggersList**](ProjectsApi.md#dlpProjectsLocationsJobTriggersList) | **GET** /v2/{parent}/jobTriggers | 
[**dlpProjectsLocationsProjectDataProfilesList**](ProjectsApi.md#dlpProjectsLocationsProjectDataProfilesList) | **GET** /v2/{parent}/projectDataProfiles | 
[**dlpProjectsLocationsTableDataProfilesList**](ProjectsApi.md#dlpProjectsLocationsTableDataProfilesList) | **GET** /v2/{parent}/tableDataProfiles | 
[**dlpProjectsStoredInfoTypesCreate**](ProjectsApi.md#dlpProjectsStoredInfoTypesCreate) | **POST** /v2/{parent}/storedInfoTypes | 
[**dlpProjectsStoredInfoTypesDelete**](ProjectsApi.md#dlpProjectsStoredInfoTypesDelete) | **DELETE** /v2/{name} | 
[**dlpProjectsStoredInfoTypesGet**](ProjectsApi.md#dlpProjectsStoredInfoTypesGet) | **GET** /v2/{name} | 
[**dlpProjectsStoredInfoTypesList**](ProjectsApi.md#dlpProjectsStoredInfoTypesList) | **GET** /v2/{parent}/storedInfoTypes | 
[**dlpProjectsStoredInfoTypesPatch**](ProjectsApi.md#dlpProjectsStoredInfoTypesPatch) | **PATCH** /v2/{name} | 



## dlpProjectsLocationsColumnDataProfilesList

> GooglePrivacyDlpV2ListColumnDataProfilesResponse dlpProjectsLocationsColumnDataProfilesList(parent, opts)



Lists data profiles for an organization.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or projects/project-id/locations/asia.
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
  'filter': "filter_example", // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * Supported fields/values: - `table_data_profile_name` - The name of the related table data profile. - `project_id` - The Google Cloud project ID. (REQUIRED) - `dataset_id` - The BigQuery dataset ID. (REQUIRED) - `table_id` - The BigQuery table ID. (REQUIRED) - `field_id` - The ID of the BigQuery field. - `info_type` - The infotype detected in the resource. - `sensitivity_level` - HIGH|MEDIUM|LOW - `data_risk_level`: How much risk is associated with this data. - `status_code` - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be `=` for project_id, dataset_id, and table_id. Other filters also support `!=`. Examples: * project_id = 12345 AND status_code = 1 * project_id = 12345 AND sensitivity_level = HIGH * project_id = 12345 AND info_type = STREET_ADDRESS The length of this field should be no more than 500 characters.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * `project_id asc` * `table_id` * `sensitivity_level desc` Supported fields are: - `project_id`: The Google Cloud project ID. - `dataset_id`: The ID of a BigQuery dataset. - `table_id`: The ID of a BigQuery table. - `sensitivity_level`: How sensitive the data in a column is, at most. - `data_risk_level`: How much risk is associated with this data. - `profile_last_generated`: When the profile was last updated in epoch seconds.
  'pageSize': 56, // Number | Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval.
};
apiInstance.dlpProjectsLocationsColumnDataProfilesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Resource name of the organization or project, for example &#x60;organizations/433245324/locations/europe&#x60; or projects/project-id/locations/asia. | 
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
 **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values: - &#x60;table_data_profile_name&#x60; - The name of the related table data profile. - &#x60;project_id&#x60; - The Google Cloud project ID. (REQUIRED) - &#x60;dataset_id&#x60; - The BigQuery dataset ID. (REQUIRED) - &#x60;table_id&#x60; - The BigQuery table ID. (REQUIRED) - &#x60;field_id&#x60; - The ID of the BigQuery field. - &#x60;info_type&#x60; - The infotype detected in the resource. - &#x60;sensitivity_level&#x60; - HIGH|MEDIUM|LOW - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;status_code&#x60; - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be &#x60;&#x3D;&#x60; for project_id, dataset_id, and table_id. Other filters also support &#x60;!&#x3D;&#x60;. Examples: * project_id &#x3D; 12345 AND status_code &#x3D; 1 * project_id &#x3D; 12345 AND sensitivity_level &#x3D; HIGH * project_id &#x3D; 12345 AND info_type &#x3D; STREET_ADDRESS The length of this field should be no more than 500 characters. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * &#x60;project_id asc&#x60; * &#x60;table_id&#x60; * &#x60;sensitivity_level desc&#x60; Supported fields are: - &#x60;project_id&#x60;: The Google Cloud project ID. - &#x60;dataset_id&#x60;: The ID of a BigQuery dataset. - &#x60;table_id&#x60;: The ID of a BigQuery table. - &#x60;sensitivity_level&#x60;: How sensitive the data in a column is, at most. - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;profile_last_generated&#x60;: When the profile was last updated in epoch seconds. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListColumnDataProfilesResponse**](GooglePrivacyDlpV2ListColumnDataProfilesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsContentDeidentify

> GooglePrivacyDlpV2DeidentifyContentResponse dlpProjectsLocationsContentDeidentify(parent, opts)



De-identifies potentially sensitive info from a ContentItem. This method has limits on input size and output size. See https://cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data to learn more. When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2DeidentifyContentRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2DeidentifyContentRequest() // GooglePrivacyDlpV2DeidentifyContentRequest | 
};
apiInstance.dlpProjectsLocationsContentDeidentify(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2DeidentifyContentRequest** | [**GooglePrivacyDlpV2DeidentifyContentRequest**](GooglePrivacyDlpV2DeidentifyContentRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2DeidentifyContentResponse**](GooglePrivacyDlpV2DeidentifyContentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsContentInspect

> GooglePrivacyDlpV2InspectContentResponse dlpProjectsLocationsContentInspect(parent, opts)



Finds potentially sensitive info in content. This method has limits on input size, processing time, and output size. When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. For how to guides, see https://cloud.google.com/sensitive-data-protection/docs/inspecting-images and https://cloud.google.com/sensitive-data-protection/docs/inspecting-text,

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2InspectContentRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2InspectContentRequest() // GooglePrivacyDlpV2InspectContentRequest | 
};
apiInstance.dlpProjectsLocationsContentInspect(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2InspectContentRequest** | [**GooglePrivacyDlpV2InspectContentRequest**](GooglePrivacyDlpV2InspectContentRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2InspectContentResponse**](GooglePrivacyDlpV2InspectContentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsContentReidentify

> GooglePrivacyDlpV2ReidentifyContentResponse dlpProjectsLocationsContentReidentify(parent, opts)



Re-identifies content that has been de-identified. See https://cloud.google.com/sensitive-data-protection/docs/pseudonymization#re-identification_in_free_text_code_example to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2ReidentifyContentRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2ReidentifyContentRequest() // GooglePrivacyDlpV2ReidentifyContentRequest | 
};
apiInstance.dlpProjectsLocationsContentReidentify(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2ReidentifyContentRequest** | [**GooglePrivacyDlpV2ReidentifyContentRequest**](GooglePrivacyDlpV2ReidentifyContentRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2ReidentifyContentResponse**](GooglePrivacyDlpV2ReidentifyContentResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsDeidentifyTemplatesCreate

> GooglePrivacyDlpV2DeidentifyTemplate dlpProjectsLocationsDeidentifyTemplatesCreate(parent, opts)



Creates a DeidentifyTemplate for reusing frequently used configuration for de-identifying content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID + Organizations scope, location specified: `organizations/`ORG_ID`/locations/`LOCATION_ID + Organizations scope, no location specified (defaults to global): `organizations/`ORG_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2CreateDeidentifyTemplateRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2CreateDeidentifyTemplateRequest() // GooglePrivacyDlpV2CreateDeidentifyTemplateRequest | 
};
apiInstance.dlpProjectsLocationsDeidentifyTemplatesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2CreateDeidentifyTemplateRequest** | [**GooglePrivacyDlpV2CreateDeidentifyTemplateRequest**](GooglePrivacyDlpV2CreateDeidentifyTemplateRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2DeidentifyTemplate**](GooglePrivacyDlpV2DeidentifyTemplate.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsDeidentifyTemplatesList

> GooglePrivacyDlpV2ListDeidentifyTemplatesResponse dlpProjectsLocationsDeidentifyTemplatesList(parent, opts)



Lists DeidentifyTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates-deid to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID + Organizations scope, location specified: `organizations/`ORG_ID`/locations/`LOCATION_ID + Organizations scope, no location specified (defaults to global): `organizations/`ORG_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'locationId': "locationId_example", // String | Deprecated. This field has no effect.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: `name asc,update_time, create_time desc` Supported fields are: - `create_time`: corresponds to the time the template was created. - `update_time`: corresponds to the time the template was last updated. - `name`: corresponds to the template's name. - `display_name`: corresponds to the template's display name.
  'pageSize': 56, // Number | Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval. Comes from the previous call to `ListDeidentifyTemplates`.
};
apiInstance.dlpProjectsLocationsDeidentifyTemplatesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **locationId** | **String**| Deprecated. This field has no effect. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the template was created. - &#x60;update_time&#x60;: corresponds to the time the template was last updated. - &#x60;name&#x60;: corresponds to the template&#39;s name. - &#x60;display_name&#x60;: corresponds to the template&#39;s display name. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by the server. If zero server returns a page of max size 100. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. Comes from the previous call to &#x60;ListDeidentifyTemplates&#x60;. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListDeidentifyTemplatesResponse**](GooglePrivacyDlpV2ListDeidentifyTemplatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsDiscoveryConfigsCreate

> GooglePrivacyDlpV2DiscoveryConfig dlpProjectsLocationsDiscoveryConfigsCreate(parent, opts)



Creates a config for discovery to scan and profile storage.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value is as follows: `projects/`PROJECT_ID`/locations/`LOCATION_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2CreateDiscoveryConfigRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2CreateDiscoveryConfigRequest() // GooglePrivacyDlpV2CreateDiscoveryConfigRequest | 
};
apiInstance.dlpProjectsLocationsDiscoveryConfigsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value is as follows: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2CreateDiscoveryConfigRequest** | [**GooglePrivacyDlpV2CreateDiscoveryConfigRequest**](GooglePrivacyDlpV2CreateDiscoveryConfigRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2DiscoveryConfig**](GooglePrivacyDlpV2DiscoveryConfig.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsDiscoveryConfigsList

> GooglePrivacyDlpV2ListDiscoveryConfigsResponse dlpProjectsLocationsDiscoveryConfigsList(parent, opts)



Lists discovery configurations.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value is as follows: `projects/`PROJECT_ID`/locations/`LOCATION_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'orderBy': "orderBy_example", // String | Comma separated list of config fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: `name asc,update_time, create_time desc` Supported fields are: - `last_run_time`: corresponds to the last time the DiscoveryConfig ran. - `name`: corresponds to the DiscoveryConfig's name. - `status`: corresponds to DiscoveryConfig's status.
  'pageSize': 56, // Number | Size of the page. This value can be limited by a server.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval. Comes from the previous call to ListDiscoveryConfigs. `order_by` field must not change for subsequent calls.
};
apiInstance.dlpProjectsLocationsDiscoveryConfigsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value is as follows: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **orderBy** | **String**| Comma separated list of config fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;last_run_time&#x60;: corresponds to the last time the DiscoveryConfig ran. - &#x60;name&#x60;: corresponds to the DiscoveryConfig&#39;s name. - &#x60;status&#x60;: corresponds to DiscoveryConfig&#39;s status. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by a server. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. Comes from the previous call to ListDiscoveryConfigs. &#x60;order_by&#x60; field must not change for subsequent calls. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListDiscoveryConfigsResponse**](GooglePrivacyDlpV2ListDiscoveryConfigsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsDlpJobsCancel

> Object dlpProjectsLocationsDlpJobsCancel(name, opts)



Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. The name of the DlpJob resource to be cancelled.
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
  'body': {key: null} // Object | 
};
apiInstance.dlpProjectsLocationsDlpJobsCancel(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the DlpJob resource to be cancelled. | 
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
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsDlpJobsCreate

> GooglePrivacyDlpV2DlpJob dlpProjectsLocationsDlpJobsCreate(parent, opts)



Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2CreateDlpJobRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2CreateDlpJobRequest() // GooglePrivacyDlpV2CreateDlpJobRequest | 
};
apiInstance.dlpProjectsLocationsDlpJobsCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2CreateDlpJobRequest** | [**GooglePrivacyDlpV2CreateDlpJobRequest**](GooglePrivacyDlpV2CreateDlpJobRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2DlpJob**](GooglePrivacyDlpV2DlpJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsDlpJobsFinish

> Object dlpProjectsLocationsDlpJobsFinish(name, opts)



Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. The name of the DlpJob resource to be finished.
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
  'body': {key: null} // Object | 
};
apiInstance.dlpProjectsLocationsDlpJobsFinish(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. The name of the DlpJob resource to be finished. | 
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
 **body** | **Object**|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsDlpJobsList

> GooglePrivacyDlpV2ListDlpJobsResponse dlpProjectsLocationsDlpJobsList(parent, opts)



Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'filter': "filter_example", // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * Supported fields/values for inspect jobs: - `state` - PENDING|RUNNING|CANCELED|FINISHED|FAILED - `inspected_storage` - DATASTORE|CLOUD_STORAGE|BIGQUERY - `trigger_name` - The name of the trigger that created the job. - 'end_time` - Corresponds to the time the job finished. - 'start_time` - Corresponds to the time the job finished. * Supported fields for risk analysis jobs: - `state` - RUNNING|CANCELED|FINISHED|FAILED - 'end_time` - Corresponds to the time the job finished. - 'start_time` - Corresponds to the time the job finished. * The operator must be `=` or `!=`. Examples: * inspected_storage = cloud_storage AND state = done * inspected_storage = cloud_storage OR inspected_storage = bigquery * inspected_storage = cloud_storage AND (state = done OR state = canceled) * end_time > \\\"2017-12-12T00:00:00+00:00\\\" The length of this field should be no more than 500 characters.
  'locationId': "locationId_example", // String | Deprecated. This field has no effect.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: `name asc, end_time asc, create_time desc` Supported fields are: - `create_time`: corresponds to the time the job was created. - `end_time`: corresponds to the time the job ended. - `name`: corresponds to the job's name. - `state`: corresponds to `state`
  'pageSize': 56, // Number | The standard list page size.
  'pageToken': "pageToken_example", // String | The standard list page token.
  'type': "type_example" // String | The type of job. Defaults to `DlpJobType.INSPECT`
};
apiInstance.dlpProjectsLocationsDlpJobsList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values for inspect jobs: - &#x60;state&#x60; - PENDING|RUNNING|CANCELED|FINISHED|FAILED - &#x60;inspected_storage&#x60; - DATASTORE|CLOUD_STORAGE|BIGQUERY - &#x60;trigger_name&#x60; - The name of the trigger that created the job. - &#39;end_time&#x60; - Corresponds to the time the job finished. - &#39;start_time&#x60; - Corresponds to the time the job finished. * Supported fields for risk analysis jobs: - &#x60;state&#x60; - RUNNING|CANCELED|FINISHED|FAILED - &#39;end_time&#x60; - Corresponds to the time the job finished. - &#39;start_time&#x60; - Corresponds to the time the job finished. * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60;. Examples: * inspected_storage &#x3D; cloud_storage AND state &#x3D; done * inspected_storage &#x3D; cloud_storage OR inspected_storage &#x3D; bigquery * inspected_storage &#x3D; cloud_storage AND (state &#x3D; done OR state &#x3D; canceled) * end_time &gt; \\\&quot;2017-12-12T00:00:00+00:00\\\&quot; The length of this field should be no more than 500 characters. | [optional] 
 **locationId** | **String**| Deprecated. This field has no effect. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc, end_time asc, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the job was created. - &#x60;end_time&#x60;: corresponds to the time the job ended. - &#x60;name&#x60;: corresponds to the job&#39;s name. - &#x60;state&#x60;: corresponds to &#x60;state&#x60; | [optional] 
 **pageSize** | **Number**| The standard list page size. | [optional] 
 **pageToken** | **String**| The standard list page token. | [optional] 
 **type** | **String**| The type of job. Defaults to &#x60;DlpJobType.INSPECT&#x60; | [optional] 

### Return type

[**GooglePrivacyDlpV2ListDlpJobsResponse**](GooglePrivacyDlpV2ListDlpJobsResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsImageRedact

> GooglePrivacyDlpV2RedactImageResponse dlpProjectsLocationsImageRedact(parent, opts)



Redacts potentially sensitive info from an image. This method has limits on input size, processing time, and output size. See https://cloud.google.com/sensitive-data-protection/docs/redacting-sensitive-data-images to learn more. When no InfoTypes or CustomInfoTypes are specified in this request, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2RedactImageRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2RedactImageRequest() // GooglePrivacyDlpV2RedactImageRequest | 
};
apiInstance.dlpProjectsLocationsImageRedact(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2RedactImageRequest** | [**GooglePrivacyDlpV2RedactImageRequest**](GooglePrivacyDlpV2RedactImageRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2RedactImageResponse**](GooglePrivacyDlpV2RedactImageResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsInspectTemplatesCreate

> GooglePrivacyDlpV2InspectTemplate dlpProjectsLocationsInspectTemplatesCreate(parent, opts)



Creates an InspectTemplate for reusing frequently used configuration for inspecting content, images, and storage. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID + Organizations scope, location specified: `organizations/`ORG_ID`/locations/`LOCATION_ID + Organizations scope, no location specified (defaults to global): `organizations/`ORG_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2CreateInspectTemplateRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2CreateInspectTemplateRequest() // GooglePrivacyDlpV2CreateInspectTemplateRequest | 
};
apiInstance.dlpProjectsLocationsInspectTemplatesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2CreateInspectTemplateRequest** | [**GooglePrivacyDlpV2CreateInspectTemplateRequest**](GooglePrivacyDlpV2CreateInspectTemplateRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2InspectTemplate**](GooglePrivacyDlpV2InspectTemplate.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsInspectTemplatesList

> GooglePrivacyDlpV2ListInspectTemplatesResponse dlpProjectsLocationsInspectTemplatesList(parent, opts)



Lists InspectTemplates. See https://cloud.google.com/sensitive-data-protection/docs/creating-templates to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID + Organizations scope, location specified: `organizations/`ORG_ID`/locations/`LOCATION_ID + Organizations scope, no location specified (defaults to global): `organizations/`ORG_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'locationId': "locationId_example", // String | Deprecated. This field has no effect.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: `name asc,update_time, create_time desc` Supported fields are: - `create_time`: corresponds to the time the template was created. - `update_time`: corresponds to the time the template was last updated. - `name`: corresponds to the template's name. - `display_name`: corresponds to the template's display name.
  'pageSize': 56, // Number | Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval. Comes from the previous call to `ListInspectTemplates`.
};
apiInstance.dlpProjectsLocationsInspectTemplatesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **locationId** | **String**| Deprecated. This field has no effect. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the template was created. - &#x60;update_time&#x60;: corresponds to the time the template was last updated. - &#x60;name&#x60;: corresponds to the template&#39;s name. - &#x60;display_name&#x60;: corresponds to the template&#39;s display name. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by the server. If zero server returns a page of max size 100. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. Comes from the previous call to &#x60;ListInspectTemplates&#x60;. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListInspectTemplatesResponse**](GooglePrivacyDlpV2ListInspectTemplatesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsJobTriggersActivate

> GooglePrivacyDlpV2DlpJob dlpProjectsLocationsJobTriggersActivate(name, opts)



Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the trigger to activate, for example `projects/dlp-test-project/jobTriggers/53234423`.
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
  'body': {key: null} // Object | 
};
apiInstance.dlpProjectsLocationsJobTriggersActivate(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the trigger to activate, for example &#x60;projects/dlp-test-project/jobTriggers/53234423&#x60;. | 
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
 **body** | **Object**|  | [optional] 

### Return type

[**GooglePrivacyDlpV2DlpJob**](GooglePrivacyDlpV2DlpJob.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsJobTriggersCreate

> GooglePrivacyDlpV2JobTrigger dlpProjectsLocationsJobTriggersCreate(parent, opts)



Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2CreateJobTriggerRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2CreateJobTriggerRequest() // GooglePrivacyDlpV2CreateJobTriggerRequest | 
};
apiInstance.dlpProjectsLocationsJobTriggersCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2CreateJobTriggerRequest** | [**GooglePrivacyDlpV2CreateJobTriggerRequest**](GooglePrivacyDlpV2CreateJobTriggerRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2JobTrigger**](GooglePrivacyDlpV2JobTrigger.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsJobTriggersHybridInspect

> Object dlpProjectsLocationsJobTriggersHybridInspect(name, opts)



Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the trigger to execute a hybrid inspect on, for example `projects/dlp-test-project/jobTriggers/53234423`.
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
  'googlePrivacyDlpV2HybridInspectJobTriggerRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2HybridInspectJobTriggerRequest() // GooglePrivacyDlpV2HybridInspectJobTriggerRequest | 
};
apiInstance.dlpProjectsLocationsJobTriggersHybridInspect(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the trigger to execute a hybrid inspect on, for example &#x60;projects/dlp-test-project/jobTriggers/53234423&#x60;. | 
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
 **googlePrivacyDlpV2HybridInspectJobTriggerRequest** | [**GooglePrivacyDlpV2HybridInspectJobTriggerRequest**](GooglePrivacyDlpV2HybridInspectJobTriggerRequest.md)|  | [optional] 

### Return type

**Object**

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsLocationsJobTriggersList

> GooglePrivacyDlpV2ListJobTriggersResponse dlpProjectsLocationsJobTriggersList(parent, opts)



Lists job triggers. See https://cloud.google.com/sensitive-data-protection/docs/creating-job-triggers to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'filter': "filter_example", // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * Supported fields/values for inspect triggers: - `status` - HEALTHY|PAUSED|CANCELLED - `inspected_storage` - DATASTORE|CLOUD_STORAGE|BIGQUERY - 'last_run_time` - RFC 3339 formatted timestamp, surrounded by quotation marks. Nanoseconds are ignored. - 'error_count' - Number of errors that have occurred while running. * The operator must be `=` or `!=` for status and inspected_storage. Examples: * inspected_storage = cloud_storage AND status = HEALTHY * inspected_storage = cloud_storage OR inspected_storage = bigquery * inspected_storage = cloud_storage AND (state = PAUSED OR state = HEALTHY) * last_run_time > \\\"2017-12-12T00:00:00+00:00\\\" The length of this field should be no more than 500 characters.
  'locationId': "locationId_example", // String | Deprecated. This field has no effect.
  'orderBy': "orderBy_example", // String | Comma separated list of triggeredJob fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: `name asc,update_time, create_time desc` Supported fields are: - `create_time`: corresponds to the time the JobTrigger was created. - `update_time`: corresponds to the time the JobTrigger was last updated. - `last_run_time`: corresponds to the last time the JobTrigger ran. - `name`: corresponds to the JobTrigger's name. - `display_name`: corresponds to the JobTrigger's display name. - `status`: corresponds to JobTrigger's status.
  'pageSize': 56, // Number | Size of the page. This value can be limited by a server.
  'pageToken': "pageToken_example", // String | Page token to continue retrieval. Comes from the previous call to ListJobTriggers. `order_by` field must not change for subsequent calls.
  'type': "type_example" // String | The type of jobs. Will use `DlpJobType.INSPECT` if not set.
};
apiInstance.dlpProjectsLocationsJobTriggersList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values for inspect triggers: - &#x60;status&#x60; - HEALTHY|PAUSED|CANCELLED - &#x60;inspected_storage&#x60; - DATASTORE|CLOUD_STORAGE|BIGQUERY - &#39;last_run_time&#x60; - RFC 3339 formatted timestamp, surrounded by quotation marks. Nanoseconds are ignored. - &#39;error_count&#39; - Number of errors that have occurred while running. * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60; for status and inspected_storage. Examples: * inspected_storage &#x3D; cloud_storage AND status &#x3D; HEALTHY * inspected_storage &#x3D; cloud_storage OR inspected_storage &#x3D; bigquery * inspected_storage &#x3D; cloud_storage AND (state &#x3D; PAUSED OR state &#x3D; HEALTHY) * last_run_time &gt; \\\&quot;2017-12-12T00:00:00+00:00\\\&quot; The length of this field should be no more than 500 characters. | [optional] 
 **locationId** | **String**| Deprecated. This field has no effect. | [optional] 
 **orderBy** | **String**| Comma separated list of triggeredJob fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc,update_time, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the JobTrigger was created. - &#x60;update_time&#x60;: corresponds to the time the JobTrigger was last updated. - &#x60;last_run_time&#x60;: corresponds to the last time the JobTrigger ran. - &#x60;name&#x60;: corresponds to the JobTrigger&#39;s name. - &#x60;display_name&#x60;: corresponds to the JobTrigger&#39;s display name. - &#x60;status&#x60;: corresponds to JobTrigger&#39;s status. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by a server. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. Comes from the previous call to ListJobTriggers. &#x60;order_by&#x60; field must not change for subsequent calls. | [optional] 
 **type** | **String**| The type of jobs. Will use &#x60;DlpJobType.INSPECT&#x60; if not set. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListJobTriggersResponse**](GooglePrivacyDlpV2ListJobTriggersResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsProjectDataProfilesList

> GooglePrivacyDlpV2ListProjectDataProfilesResponse dlpProjectsLocationsProjectDataProfilesList(parent, opts)



Lists data profiles for an organization.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. organizations/{org_id}/locations/{loc_id}
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
  'filter': "filter_example", // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * Supported fields/values: - `sensitivity_level` - HIGH|MODERATE|LOW - `data_risk_level` - HIGH|MODERATE|LOW - `status_code` - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be `=` or `!=`. Examples: * project_id = 12345 AND status_code = 1 * project_id = 12345 AND sensitivity_level = HIGH The length of this field should be no more than 500 characters.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * `project_id` * `sensitivity_level desc` Supported fields are: - `project_id`: GCP project ID - `sensitivity_level`: How sensitive the data in a project is, at most. - `data_risk_level`: How much risk is associated with this data. - `profile_last_generated`: When the profile was last updated in epoch seconds.
  'pageSize': 56, // Number | Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval.
};
apiInstance.dlpProjectsLocationsProjectDataProfilesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. organizations/{org_id}/locations/{loc_id} | 
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
 **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values: - &#x60;sensitivity_level&#x60; - HIGH|MODERATE|LOW - &#x60;data_risk_level&#x60; - HIGH|MODERATE|LOW - &#x60;status_code&#x60; - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60;. Examples: * project_id &#x3D; 12345 AND status_code &#x3D; 1 * project_id &#x3D; 12345 AND sensitivity_level &#x3D; HIGH The length of this field should be no more than 500 characters. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * &#x60;project_id&#x60; * &#x60;sensitivity_level desc&#x60; Supported fields are: - &#x60;project_id&#x60;: GCP project ID - &#x60;sensitivity_level&#x60;: How sensitive the data in a project is, at most. - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;profile_last_generated&#x60;: When the profile was last updated in epoch seconds. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListProjectDataProfilesResponse**](GooglePrivacyDlpV2ListProjectDataProfilesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsLocationsTableDataProfilesList

> GooglePrivacyDlpV2ListTableDataProfilesResponse dlpProjectsLocationsTableDataProfilesList(parent, opts)



Lists data profiles for an organization.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Resource name of the organization or project, for example `organizations/433245324/locations/europe` or `projects/project-id/locations/asia`.
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
  'filter': "filter_example", // String | Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by `AND` or `OR` logical operators. A sequence of restrictions implicitly uses `AND`. * A restriction has the form of `{field} {operator} {value}`. * Supported fields/values: - `project_id` - The GCP project ID. - `dataset_id` - The BigQuery dataset ID. - `table_id` - The ID of the BigQuery table. - `sensitivity_level` - HIGH|MODERATE|LOW - `data_risk_level` - HIGH|MODERATE|LOW - `resource_visibility`: PUBLIC|RESTRICTED - `status_code` - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be `=` or `!=`. Examples: * project_id = 12345 AND status_code = 1 * project_id = 12345 AND sensitivity_level = HIGH * project_id = 12345 AND resource_visibility = PUBLIC The length of this field should be no more than 500 characters.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * `project_id asc` * `table_id` * `sensitivity_level desc` Supported fields are: - `project_id`: The GCP project ID. - `dataset_id`: The ID of a BigQuery dataset. - `table_id`: The ID of a BigQuery table. - `sensitivity_level`: How sensitive the data in a table is, at most. - `data_risk_level`: How much risk is associated with this data. - `profile_last_generated`: When the profile was last updated in epoch seconds. - `last_modified`: The last time the resource was modified. - `resource_visibility`: Visibility restriction for this resource. - `row_count`: Number of rows in this resource.
  'pageSize': 56, // Number | Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval.
};
apiInstance.dlpProjectsLocationsTableDataProfilesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Resource name of the organization or project, for example &#x60;organizations/433245324/locations/europe&#x60; or &#x60;projects/project-id/locations/asia&#x60;. | 
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
 **filter** | **String**| Allows filtering. Supported syntax: * Filter expressions are made up of one or more restrictions. * Restrictions can be combined by &#x60;AND&#x60; or &#x60;OR&#x60; logical operators. A sequence of restrictions implicitly uses &#x60;AND&#x60;. * A restriction has the form of &#x60;{field} {operator} {value}&#x60;. * Supported fields/values: - &#x60;project_id&#x60; - The GCP project ID. - &#x60;dataset_id&#x60; - The BigQuery dataset ID. - &#x60;table_id&#x60; - The ID of the BigQuery table. - &#x60;sensitivity_level&#x60; - HIGH|MODERATE|LOW - &#x60;data_risk_level&#x60; - HIGH|MODERATE|LOW - &#x60;resource_visibility&#x60;: PUBLIC|RESTRICTED - &#x60;status_code&#x60; - an RPC status code as defined in https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto * The operator must be &#x60;&#x3D;&#x60; or &#x60;!&#x3D;&#x60;. Examples: * project_id &#x3D; 12345 AND status_code &#x3D; 1 * project_id &#x3D; 12345 AND sensitivity_level &#x3D; HIGH * project_id &#x3D; 12345 AND resource_visibility &#x3D; PUBLIC The length of this field should be no more than 500 characters. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Only one order field at a time is allowed. Examples: * &#x60;project_id asc&#x60; * &#x60;table_id&#x60; * &#x60;sensitivity_level desc&#x60; Supported fields are: - &#x60;project_id&#x60;: The GCP project ID. - &#x60;dataset_id&#x60;: The ID of a BigQuery dataset. - &#x60;table_id&#x60;: The ID of a BigQuery table. - &#x60;sensitivity_level&#x60;: How sensitive the data in a table is, at most. - &#x60;data_risk_level&#x60;: How much risk is associated with this data. - &#x60;profile_last_generated&#x60;: When the profile was last updated in epoch seconds. - &#x60;last_modified&#x60;: The last time the resource was modified. - &#x60;resource_visibility&#x60;: Visibility restriction for this resource. - &#x60;row_count&#x60;: Number of rows in this resource. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by the server. If zero, server returns a page of max size 100. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListTableDataProfilesResponse**](GooglePrivacyDlpV2ListTableDataProfilesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsStoredInfoTypesCreate

> GooglePrivacyDlpV2StoredInfoType dlpProjectsStoredInfoTypesCreate(parent, opts)



Creates a pre-built stored infoType to be used for inspection. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID + Organizations scope, location specified: `organizations/`ORG_ID`/locations/`LOCATION_ID + Organizations scope, no location specified (defaults to global): `organizations/`ORG_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'googlePrivacyDlpV2CreateStoredInfoTypeRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2CreateStoredInfoTypeRequest() // GooglePrivacyDlpV2CreateStoredInfoTypeRequest | 
};
apiInstance.dlpProjectsStoredInfoTypesCreate(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID + Organizations scope, location specified: &#x60;organizations/&#x60;ORG_ID&#x60;/locations/&#x60;LOCATION_ID + Organizations scope, no location specified (defaults to global): &#x60;organizations/&#x60;ORG_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **googlePrivacyDlpV2CreateStoredInfoTypeRequest** | [**GooglePrivacyDlpV2CreateStoredInfoTypeRequest**](GooglePrivacyDlpV2CreateStoredInfoTypeRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2StoredInfoType**](GooglePrivacyDlpV2StoredInfoType.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## dlpProjectsStoredInfoTypesDelete

> Object dlpProjectsStoredInfoTypesDelete(name, opts)



Deletes a stored infoType. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the organization and storedInfoType to be deleted, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342.
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
apiInstance.dlpProjectsStoredInfoTypesDelete(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the organization and storedInfoType to be deleted, for example &#x60;organizations/433245324/storedInfoTypes/432452342&#x60; or projects/project-id/storedInfoTypes/432452342. | 
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


## dlpProjectsStoredInfoTypesGet

> GooglePrivacyDlpV2StoredInfoType dlpProjectsStoredInfoTypesGet(name, opts)



Gets a stored infoType. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of the organization and storedInfoType to be read, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342.
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
apiInstance.dlpProjectsStoredInfoTypesGet(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of the organization and storedInfoType to be read, for example &#x60;organizations/433245324/storedInfoTypes/432452342&#x60; or projects/project-id/storedInfoTypes/432452342. | 
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

[**GooglePrivacyDlpV2StoredInfoType**](GooglePrivacyDlpV2StoredInfoType.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsStoredInfoTypesList

> GooglePrivacyDlpV2ListStoredInfoTypesResponse dlpProjectsStoredInfoTypesList(parent, opts)



Lists stored infoTypes. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let parent = "parent_example"; // String | Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: `projects/`PROJECT_ID`/locations/`LOCATION_ID + Projects scope, no location specified (defaults to global): `projects/`PROJECT_ID The following example `parent` string specifies a parent project with the identifier `example-project`, and specifies the `europe-west3` location for processing data: parent=projects/example-project/locations/europe-west3
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
  'locationId': "locationId_example", // String | Deprecated. This field has no effect.
  'orderBy': "orderBy_example", // String | Comma separated list of fields to order by, followed by `asc` or `desc` postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: `name asc, display_name, create_time desc` Supported fields are: - `create_time`: corresponds to the time the most recent version of the resource was created. - `state`: corresponds to the state of the resource. - `name`: corresponds to resource name. - `display_name`: corresponds to info type's display name.
  'pageSize': 56, // Number | Size of the page. This value can be limited by the server. If zero server returns a page of max size 100.
  'pageToken': "pageToken_example" // String | Page token to continue retrieval. Comes from the previous call to `ListStoredInfoTypes`.
};
apiInstance.dlpProjectsStoredInfoTypesList(parent, opts, (error, data, response) => {
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
 **parent** | **String**| Required. Parent resource name. The format of this value varies depending on the scope of the request (project or organization) and whether you have [specified a processing location](https://cloud.google.com/sensitive-data-protection/docs/specifying-location): + Projects scope, location specified: &#x60;projects/&#x60;PROJECT_ID&#x60;/locations/&#x60;LOCATION_ID + Projects scope, no location specified (defaults to global): &#x60;projects/&#x60;PROJECT_ID The following example &#x60;parent&#x60; string specifies a parent project with the identifier &#x60;example-project&#x60;, and specifies the &#x60;europe-west3&#x60; location for processing data: parent&#x3D;projects/example-project/locations/europe-west3 | 
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
 **locationId** | **String**| Deprecated. This field has no effect. | [optional] 
 **orderBy** | **String**| Comma separated list of fields to order by, followed by &#x60;asc&#x60; or &#x60;desc&#x60; postfix. This list is case insensitive. The default sorting order is ascending. Redundant space characters are insignificant. Example: &#x60;name asc, display_name, create_time desc&#x60; Supported fields are: - &#x60;create_time&#x60;: corresponds to the time the most recent version of the resource was created. - &#x60;state&#x60;: corresponds to the state of the resource. - &#x60;name&#x60;: corresponds to resource name. - &#x60;display_name&#x60;: corresponds to info type&#39;s display name. | [optional] 
 **pageSize** | **Number**| Size of the page. This value can be limited by the server. If zero server returns a page of max size 100. | [optional] 
 **pageToken** | **String**| Page token to continue retrieval. Comes from the previous call to &#x60;ListStoredInfoTypes&#x60;. | [optional] 

### Return type

[**GooglePrivacyDlpV2ListStoredInfoTypesResponse**](GooglePrivacyDlpV2ListStoredInfoTypesResponse.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## dlpProjectsStoredInfoTypesPatch

> GooglePrivacyDlpV2StoredInfoType dlpProjectsStoredInfoTypesPatch(name, opts)



Updates the stored infoType by creating a new version. The existing version will continue to be used until the new version is ready. See https://cloud.google.com/sensitive-data-protection/docs/creating-stored-infotypes to learn more.

### Example

```javascript
import SensitiveDataProtectionDlp from 'sensitive_data_protection__dlp';
let defaultClient = SensitiveDataProtectionDlp.ApiClient.instance;
// Configure OAuth2 access token for authorization: Oauth2c
let Oauth2c = defaultClient.authentications['Oauth2c'];
Oauth2c.accessToken = 'YOUR ACCESS TOKEN';
// Configure OAuth2 access token for authorization: Oauth2
let Oauth2 = defaultClient.authentications['Oauth2'];
Oauth2.accessToken = 'YOUR ACCESS TOKEN';

let apiInstance = new SensitiveDataProtectionDlp.ProjectsApi();
let name = "name_example"; // String | Required. Resource name of organization and storedInfoType to be updated, for example `organizations/433245324/storedInfoTypes/432452342` or projects/project-id/storedInfoTypes/432452342.
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
  'googlePrivacyDlpV2UpdateStoredInfoTypeRequest': new SensitiveDataProtectionDlp.GooglePrivacyDlpV2UpdateStoredInfoTypeRequest() // GooglePrivacyDlpV2UpdateStoredInfoTypeRequest | 
};
apiInstance.dlpProjectsStoredInfoTypesPatch(name, opts, (error, data, response) => {
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
 **name** | **String**| Required. Resource name of organization and storedInfoType to be updated, for example &#x60;organizations/433245324/storedInfoTypes/432452342&#x60; or projects/project-id/storedInfoTypes/432452342. | 
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
 **googlePrivacyDlpV2UpdateStoredInfoTypeRequest** | [**GooglePrivacyDlpV2UpdateStoredInfoTypeRequest**](GooglePrivacyDlpV2UpdateStoredInfoTypeRequest.md)|  | [optional] 

### Return type

[**GooglePrivacyDlpV2StoredInfoType**](GooglePrivacyDlpV2StoredInfoType.md)

### Authorization

[Oauth2c](../README.md#Oauth2c), [Oauth2](../README.md#Oauth2)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

