# BetaBuildLocalizationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**betaBuildLocalizationsBuildGetToOneRelated**](BetaBuildLocalizationsApi.md#betaBuildLocalizationsBuildGetToOneRelated) | **GET** /v1/betaBuildLocalizations/{id}/build |  |
| [**betaBuildLocalizationsCreateInstance**](BetaBuildLocalizationsApi.md#betaBuildLocalizationsCreateInstance) | **POST** /v1/betaBuildLocalizations |  |
| [**betaBuildLocalizationsDeleteInstance**](BetaBuildLocalizationsApi.md#betaBuildLocalizationsDeleteInstance) | **DELETE** /v1/betaBuildLocalizations/{id} |  |
| [**betaBuildLocalizationsGetCollection**](BetaBuildLocalizationsApi.md#betaBuildLocalizationsGetCollection) | **GET** /v1/betaBuildLocalizations |  |
| [**betaBuildLocalizationsGetInstance**](BetaBuildLocalizationsApi.md#betaBuildLocalizationsGetInstance) | **GET** /v1/betaBuildLocalizations/{id} |  |
| [**betaBuildLocalizationsUpdateInstance**](BetaBuildLocalizationsApi.md#betaBuildLocalizationsUpdateInstance) | **PATCH** /v1/betaBuildLocalizations/{id} |  |


<a id="betaBuildLocalizationsBuildGetToOneRelated"></a>
# **betaBuildLocalizationsBuildGetToOneRelated**
> BuildResponse betaBuildLocalizationsBuildGetToOneRelated(id, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaBuildLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaBuildLocalizationsApi apiInstance = new BetaBuildLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BuildResponse result = apiInstance.betaBuildLocalizationsBuildGetToOneRelated(id, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaBuildLocalizationsApi#betaBuildLocalizationsBuildGetToOneRelated");
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

<a id="betaBuildLocalizationsCreateInstance"></a>
# **betaBuildLocalizationsCreateInstance**
> BetaBuildLocalizationResponse betaBuildLocalizationsCreateInstance(betaBuildLocalizationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaBuildLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaBuildLocalizationsApi apiInstance = new BetaBuildLocalizationsApi(defaultClient);
    BetaBuildLocalizationCreateRequest betaBuildLocalizationCreateRequest = new BetaBuildLocalizationCreateRequest(); // BetaBuildLocalizationCreateRequest | BetaBuildLocalization representation
    try {
      BetaBuildLocalizationResponse result = apiInstance.betaBuildLocalizationsCreateInstance(betaBuildLocalizationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaBuildLocalizationsApi#betaBuildLocalizationsCreateInstance");
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
| **betaBuildLocalizationCreateRequest** | [**BetaBuildLocalizationCreateRequest**](BetaBuildLocalizationCreateRequest.md)| BetaBuildLocalization representation | |

### Return type

[**BetaBuildLocalizationResponse**](BetaBuildLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single BetaBuildLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="betaBuildLocalizationsDeleteInstance"></a>
# **betaBuildLocalizationsDeleteInstance**
> betaBuildLocalizationsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaBuildLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaBuildLocalizationsApi apiInstance = new BetaBuildLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.betaBuildLocalizationsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaBuildLocalizationsApi#betaBuildLocalizationsDeleteInstance");
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

<a id="betaBuildLocalizationsGetCollection"></a>
# **betaBuildLocalizationsGetCollection**
> BetaBuildLocalizationsResponse betaBuildLocalizationsGetCollection(filterLocale, filterBuild, fieldsBetaBuildLocalizations, limit, include, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaBuildLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaBuildLocalizationsApi apiInstance = new BetaBuildLocalizationsApi(defaultClient);
    List<String> filterLocale = Arrays.asList(); // List<String> | filter by attribute 'locale'
    List<String> filterBuild = Arrays.asList(); // List<String> | filter by id(s) of related 'build'
    List<String> fieldsBetaBuildLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaBuildLocalizations
    Integer limit = 56; // Integer | maximum resources per page
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BetaBuildLocalizationsResponse result = apiInstance.betaBuildLocalizationsGetCollection(filterLocale, filterBuild, fieldsBetaBuildLocalizations, limit, include, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaBuildLocalizationsApi#betaBuildLocalizationsGetCollection");
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
| **filterBuild** | [**List&lt;String&gt;**](String.md)| filter by id(s) of related &#39;build&#39; | [optional] |
| **fieldsBetaBuildLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type betaBuildLocalizations | [optional] [enum: build, locale, whatsNew] |
| **limit** | **Integer**| maximum resources per page | [optional] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: build] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |

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
| **200** | List of BetaBuildLocalizations |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |

<a id="betaBuildLocalizationsGetInstance"></a>
# **betaBuildLocalizationsGetInstance**
> BetaBuildLocalizationResponse betaBuildLocalizationsGetInstance(id, fieldsBetaBuildLocalizations, include, fieldsBuilds)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaBuildLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaBuildLocalizationsApi apiInstance = new BetaBuildLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsBetaBuildLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type betaBuildLocalizations
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    List<String> fieldsBuilds = Arrays.asList(); // List<String> | the fields to include for returned resources of type builds
    try {
      BetaBuildLocalizationResponse result = apiInstance.betaBuildLocalizationsGetInstance(id, fieldsBetaBuildLocalizations, include, fieldsBuilds);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaBuildLocalizationsApi#betaBuildLocalizationsGetInstance");
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
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: build] |
| **fieldsBuilds** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type builds | [optional] [enum: app, appEncryptionDeclaration, appStoreVersion, betaAppReviewSubmission, betaBuildLocalizations, betaGroups, buildBetaDetail, diagnosticSignatures, expirationDate, expired, iconAssetToken, icons, individualTesters, minOsVersion, perfPowerMetrics, preReleaseVersion, processingState, uploadedDate, usesNonExemptEncryption, version] |

### Return type

[**BetaBuildLocalizationResponse**](BetaBuildLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaBuildLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="betaBuildLocalizationsUpdateInstance"></a>
# **betaBuildLocalizationsUpdateInstance**
> BetaBuildLocalizationResponse betaBuildLocalizationsUpdateInstance(id, betaBuildLocalizationUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BetaBuildLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    BetaBuildLocalizationsApi apiInstance = new BetaBuildLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    BetaBuildLocalizationUpdateRequest betaBuildLocalizationUpdateRequest = new BetaBuildLocalizationUpdateRequest(); // BetaBuildLocalizationUpdateRequest | BetaBuildLocalization representation
    try {
      BetaBuildLocalizationResponse result = apiInstance.betaBuildLocalizationsUpdateInstance(id, betaBuildLocalizationUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BetaBuildLocalizationsApi#betaBuildLocalizationsUpdateInstance");
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
| **betaBuildLocalizationUpdateRequest** | [**BetaBuildLocalizationUpdateRequest**](BetaBuildLocalizationUpdateRequest.md)| BetaBuildLocalization representation | |

### Return type

[**BetaBuildLocalizationResponse**](BetaBuildLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single BetaBuildLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

