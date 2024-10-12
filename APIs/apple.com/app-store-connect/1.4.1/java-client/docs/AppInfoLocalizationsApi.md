# AppInfoLocalizationsApi

All URIs are relative to *https://api.appstoreconnect.apple.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**appInfoLocalizationsCreateInstance**](AppInfoLocalizationsApi.md#appInfoLocalizationsCreateInstance) | **POST** /v1/appInfoLocalizations |  |
| [**appInfoLocalizationsDeleteInstance**](AppInfoLocalizationsApi.md#appInfoLocalizationsDeleteInstance) | **DELETE** /v1/appInfoLocalizations/{id} |  |
| [**appInfoLocalizationsGetInstance**](AppInfoLocalizationsApi.md#appInfoLocalizationsGetInstance) | **GET** /v1/appInfoLocalizations/{id} |  |
| [**appInfoLocalizationsUpdateInstance**](AppInfoLocalizationsApi.md#appInfoLocalizationsUpdateInstance) | **PATCH** /v1/appInfoLocalizations/{id} |  |


<a id="appInfoLocalizationsCreateInstance"></a>
# **appInfoLocalizationsCreateInstance**
> AppInfoLocalizationResponse appInfoLocalizationsCreateInstance(appInfoLocalizationCreateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfoLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfoLocalizationsApi apiInstance = new AppInfoLocalizationsApi(defaultClient);
    AppInfoLocalizationCreateRequest appInfoLocalizationCreateRequest = new AppInfoLocalizationCreateRequest(); // AppInfoLocalizationCreateRequest | AppInfoLocalization representation
    try {
      AppInfoLocalizationResponse result = apiInstance.appInfoLocalizationsCreateInstance(appInfoLocalizationCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfoLocalizationsApi#appInfoLocalizationsCreateInstance");
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
| **appInfoLocalizationCreateRequest** | [**AppInfoLocalizationCreateRequest**](AppInfoLocalizationCreateRequest.md)| AppInfoLocalization representation | |

### Return type

[**AppInfoLocalizationResponse**](AppInfoLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Single AppInfoLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **409** | Request entity error(s) |  -  |

<a id="appInfoLocalizationsDeleteInstance"></a>
# **appInfoLocalizationsDeleteInstance**
> appInfoLocalizationsDeleteInstance(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfoLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfoLocalizationsApi apiInstance = new AppInfoLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    try {
      apiInstance.appInfoLocalizationsDeleteInstance(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfoLocalizationsApi#appInfoLocalizationsDeleteInstance");
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

<a id="appInfoLocalizationsGetInstance"></a>
# **appInfoLocalizationsGetInstance**
> AppInfoLocalizationResponse appInfoLocalizationsGetInstance(id, fieldsAppInfoLocalizations, include)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfoLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfoLocalizationsApi apiInstance = new AppInfoLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    List<String> fieldsAppInfoLocalizations = Arrays.asList(); // List<String> | the fields to include for returned resources of type appInfoLocalizations
    List<String> include = Arrays.asList(); // List<String> | comma-separated list of relationships to include
    try {
      AppInfoLocalizationResponse result = apiInstance.appInfoLocalizationsGetInstance(id, fieldsAppInfoLocalizations, include);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfoLocalizationsApi#appInfoLocalizationsGetInstance");
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
| **fieldsAppInfoLocalizations** | [**List&lt;String&gt;**](String.md)| the fields to include for returned resources of type appInfoLocalizations | [optional] [enum: appInfo, locale, name, privacyPolicyText, privacyPolicyUrl, subtitle] |
| **include** | [**List&lt;String&gt;**](String.md)| comma-separated list of relationships to include | [optional] [enum: appInfo] |

### Return type

[**AppInfoLocalizationResponse**](AppInfoLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppInfoLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |

<a id="appInfoLocalizationsUpdateInstance"></a>
# **appInfoLocalizationsUpdateInstance**
> AppInfoLocalizationResponse appInfoLocalizationsUpdateInstance(id, appInfoLocalizationUpdateRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AppInfoLocalizationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.appstoreconnect.apple.com");
    
    // Configure HTTP bearer authorization: itc-bearer-token
    HttpBearerAuth itc-bearer-token = (HttpBearerAuth) defaultClient.getAuthentication("itc-bearer-token");
    itc-bearer-token.setBearerToken("BEARER TOKEN");

    AppInfoLocalizationsApi apiInstance = new AppInfoLocalizationsApi(defaultClient);
    String id = "id_example"; // String | the id of the requested resource
    AppInfoLocalizationUpdateRequest appInfoLocalizationUpdateRequest = new AppInfoLocalizationUpdateRequest(); // AppInfoLocalizationUpdateRequest | AppInfoLocalization representation
    try {
      AppInfoLocalizationResponse result = apiInstance.appInfoLocalizationsUpdateInstance(id, appInfoLocalizationUpdateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AppInfoLocalizationsApi#appInfoLocalizationsUpdateInstance");
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
| **appInfoLocalizationUpdateRequest** | [**AppInfoLocalizationUpdateRequest**](AppInfoLocalizationUpdateRequest.md)| AppInfoLocalization representation | |

### Return type

[**AppInfoLocalizationResponse**](AppInfoLocalizationResponse.md)

### Authorization

[itc-bearer-token](../README.md#itc-bearer-token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Single AppInfoLocalization |  -  |
| **400** | Parameter error(s) |  -  |
| **403** | Forbidden error |  -  |
| **404** | Not found error |  -  |
| **409** | Request entity error(s) |  -  |

