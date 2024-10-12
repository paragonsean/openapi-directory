# DomainsApi

All URIs are relative to *http://apiv2.clickmeter.com:80*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**domainsCount**](DomainsApi.md#domainsCount) | **GET** /domains/count | Retrieve count of domains |
| [**domainsDelete**](DomainsApi.md#domainsDelete) | **DELETE** /domains/{id} | Delete a domain |
| [**domainsGet**](DomainsApi.md#domainsGet) | **GET** /domains | Retrieve a list of domains |
| [**domainsIdGet**](DomainsApi.md#domainsIdGet) | **GET** /domains/{id} | Get a domain |
| [**domainsPut**](DomainsApi.md#domainsPut) | **POST** /domains | Create a domain |
| [**domainsUpdate**](DomainsApi.md#domainsUpdate) | **POST** /domains/{id} | Update a domain |


<a id="domainsCount"></a>
# **domainsCount**
> ApiCoreResponsesCountResponce domainsCount(type, name)

Retrieve count of domains

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    String type = "system"; // String | Type of domain (\"system\"/\"go\"/\"personal\"/\"dedicated\"). If not specified default is \"system\"
    String name = "name_example"; // String | Filter domains with this anmen
    try {
      ApiCoreResponsesCountResponce result = apiInstance.domainsCount(type, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsCount");
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
| **type** | **String**| Type of domain (\&quot;system\&quot;/\&quot;go\&quot;/\&quot;personal\&quot;/\&quot;dedicated\&quot;). If not specified default is \&quot;system\&quot; | [optional] [default to system] [enum: system, go, personal, dedicated] |
| **name** | **String**| Filter domains with this anmen | [optional] |

### Return type

[**ApiCoreResponsesCountResponce**](ApiCoreResponsesCountResponce.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="domainsDelete"></a>
# **domainsDelete**
> ApiCoreResponsesEntityUriSystemInt64 domainsDelete(id)

Delete a domain

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Long id = 56L; // Long | Id of domain
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.domainsDelete(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsDelete");
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
| **id** | **Long**| Id of domain | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="domainsGet"></a>
# **domainsGet**
> ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 domainsGet(offset, limit, type, name)

Retrieve a list of domains

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Integer offset = 56; // Integer | Offset where to start from
    Integer limit = 56; // Integer | Limit results to this number
    String type = "system"; // String | Type of domain (\"system\"/\"go\"/\"personal\"/\"dedicated\"). If not specified default is \"system\"
    String name = "name_example"; // String | Filter domains with this anmen
    try {
      ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64 result = apiInstance.domainsGet(offset, limit, type, name);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsGet");
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
| **offset** | **Integer**| Offset where to start from | [optional] |
| **limit** | **Integer**| Limit results to this number | [optional] |
| **type** | **String**| Type of domain (\&quot;system\&quot;/\&quot;go\&quot;/\&quot;personal\&quot;/\&quot;dedicated\&quot;). If not specified default is \&quot;system\&quot; | [optional] [default to system] [enum: system, go, personal, dedicated] |
| **name** | **String**| Filter domains with this anmen | [optional] |

### Return type

[**ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntitiesResponseApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="domainsIdGet"></a>
# **domainsIdGet**
> ApiCoreDtoDomainsDomain domainsIdGet(id)

Get a domain

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Long id = 56L; // Long | Id of domain
    try {
      ApiCoreDtoDomainsDomain result = apiInstance.domainsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsIdGet");
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
| **id** | **Long**| Id of domain | |

### Return type

[**ApiCoreDtoDomainsDomain**](ApiCoreDtoDomainsDomain.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="domainsPut"></a>
# **domainsPut**
> ApiCoreResponsesEntityUriSystemInt64 domainsPut(apiCoreDtoDomainsDomain)

Create a domain

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    ApiCoreDtoDomainsDomain apiCoreDtoDomainsDomain = new ApiCoreDtoDomainsDomain(); // ApiCoreDtoDomainsDomain | The domain to create
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.domainsPut(apiCoreDtoDomainsDomain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsPut");
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
| **apiCoreDtoDomainsDomain** | [**ApiCoreDtoDomainsDomain**](ApiCoreDtoDomainsDomain.md)| The domain to create | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

<a id="domainsUpdate"></a>
# **domainsUpdate**
> ApiCoreResponsesEntityUriSystemInt64 domainsUpdate(id, apiCoreDtoDomainsDomain)

Update a domain

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
    defaultClient.setBasePath("http://apiv2.clickmeter.com:80");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    DomainsApi apiInstance = new DomainsApi(defaultClient);
    Long id = 56L; // Long | Id of domain
    ApiCoreDtoDomainsDomain apiCoreDtoDomainsDomain = new ApiCoreDtoDomainsDomain(); // ApiCoreDtoDomainsDomain | The domain to update
    try {
      ApiCoreResponsesEntityUriSystemInt64 result = apiInstance.domainsUpdate(id, apiCoreDtoDomainsDomain);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApi#domainsUpdate");
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
| **id** | **Long**| Id of domain | |
| **apiCoreDtoDomainsDomain** | [**ApiCoreDtoDomainsDomain**](ApiCoreDtoDomainsDomain.md)| The domain to update | |

### Return type

[**ApiCoreResponsesEntityUriSystemInt64**](ApiCoreResponsesEntityUriSystemInt64.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **401** | Unauthorized |  -  |
| **500** | Internal Server Error |  -  |

