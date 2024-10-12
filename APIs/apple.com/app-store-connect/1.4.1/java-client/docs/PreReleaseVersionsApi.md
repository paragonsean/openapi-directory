# PreReleaseVersionsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**preReleaseVersionsAppGetToOneRelated**](PreReleaseVersionsApi.md#preReleaseVersionsAppGetToOneRelated) | **GET** /v1/preReleaseVersions/{id}/app |  |
| [**preReleaseVersionsBuildsGetToManyRelated**](PreReleaseVersionsApi.md#preReleaseVersionsBuildsGetToManyRelated) | **GET** /v1/preReleaseVersions/{id}/builds |  |
| [**preReleaseVersionsGetCollection**](PreReleaseVersionsApi.md#preReleaseVersionsGetCollection) | **GET** /v1/preReleaseVersions |  |
| [**preReleaseVersionsGetInstance**](PreReleaseVersionsApi.md#preReleaseVersionsGetInstance) | **GET** /v1/preReleaseVersions/{id} |  |


<a id="preReleaseVersionsAppGetToOneRelated"></a>
# **preReleaseVersionsAppGetToOneRelated**
> AppResponse preReleaseVersionsAppGetToOneRelated(id, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreReleaseVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    PreReleaseVersionsApi apiInstance = new PreReleaseVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppResponse result = apiInstance.preReleaseVersionsAppGetToOneRelated(id, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreReleaseVersionsApi#preReleaseVersionsAppGetToOneRelated");
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

<a id="preReleaseVersionsBuildsGetToManyRelated"></a>
# **preReleaseVersionsBuildsGetToManyRelated**
> BuildsResponse preReleaseVersionsBuildsGetToManyRelated(id, fieldsBuilds, limit)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreReleaseVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    PreReleaseVersionsApi apiInstance = new PreReleaseVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    Integer limit = 56; // Integer | maximum resources per page
    try {
      BuildsResponse result = apiInstance.preReleaseVersionsBuildsGetToManyRelated(id, fieldsBuilds, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreReleaseVersionsApi#preReleaseVersionsBuildsGetToManyRelated");
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

<a id="preReleaseVersionsGetCollection"></a>
# **preReleaseVersionsGetCollection**
> PreReleaseVersionsResponse preReleaseVersionsGetCollection(filterBuildsExpired, filterBuildsProcessingState, filterPlatform, filterVersion, filterApp, filterBuilds, sort, fieldsPreReleaseVersions, limit, include, fieldsBuilds, fieldsApps, limitBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreReleaseVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    PreReleaseVersionsApi apiInstance = new PreReleaseVersionsApi(defaultClient);
    List<String> filterBuildsExpired = Arrays.asList(); // List<String> | filter by attribute 'builds.expired'
    List<String> filterBuildsProcessingState = Arrays.asList(); // List<String> | filter by attribute 'builds.processingState'
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    List<String> filterVersion = Arrays.asList(); // List<String> | filter by attribute 'version'
    List<String> filterApp = Arrays.asList(); // List<String> | filter by id(s) of related 'app'
    List<String> filterBuilds = Arrays.asList(); // List<String> | filter by id(s) of related 'builds'
    List<String> sort = Arrays.asList(); // List<String> | comma-separated list of sort expressions; resources will be sorted as specified
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    try {
      PreReleaseVersionsResponse result = apiInstance.preReleaseVersionsGetCollection(filterBuildsExpired, filterBuildsProcessingState, filterPlatform, filterVersion, filterApp, filterBuilds, sort, fieldsPreReleaseVersions, limit, include, fieldsBuilds, fieldsApps, limitBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreReleaseVersionsApi#preReleaseVersionsGetCollection");
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
| **filterBuildsExpired** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;builds.expired&#39; | [optional] |
| **filterBuildsProcessingState** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;builds.processingState&#39; | [optional] [enum: PROCESSING, FAILED, INVALID, VALID] |
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterVersion** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;version&#39; | [optional] |
| **filterApp** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] |
| **filterBuilds** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;builds&#39; | [optional] |
| **sort** | [**List&lt;String&gt;**](String.md)| comma-separated list of sort expressions; resources will be sorted as specified | [optional] [enum: version, -version] |
| **fieldsPreReleaseVersions** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type preReleaseVersions | [optional] [enum: app, builds, platform, version] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, builds] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |

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
| **200** | List of PreReleaseVersions |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="preReleaseVersionsGetInstance"></a>
# **preReleaseVersionsGetInstance**
> PrereleaseVersionResponse preReleaseVersionsGetInstance(id, fieldsPreReleaseVersions, include, fieldsBuilds, fieldsApps, limitBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PreReleaseVersionsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    PreReleaseVersionsApi apiInstance = new PreReleaseVersionsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsPreReleaseVersions = Arrays.asList(); // List<String> | the fields to include for returned resources of type preReleaseVersions
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    Integer limitBuilds = 56; // Integer | maximum number of related builds returned (when they are included)
    try {
      PrereleaseVersionResponse result = apiInstance.preReleaseVersionsGetInstance(id, fieldsPreReleaseVersions, include, fieldsBuilds, fieldsApps, limitBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PreReleaseVersionsApi#preReleaseVersionsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app, builds] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |
| **limitBuilds** | **Integer**| maximum number of related builds returned (when they are included) | [optional] |

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
| **200** | Single PrereleaseVersion |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

