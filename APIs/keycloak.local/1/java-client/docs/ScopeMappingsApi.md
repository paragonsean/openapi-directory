# ScopeMappingsApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientScopesIdScopeMappingsClientsClientAvailableGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientAvailableGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client}/available | The available client-level roles   Returns the roles for the client that can be associated with the client’s scope |
| [**realmClientScopesIdScopeMappingsClientsClientCompositeGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientCompositeGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client}/composite | Get effective client roles   Returns the roles for the client that are associated with the client’s scope. |
| [**realmClientScopesIdScopeMappingsClientsClientDelete**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientDelete) | **DELETE** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Remove client-level roles from the client’s scope. |
| [**realmClientScopesIdScopeMappingsClientsClientGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Get the roles associated with a client’s scope   Returns roles for the client. |
| [**realmClientScopesIdScopeMappingsClientsClientPost**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsClientsClientPost) | **POST** /{realm}/client-scopes/{id}/scope-mappings/clients/{client} | Add client-level roles to the client’s scope |
| [**realmClientScopesIdScopeMappingsGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings | Get all scope mappings for the client |
| [**realmClientScopesIdScopeMappingsRealmAvailableGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmAvailableGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client’s scope |
| [**realmClientScopesIdScopeMappingsRealmCompositeGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmCompositeGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists. |
| [**realmClientScopesIdScopeMappingsRealmDelete**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmDelete) | **DELETE** /{realm}/client-scopes/{id}/scope-mappings/realm | Remove a set of realm-level roles from the client’s scope |
| [**realmClientScopesIdScopeMappingsRealmGet**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmGet) | **GET** /{realm}/client-scopes/{id}/scope-mappings/realm | Get realm-level roles associated with the client’s scope |
| [**realmClientScopesIdScopeMappingsRealmPost**](ScopeMappingsApi.md#realmClientScopesIdScopeMappingsRealmPost) | **POST** /{realm}/client-scopes/{id}/scope-mappings/realm | Add a set of realm-level roles to the client’s scope |
| [**realmClientsIdScopeMappingsClientsClientAvailableGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientAvailableGet) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client}/available | The available client-level roles   Returns the roles for the client that can be associated with the client’s scope |
| [**realmClientsIdScopeMappingsClientsClientCompositeGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientCompositeGet) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client}/composite | Get effective client roles   Returns the roles for the client that are associated with the client’s scope. |
| [**realmClientsIdScopeMappingsClientsClientDelete**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientDelete) | **DELETE** /{realm}/clients/{id}/scope-mappings/clients/{client} | Remove client-level roles from the client’s scope. |
| [**realmClientsIdScopeMappingsClientsClientGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientGet) | **GET** /{realm}/clients/{id}/scope-mappings/clients/{client} | Get the roles associated with a client’s scope   Returns roles for the client. |
| [**realmClientsIdScopeMappingsClientsClientPost**](ScopeMappingsApi.md#realmClientsIdScopeMappingsClientsClientPost) | **POST** /{realm}/clients/{id}/scope-mappings/clients/{client} | Add client-level roles to the client’s scope |
| [**realmClientsIdScopeMappingsGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsGet) | **GET** /{realm}/clients/{id}/scope-mappings | Get all scope mappings for the client |
| [**realmClientsIdScopeMappingsRealmAvailableGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmAvailableGet) | **GET** /{realm}/clients/{id}/scope-mappings/realm/available | Get realm-level roles that are available to attach to this client’s scope |
| [**realmClientsIdScopeMappingsRealmCompositeGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmCompositeGet) | **GET** /{realm}/clients/{id}/scope-mappings/realm/composite | Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists. |
| [**realmClientsIdScopeMappingsRealmDelete**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmDelete) | **DELETE** /{realm}/clients/{id}/scope-mappings/realm | Remove a set of realm-level roles from the client’s scope |
| [**realmClientsIdScopeMappingsRealmGet**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmGet) | **GET** /{realm}/clients/{id}/scope-mappings/realm | Get realm-level roles associated with the client’s scope |
| [**realmClientsIdScopeMappingsRealmPost**](ScopeMappingsApi.md#realmClientsIdScopeMappingsRealmPost) | **POST** /{realm}/clients/{id}/scope-mappings/realm | Add a set of realm-level roles to the client’s scope |


<a id="realmClientScopesIdScopeMappingsClientsClientAvailableGet"></a>
# **realmClientScopesIdScopeMappingsClientsClientAvailableGet**
> List&lt;RoleRepresentation&gt; realmClientScopesIdScopeMappingsClientsClientAvailableGet(realm, id, client)

The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientScopesIdScopeMappingsClientsClientAvailableGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsClientsClientAvailableGet");
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
| **client** | **String**|  | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsClientsClientCompositeGet"></a>
# **realmClientScopesIdScopeMappingsClientsClientCompositeGet**
> List&lt;RoleRepresentation&gt; realmClientScopesIdScopeMappingsClientsClientCompositeGet(realm, id, client)

Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientScopesIdScopeMappingsClientsClientCompositeGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsClientsClientCompositeGet");
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
| **client** | **String**|  | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsClientsClientDelete"></a>
# **realmClientScopesIdScopeMappingsClientsClientDelete**
> realmClientScopesIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Remove client-level roles from the client’s scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientScopesIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsClientsClientDelete");
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
| **client** | **String**|  | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientScopesIdScopeMappingsClientsClientGet"></a>
# **realmClientScopesIdScopeMappingsClientsClientGet**
> List&lt;RoleRepresentation&gt; realmClientScopesIdScopeMappingsClientsClientGet(realm, id, client)

Get the roles associated with a client’s scope   Returns roles for the client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientScopesIdScopeMappingsClientsClientGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsClientsClientGet");
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
| **client** | **String**|  | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsClientsClientPost"></a>
# **realmClientScopesIdScopeMappingsClientsClientPost**
> realmClientScopesIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientScopesIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsClientsClientPost");
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
| **client** | **String**|  | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientScopesIdScopeMappingsGet"></a>
# **realmClientScopesIdScopeMappingsGet**
> MappingsRepresentation realmClientScopesIdScopeMappingsGet(realm, id)

Get all scope mappings for the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      MappingsRepresentation result = apiInstance.realmClientScopesIdScopeMappingsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsGet");
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

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsRealmAvailableGet"></a>
# **realmClientScopesIdScopeMappingsRealmAvailableGet**
> List&lt;RoleRepresentation&gt; realmClientScopesIdScopeMappingsRealmAvailableGet(realm, id)

Get realm-level roles that are available to attach to this client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientScopesIdScopeMappingsRealmAvailableGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsRealmAvailableGet");
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

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsRealmCompositeGet"></a>
# **realmClientScopesIdScopeMappingsRealmCompositeGet**
> List&lt;RoleRepresentation&gt; realmClientScopesIdScopeMappingsRealmCompositeGet(realm, id)

Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientScopesIdScopeMappingsRealmCompositeGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsRealmCompositeGet");
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

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsRealmDelete"></a>
# **realmClientScopesIdScopeMappingsRealmDelete**
> realmClientScopesIdScopeMappingsRealmDelete(realm, id, roleRepresentation)

Remove a set of realm-level roles from the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientScopesIdScopeMappingsRealmDelete(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsRealmDelete");
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
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientScopesIdScopeMappingsRealmGet"></a>
# **realmClientScopesIdScopeMappingsRealmGet**
> List&lt;RoleRepresentation&gt; realmClientScopesIdScopeMappingsRealmGet(realm, id)

Get realm-level roles associated with the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientScopesIdScopeMappingsRealmGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsRealmGet");
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

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientScopesIdScopeMappingsRealmPost"></a>
# **realmClientScopesIdScopeMappingsRealmPost**
> realmClientScopesIdScopeMappingsRealmPost(realm, id, roleRepresentation)

Add a set of realm-level roles to the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client scope (not name)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientScopesIdScopeMappingsRealmPost(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientScopesIdScopeMappingsRealmPost");
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
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientsIdScopeMappingsClientsClientAvailableGet"></a>
# **realmClientsIdScopeMappingsClientsClientAvailableGet**
> List&lt;RoleRepresentation&gt; realmClientsIdScopeMappingsClientsClientAvailableGet(realm, id, client)

The available client-level roles   Returns the roles for the client that can be associated with the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdScopeMappingsClientsClientAvailableGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsClientsClientAvailableGet");
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
| **id** | **String**| id of client (not client-id) | |
| **client** | **String**|  | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsClientsClientCompositeGet"></a>
# **realmClientsIdScopeMappingsClientsClientCompositeGet**
> List&lt;RoleRepresentation&gt; realmClientsIdScopeMappingsClientsClientCompositeGet(realm, id, client)

Get effective client roles   Returns the roles for the client that are associated with the client’s scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdScopeMappingsClientsClientCompositeGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsClientsClientCompositeGet");
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
| **id** | **String**| id of client (not client-id) | |
| **client** | **String**|  | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsClientsClientDelete"></a>
# **realmClientsIdScopeMappingsClientsClientDelete**
> realmClientsIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Remove client-level roles from the client’s scope.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientsIdScopeMappingsClientsClientDelete(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsClientsClientDelete");
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
| **id** | **String**| id of client (not client-id) | |
| **client** | **String**|  | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientsIdScopeMappingsClientsClientGet"></a>
# **realmClientsIdScopeMappingsClientsClientGet**
> List&lt;RoleRepresentation&gt; realmClientsIdScopeMappingsClientsClientGet(realm, id, client)

Get the roles associated with a client’s scope   Returns roles for the client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdScopeMappingsClientsClientGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsClientsClientGet");
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
| **id** | **String**| id of client (not client-id) | |
| **client** | **String**|  | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsClientsClientPost"></a>
# **realmClientsIdScopeMappingsClientsClientPost**
> realmClientsIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientsIdScopeMappingsClientsClientPost(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsClientsClientPost");
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
| **id** | **String**| id of client (not client-id) | |
| **client** | **String**|  | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientsIdScopeMappingsGet"></a>
# **realmClientsIdScopeMappingsGet**
> MappingsRepresentation realmClientsIdScopeMappingsGet(realm, id)

Get all scope mappings for the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      MappingsRepresentation result = apiInstance.realmClientsIdScopeMappingsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsGet");
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
| **id** | **String**| id of client (not client-id) | |

### Return type

[**MappingsRepresentation**](MappingsRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsRealmAvailableGet"></a>
# **realmClientsIdScopeMappingsRealmAvailableGet**
> List&lt;RoleRepresentation&gt; realmClientsIdScopeMappingsRealmAvailableGet(realm, id)

Get realm-level roles that are available to attach to this client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdScopeMappingsRealmAvailableGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsRealmAvailableGet");
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
| **id** | **String**| id of client (not client-id) | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsRealmCompositeGet"></a>
# **realmClientsIdScopeMappingsRealmCompositeGet**
> List&lt;RoleRepresentation&gt; realmClientsIdScopeMappingsRealmCompositeGet(realm, id)

Get effective realm-level roles associated with the client’s scope   What this does is recurse  any composite roles associated with the client’s scope and adds the roles to this lists.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdScopeMappingsRealmCompositeGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsRealmCompositeGet");
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
| **id** | **String**| id of client (not client-id) | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsRealmDelete"></a>
# **realmClientsIdScopeMappingsRealmDelete**
> realmClientsIdScopeMappingsRealmDelete(realm, id, roleRepresentation)

Remove a set of realm-level roles from the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientsIdScopeMappingsRealmDelete(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsRealmDelete");
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
| **id** | **String**| id of client (not client-id) | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

<a id="realmClientsIdScopeMappingsRealmGet"></a>
# **realmClientsIdScopeMappingsRealmGet**
> List&lt;RoleRepresentation&gt; realmClientsIdScopeMappingsRealmGet(realm, id)

Get realm-level roles associated with the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdScopeMappingsRealmGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsRealmGet");
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
| **id** | **String**| id of client (not client-id) | |

### Return type

[**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdScopeMappingsRealmPost"></a>
# **realmClientsIdScopeMappingsRealmPost**
> realmClientsIdScopeMappingsRealmPost(realm, id, roleRepresentation)

Add a set of realm-level roles to the client’s scope

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScopeMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ScopeMappingsApi apiInstance = new ScopeMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientsIdScopeMappingsRealmPost(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScopeMappingsApi#realmClientsIdScopeMappingsRealmPost");
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
| **id** | **String**| id of client (not client-id) | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)|  | |

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

