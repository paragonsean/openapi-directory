# AppsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appsAppInfosGetToManyRelated**](AppsApi.md#appsAppInfosGetToManyRelated) | **GET** /v1/apps/{id}/appInfos |  |
| [**appsAppStoreVersionsGetToManyRelated**](AppsApi.md#appsAppStoreVersionsGetToManyRelated) | **GET** /v1/apps/{id}/appStoreVersions |  |
| [**appsAvailableTerritoriesGetToManyRelated**](AppsApi.md#appsAvailableTerritoriesGetToManyRelated) | **GET** /v1/apps/{id}/availableTerritories |  |
| [**appsBetaAppLocalizationsGetToManyRelated**](AppsApi.md#appsBetaAppLocalizationsGetToManyRelated) | **GET** /v1/apps/{id}/betaAppLocalizations |  |
| [**appsBetaAppReviewDetailGetToOneRelated**](AppsApi.md#appsBetaAppReviewDetailGetToOneRelated) | **GET** /v1/apps/{id}/betaAppReviewDetail |  |
| [**appsBetaGroupsGetToManyRelated**](AppsApi.md#appsBetaGroupsGetToManyRelated) | **GET** /v1/apps/{id}/betaGroups |  |
| [**appsBetaLicenseAgreementGetToOneRelated**](AppsApi.md#appsBetaLicenseAgreementGetToOneRelated) | **GET** /v1/apps/{id}/betaLicenseAgreement |  |
| [**appsBetaTestersDeleteToManyRelationship**](AppsApi.md#appsBetaTestersDeleteToManyRelationship) | **DELETE** /v1/apps/{id}/relationships/betaTesters |  |
| [**appsBuildsGetToManyRelated**](AppsApi.md#appsBuildsGetToManyRelated) | **GET** /v1/apps/{id}/builds |  |
| [**appsEndUserLicenseAgreementGetToOneRelated**](AppsApi.md#appsEndUserLicenseAgreementGetToOneRelated) | **GET** /v1/apps/{id}/endUserLicenseAgreement |  |
| [**appsGameCenterEnabledVersionsGetToManyRelated**](AppsApi.md#appsGameCenterEnabledVersionsGetToManyRelated) | **GET** /v1/apps/{id}/gameCenterEnabledVersions |  |
| [**appsGetCollection**](AppsApi.md#appsGetCollection) | **GET** /v1/apps |  |
| [**appsGetInstance**](AppsApi.md#appsGetInstance) | **GET** /v1/apps/{id} |  |
| [**appsInAppPurchasesGetToManyRelated**](AppsApi.md#appsInAppPurchasesGetToManyRelated) | **GET** /v1/apps/{id}/inAppPurchases |  |
| [**appsPerfPowerMetricsGetToManyRelated**](AppsApi.md#appsPerfPowerMetricsGetToManyRelated) | **GET** /v1/apps/{id}/perfPowerMetrics |  |
| [**appsPreOrderGetToOneRelated**](AppsApi.md#appsPreOrderGetToOneRelated) | **GET** /v1/apps/{id}/preOrder |  |
| [**appsPreReleaseVersionsGetToManyRelated**](AppsApi.md#appsPreReleaseVersionsGetToManyRelated) | **GET** /v1/apps/{id}/preReleaseVersions |  |
| [**appsPricesGetToManyRelated**](AppsApi.md#appsPricesGetToManyRelated) | **GET** /v1/apps/{id}/prices |  |
| [**appsUpdateInstance**](AppsApi.md#appsUpdateInstance) | **PATCH** /v1/apps/{id} |  |


<a id="appsAppInfosGetToManyRelated"></a>
# **appsAppInfosGetToManyRelated**
> AppInfosResponse appsAppInfosGetToManyRelated(id, fieldsAgeRatingDeclarations, fieldsAppInfos, fieldsAppCategories, fieldsAppInfoLocalizations, fieldsApps, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAgeRatingDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type ageRatingDeclarations
    List<String> fieldsAppInfos = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfos
    List<String> fieldsAppCategories = Arrays.asList(); // List<String> | the fields to include for returned resources of type appCategories
    List<String> fieldsAppInfoLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfoLocalizations
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppInfosResponse result = apiInstance.appsAppInfosGetToManyRelated(id, fieldsAgeRatingDeclarations, fieldsAppInfos, fieldsAppCategories, fieldsAppInfoLocalizations, fieldsApps, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsAppInfosGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsAgeRatingDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] [enum: alcoholTobaccoOrDrugUseOrReferences, contests, gambling, gamblingAndContests, gamblingSimulated, horrorOrFearThemes, kidsAgeBand, matureOrSuggestiveThemes, medicalOrTreatmentInformation, profanityOrCrudeHumor, seventeenPlus, sexualContentGraphicAndNudity, sexualContentOrNudity, unrestrictedWebAccess, violenceCartoonOrFantasy, violenceRealistic, violenceRealisticProlongedGraphicOrSadistic] |
| **fieldsAppInfos** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfos | [optional] [enum: ageRatingDeclaration, app, appInfoLocalizations, appStoreAgeRating, appStoreState, brazilAgeRating, kidsAgeBand, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |
| **fieldsAppCategories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appCategories | [optional] [enum: parent, platforms, subcategories] |
| **fieldsAppInfoLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] [enum: appInfo, locale, name, privacyPolicyText, privacyPolicyUrl, subtitle] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, appInfoLocalizations, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |

### Return type

[**AppInfosResponse**](AppInfosResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsAppStoreVersionsGetToManyRelated"></a>
# **appsAppStoreVersionsGetToManyRelated**
> AppStoreVersionsResponse appsAppStoreVersionsGetToManyRelated(id, filterAppStoreState, filterPlatform, filterVersionString, filterId, fieldsIdfaDeclarations, fieldsAppStoreVersionLocalizations, fieldsRoutingAppCoverages, fieldsAppStoreVersionPhasedReleases, fieldsAgeRatingDeclarations, fieldsAppStoreReviewDetails, fieldsAppStoreVersions, fieldsBuilds, fieldsAppStoreVersionSubmissions, fieldsApps, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterAppStoreState = Arrays.asList(); // List<String> | filter by attribute 'appStoreState'
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    List<String> filterVersionString = Arrays.asList(); // List<String> | filter by attribute 'versionString'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> fieldsIdfaDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type idfaDeclarations
    List<String> fieldsAppStoreVersionLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionLocalizations
    List<String> fieldsRoutingAppCoverages = Arrays.asList(); // List<String> | the fields to include for returned resources of type routingAppCoverages
    List<String> fieldsAppStoreVersionPhasedReleases = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionPhasedReleases
    List<String> fieldsAgeRatingDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type ageRatingDeclarations
    List<String> fieldsAppStoreReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewDetails
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsAppStoreVersionSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionSubmissions
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppStoreVersionsResponse result = apiInstance.appsAppStoreVersionsGetToManyRelated(id, filterAppStoreState, filterPlatform, filterVersionString, filterId, fieldsIdfaDeclarations, fieldsAppStoreVersionLocalizations, fieldsRoutingAppCoverages, fieldsAppStoreVersionPhasedReleases, fieldsAgeRatingDeclarations, fieldsAppStoreReviewDetails, fieldsAppStoreVersions, fieldsBuilds, fieldsAppStoreVersionSubmissions, fieldsApps, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsAppStoreVersionsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **filterAppStoreState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;appStoreState&#39; | [optional] [enum: DEVELOPER_REMOVED_FROM_SALE, DEVELOPER_REJECTED, IN_REVIEW, INVALID_BINARY, METADATA_REJECTED, PENDING_APPLE_RELEASE, PENDING_CONTRACT, PENDING_DEVELOPER_RELEASE, PREPARE_FOR_SUBMISSION, PREORDER_READY_FOR_SALE, PROCESSING_FOR_APP_STORE, READY_FOR_SALE, REJECTED, REMOVED_FROM_SALE, WAITING_FOR_EXPORT_COMPLIANCE, WAITING_FOR_REVIEW, REPLACED_WITH_NEW_VERSION] |
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterVersionString** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;versionString&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **fieldsIdfaDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type idfaDeclarations | [optional] [enum: appStoreVersion, attributesActionWithPreviousAd, attributesAppInstallationToPreviousAd, honorsLimitedAdTracking, servesAds] |
| **fieldsAppStoreVersionLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion, description, keywords, locale, marketingUrl, promotionalText, supportUrl, whatsNew] |
| **fieldsRoutingAppCoverages** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type routingAppCoverages | [optional] [enum: appStoreVersion, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **fieldsAppStoreVersionPhasedReleases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionPhasedReleases | [optional] [enum: appStoreVersion, currentDayNumber, phasedReleaseState, startDate, totalPauseDuration] |
| **fieldsAgeRatingDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] [enum: alcoholTobaccoOrDrugUseOrReferences, gamblingAndContests, gamblingSimulated, horrorOrFearThemes, kidsAgeBand, matureOrSuggestiveThemes, medicalOrTreatmentInformation, profanityOrCrudeHumor, sexualContentGraphicAndNudity, sexualContentOrNudity, unrestrictedWebAccess, violenceCartoonOrFantasy, violenceRealistic, violenceRealisticProlongedGraphicOrSadistic] |
| **fieldsAppStoreReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewDetails | [optional] [enum: appStoreReviewAttachments, appStoreVersion, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsAppStoreVersionSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionSubmissions | [optional] [enum: appStoreVersion] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, idfaDeclaration, routingAppCoverage] |

### Return type

[**AppStoreVersionsResponse**](AppStoreVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsAvailableTerritoriesGetToManyRelated"></a>
# **appsAvailableTerritoriesGetToManyRelated**
> TerritoriesResponse appsAvailableTerritoriesGetToManyRelated(id, fieldsTerritories, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    Integer limit = 56; // Integer | maximum resources per page
    try {
      TerritoriesResponse result = apiInstance.appsAvailableTerritoriesGetToManyRelated(id, fieldsTerritories, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsAvailableTerritoriesGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**TerritoriesResponse**](TerritoriesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsBetaAppLocalizationsGetToManyRelated"></a>
# **appsBetaAppLocalizationsGetToManyRelated**
> BetaAppLocalizationsResponse appsBetaAppLocalizationsGetToManyRelated(id, fieldsBetaAppLocalizations, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaAppLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppLocalizations
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaAppLocalizationsResponse result = apiInstance.appsBetaAppLocalizationsGetToManyRelated(id, fieldsBetaAppLocalizations, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsBetaAppLocalizationsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaAppLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] [enum: app, description, feedbackEmail, locale, marketingUrl, privacyPolicyUrl, tvOsPrivacyPolicy] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaAppLocalizationsResponse**](BetaAppLocalizationsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsBetaAppReviewDetailGetToOneRelated"></a>
# **appsBetaAppReviewDetailGetToOneRelated**
> BetaAppReviewDetailResponse appsBetaAppReviewDetailGetToOneRelated(id, fieldsBetaAppReviewDetails)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaAppReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewDetails
    try {
      BetaAppReviewDetailResponse result = apiInstance.appsBetaAppReviewDetailGetToOneRelated(id, fieldsBetaAppReviewDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsBetaAppReviewDetailGetToOneRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaAppReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewDetails | [optional] [enum: app, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |

### Return type

[**BetaAppReviewDetailResponse**](BetaAppReviewDetailResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsBetaGroupsGetToManyRelated"></a>
# **appsBetaGroupsGetToManyRelated**
> BetaGroupsResponse appsBetaGroupsGetToManyRelated(id, fieldsBetaGroups, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaGroupsResponse result = apiInstance.appsBetaGroupsGetToManyRelated(id, fieldsBetaGroups, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsBetaGroupsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaGroupsResponse**](BetaGroupsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsBetaLicenseAgreementGetToOneRelated"></a>
# **appsBetaLicenseAgreementGetToOneRelated**
> BetaLicenseAgreementResponse appsBetaLicenseAgreementGetToOneRelated(id, fieldsBetaLicenseAgreements)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaLicenseAgreements = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaLicenseAgreements
    try {
      BetaLicenseAgreementResponse result = apiInstance.appsBetaLicenseAgreementGetToOneRelated(id, fieldsBetaLicenseAgreements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsBetaLicenseAgreementGetToOneRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsBetaLicenseAgreements** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaLicenseAgreements | [optional] [enum: agreementText, app] |

### Return type

[**BetaLicenseAgreementResponse**](BetaLicenseAgreementResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsBetaTestersDeleteToManyRelationship"></a>
# **appsBetaTestersDeleteToManyRelationship**
> appsBetaTestersDeleteToManyRelationship(id, appBetaTestersLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppBetaTestersLinkagesRequest appBetaTestersLinkagesRequest = new AppBetaTestersLinkagesRequest(); // AppBetaTestersLinkagesRequest | List of related linkages
    try {
      apiInstance.appsBetaTestersDeleteToManyRelationship(id, appBetaTestersLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsBetaTestersDeleteToManyRelationship");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **appBetaTestersLinkagesRequest** | [**AppBetaTestersLinkagesRequest**](AppBetaTestersLinkagesRequest.md)| List of related linkages | |

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appsBuildsGetToManyRelated"></a>
# **appsBuildsGetToManyRelated**
> BuildsResponse appsBuildsGetToManyRelated(id, fieldsBuilds, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BuildsResponse result = apiInstance.appsBuildsGetToManyRelated(id, fieldsBuilds, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsBuildsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BuildsResponse**](BuildsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsEndUserLicenseAgreementGetToOneRelated"></a>
# **appsEndUserLicenseAgreementGetToOneRelated**
> EndUserLicenseAgreementResponse appsEndUserLicenseAgreementGetToOneRelated(id, fieldsEndUserLicenseAgreements)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsEndUserLicenseAgreements = Arrays.asList(); // List<String> | the fields to include for returned resources of type endUserLicenseAgreements
    try {
      EndUserLicenseAgreementResponse result = apiInstance.appsEndUserLicenseAgreementGetToOneRelated(id, fieldsEndUserLicenseAgreements);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsEndUserLicenseAgreementGetToOneRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsEndUserLicenseAgreements** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type endUserLicenseAgreements | [optional] [enum: agreementText, app, territories] |

### Return type

[**EndUserLicenseAgreementResponse**](EndUserLicenseAgreementResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsGameCenterEnabledVersionsGetToManyRelated"></a>
# **appsGameCenterEnabledVersionsGetToManyRelated**
> GameCenterEnabledVersionsResponse appsGameCenterEnabledVersionsGetToManyRelated(id, filterPlatform, filterVersionString, filterId, sort, fieldsGameCenterEnabledVersions, fieldsApps, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    List<String> filterVersionString = Arrays.asList(); // List<String> | filter by attribute 'versionString'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsGameCenterEnabledVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type gameCenterEnabledVersions
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      GameCenterEnabledVersionsResponse result = apiInstance.appsGameCenterEnabledVersionsGetToManyRelated(id, filterPlatform, filterVersionString, filterId, sort, fieldsGameCenterEnabledVersions, fieldsApps, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGameCenterEnabledVersionsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterVersionString** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;versionString&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: versionString, -versionString] |
| **fieldsGameCenterEnabledVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] [enum: app, compatibleVersions, iconAsset, platform, versionString] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, compatibleVersions] |

### Return type

[**GameCenterEnabledVersionsResponse**](GameCenterEnabledVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsGetCollection"></a>
# **appsGetCollection**
> AppsResponse appsGetCollection(filterAppStoreVersionsAppStoreState, filterAppStoreVersionsPlatform, filterBundleId, filterName, filterSku, filterAppStoreVersions, filterId, existsGameCenterEnabledVersions, sort, fieldsApps, limit, include, fieldsBetaGroups, fieldsPerfPowerMetrics, fieldsAppInfos, fieldsAppPreOrders, fieldsPreReleaseVersions, fieldsAppPrices, fieldsInAppPurchases, fieldsBetaAppReviewDetails, fieldsTerritories, fieldsGameCenterEnabledVersions, fieldsAppStoreVersions, fieldsBuilds, fieldsBetaAppLocalizations, fieldsBetaLicenseAgreements, fieldsEndUserLicenseAgreements, limitAppInfos, limitAppStoreVersions, limitAvailableTerritories, limitBetaAppLocalizations, limitBetaGroups, limitBuilds, limitGameCenterEnabledVersions, limitInAppPurchases, limitPreReleaseVersions, limitPrices)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    List<String> filterAppStoreVersionsAppStoreState = Arrays.asList(); // List<String> | filter by attribute 'appStoreVersions.appStoreState'
    List<String> filterAppStoreVersionsPlatform = Arrays.asList(); // List<String> | filter by attribute 'appStoreVersions.platform'
    List<String> filterBundleId = Arrays.asList(); // List<String> | filter by attribute 'bundleId'
    List<String> filterName = Arrays.asList(); // List<String> | filter by attribute 'name'
    List<String> filterSku = Arrays.asList(); // List<String> | filter by attribute 'sku'
    List<String> filterAppStoreVersions = Arrays.asList(); // List<String> | filter by id(s) of related 'appStoreVersions'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> existsGameCenterEnabledVersions = Arrays.asList(); // List<String> | filter by existence or non-existence of related 'gameCenterEnabledVersions'
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    List<String> fieldsPerfPowerMetrics = Arrays.asList(); // List<String> | the fields to include for returned resources of type perfPowerMetrics
    List<String> fieldsAppInfos = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfos
    List<String> fieldsAppPreOrders = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreOrders
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    List<String> fieldsAppPrices = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPrices
    List<String> fieldsInAppPurchases = Arrays.asList(); // List<String> | the fields to include for returned resources of type inAppPurchases
    List<String> fieldsBetaAppReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewDetails
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    List<String> fieldsGameCenterEnabledVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type gameCenterEnabledVersions
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsBetaAppLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppLocalizations
    List<String> fieldsBetaLicenseAgreements = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaLicenseAgreements
    List<String> fieldsEndUserLicenseAgreements = Arrays.asList(); // List<String> | the fields to include for returned resources of type endUserLicenseAgreements
    Integer limitAppInfos = 56; // Integer | maximum number of related appInfos returned (when they are included)
    Integer limitAppStoreVersions = 56; // Integer | maximum number of related appStoreVersions returned (when they are included)
    Integer limitAvailableTerritories = 56; // Integer | maximum number of related availableTerritories returned (when they are included)
    Integer limitBetaAppLocalizations = 56; // Integer | maximum number of related betaAppLocalizations returned (when they are included)
    Integer limitBetaGroups = 56; // Integer | maximum number of related betaGroups returned (when they are included)
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    Integer limitGameCenterEnabledVersions = 56; // Integer | maximum number of related gameCenterEnabledVersions returned (when they are included)
    Integer limitInAppPurchases = 56; // Integer | maximum number of related inAppPurchases returned (when they are included)
    Integer limitPreReleaseVersions = 56; // Integer | maximum number of related preReleaseVersions returned (when they are included)
    Integer limitPrices = 56; // Integer | maximum number of related prices returned (when they are included)
    try {
      AppsResponse result = apiInstance.appsGetCollection(filterAppStoreVersionsAppStoreState, filterAppStoreVersionsPlatform, filterBundleId, filterName, filterSku, filterAppStoreVersions, filterId, existsGameCenterEnabledVersions, sort, fieldsApps, limit, include, fieldsBetaGroups, fieldsPerfPowerMetrics, fieldsAppInfos, fieldsAppPreOrders, fieldsPreReleaseVersions, fieldsAppPrices, fieldsInAppPurchases, fieldsBetaAppReviewDetails, fieldsTerritories, fieldsGameCenterEnabledVersions, fieldsAppStoreVersions, fieldsBuilds, fieldsBetaAppLocalizations, fieldsBetaLicenseAgreements, fieldsEndUserLicenseAgreements, limitAppInfos, limitAppStoreVersions, limitAvailableTerritories, limitBetaAppLocalizations, limitBetaGroups, limitBuilds, limitGameCenterEnabledVersions, limitInAppPurchases, limitPreReleaseVersions, limitPrices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetCollection");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **filterAppStoreVersionsAppStoreState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;appStoreVersions.appStoreState&#39; | [optional] [enum: DEVELOPER_REMOVED_FROM_SALE, DEVELOPER_REJECTED, IN_REVIEW, INVALID_BINARY, METADATA_REJECTED, PENDING_APPLE_RELEASE, PENDING_CONTRACT, PENDING_DEVELOPER_RELEASE, PREPARE_FOR_SUBMISSION, PREORDER_READY_FOR_SALE, PROCESSING_FOR_APP_STORE, READY_FOR_SALE, REJECTED, REMOVED_FROM_SALE, WAITING_FOR_EXPORT_COMPLIANCE, WAITING_FOR_REVIEW, REPLACED_WITH_NEW_VERSION] |
| **filterAppStoreVersionsPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;appStoreVersions.platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterBundleId** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;bundleId&#39; | [optional] |
| **filterName** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;name&#39; | [optional] |
| **filterSku** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;sku&#39; | [optional] |
| **filterAppStoreVersions** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;appStoreVersions&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **existsGameCenterEnabledVersions** | [**List&lt;String&gt;**](String.md)| filter by existence or non-existence of related &#39;gameCenterEnabledVersions&#39; | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: bundleId, -bundleId, name, -name, sku, -sku] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appInfos, appStoreVersions, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, builds, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, preOrder, preReleaseVersions, prices] |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **fieldsPerfPowerMetrics** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] [enum: deviceType, metricType, platform] |
| **fieldsAppInfos** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfos | [optional] [enum: ageRatingDeclaration, app, appInfoLocalizations, appStoreAgeRating, appStoreState, brazilAgeRating, kidsAgeBand, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |
| **fieldsAppPreOrders** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] [enum: app, appReleaseDate, preOrderAvailableDate] |
| **fieldsPreReleaseVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] [enum: app, builds, platform, version] |
| **fieldsAppPrices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPrices | [optional] [enum: app, priceTier] |
| **fieldsInAppPurchases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] [enum: apps, inAppPurchaseType, productId, referenceName, state] |
| **fieldsBetaAppReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewDetails | [optional] [enum: app, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |
| **fieldsGameCenterEnabledVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] [enum: app, compatibleVersions, iconAsset, platform, versionString] |
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsBetaAppLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] [enum: app, description, feedbackEmail, locale, marketingUrl, privacyPolicyUrl, tvOsPrivacyPolicy] |
| **fieldsBetaLicenseAgreements** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaLicenseAgreements | [optional] [enum: agreementText, app] |
| **fieldsEndUserLicenseAgreements** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type endUserLicenseAgreements | [optional] [enum: agreementText, app, territories] |
| **limitAppInfos** | **Integer**| maximum number of related appInfos returned (when they are included) | [optional] |
| **limitAppStoreVersions** | **Integer**| maximum number of related appStoreVersions returned (when they are included) | [optional] |
| **limitAvailableTerritories** | **Integer**| maximum number of related availableTerritories returned (when they are included) | [optional] |
| **limitBetaAppLocalizations** | **Integer**| maximum number of related betaAppLocalizations returned (when they are included) | [optional] |
| **limitBetaGroups** | **Integer**| maximum number of related betaGroups returned (when they are included) | [optional] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |
| **limitGameCenterEnabledVersions** | **Integer**| maximum number of related gameCenterEnabledVersions returned (when they are included) | [optional] |
| **limitInAppPurchases** | **Integer**| maximum number of related inAppPurchases returned (when they are included) | [optional] |
| **limitPreReleaseVersions** | **Integer**| maximum number of related preReleaseVersions returned (when they are included) | [optional] |
| **limitPrices** | **Integer**| maximum number of related prices returned (when they are included) | [optional] |

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of Apps |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="appsGetInstance"></a>
# **appsGetInstance**
> AppResponse appsGetInstance(id, fieldsApps, include, fieldsBetaGroups, fieldsPerfPowerMetrics, fieldsAppInfos, fieldsAppPreOrders, fieldsPreReleaseVersions, fieldsAppPrices, fieldsInAppPurchases, fieldsBetaAppReviewDetails, fieldsTerritories, fieldsGameCenterEnabledVersions, fieldsAppStoreVersions, fieldsBuilds, fieldsBetaAppLocalizations, fieldsBetaLicenseAgreements, fieldsEndUserLicenseAgreements, limitAppInfos, limitAppStoreVersions, limitAvailableTerritories, limitBetaAppLocalizations, limitBetaGroups, limitBuilds, limitGameCenterEnabledVersions, limitInAppPurchases, limitPreReleaseVersions, limitPrices)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBetaGroups = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaGroups
    List<String> fieldsPerfPowerMetrics = Arrays.asList(); // List<String> | the fields to include for returned resources of type perfPowerMetrics
    List<String> fieldsAppInfos = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfos
    List<String> fieldsAppPreOrders = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreOrders
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    List<String> fieldsAppPrices = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPrices
    List<String> fieldsInAppPurchases = Arrays.asList(); // List<String> | the fields to include for returned resources of type inAppPurchases
    List<String> fieldsBetaAppReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewDetails
    List<String> fieldsTerritories = Arrays.asList(); // List<String> | the fields to include for returned resources of type territories
    List<String> fieldsGameCenterEnabledVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type gameCenterEnabledVersions
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsBetaAppLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppLocalizations
    List<String> fieldsBetaLicenseAgreements = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaLicenseAgreements
    List<String> fieldsEndUserLicenseAgreements = Arrays.asList(); // List<String> | the fields to include for returned resources of type endUserLicenseAgreements
    Integer limitAppInfos = 56; // Integer | maximum number of related appInfos returned (when they are included)
    Integer limitAppStoreVersions = 56; // Integer | maximum number of related appStoreVersions returned (when they are included)
    Integer limitAvailableTerritories = 56; // Integer | maximum number of related availableTerritories returned (when they are included)
    Integer limitBetaAppLocalizations = 56; // Integer | maximum number of related betaAppLocalizations returned (when they are included)
    Integer limitBetaGroups = 56; // Integer | maximum number of related betaGroups returned (when they are included)
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    Integer limitGameCenterEnabledVersions = 56; // Integer | maximum number of related gameCenterEnabledVersions returned (when they are included)
    Integer limitInAppPurchases = 56; // Integer | maximum number of related inAppPurchases returned (when they are included)
    Integer limitPreReleaseVersions = 56; // Integer | maximum number of related preReleaseVersions returned (when they are included)
    Integer limitPrices = 56; // Integer | maximum number of related prices returned (when they are included)
    try {
      AppResponse result = apiInstance.appsGetInstance(id, fieldsApps, include, fieldsBetaGroups, fieldsPerfPowerMetrics, fieldsAppInfos, fieldsAppPreOrders, fieldsPreReleaseVersions, fieldsAppPrices, fieldsInAppPurchases, fieldsBetaAppReviewDetails, fieldsTerritories, fieldsGameCenterEnabledVersions, fieldsAppStoreVersions, fieldsBuilds, fieldsBetaAppLocalizations, fieldsBetaLicenseAgreements, fieldsEndUserLicenseAgreements, limitAppInfos, limitAppStoreVersions, limitAvailableTerritories, limitBetaAppLocalizations, limitBetaGroups, limitBuilds, limitGameCenterEnabledVersions, limitInAppPurchases, limitPreReleaseVersions, limitPrices);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsGetInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appInfos, appStoreVersions, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, builds, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, preOrder, preReleaseVersions, prices] |
| **fieldsBetaGroups** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaGroups | [optional] [enum: app, betaTesters, builds, createdDate, feedbackEnabled, isInternalGroup, name, publicLink, publicLinkEnabled, publicLinkId, publicLinkLimit, publicLinkLimitEnabled] |
| **fieldsPerfPowerMetrics** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] [enum: deviceType, metricType, platform] |
| **fieldsAppInfos** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfos | [optional] [enum: ageRatingDeclaration, app, appInfoLocalizations, appStoreAgeRating, appStoreState, brazilAgeRating, kidsAgeBand, primaryCategory, primarySubcategoryOne, primarySubcategoryTwo, secondaryCategory, secondarySubcategoryOne, secondarySubcategoryTwo] |
| **fieldsAppPreOrders** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] [enum: app, appReleaseDate, preOrderAvailableDate] |
| **fieldsPreReleaseVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] [enum: app, builds, platform, version] |
| **fieldsAppPrices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPrices | [optional] [enum: app, priceTier] |
| **fieldsInAppPurchases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] [enum: apps, inAppPurchaseType, productId, referenceName, state] |
| **fieldsBetaAppReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewDetails | [optional] [enum: app, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **fieldsTerritories** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type territories | [optional] [enum: currency] |
| **fieldsGameCenterEnabledVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type gameCenterEnabledVersions | [optional] [enum: app, compatibleVersions, iconAsset, platform, versionString] |
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsBetaAppLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] [enum: app, description, feedbackEmail, locale, marketingUrl, privacyPolicyUrl, tvOsPrivacyPolicy] |
| **fieldsBetaLicenseAgreements** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaLicenseAgreements | [optional] [enum: agreementText, app] |
| **fieldsEndUserLicenseAgreements** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type endUserLicenseAgreements | [optional] [enum: agreementText, app, territories] |
| **limitAppInfos** | **Integer**| maximum number of related appInfos returned (when they are included) | [optional] |
| **limitAppStoreVersions** | **Integer**| maximum number of related appStoreVersions returned (when they are included) | [optional] |
| **limitAvailableTerritories** | **Integer**| maximum number of related availableTerritories returned (when they are included) | [optional] |
| **limitBetaAppLocalizations** | **Integer**| maximum number of related betaAppLocalizations returned (when they are included) | [optional] |
| **limitBetaGroups** | **Integer**| maximum number of related betaGroups returned (when they are included) | [optional] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |
| **limitGameCenterEnabledVersions** | **Integer**| maximum number of related gameCenterEnabledVersions returned (when they are included) | [optional] |
| **limitInAppPurchases** | **Integer**| maximum number of related inAppPurchases returned (when they are included) | [optional] |
| **limitPreReleaseVersions** | **Integer**| maximum number of related preReleaseVersions returned (when they are included) | [optional] |
| **limitPrices** | **Integer**| maximum number of related prices returned (when they are included) | [optional] |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single App |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsInAppPurchasesGetToManyRelated"></a>
# **appsInAppPurchasesGetToManyRelated**
> InAppPurchasesResponse appsInAppPurchasesGetToManyRelated(id, filterInAppPurchaseType, filterCanBeSubmitted, sort, fieldsInAppPurchases, fieldsApps, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterInAppPurchaseType = Arrays.asList(); // List<String> | filter by attribute 'inAppPurchaseType'
    List<String> filterCanBeSubmitted = Arrays.asList(); // List<String> | filter by canBeSubmitted
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsInAppPurchases = Arrays.asList(); // List<String> | the fields to include for returned resources of type inAppPurchases
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      InAppPurchasesResponse result = apiInstance.appsInAppPurchasesGetToManyRelated(id, filterInAppPurchaseType, filterCanBeSubmitted, sort, fieldsInAppPurchases, fieldsApps, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsInAppPurchasesGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **filterInAppPurchaseType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;inAppPurchaseType&#39; | [optional] [enum: AUTOMATICALLY_RENEWABLE_SUBSCRIPTION, NON_CONSUMABLE, CONSUMABLE, NON_RENEWING_SUBSCRIPTION, FREE_SUBSCRIPTION] |
| **filterCanBeSubmitted** | [**List&lt;String&gt;**](String.md)| filter by canBeSubmitted | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: inAppPurchaseType, -inAppPurchaseType, productId, -productId, referenceName, -referenceName] |
| **fieldsInAppPurchases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type inAppPurchases | [optional] [enum: apps, inAppPurchaseType, productId, referenceName, state] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: apps] |

### Return type

[**InAppPurchasesResponse**](InAppPurchasesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsPerfPowerMetricsGetToManyRelated"></a>
# **appsPerfPowerMetricsGetToManyRelated**
> PerfPowerMetricsResponse appsPerfPowerMetricsGetToManyRelated(id, filterDeviceType, filterMetricType, filterPlatform)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterDeviceType = Arrays.asList(); // List<String> | filter by attribute 'deviceType'
    List<String> filterMetricType = Arrays.asList(); // List<String> | filter by attribute 'metricType'
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    try {
      PerfPowerMetricsResponse result = apiInstance.appsPerfPowerMetricsGetToManyRelated(id, filterDeviceType, filterMetricType, filterPlatform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPerfPowerMetricsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **filterDeviceType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;deviceType&#39; | [optional] |
| **filterMetricType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;metricType&#39; | [optional] [enum: DISK, HANG, BATTERY, LAUNCH, MEMORY, ANIMATION, TERMINATION] |
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS] |

### Return type

[**PerfPowerMetricsResponse**](PerfPowerMetricsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsPreOrderGetToOneRelated"></a>
# **appsPreOrderGetToOneRelated**
> AppPreOrderResponse appsPreOrderGetToOneRelated(id, fieldsAppPreOrders)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPreOrders = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPreOrders
    try {
      AppPreOrderResponse result = apiInstance.appsPreOrderGetToOneRelated(id, fieldsAppPreOrders);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPreOrderGetToOneRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsAppPreOrders** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPreOrders | [optional] [enum: app, appReleaseDate, preOrderAvailableDate] |

### Return type

[**AppPreOrderResponse**](AppPreOrderResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsPreReleaseVersionsGetToManyRelated"></a>
# **appsPreReleaseVersionsGetToManyRelated**
> PreReleaseVersionsResponse appsPreReleaseVersionsGetToManyRelated(id, fieldsPreReleaseVersions, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    Integer limit = 56; // Integer | maximum resources per page
    try {
      PreReleaseVersionsResponse result = apiInstance.appsPreReleaseVersionsGetToManyRelated(id, fieldsPreReleaseVersions, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPreReleaseVersionsGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsPreReleaseVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] [enum: app, builds, platform, version] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**PreReleaseVersionsResponse**](PreReleaseVersionsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsPricesGetToManyRelated"></a>
# **appsPricesGetToManyRelated**
> AppPricesResponse appsPricesGetToManyRelated(id, fieldsAppPrices, fieldsAppPriceTiers, fieldsApps, limit, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppPrices = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPrices
    List<String> fieldsAppPriceTiers = Arrays.asList(); // List<String> | the fields to include for returned resources of type appPriceTiers
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppPricesResponse result = apiInstance.appsPricesGetToManyRelated(id, fieldsAppPrices, fieldsAppPriceTiers, fieldsApps, limit, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsPricesGetToManyRelated");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **fieldsAppPrices** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPrices | [optional] [enum: app, priceTier] |
| **fieldsAppPriceTiers** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appPriceTiers | [optional] [enum: pricePoints] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, priceTier] |

### Return type

[**AppPricesResponse**](AppPricesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related resources |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appsUpdateInstance"></a>
# **appsUpdateInstance**
> AppResponse appsUpdateInstance(id, appUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppsApi apiInstance = new AppsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppUpdateRequest appUpdateRequest = new AppUpdateRequest(); // AppUpdateRequest | App representation
    try {
      AppResponse result = apiInstance.appsUpdateInstance(id, appUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppsApi#appsUpdateInstance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters

| Name | Type | Description  | Notes |
|------------- | ------------- | ------------- | -------------|
| **id** | **String**| the id of the requested resource | |
| **appUpdateRequest** | [**AppUpdateRequest**](AppUpdateRequest.md)| App representation | |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single App |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

