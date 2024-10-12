# DomainsApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDomain**](DomainsApi.md#addDomain) | **POST** /domains | Claim a new Domain |
| [**checkDomainVerify**](DomainsApi.md#checkDomainVerify) | **POST** /domains/verify/{domain} | Check a new Domain |
| [**getAllDomains**](DomainsApi.md#getAllDomains) | **GET** /domains | Get all domains you have access to |
| [**getDomainVerify**](DomainsApi.md#getDomainVerify) | **GET** /domains/verify/{domain} | Get domain verification |
| [**removeDomainVerify**](DomainsApi.md#removeDomainVerify) | **DELETE** /domains/{domain} | Remove a domain |


<a id="addDomain"></a>
# **addDomain**
> DomainResponse addDomain(addDomainRequest)

Claim a new Domain



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    AddDomainRequest addDomainRequest = new AddDomainRequest(); // AddDomainRequest | Domain body
    try {
      DomainResponse result = apiInstance.addDomain(addDomainRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#addDomain");
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
| **addDomainRequest** | [**AddDomainRequest**](AddDomainRequest.md)| Domain body | |

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Internal error |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="checkDomainVerify"></a>
# **checkDomainVerify**
> CheckDomainVerify checkDomainVerify(domain)

Check a new Domain



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domain = "domain_example"; // String | Full Top-level domain name
    try {
      CheckDomainVerify result = apiInstance.checkDomainVerify(domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#checkDomainVerify");
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
| **domain** | **String**| Full Top-level domain name | |

### Return type

[**CheckDomainVerify**](CheckDomainVerify.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Internal error |  -  |
| **401** | Authorization failed |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="getAllDomains"></a>
# **getAllDomains**
> GetAllDomainsResponse getAllDomains()

Get all domains you have access to



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    try {
      GetAllDomainsResponse result = apiInstance.getAllDomains();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getAllDomains");
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

[**GetAllDomainsResponse**](GetAllDomainsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Internal error |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="getDomainVerify"></a>
# **getDomainVerify**
> DomainResponse getDomainVerify(domain)

Get domain verification



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domain = "domain_example"; // String | Full Top-level domain name
    try {
      DomainResponse result = apiInstance.getDomainVerify(domain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#getDomainVerify");
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
| **domain** | **String**| Full Top-level domain name | |

### Return type

[**DomainResponse**](DomainResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Internal error |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

<a id="removeDomainVerify"></a>
# **removeDomainVerify**
> removeDomainVerify(domain)

Remove a domain



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String domain = "domain_example"; // String | Full Top-level domain name
    try {
      apiInstance.removeDomainVerify(domain);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#removeDomainVerify");
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
| **domain** | **String**| Full Top-level domain name | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Internal error |  -  |
| **403** | Bad credentials |  -  |
| **405** | Invalid input |  -  |

