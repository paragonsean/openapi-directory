# DomainApi

All URIs are relative to *https://api.turbinelabs.io/v1.0*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainDomainKeyDelete**](DomainApi.md#domainDomainKeyDelete) | **DELETE** /domain/{domainKey} | delete domain |
| [**domainDomainKeyGet**](DomainApi.md#domainDomainKeyGet) | **GET** /domain/{domainKey} | get domain |
| [**domainGet**](DomainApi.md#domainGet) | **GET** /domain | get domains |
| [**domainPost**](DomainApi.md#domainPost) | **POST** /domain | create domain |


<a id="domainDomainKeyDelete"></a>
# **domainDomainKeyDelete**
> Object domainDomainKeyDelete(domainKey, checksum)

delete domain

Delete an existing domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainApi apiInstance = new DomainApi(defaultClient);
    String domainKey = "48cf1c9b-f027-4223-b405-d48018ffb900"; // String | the domain key
    String checksum = "9cd24183-f848-48f8-6f55-0f07240700b9"; // String | the current checksum of the domain to be deleted
    try {
      Object result = apiInstance.domainDomainKeyDelete(domainKey, checksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainApi#domainDomainKeyDelete");
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
| **domainKey** | **String**| the domain key | |
| **checksum** | **String**| the current checksum of the domain to be deleted | |

### Return type

**Object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | an empty result |  -  |
| **0** | Unexpected error |  -  |

<a id="domainDomainKeyGet"></a>
# **domainDomainKeyGet**
> DomainResult domainDomainKeyGet(domainKey)

get domain

Get details for a single domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainApi apiInstance = new DomainApi(defaultClient);
    String domainKey = "48cf1c9b-f027-4223-b405-d48018ffb900"; // String | the domain key
    try {
      DomainResult result = apiInstance.domainDomainKeyGet(domainKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainApi#domainDomainKeyGet");
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
| **domainKey** | **String**| the domain key | |

### Return type

[**DomainResult**](DomainResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a single domain |  -  |
| **0** | Unexpected error |  -  |

<a id="domainGet"></a>
# **domainGet**
> MultiDomainResult domainGet(filters)

get domains

Get a list of domains

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainApi apiInstance = new DomainApi(defaultClient);
    String filters = "filters_example"; // String | A JSON encoded array of DomainFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any DomainFilter will be included. 
    try {
      MultiDomainResult result = apiInstance.domainGet(filters);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainApi#domainGet");
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
| **filters** | **String**| A JSON encoded array of DomainFilter objects. The filter is taken as a union of intersections. In other words an object that matches every constraint in any DomainFilter will be included.  | [optional] |

### Return type

[**MultiDomainResult**](MultiDomainResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | a result containing a list of domains |  -  |
| **0** | Unexpected error |  -  |

<a id="domainPost"></a>
# **domainPost**
> DomainResult domainPost(domain)

create domain

Create a new domain

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.turbinelabs.io/v1.0");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainApi apiInstance = new DomainApi(defaultClient);
    DomainCreate domain = new DomainCreate(); // DomainCreate | the domain to create
    try {
      DomainResult result = apiInstance.domainPost(domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainApi#domainPost");
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
| **domain** | [**DomainCreate**](DomainCreate.md)| the domain to create | |

### Return type

[**DomainResult**](DomainResult.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | the newly created zone |  -  |
| **0** | Unexpected error |  -  |

