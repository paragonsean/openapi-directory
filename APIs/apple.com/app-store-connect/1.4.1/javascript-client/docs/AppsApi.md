# AppStoreConnectApi.AppsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**appsAppInfosGetToManyRelated**](AppsApi.md#appsAppInfosGetToManyRelated) | **GET** /v1/apps/{id}/appInfos | 
[**appsAppStoreVersionsGetToManyRelated**](AppsApi.md#appsAppStoreVersionsGetToManyRelated) | **GET** /v1/apps/{id}/appStoreVersions | 
[**appsAvailableTerritoriesGetToManyRelated**](AppsApi.md#appsAvailableTerritoriesGetToManyRelated) | **GET** /v1/apps/{id}/availableTerritories | 
[**appsBetaAppLocalizationsGetToManyRelated**](AppsApi.md#appsBetaAppLocalizationsGetToManyRelated) | **GET** /v1/apps/{id}/betaAppLocalizations | 
[**appsBetaAppReviewDetailGetToOneRelated**](AppsApi.md#appsBetaAppReviewDetailGetToOneRelated) | **GET** /v1/apps/{id}/betaAppReviewDetail | 
[**appsBetaGroupsGetToManyRelated**](AppsApi.md#appsBetaGroupsGetToManyRelated) | **GET** /v1/apps/{id}/betaGroups | 
[**appsBetaLicenseAgreementGetToOneRelated**](AppsApi.md#appsBetaLicenseAgreementGetToOneRelated) | **GET** /v1/apps/{id}/betaLicenseAgreement | 
[**appsBetaTestersDeleteToManyRelationship**](AppsApi.md#appsBetaTestersDeleteToManyRelationship) | **DELETE** /v1/apps/{id}/relationships/betaTesters | 
[**appsBuildsGetToManyRelated**](AppsApi.md#appsBuildsGetToManyRelated) | **GET** /v1/apps/{id}/builds | 
[**appsEndUserLicenseAgreementGetToOneRelated**](AppsApi.md#appsEndUserLicenseAgreementGetToOneRelated) | **GET** /v1/apps/{id}/endUserLicenseAgreement | 
[**appsGameCenterEnabledVersionsGetToManyRelated**](AppsApi.md#appsGameCenterEnabledVersionsGetToManyRelated) | **GET** /v1/apps/{id}/gameCenterEnabledVersions | 
[**appsGetCollection**](AppsApi.md#appsGetCollection) | **GET** /v1/apps | 
[**appsGetInstance**](AppsApi.md#appsGetInstance) | **GET** /v1/apps/{id} | 
[**appsInAppPurchasesGetToManyRelated**](AppsApi.md#appsInAppPurchasesGetToManyRelated) | **GET** /v1/apps/{id}/inAppPurchases | 
[**appsPerfPowerMetricsGetToManyRelated**](AppsApi.md#appsPerfPowerMetricsGetToManyRelated) | **GET** /v1/apps/{id}/perfPowerMetrics | 
[**appsPreOrderGetToOneRelated**](AppsApi.md#appsPreOrderGetToOneRelated) | **GET** /v1/apps/{id}/preOrder | 
[**appsPreReleaseVersionsGetToManyRelated**](AppsApi.md#appsPreReleaseVersionsGetToManyRelated) | **GET** /v1/apps/{id}/preReleaseVersions | 
[**appsPricesGetToManyRelated**](AppsApi.md#appsPricesGetToManyRelated) | **GET** /v1/apps/{id}/prices | 
[**appsUpdateInstance**](AppsApi.md#appsUpdateInstance) | **PATCH** /v1/apps/{id} | 



## appsAppInfosGetToManyRelated

> AppInfosResponse appsAppInfosGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAgeRatingDeclarations': ["null"], // [String] | the fields to include for returned resources of type ageRatingDeclarations
  'fieldsAppInfos': ["null"], // [String] | the fields to include for returned resources of type appInfos
  'fieldsAppCategories': ["null"], // [String] | the fields to include for returned resources of type appCategories
  'fieldsAppInfoLocalizations': ["null"], // [String] | the fields to include for returned resources of type appInfoLocalizations
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56, // Number | maximum resources per page
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appsAppInfosGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsAgeRatingDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] 
 **fieldsAppInfos** | [**[String]**](String.md)| the fields to include for returned resources of type appInfos | [optional] 
 **fieldsAppCategories** | [**[String]**](String.md)| the fields to include for returned resources of type appCategories | [optional] 
 **fieldsAppInfoLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**AppInfosResponse**](AppInfosResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAppStoreVersionsGetToManyRelated

> AppStoreVersionsResponse appsAppStoreVersionsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterAppStoreState': ["null"], // [String] | filter by attribute 'appStoreState'
  'filterPlatform': ["null"], // [String] | filter by attribute 'platform'
  'filterVersionString': ["null"], // [String] | filter by attribute 'versionString'
  'filterId': ["null"], // [String] | filter by id(s)
  'fieldsIdfaDeclarations': ["null"], // [String] | the fields to include for returned resources of type idfaDeclarations
  'fieldsAppStoreVersionLocalizations': ["null"], // [String] | the fields to include for returned resources of type appStoreVersionLocalizations
  'fieldsRoutingAppCoverages': ["null"], // [String] | the fields to include for returned resources of type routingAppCoverages
  'fieldsAppStoreVersionPhasedReleases': ["null"], // [String] | the fields to include for returned resources of type appStoreVersionPhasedReleases
  'fieldsAgeRatingDeclarations': ["null"], // [String] | the fields to include for returned resources of type ageRatingDeclarations
  'fieldsAppStoreReviewDetails': ["null"], // [String] | the fields to include for returned resources of type appStoreReviewDetails
  'fieldsAppStoreVersions': ["null"], // [String] | the fields to include for returned resources of type appStoreVersions
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsAppStoreVersionSubmissions': ["null"], // [String] | the fields to include for returned resources of type appStoreVersionSubmissions
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56, // Number | maximum resources per page
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appsAppStoreVersionsGetToManyRelated(id, opts, (error, data, response) => {
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
 **filterAppStoreState** | [**[String]**](String.md)| filter by attribute &#39;appStoreState&#39; | [optional] 
 **filterPlatform** | [**[String]**](String.md)| filter by attribute &#39;platform&#39; | [optional] 
 **filterVersionString** | [**[String]**](String.md)| filter by attribute &#39;versionString&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **fieldsIdfaDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type idfaDeclarations | [optional] 
 **fieldsAppStoreVersionLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] 
 **fieldsRoutingAppCoverages** | [**[String]**](String.md)| the fields to include for returned resources of type routingAppCoverages | [optional] 
 **fieldsAppStoreVersionPhasedReleases** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersionPhasedReleases | [optional] 
 **fieldsAgeRatingDeclarations** | [**[String]**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] 
 **fieldsAppStoreReviewDetails** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreReviewDetails | [optional] 
 **fieldsAppStoreVersions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsAppStoreVersionSubmissions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersionSubmissions | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**AppStoreVersionsResponse**](AppStoreVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsAvailableTerritoriesGetToManyRelated

> TerritoriesResponse appsAvailableTerritoriesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsTerritories': ["null"], // [String] | the fields to include for returned resources of type territories
  'limit': 56 // Number | maximum resources per page
};
apiInstance.appsAvailableTerritoriesGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsTerritories** | [**[String]**](String.md)| the fields to include for returned resources of type territories | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**TerritoriesResponse**](TerritoriesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsBetaAppLocalizationsGetToManyRelated

> BetaAppLocalizationsResponse appsBetaAppLocalizationsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaAppLocalizations': ["null"], // [String] | the fields to include for returned resources of type betaAppLocalizations
  'limit': 56 // Number | maximum resources per page
};
apiInstance.appsBetaAppLocalizationsGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsBetaAppLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaAppLocalizationsResponse**](BetaAppLocalizationsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsBetaAppReviewDetailGetToOneRelated

> BetaAppReviewDetailResponse appsBetaAppReviewDetailGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaAppReviewDetails': ["null"] // [String] | the fields to include for returned resources of type betaAppReviewDetails
};
apiInstance.appsBetaAppReviewDetailGetToOneRelated(id, opts, (error, data, response) => {
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
 **fieldsBetaAppReviewDetails** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppReviewDetails | [optional] 

### Return type

[**BetaAppReviewDetailResponse**](BetaAppReviewDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsBetaGroupsGetToManyRelated

> BetaGroupsResponse appsBetaGroupsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaGroups': ["null"], // [String] | the fields to include for returned resources of type betaGroups
  'limit': 56 // Number | maximum resources per page
};
apiInstance.appsBetaGroupsGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsBetaGroups** | [**[String]**](String.md)| the fields to include for returned resources of type betaGroups | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BetaGroupsResponse**](BetaGroupsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsBetaLicenseAgreementGetToOneRelated

> BetaLicenseAgreementResponse appsBetaLicenseAgreementGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBetaLicenseAgreements': ["null"] // [String] | the fields to include for returned resources of type betaLicenseAgreements
};
apiInstance.appsBetaLicenseAgreementGetToOneRelated(id, opts, (error, data, response) => {
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
 **fieldsBetaLicenseAgreements** | [**[String]**](String.md)| the fields to include for returned resources of type betaLicenseAgreements | [optional] 

### Return type

[**BetaLicenseAgreementResponse**](BetaLicenseAgreementResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsBetaTestersDeleteToManyRelationship

> appsBetaTestersDeleteToManyRelationship(id, appBetaTestersLinkagesRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let appBetaTestersLinkagesRequest = new AppStoreConnectApi.AppBetaTestersLinkagesRequest(); // AppBetaTestersLinkagesRequest | List of related linkages
apiInstance.appsBetaTestersDeleteToManyRelationship(id, appBetaTestersLinkagesRequest, (error, data, response) => {
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
 **appBetaTestersLinkagesRequest** | [**AppBetaTestersLinkagesRequest**](AppBetaTestersLinkagesRequest.md)| List of related linkages | 

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## appsBuildsGetToManyRelated

> BuildsResponse appsBuildsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'limit': 56 // Number | maximum resources per page
};
apiInstance.appsBuildsGetToManyRelated(id, opts, (error, data, response) => {
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
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**BuildsResponse**](BuildsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsEndUserLicenseAgreementGetToOneRelated

> EndUserLicenseAgreementResponse appsEndUserLicenseAgreementGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsEndUserLicenseAgreements': ["null"] // [String] | the fields to include for returned resources of type endUserLicenseAgreements
};
apiInstance.appsEndUserLicenseAgreementGetToOneRelated(id, opts, (error, data, response) => {
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
 **fieldsEndUserLicenseAgreements** | [**[String]**](String.md)| the fields to include for returned resources of type endUserLicenseAgreements | [optional] 

### Return type

[**EndUserLicenseAgreementResponse**](EndUserLicenseAgreementResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGameCenterEnabledVersionsGetToManyRelated

> GameCenterEnabledVersionsResponse appsGameCenterEnabledVersionsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterPlatform': ["null"], // [String] | filter by attribute 'platform'
  'filterVersionString': ["null"], // [String] | filter by attribute 'versionString'
  'filterId': ["null"], // [String] | filter by id(s)
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsGameCenterEnabledVersions': ["null"], // [String] | the fields to include for returned resources of type gameCenterEnabledVersions
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56, // Number | maximum resources per page
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appsGameCenterEnabledVersionsGetToManyRelated(id, opts, (error, data, response) => {
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
 **filterPlatform** | [**[String]**](String.md)| filter by attribute &#39;platform&#39; | [optional] 
 **filterVersionString** | [**[String]**](String.md)| filter by attribute &#39;versionString&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsGameCenterEnabledVersions** | [**[String]**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**GameCenterEnabledVersionsResponse**](GameCenterEnabledVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetCollection

> AppsResponse appsGetCollection(opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let opts = {
  'filterAppStoreVersionsAppStoreState': ["null"], // [String] | filter by attribute 'appStoreVersions.appStoreState'
  'filterAppStoreVersionsPlatform': ["null"], // [String] | filter by attribute 'appStoreVersions.platform'
  'filterBundleId': ["null"], // [String] | filter by attribute 'bundleId'
  'filterName': ["null"], // [String] | filter by attribute 'name'
  'filterSku': ["null"], // [String] | filter by attribute 'sku'
  'filterAppStoreVersions': ["null"], // [String] | filter by id(s) of related 'appStoreVersions'
  'filterId': ["null"], // [String] | filter by id(s)
  'existsGameCenterEnabledVersions': ["null"], // [String] | filter by existence or non-existence of related 'gameCenterEnabledVersions'
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56, // Number | maximum resources per page
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBetaGroups': ["null"], // [String] | the fields to include for returned resources of type betaGroups
  'fieldsPerfPowerMetrics': ["null"], // [String] | the fields to include for returned resources of type perfPowerMetrics
  'fieldsAppInfos': ["null"], // [String] | the fields to include for returned resources of type appInfos
  'fieldsAppPreOrders': ["null"], // [String] | the fields to include for returned resources of type appPreOrders
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'fieldsAppPrices': ["null"], // [String] | the fields to include for returned resources of type appPrices
  'fieldsInAppPurchases': ["null"], // [String] | the fields to include for returned resources of type inAppPurchases
  'fieldsBetaAppReviewDetails': ["null"], // [String] | the fields to include for returned resources of type betaAppReviewDetails
  'fieldsTerritories': ["null"], // [String] | the fields to include for returned resources of type territories
  'fieldsGameCenterEnabledVersions': ["null"], // [String] | the fields to include for returned resources of type gameCenterEnabledVersions
  'fieldsAppStoreVersions': ["null"], // [String] | the fields to include for returned resources of type appStoreVersions
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsBetaAppLocalizations': ["null"], // [String] | the fields to include for returned resources of type betaAppLocalizations
  'fieldsBetaLicenseAgreements': ["null"], // [String] | the fields to include for returned resources of type betaLicenseAgreements
  'fieldsEndUserLicenseAgreements': ["null"], // [String] | the fields to include for returned resources of type endUserLicenseAgreements
  'limitAppInfos': 56, // Number | maximum number of related appInfos returned (when they are included)
  'limitAppStoreVersions': 56, // Number | maximum number of related appStoreVersions returned (when they are included)
  'limitAvailableTerritories': 56, // Number | maximum number of related availableTerritories returned (when they are included)
  'limitBetaAppLocalizations': 56, // Number | maximum number of related betaAppLocalizations returned (when they are included)
  'limitBetaGroups': 56, // Number | maximum number of related betaGroups returned (when they are included)
  'limitBuilds': 56, // Number | maximum number of related builds returned (when they are included)
  'limitGameCenterEnabledVersions': 56, // Number | maximum number of related gameCenterEnabledVersions returned (when they are included)
  'limitInAppPurchases': 56, // Number | maximum number of related inAppPurchases returned (when they are included)
  'limitPreReleaseVersions': 56, // Number | maximum number of related preReleaseVersions returned (when they are included)
  'limitPrices': 56 // Number | maximum number of related prices returned (when they are included)
};
apiInstance.appsGetCollection(opts, (error, data, response) => {
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
 **filterAppStoreVersionsAppStoreState** | [**[String]**](String.md)| filter by attribute &#39;appStoreVersions.appStoreState&#39; | [optional] 
 **filterAppStoreVersionsPlatform** | [**[String]**](String.md)| filter by attribute &#39;appStoreVersions.platform&#39; | [optional] 
 **filterBundleId** | [**[String]**](String.md)| filter by attribute &#39;bundleId&#39; | [optional] 
 **filterName** | [**[String]**](String.md)| filter by attribute &#39;name&#39; | [optional] 
 **filterSku** | [**[String]**](String.md)| filter by attribute &#39;sku&#39; | [optional] 
 **filterAppStoreVersions** | [**[String]**](String.md)| filter by id(s) of related &#39;appStoreVersions&#39; | [optional] 
 **filterId** | [**[String]**](String.md)| filter by id(s) | [optional] 
 **existsGameCenterEnabledVersions** | [**[String]**](String.md)| filter by existence or non-existence of related &#39;gameCenterEnabledVersions&#39; | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBetaGroups** | [**[String]**](String.md)| the fields to include for returned resources of type betaGroups | [optional] 
 **fieldsPerfPowerMetrics** | [**[String]**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] 
 **fieldsAppInfos** | [**[String]**](String.md)| the fields to include for returned resources of type appInfos | [optional] 
 **fieldsAppPreOrders** | [**[String]**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] 
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 
 **fieldsAppPrices** | [**[String]**](String.md)| the fields to include for returned resources of type appPrices | [optional] 
 **fieldsInAppPurchases** | [**[String]**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] 
 **fieldsBetaAppReviewDetails** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppReviewDetails | [optional] 
 **fieldsTerritories** | [**[String]**](String.md)| the fields to include for returned resources of type territories | [optional] 
 **fieldsGameCenterEnabledVersions** | [**[String]**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] 
 **fieldsAppStoreVersions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsBetaAppLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] 
 **fieldsBetaLicenseAgreements** | [**[String]**](String.md)| the fields to include for returned resources of type betaLicenseAgreements | [optional] 
 **fieldsEndUserLicenseAgreements** | [**[String]**](String.md)| the fields to include for returned resources of type endUserLicenseAgreements | [optional] 
 **limitAppInfos** | **Number**| maximum number of related appInfos returned (when they are included) | [optional] 
 **limitAppStoreVersions** | **Number**| maximum number of related appStoreVersions returned (when they are included) | [optional] 
 **limitAvailableTerritories** | **Number**| maximum number of related availableTerritories returned (when they are included) | [optional] 
 **limitBetaAppLocalizations** | **Number**| maximum number of related betaAppLocalizations returned (when they are included) | [optional] 
 **limitBetaGroups** | **Number**| maximum number of related betaGroups returned (when they are included) | [optional] 
 **limitBuilds** | **Number**| maximum number of related builds returned (when they are included) | [optional] 
 **limitGameCenterEnabledVersions** | **Number**| maximum number of related gameCenterEnabledVersions returned (when they are included) | [optional] 
 **limitInAppPurchases** | **Number**| maximum number of related inAppPurchases returned (when they are included) | [optional] 
 **limitPreReleaseVersions** | **Number**| maximum number of related preReleaseVersions returned (when they are included) | [optional] 
 **limitPrices** | **Number**| maximum number of related prices returned (when they are included) | [optional] 

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsGetInstance

> AppResponse appsGetInstance(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'include': ["null"], // [String] | comma-separated list of relationships to include
  'fieldsBetaGroups': ["null"], // [String] | the fields to include for returned resources of type betaGroups
  'fieldsPerfPowerMetrics': ["null"], // [String] | the fields to include for returned resources of type perfPowerMetrics
  'fieldsAppInfos': ["null"], // [String] | the fields to include for returned resources of type appInfos
  'fieldsAppPreOrders': ["null"], // [String] | the fields to include for returned resources of type appPreOrders
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'fieldsAppPrices': ["null"], // [String] | the fields to include for returned resources of type appPrices
  'fieldsInAppPurchases': ["null"], // [String] | the fields to include for returned resources of type inAppPurchases
  'fieldsBetaAppReviewDetails': ["null"], // [String] | the fields to include for returned resources of type betaAppReviewDetails
  'fieldsTerritories': ["null"], // [String] | the fields to include for returned resources of type territories
  'fieldsGameCenterEnabledVersions': ["null"], // [String] | the fields to include for returned resources of type gameCenterEnabledVersions
  'fieldsAppStoreVersions': ["null"], // [String] | the fields to include for returned resources of type appStoreVersions
  'fieldsBuilds': ["null"], // [String] | the fields to include for returned resources of type builds
  'fieldsBetaAppLocalizations': ["null"], // [String] | the fields to include for returned resources of type betaAppLocalizations
  'fieldsBetaLicenseAgreements': ["null"], // [String] | the fields to include for returned resources of type betaLicenseAgreements
  'fieldsEndUserLicenseAgreements': ["null"], // [String] | the fields to include for returned resources of type endUserLicenseAgreements
  'limitAppInfos': 56, // Number | maximum number of related appInfos returned (when they are included)
  'limitAppStoreVersions': 56, // Number | maximum number of related appStoreVersions returned (when they are included)
  'limitAvailableTerritories': 56, // Number | maximum number of related availableTerritories returned (when they are included)
  'limitBetaAppLocalizations': 56, // Number | maximum number of related betaAppLocalizations returned (when they are included)
  'limitBetaGroups': 56, // Number | maximum number of related betaGroups returned (when they are included)
  'limitBuilds': 56, // Number | maximum number of related builds returned (when they are included)
  'limitGameCenterEnabledVersions': 56, // Number | maximum number of related gameCenterEnabledVersions returned (when they are included)
  'limitInAppPurchases': 56, // Number | maximum number of related inAppPurchases returned (when they are included)
  'limitPreReleaseVersions': 56, // Number | maximum number of related preReleaseVersions returned (when they are included)
  'limitPrices': 56 // Number | maximum number of related prices returned (when they are included)
};
apiInstance.appsGetInstance(id, opts, (error, data, response) => {
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
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 
 **fieldsBetaGroups** | [**[String]**](String.md)| the fields to include for returned resources of type betaGroups | [optional] 
 **fieldsPerfPowerMetrics** | [**[String]**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] 
 **fieldsAppInfos** | [**[String]**](String.md)| the fields to include for returned resources of type appInfos | [optional] 
 **fieldsAppPreOrders** | [**[String]**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] 
 **fieldsPreReleaseVersions** | [**[String]**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] 
 **fieldsAppPrices** | [**[String]**](String.md)| the fields to include for returned resources of type appPrices | [optional] 
 **fieldsInAppPurchases** | [**[String]**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] 
 **fieldsBetaAppReviewDetails** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppReviewDetails | [optional] 
 **fieldsTerritories** | [**[String]**](String.md)| the fields to include for returned resources of type territories | [optional] 
 **fieldsGameCenterEnabledVersions** | [**[String]**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] 
 **fieldsAppStoreVersions** | [**[String]**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] 
 **fieldsBuilds** | [**[String]**](String.md)| the fields to include for returned resources of type builds | [optional] 
 **fieldsBetaAppLocalizations** | [**[String]**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] 
 **fieldsBetaLicenseAgreements** | [**[String]**](String.md)| the fields to include for returned resources of type betaLicenseAgreements | [optional] 
 **fieldsEndUserLicenseAgreements** | [**[String]**](String.md)| the fields to include for returned resources of type endUserLicenseAgreements | [optional] 
 **limitAppInfos** | **Number**| maximum number of related appInfos returned (when they are included) | [optional] 
 **limitAppStoreVersions** | **Number**| maximum number of related appStoreVersions returned (when they are included) | [optional] 
 **limitAvailableTerritories** | **Number**| maximum number of related availableTerritories returned (when they are included) | [optional] 
 **limitBetaAppLocalizations** | **Number**| maximum number of related betaAppLocalizations returned (when they are included) | [optional] 
 **limitBetaGroups** | **Number**| maximum number of related betaGroups returned (when they are included) | [optional] 
 **limitBuilds** | **Number**| maximum number of related builds returned (when they are included) | [optional] 
 **limitGameCenterEnabledVersions** | **Number**| maximum number of related gameCenterEnabledVersions returned (when they are included) | [optional] 
 **limitInAppPurchases** | **Number**| maximum number of related inAppPurchases returned (when they are included) | [optional] 
 **limitPreReleaseVersions** | **Number**| maximum number of related preReleaseVersions returned (when they are included) | [optional] 
 **limitPrices** | **Number**| maximum number of related prices returned (when they are included) | [optional] 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsInAppPurchasesGetToManyRelated

> InAppPurchasesResponse appsInAppPurchasesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterInAppPurchaseType': ["null"], // [String] | filter by attribute 'inAppPurchaseType'
  'filterCanBeSubmitted': ["null"], // [String] | filter by canBeSubmitted
  'sort': ["null"], // [String] | comma-separated list of sort expressions; resources will be sorted as specified
  'fieldsInAppPurchases': ["null"], // [String] | the fields to include for returned resources of type inAppPurchases
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56, // Number | maximum resources per page
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appsInAppPurchasesGetToManyRelated(id, opts, (error, data, response) => {
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
 **filterInAppPurchaseType** | [**[String]**](String.md)| filter by attribute &#39;inAppPurchaseType&#39; | [optional] 
 **filterCanBeSubmitted** | [**[String]**](String.md)| filter by canBeSubmitted | [optional] 
 **sort** | [**[String]**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] 
 **fieldsInAppPurchases** | [**[String]**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**InAppPurchasesResponse**](InAppPurchasesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPerfPowerMetricsGetToManyRelated

> PerfPowerMetricsResponse appsPerfPowerMetricsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'filterDeviceType': ["null"], // [String] | filter by attribute 'deviceType'
  'filterMetricType': ["null"], // [String] | filter by attribute 'metricType'
  'filterPlatform': ["null"] // [String] | filter by attribute 'platform'
};
apiInstance.appsPerfPowerMetricsGetToManyRelated(id, opts, (error, data, response) => {
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


## appsPreOrderGetToOneRelated

> AppPreOrderResponse appsPreOrderGetToOneRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPreOrders': ["null"] // [String] | the fields to include for returned resources of type appPreOrders
};
apiInstance.appsPreOrderGetToOneRelated(id, opts, (error, data, response) => {
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
 **fieldsAppPreOrders** | [**[String]**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] 

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPreReleaseVersionsGetToManyRelated

> PreReleaseVersionsResponse appsPreReleaseVersionsGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsPreReleaseVersions': ["null"], // [String] | the fields to include for returned resources of type preReleaseVersions
  'limit': 56 // Number | maximum resources per page
};
apiInstance.appsPreReleaseVersionsGetToManyRelated(id, opts, (error, data, response) => {
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
 **limit** | **Number**| maximum resources per page | [optional] 

### Return type

[**PreReleaseVersionsResponse**](PreReleaseVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsPricesGetToManyRelated

> AppPricesResponse appsPricesGetToManyRelated(id, opts)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let opts = {
  'fieldsAppPrices': ["null"], // [String] | the fields to include for returned resources of type appPrices
  'fieldsAppPriceTiers': ["null"], // [String] | the fields to include for returned resources of type appPriceTiers
  'fieldsApps': ["null"], // [String] | the fields to include for returned resources of type apps
  'limit': 56, // Number | maximum resources per page
  'include': ["null"] // [String] | comma-separated list of relationships to include
};
apiInstance.appsPricesGetToManyRelated(id, opts, (error, data, response) => {
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
 **fieldsAppPrices** | [**[String]**](String.md)| the fields to include for returned resources of type appPrices | [optional] 
 **fieldsAppPriceTiers** | [**[String]**](String.md)| the fields to include for returned resources of type appPriceTiers | [optional] 
 **fieldsApps** | [**[String]**](String.md)| the fields to include for returned resources of type apps | [optional] 
 **limit** | **Number**| maximum resources per page | [optional] 
 **include** | [**[String]**](String.md)| comma-separated list of relationships to include | [optional] 

### Return type

[**AppPricesResponse**](AppPricesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## appsUpdateInstance

> AppResponse appsUpdateInstance(id, appUpdateRequest)



### Example

```javascript
import AppStoreConnectApi from 'app_store_connect_api';
let defaultClient = AppStoreConnectApi.ApiClient.instance;
// Configure Bearer (JWT) access token for authorization: itc-bearer-token
let itc-bearer-token = defaultClient.authentications['itc-bearer-token'];
itc-bearer-token.accessToken = "YOUR ACCESS TOKEN"

let apiInstance = new AppStoreConnectApi.AppsApi();
let id = "id_example"; // String | the id of the requested resource
let appUpdateRequest = new AppStoreConnectApi.AppUpdateRequest(); // AppUpdateRequest | App representation
apiInstance.appsUpdateInstance(id, appUpdateRequest, (error, data, response) => {
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
 **appUpdateRequest** | [**AppUpdateRequest**](AppUpdateRequest.md)| App representation | 

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

