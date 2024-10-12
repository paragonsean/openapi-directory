# IntegrationsApi

All URIs are relative to *https://app.apacta.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getIntegrationsContactsSync**](IntegrationsApi.md#getIntegrationsContactsSync) | **GET** /integrations/contactsSync | Force Synchronization with ERP systems |
| [**getIntegrationsList**](IntegrationsApi.md#getIntegrationsList) | **GET** /integrations | Get integrations list |
| [**getIntegrationsView**](IntegrationsApi.md#getIntegrationsView) | **GET** /integrations/{integration_id} | View integration details |
| [**integrationsBillysAuthenticatePost**](IntegrationsApi.md#integrationsBillysAuthenticatePost) | **POST** /integrations/billysAuthenticate | Authenticate to Billys |
| [**integrationsProductsSyncGet**](IntegrationsApi.md#integrationsProductsSyncGet) | **GET** /integrations/productsSync | Sync products from erp integration |


<a id="getIntegrationsContactsSync"></a>
# **getIntegrationsContactsSync**
> GetIntegrationsList200Response getIntegrationsContactsSync()

Force Synchronization with ERP systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    try {
      GetIntegrationsList200Response result = apiInstance.getIntegrationsContactsSync();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#getIntegrationsContactsSync");
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

[**GetIntegrationsList200Response**](GetIntegrationsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getIntegrationsList"></a>
# **getIntegrationsList**
> GetIntegrationsList200Response getIntegrationsList()

Get integrations list

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    try {
      GetIntegrationsList200Response result = apiInstance.getIntegrationsList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#getIntegrationsList");
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

[**GetIntegrationsList200Response**](GetIntegrationsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="getIntegrationsView"></a>
# **getIntegrationsView**
> GetIntegrationsList200Response getIntegrationsView(integrationId)

View integration details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    String integrationId = "integrationId_example"; // String | Automatically added
    try {
      GetIntegrationsList200Response result = apiInstance.getIntegrationsView(integrationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#getIntegrationsView");
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
| **integrationId** | **String**| Automatically added | |

### Return type

[**GetIntegrationsList200Response**](GetIntegrationsList200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="integrationsBillysAuthenticatePost"></a>
# **integrationsBillysAuthenticatePost**
> IntegrationsBillysAuthenticatePost200Response integrationsBillysAuthenticatePost()

Authenticate to Billys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    try {
      IntegrationsBillysAuthenticatePost200Response result = apiInstance.integrationsBillysAuthenticatePost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#integrationsBillysAuthenticatePost");
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

[**IntegrationsBillysAuthenticatePost200Response**](IntegrationsBillysAuthenticatePost200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

<a id="integrationsProductsSyncGet"></a>
# **integrationsProductsSyncGet**
> IntegrationsProductsSyncGet200Response integrationsProductsSyncGet()

Sync products from erp integration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IntegrationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://app.apacta.com/api/v1");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: X-Auth-Token
    ApiKeyAuth X-Auth-Token = (ApiKeyAuth) defaultClient.getAuthentication("X-Auth-Token");
    X-Auth-Token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //X-Auth-Token.setApiKeyPrefix("Token");

    IntegrationsApi apiInstance = new IntegrationsApi(defaultClient);
    try {
      IntegrationsProductsSyncGet200Response result = apiInstance.integrationsProductsSyncGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IntegrationsApi#integrationsProductsSyncGet");
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

[**IntegrationsProductsSyncGet200Response**](IntegrationsProductsSyncGet200Response.md)

### Authorization

[api_key](../README.md#api_key), [X-Auth-Token](../README.md#X-Auth-Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |

