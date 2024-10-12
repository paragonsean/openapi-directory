# AppStoreVersionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appStoreVersionsAgeRatingDeclarationGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsAgeRatingDeclarationGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/ageRatingDeclaration |  |
| [**appStoreVersionsAppStoreReviewDetailGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsAppStoreReviewDetailGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/appStoreReviewDetail |  |
| [**appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated**](AppStoreVersionsApi.md#appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated) | **GET** /v1/appStoreVersions/{id}/appStoreVersionLocalizations |  |
| [**appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/appStoreVersionPhasedRelease |  |
| [**appStoreVersionsAppStoreVersionSubmissionGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsAppStoreVersionSubmissionGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/appStoreVersionSubmission |  |
| [**appStoreVersionsBuildGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsBuildGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/build |  |
| [**appStoreVersionsBuildGetToOneRelationship**](AppStoreVersionsApi.md#appStoreVersionsBuildGetToOneRelationship) | **GET** /v1/appStoreVersions/{id}/relationships/build |  |
| [**appStoreVersionsBuildUpdateToOneRelationship**](AppStoreVersionsApi.md#appStoreVersionsBuildUpdateToOneRelationship) | **PATCH** /v1/appStoreVersions/{id}/relationships/build |  |
| [**appStoreVersionsCreateInstance**](AppStoreVersionsApi.md#appStoreVersionsCreateInstance) | **POST** /v1/appStoreVersions |  |
| [**appStoreVersionsDeleteInstance**](AppStoreVersionsApi.md#appStoreVersionsDeleteInstance) | **DELETE** /v1/appStoreVersions/{id} |  |
| [**appStoreVersionsGetInstance**](AppStoreVersionsApi.md#appStoreVersionsGetInstance) | **GET** /v1/appStoreVersions/{id} |  |
| [**appStoreVersionsIdfaDeclarationGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsIdfaDeclarationGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/idfaDeclaration |  |
| [**appStoreVersionsRoutingAppCoverageGetToOneRelated**](AppStoreVersionsApi.md#appStoreVersionsRoutingAppCoverageGetToOneRelated) | **GET** /v1/appStoreVersions/{id}/routingAppCoverage |  |
| [**appStoreVersionsUpdateInstance**](AppStoreVersionsApi.md#appStoreVersionsUpdateInstance) | **PATCH** /v1/appStoreVersions/{id} |  |


<a id="appStoreVersionsAgeRatingDeclarationGetToOneRelated"></a>
# **appStoreVersionsAgeRatingDeclarationGetToOneRelated**
> AgeRatingDeclarationResponse appStoreVersionsAgeRatingDeclarationGetToOneRelated(id, fieldsAgeRatingDeclarations)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAgeRatingDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type ageRatingDeclarations
    try {
      AgeRatingDeclarationResponse result = apiInstance.appStoreVersionsAgeRatingDeclarationGetToOneRelated(id, fieldsAgeRatingDeclarations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsAgeRatingDeclarationGetToOneRelated");
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
| **fieldsAgeRatingDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] [enum: alcoholTobaccoOrDrugUseOrReferences, gamblingAndContests, gamblingSimulated, horrorOrFearThemes, kidsAgeBand, matureOrSuggestiveThemes, medicalOrTreatmentInformation, profanityOrCrudeHumor, sexualContentGraphicAndNudity, sexualContentOrNudity, unrestrictedWebAccess, violenceCartoonOrFantasy, violenceRealistic, violenceRealisticProlongedGraphicOrSadistic] |

### Return type

[**AgeRatingDeclarationResponse**](AgeRatingDeclarationResponse.md)

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

<a id="appStoreVersionsAppStoreReviewDetailGetToOneRelated"></a>
# **appStoreVersionsAppStoreReviewDetailGetToOneRelated**
> AppStoreReviewDetailResponse appStoreVersionsAppStoreReviewDetailGetToOneRelated(id, fieldsAppStoreReviewDetails, fieldsAppStoreVersions, fieldsAppStoreReviewAttachments, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewDetails
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsAppStoreReviewAttachments = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewAttachments
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppStoreReviewDetailResponse result = apiInstance.appStoreVersionsAppStoreReviewDetailGetToOneRelated(id, fieldsAppStoreReviewDetails, fieldsAppStoreVersions, fieldsAppStoreReviewAttachments, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsAppStoreReviewDetailGetToOneRelated");
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
| **fieldsAppStoreReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewDetails | [optional] [enum: appStoreReviewAttachments, appStoreVersion, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsAppStoreReviewAttachments** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewAttachments | [optional] [enum: appStoreReviewDetail, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appStoreReviewAttachments, appStoreVersion] |

### Return type

[**AppStoreReviewDetailResponse**](AppStoreReviewDetailResponse.md)

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

<a id="appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated"></a>
# **appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated**
> AppStoreVersionLocalizationsResponse appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated(id, fieldsAppStoreVersionLocalizations, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreVersionLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionLocalizations
    Integer limit = 56; // Integer | maximum resources per page
    try {
      AppStoreVersionLocalizationsResponse result = apiInstance.appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated(id, fieldsAppStoreVersionLocalizations, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsAppStoreVersionLocalizationsGetToManyRelated");
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
| **fieldsAppStoreVersionLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion, description, keywords, locale, marketingUrl, promotionalText, supportUrl, whatsNew] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**AppStoreVersionLocalizationsResponse**](AppStoreVersionLocalizationsResponse.md)

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

<a id="appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated"></a>
# **appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated**
> AppStoreVersionPhasedReleaseResponse appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated(id, fieldsAppStoreVersionPhasedReleases)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreVersionPhasedReleases = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionPhasedReleases
    try {
      AppStoreVersionPhasedReleaseResponse result = apiInstance.appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated(id, fieldsAppStoreVersionPhasedReleases);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsAppStoreVersionPhasedReleaseGetToOneRelated");
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
| **fieldsAppStoreVersionPhasedReleases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionPhasedReleases | [optional] [enum: appStoreVersion, currentDayNumber, phasedReleaseState, startDate, totalPauseDuration] |

### Return type

[**AppStoreVersionPhasedReleaseResponse**](AppStoreVersionPhasedReleaseResponse.md)

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

<a id="appStoreVersionsAppStoreVersionSubmissionGetToOneRelated"></a>
# **appStoreVersionsAppStoreVersionSubmissionGetToOneRelated**
> AppStoreVersionSubmissionResponse appStoreVersionsAppStoreVersionSubmissionGetToOneRelated(id, fieldsAppStoreVersions, fieldsAppStoreVersionSubmissions, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsAppStoreVersionSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionSubmissions
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppStoreVersionSubmissionResponse result = apiInstance.appStoreVersionsAppStoreVersionSubmissionGetToOneRelated(id, fieldsAppStoreVersions, fieldsAppStoreVersionSubmissions, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsAppStoreVersionSubmissionGetToOneRelated");
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
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsAppStoreVersionSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionSubmissions | [optional] [enum: appStoreVersion] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appStoreVersion] |

### Return type

[**AppStoreVersionSubmissionResponse**](AppStoreVersionSubmissionResponse.md)

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

<a id="appStoreVersionsBuildGetToOneRelated"></a>
# **appStoreVersionsBuildGetToOneRelated**
> BuildResponse appStoreVersionsBuildGetToOneRelated(id, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BuildResponse result = apiInstance.appStoreVersionsBuildGetToOneRelated(id, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsBuildGetToOneRelated");
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

### Return type

[**BuildResponse**](BuildResponse.md)

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

<a id="appStoreVersionsBuildGetToOneRelationship"></a>
# **appStoreVersionsBuildGetToOneRelationship**
> AppStoreVersionBuildLinkageResponse appStoreVersionsBuildGetToOneRelationship(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      AppStoreVersionBuildLinkageResponse result = apiInstance.appStoreVersionsBuildGetToOneRelationship(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsBuildGetToOneRelationship");
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

### Return type

[**AppStoreVersionBuildLinkageResponse**](AppStoreVersionBuildLinkageResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Related linkage |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appStoreVersionsBuildUpdateToOneRelationship"></a>
# **appStoreVersionsBuildUpdateToOneRelationship**
> appStoreVersionsBuildUpdateToOneRelationship(id, appStoreVersionBuildLinkageRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppStoreVersionBuildLinkageRequest appStoreVersionBuildLinkageRequest = new AppStoreVersionBuildLinkageRequest(); // AppStoreVersionBuildLinkageRequest | Related linkage
    try {
      apiInstance.appStoreVersionsBuildUpdateToOneRelationship(id, appStoreVersionBuildLinkageRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsBuildUpdateToOneRelationship");
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
| **appStoreVersionBuildLinkageRequest** | [**AppStoreVersionBuildLinkageRequest**](AppStoreVersionBuildLinkageRequest.md)| Related linkage | |

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

<a id="appStoreVersionsCreateInstance"></a>
# **appStoreVersionsCreateInstance**
> AppStoreVersionResponse appStoreVersionsCreateInstance(appStoreVersionCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    AppStoreVersionCreateRequest appStoreVersionCreateRequest = new AppStoreVersionCreateRequest(); // AppStoreVersionCreateRequest | AppStoreVersion representation
    try {
      AppStoreVersionResponse result = apiInstance.appStoreVersionsCreateInstance(appStoreVersionCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsCreateInstance");
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
| **appStoreVersionCreateRequest** | [**AppStoreVersionCreateRequest**](AppStoreVersionCreateRequest.md)| AppStoreVersion representation | |

### Return type

[**AppStoreVersionResponse**](AppStoreVersionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppStoreVersion |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreVersionsDeleteInstance"></a>
# **appStoreVersionsDeleteInstance**
> appStoreVersionsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appStoreVersionsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsDeleteInstance");
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

### Return type

null (empty response body)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Success (no content) |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appStoreVersionsGetInstance"></a>
# **appStoreVersionsGetInstance**
> AppStoreVersionResponse appStoreVersionsGetInstance(id, fieldsAppStoreVersions, include, fieldsAppStoreVersionLocalizations, fieldsIdfaDeclarations, fieldsRoutingAppCoverages, fieldsAppStoreVersionPhasedReleases, fieldsAgeRatingDeclarations, fieldsAppStoreReviewDetails, fieldsBuilds, fieldsAppStoreVersionSubmissions, limitAppStoreVersionLocalizations)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppStoreVersionLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionLocalizations
    List<String> fieldsIdfaDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type idfaDeclarations
    List<String> fieldsRoutingAppCoverages = Arrays.asList(); // List<String> | the fields to include for returned resources of type routingAppCoverages
    List<String> fieldsAppStoreVersionPhasedReleases = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionPhasedReleases
    List<String> fieldsAgeRatingDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type ageRatingDeclarations
    List<String> fieldsAppStoreReviewDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreReviewDetails
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsAppStoreVersionSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersionSubmissions
    Integer limitAppStoreVersionLocalizations = 56; // Integer | maximum number of related appStoreVersionLocalizations returned (when they are included)
    try {
      AppStoreVersionResponse result = apiInstance.appStoreVersionsGetInstance(id, fieldsAppStoreVersions, include, fieldsAppStoreVersionLocalizations, fieldsIdfaDeclarations, fieldsRoutingAppCoverages, fieldsAppStoreVersionPhasedReleases, fieldsAgeRatingDeclarations, fieldsAppStoreReviewDetails, fieldsBuilds, fieldsAppStoreVersionSubmissions, limitAppStoreVersionLocalizations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsGetInstance");
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
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, idfaDeclaration, routingAppCoverage] |
| **fieldsAppStoreVersionLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionLocalizations | [optional] [enum: appPreviewSets, appScreenshotSets, appStoreVersion, description, keywords, locale, marketingUrl, promotionalText, supportUrl, whatsNew] |
| **fieldsIdfaDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type idfaDeclarations | [optional] [enum: appStoreVersion, attributesActionWithPreviousAd, attributesAppInstallationToPreviousAd, honorsLimitedAdTracking, servesAds] |
| **fieldsRoutingAppCoverages** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type routingAppCoverages | [optional] [enum: appStoreVersion, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |
| **fieldsAppStoreVersionPhasedReleases** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionPhasedReleases | [optional] [enum: appStoreVersion, currentDayNumber, phasedReleaseState, startDate, totalPauseDuration] |
| **fieldsAgeRatingDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type ageRatingDeclarations | [optional] [enum: alcoholTobaccoOrDrugUseOrReferences, gamblingAndContests, gamblingSimulated, horrorOrFearThemes, kidsAgeBand, matureOrSuggestiveThemes, medicalOrTreatmentInformation, profanityOrCrudeHumor, sexualContentGraphicAndNudity, sexualContentOrNudity, unrestrictedWebAccess, violenceCartoonOrFantasy, violenceRealistic, violenceRealisticProlongedGraphicOrSadistic] |
| **fieldsAppStoreReviewDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreReviewDetails | [optional] [enum: appStoreReviewAttachments, appStoreVersion, contactEmail, contactFirstName, contactLastName, contactPhone, demoAccountName, demoAccountPassword, demoAccountRequired, notes] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsAppStoreVersionSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersionSubmissions | [optional] [enum: appStoreVersion] |
| **limitAppStoreVersionLocalizations** | **Integer**| maximum number of related appStoreVersionLocalizations returned (when they are included) | [optional] |

### Return type

[**AppStoreVersionResponse**](AppStoreVersionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreVersion |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appStoreVersionsIdfaDeclarationGetToOneRelated"></a>
# **appStoreVersionsIdfaDeclarationGetToOneRelated**
> IdfaDeclarationResponse appStoreVersionsIdfaDeclarationGetToOneRelated(id, fieldsIdfaDeclarations)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsIdfaDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type idfaDeclarations
    try {
      IdfaDeclarationResponse result = apiInstance.appStoreVersionsIdfaDeclarationGetToOneRelated(id, fieldsIdfaDeclarations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsIdfaDeclarationGetToOneRelated");
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
| **fieldsIdfaDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type idfaDeclarations | [optional] [enum: appStoreVersion, attributesActionWithPreviousAd, attributesAppInstallationToPreviousAd, honorsLimitedAdTracking, servesAds] |

### Return type

[**IdfaDeclarationResponse**](IdfaDeclarationResponse.md)

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

<a id="appStoreVersionsRoutingAppCoverageGetToOneRelated"></a>
# **appStoreVersionsRoutingAppCoverageGetToOneRelated**
> RoutingAppCoverageResponse appStoreVersionsRoutingAppCoverageGetToOneRelated(id, fieldsRoutingAppCoverages)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsRoutingAppCoverages = Arrays.asList(); // List<String> | the fields to include for returned resources of type routingAppCoverages
    try {
      RoutingAppCoverageResponse result = apiInstance.appStoreVersionsRoutingAppCoverageGetToOneRelated(id, fieldsRoutingAppCoverages);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsRoutingAppCoverageGetToOneRelated");
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
| **fieldsRoutingAppCoverages** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type routingAppCoverages | [optional] [enum: appStoreVersion, assetDeliveryState, fileName, fileSize, sourceFileChecksum, uploadOperations, uploaded] |

### Return type

[**RoutingAppCoverageResponse**](RoutingAppCoverageResponse.md)

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

<a id="appStoreVersionsUpdateInstance"></a>
# **appStoreVersionsUpdateInstance**
> AppStoreVersionResponse appStoreVersionsUpdateInstance(id, appStoreVersionUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppStoreVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppStoreVersionsApi apiInstance = new AppStoreVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppStoreVersionUpdateRequest appStoreVersionUpdateRequest = new AppStoreVersionUpdateRequest(); // AppStoreVersionUpdateRequest | AppStoreVersion representation
    try {
      AppStoreVersionResponse result = apiInstance.appStoreVersionsUpdateInstance(id, appStoreVersionUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppStoreVersionsApi#appStoreVersionsUpdateInstance");
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
| **appStoreVersionUpdateRequest** | [**AppStoreVersionUpdateRequest**](AppStoreVersionUpdateRequest.md)| AppStoreVersion representation | |

### Return type

[**AppStoreVersionResponse**](AppStoreVersionResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppStoreVersion |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

