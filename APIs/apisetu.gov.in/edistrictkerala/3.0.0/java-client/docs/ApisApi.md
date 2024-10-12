# ApisApi

All URIs are relative to *https://apisetu.gov.in/edistrictkerala/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cmcer**](ApisApi.md#cmcer) | **POST** /cmcer/certificate | Community Certificate |
| [**cncer**](ApisApi.md#cncer) | **POST** /cncer/certificate | Conversion Certificate |
| [**ctcer**](ApisApi.md#ctcer) | **POST** /ctcer/certificate | Caste Certificate |
| [**dmcer**](ApisApi.md#dmcer) | **POST** /dmcer/certificate | Domicile Certificate |
| [**dpcer**](ApisApi.md#dpcer) | **POST** /dpcer/certificate | Dependency Certificate |
| [**dscer**](ApisApi.md#dscer) | **POST** /dscer/certificate | Destitute Certificate |
| [**fmcer**](ApisApi.md#fmcer) | **POST** /fmcer/certificate | Family Membership Certificate |
| [**idcer**](ApisApi.md#idcer) | **POST** /idcer/certificate | Identification Certificate |
| [**imcer**](ApisApi.md#imcer) | **POST** /imcer/certificate | Inter-Caste Marriage Certificate |
| [**incer**](ApisApi.md#incer) | **POST** /incer/certificate | Income Certificate |
| [**lfcer**](ApisApi.md#lfcer) | **POST** /lfcer/certificate | Life Certificate |
| [**lhcer**](ApisApi.md#lhcer) | **POST** /lhcer/certificate | Legal Heir Certificate |
| [**locer**](ApisApi.md#locer) | **POST** /locer/certificate | Location Certificate |
| [**mncer**](ApisApi.md#mncer) | **POST** /mncer/certificate | Minority Certificate |
| [**nrcer**](ApisApi.md#nrcer) | **POST** /nrcer/certificate | Non-Remarriage Certificate |
| [**ntcer**](ApisApi.md#ntcer) | **POST** /ntcer/certificate | Nativity Certificate |
| [**oscer**](ApisApi.md#oscer) | **POST** /oscer/certificate | One and the Same Certificate |
| [**pncer**](ApisApi.md#pncer) | **POST** /pncer/certificate | Possession and Non-Attachment Certificate |
| [**pscer**](ApisApi.md#pscer) | **POST** /pscer/certificate | Possession Certificate |
| [**rlcer**](ApisApi.md#rlcer) | **POST** /rlcer/certificate | Relationship Certificate |
| [**rscer**](ApisApi.md#rscer) | **POST** /rscer/certificate | Residence Certificate |
| [**slcer**](ApisApi.md#slcer) | **POST** /slcer/certificate | Solvency Certificate |
| [**vlcer**](ApisApi.md#vlcer) | **POST** /vlcer/certificate | Valuation Certificate |
| [**wwcer**](ApisApi.md#wwcer) | **POST** /wwcer/certificate | Widow-Widower Certificate |


<a id="cmcer"></a>
# **cmcer**
> cmcer(cmcerRequest)

Community Certificate

API to verify Community Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.cmcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#cmcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="cncer"></a>
# **cncer**
> cncer(cmcerRequest)

Conversion Certificate

API to verify Conversion Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.cncer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#cncer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="ctcer"></a>
# **ctcer**
> ctcer(cmcerRequest)

Caste Certificate

API to verify Caste Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.ctcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#ctcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="dmcer"></a>
# **dmcer**
> dmcer(cmcerRequest)

Domicile Certificate

API to verify Domicile Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.dmcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#dmcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="dpcer"></a>
# **dpcer**
> dpcer(cmcerRequest)

Dependency Certificate

API to verify Dependency Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.dpcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#dpcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="dscer"></a>
# **dscer**
> dscer(cmcerRequest)

Destitute Certificate

API to verify Destitute Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.dscer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#dscer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="fmcer"></a>
# **fmcer**
> fmcer(cmcerRequest)

Family Membership Certificate

API to verify Family Membership Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.fmcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#fmcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="idcer"></a>
# **idcer**
> idcer(cmcerRequest)

Identification Certificate

API to verify Identification Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.idcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#idcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="imcer"></a>
# **imcer**
> imcer(cmcerRequest)

Inter-Caste Marriage Certificate

API to verify Inter-Caste Marriage Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.imcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#imcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="incer"></a>
# **incer**
> incer(cmcerRequest)

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.incer(cmcerRequest);
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="lfcer"></a>
# **lfcer**
> lfcer(cmcerRequest)

Life Certificate

API to verify Life Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.lfcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#lfcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="lhcer"></a>
# **lhcer**
> lhcer(cmcerRequest)

Legal Heir Certificate

API to verify Legal Heir Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.lhcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#lhcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="locer"></a>
# **locer**
> locer(cmcerRequest)

Location Certificate

API to verify Location Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.locer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#locer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="mncer"></a>
# **mncer**
> mncer(cmcerRequest)

Minority Certificate

API to verify Minority Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.mncer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#mncer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="nrcer"></a>
# **nrcer**
> nrcer(cmcerRequest)

Non-Remarriage Certificate

API to verify Non-Remarriage Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.nrcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#nrcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="ntcer"></a>
# **ntcer**
> ntcer(cmcerRequest)

Nativity Certificate

API to verify Nativity Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.ntcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#ntcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="oscer"></a>
# **oscer**
> oscer(cmcerRequest)

One and the Same Certificate

API to verify One and the Same Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.oscer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#oscer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="pncer"></a>
# **pncer**
> pncer(cmcerRequest)

Possession and Non-Attachment Certificate

API to verify Possession and Non-Attachment Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.pncer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#pncer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="pscer"></a>
# **pscer**
> pscer(cmcerRequest)

Possession Certificate

API to verify Possession Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.pscer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#pscer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="rlcer"></a>
# **rlcer**
> rlcer(cmcerRequest)

Relationship Certificate

API to verify Relationship Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.rlcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#rlcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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
> rscer(cmcerRequest)

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.rscer(cmcerRequest);
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="slcer"></a>
# **slcer**
> slcer(cmcerRequest)

Solvency Certificate

API to verify Solvency Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.slcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#slcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="vlcer"></a>
# **vlcer**
> vlcer(cmcerRequest)

Valuation Certificate

API to verify Valuation Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.vlcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#vlcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

<a id="wwcer"></a>
# **wwcer**
> wwcer(cmcerRequest)

Widow-Widower Certificate

API to verify Widow-Widower Certificate.

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
    defaultClient.setBasePath("https://apisetu.gov.in/edistrictkerala/v3");
    
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
    CmcerRequest cmcerRequest = new CmcerRequest(); // CmcerRequest | Request format
    try {
      apiInstance.wwcer(cmcerRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#wwcer");
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
| **cmcerRequest** | [**CmcerRequest**](CmcerRequest.md)| Request format | [optional] |

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

