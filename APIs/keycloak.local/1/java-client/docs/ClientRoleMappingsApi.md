# ClientRoleMappingsApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmGroupsIdRoleMappingsClientsClientAvailableGet**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientAvailableGet) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client}/available | Get available client-level roles that can be mapped to the user |
| [**realmGroupsIdRoleMappingsClientsClientCompositeGet**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientCompositeGet) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client}/composite | Get effective client-level role mappings   This recurses any composite roles |
| [**realmGroupsIdRoleMappingsClientsClientDelete**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientDelete) | **DELETE** /{realm}/groups/{id}/role-mappings/clients/{client} | Delete client-level roles from user role mapping |
| [**realmGroupsIdRoleMappingsClientsClientGet**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientGet) | **GET** /{realm}/groups/{id}/role-mappings/clients/{client} | Get client-level role mappings for the user, and the app |
| [**realmGroupsIdRoleMappingsClientsClientPost**](ClientRoleMappingsApi.md#realmGroupsIdRoleMappingsClientsClientPost) | **POST** /{realm}/groups/{id}/role-mappings/clients/{client} | Add client-level roles to the user role mapping |
| [**realmUsersIdRoleMappingsClientsClientAvailableGet**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientAvailableGet) | **GET** /{realm}/users/{id}/role-mappings/clients/{client}/available | Get available client-level roles that can be mapped to the user |
| [**realmUsersIdRoleMappingsClientsClientCompositeGet**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientCompositeGet) | **GET** /{realm}/users/{id}/role-mappings/clients/{client}/composite | Get effective client-level role mappings   This recurses any composite roles |
| [**realmUsersIdRoleMappingsClientsClientDelete**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientDelete) | **DELETE** /{realm}/users/{id}/role-mappings/clients/{client} | Delete client-level roles from user role mapping |
| [**realmUsersIdRoleMappingsClientsClientGet**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientGet) | **GET** /{realm}/users/{id}/role-mappings/clients/{client} | Get client-level role mappings for the user, and the app |
| [**realmUsersIdRoleMappingsClientsClientPost**](ClientRoleMappingsApi.md#realmUsersIdRoleMappingsClientsClientPost) | **POST** /{realm}/users/{id}/role-mappings/clients/{client} | Add client-level roles to the user role mapping |


<a id="realmGroupsIdRoleMappingsClientsClientAvailableGet"></a>
# **realmGroupsIdRoleMappingsClientsClientAvailableGet**
> List&lt;RoleRepresentation&gt; realmGroupsIdRoleMappingsClientsClientAvailableGet(realm, id, client)

Get available client-level roles that can be mapped to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmGroupsIdRoleMappingsClientsClientAvailableGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmGroupsIdRoleMappingsClientsClientAvailableGet");
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
| **id** | **String**|  | |
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

<a id="realmGroupsIdRoleMappingsClientsClientCompositeGet"></a>
# **realmGroupsIdRoleMappingsClientsClientCompositeGet**
> List&lt;RoleRepresentation&gt; realmGroupsIdRoleMappingsClientsClientCompositeGet(realm, id, client)

Get effective client-level role mappings   This recurses any composite roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmGroupsIdRoleMappingsClientsClientCompositeGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmGroupsIdRoleMappingsClientsClientCompositeGet");
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
| **id** | **String**|  | |
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

<a id="realmGroupsIdRoleMappingsClientsClientDelete"></a>
# **realmGroupsIdRoleMappingsClientsClientDelete**
> realmGroupsIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Delete client-level roles from user role mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmGroupsIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmGroupsIdRoleMappingsClientsClientDelete");
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
| **id** | **String**|  | |
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

<a id="realmGroupsIdRoleMappingsClientsClientGet"></a>
# **realmGroupsIdRoleMappingsClientsClientGet**
> List&lt;RoleRepresentation&gt; realmGroupsIdRoleMappingsClientsClientGet(realm, id, client)

Get client-level role mappings for the user, and the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmGroupsIdRoleMappingsClientsClientGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmGroupsIdRoleMappingsClientsClientGet");
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
| **id** | **String**|  | |
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

<a id="realmGroupsIdRoleMappingsClientsClientPost"></a>
# **realmGroupsIdRoleMappingsClientsClientPost**
> realmGroupsIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the user role mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | 
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmGroupsIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmGroupsIdRoleMappingsClientsClientPost");
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
| **id** | **String**|  | |
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

<a id="realmUsersIdRoleMappingsClientsClientAvailableGet"></a>
# **realmUsersIdRoleMappingsClientsClientAvailableGet**
> List&lt;RoleRepresentation&gt; realmUsersIdRoleMappingsClientsClientAvailableGet(realm, id, client)

Get available client-level roles that can be mapped to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmUsersIdRoleMappingsClientsClientAvailableGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmUsersIdRoleMappingsClientsClientAvailableGet");
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
| **id** | **String**| User id | |
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

<a id="realmUsersIdRoleMappingsClientsClientCompositeGet"></a>
# **realmUsersIdRoleMappingsClientsClientCompositeGet**
> List&lt;RoleRepresentation&gt; realmUsersIdRoleMappingsClientsClientCompositeGet(realm, id, client)

Get effective client-level role mappings   This recurses any composite roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmUsersIdRoleMappingsClientsClientCompositeGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmUsersIdRoleMappingsClientsClientCompositeGet");
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
| **id** | **String**| User id | |
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

<a id="realmUsersIdRoleMappingsClientsClientDelete"></a>
# **realmUsersIdRoleMappingsClientsClientDelete**
> realmUsersIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation)

Delete client-level roles from user role mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmUsersIdRoleMappingsClientsClientDelete(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmUsersIdRoleMappingsClientsClientDelete");
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
| **id** | **String**| User id | |
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

<a id="realmUsersIdRoleMappingsClientsClientGet"></a>
# **realmUsersIdRoleMappingsClientsClientGet**
> List&lt;RoleRepresentation&gt; realmUsersIdRoleMappingsClientsClientGet(realm, id, client)

Get client-level role mappings for the user, and the app

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmUsersIdRoleMappingsClientsClientGet(realm, id, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmUsersIdRoleMappingsClientsClientGet");
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
| **id** | **String**| User id | |
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

<a id="realmUsersIdRoleMappingsClientsClientPost"></a>
# **realmUsersIdRoleMappingsClientsClientPost**
> realmUsersIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation)

Add client-level roles to the user role mapping

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientRoleMappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientRoleMappingsApi apiInstance = new ClientRoleMappingsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String client = "client_example"; // String | 
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmUsersIdRoleMappingsClientsClientPost(realm, id, client, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientRoleMappingsApi#realmUsersIdRoleMappingsClientsClientPost");
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
| **id** | **String**| User id | |
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

