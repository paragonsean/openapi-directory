# DnsApi

All URIs are relative to *http://api.ss.solarvps.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**dnsDomainAddPost**](DnsApi.md#dnsDomainAddPost) | **POST** /dns/{domain}/add | Add dns record for given domain |
| [**dnsDomainDeletePost**](DnsApi.md#dnsDomainDeletePost) | **POST** /dns/{domain}/delete | Delete dns record for a given domain |
| [**dnsDomainGet**](DnsApi.md#dnsDomainGet) | **GET** /dns/{domain} | View all your records for a given domain |
| [**dnsDomainUpdatePost**](DnsApi.md#dnsDomainUpdatePost) | **POST** /dns/{domain}/update | Update dns record for a given domain |


<a id="dnsDomainAddPost"></a>
# **dnsDomainAddPost**
> dnsDomainAddPost(domain, name, type, content, ttl, prio)

Add dns record for given domain

You can try example.com below. Types allowed are: A CNAME NS TXT MX SRV SPF

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DnsApi apiInstance = new DnsApi(defaultClient);
    String domain = "domain_example"; // String | Domain you want to add records for
    String name = "name_example"; // String | Fully qualified DNS name
    String type = "type_example"; // String | Type of DNS record
    String content = "content_example"; // String | Content for DNS record
    String ttl = "ttl_example"; // String | Time To Live for DNS record
    String prio = "prio_example"; // String | Priority of DNS record
    try {
      apiInstance.dnsDomainAddPost(domain, name, type, content, ttl, prio);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsApi#dnsDomainAddPost");
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
| **domain** | **String**| Domain you want to add records for | |
| **name** | **String**| Fully qualified DNS name | |
| **type** | **String**| Type of DNS record | |
| **content** | **String**| Content for DNS record | |
| **ttl** | **String**| Time To Live for DNS record | |
| **prio** | **String**| Priority of DNS record | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="dnsDomainDeletePost"></a>
# **dnsDomainDeletePost**
> dnsDomainDeletePost(domain, id)

Delete dns record for a given domain

Shows all your records for a specific domain. You can try example.com below.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DnsApi apiInstance = new DnsApi(defaultClient);
    String domain = "domain_example"; // String | Domain name you want to get records for
    String id = "id_example"; // String | Id of the DNS Record
    try {
      apiInstance.dnsDomainDeletePost(domain, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsApi#dnsDomainDeletePost");
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
| **domain** | **String**| Domain name you want to get records for | |
| **id** | **String**| Id of the DNS Record | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="dnsDomainGet"></a>
# **dnsDomainGet**
> dnsDomainGet(domain)

View all your records for a given domain

Shows all your records for a specific domain. You can try example.com below.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DnsApi apiInstance = new DnsApi(defaultClient);
    String domain = "domain_example"; // String | Domain name you want to get records for
    try {
      apiInstance.dnsDomainGet(domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsApi#dnsDomainGet");
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
| **domain** | **String**| Domain name you want to get records for | |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

<a id="dnsDomainUpdatePost"></a>
# **dnsDomainUpdatePost**
> dnsDomainUpdatePost(domain, id, name, type, content, ttl, prio)

Update dns record for a given domain

You can try example.com below.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DnsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ss.solarvps.com");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    DnsApi apiInstance = new DnsApi(defaultClient);
    String domain = "domain_example"; // String | Domain name to add record under
    String id = "id_example"; // String | Id of DNS record
    String name = "name_example"; // String | Fully qualified name for the DNS record
    String type = "type_example"; // String | Type for DNS record
    String content = "content_example"; // String | Content for the DNS Record
    String ttl = "ttl_example"; // String | Time To Live for DNS record
    String prio = "prio_example"; // String | Priority of the DNS record
    try {
      apiInstance.dnsDomainUpdatePost(domain, id, name, type, content, ttl, prio);
    } catch (ApiException e) {
      System.err.println("Exception when calling DnsApi#dnsDomainUpdatePost");
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
| **domain** | **String**| Domain name to add record under | |
| **id** | **String**| Id of DNS record | |
| **name** | **String**| Fully qualified name for the DNS record | [optional] |
| **type** | **String**| Type for DNS record | [optional] |
| **content** | **String**| Content for the DNS Record | [optional] |
| **ttl** | **String**| Time To Live for DNS record | [optional] |
| **prio** | **String**| Priority of the DNS record | [optional] |

### Return type

null (empty response body)

### Authorization

[apiKey](../README.md#apiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

