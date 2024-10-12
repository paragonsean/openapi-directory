# BetaAppLocalizationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaAppLocalizationsAppGetToOneRelated**](BetaAppLocalizationsApi.md#betaAppLocalizationsAppGetToOneRelated) | **GET** /v1/betaAppLocalizations/{id}/app |  |
| [**betaAppLocalizationsCreateInstance**](BetaAppLocalizationsApi.md#betaAppLocalizationsCreateInstance) | **POST** /v1/betaAppLocalizations |  |
| [**betaAppLocalizationsDeleteInstance**](BetaAppLocalizationsApi.md#betaAppLocalizationsDeleteInstance) | **DELETE** /v1/betaAppLocalizations/{id} |  |
| [**betaAppLocalizationsGetCollection**](BetaAppLocalizationsApi.md#betaAppLocalizationsGetCollection) | **GET** /v1/betaAppLocalizations |  |
| [**betaAppLocalizationsGetInstance**](BetaAppLocalizationsApi.md#betaAppLocalizationsGetInstance) | **GET** /v1/betaAppLocalizations/{id} |  |
| [**betaAppLocalizationsUpdateInstance**](BetaAppLocalizationsApi.md#betaAppLocalizationsUpdateInstance) | **PATCH** /v1/betaAppLocalizations/{id} |  |


<a id="betaAppLocalizationsAppGetToOneRelated"></a>
# **betaAppLocalizationsAppGetToOneRelated**
> AppResponse betaAppLocalizationsAppGetToOneRelated(id, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppLocalizationsApi apiInstance = new BetaAppLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      AppResponse result = apiInstance.betaAppLocalizationsAppGetToOneRelated(id, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppLocalizationsApi#betaAppLocalizationsAppGetToOneRelated");
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

<a id="betaAppLocalizationsCreateInstance"></a>
# **betaAppLocalizationsCreateInstance**
> BetaAppLocalizationResponse betaAppLocalizationsCreateInstance(betaAppLocalizationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppLocalizationsApi apiInstance = new BetaAppLocalizationsApi(defaultClient);
    BetaAppLocalizationCreateRequest betaAppLocalizationCreateRequest = new BetaAppLocalizationCreateRequest(); // BetaAppLocalizationCreateRequest | BetaAppLocalization representation
    try {
      BetaAppLocalizationResponse result = apiInstance.betaAppLocalizationsCreateInstance(betaAppLocalizationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppLocalizationsApi#betaAppLocalizationsCreateInstance");
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
| **betaAppLocalizationCreateRequest** | [**BetaAppLocalizationCreateRequest**](BetaAppLocalizationCreateRequest.md)| BetaAppLocalization representation | |

### Return type

[**BetaAppLocalizationResponse**](BetaAppLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BetaAppLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaAppLocalizationsDeleteInstance"></a>
# **betaAppLocalizationsDeleteInstance**
> betaAppLocalizationsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppLocalizationsApi apiInstance = new BetaAppLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.betaAppLocalizationsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppLocalizationsApi#betaAppLocalizationsDeleteInstance");
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

<a id="betaAppLocalizationsGetCollection"></a>
# **betaAppLocalizationsGetCollection**
> BetaAppLocalizationsResponse betaAppLocalizationsGetCollection(filterLocale, filterApp, fieldsBetaAppLocalizations, limit, include, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppLocalizationsApi apiInstance = new BetaAppLocalizationsApi(defaultClient);
    List<String> filterLocale = Arrays.asList(); // List<String> | filter by attribute 'locale'
    List<String> filterApp = Arrays.asList(); // List<String> | filter by id(s) of related 'app'
    List<String> fieldsBetaAppLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppLocalizations
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      BetaAppLocalizationsResponse result = apiInstance.betaAppLocalizationsGetCollection(filterLocale, filterApp, fieldsBetaAppLocalizations, limit, include, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppLocalizationsApi#betaAppLocalizationsGetCollection");
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
| **filterLocale** | [**List&lt;String&gt;**](String.md)| filter by attribute &#39;locale&#39; | [optional] |
| **filterApp** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;app&#39; | [optional] |
| **fieldsBetaAppLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaAppLocalizations | [optional] [enum: app, description, feedbackEmail, locale, marketingUrl, privacyPolicyUrl, tvOsPrivacyPolicy] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |

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
| **200** | List of BetaAppLocalizations |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="betaAppLocalizationsGetInstance"></a>
# **betaAppLocalizationsGetInstance**
> BetaAppLocalizationResponse betaAppLocalizationsGetInstance(id, fieldsBetaAppLocalizations, include, fieldsApps)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppLocalizationsApi apiInstance = new BetaAppLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaAppLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaAppLocalizations
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsApps = Arrays.asList(); // List<String> | the fields to include for returned resources of type apps
    try {
      BetaAppLocalizationResponse result = apiInstance.betaAppLocalizationsGetInstance(id, fieldsBetaAppLocalizations, include, fieldsApps);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppLocalizationsApi#betaAppLocalizationsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: app] |
| **fieldsApps** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type apps | [optional] [enum: appInfos, appStoreVersions, availableInNewTerritories, availableTerritories, betaAppLocalizations, betaAppReviewDetail, betaGroups, betaLicenseAgreement, betaTesters, builds, bundleId, contentRightsDeclaration, endUserLicenseAgreement, gameCenterEnabledVersions, inAppPurchases, isOrEverWasMadeForKids, name, perfPowerMetrics, preOrder, preReleaseVersions, prices, primaryLocale, sku] |

### Return type

[**BetaAppLocalizationResponse**](BetaAppLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaAppLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaAppLocalizationsUpdateInstance"></a>
# **betaAppLocalizationsUpdateInstance**
> BetaAppLocalizationResponse betaAppLocalizationsUpdateInstance(id, betaAppLocalizationUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaAppLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaAppLocalizationsApi apiInstance = new BetaAppLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaAppLocalizationUpdateRequest betaAppLocalizationUpdateRequest = new BetaAppLocalizationUpdateRequest(); // BetaAppLocalizationUpdateRequest | BetaAppLocalization representation
    try {
      BetaAppLocalizationResponse result = apiInstance.betaAppLocalizationsUpdateInstance(id, betaAppLocalizationUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaAppLocalizationsApi#betaAppLocalizationsUpdateInstance");
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
| **betaAppLocalizationUpdateRequest** | [**BetaAppLocalizationUpdateRequest**](BetaAppLocalizationUpdateRequest.md)| BetaAppLocalization representation | |

### Return type

[**BetaAppLocalizationResponse**](BetaAppLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaAppLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

