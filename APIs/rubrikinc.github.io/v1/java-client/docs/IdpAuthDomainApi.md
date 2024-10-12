# IdpAuthDomainApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createIdProviderAuthDomain**](IdpAuthDomainApi.md#createIdProviderAuthDomain) | **POST** /idp_auth_domain | Add a new IdP authentication domain |
| [**deleteIdProviderAuthDomain**](IdpAuthDomainApi.md#deleteIdProviderAuthDomain) | **DELETE** /idp_auth_domain/{id} | Delete an IdP authentication domain for the given ID |
| [**getIdProviderAuthDomain**](IdpAuthDomainApi.md#getIdProviderAuthDomain) | **GET** /idp_auth_domain/{id} | Get an IdP authentication domain for the given id |
| [**queryIdProviderAuthDomain**](IdpAuthDomainApi.md#queryIdProviderAuthDomain) | **GET** /idp_auth_domain | Get a list of IdP authentication domains |
| [**updateIdProviderAuthDomain**](IdpAuthDomainApi.md#updateIdProviderAuthDomain) | **PATCH** /idp_auth_domain/{id} | Update an existing IdP authentication domain |


<a id="createIdProviderAuthDomain"></a>
# **createIdProviderAuthDomain**
> IdProviderAuthDomainSummary createIdProviderAuthDomain(idProviderAuthDomainInfo)

Add a new IdP authentication domain

Add a new IdP authentication domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpAuthDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IdpAuthDomainApi apiInstance = new IdpAuthDomainApi(defaultClient);
    IdProviderAuthDomainInfo idProviderAuthDomainInfo = new IdProviderAuthDomainInfo(); // IdProviderAuthDomainInfo | Information for joining an IdP authentication domain.
    try {
      IdProviderAuthDomainSummary result = apiInstance.createIdProviderAuthDomain(idProviderAuthDomainInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpAuthDomainApi#createIdProviderAuthDomain");
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
| **idProviderAuthDomainInfo** | [**IdProviderAuthDomainInfo**](IdProviderAuthDomainInfo.md)| Information for joining an IdP authentication domain. | |

### Return type

[**IdProviderAuthDomainSummary**](IdProviderAuthDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Returns a summary of the newly created IdP authentication domain. |  -  |

<a id="deleteIdProviderAuthDomain"></a>
# **deleteIdProviderAuthDomain**
> deleteIdProviderAuthDomain(id)

Delete an IdP authentication domain for the given ID

Delete an IdP authentication domain for the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpAuthDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IdpAuthDomainApi apiInstance = new IdpAuthDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the IdP authentication domain to be deleted.
    try {
      apiInstance.deleteIdProviderAuthDomain(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpAuthDomainApi#deleteIdProviderAuthDomain");
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
| **id** | **String**| ID of the IdP authentication domain to be deleted. | |

### Return type

null (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Delete Successful. |  -  |

<a id="getIdProviderAuthDomain"></a>
# **getIdProviderAuthDomain**
> IdProviderAuthDomainSummary getIdProviderAuthDomain(id)

Get an IdP authentication domain for the given id

Get an IdP authentication domain for the given id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpAuthDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IdpAuthDomainApi apiInstance = new IdpAuthDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the IdP Authentication Domain to be retrieved.
    try {
      IdProviderAuthDomainSummary result = apiInstance.getIdProviderAuthDomain(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpAuthDomainApi#getIdProviderAuthDomain");
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
| **id** | **String**| ID of the IdP Authentication Domain to be retrieved. | |

### Return type

[**IdProviderAuthDomainSummary**](IdProviderAuthDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a summary of the requested IdP authentication domain. |  -  |

<a id="queryIdProviderAuthDomain"></a>
# **queryIdProviderAuthDomain**
> IdProviderAuthDomainSummaryListResponse queryIdProviderAuthDomain()

Get a list of IdP authentication domains

Get a list of IdP authentication domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpAuthDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IdpAuthDomainApi apiInstance = new IdpAuthDomainApi(defaultClient);
    try {
      IdProviderAuthDomainSummaryListResponse result = apiInstance.queryIdProviderAuthDomain();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpAuthDomainApi#queryIdProviderAuthDomain");
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

[**IdProviderAuthDomainSummaryListResponse**](IdProviderAuthDomainSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of IdP authentication domains. |  -  |

<a id="updateIdProviderAuthDomain"></a>
# **updateIdProviderAuthDomain**
> IdProviderAuthDomainSummary updateIdProviderAuthDomain(id, idProviderAuthDomainInfoUpdate)

Update an existing IdP authentication domain

Update an existing IdP authentication domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IdpAuthDomainApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api/v1");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: Bearer
    ApiKeyAuth Bearer = (ApiKeyAuth) defaultClient.getAuthentication("Bearer");
    Bearer.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //Bearer.setApiKeyPrefix("Token");

    IdpAuthDomainApi apiInstance = new IdpAuthDomainApi(defaultClient);
    String id = "id_example"; // String | ID of the IdP authentication domain to be updated.
    IdProviderAuthDomainInfoUpdate idProviderAuthDomainInfoUpdate = new IdProviderAuthDomainInfoUpdate(); // IdProviderAuthDomainInfoUpdate | Information for updating an IdP authentication domain.
    try {
      IdProviderAuthDomainSummary result = apiInstance.updateIdProviderAuthDomain(id, idProviderAuthDomainInfoUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IdpAuthDomainApi#updateIdProviderAuthDomain");
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
| **id** | **String**| ID of the IdP authentication domain to be updated. | |
| **idProviderAuthDomainInfoUpdate** | [**IdProviderAuthDomainInfoUpdate**](IdProviderAuthDomainInfoUpdate.md)| Information for updating an IdP authentication domain. | |

### Return type

[**IdProviderAuthDomainSummary**](IdProviderAuthDomainSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a summary of the newly updated IdP authentication domain. |  -  |

