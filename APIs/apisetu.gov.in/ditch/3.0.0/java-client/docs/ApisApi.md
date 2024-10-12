# ApisApi

All URIs are relative to *https://apisetu.gov.in/ditch/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**incer**](ApisApi.md#incer) | **POST** /incer/certificate | Income Certificate |
| [**rmcer**](ApisApi.md#rmcer) | **POST** /rmcer/certificate | Marriage Certificate |
| [**rscer**](ApisApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate |
| [**sicrd**](ApisApi.md#sicrd) | **POST** /sicrd/certificate | Senior Citizen Identity Card/ Certificate |


<a id="incer"></a>
# **incer**
> incer(incerRequest)

Income Certificate

API to verify Income Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/ditch/v3");
    
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
    IncerRequest incerRequest = new IncerRequest(); // IncerRequest | Request format
    try {
      apiInstance.incer(incerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#incer");
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
| **incerRequest** | [**IncerRequest**](IncerRequest.md)| Request format | [optional] |

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

<a id="rmcer"></a>
# **rmcer**
> rmcer(incerRequest)

Marriage Certificate

API to verify Marriage Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/ditch/v3");
    
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
    IncerRequest incerRequest = new IncerRequest(); // IncerRequest | Request format
    try {
      apiInstance.rmcer(incerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#rmcer");
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
| **incerRequest** | [**IncerRequest**](IncerRequest.md)| Request format | [optional] |

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

<a id="rscer"></a>
# **rscer**
> rscer(incerRequest)

Residence Certificate

API to verify Residence Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/ditch/v3");
    
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
    IncerRequest incerRequest = new IncerRequest(); // IncerRequest | Request format
    try {
      apiInstance.rscer(incerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#rscer");
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
| **incerRequest** | [**IncerRequest**](IncerRequest.md)| Request format | [optional] |

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

<a id="sicrd"></a>
# **sicrd**
> sicrd(sicrdRequest)

Senior Citizen Identity Card/ Certificate

API to verify Senior Citizen Identity Card/ Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/ditch/v3");
    
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
    SicrdRequest sicrdRequest = new SicrdRequest(); // SicrdRequest | Request format
    try {
      apiInstance.sicrd(sicrdRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#sicrd");
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
| **sicrdRequest** | [**SicrdRequest**](SicrdRequest.md)| Request format | [optional] |

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

