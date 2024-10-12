# RolesApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientsIdRolesGet**](RolesApi.md#realmClientsIdRolesGet) | **GET** /{realm}/clients/{id}/roles | Get all roles for the realm or client |
| [**realmClientsIdRolesPost**](RolesApi.md#realmClientsIdRolesPost) | **POST** /{realm}/clients/{id}/roles | Create a new role for the realm or client |
| [**realmClientsIdRolesRoleNameCompositesClientsClientGet**](RolesApi.md#realmClientsIdRolesRoleNameCompositesClientsClientGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites/clients/{client} | An app-level roles for the specified app for the role’s composite |
| [**realmClientsIdRolesRoleNameCompositesDelete**](RolesApi.md#realmClientsIdRolesRoleNameCompositesDelete) | **DELETE** /{realm}/clients/{id}/roles/{role-name}/composites | Remove roles from the role’s composite |
| [**realmClientsIdRolesRoleNameCompositesGet**](RolesApi.md#realmClientsIdRolesRoleNameCompositesGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites | Get composites of the role |
| [**realmClientsIdRolesRoleNameCompositesPost**](RolesApi.md#realmClientsIdRolesRoleNameCompositesPost) | **POST** /{realm}/clients/{id}/roles/{role-name}/composites | Add a composite to the role |
| [**realmClientsIdRolesRoleNameCompositesRealmGet**](RolesApi.md#realmClientsIdRolesRoleNameCompositesRealmGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/composites/realm | Get realm-level roles of the role’s composite |
| [**realmClientsIdRolesRoleNameDelete**](RolesApi.md#realmClientsIdRolesRoleNameDelete) | **DELETE** /{realm}/clients/{id}/roles/{role-name} | Delete a role by name |
| [**realmClientsIdRolesRoleNameGet**](RolesApi.md#realmClientsIdRolesRoleNameGet) | **GET** /{realm}/clients/{id}/roles/{role-name} | Get a role by name |
| [**realmClientsIdRolesRoleNameGroupsGet**](RolesApi.md#realmClientsIdRolesRoleNameGroupsGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/groups | Return List of Groups that have the specified role name |
| [**realmClientsIdRolesRoleNameManagementPermissionsGet**](RolesApi.md#realmClientsIdRolesRoleNameManagementPermissionsGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference |
| [**realmClientsIdRolesRoleNameManagementPermissionsPut**](RolesApi.md#realmClientsIdRolesRoleNameManagementPermissionsPut) | **PUT** /{realm}/clients/{id}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference |
| [**realmClientsIdRolesRoleNamePut**](RolesApi.md#realmClientsIdRolesRoleNamePut) | **PUT** /{realm}/clients/{id}/roles/{role-name} | Update a role by name |
| [**realmClientsIdRolesRoleNameUsersGet**](RolesApi.md#realmClientsIdRolesRoleNameUsersGet) | **GET** /{realm}/clients/{id}/roles/{role-name}/users | Return List of Users that have the specified role name |
| [**realmRolesGet**](RolesApi.md#realmRolesGet) | **GET** /{realm}/roles | Get all roles for the realm or client |
| [**realmRolesPost**](RolesApi.md#realmRolesPost) | **POST** /{realm}/roles | Create a new role for the realm or client |
| [**realmRolesRoleNameCompositesClientsClientGet**](RolesApi.md#realmRolesRoleNameCompositesClientsClientGet) | **GET** /{realm}/roles/{role-name}/composites/clients/{client} | An app-level roles for the specified app for the role’s composite |
| [**realmRolesRoleNameCompositesDelete**](RolesApi.md#realmRolesRoleNameCompositesDelete) | **DELETE** /{realm}/roles/{role-name}/composites | Remove roles from the role’s composite |
| [**realmRolesRoleNameCompositesGet**](RolesApi.md#realmRolesRoleNameCompositesGet) | **GET** /{realm}/roles/{role-name}/composites | Get composites of the role |
| [**realmRolesRoleNameCompositesPost**](RolesApi.md#realmRolesRoleNameCompositesPost) | **POST** /{realm}/roles/{role-name}/composites | Add a composite to the role |
| [**realmRolesRoleNameCompositesRealmGet**](RolesApi.md#realmRolesRoleNameCompositesRealmGet) | **GET** /{realm}/roles/{role-name}/composites/realm | Get realm-level roles of the role’s composite |
| [**realmRolesRoleNameDelete**](RolesApi.md#realmRolesRoleNameDelete) | **DELETE** /{realm}/roles/{role-name} | Delete a role by name |
| [**realmRolesRoleNameGet**](RolesApi.md#realmRolesRoleNameGet) | **GET** /{realm}/roles/{role-name} | Get a role by name |
| [**realmRolesRoleNameGroupsGet**](RolesApi.md#realmRolesRoleNameGroupsGet) | **GET** /{realm}/roles/{role-name}/groups | Return List of Groups that have the specified role name |
| [**realmRolesRoleNameManagementPermissionsGet**](RolesApi.md#realmRolesRoleNameManagementPermissionsGet) | **GET** /{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference |
| [**realmRolesRoleNameManagementPermissionsPut**](RolesApi.md#realmRolesRoleNameManagementPermissionsPut) | **PUT** /{realm}/roles/{role-name}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference |
| [**realmRolesRoleNamePut**](RolesApi.md#realmRolesRoleNamePut) | **PUT** /{realm}/roles/{role-name} | Update a role by name |
| [**realmRolesRoleNameUsersGet**](RolesApi.md#realmRolesRoleNameUsersGet) | **GET** /{realm}/roles/{role-name}/users | Return List of Users that have the specified role name |


<a id="realmClientsIdRolesGet"></a>
# **realmClientsIdRolesGet**
> List&lt;RoleRepresentation&gt; realmClientsIdRolesGet(realm, id, briefRepresentation, first, max, search)

Get all roles for the realm or client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    Boolean briefRepresentation = true; // Boolean | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    String search = "search_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdRolesGet(realm, id, briefRepresentation, first, max, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesGet");
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
| **briefRepresentation** | **Boolean**|  | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |
| **search** | **String**|  | [optional] |

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

<a id="realmClientsIdRolesPost"></a>
# **realmClientsIdRolesPost**
> realmClientsIdRolesPost(realm, id, roleRepresentation)

Create a new role for the realm or client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    RoleRepresentation roleRepresentation = new RoleRepresentation(); // RoleRepresentation | 
    try {
      apiInstance.realmClientsIdRolesPost(realm, id, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesPost");
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
| **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | |

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

<a id="realmClientsIdRolesRoleNameCompositesClientsClientGet"></a>
# **realmClientsIdRolesRoleNameCompositesClientsClientGet**
> List&lt;RoleRepresentation&gt; realmClientsIdRolesRoleNameCompositesClientsClientGet(realm, id, roleName, client)

An app-level roles for the specified app for the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdRolesRoleNameCompositesClientsClientGet(realm, id, roleName, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameCompositesClientsClientGet");
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
| **roleName** | **String**| role’s name (not id!) | |
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

<a id="realmClientsIdRolesRoleNameCompositesDelete"></a>
# **realmClientsIdRolesRoleNameCompositesDelete**
> realmClientsIdRolesRoleNameCompositesDelete(realm, id, roleName, roleRepresentation)

Remove roles from the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | roles to remove
    try {
      apiInstance.realmClientsIdRolesRoleNameCompositesDelete(realm, id, roleName, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameCompositesDelete");
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
| **roleName** | **String**| role’s name (not id!) | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)| roles to remove | |

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

<a id="realmClientsIdRolesRoleNameCompositesGet"></a>
# **realmClientsIdRolesRoleNameCompositesGet**
> List&lt;RoleRepresentation&gt; realmClientsIdRolesRoleNameCompositesGet(realm, id, roleName)

Get composites of the role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdRolesRoleNameCompositesGet(realm, id, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameCompositesGet");
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
| **roleName** | **String**| role’s name (not id!) | |

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

<a id="realmClientsIdRolesRoleNameCompositesPost"></a>
# **realmClientsIdRolesRoleNameCompositesPost**
> realmClientsIdRolesRoleNameCompositesPost(realm, id, roleName, roleRepresentation)

Add a composite to the role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmClientsIdRolesRoleNameCompositesPost(realm, id, roleName, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameCompositesPost");
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
| **roleName** | **String**| role’s name (not id!) | |
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

<a id="realmClientsIdRolesRoleNameCompositesRealmGet"></a>
# **realmClientsIdRolesRoleNameCompositesRealmGet**
> List&lt;RoleRepresentation&gt; realmClientsIdRolesRoleNameCompositesRealmGet(realm, id, roleName)

Get realm-level roles of the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdRolesRoleNameCompositesRealmGet(realm, id, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameCompositesRealmGet");
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
| **roleName** | **String**| role’s name (not id!) | |

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

<a id="realmClientsIdRolesRoleNameDelete"></a>
# **realmClientsIdRolesRoleNameDelete**
> realmClientsIdRolesRoleNameDelete(realm, id, roleName)

Delete a role by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      apiInstance.realmClientsIdRolesRoleNameDelete(realm, id, roleName);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameDelete");
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
| **roleName** | **String**| role’s name (not id!) | |

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

<a id="realmClientsIdRolesRoleNameGet"></a>
# **realmClientsIdRolesRoleNameGet**
> RoleRepresentation realmClientsIdRolesRoleNameGet(realm, id, roleName)

Get a role by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      RoleRepresentation result = apiInstance.realmClientsIdRolesRoleNameGet(realm, id, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameGet");
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
| **roleName** | **String**| role’s name (not id!) | |

### Return type

[**RoleRepresentation**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdRolesRoleNameGroupsGet"></a>
# **realmClientsIdRolesRoleNameGroupsGet**
> List&lt;GroupRepresentation&gt; realmClientsIdRolesRoleNameGroupsGet(realm, id, roleName, briefRepresentation, first, max)

Return List of Groups that have the specified role name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | 
    Boolean briefRepresentation = true; // Boolean | if false, return a full representation of the GroupRepresentation objects
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    try {
      List<GroupRepresentation> result = apiInstance.realmClientsIdRolesRoleNameGroupsGet(realm, id, roleName, briefRepresentation, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameGroupsGet");
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
| **roleName** | **String**|  | |
| **briefRepresentation** | **Boolean**| if false, return a full representation of the GroupRepresentation objects | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |

### Return type

[**List&lt;GroupRepresentation&gt;**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdRolesRoleNameManagementPermissionsGet"></a>
# **realmClientsIdRolesRoleNameManagementPermissionsGet**
> ManagementPermissionReference realmClientsIdRolesRoleNameManagementPermissionsGet(realm, id, roleName)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | 
    try {
      ManagementPermissionReference result = apiInstance.realmClientsIdRolesRoleNameManagementPermissionsGet(realm, id, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameManagementPermissionsGet");
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
| **roleName** | **String**|  | |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdRolesRoleNameManagementPermissionsPut"></a>
# **realmClientsIdRolesRoleNameManagementPermissionsPut**
> ManagementPermissionReference realmClientsIdRolesRoleNameManagementPermissionsPut(realm, id, roleName, managementPermissionReference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | 
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmClientsIdRolesRoleNameManagementPermissionsPut(realm, id, roleName, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameManagementPermissionsPut");
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
| **roleName** | **String**|  | |
| **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdRolesRoleNamePut"></a>
# **realmClientsIdRolesRoleNamePut**
> realmClientsIdRolesRoleNamePut(realm, id, roleName, roleRepresentation)

Update a role by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    RoleRepresentation roleRepresentation = new RoleRepresentation(); // RoleRepresentation | 
    try {
      apiInstance.realmClientsIdRolesRoleNamePut(realm, id, roleName, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNamePut");
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
| **roleName** | **String**| role’s name (not id!) | |
| **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | |

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

<a id="realmClientsIdRolesRoleNameUsersGet"></a>
# **realmClientsIdRolesRoleNameUsersGet**
> List&lt;UserRepresentation&gt; realmClientsIdRolesRoleNameUsersGet(realm, id, roleName, first, max)

Return List of Users that have the specified role name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleName = "roleName_example"; // String | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    try {
      List<UserRepresentation> result = apiInstance.realmClientsIdRolesRoleNameUsersGet(realm, id, roleName, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmClientsIdRolesRoleNameUsersGet");
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
| **roleName** | **String**|  | |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |

### Return type

[**List&lt;UserRepresentation&gt;**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmRolesGet"></a>
# **realmRolesGet**
> List&lt;RoleRepresentation&gt; realmRolesGet(realm, briefRepresentation, first, max, search)

Get all roles for the realm or client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    Boolean briefRepresentation = true; // Boolean | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    String search = "search_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesGet(realm, briefRepresentation, first, max, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesGet");
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
| **briefRepresentation** | **Boolean**|  | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |
| **search** | **String**|  | [optional] |

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

<a id="realmRolesPost"></a>
# **realmRolesPost**
> realmRolesPost(realm, roleRepresentation)

Create a new role for the realm or client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    RoleRepresentation roleRepresentation = new RoleRepresentation(); // RoleRepresentation | 
    try {
      apiInstance.realmRolesPost(realm, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesPost");
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
| **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | |

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

<a id="realmRolesRoleNameCompositesClientsClientGet"></a>
# **realmRolesRoleNameCompositesClientsClientGet**
> List&lt;RoleRepresentation&gt; realmRolesRoleNameCompositesClientsClientGet(realm, roleName, client)

An app-level roles for the specified app for the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesRoleNameCompositesClientsClientGet(realm, roleName, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameCompositesClientsClientGet");
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
| **roleName** | **String**| role’s name (not id!) | |
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

<a id="realmRolesRoleNameCompositesDelete"></a>
# **realmRolesRoleNameCompositesDelete**
> realmRolesRoleNameCompositesDelete(realm, roleName, roleRepresentation)

Remove roles from the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | roles to remove
    try {
      apiInstance.realmRolesRoleNameCompositesDelete(realm, roleName, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameCompositesDelete");
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
| **roleName** | **String**| role’s name (not id!) | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)| roles to remove | |

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

<a id="realmRolesRoleNameCompositesGet"></a>
# **realmRolesRoleNameCompositesGet**
> List&lt;RoleRepresentation&gt; realmRolesRoleNameCompositesGet(realm, roleName)

Get composites of the role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesRoleNameCompositesGet(realm, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameCompositesGet");
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
| **roleName** | **String**| role’s name (not id!) | |

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

<a id="realmRolesRoleNameCompositesPost"></a>
# **realmRolesRoleNameCompositesPost**
> realmRolesRoleNameCompositesPost(realm, roleName, roleRepresentation)

Add a composite to the role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmRolesRoleNameCompositesPost(realm, roleName, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameCompositesPost");
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
| **roleName** | **String**| role’s name (not id!) | |
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

<a id="realmRolesRoleNameCompositesRealmGet"></a>
# **realmRolesRoleNameCompositesRealmGet**
> List&lt;RoleRepresentation&gt; realmRolesRoleNameCompositesRealmGet(realm, roleName)

Get realm-level roles of the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesRoleNameCompositesRealmGet(realm, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameCompositesRealmGet");
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
| **roleName** | **String**| role’s name (not id!) | |

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

<a id="realmRolesRoleNameDelete"></a>
# **realmRolesRoleNameDelete**
> realmRolesRoleNameDelete(realm, roleName)

Delete a role by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      apiInstance.realmRolesRoleNameDelete(realm, roleName);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameDelete");
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
| **roleName** | **String**| role’s name (not id!) | |

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

<a id="realmRolesRoleNameGet"></a>
# **realmRolesRoleNameGet**
> RoleRepresentation realmRolesRoleNameGet(realm, roleName)

Get a role by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    try {
      RoleRepresentation result = apiInstance.realmRolesRoleNameGet(realm, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameGet");
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
| **roleName** | **String**| role’s name (not id!) | |

### Return type

[**RoleRepresentation**](RoleRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmRolesRoleNameGroupsGet"></a>
# **realmRolesRoleNameGroupsGet**
> List&lt;GroupRepresentation&gt; realmRolesRoleNameGroupsGet(realm, roleName, briefRepresentation, first, max)

Return List of Groups that have the specified role name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | 
    Boolean briefRepresentation = true; // Boolean | if false, return a full representation of the GroupRepresentation objects
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    try {
      List<GroupRepresentation> result = apiInstance.realmRolesRoleNameGroupsGet(realm, roleName, briefRepresentation, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameGroupsGet");
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
| **roleName** | **String**|  | |
| **briefRepresentation** | **Boolean**| if false, return a full representation of the GroupRepresentation objects | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |

### Return type

[**List&lt;GroupRepresentation&gt;**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmRolesRoleNameManagementPermissionsGet"></a>
# **realmRolesRoleNameManagementPermissionsGet**
> ManagementPermissionReference realmRolesRoleNameManagementPermissionsGet(realm, roleName)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | 
    try {
      ManagementPermissionReference result = apiInstance.realmRolesRoleNameManagementPermissionsGet(realm, roleName);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameManagementPermissionsGet");
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
| **roleName** | **String**|  | |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmRolesRoleNameManagementPermissionsPut"></a>
# **realmRolesRoleNameManagementPermissionsPut**
> ManagementPermissionReference realmRolesRoleNameManagementPermissionsPut(realm, roleName, managementPermissionReference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | 
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmRolesRoleNameManagementPermissionsPut(realm, roleName, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameManagementPermissionsPut");
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
| **roleName** | **String**|  | |
| **managementPermissionReference** | [**ManagementPermissionReference**](ManagementPermissionReference.md)|  | |

### Return type

[**ManagementPermissionReference**](ManagementPermissionReference.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmRolesRoleNamePut"></a>
# **realmRolesRoleNamePut**
> realmRolesRoleNamePut(realm, roleName, roleRepresentation)

Update a role by name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | role’s name (not id!)
    RoleRepresentation roleRepresentation = new RoleRepresentation(); // RoleRepresentation | 
    try {
      apiInstance.realmRolesRoleNamePut(realm, roleName, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNamePut");
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
| **roleName** | **String**| role’s name (not id!) | |
| **roleRepresentation** | [**RoleRepresentation**](RoleRepresentation.md)|  | |

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

<a id="realmRolesRoleNameUsersGet"></a>
# **realmRolesRoleNameUsersGet**
> List&lt;UserRepresentation&gt; realmRolesRoleNameUsersGet(realm, roleName, first, max)

Return List of Users that have the specified role name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesApi apiInstance = new RolesApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleName = "roleName_example"; // String | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    try {
      List<UserRepresentation> result = apiInstance.realmRolesRoleNameUsersGet(realm, roleName, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesApi#realmRolesRoleNameUsersGet");
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
| **roleName** | **String**|  | |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |

### Return type

[**List&lt;UserRepresentation&gt;**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

