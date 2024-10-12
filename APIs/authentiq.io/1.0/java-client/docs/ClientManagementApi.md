# ClientManagementApi

All URIs are relative to *https://connect.authentiq.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**client**](ClientManagementApi.md#client) | **GET** /client | List clients |
| [**clientClientId**](ClientManagementApi.md#clientClientId) | **DELETE** /client/{client_id} | Delete a client |
| [**createClient**](ClientManagementApi.md#createClient) | **POST** /client | Register a client |
| [**getClient**](ClientManagementApi.md#getClient) | **GET** /client/{client_id} | View a client |
| [**updateClient**](ClientManagementApi.md#updateClient) | **PUT** /client/{client_id} | Update a client |


<a id="client"></a>
# **client**
> List&lt;Client&gt; client()

List clients

Retrieve a list of clients. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.authentiq.io");
    
    // Configure API key authorization: client_registration_token
    ApiKeyAuth client_registration_token = (ApiKeyAuth) defaultClient.getAuthentication("client_registration_token");
    client_registration_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //client_registration_token.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth_code
    OAuth oauth_code = (OAuth) defaultClient.getAuthentication("oauth_code");
    oauth_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth_implicit
    OAuth oauth_implicit = (OAuth) defaultClient.getAuthentication("oauth_implicit");
    oauth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    ClientManagementApi apiInstance = new ClientManagementApi(defaultClient);
    try {
      List<Client> result = apiInstance.client();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientManagementApi#client");
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

[**List&lt;Client&gt;**](Client.md)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A list of Client Objects. |  -  |
| **0** | OAuth 2.0 error response |  -  |

<a id="clientClientId"></a>
# **clientClientId**
> clientClientId(clientId)

Delete a client

Delete a previously registered client. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.authentiq.io");
    
    // Configure API key authorization: client_registration_token
    ApiKeyAuth client_registration_token = (ApiKeyAuth) defaultClient.getAuthentication("client_registration_token");
    client_registration_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //client_registration_token.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth_code
    OAuth oauth_code = (OAuth) defaultClient.getAuthentication("oauth_code");
    oauth_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth_implicit
    OAuth oauth_implicit = (OAuth) defaultClient.getAuthentication("oauth_implicit");
    oauth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    ClientManagementApi apiInstance = new ClientManagementApi(defaultClient);
    String clientId = "clientId_example"; // String | Client identifier
    try {
      apiInstance.clientClientId(clientId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientManagementApi#clientClientId");
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
| **clientId** | **String**| Client identifier | |

### Return type

null (empty response body)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Client deleted |  -  |
| **0** | Problem Detail error response |  -  |

<a id="createClient"></a>
# **createClient**
> createClient(client)

Register a client

Register a new client with this Authentiq Connect provider.  This endpoint is compatible with [OIDC&#39;s Client Registration](http://openid.net/specs/openid-connect-registration-1_0.html) extension. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.authentiq.io");
    
    // Configure API key authorization: client_registration_token
    ApiKeyAuth client_registration_token = (ApiKeyAuth) defaultClient.getAuthentication("client_registration_token");
    client_registration_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //client_registration_token.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth_code
    OAuth oauth_code = (OAuth) defaultClient.getAuthentication("oauth_code");
    oauth_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth_implicit
    OAuth oauth_implicit = (OAuth) defaultClient.getAuthentication("oauth_implicit");
    oauth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    ClientManagementApi apiInstance = new ClientManagementApi(defaultClient);
    Client client = new Client(); // Client | Client Object
    try {
      apiInstance.createClient(client);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientManagementApi#createClient");
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
| **client** | [**Client**](Client.md)| Client Object | |

### Return type

null (empty response body)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Client created |  * Location - URL of new client resource <br>  |
| **0** | Problem Detail error response |  -  |

<a id="getClient"></a>
# **getClient**
> Client getClient(clientId)

View a client

Retrieve the configuration of a previously registered client. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.authentiq.io");
    
    // Configure API key authorization: client_registration_token
    ApiKeyAuth client_registration_token = (ApiKeyAuth) defaultClient.getAuthentication("client_registration_token");
    client_registration_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //client_registration_token.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth_code
    OAuth oauth_code = (OAuth) defaultClient.getAuthentication("oauth_code");
    oauth_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth_implicit
    OAuth oauth_implicit = (OAuth) defaultClient.getAuthentication("oauth_implicit");
    oauth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    ClientManagementApi apiInstance = new ClientManagementApi(defaultClient);
    String clientId = "clientId_example"; // String | Client identifier
    try {
      Client result = apiInstance.getClient(clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientManagementApi#getClient");
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
| **clientId** | **String**| Client identifier | |

### Return type

[**Client**](Client.md)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client found |  -  |
| **0** | OAuth 2.0 error response |  -  |

<a id="updateClient"></a>
# **updateClient**
> Client updateClient(clientId, client)

Update a client

Update the configuration of a previously registered client. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.authentiq.io");
    
    // Configure API key authorization: client_registration_token
    ApiKeyAuth client_registration_token = (ApiKeyAuth) defaultClient.getAuthentication("client_registration_token");
    client_registration_token.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //client_registration_token.setApiKeyPrefix("Token");

    // Configure OAuth2 access token for authorization: oauth_code
    OAuth oauth_code = (OAuth) defaultClient.getAuthentication("oauth_code");
    oauth_code.setAccessToken("YOUR ACCESS TOKEN");

    // Configure OAuth2 access token for authorization: oauth_implicit
    OAuth oauth_implicit = (OAuth) defaultClient.getAuthentication("oauth_implicit");
    oauth_implicit.setAccessToken("YOUR ACCESS TOKEN");

    ClientManagementApi apiInstance = new ClientManagementApi(defaultClient);
    String clientId = "clientId_example"; // String | Client identifier
    Client client = new Client(); // Client | Client Object
    try {
      Client result = apiInstance.updateClient(clientId, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientManagementApi#updateClient");
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
| **clientId** | **String**| Client identifier | |
| **client** | [**Client**](Client.md)| Client Object | |

### Return type

[**Client**](Client.md)

### Authorization

[client_registration_token](../README.md#client_registration_token), [oauth_code](../README.md#oauth_code), [oauth_implicit](../README.md#oauth_implicit)

### HTTP request headers

 - **Content-Type**: application/json, multipart/form-data
 - **Accept**: application/json, application/problem+json, application/x-www-form-urlencoded, text/html

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Client updated |  -  |
| **0** | Problem Detail error response |  -  |

