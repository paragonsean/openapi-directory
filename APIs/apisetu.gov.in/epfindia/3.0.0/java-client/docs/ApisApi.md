# ApisApi

All URIs are relative to *https://apisetu.gov.in/epfindia/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**epfsc**](ApisApi.md#epfsc) | **POST** /epfsc/certificate | Scheme Certificate |
| [**pecer**](ApisApi.md#pecer) | **POST** /pecer/certificate | Pension Certificate |
| [**uncrd**](ApisApi.md#uncrd) | **POST** /uncrd/certificate | UAN Card |


<a id="epfsc"></a>
# **epfsc**
> epfsc(epfscRequest)

Scheme Certificate

API to verify Scheme Certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apisetu.gov.in/epfindia/v3");
    
    // Configure API key authorization: clientId
    ApiKeyAuth clientId = (ApiKeyAuth) defaultClient.getAuthentication("clientId");
    clientId.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientId.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    EpfscRequest epfscRequest = new EpfscRequest(); // EpfscRequest | Request format
    try {
      apiInstance.epfsc(epfscRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#epfsc");
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
| **epfscRequest** | [**EpfscRequest**](EpfscRequest.md)| Request format | [optional] |

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate data in response body in PDF, XML or JSON format as requested in format parameter. |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized access |  -  |
| **404** | No record found |  -  |
| **500** | Internal server error |  -  |
| **502** | Bad gateway |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="pecer"></a>
# **pecer**
> pecer(pecerRequest)

Pension Certificate

API to verify Pension Certificate.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apisetu.gov.in/epfindia/v3");
    
    // Configure API key authorization: clientId
    ApiKeyAuth clientId = (ApiKeyAuth) defaultClient.getAuthentication("clientId");
    clientId.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientId.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    PecerRequest pecerRequest = new PecerRequest(); // PecerRequest | Request format
    try {
      apiInstance.pecer(pecerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#pecer");
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
| **pecerRequest** | [**PecerRequest**](PecerRequest.md)| Request format | [optional] |

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate data in response body in PDF, XML or JSON format as requested in format parameter. |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized access |  -  |
| **404** | No record found |  -  |
| **500** | Internal server error |  -  |
| **502** | Bad gateway |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

<a id="uncrd"></a>
# **uncrd**
> uncrd(uncrdRequest)

UAN Card

API to verify UAN Card.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apisetu.gov.in/epfindia/v3");
    
    // Configure API key authorization: clientId
    ApiKeyAuth clientId = (ApiKeyAuth) defaultClient.getAuthentication("clientId");
    clientId.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //clientId.setApiKeyPrefix("Token");

    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    ApisApi apiInstance = new ApisApi(defaultClient);
    UncrdRequest uncrdRequest = new UncrdRequest(); // UncrdRequest | Request format
    try {
      apiInstance.uncrd(uncrdRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#uncrd");
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
| **uncrdRequest** | [**UncrdRequest**](UncrdRequest.md)| Request format | [optional] |

### Return type

null (empty response body)

### Authorization

[clientId](../README.md#clientId), [apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/pdf, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The certificate data in response body in PDF, XML or JSON format as requested in format parameter. |  -  |
| **400** | Bad request |  -  |
| **401** | Unauthorized access |  -  |
| **404** | No record found |  -  |
| **500** | Internal server error |  -  |
| **502** | Bad gateway |  -  |
| **503** | Service unavailable |  -  |
| **504** | Gateway timeout |  -  |

