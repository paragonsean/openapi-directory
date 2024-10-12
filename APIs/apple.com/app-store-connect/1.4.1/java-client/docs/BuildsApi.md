# BuildsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**buildsAppEncryptionDeclarationGetToOneRelated**](BuildsApi.md#buildsAppEncryptionDeclarationGetToOneRelated) | **GET** /v1/builds/{id}/appEncryptionDeclaration |  |
| [**buildsAppEncryptionDeclarationGetToOneRelationship**](BuildsApi.md#buildsAppEncryptionDeclarationGetToOneRelationship) | **GET** /v1/builds/{id}/relationships/appEncryptionDeclaration |  |
| [**buildsAppEncryptionDeclarationUpdateToOneRelationship**](BuildsApi.md#buildsAppEncryptionDeclarationUpdateToOneRelationship) | **PATCH** /v1/builds/{id}/relationships/appEncryptionDeclaration |  |
| [**buildsAppGetToOneRelated**](BuildsApi.md#buildsAppGetToOneRelated) | **GET** /v1/builds/{id}/app |  |
| [**buildsAppStoreVersionGetToOneRelated**](BuildsApi.md#buildsAppStoreVersionGetToOneRelated) | **GET** /v1/builds/{id}/appStoreVersion |  |
| [**buildsBetaAppReviewSubmissionGetToOneRelated**](BuildsApi.md#buildsBetaAppReviewSubmissionGetToOneRelated) | **GET** /v1/builds/{id}/betaAppReviewSubmission |  |
| [**buildsBetaBuildLocalizationsGetToManyRelated**](BuildsApi.md#buildsBetaBuildLocalizationsGetToManyRelated) | **GET** /v1/builds/{id}/betaBuildLocalizations |  |
| [**buildsBetaGroupsCreateToManyRelationship**](BuildsApi.md#buildsBetaGroupsCreateToManyRelationship) | **POST** /v1/builds/{id}/relationships/betaGroups |  |
| [**buildsBetaGroupsDeleteToManyRelationship**](BuildsApi.md#buildsBetaGroupsDeleteToManyRelationship) | **DELETE** /v1/builds/{id}/relationships/betaGroups |  |
| [**buildsBuildBetaDetailGetToOneRelated**](BuildsApi.md#buildsBuildBetaDetailGetToOneRelated) | **GET** /v1/builds/{id}/buildBetaDetail |  |
| [**buildsDiagnosticSignaturesGetToManyRelated**](BuildsApi.md#buildsDiagnosticSignaturesGetToManyRelated) | **GET** /v1/builds/{id}/diagnosticSignatures |  |
| [**buildsGetCollection**](BuildsApi.md#buildsGetCollection) | **GET** /v1/builds |  |
| [**buildsGetInstance**](BuildsApi.md#buildsGetInstance) | **GET** /v1/builds/{id} |  |
| [**buildsIconsGetToManyRelated**](BuildsApi.md#buildsIconsGetToManyRelated) | **GET** /v1/builds/{id}/icons |  |
| [**buildsIndividualTestersCreateToManyRelationship**](BuildsApi.md#buildsIndividualTestersCreateToManyRelationship) | **POST** /v1/builds/{id}/relationships/individualTesters |  |
| [**buildsIndividualTestersDeleteToManyRelationship**](BuildsApi.md#buildsIndividualTestersDeleteToManyRelationship) | **DELETE** /v1/builds/{id}/relationships/individualTesters |  |
| [**buildsIndividualTestersGetToManyRelated**](BuildsApi.md#buildsIndividualTestersGetToManyRelated) | **GET** /v1/builds/{id}/individualTesters |  |
| [**buildsIndividualTestersGetToManyRelationship**](BuildsApi.md#buildsIndividualTestersGetToManyRelationship) | **GET** /v1/builds/{id}/relationships/individualTesters |  |
| [**buildsPerfPowerMetricsGetToManyRelated**](BuildsApi.md#buildsPerfPowerMetricsGetToManyRelated) | **GET** /v1/builds/{id}/perfPowerMetrics |  |
| [**buildsPreReleaseVersionGetToOneRelated**](BuildsApi.md#buildsPreReleaseVersionGetToOneRelated) | **GET** /v1/builds/{id}/preReleaseVersion |  |
| [**buildsUpdateInstance**](BuildsApi.md#buildsUpdateInstance) | **PATCH** /v1/builds/{id} |  |


<a id="buildsAppEncryptionDeclarationGetToOneRelated"></a>
# **buildsAppEncryptionDeclarationGetToOneRelated**
> AppEncryptionDeclarationResponse buildsAppEncryptionDeclarationGetToOneRelated(id, fieldsAppEncryptionDeclarations)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppEncryptionDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appEncryptionDeclarations
    try {
      AppEncryptionDeclarationResponse result = apiInstance.buildsAppEncryptionDeclarationGetToOneRelated(id, fieldsAppEncryptionDeclarations);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsAppEncryptionDeclarationGetToOneRelated");
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
| **fieldsAppEncryptionDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] [enum: app, appEncryptionDeclarationState, availableOnFrenchStore, builds, codeValue, containsProprietaryCryptography, containsThirdPartyCryptography, documentName, documentType, documentUrl, exempt, platform, uploadedDate, usesEncryption] |

### Return type

[**AppEncryptionDeclarationResponse**](AppEncryptionDeclarationResponse.md)

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

<a id="buildsAppEncryptionDeclarationGetToOneRelationship"></a>
# **buildsAppEncryptionDeclarationGetToOneRelationship**
> BuildAppEncryptionDeclarationLinkageResponse buildsAppEncryptionDeclarationGetToOneRelationship(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      BuildAppEncryptionDeclarationLinkageResponse result = apiInstance.buildsAppEncryptionDeclarationGetToOneRelationship(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsAppEncryptionDeclarationGetToOneRelationship");
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

[**BuildAppEncryptionDeclarationLinkageResponse**](BuildAppEncryptionDeclarationLinkageResponse.md)

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

<a id="buildsAppEncryptionDeclarationUpdateToOneRelationship"></a>
# **buildsAppEncryptionDeclarationUpdateToOneRelationship**
> buildsAppEncryptionDeclarationUpdateToOneRelationship(id, buildAppEncryptionDeclarationLinkageRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BuildAppEncryptionDeclarationLinkageRequest buildAppEncryptionDeclarationLinkageRequest = new BuildAppEncryptionDeclarationLinkageRequest(); // BuildAppEncryptionDeclarationLinkageRequest | Related linkage
    try {
      apiInstance.buildsAppEncryptionDeclarationUpdateToOneRelationship(id, buildAppEncryptionDeclarationLinkageRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsAppEncryptionDeclarationUpdateToOneRelationship");
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
| **buildAppEncryptionDeclarationLinkageRequest** | [**BuildAppEncryptionDeclarationLinkageRequest**](BuildAppEncryptionDeclarationLinkageRequest.md)| Related linkage | |

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

<a id="buildsAppGetToOneRelated"></a>
# **buildsAppGetToOneRelated**
> AppResponse buildsAppGetToOneRelated(id, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppResponse result = apiInstance.buildsAppGetToOneRelated(id, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsAppGetToOneRelated");
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
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="buildsAppStoreVersionGetToOneRelated"></a>
# **buildsAppStoreVersionGetToOneRelated**
> AppStoreVersionResponse buildsAppStoreVersionGetToOneRelated(id, fieldsAppStoreVersions)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    try {
      AppStoreVersionResponse result = apiInstance.buildsAppStoreVersionGetToOneRelated(id, fieldsAppStoreVersions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsAppStoreVersionGetToOneRelated");
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
| **200** | Related resource |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="buildsBetaAppReviewSubmissionGetToOneRelated"></a>
# **buildsBetaAppReviewSubmissionGetToOneRelated**
> BetaAppReviewSubmissionResponse buildsBetaAppReviewSubmissionGetToOneRelated(id, fieldsBetaAppReviewSubmissions)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaAppReviewSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewSubmissions
    try {
      BetaAppReviewSubmissionResponse result = apiInstance.buildsBetaAppReviewSubmissionGetToOneRelated(id, fieldsBetaAppReviewSubmissions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsBetaAppReviewSubmissionGetToOneRelated");
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
| **fieldsBetaAppReviewSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] [enum: betaReviewState, build] |

### Return type

[**BetaAppReviewSubmissionResponse**](BetaAppReviewSubmissionResponse.md)

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

<a id="buildsBetaBuildLocalizationsGetToManyRelated"></a>
# **buildsBetaBuildLocalizationsGetToManyRelated**
> BetaBuildLocalizationsResponse buildsBetaBuildLocalizationsGetToManyRelated(id, fieldsBetaBuildLocalizations, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaBuildLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaBuildLocalizations
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaBuildLocalizationsResponse result = apiInstance.buildsBetaBuildLocalizationsGetToManyRelated(id, fieldsBetaBuildLocalizations, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsBetaBuildLocalizationsGetToManyRelated");
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
| **fieldsBetaBuildLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] [enum: build, locale, whatsNew] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaBuildLocalizationsResponse**](BetaBuildLocalizationsResponse.md)

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

<a id="buildsBetaGroupsCreateToManyRelationship"></a>
# **buildsBetaGroupsCreateToManyRelationship**
> buildsBetaGroupsCreateToManyRelationship(id, buildBetaGroupsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BuildBetaGroupsLinkagesRequest buildBetaGroupsLinkagesRequest = new BuildBetaGroupsLinkagesRequest(); // BuildBetaGroupsLinkagesRequest | List of related linkages
    try {
      apiInstance.buildsBetaGroupsCreateToManyRelationship(id, buildBetaGroupsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsBetaGroupsCreateToManyRelationship");
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
| **buildBetaGroupsLinkagesRequest** | [**BuildBetaGroupsLinkagesRequest**](BuildBetaGroupsLinkagesRequest.md)| List of related linkages | |

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

<a id="buildsBetaGroupsDeleteToManyRelationship"></a>
# **buildsBetaGroupsDeleteToManyRelationship**
> buildsBetaGroupsDeleteToManyRelationship(id, buildBetaGroupsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BuildBetaGroupsLinkagesRequest buildBetaGroupsLinkagesRequest = new BuildBetaGroupsLinkagesRequest(); // BuildBetaGroupsLinkagesRequest | List of related linkages
    try {
      apiInstance.buildsBetaGroupsDeleteToManyRelationship(id, buildBetaGroupsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsBetaGroupsDeleteToManyRelationship");
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
| **buildBetaGroupsLinkagesRequest** | [**BuildBetaGroupsLinkagesRequest**](BuildBetaGroupsLinkagesRequest.md)| List of related linkages | |

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

<a id="buildsBuildBetaDetailGetToOneRelated"></a>
# **buildsBuildBetaDetailGetToOneRelated**
> BuildBetaDetailResponse buildsBuildBetaDetailGetToOneRelated(id, fieldsBuildBetaDetails)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuildBetaDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type buildBetaDetails
    try {
      BuildBetaDetailResponse result = apiInstance.buildsBuildBetaDetailGetToOneRelated(id, fieldsBuildBetaDetails);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsBuildBetaDetailGetToOneRelated");
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
| **fieldsBuildBetaDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] [enum: autoNotifyEnabled, build, externalBuildState, internalBuildState] |

### Return type

[**BuildBetaDetailResponse**](BuildBetaDetailResponse.md)

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

<a id="buildsDiagnosticSignaturesGetToManyRelated"></a>
# **buildsDiagnosticSignaturesGetToManyRelated**
> DiagnosticSignaturesResponse buildsDiagnosticSignaturesGetToManyRelated(id, filterDiagnosticType, fieldsDiagnosticSignatures, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterDiagnosticType = Arrays.asList(); // List<String> | filter by attribute 'diagnosticType'
    List<String> fieldsDiagnosticSignatures = Arrays.asList(); // List<String> | the fields to include for returned resources of type diagnosticSignatures
    Integer limit = 56; // Integer | maximum resources per page
    try {
      DiagnosticSignaturesResponse result = apiInstance.buildsDiagnosticSignaturesGetToManyRelated(id, filterDiagnosticType, fieldsDiagnosticSignatures, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsDiagnosticSignaturesGetToManyRelated");
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
| **filterDiagnosticType** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;diagnosticType&#39; | [optional] [enum: DISK_WRITES] |
| **fieldsDiagnosticSignatures** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type diagnosticSignatures | [optional] [enum: diagnosticType, logs, signature, weight] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**DiagnosticSignaturesResponse**](DiagnosticSignaturesResponse.md)

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

<a id="buildsGetCollection"></a>
# **buildsGetCollection**
> BuildsResponse buildsGetCollection(filterBetaAppReviewSubmissionBetaReviewState, filterExpired, filterPreReleaseVersionPlatform, filterPreReleaseVersionVersion, filterProcessingState, filterUsesNonExemptEncryption, filterVersion, filterApp, filterAppStoreVersion, filterBetaGroups, filterPreReleaseVersion, filterId, sort, fieldsBuilds, limit, include, fieldsAppEncryptionDeclarations, fieldsBetaAppReviewSubmissions, fieldsBuildBetaDetails, fieldsBuildIcons, fieldsPerfPowerMetrics, fieldsPreReleaseVersions, fieldsAppStoreVersions, fieldsDiagnosticSignatures, fieldsBetaTesters, fieldsBetaBuildLocalizations, fieldsApps, limitBetaBuildLocalizations, limitIcons, limitIndividualTesters)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    List<String> filterBetaAppReviewSubmissionBetaReviewState = Arrays.asList(); // List<String> | filter by attribute 'betaAppReviewSubmission.betaReviewState'
    List<String> filterExpired = Arrays.asList(); // List<String> | filter by attribute 'expired'
    List<String> filterPreReleaseVersionPlatform = Arrays.asList(); // List<String> | filter by attribute 'preReleaseVersion.platform'
    List<String> filterPreReleaseVersionVersion = Arrays.asList(); // List<String> | filter by attribute 'preReleaseVersion.version'
    List<String> filterProcessingState = Arrays.asList(); // List<String> | filter by attribute 'processingState'
    List<String> filterUsesNonExemptEncryption = Arrays.asList(); // List<String> | filter by attribute 'usesNonExemptEncryption'
    List<String> filterVersion = Arrays.asList(); // List<String> | filter by attribute 'version'
    List<String> filterApp = Arrays.asList(); // List<String> | filter by id(s) of related 'app'
    List<String> filterAppStoreVersion = Arrays.asList(); // List<String> | filter by id(s) of related 'appStoreVersion'
    List<String> filterBetaGroups = Arrays.asList(); // List<String> | filter by id(s) of related 'betaGroups'
    List<String> filterPreReleaseVersion = Arrays.asList(); // List<String> | filter by id(s) of related 'preReleaseVersion'
    List<String> filterId = Arrays.asList(); // List<String> | filter by id(s)
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppEncryptionDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appEncryptionDeclarations
    List<String> fieldsBetaAppReviewSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewSubmissions
    List<String> fieldsBuildBetaDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type buildBetaDetails
    List<String> fieldsBuildIcons = Arrays.asList(); // List<String> | the fields to include for returned resources of type buildIcons
    List<String> fieldsPerfPowerMetrics = Arrays.asList(); // List<String> | the fields to include for returned resources of type perfPowerMetrics
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsDiagnosticSignatures = Arrays.asList(); // List<String> | the fields to include for returned resources of type diagnosticSignatures
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    List<String> fieldsBetaBuildLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaBuildLocalizations
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitBetaBuildLocalizations = 56; // Integer | maximum number of related betaBuildLocalizations returned (when they are included)
    Integer limitIcons = 56; // Integer | maximum number of related icons returned (when they are included)
    Integer limitIndividualTesters = 56; // Integer | maximum number of related individualTesters returned (when they are included)
    try {
      BuildsResponse result = apiInstance.buildsGetCollection(filterBetaAppReviewSubmissionBetaReviewState, filterExpired, filterPreReleaseVersionPlatform, filterPreReleaseVersionVersion, filterProcessingState, filterUsesNonExemptEncryption, filterVersion, filterApp, filterAppStoreVersion, filterBetaGroups, filterPreReleaseVersion, filterId, sort, fieldsBuilds, limit, include, fieldsAppEncryptionDeclarations, fieldsBetaAppReviewSubmissions, fieldsBuildBetaDetails, fieldsBuildIcons, fieldsPerfPowerMetrics, fieldsPreReleaseVersions, fieldsAppStoreVersions, fieldsDiagnosticSignatures, fieldsBetaTesters, fieldsBetaBuildLocalizations, fieldsApps, limitBetaBuildLocalizations, limitIcons, limitIndividualTesters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsGetCollection");
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
| **filterBetaAppReviewSubmissionBetaReviewState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;betaAppReviewSubmission.betaReviewState&#39; | [optional] [enum: WAITING_FOR_REVIEW, IN_REVIEW, REJECTED, APPROVED] |
| **filterExpired** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;expired&#39; | [optional] |
| **filterPreReleaseVersionPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;preReleaseVersion.platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterPreReleaseVersionVersion** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;preReleaseVersion.version&#39; | [optional] |
| **filterProcessingState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;processingState&#39; | [optional] [enum: PROCESSING, FAILED, INVALID, VALID] |
| **filterUsesNonExemptEncryption** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;usesNonExemptEncryption&#39; | [optional] |
| **filterVersion** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;version&#39; | [optional] |
| **filterApp** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] |
| **filterAppStoreVersion** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;appStoreVersion&#39; | [optional] |
| **filterBetaGroups** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;betaGroups&#39; | [optional] |
| **filterPreReleaseVersion** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;preReleaseVersion&#39; | [optional] |
| **filterId** | [**List&lt;String&gt;**](String.md)| filter by id(s) | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: preReleaseVersion, -preReleaseVersion, uploadedDate, -uploadedDate, version, -version] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, buildBetaDetail, icons, individualTesters, preReleaseVersion] |
| **fieldsAppEncryptionDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] [enum: app, appEncryptionDeclarationState, availableOnFrenchStore, builds, codeValue, containsProprietaryCryptography, containsThirdPartyCryptography, documentName, documentType, documentUrl, exempt, platform, uploadedDate, usesEncryption] |
| **fieldsBetaAppReviewSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] [enum: betaReviewState, build] |
| **fieldsBuildBetaDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] [enum: autoNotifyEnabled, build, externalBuildState, internalBuildState] |
| **fieldsBuildIcons** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type buildIcons | [optional] [enum: iconAsset, iconType] |
| **fieldsPerfPowerMetrics** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] [enum: deviceType, metricType, platform] |
| **fieldsPreReleaseVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] [enum: app, builds, platform, version] |
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsDiagnosticSignatures** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type diagnosticSignatures | [optional] [enum: diagnosticType, logs, signature, weight] |
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **fieldsBetaBuildLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] [enum: build, locale, whatsNew] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitBetaBuildLocalizations** | **Integer**| maximum number of related betaBuildLocalizations returned (when they are included) | [optional] |
| **limitIcons** | **Integer**| maximum number of related icons returned (when they are included) | [optional] |
| **limitIndividualTesters** | **Integer**| maximum number of related individualTesters returned (when they are included) | [optional] |

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
| **200** | List of Builds |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="buildsGetInstance"></a>
# **buildsGetInstance**
> BuildResponse buildsGetInstance(id, fieldsBuilds, include, fieldsAppEncryptionDeclarations, fieldsBetaAppReviewSubmissions, fieldsBuildBetaDetails, fieldsBuildIcons, fieldsPerfPowerMetrics, fieldsPreReleaseVersions, fieldsAppStoreVersions, fieldsDiagnosticSignatures, fieldsBetaTesters, fieldsBetaBuildLocalizations, fieldsApps, limitBetaBuildLocalizations, limitIcons, limitIndividualTesters)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsAppEncryptionDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appEncryptionDeclarations
    List<String> fieldsBetaAppReviewSubmissions = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppReviewSubmissions
    List<String> fieldsBuildBetaDetails = Arrays.asList(); // List<String> | the fields to include for returned resources of type buildBetaDetails
    List<String> fieldsBuildIcons = Arrays.asList(); // List<String> | the fields to include for returned resources of type buildIcons
    List<String> fieldsPerfPowerMetrics = Arrays.asList(); // List<String> | the fields to include for returned resources of type perfPowerMetrics
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    List<String> fieldsAppStoreVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type appStoreVersions
    List<String> fieldsDiagnosticSignatures = Arrays.asList(); // List<String> | the fields to include for returned resources of type diagnosticSignatures
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    List<String> fieldsBetaBuildLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaBuildLocalizations
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitBetaBuildLocalizations = 56; // Integer | maximum number of related betaBuildLocalizations returned (when they are included)
    Integer limitIcons = 56; // Integer | maximum number of related icons returned (when they are included)
    Integer limitIndividualTesters = 56; // Integer | maximum number of related individualTesters returned (when they are included)
    try {
      BuildResponse result = apiInstance.buildsGetInstance(id, fieldsBuilds, include, fieldsAppEncryptionDeclarations, fieldsBetaAppReviewSubmissions, fieldsBuildBetaDetails, fieldsBuildIcons, fieldsPerfPowerMetrics, fieldsPreReleaseVersions, fieldsAppStoreVersions, fieldsDiagnosticSignatures, fieldsBetaTesters, fieldsBetaBuildLocalizations, fieldsApps, limitBetaBuildLocalizations, limitIcons, limitIndividualTesters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, buildBetaDetail, icons, individualTesters, preReleaseVersion] |
| **fieldsAppEncryptionDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] [enum: app, appEncryptionDeclarationState, availableOnFrenchStore, builds, codeValue, containsProprietaryCryptography, containsThirdPartyCryptography, documentName, documentType, documentUrl, exempt, platform, uploadedDate, usesEncryption] |
| **fieldsBetaAppReviewSubmissions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppReviewSubmissions | [optional] [enum: betaReviewState, build] |
| **fieldsBuildBetaDetails** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type buildBetaDetails | [optional] [enum: autoNotifyEnabled, build, externalBuildState, internalBuildState] |
| **fieldsBuildIcons** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type buildIcons | [optional] [enum: iconAsset, iconType] |
| **fieldsPerfPowerMetrics** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type perfPowerMetrics | [optional] [enum: deviceType, metricType, platform] |
| **fieldsPreReleaseVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] [enum: app, builds, platform, version] |
| **fieldsAppStoreVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appStoreVersions | [optional] [enum: ageRatingDeclaration, app, appStoreReviewDetail, appStoreState, appStoreVersionLocalizations, appStoreVersionPhasedRelease, appStoreVersionSubmission, build, copyright, createdDate, downloadable, earliestReleaseDate, idfaDeclaration, platform, releaseType, routingAppCoverage, usesIdfa, versionString] |
| **fieldsDiagnosticSignatures** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type diagnosticSignatures | [optional] [enum: diagnosticType, logs, signature, weight] |
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **fieldsBetaBuildLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] [enum: build, locale, whatsNew] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitBetaBuildLocalizations** | **Integer**| maximum number of related betaBuildLocalizations returned (when they are included) | [optional] |
| **limitIcons** | **Integer**| maximum number of related icons returned (when they are included) | [optional] |
| **limitIndividualTesters** | **Integer**| maximum number of related individualTesters returned (when they are included) | [optional] |

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
| **200** | Single Build |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="buildsIconsGetToManyRelated"></a>
# **buildsIconsGetToManyRelated**
> BuildIconsResponse buildsIconsGetToManyRelated(id, fieldsBuildIcons, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuildIcons = Arrays.asList(); // List<String> | the fields to include for returned resources of type buildIcons
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BuildIconsResponse result = apiInstance.buildsIconsGetToManyRelated(id, fieldsBuildIcons, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsIconsGetToManyRelated");
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
| **fieldsBuildIcons** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type buildIcons | [optional] [enum: iconAsset, iconType] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BuildIconsResponse**](BuildIconsResponse.md)

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

<a id="buildsIndividualTestersCreateToManyRelationship"></a>
# **buildsIndividualTestersCreateToManyRelationship**
> buildsIndividualTestersCreateToManyRelationship(id, buildIndividualTestersLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BuildIndividualTestersLinkagesRequest buildIndividualTestersLinkagesRequest = new BuildIndividualTestersLinkagesRequest(); // BuildIndividualTestersLinkagesRequest | List of related linkages
    try {
      apiInstance.buildsIndividualTestersCreateToManyRelationship(id, buildIndividualTestersLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsIndividualTestersCreateToManyRelationship");
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
| **buildIndividualTestersLinkagesRequest** | [**BuildIndividualTestersLinkagesRequest**](BuildIndividualTestersLinkagesRequest.md)| List of related linkages | |

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

<a id="buildsIndividualTestersDeleteToManyRelationship"></a>
# **buildsIndividualTestersDeleteToManyRelationship**
> buildsIndividualTestersDeleteToManyRelationship(id, buildIndividualTestersLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BuildIndividualTestersLinkagesRequest buildIndividualTestersLinkagesRequest = new BuildIndividualTestersLinkagesRequest(); // BuildIndividualTestersLinkagesRequest | List of related linkages
    try {
      apiInstance.buildsIndividualTestersDeleteToManyRelationship(id, buildIndividualTestersLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsIndividualTestersDeleteToManyRelationship");
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
| **buildIndividualTestersLinkagesRequest** | [**BuildIndividualTestersLinkagesRequest**](BuildIndividualTestersLinkagesRequest.md)| List of related linkages | |

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

<a id="buildsIndividualTestersGetToManyRelated"></a>
# **buildsIndividualTestersGetToManyRelated**
> BetaTestersResponse buildsIndividualTestersGetToManyRelated(id, fieldsBetaTesters, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaTesters = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaTesters
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BetaTestersResponse result = apiInstance.buildsIndividualTestersGetToManyRelated(id, fieldsBetaTesters, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsIndividualTestersGetToManyRelated");
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
| **fieldsBetaTesters** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaTesters | [optional] [enum: apps, betaGroups, builds, email, firstName, inviteType, lastName] |
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BetaTestersResponse**](BetaTestersResponse.md)

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

<a id="buildsIndividualTestersGetToManyRelationship"></a>
# **buildsIndividualTestersGetToManyRelationship**
> BuildIndividualTestersLinkagesResponse buildsIndividualTestersGetToManyRelationship(id, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BuildIndividualTestersLinkagesResponse result = apiInstance.buildsIndividualTestersGetToManyRelationship(id, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsIndividualTestersGetToManyRelationship");
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
| **limit** | **Integer**| maximum resources per page | [optional] |

### Return type

[**BuildIndividualTestersLinkagesResponse**](BuildIndividualTestersLinkagesResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of related linkages |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="buildsPerfPowerMetricsGetToManyRelated"></a>
# **buildsPerfPowerMetricsGetToManyRelated**
> PerfPowerMetricsResponse buildsPerfPowerMetricsGetToManyRelated(id, filterDeviceType, filterMetricType, filterPlatform)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> filterDeviceType = Arrays.asList(); // List<String> | filter by attribute 'deviceType'
    List<String> filterMetricType = Arrays.asList(); // List<String> | filter by attribute 'metricType'
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    try {
      PerfPowerMetricsResponse result = apiInstance.buildsPerfPowerMetricsGetToManyRelated(id, filterDeviceType, filterMetricType, filterPlatform);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsPerfPowerMetricsGetToManyRelated");
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

<a id="buildsPreReleaseVersionGetToOneRelated"></a>
# **buildsPreReleaseVersionGetToOneRelated**
> PrereleaseVersionResponse buildsPreReleaseVersionGetToOneRelated(id, fieldsPreReleaseVersions)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    try {
      PrereleaseVersionResponse result = apiInstance.buildsPreReleaseVersionGetToOneRelated(id, fieldsPreReleaseVersions);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsPreReleaseVersionGetToOneRelated");
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

### Return type

[**PrereleaseVersionResponse**](PrereleaseVersionResponse.md)

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

<a id="buildsUpdateInstance"></a>
# **buildsUpdateInstance**
> BuildResponse buildsUpdateInstance(id, buildUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BuildsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BuildsApi apiInstance = new BuildsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BuildUpdateRequest buildUpdateRequest = new BuildUpdateRequest(); // BuildUpdateRequest | Build representation
    try {
      BuildResponse result = apiInstance.buildsUpdateInstance(id, buildUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BuildsApi#buildsUpdateInstance");
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
| **buildUpdateRequest** | [**BuildUpdateRequest**](BuildUpdateRequest.md)| Build representation | |

### Return type

[**BuildResponse**](BuildResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single Build |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

