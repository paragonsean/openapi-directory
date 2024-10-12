# AppStoreConnectApi.BuildsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**buildsAppEncryptionDeclarationGetToOneRelated**](BuildsApi.md#buildsAppEncryptionDeclarationGetToOneRelated) | **GET** /v1/builds/{id}/appEncryptionDeclaration | 
[**buildsAppEncryptionDeclarationGetToOneRelationship**](BuildsApi.md#buildsAppEncryptionDeclarationGetToOneRelationship) | **GET** /v1/builds/{id}/relationships/appEncryptionDeclaration | 
[**buildsAppEncryptionDeclarationUpdateToOneRelationship**](BuildsApi.md#buildsAppEncryptionDeclarationUpdateToOneRelationship) | **PATCH** /v1/builds/{id}/relationships/appEncryptionDeclaration | 
[**buildsAppGetToOneRelated**](BuildsApi.md#buildsAppGetToOneRelated) | **GET** /v1/builds/{id}/app | 
[**buildsAppStoreVersionGetToOneRelated**](BuildsApi.md#buildsAppStoreVersionGetToOneRelated) | **GET** /v1/builds/{id}/appStoreVersion | 
[**buildsBetaAppReviewSubmissionGetToOneRelated**](BuildsApi.md#buildsBetaAppReviewSubmissionGetToOneRelated) | **GET** /v1/builds/{id}/betaAppReviewSubmission | 
[**buildsBetaBuildLocalizationsGetToManyRelated**](BuildsApi.md#buildsBetaBuildLocalizationsGetToManyRelated) | **GET** /v1/builds/{id}/betaBuildLocalizations | 
[**buildsBetaGroupsCreateToManyRelationship**](BuildsApi.md#buildsBetaGroupsCreateToManyRelationship) | **POST** /v1/builds/{id}/relationships/betaGroups | 
[**buildsBetaGroupsDeleteToManyRelationship**](BuildsApi.md#buildsBetaGroupsDeleteToManyRelationship) | **DELETE** /v1/builds/{id}/relationships/betaGroups | 
[**buildsBuildBetaDetailGetToOneRelated**](BuildsApi.md#buildsBuildBetaDetailGetToOneRelated) | **GET** /v1/builds/{id}/buildBetaDetail | 
[**buildsDiagnosticSignaturesGetToManyRelated**](BuildsApi.md#buildsDiagnosticSignaturesGetToManyRelated) | **GET** /v1/builds/{id}/diagnosticSignatures | 
[**buildsGetCollection**](BuildsApi.md#buildsGetCollection) | **GET** /v1/builds | 
[**buildsGetInstance**](BuildsApi.md#buildsGetInstance) | **GET** /v1/builds/{id} | 
[**buildsIconsGetToManyRelated**](BuildsApi.md#buildsIconsGetToManyRelated) | **GET** /v1/builds/{id}/icons | 
[**buildsIndividualTestersCreateToManyRelationship**](BuildsApi.md#buildsIndividualTestersCreateToManyRelationship) | **POST** /v1/builds/{id}/relationships/individualTesters | 
[**buildsIndividualTestersDeleteToManyRelationship**](BuildsApi.md#buildsIndividualTestersDeleteToManyRelationship) | **DELETE** /v1/builds/{id}/relationships/individualTesters | 
[**buildsIndividualTestersGetToManyRelated**](BuildsApi.md#buildsIndividualTestersGetToManyRelated) | **GET** /v1/builds/{id}/individualTesters | 
[**buildsIndividualTestersGetToManyRelationship**](BuildsApi.md#buildsIndividualTestersGetToManyRelationship) | **GET** /v1/builds/{id}/relationships/individualTesters | 
[**buildsPerfPowerMetricsGetToManyRelated**](BuildsApi.md#buildsPerfPowerMetricsGetToManyRelated) | **GET** /v1/builds/{id}/perfPowerMetrics | 
[**buildsPreReleaseVersionGetToOneRelated**](BuildsApi.md#buildsPreReleaseVersionGetToOneRelated) | **GET** /v1/builds/{id}/preReleaseVersion | 
[**buildsUpdateInstance**](BuildsApi.md#buildsUpdateInstance) | **PATCH** /v1/builds/{id} | 



## buildsAppEncryptionDeclarationGetToOneRelated

> AppEncryptionDeclarationResponse buildsAppEncryptionDeclarationGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppEncryptionDeclarations': ["null"] // [String] | the fields to include for returned resources of type appEncryptionDeclarations
};
apiInstance.buildsAppEncryptionDeclarationGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppEncryptionDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] 

### Return type

[**AppEncryptionDeclarationResponse**](AppEncryptionDeclarationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsAppEncryptionDeclarationGetToOneRelationship

> BuildAppEncryptionDeclarationLinkageResponse buildsAppEncryptionDeclarationGetToOneRelationship(id)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
apiInstance.buildsAppEncryptionDeclarationGetToOneRelationship(id, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 

### Return type

[**BuildAppEncryptionDeclarationLinkageResponse**](BuildAppEncryptionDeclarationLinkageResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsAppEncryptionDeclarationUpdateToOneRelationship

> buildsAppEncryptionDeclarationUpdateToOneRelationship(id, buildAppEncryptionDeclarationLinkageRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let buildAppEncryptionDeclarationLinkageRequest = new AppStoreConnectApi.BuildAppEncryptionDeclarationLinkageRequest(); // BuildAppEncryptionDeclarationLinkageRequest | Related linkage
apiInstance.buildsAppEncryptionDeclarationUpdateToOneRelationship(id, buildAppEncryptionDeclarationLinkageRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **buildAppEncryptionDeclarationLinkageRequest** | [**BuildAppEncryptionDeclarationLinkageRequest**](BuildAppEncryptionDeclarationLinkageRequest.md)| Related linkage | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsAppGetToOneRelated

> AppResponse buildsAppGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsApps': ["null"] // [String] | the fields to include for returned resources of type apps
};
apiInstance.buildsAppGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsAppStoreVersionGetToOneRelated

> AppStoreVersionResponse buildsAppStoreVersionGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppStoreVersions': ["null"] // [String] | the fields to include for returned resources of type appStoreVersions
};
apiInstance.buildsAppStoreVersionGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsAppStoreVersions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] 

### Return type

[**AppStoreVersionResponse**](AppStoreVersionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsBetaAppReviewSubmissionGetToOneRelated

> BetaAppReviewSubmissionResponse buildsBetaAppReviewSubmissionGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaAppReviewSubmissions': ["null"] // [String] | the fields to include for returned resources of type betaAppReviewSubmissions
};
apiInstance.buildsBetaAppReviewSubmissionGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBetaAppReviewSubmissions** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] 

### Return type

[**BetaAppReviewSubmissionResponse**](BetaAppReviewSubmissionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsBetaBuildLocalizationsGetToManyRelated

> BetaBuildLocalizationsResponse buildsBetaBuildLocalizationsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaBuildLocalizations': ["null"], // [String] | the fields to include for returned resources of type betaBuildLocalizations
  'limit': 56 // Number | maximum resources per page
};
apiInstance.buildsBetaBuildLocalizationsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBetaBuildLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaBuildLocalizationsResponse**](BetaBuildLocalizationsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsBetaGroupsCreateToManyRelationship

> buildsBetaGroupsCreateToManyRelationship(id, buildBetaGroupsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let buildBetaGroupsLinkagesRequest = new AppStoreConnectApi.BuildBetaGroupsLinkagesRequest(); // BuildBetaGroupsLinkagesRequest | List of related linkages
apiInstance.buildsBetaGroupsCreateToManyRelationship(id, buildBetaGroupsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **buildBetaGroupsLinkagesRequest** | [**BuildBetaGroupsLinkagesRequest**](BuildBetaGroupsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsBetaGroupsDeleteToManyRelationship

> buildsBetaGroupsDeleteToManyRelationship(id, buildBetaGroupsLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let buildBetaGroupsLinkagesRequest = new AppStoreConnectApi.BuildBetaGroupsLinkagesRequest(); // BuildBetaGroupsLinkagesRequest | List of related linkages
apiInstance.buildsBetaGroupsDeleteToManyRelationship(id, buildBetaGroupsLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **buildBetaGroupsLinkagesRequest** | [**BuildBetaGroupsLinkagesRequest**](BuildBetaGroupsLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsBuildBetaDetailGetToOneRelated

> BuildBetaDetailResponse buildsBuildBetaDetailGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuildBetaDetails': ["null"] // [String] | the fields to include for returned resources of type buildBetaDetails
};
apiInstance.buildsBuildBetaDetailGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBuildBetaDetails** | [**[String]**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] 

### Return type

[**BuildBetaDetailResponse**](BuildBetaDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsDiagnosticSignaturesGetToManyRelated

> DiagnosticSignaturesResponse buildsDiagnosticSignaturesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterDiagnosticType': ["null"], // [String] | filter by attribute 'diagnosticType'
  'fieldsDiagnosticSignatures': ["null"], // [String] | the fields to include for returned resources of type diagnosticSignatures
  'limit': 56 // Number | maximum resources per page
};
apiInstance.buildsDiagnosticSignaturesGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **filterDiagnosticType** | [**[String]**](String.md)| filter by attribute &#39;diagnosticType&#39; | [optional] 
 **fieldsDiagnosticSignatures** | [**[String]**](String.md)| the fields to include for returned resources of type diagnosticSignatures | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**DiagnosticSignaturesResponse**](DiagnosticSignaturesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsGetCollection

> BuildsResponse buildsGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let opts = {
  'filterBetaAppReviewSubmissionBetaReviewState': ["null"], // [String] | filter by attribute 'betaAppReviewSubmission.betaReviewState'
  'filterExpired': ["null"], // [String] | filter by attribute 'expired'
  'filterPreReleaseVersionPlatform': ["null"], // [String] | filter by attribute 'preReleaseVersion.platform'
  'filterPreReleaseVersionVersion': ["null"], // [String] | filter by attribute 'preReleaseVersion.version'
  'filterProcessingState': ["null"], // [String] | filter by attribute 'processingState'
  'filterUsesNonExemptEncryption': ["null"], // [String] | filter by attribute 'usesNonExemptEncryption'
  'filterVersion': ["null"], // [String] | filter by attribute 'version'
  'filterApp': ["null"], // [String] | filter by id(s) of related 'app'
  'filterAppStoreVersion': ["null"], // [String] | filter by id(s) of related 'appStoreVersion'
  'filterBetaGroups': ["null"], // [String] | filter by id(s) of related 'betaGroups'
  'filterPreReleaseVersion': ["null"], // [String] | filter by id(s) of related 'preReleaseVersion'
  'filterId': ["null"], // [String] | filter by id(s)
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsAppEncryptionDeclarations': ["null"], // [String] | the fields to include for returned resources of type appEncryptionDeclarations
  'fieldsBetaAppReviewSubmissions': ["null"], // [String] | the fields to include for returned resources of type betaAppReviewSubmissions
  'fieldsBuildBetaDetails': ["null"], // [String] | the fields to include for returned resources of type buildBetaDetails
  'fieldsBuildIcons': ["null"], // [String] | the fields to include for returned resources of type buildIcons
  'fieldsPerfPowerMetrics': ["null"], // [String] | the fields to include for returned resources of type perfPowerMetrics
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'fieldsAppStoreVersions': ["null"], // [String] | the fields to include for returned resources of type appStoreVersions
  'fieldsDiagnosticSignatures': ["null"], // [String] | the fields to include for returned resources of type diagnosticSignatures
  'fieldsBetaTesters': ["null"], // [String] | the fields to include for returned resources of type betaTesters
  'fieldsBetaBuildLocalizations': ["null"], // [String] | the fields to include for returned resources of type betaBuildLocalizations
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitBetaBuildLocalizations': 56, // Number | maximum number of related betaBuildLocalizations returned (when they are included)
  'limitIcons': 56, // Number | maximum number of related icons returned (when they are included)
  'limitIndividualTesters': 56 // Number | maximum number of related individualTesters returned (when they are included)
};
apiInstance.buildsGetCollection(opts, (error, data, response) => {
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
 **filterBetaAppReviewSubmissionBetaReviewState** | [**[String]**](String.md)| filter by attribute &#39;betaAppReviewSubmission.betaReviewState&#39; | [optional] 
 **filterExpired** | [**[String]**](String.md)| filter by attribute &#39;expired&#39; | [optional] 
 **filterPreReleaseVersionPlatform** | [**[String]**](String.md)| filter by attribute &#39;preReleaseVersion.platform&#39; | [optional] 
 **filterPreReleaseVersionVersion** | [**[String]**](String.md)| filter by attribute &#39;preReleaseVersion.version&#39; | [optional] 
 **filterProcessingState** | [**[String]**](String.md)| filter by attribute &#39;processingState&#39; | [optional] 
 **filterUsesNonExemptEncryption** | [**[String]**](String.md)| filter by attribute &#39;usesNonExemptEncryption&#39; | [optional] 
 **filterVersion** | [**[String]**](String.md)| filter by attribute &#39;version&#39; | [optional] 
 **filterApp** | [**[String]**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] 
 **filterAppStoreVersion** | [**[String]**](String.md)| filter by id(s) of related &#39;appStoreVersion&#39; | [optional] 
 **filterBetaGroups** | [**[String]**](String.md)| filter by id(s) of related &#39;betaGroups&#39; | [optional] 
 **filterPreReleaseVersion** | [**[String]**](String.md)| filter by id(s) of related &#39;preReleaseVersion&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsAppEncryptionDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] 
 **fieldsBetaAppReviewSubmissions** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] 
 **fieldsBuildBetaDetails** | [**[String]**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] 
 **fieldsBuildIcons** | [**[String]**](String.md)| the fields to include for returned resources of type buildIcons | [optional] 
 **fieldsPerfPowerMetrics** | [**[String]**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] 
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 
 **fieldsAppStoreVersions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] 
 **fieldsDiagnosticSignatures** | [**[String]**](String.md)| the fields to include for returned resources of type diagnosticSignatures | [optional] 
 **fieldsBetaTesters** | [**[String]**](String.md)| the fields to include for returned resources of type betaTesters | [optional] 
 **fieldsBetaBuildLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitBetaBuildLocalizations** | **Number**| maximum number of related betaBuildLocalizations returned (when they are included) | [optional] 
 **limitIcons** | **Number**| maximum number of related icons returned (when they are included) | [optional] 
 **limitIndividualTesters** | **Number**| maximum number of related individualTesters returned (when they are included) | [optional] 

### Return type

[**BuildsResponse**](BuildsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsGetInstance

> BuildResponse buildsGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsAppEncryptionDeclarations': ["null"], // [String] | the fields to include for returned resources of type appEncryptionDeclarations
  'fieldsBetaAppReviewSubmissions': ["null"], // [String] | the fields to include for returned resources of type betaAppReviewSubmissions
  'fieldsBuildBetaDetails': ["null"], // [String] | the fields to include for returned resources of type buildBetaDetails
  'fieldsBuildIcons': ["null"], // [String] | the fields to include for returned resources of type buildIcons
  'fieldsPerfPowerMetrics': ["null"], // [String] | the fields to include for returned resources of type perfPowerMetrics
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'fieldsAppStoreVersions': ["null"], // [String] | the fields to include for returned resources of type appStoreVersions
  'fieldsDiagnosticSignatures': ["null"], // [String] | the fields to include for returned resources of type diagnosticSignatures
  'fieldsBetaTesters': ["null"], // [String] | the fields to include for returned resources of type betaTesters
  'fieldsBetaBuildLocalizations': ["null"], // [String] | the fields to include for returned resources of type betaBuildLocalizations
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limitBetaBuildLocalizations': 56, // Number | maximum number of related betaBuildLocalizations returned (when they are included)
  'limitIcons': 56, // Number | maximum number of related icons returned (when they are included)
  'limitIndividualTesters': 56 // Number | maximum number of related individualTesters returned (when they are included)
};
apiInstance.buildsGetInstance(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsAppEncryptionDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] 
 **fieldsBetaAppReviewSubmissions** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] 
 **fieldsBuildBetaDetails** | [**[String]**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] 
 **fieldsBuildIcons** | [**[String]**](String.md)| the fields to include for returned resources of type buildIcons | [optional] 
 **fieldsPerfPowerMetrics** | [**[String]**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] 
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 
 **fieldsAppStoreVersions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] 
 **fieldsDiagnosticSignatures** | [**[String]**](String.md)| the fields to include for returned resources of type diagnosticSignatures | [optional] 
 **fieldsBetaTesters** | [**[String]**](String.md)| the fields to include for returned resources of type betaTesters | [optional] 
 **fieldsBetaBuildLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limitBetaBuildLocalizations** | **Number**| maximum number of related betaBuildLocalizations returned (when they are included) | [optional] 
 **limitIcons** | **Number**| maximum number of related icons returned (when they are included) | [optional] 
 **limitIndividualTesters** | **Number**| maximum number of related individualTesters returned (when they are included) | [optional] 

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsIconsGetToManyRelated

> BuildIconsResponse buildsIconsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuildIcons': ["null"], // [String] | the fields to include for returned resources of type buildIcons
  'limit': 56 // Number | maximum resources per page
};
apiInstance.buildsIconsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBuildIcons** | [**[String]**](String.md)| the fields to include for returned resources of type buildIcons | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BuildIconsResponse**](BuildIconsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsIndividualTestersCreateToManyRelationship

> buildsIndividualTestersCreateToManyRelationship(id, buildIndividualTestersLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let buildIndividualTestersLinkagesRequest = new AppStoreConnectApi.BuildIndividualTestersLinkagesRequest(); // BuildIndividualTestersLinkagesRequest | List of related linkages
apiInstance.buildsIndividualTestersCreateToManyRelationship(id, buildIndividualTestersLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **buildIndividualTestersLinkagesRequest** | [**BuildIndividualTestersLinkagesRequest**](BuildIndividualTestersLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsIndividualTestersDeleteToManyRelationship

> buildsIndividualTestersDeleteToManyRelationship(id, buildIndividualTestersLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let buildIndividualTestersLinkagesRequest = new AppStoreConnectApi.BuildIndividualTestersLinkagesRequest(); // BuildIndividualTestersLinkagesRequest | List of related linkages
apiInstance.buildsIndividualTestersDeleteToManyRelationship(id, buildIndividualTestersLinkagesRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **buildIndividualTestersLinkagesRequest** | [**BuildIndividualTestersLinkagesRequest**](BuildIndividualTestersLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## buildsIndividualTestersGetToManyRelated

> BetaTestersResponse buildsIndividualTestersGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaTesters': ["null"], // [String] | the fields to include for returned resources of type betaTesters
  'limit': 56 // Number | maximum resources per page
};
apiInstance.buildsIndividualTestersGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsBetaTesters** | [**[String]**](String.md)| the fields to include for returned resources of type betaTesters | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaTestersResponse**](BetaTestersResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsIndividualTestersGetToManyRelationship

> BuildIndividualTestersLinkagesResponse buildsIndividualTestersGetToManyRelationship(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'limit': 56 // Number | maximum resources per page
};
apiInstance.buildsIndividualTestersGetToManyRelationship(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BuildIndividualTestersLinkagesResponse**](BuildIndividualTestersLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsPerfPowerMetricsGetToManyRelated

> PerfPowerMetricsResponse buildsPerfPowerMetricsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterDeviceType': ["null"], // [String] | filter by attribute 'deviceType'
  'filterMetricType': ["null"], // [String] | filter by attribute 'metricType'
  'filterPlatform': ["null"] // [String] | filter by attribute 'platform'
};
apiInstance.buildsPerfPowerMetricsGetToManyRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **filterDeviceType** | [**[String]**](String.md)| filter by attribute &#39;deviceType&#39; | [optional] 
 **filterMetricType** | [**[String]**](String.md)| filter by attribute &#39;metricType&#39; | [optional] 
 **filterPlatform** | [**[String]**](String.md)| filter by attribute &#39;platform&#39; | [optional] 

### Return type

[**PerfPowerMetricsResponse**](PerfPowerMetricsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsPreReleaseVersionGetToOneRelated

> PrereleaseVersionResponse buildsPreReleaseVersionGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsPreReleaseVersions': ["null"] // [String] | the fields to include for returned resources of type preReleaseVersions
};
apiInstance.buildsPreReleaseVersionGetToOneRelated(id, opts, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 

### Return type

[**PrereleaseVersionResponse**](PrereleaseVersionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## buildsUpdateInstance

> BuildResponse buildsUpdateInstance(id, buildUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.BuildsApi();
let id = "id_example"; // String | the id of the requested resource
let buildUpdateRequest = new AppStoreConnectApi.BuildUpdateRequest(); // BuildUpdateRequest | Build representation
apiInstance.buildsUpdateInstance(id, buildUpdateRequest, (error, data, response) => {
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
 **id** | **String**| the id of the requested resource | 
 **buildUpdateRequest** | [**BuildUpdateRequest**](BuildUpdateRequest.md)| Build representation | 

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

