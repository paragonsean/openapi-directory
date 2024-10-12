# HostedOnboardingApi

All URIs are relative to *https://kyc-test.adyen.com/lem/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getThemes**](HostedOnboardingApi.md#getThemes) | **GET** /themes | Get a list of hosted onboarding page themes |
| [**getThemesId**](HostedOnboardingApi.md#getThemesId) | **GET** /themes/{id} | Get an onboarding link theme |
| [**postLegalEntitiesIdOnboardingLinks**](HostedOnboardingApi.md#postLegalEntitiesIdOnboardingLinks) | **POST** /legalEntities/{id}/onboardingLinks | Get a link to an Adyen-hosted onboarding page |


<a id="getThemes"></a>
# **getThemes**
> OnboardingThemes getThemes()

Get a list of hosted onboarding page themes

Returns a list of hosted onboarding page themes.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostedOnboardingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    HostedOnboardingApi apiInstance = new HostedOnboardingApi(defaultClient);
    try {
      OnboardingThemes result = apiInstance.getThemes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostedOnboardingApi#getThemes");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**OnboardingThemes**](OnboardingThemes.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getThemesId"></a>
# **getThemesId**
> OnboardingTheme getThemesId(id)

Get an onboarding link theme

Returns the details of the theme identified in the path.&gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostedOnboardingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    HostedOnboardingApi apiInstance = new HostedOnboardingApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the theme
    try {
      OnboardingTheme result = apiInstance.getThemesId(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostedOnboardingApi#getThemesId");
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
| **id** | **String**| The unique identifier of the theme | |

### Return type

[**OnboardingTheme**](OnboardingTheme.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postLegalEntitiesIdOnboardingLinks"></a>
# **postLegalEntitiesIdOnboardingLinks**
> OnboardingLink postLegalEntitiesIdOnboardingLinks(id, onboardingLinkInfo)

Get a link to an Adyen-hosted onboarding page

Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.  &gt;If you are using hosted onboarding and just beginning your integration, use v3 for your API requests. Otherwise, use v2.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HostedOnboardingApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://kyc-test.adyen.com/lem/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    HostedOnboardingApi apiInstance = new HostedOnboardingApi(defaultClient);
    String id = "id_example"; // String | The unique identifier of the legal entity
    OnboardingLinkInfo onboardingLinkInfo = new OnboardingLinkInfo(); // OnboardingLinkInfo | 
    try {
      OnboardingLink result = apiInstance.postLegalEntitiesIdOnboardingLinks(id, onboardingLinkInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HostedOnboardingApi#postLegalEntitiesIdOnboardingLinks");
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
| **id** | **String**| The unique identifier of the legal entity | |
| **onboardingLinkInfo** | [**OnboardingLinkInfo**](OnboardingLinkInfo.md)|  | [optional] |

### Return type

[**OnboardingLink**](OnboardingLink.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

