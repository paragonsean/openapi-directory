# AppEncryptionDeclarationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appEncryptionDeclarationsAppGetToOneRelated**](AppEncryptionDeclarationsApi.md#appEncryptionDeclarationsAppGetToOneRelated) | **GET** /v1/appEncryptionDeclarations/{id}/app |  |
| [**appEncryptionDeclarationsBuildsCreateToManyRelationship**](AppEncryptionDeclarationsApi.md#appEncryptionDeclarationsBuildsCreateToManyRelationship) | **POST** /v1/appEncryptionDeclarations/{id}/relationships/builds |  |
| [**appEncryptionDeclarationsGetCollection**](AppEncryptionDeclarationsApi.md#appEncryptionDeclarationsGetCollection) | **GET** /v1/appEncryptionDeclarations |  |
| [**appEncryptionDeclarationsGetInstance**](AppEncryptionDeclarationsApi.md#appEncryptionDeclarationsGetInstance) | **GET** /v1/appEncryptionDeclarations/{id} |  |


<a id="appEncryptionDeclarationsAppGetToOneRelated"></a>
# **appEncryptionDeclarationsAppGetToOneRelated**
> AppResponse appEncryptionDeclarationsAppGetToOneRelated(id, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppEncryptionDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppEncryptionDeclarationsApi apiInstance = new AppEncryptionDeclarationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppResponse result = apiInstance.appEncryptionDeclarationsAppGetToOneRelated(id, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppEncryptionDeclarationsApi#appEncryptionDeclarationsAppGetToOneRelated");
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

<a id="appEncryptionDeclarationsBuildsCreateToManyRelationship"></a>
# **appEncryptionDeclarationsBuildsCreateToManyRelationship**
> appEncryptionDeclarationsBuildsCreateToManyRelationship(id, appEncryptionDeclarationBuildsLinkagesRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppEncryptionDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppEncryptionDeclarationsApi apiInstance = new AppEncryptionDeclarationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppEncryptionDeclarationBuildsLinkagesRequest appEncryptionDeclarationBuildsLinkagesRequest = new AppEncryptionDeclarationBuildsLinkagesRequest(); // AppEncryptionDeclarationBuildsLinkagesRequest | List of related linkages
    try {
      apiInstance.appEncryptionDeclarationsBuildsCreateToManyRelationship(id, appEncryptionDeclarationBuildsLinkagesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppEncryptionDeclarationsApi#appEncryptionDeclarationsBuildsCreateToManyRelationship");
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
| **appEncryptionDeclarationBuildsLinkagesRequest** | [**AppEncryptionDeclarationBuildsLinkagesRequest**](AppEncryptionDeclarationBuildsLinkagesRequest.md)| List of related linkages | |

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

<a id="appEncryptionDeclarationsGetCollection"></a>
# **appEncryptionDeclarationsGetCollection**
> AppEncryptionDeclarationsResponse appEncryptionDeclarationsGetCollection(filterPlatform, filterApp, filterBuilds, fieldsAppEncryptionDeclarations, limit, include, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppEncryptionDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppEncryptionDeclarationsApi apiInstance = new AppEncryptionDeclarationsApi(defaultClient);
    List<String> filterPlatform = Arrays.asList(); // List<String> | filter by attribute 'platform'
    List<String> filterApp = Arrays.asList(); // List<String> | filter by id(s) of related 'app'
    List<String> filterBuilds = Arrays.asList(); // List<String> | filter by id(s) of related 'builds'
    List<String> fieldsAppEncryptionDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appEncryptionDeclarations
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppEncryptionDeclarationsResponse result = apiInstance.appEncryptionDeclarationsGetCollection(filterPlatform, filterApp, filterBuilds, fieldsAppEncryptionDeclarations, limit, include, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppEncryptionDeclarationsApi#appEncryptionDeclarationsGetCollection");
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
| **filterPlatform** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;platform&#39; | [optional] [enum: IOS, MAC_OS, TV_OS] |
| **filterApp** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] |
| **filterBuilds** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;builds&#39; | [optional] |
| **fieldsAppEncryptionDeclarations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appEncryptionDeclarations | [optional] [enum: app, appEncryptionDeclarationState, availableOnFrenchStore, builds, codeValue, containsProprietaryCryptography, containsThirdPartyCryptography, documentName, documentType, documentUrl, exempt, platform, uploadedDate, usesEncryption] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |

### Return type

[**AppEncryptionDeclarationsResponse**](AppEncryptionDeclarationsResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of AppEncryptionDeclarations |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="appEncryptionDeclarationsGetInstance"></a>
# **appEncryptionDeclarationsGetInstance**
> AppEncryptionDeclarationResponse appEncryptionDeclarationsGetInstance(id, fieldsAppEncryptionDeclarations, include, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppEncryptionDeclarationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppEncryptionDeclarationsApi apiInstance = new AppEncryptionDeclarationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppEncryptionDeclarations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appEncryptionDeclarations
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppEncryptionDeclarationResponse result = apiInstance.appEncryptionDeclarationsGetInstance(id, fieldsAppEncryptionDeclarations, include, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppEncryptionDeclarationsApi#appEncryptionDeclarationsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |

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
| **200** | Single AppEncryptionDeclaration |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

