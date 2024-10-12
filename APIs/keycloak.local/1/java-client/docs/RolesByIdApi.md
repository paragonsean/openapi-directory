# RolesByIdApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmRolesByIdRoleIdCompositesClientsClientGet**](RolesByIdApi.md#realmRolesByIdRoleIdCompositesClientsClientGet) | **GET** /{realm}/roles-by-id/{role-id}/composites/clients/{client} | Get client-level roles for the client that are in the role’s composite |
| [**realmRolesByIdRoleIdCompositesDelete**](RolesByIdApi.md#realmRolesByIdRoleIdCompositesDelete) | **DELETE** /{realm}/roles-by-id/{role-id}/composites | Remove a set of roles from the role’s composite |
| [**realmRolesByIdRoleIdCompositesGet**](RolesByIdApi.md#realmRolesByIdRoleIdCompositesGet) | **GET** /{realm}/roles-by-id/{role-id}/composites | Get role’s children   Returns a set of role’s children provided the role is a composite. |
| [**realmRolesByIdRoleIdCompositesPost**](RolesByIdApi.md#realmRolesByIdRoleIdCompositesPost) | **POST** /{realm}/roles-by-id/{role-id}/composites | Make the role a composite role by associating some child roles |
| [**realmRolesByIdRoleIdCompositesRealmGet**](RolesByIdApi.md#realmRolesByIdRoleIdCompositesRealmGet) | **GET** /{realm}/roles-by-id/{role-id}/composites/realm | Get realm-level roles that are in the role’s composite |
| [**realmRolesByIdRoleIdDelete**](RolesByIdApi.md#realmRolesByIdRoleIdDelete) | **DELETE** /{realm}/roles-by-id/{role-id} | Delete the role |
| [**realmRolesByIdRoleIdGet**](RolesByIdApi.md#realmRolesByIdRoleIdGet) | **GET** /{realm}/roles-by-id/{role-id} | Get a specific role’s representation |
| [**realmRolesByIdRoleIdManagementPermissionsGet**](RolesByIdApi.md#realmRolesByIdRoleIdManagementPermissionsGet) | **GET** /{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference |
| [**realmRolesByIdRoleIdManagementPermissionsPut**](RolesByIdApi.md#realmRolesByIdRoleIdManagementPermissionsPut) | **PUT** /{realm}/roles-by-id/{role-id}/management/permissions | Return object stating whether role Authoirzation permissions have been initialized or not and a reference |
| [**realmRolesByIdRoleIdPut**](RolesByIdApi.md#realmRolesByIdRoleIdPut) | **PUT** /{realm}/roles-by-id/{role-id} | Update the role |


<a id="realmRolesByIdRoleIdCompositesClientsClientGet"></a>
# **realmRolesByIdRoleIdCompositesClientsClientGet**
> List&lt;RoleRepresentation&gt; realmRolesByIdRoleIdCompositesClientsClientGet(realm, roleId, client)

Get client-level roles for the client that are in the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | 
    String client = "client_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesByIdRoleIdCompositesClientsClientGet(realm, roleId, client);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdCompositesClientsClientGet");
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
| **roleId** | **String**|  | |
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

<a id="realmRolesByIdRoleIdCompositesDelete"></a>
# **realmRolesByIdRoleIdCompositesDelete**
> realmRolesByIdRoleIdCompositesDelete(realm, roleId, roleRepresentation)

Remove a set of roles from the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | Role id
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | A set of roles to be removed
    try {
      apiInstance.realmRolesByIdRoleIdCompositesDelete(realm, roleId, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdCompositesDelete");
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
| **roleId** | **String**| Role id | |
| **roleRepresentation** | [**List&lt;RoleRepresentation&gt;**](RoleRepresentation.md)| A set of roles to be removed | |

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

<a id="realmRolesByIdRoleIdCompositesGet"></a>
# **realmRolesByIdRoleIdCompositesGet**
> List&lt;RoleRepresentation&gt; realmRolesByIdRoleIdCompositesGet(realm, roleId)

Get role’s children   Returns a set of role’s children provided the role is a composite.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | Role id
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesByIdRoleIdCompositesGet(realm, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdCompositesGet");
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
| **roleId** | **String**| Role id | |

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

<a id="realmRolesByIdRoleIdCompositesPost"></a>
# **realmRolesByIdRoleIdCompositesPost**
> realmRolesByIdRoleIdCompositesPost(realm, roleId, roleRepresentation)

Make the role a composite role by associating some child roles

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | Role id
    List<RoleRepresentation> roleRepresentation = Arrays.asList(); // List<RoleRepresentation> | 
    try {
      apiInstance.realmRolesByIdRoleIdCompositesPost(realm, roleId, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdCompositesPost");
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
| **roleId** | **String**| Role id | |
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

<a id="realmRolesByIdRoleIdCompositesRealmGet"></a>
# **realmRolesByIdRoleIdCompositesRealmGet**
> List&lt;RoleRepresentation&gt; realmRolesByIdRoleIdCompositesRealmGet(realm, roleId)

Get realm-level roles that are in the role’s composite

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmRolesByIdRoleIdCompositesRealmGet(realm, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdCompositesRealmGet");
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
| **roleId** | **String**|  | |

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

<a id="realmRolesByIdRoleIdDelete"></a>
# **realmRolesByIdRoleIdDelete**
> realmRolesByIdRoleIdDelete(realm, roleId)

Delete the role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | id of role
    try {
      apiInstance.realmRolesByIdRoleIdDelete(realm, roleId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdDelete");
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
| **roleId** | **String**| id of role | |

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

<a id="realmRolesByIdRoleIdGet"></a>
# **realmRolesByIdRoleIdGet**
> RoleRepresentation realmRolesByIdRoleIdGet(realm, roleId)

Get a specific role’s representation

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | id of role
    try {
      RoleRepresentation result = apiInstance.realmRolesByIdRoleIdGet(realm, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdGet");
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
| **roleId** | **String**| id of role | |

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

<a id="realmRolesByIdRoleIdManagementPermissionsGet"></a>
# **realmRolesByIdRoleIdManagementPermissionsGet**
> ManagementPermissionReference realmRolesByIdRoleIdManagementPermissionsGet(realm, roleId)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | 
    try {
      ManagementPermissionReference result = apiInstance.realmRolesByIdRoleIdManagementPermissionsGet(realm, roleId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdManagementPermissionsGet");
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
| **roleId** | **String**|  | |

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

<a id="realmRolesByIdRoleIdManagementPermissionsPut"></a>
# **realmRolesByIdRoleIdManagementPermissionsPut**
> ManagementPermissionReference realmRolesByIdRoleIdManagementPermissionsPut(realm, roleId, managementPermissionReference)

Return object stating whether role Authoirzation permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | 
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmRolesByIdRoleIdManagementPermissionsPut(realm, roleId, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdManagementPermissionsPut");
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
| **roleId** | **String**|  | |
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

<a id="realmRolesByIdRoleIdPut"></a>
# **realmRolesByIdRoleIdPut**
> realmRolesByIdRoleIdPut(realm, roleId, roleRepresentation)

Update the role

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RolesByIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RolesByIdApi apiInstance = new RolesByIdApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String roleId = "roleId_example"; // String | id of role
    RoleRepresentation roleRepresentation = new RoleRepresentation(); // RoleRepresentation | 
    try {
      apiInstance.realmRolesByIdRoleIdPut(realm, roleId, roleRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RolesByIdApi#realmRolesByIdRoleIdPut");
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
| **roleId** | **String**| id of role | |
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

