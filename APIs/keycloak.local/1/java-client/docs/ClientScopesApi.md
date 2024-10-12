# ClientScopesApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientScopesGet**](ClientScopesApi.md#realmClientScopesGet) | **GET** /{realm}/client-scopes | Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm |
| [**realmClientScopesIdDelete**](ClientScopesApi.md#realmClientScopesIdDelete) | **DELETE** /{realm}/client-scopes/{id} | Delete the client scope |
| [**realmClientScopesIdGet**](ClientScopesApi.md#realmClientScopesIdGet) | **GET** /{realm}/client-scopes/{id} | Get representation of the client scope |
| [**realmClientScopesIdPut**](ClientScopesApi.md#realmClientScopesIdPut) | **PUT** /{realm}/client-scopes/{id} | Update the client scope |
| [**realmClientScopesPost**](ClientScopesApi.md#realmClientScopesPost) | **POST** /{realm}/client-scopes | Create a new client scope   Client Scope’s name must be unique! |


<a id="realmClientScopesGet"></a>
# **realmClientScopesGet**
> List&lt;ClientScopeRepresentation&gt; realmClientScopesGet(realm)

Get client scopes belonging to the realm   Returns a list of client scopes belonging to the realm

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientScopesApi apiInstance = new ClientScopesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<ClientScopeRepresentation> result = apiInstance.realmClientScopesGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientScopesApi#realmClientScopesGet");
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
| **realm** | **String**| realm name (not id!) | |

### Return type

[**List&lt;ClientScopeRepresentation&gt;**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdDelete"></a>
# **realmClientScopesIdDelete**
> realmClientScopesIdDelete(realm, id)

Delete the client scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientScopesApi apiInstance = new ClientScopesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      apiInstance.realmClientScopesIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientScopesApi#realmClientScopesIdDelete");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client scope (not name) | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdGet"></a>
# **realmClientScopesIdGet**
> ClientScopeRepresentation realmClientScopesIdGet(realm, id)

Get representation of the client scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientScopesApi apiInstance = new ClientScopesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      ClientScopeRepresentation result = apiInstance.realmClientScopesIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientScopesApi#realmClientScopesIdGet");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client scope (not name) | |

### Return type

[**ClientScopeRepresentation**](ClientScopeRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdPut"></a>
# **realmClientScopesIdPut**
> realmClientScopesIdPut(realm, id, clientScopeRepresentation)

Update the client scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientScopesApi apiInstance = new ClientScopesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    ClientScopeRepresentation clientScopeRepresentation = new ClientScopeRepresentation(); // ClientScopeRepresentation | 
    try {
      apiInstance.realmClientScopesIdPut(realm, id, clientScopeRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientScopesApi#realmClientScopesIdPut");
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
| **realm** | **String**| realm name (not id!) | |
| **id** | **String**| id of client scope (not name) | |
| **clientScopeRepresentation** | [**ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesPost"></a>
# **realmClientScopesPost**
> realmClientScopesPost(realm, clientScopeRepresentation)

Create a new client scope   Client Scope’s name must be unique!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientScopesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientScopesApi apiInstance = new ClientScopesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    ClientScopeRepresentation clientScopeRepresentation = new ClientScopeRepresentation(); // ClientScopeRepresentation | 
    try {
      apiInstance.realmClientScopesPost(realm, clientScopeRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientScopesApi#realmClientScopesPost");
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
| **realm** | **String**| realm name (not id!) | |
| **clientScopeRepresentation** | [**ClientScopeRepresentation**](ClientScopeRepresentation.md)|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

