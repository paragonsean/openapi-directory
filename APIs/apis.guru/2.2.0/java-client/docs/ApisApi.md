# ApisApi

All URIs are relative to *https://api.apis.guru/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAPI**](ApisApi.md#getAPI) | **GET** /specs/{provider}/{api}.json | Retrieve one version of a particular API |
| [**getMetrics**](ApisApi.md#getMetrics) | **GET** /metrics.json | Get basic metrics |
| [**getProvider**](ApisApi.md#getProvider) | **GET** /{provider}.json | List all APIs for a particular provider |
| [**getProviders**](ApisApi.md#getProviders) | **GET** /providers.json | List all providers |
| [**getServiceAPI**](ApisApi.md#getServiceAPI) | **GET** /specs/{provider}/{service}/{api}.json | Retrieve one version of a particular API with a serviceName. |
| [**getServices**](ApisApi.md#getServices) | **GET** /{provider}/services.json | List all serviceNames for a particular provider |
| [**listAPIs**](ApisApi.md#listAPIs) | **GET** /list.json | List all APIs |


<a id="getAPI"></a>
# **getAPI**
> API getAPI(provider, api)

Retrieve one version of a particular API

Returns the API entry for one specific version of an API where there is no serviceName.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String provider = "apis.guru"; // String | 
    String api = "2.1.0"; // String | 
    try {
      API result = apiInstance.getAPI(provider, api);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getAPI");
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
| **provider** | **String**|  | |
| **api** | **String**|  | |

### Return type

[**API**](API.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getMetrics"></a>
# **getMetrics**
> Metrics getMetrics()

Get basic metrics

Some basic metrics for the entire directory. Just stunning numbers to put on a front page and are intended purely for WoW effect :) 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    try {
      Metrics result = apiInstance.getMetrics();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getMetrics");
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

[**Metrics**](Metrics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProvider"></a>
# **getProvider**
> Map&lt;String, API&gt; getProvider(provider)

List all APIs for a particular provider

List all APIs in the directory for a particular providerName Returns links to the individual API entry for each API. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String provider = "apis.guru"; // String | 
    try {
      Map<String, API> result = apiInstance.getProvider(provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getProvider");
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
| **provider** | **String**|  | |

### Return type

[**Map&lt;String, API&gt;**](API.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getProviders"></a>
# **getProviders**
> GetProviders200Response getProviders()

List all providers

List all the providers in the directory 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    try {
      GetProviders200Response result = apiInstance.getProviders();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getProviders");
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

[**GetProviders200Response**](GetProviders200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getServiceAPI"></a>
# **getServiceAPI**
> API getServiceAPI(provider, service, api)

Retrieve one version of a particular API with a serviceName.

Returns the API entry for one specific version of an API where there is a serviceName.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String provider = "apis.guru"; // String | 
    String service = "graph"; // String | 
    String api = "2.1.0"; // String | 
    try {
      API result = apiInstance.getServiceAPI(provider, service, api);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getServiceAPI");
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
| **provider** | **String**|  | |
| **service** | **String**|  | |
| **api** | **String**|  | |

### Return type

[**API**](API.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getServices"></a>
# **getServices**
> GetServices200Response getServices(provider)

List all serviceNames for a particular provider

List all serviceNames in the directory for a particular providerName 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    String provider = "apis.guru"; // String | 
    try {
      GetServices200Response result = apiInstance.getServices(provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#getServices");
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
| **provider** | **String**|  | |

### Return type

[**GetServices200Response**](GetServices200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="listAPIs"></a>
# **listAPIs**
> Map&lt;String, API&gt; listAPIs()

List all APIs

List all APIs in the directory. Returns links to the OpenAPI definitions for each API in the directory. If API exist in multiple versions &#x60;preferred&#x60; one is explicitly marked. Some basic info from the OpenAPI definition is cached inside each object. This allows you to generate some simple views without needing to fetch the OpenAPI definition for each API. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApisApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.apis.guru/v2");

    ApisApi apiInstance = new ApisApi(defaultClient);
    try {
      Map<String, API> result = apiInstance.listAPIs();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApisApi#listAPIs");
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

[**Map&lt;String, API&gt;**](API.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

