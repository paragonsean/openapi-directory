# RealmsAdminApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmAdminEventsDelete**](RealmsAdminApi.md#realmAdminEventsDelete) | **DELETE** /{realm}/admin-events | Delete all admin events |
| [**realmAdminEventsGet**](RealmsAdminApi.md#realmAdminEventsGet) | **GET** /{realm}/admin-events | Get admin events   Returns all admin events, or filters events based on URL query parameters listed here |
| [**realmClearKeysCachePost**](RealmsAdminApi.md#realmClearKeysCachePost) | **POST** /{realm}/clear-keys-cache | Clear cache of external public keys (Public keys of clients or Identity providers) |
| [**realmClearRealmCachePost**](RealmsAdminApi.md#realmClearRealmCachePost) | **POST** /{realm}/clear-realm-cache | Clear realm cache |
| [**realmClearUserCachePost**](RealmsAdminApi.md#realmClearUserCachePost) | **POST** /{realm}/clear-user-cache | Clear user cache |
| [**realmClientDescriptionConverterPost**](RealmsAdminApi.md#realmClientDescriptionConverterPost) | **POST** /{realm}/client-description-converter | Base path for importing clients under this realm. |
| [**realmClientSessionStatsGet**](RealmsAdminApi.md#realmClientSessionStatsGet) | **GET** /{realm}/client-session-stats | Get client session stats   Returns a JSON map. |
| [**realmCredentialRegistratorsGet**](RealmsAdminApi.md#realmCredentialRegistratorsGet) | **GET** /{realm}/credential-registrators |  |
| [**realmDefaultDefaultClientScopesClientScopeIdDelete**](RealmsAdminApi.md#realmDefaultDefaultClientScopesClientScopeIdDelete) | **DELETE** /{realm}/default-default-client-scopes/{clientScopeId} |  |
| [**realmDefaultDefaultClientScopesClientScopeIdPut**](RealmsAdminApi.md#realmDefaultDefaultClientScopesClientScopeIdPut) | **PUT** /{realm}/default-default-client-scopes/{clientScopeId} |  |
| [**realmDefaultDefaultClientScopesGet**](RealmsAdminApi.md#realmDefaultDefaultClientScopesGet) | **GET** /{realm}/default-default-client-scopes | Get realm default client scopes. |
| [**realmDefaultGroupsGet**](RealmsAdminApi.md#realmDefaultGroupsGet) | **GET** /{realm}/default-groups | Get group hierarchy. |
| [**realmDefaultGroupsGroupIdDelete**](RealmsAdminApi.md#realmDefaultGroupsGroupIdDelete) | **DELETE** /{realm}/default-groups/{groupId} |  |
| [**realmDefaultGroupsGroupIdPut**](RealmsAdminApi.md#realmDefaultGroupsGroupIdPut) | **PUT** /{realm}/default-groups/{groupId} |  |
| [**realmDefaultOptionalClientScopesClientScopeIdDelete**](RealmsAdminApi.md#realmDefaultOptionalClientScopesClientScopeIdDelete) | **DELETE** /{realm}/default-optional-client-scopes/{clientScopeId} |  |
| [**realmDefaultOptionalClientScopesClientScopeIdPut**](RealmsAdminApi.md#realmDefaultOptionalClientScopesClientScopeIdPut) | **PUT** /{realm}/default-optional-client-scopes/{clientScopeId} |  |
| [**realmDefaultOptionalClientScopesGet**](RealmsAdminApi.md#realmDefaultOptionalClientScopesGet) | **GET** /{realm}/default-optional-client-scopes | Get realm optional client scopes. |
| [**realmDelete**](RealmsAdminApi.md#realmDelete) | **DELETE** /{realm} | Delete the realm |
| [**realmEventsConfigGet**](RealmsAdminApi.md#realmEventsConfigGet) | **GET** /{realm}/events/config | Get the events provider configuration   Returns JSON object with events provider configuration |
| [**realmEventsConfigPut**](RealmsAdminApi.md#realmEventsConfigPut) | **PUT** /{realm}/events/config | Update the events provider   Change the events provider and/or its configuration |
| [**realmEventsDelete**](RealmsAdminApi.md#realmEventsDelete) | **DELETE** /{realm}/events | Delete all events |
| [**realmEventsGet**](RealmsAdminApi.md#realmEventsGet) | **GET** /{realm}/events | Get events   Returns all events, or filters them based on URL query parameters listed here |
| [**realmGet**](RealmsAdminApi.md#realmGet) | **GET** /{realm} | Get the top-level representation of the realm   It will not include nested information like User and Client representations. |
| [**realmGroupByPathPathGet**](RealmsAdminApi.md#realmGroupByPathPathGet) | **GET** /{realm}/group-by-path/{path} |  |
| [**realmLogoutAllPost**](RealmsAdminApi.md#realmLogoutAllPost) | **POST** /{realm}/logout-all | Removes all user sessions. |
| [**realmPartialExportPost**](RealmsAdminApi.md#realmPartialExportPost) | **POST** /{realm}/partial-export | Partial export of existing realm into a JSON file. |
| [**realmPartialImportPost**](RealmsAdminApi.md#realmPartialImportPost) | **POST** /{realm}/partialImport | Partial import from a JSON file to an existing realm. |
| [**realmPushRevocationPost**](RealmsAdminApi.md#realmPushRevocationPost) | **POST** /{realm}/push-revocation | Push the realm’s revocation policy to any client that has an admin url associated with it. |
| [**realmPut**](RealmsAdminApi.md#realmPut) | **PUT** /{realm} | Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored. |
| [**realmSessionsSessionDelete**](RealmsAdminApi.md#realmSessionsSessionDelete) | **DELETE** /{realm}/sessions/{session} | Remove a specific user session. |
| [**realmTestLDAPConnectionPost**](RealmsAdminApi.md#realmTestLDAPConnectionPost) | **POST** /{realm}/testLDAPConnection | Test LDAP connection |
| [**realmTestSMTPConnectionPost**](RealmsAdminApi.md#realmTestSMTPConnectionPost) | **POST** /{realm}/testSMTPConnection |  |
| [**realmUsersManagementPermissionsGet**](RealmsAdminApi.md#realmUsersManagementPermissionsGet) | **GET** /{realm}/users-management-permissions |  |
| [**realmUsersManagementPermissionsPut**](RealmsAdminApi.md#realmUsersManagementPermissionsPut) | **PUT** /{realm}/users-management-permissions |  |
| [**rootPost**](RealmsAdminApi.md#rootPost) | **POST** / | Import a realm   Imports a realm from a full representation of that realm. |


<a id="realmAdminEventsDelete"></a>
# **realmAdminEventsDelete**
> realmAdminEventsDelete(realm)

Delete all admin events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmAdminEventsDelete(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmAdminEventsDelete");
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

<a id="realmAdminEventsGet"></a>
# **realmAdminEventsGet**
> List&lt;AdminEventRepresentation&gt; realmAdminEventsGet(realm, authClient, authIpAddress, authRealm, authUser, dateFrom, dateTo, first, max, operationTypes, resourcePath, resourceTypes)

Get admin events   Returns all admin events, or filters events based on URL query parameters listed here

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String authClient = "authClient_example"; // String | 
    String authIpAddress = "authIpAddress_example"; // String | 
    String authRealm = "authRealm_example"; // String | 
    String authUser = "authUser_example"; // String | user id
    String dateFrom = "dateFrom_example"; // String | 
    String dateTo = "dateTo_example"; // String | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | Maximum results size (defaults to 100)
    List<String> operationTypes = Arrays.asList(); // List<String> | 
    String resourcePath = "resourcePath_example"; // String | 
    List<String> resourceTypes = Arrays.asList(); // List<String> | 
    try {
      List<AdminEventRepresentation> result = apiInstance.realmAdminEventsGet(realm, authClient, authIpAddress, authRealm, authUser, dateFrom, dateTo, first, max, operationTypes, resourcePath, resourceTypes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmAdminEventsGet");
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
| **authClient** | **String**|  | [optional] |
| **authIpAddress** | **String**|  | [optional] |
| **authRealm** | **String**|  | [optional] |
| **authUser** | **String**| user id | [optional] |
| **dateFrom** | **String**|  | [optional] |
| **dateTo** | **String**|  | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**| Maximum results size (defaults to 100) | [optional] |
| **operationTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **resourcePath** | **String**|  | [optional] |
| **resourceTypes** | [**List&lt;String&gt;**](String.md)|  | [optional] |

### Return type

[**List&lt;AdminEventRepresentation&gt;**](AdminEventRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClearKeysCachePost"></a>
# **realmClearKeysCachePost**
> realmClearKeysCachePost(realm)

Clear cache of external public keys (Public keys of clients or Identity providers)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmClearKeysCachePost(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmClearKeysCachePost");
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

<a id="realmClearRealmCachePost"></a>
# **realmClearRealmCachePost**
> realmClearRealmCachePost(realm)

Clear realm cache

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmClearRealmCachePost(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmClearRealmCachePost");
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

<a id="realmClearUserCachePost"></a>
# **realmClearUserCachePost**
> realmClearUserCachePost(realm)

Clear user cache

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmClearUserCachePost(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmClearUserCachePost");
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

<a id="realmClientDescriptionConverterPost"></a>
# **realmClientDescriptionConverterPost**
> ClientRepresentation realmClientDescriptionConverterPost(realm, body)

Base path for importing clients under this realm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String body = "body_example"; // String | 
    try {
      ClientRepresentation result = apiInstance.realmClientDescriptionConverterPost(realm, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmClientDescriptionConverterPost");
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
| **body** | **String**|  | |

### Return type

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientSessionStatsGet"></a>
# **realmClientSessionStatsGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmClientSessionStatsGet(realm)

Get client session stats   Returns a JSON map.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<Map<String, Object>> result = apiInstance.realmClientSessionStatsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmClientSessionStatsGet");
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

[**List&lt;Map&lt;String, Object&gt;&gt;**](Map.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmCredentialRegistratorsGet"></a>
# **realmCredentialRegistratorsGet**
> List&lt;String&gt; realmCredentialRegistratorsGet(realm)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<String> result = apiInstance.realmCredentialRegistratorsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmCredentialRegistratorsGet");
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

**List&lt;String&gt;**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmDefaultDefaultClientScopesClientScopeIdDelete"></a>
# **realmDefaultDefaultClientScopesClientScopeIdDelete**
> realmDefaultDefaultClientScopesClientScopeIdDelete(realm, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmDefaultDefaultClientScopesClientScopeIdDelete(realm, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultDefaultClientScopesClientScopeIdDelete");
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
| **clientScopeId** | **String**|  | |

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

<a id="realmDefaultDefaultClientScopesClientScopeIdPut"></a>
# **realmDefaultDefaultClientScopesClientScopeIdPut**
> realmDefaultDefaultClientScopesClientScopeIdPut(realm, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmDefaultDefaultClientScopesClientScopeIdPut(realm, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultDefaultClientScopesClientScopeIdPut");
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
| **clientScopeId** | **String**|  | |

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

<a id="realmDefaultDefaultClientScopesGet"></a>
# **realmDefaultDefaultClientScopesGet**
> List&lt;ClientScopeRepresentation&gt; realmDefaultDefaultClientScopesGet(realm)

Get realm default client scopes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<ClientScopeRepresentation> result = apiInstance.realmDefaultDefaultClientScopesGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultDefaultClientScopesGet");
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

<a id="realmDefaultGroupsGet"></a>
# **realmDefaultGroupsGet**
> List&lt;GroupRepresentation&gt; realmDefaultGroupsGet(realm)

Get group hierarchy.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<GroupRepresentation> result = apiInstance.realmDefaultGroupsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultGroupsGet");
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

<a id="realmDefaultGroupsGroupIdDelete"></a>
# **realmDefaultGroupsGroupIdDelete**
> realmDefaultGroupsGroupIdDelete(realm, groupId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.realmDefaultGroupsGroupIdDelete(realm, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultGroupsGroupIdDelete");
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
| **groupId** | **String**|  | |

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

<a id="realmDefaultGroupsGroupIdPut"></a>
# **realmDefaultGroupsGroupIdPut**
> realmDefaultGroupsGroupIdPut(realm, groupId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.realmDefaultGroupsGroupIdPut(realm, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultGroupsGroupIdPut");
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
| **groupId** | **String**|  | |

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

<a id="realmDefaultOptionalClientScopesClientScopeIdDelete"></a>
# **realmDefaultOptionalClientScopesClientScopeIdDelete**
> realmDefaultOptionalClientScopesClientScopeIdDelete(realm, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmDefaultOptionalClientScopesClientScopeIdDelete(realm, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultOptionalClientScopesClientScopeIdDelete");
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
| **clientScopeId** | **String**|  | |

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

<a id="realmDefaultOptionalClientScopesClientScopeIdPut"></a>
# **realmDefaultOptionalClientScopesClientScopeIdPut**
> realmDefaultOptionalClientScopesClientScopeIdPut(realm, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmDefaultOptionalClientScopesClientScopeIdPut(realm, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultOptionalClientScopesClientScopeIdPut");
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
| **clientScopeId** | **String**|  | |

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

<a id="realmDefaultOptionalClientScopesGet"></a>
# **realmDefaultOptionalClientScopesGet**
> List&lt;ClientScopeRepresentation&gt; realmDefaultOptionalClientScopesGet(realm)

Get realm optional client scopes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<ClientScopeRepresentation> result = apiInstance.realmDefaultOptionalClientScopesGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDefaultOptionalClientScopesGet");
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

<a id="realmDelete"></a>
# **realmDelete**
> realmDelete(realm)

Delete the realm

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmDelete(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmDelete");
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

<a id="realmEventsConfigGet"></a>
# **realmEventsConfigGet**
> RealmEventsConfigRepresentation realmEventsConfigGet(realm)

Get the events provider configuration   Returns JSON object with events provider configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      RealmEventsConfigRepresentation result = apiInstance.realmEventsConfigGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmEventsConfigGet");
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

[**RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmEventsConfigPut"></a>
# **realmEventsConfigPut**
> realmEventsConfigPut(realm, realmEventsConfigRepresentation)

Update the events provider   Change the events provider and/or its configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    RealmEventsConfigRepresentation realmEventsConfigRepresentation = new RealmEventsConfigRepresentation(); // RealmEventsConfigRepresentation | 
    try {
      apiInstance.realmEventsConfigPut(realm, realmEventsConfigRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmEventsConfigPut");
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
| **realmEventsConfigRepresentation** | [**RealmEventsConfigRepresentation**](RealmEventsConfigRepresentation.md)|  | |

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

<a id="realmEventsDelete"></a>
# **realmEventsDelete**
> realmEventsDelete(realm)

Delete all events

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmEventsDelete(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmEventsDelete");
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

<a id="realmEventsGet"></a>
# **realmEventsGet**
> List&lt;EventRepresentation&gt; realmEventsGet(realm, client, dateFrom, dateTo, first, ipAddress, max, type, user)

Get events   Returns all events, or filters them based on URL query parameters listed here

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String client = "client_example"; // String | App or oauth client name
    String dateFrom = "dateFrom_example"; // String | From date
    String dateTo = "dateTo_example"; // String | To date
    Integer first = 56; // Integer | Paging offset
    String ipAddress = "ipAddress_example"; // String | IP address
    Integer max = 56; // Integer | Maximum results size (defaults to 100)
    List<String> type = Arrays.asList(); // List<String> | The types of events to return
    String user = "user_example"; // String | User id
    try {
      List<EventRepresentation> result = apiInstance.realmEventsGet(realm, client, dateFrom, dateTo, first, ipAddress, max, type, user);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmEventsGet");
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
| **client** | **String**| App or oauth client name | [optional] |
| **dateFrom** | **String**| From date | [optional] |
| **dateTo** | **String**| To date | [optional] |
| **first** | **Integer**| Paging offset | [optional] |
| **ipAddress** | **String**| IP address | [optional] |
| **max** | **Integer**| Maximum results size (defaults to 100) | [optional] |
| **type** | [**List&lt;String&gt;**](String.md)| The types of events to return | [optional] |
| **user** | **String**| User id | [optional] |

### Return type

[**List&lt;EventRepresentation&gt;**](EventRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGet"></a>
# **realmGet**
> RealmRepresentation realmGet(realm)

Get the top-level representation of the realm   It will not include nested information like User and Client representations.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      RealmRepresentation result = apiInstance.realmGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmGet");
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

[**RealmRepresentation**](RealmRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmGroupByPathPathGet"></a>
# **realmGroupByPathPathGet**
> GroupRepresentation realmGroupByPathPathGet(realm, path)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String path = "path_example"; // String | 
    try {
      GroupRepresentation result = apiInstance.realmGroupByPathPathGet(realm, path);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmGroupByPathPathGet");
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
| **path** | **String**|  | |

### Return type

[**GroupRepresentation**](GroupRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmLogoutAllPost"></a>
# **realmLogoutAllPost**
> realmLogoutAllPost(realm)

Removes all user sessions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmLogoutAllPost(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmLogoutAllPost");
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

<a id="realmPartialExportPost"></a>
# **realmPartialExportPost**
> RealmRepresentation realmPartialExportPost(realm, exportClients, exportGroupsAndRoles)

Partial export of existing realm into a JSON file.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    Boolean exportClients = true; // Boolean | 
    Boolean exportGroupsAndRoles = true; // Boolean | 
    try {
      RealmRepresentation result = apiInstance.realmPartialExportPost(realm, exportClients, exportGroupsAndRoles);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmPartialExportPost");
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
| **exportClients** | **Boolean**|  | [optional] |
| **exportGroupsAndRoles** | **Boolean**|  | [optional] |

### Return type

[**RealmRepresentation**](RealmRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmPartialImportPost"></a>
# **realmPartialImportPost**
> realmPartialImportPost(realm, partialImportRepresentation)

Partial import from a JSON file to an existing realm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    PartialImportRepresentation partialImportRepresentation = new PartialImportRepresentation(); // PartialImportRepresentation | 
    try {
      apiInstance.realmPartialImportPost(realm, partialImportRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmPartialImportPost");
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
| **partialImportRepresentation** | [**PartialImportRepresentation**](PartialImportRepresentation.md)|  | |

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

<a id="realmPushRevocationPost"></a>
# **realmPushRevocationPost**
> realmPushRevocationPost(realm)

Push the realm’s revocation policy to any client that has an admin url associated with it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      apiInstance.realmPushRevocationPost(realm);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmPushRevocationPost");
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

<a id="realmPut"></a>
# **realmPut**
> realmPut(realm, realmRepresentation)

Update the top-level information of the realm   Any user, roles or client information in the representation  will be ignored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    RealmRepresentation realmRepresentation = new RealmRepresentation(); // RealmRepresentation | 
    try {
      apiInstance.realmPut(realm, realmRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmPut");
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
| **realmRepresentation** | [**RealmRepresentation**](RealmRepresentation.md)|  | |

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

<a id="realmSessionsSessionDelete"></a>
# **realmSessionsSessionDelete**
> realmSessionsSessionDelete(realm, session)

Remove a specific user session.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String session = "session_example"; // String | 
    try {
      apiInstance.realmSessionsSessionDelete(realm, session);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmSessionsSessionDelete");
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
| **session** | **String**|  | |

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

<a id="realmTestLDAPConnectionPost"></a>
# **realmTestLDAPConnectionPost**
> realmTestLDAPConnectionPost(realm, testLdapConnectionRepresentation)

Test LDAP connection

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    TestLdapConnectionRepresentation testLdapConnectionRepresentation = new TestLdapConnectionRepresentation(); // TestLdapConnectionRepresentation | 
    try {
      apiInstance.realmTestLDAPConnectionPost(realm, testLdapConnectionRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmTestLDAPConnectionPost");
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
| **testLdapConnectionRepresentation** | [**TestLdapConnectionRepresentation**](TestLdapConnectionRepresentation.md)|  | |

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

<a id="realmTestSMTPConnectionPost"></a>
# **realmTestSMTPConnectionPost**
> realmTestSMTPConnectionPost(realm, requestBody)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      apiInstance.realmTestSMTPConnectionPost(realm, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmTestSMTPConnectionPost");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)|  | |

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

<a id="realmUsersManagementPermissionsGet"></a>
# **realmUsersManagementPermissionsGet**
> ManagementPermissionReference realmUsersManagementPermissionsGet(realm)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      ManagementPermissionReference result = apiInstance.realmUsersManagementPermissionsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmUsersManagementPermissionsGet");
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

<a id="realmUsersManagementPermissionsPut"></a>
# **realmUsersManagementPermissionsPut**
> ManagementPermissionReference realmUsersManagementPermissionsPut(realm, managementPermissionReference)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmUsersManagementPermissionsPut(realm, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#realmUsersManagementPermissionsPut");
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

<a id="rootPost"></a>
# **rootPost**
> rootPost(realmRepresentation)

Import a realm   Imports a realm from a full representation of that realm.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RealmsAdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    RealmsAdminApi apiInstance = new RealmsAdminApi(defaultClient);
    RealmRepresentation realmRepresentation = new RealmRepresentation(); // RealmRepresentation | JSON representation of the realm
    try {
      apiInstance.rootPost(realmRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling RealmsAdminApi#rootPost");
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
| **realmRepresentation** | [**RealmRepresentation**](RealmRepresentation.md)| JSON representation of the realm | |

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

