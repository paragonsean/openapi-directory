# StatusApi

All URIs are relative to *http://conjur.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAuthenticators**](StatusApi.md#getAuthenticators) | **GET** /authenticators | Details about which authenticators are on the Conjur Server |
| [**getGCPAuthenticatorStatus**](StatusApi.md#getGCPAuthenticatorStatus) | **GET** /authn-gcp/{account}/status | Details whether an authentication service has been configured properly |
| [**getServiceAuthenticatorStatus**](StatusApi.md#getServiceAuthenticatorStatus) | **GET** /{authenticator}/{service_id}/{account}/status | Details whether an authentication service has been configured properly |
| [**health**](StatusApi.md#health) | **GET** /health | Health info about conjur |
| [**info**](StatusApi.md#info) | **GET** /info | Basic information about the Conjur Enterprise server |
| [**remoteHealth**](StatusApi.md#remoteHealth) | **GET** /remote_health/{remote} | Health info about a given Conjur Enterprise server |
| [**whoAmI**](StatusApi.md#whoAmI) | **GET** /whoami | Provides information about the client making an API request. |


<a id="getAuthenticators"></a>
# **getAuthenticators**
> GetAuthenticators200Response getAuthenticators(xRequestId)

Details about which authenticators are on the Conjur Server

Response contains three members: installed, configured, and enabled.  installed: The authenticator is implemented in Conjur and is available for configuration configured: The authenticator has a webservice in the DB that was loaded by policy enabled: The authenticator is enabled (in the DB or in the ENV) and is ready for authentication 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");


    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    try {
      GetAuthenticators200Response result = apiInstance.getAuthenticators(xRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getAuthenticators");
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
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |

### Return type

[**GetAuthenticators200Response**](GetAuthenticators200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about authenticators for this Conjur server |  -  |

<a id="getGCPAuthenticatorStatus"></a>
# **getGCPAuthenticatorStatus**
> getGCPAuthenticatorStatus(account, xRequestId)

Details whether an authentication service has been configured properly

Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  This operation only supports the GCP authenticator  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String account = "dev"; // String | The organization account name
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    try {
      apiInstance.getGCPAuthenticatorStatus(account, xRequestId);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getGCPAuthenticatorStatus");
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
| **account** | **String**| The organization account name | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |

### Return type

null (empty response body)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **404** | The service was not found |  -  |
| **500** |  |  -  |
| **501** |  |  -  |

<a id="getServiceAuthenticatorStatus"></a>
# **getServiceAuthenticatorStatus**
> GetServiceAuthenticatorStatus200Response getServiceAuthenticatorStatus(authenticator, serviceId, account, xRequestId)

Details whether an authentication service has been configured properly

Once the status webservice has been properly configured and the relevant user groups have been given permissions to access the status webservice, the users in those groups can check the status of the authenticator.  Supported Authenticators:   - Azure   - OIDC  Not Supported:   - AWS IAM   - Kubernetes   - LDAP  See [Conjur Documentation](https://docs.conjur.org/Latest/en/Content/Integrations/Authn-status.htm) for details on setting up the authenticator status webservice. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String authenticator = "authn-oidc"; // String | The type of authenticator
    String serviceId = "prod%2fgke"; // String | URL-Encoded authenticator service ID
    String account = "dev"; // String | The organization account name
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    try {
      GetServiceAuthenticatorStatus200Response result = apiInstance.getServiceAuthenticatorStatus(authenticator, serviceId, account, xRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#getServiceAuthenticatorStatus");
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
| **authenticator** | **String**| The type of authenticator | |
| **serviceId** | **String**| URL-Encoded authenticator service ID | |
| **account** | **String**| The organization account name | |
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |

### Return type

[**GetServiceAuthenticatorStatus200Response**](GetServiceAuthenticatorStatus200Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The response contains info about the result |  -  |
| **400** | The server cannot process the request due to malformed request syntax |  -  |
| **401** | Authentication information is missing or invalid |  -  |
| **403** | The authenticated user lacks the necessary privileges |  -  |
| **404** | The service was not found |  -  |
| **500** |  |  -  |
| **501** |  |  -  |

<a id="health"></a>
# **health**
> Object health()

Health info about conjur

You can request health checks against any cluster node using the Conjur API. These routes do not require authentication.  The health check attempts an internal HTTP or TCP connection to each Conjur Enterprise service. It also attempts a simple transaction against all internal databases. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");


    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    try {
      Object result = apiInstance.health();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#health");
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

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tests were successful |  -  |
| **502** | The tests failed |  -  |

<a id="info"></a>
# **info**
> Info200Response info()

Basic information about the Conjur Enterprise server

Information about the Conjur Enterprise node which was queried against.  Includes authenticator info, release/version info, configuration details, internal services, and role information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");


    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    try {
      Info200Response result = apiInstance.info();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#info");
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

[**Info200Response**](Info200Response.md)

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | info |  -  |

<a id="remoteHealth"></a>
# **remoteHealth**
> Object remoteHealth(remote)

Health info about a given Conjur Enterprise server

Use the remote_health route to check the health of any Conjur Enterprise Server from any other Conjur Enterprise Server. With this route, you can check master health relative to a follower, or follower health relative to a standby, and so on. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");


    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String remote = "conjur.myorg.com"; // String | The hostname of the remote to check
    try {
      Object result = apiInstance.remoteHealth(remote);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#remoteHealth");
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
| **remote** | **String**| The hostname of the remote to check | |

### Return type

**Object**

### Authorization

[basicAuth](../README.md#basicAuth), [conjurKubernetesMutualTls](../README.md#conjurKubernetesMutualTls), [conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The tests were successful |  -  |
| **502** | The tests failed |  -  |

<a id="whoAmI"></a>
# **whoAmI**
> WhoAmI200Response whoAmI(xRequestId)

Provides information about the client making an API request.

WhoAmI provides information about the client making an API request. It can be used to help troubleshoot configuration by verifying authentication and the client IP address for audit and network access restrictions. For more information, see Host Attributes. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://conjur.local");
    
    // Configure API key authorization: conjurAuth
    ApiKeyAuth conjurAuth = (ApiKeyAuth) defaultClient.getAuthentication("conjurAuth");
    conjurAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //conjurAuth.setApiKeyPrefix("Token");

    StatusApi apiInstance = new StatusApi(defaultClient);
    String xRequestId = "test-id"; // String | Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one. 
    try {
      WhoAmI200Response result = apiInstance.whoAmI(xRequestId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StatusApi#whoAmI");
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
| **xRequestId** | **String**| Add an ID to the request being made so it can be tracked in Conjur. If not provided the server will automatically generate one.  | [optional] |

### Return type

[**WhoAmI200Response**](WhoAmI200Response.md)

### Authorization

[conjurAuth](../README.md#conjurAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details about the client making the request |  -  |
| **401** | Authentication information is missing or invalid |  -  |

