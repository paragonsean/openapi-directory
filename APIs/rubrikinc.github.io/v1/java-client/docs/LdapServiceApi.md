# LdapServiceApi

All URIs are relative to */api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createLdapService**](LdapServiceApi.md#createLdapService) | **POST** /ldap_service | Add a new authentication domain |
| [**deleteLdapService**](LdapServiceApi.md#deleteLdapService) | **DELETE** /ldap_service/{id} | Delete an authentication domain for the given ID |
| [**getLdapService**](LdapServiceApi.md#getLdapService) | **GET** /ldap_service/{id} | Get a LDAP service for the given ID |
| [**patchLdapService**](LdapServiceApi.md#patchLdapService) | **PATCH** /ldap_service/{id} | Update an existing authentication domain |
| [**putLdapService**](LdapServiceApi.md#putLdapService) | **PUT** /ldap_service/{id} | Replace the values of an authentication domain |
| [**queryLdapService**](LdapServiceApi.md#queryLdapService) | **GET** /ldap_service | Get a list of LDAP services |


<a id="createLdapService"></a>
# **createLdapService**
> LdapServiceSummary createLdapService(ldapServiceInfo)

Add a new authentication domain

Add a new authentication domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LdapServiceApi;

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

    LdapServiceApi apiInstance = new LdapServiceApi(defaultClient);
    LdapServiceInfo ldapServiceInfo = new LdapServiceInfo(); // LdapServiceInfo | Information for joining an authentication domain.
    try {
      LdapServiceSummary result = apiInstance.createLdapService(ldapServiceInfo);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LdapServiceApi#createLdapService");
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
| **ldapServiceInfo** | [**LdapServiceInfo**](LdapServiceInfo.md)| Information for joining an authentication domain. | |

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Returns a summary of the newly created authentication. domain. |  -  |

<a id="deleteLdapService"></a>
# **deleteLdapService**
> deleteLdapService(id)

Delete an authentication domain for the given ID

Delete an authentication domain for the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LdapServiceApi;

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

    LdapServiceApi apiInstance = new LdapServiceApi(defaultClient);
    String id = "id_example"; // String | ID of the authentication domain to be deleted.
    try {
      apiInstance.deleteLdapService(id);
    } catch (ApiException e) {
      System.err.println("Exception when calling LdapServiceApi#deleteLdapService");
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
| **id** | **String**| ID of the authentication domain to be deleted. | |

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
| **204** | Delete successful. |  -  |

<a id="getLdapService"></a>
# **getLdapService**
> LdapServiceSummary getLdapService(id)

Get a LDAP service for the given ID

Get a LDAP service for the given ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LdapServiceApi;

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

    LdapServiceApi apiInstance = new LdapServiceApi(defaultClient);
    String id = "id_example"; // String | ID of the authentication domain to be retrieved.
    try {
      LdapServiceSummary result = apiInstance.getLdapService(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LdapServiceApi#getLdapService");
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
| **id** | **String**| ID of the authentication domain to be retrieved. | |

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a summary of the requested authentication domain. |  -  |

<a id="patchLdapService"></a>
# **patchLdapService**
> LdapServiceSummary patchLdapService(id, ldapServiceInfoUpdate)

Update an existing authentication domain

Modify the values of a specified authentication domain object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LdapServiceApi;

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

    LdapServiceApi apiInstance = new LdapServiceApi(defaultClient);
    String id = "id_example"; // String | ID of the authentication domain to be updated.
    LdapServiceInfoUpdate ldapServiceInfoUpdate = new LdapServiceInfoUpdate(); // LdapServiceInfoUpdate | Information for updating an authentication domain.
    try {
      LdapServiceSummary result = apiInstance.patchLdapService(id, ldapServiceInfoUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LdapServiceApi#patchLdapService");
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
| **id** | **String**| ID of the authentication domain to be updated. | |
| **ldapServiceInfoUpdate** | [**LdapServiceInfoUpdate**](LdapServiceInfoUpdate.md)| Information for updating an authentication domain. | |

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a summary of the newly updated authentication domain. |  -  |

<a id="putLdapService"></a>
# **putLdapService**
> LdapServiceSummary putLdapService(id, ldapServiceInfoUpdate)

Replace the values of an authentication domain

Replace the values of a specified authentication domain object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LdapServiceApi;

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

    LdapServiceApi apiInstance = new LdapServiceApi(defaultClient);
    String id = "id_example"; // String | ID of the authentication domain to be updated.
    LdapServiceInfoUpdate ldapServiceInfoUpdate = new LdapServiceInfoUpdate(); // LdapServiceInfoUpdate | Information for updating an authentication domain.
    try {
      LdapServiceSummary result = apiInstance.putLdapService(id, ldapServiceInfoUpdate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LdapServiceApi#putLdapService");
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
| **id** | **String**| ID of the authentication domain to be updated. | |
| **ldapServiceInfoUpdate** | [**LdapServiceInfoUpdate**](LdapServiceInfoUpdate.md)| Information for updating an authentication domain. | |

### Return type

[**LdapServiceSummary**](LdapServiceSummary.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns a summary of the newly updated authentication domain. |  -  |

<a id="queryLdapService"></a>
# **queryLdapService**
> LdapServiceSummaryListResponse queryLdapService()

Get a list of LDAP services

Get a list of LDAP services.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LdapServiceApi;

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

    LdapServiceApi apiInstance = new LdapServiceApi(defaultClient);
    try {
      LdapServiceSummaryListResponse result = apiInstance.queryLdapService();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LdapServiceApi#queryLdapService");
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

[**LdapServiceSummaryListResponse**](LdapServiceSummaryListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Returns the list of authentication domains. |  -  |

