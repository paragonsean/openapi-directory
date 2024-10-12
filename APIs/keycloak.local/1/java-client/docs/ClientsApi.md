# ClientsApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmClientsGet**](ClientsApi.md#realmClientsGet) | **GET** /{realm}/clients | Get clients belonging to the realm   Returns a list of clients belonging to the realm |
| [**realmClientsIdClientSecretGet**](ClientsApi.md#realmClientsIdClientSecretGet) | **GET** /{realm}/clients/{id}/client-secret | Get the client secret |
| [**realmClientsIdClientSecretPost**](ClientsApi.md#realmClientsIdClientSecretPost) | **POST** /{realm}/clients/{id}/client-secret | Generate a new secret for the client |
| [**realmClientsIdDefaultClientScopesClientScopeIdDelete**](ClientsApi.md#realmClientsIdDefaultClientScopesClientScopeIdDelete) | **DELETE** /{realm}/clients/{id}/default-client-scopes/{clientScopeId} |  |
| [**realmClientsIdDefaultClientScopesClientScopeIdPut**](ClientsApi.md#realmClientsIdDefaultClientScopesClientScopeIdPut) | **PUT** /{realm}/clients/{id}/default-client-scopes/{clientScopeId} |  |
| [**realmClientsIdDefaultClientScopesGet**](ClientsApi.md#realmClientsIdDefaultClientScopesGet) | **GET** /{realm}/clients/{id}/default-client-scopes | Get default client scopes. |
| [**realmClientsIdDelete**](ClientsApi.md#realmClientsIdDelete) | **DELETE** /{realm}/clients/{id} | Delete the client |
| [**realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet**](ClientsApi.md#realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/generate-example-access-token | Create JSON with payload of example access token |
| [**realmClientsIdEvaluateScopesProtocolMappersGet**](ClientsApi.md#realmClientsIdEvaluateScopesProtocolMappersGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/protocol-mappers | Return list of all protocol mappers, which will be used when generating tokens issued for particular client. |
| [**realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet**](ClientsApi.md#realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/scope-mappings/{roleContainerId}/granted | Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him. |
| [**realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet**](ClientsApi.md#realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet) | **GET** /{realm}/clients/{id}/evaluate-scopes/scope-mappings/{roleContainerId}/not-granted | Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him. |
| [**realmClientsIdGet**](ClientsApi.md#realmClientsIdGet) | **GET** /{realm}/clients/{id} | Get representation of the client |
| [**realmClientsIdInstallationProvidersProviderIdGet**](ClientsApi.md#realmClientsIdInstallationProvidersProviderIdGet) | **GET** /{realm}/clients/{id}/installation/providers/{providerId} |  |
| [**realmClientsIdManagementPermissionsGet**](ClientsApi.md#realmClientsIdManagementPermissionsGet) | **GET** /{realm}/clients/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference |
| [**realmClientsIdManagementPermissionsPut**](ClientsApi.md#realmClientsIdManagementPermissionsPut) | **PUT** /{realm}/clients/{id}/management/permissions | Return object stating whether client Authorization permissions have been initialized or not and a reference |
| [**realmClientsIdNodesNodeDelete**](ClientsApi.md#realmClientsIdNodesNodeDelete) | **DELETE** /{realm}/clients/{id}/nodes/{node} | Unregister a cluster node from the client |
| [**realmClientsIdNodesPost**](ClientsApi.md#realmClientsIdNodesPost) | **POST** /{realm}/clients/{id}/nodes | Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak |
| [**realmClientsIdOfflineSessionCountGet**](ClientsApi.md#realmClientsIdOfflineSessionCountGet) | **GET** /{realm}/clients/{id}/offline-session-count | Get application offline session count   Returns a number of offline user sessions associated with this client   {      \&quot;count\&quot;: number  } |
| [**realmClientsIdOfflineSessionsGet**](ClientsApi.md#realmClientsIdOfflineSessionsGet) | **GET** /{realm}/clients/{id}/offline-sessions | Get offline sessions for client   Returns a list of offline user sessions associated with this client |
| [**realmClientsIdOptionalClientScopesClientScopeIdDelete**](ClientsApi.md#realmClientsIdOptionalClientScopesClientScopeIdDelete) | **DELETE** /{realm}/clients/{id}/optional-client-scopes/{clientScopeId} |  |
| [**realmClientsIdOptionalClientScopesClientScopeIdPut**](ClientsApi.md#realmClientsIdOptionalClientScopesClientScopeIdPut) | **PUT** /{realm}/clients/{id}/optional-client-scopes/{clientScopeId} |  |
| [**realmClientsIdOptionalClientScopesGet**](ClientsApi.md#realmClientsIdOptionalClientScopesGet) | **GET** /{realm}/clients/{id}/optional-client-scopes | Get optional client scopes. |
| [**realmClientsIdPushRevocationPost**](ClientsApi.md#realmClientsIdPushRevocationPost) | **POST** /{realm}/clients/{id}/push-revocation | Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it. |
| [**realmClientsIdPut**](ClientsApi.md#realmClientsIdPut) | **PUT** /{realm}/clients/{id} | Update the client |
| [**realmClientsIdRegistrationAccessTokenPost**](ClientsApi.md#realmClientsIdRegistrationAccessTokenPost) | **POST** /{realm}/clients/{id}/registration-access-token | Generate a new registration access token for the client |
| [**realmClientsIdServiceAccountUserGet**](ClientsApi.md#realmClientsIdServiceAccountUserGet) | **GET** /{realm}/clients/{id}/service-account-user | Get a user dedicated to the service account |
| [**realmClientsIdSessionCountGet**](ClientsApi.md#realmClientsIdSessionCountGet) | **GET** /{realm}/clients/{id}/session-count | Get application session count   Returns a number of user sessions associated with this client   {      \&quot;count\&quot;: number  } |
| [**realmClientsIdTestNodesAvailableGet**](ClientsApi.md#realmClientsIdTestNodesAvailableGet) | **GET** /{realm}/clients/{id}/test-nodes-available | Test if registered cluster nodes are available   Tests availability by sending &#39;ping&#39; request to all cluster nodes. |
| [**realmClientsIdUserSessionsGet**](ClientsApi.md#realmClientsIdUserSessionsGet) | **GET** /{realm}/clients/{id}/user-sessions | Get user sessions for client   Returns a list of user sessions associated with this client |
| [**realmClientsPost**](ClientsApi.md#realmClientsPost) | **POST** /{realm}/clients | Create a new client   Client’s client_id must be unique! |


<a id="realmClientsGet"></a>
# **realmClientsGet**
> List&lt;ClientRepresentation&gt; realmClientsGet(realm, clientId, first, max, search, viewableOnly)

Get clients belonging to the realm   Returns a list of clients belonging to the realm

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String clientId = "clientId_example"; // String | filter by clientId
    Integer first = 56; // Integer | the first result
    Integer max = 56; // Integer | the max results to return
    Boolean search = true; // Boolean | whether this is a search query or a getClientById query
    Boolean viewableOnly = true; // Boolean | filter clients that cannot be viewed in full by admin
    try {
      List<ClientRepresentation> result = apiInstance.realmClientsGet(realm, clientId, first, max, search, viewableOnly);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsGet");
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
| **clientId** | **String**| filter by clientId | [optional] |
| **first** | **Integer**| the first result | [optional] |
| **max** | **Integer**| the max results to return | [optional] |
| **search** | **Boolean**| whether this is a search query or a getClientById query | [optional] |
| **viewableOnly** | **Boolean**| filter clients that cannot be viewed in full by admin | [optional] |

### Return type

[**List&lt;ClientRepresentation&gt;**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdClientSecretGet"></a>
# **realmClientsIdClientSecretGet**
> CredentialRepresentation realmClientsIdClientSecretGet(realm, id)

Get the client secret

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      CredentialRepresentation result = apiInstance.realmClientsIdClientSecretGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdClientSecretGet");
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

[**CredentialRepresentation**](CredentialRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdClientSecretPost"></a>
# **realmClientsIdClientSecretPost**
> CredentialRepresentation realmClientsIdClientSecretPost(realm, id)

Generate a new secret for the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      CredentialRepresentation result = apiInstance.realmClientsIdClientSecretPost(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdClientSecretPost");
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

[**CredentialRepresentation**](CredentialRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdDefaultClientScopesClientScopeIdDelete"></a>
# **realmClientsIdDefaultClientScopesClientScopeIdDelete**
> realmClientsIdDefaultClientScopesClientScopeIdDelete(realm, id, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmClientsIdDefaultClientScopesClientScopeIdDelete(realm, id, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdDefaultClientScopesClientScopeIdDelete");
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

<a id="realmClientsIdDefaultClientScopesClientScopeIdPut"></a>
# **realmClientsIdDefaultClientScopesClientScopeIdPut**
> realmClientsIdDefaultClientScopesClientScopeIdPut(realm, id, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmClientsIdDefaultClientScopesClientScopeIdPut(realm, id, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdDefaultClientScopesClientScopeIdPut");
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

<a id="realmClientsIdDefaultClientScopesGet"></a>
# **realmClientsIdDefaultClientScopesGet**
> List&lt;ClientScopeRepresentation&gt; realmClientsIdDefaultClientScopesGet(realm, id)

Get default client scopes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      List<ClientScopeRepresentation> result = apiInstance.realmClientsIdDefaultClientScopesGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdDefaultClientScopesGet");
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

<a id="realmClientsIdDelete"></a>
# **realmClientsIdDelete**
> realmClientsIdDelete(realm, id)

Delete the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      apiInstance.realmClientsIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdDelete");
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

<a id="realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet"></a>
# **realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet**
> AccessToken realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet(realm, id, scope, userId)

Create JSON with payload of example access token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String scope = "scope_example"; // String | 
    String userId = "userId_example"; // String | 
    try {
      AccessToken result = apiInstance.realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet(realm, id, scope, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdEvaluateScopesGenerateExampleAccessTokenGet");
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
| **scope** | **String**|  | [optional] |
| **userId** | **String**|  | [optional] |

### Return type

[**AccessToken**](AccessToken.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdEvaluateScopesProtocolMappersGet"></a>
# **realmClientsIdEvaluateScopesProtocolMappersGet**
> List&lt;ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation&gt; realmClientsIdEvaluateScopesProtocolMappersGet(realm, id, scope)

Return list of all protocol mappers, which will be used when generating tokens issued for particular client.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String scope = "scope_example"; // String | 
    try {
      List<ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation> result = apiInstance.realmClientsIdEvaluateScopesProtocolMappersGet(realm, id, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdEvaluateScopesProtocolMappersGet");
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
| **scope** | **String**|  | [optional] |

### Return type

[**List&lt;ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation&gt;**](ClientScopeEvaluateResourceProtocolMapperEvaluationRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet"></a>
# **realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet**
> List&lt;RoleRepresentation&gt; realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet(realm, id, roleContainerId, scope)

Get effective scope mapping of all roles of particular role container, which this client is defacto allowed to have in the accessToken issued for him.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleContainerId = "roleContainerId_example"; // String | either realm name OR client UUID
    String scope = "scope_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet(realm, id, roleContainerId, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdGrantedGet");
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
| **roleContainerId** | **String**| either realm name OR client UUID | |
| **scope** | **String**|  | [optional] |

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

<a id="realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet"></a>
# **realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet**
> List&lt;RoleRepresentation&gt; realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet(realm, id, roleContainerId, scope)

Get roles, which this client doesn’t have scope for and can’t have them in the accessToken issued for him.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String roleContainerId = "roleContainerId_example"; // String | either realm name OR client UUID
    String scope = "scope_example"; // String | 
    try {
      List<RoleRepresentation> result = apiInstance.realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet(realm, id, roleContainerId, scope);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdEvaluateScopesScopeMappingsRoleContainerIdNotGrantedGet");
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
| **roleContainerId** | **String**| either realm name OR client UUID | |
| **scope** | **String**|  | [optional] |

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

<a id="realmClientsIdGet"></a>
# **realmClientsIdGet**
> ClientRepresentation realmClientsIdGet(realm, id)

Get representation of the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      ClientRepresentation result = apiInstance.realmClientsIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdGet");
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

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdInstallationProvidersProviderIdGet"></a>
# **realmClientsIdInstallationProvidersProviderIdGet**
> realmClientsIdInstallationProvidersProviderIdGet(realm, id, providerId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String providerId = "providerId_example"; // String | 
    try {
      apiInstance.realmClientsIdInstallationProvidersProviderIdGet(realm, id, providerId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdInstallationProvidersProviderIdGet");
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
| **providerId** | **String**|  | |

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

<a id="realmClientsIdManagementPermissionsGet"></a>
# **realmClientsIdManagementPermissionsGet**
> ManagementPermissionReference realmClientsIdManagementPermissionsGet(realm, id)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      ManagementPermissionReference result = apiInstance.realmClientsIdManagementPermissionsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdManagementPermissionsGet");
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

<a id="realmClientsIdManagementPermissionsPut"></a>
# **realmClientsIdManagementPermissionsPut**
> ManagementPermissionReference realmClientsIdManagementPermissionsPut(realm, id, managementPermissionReference)

Return object stating whether client Authorization permissions have been initialized or not and a reference

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    ManagementPermissionReference managementPermissionReference = new ManagementPermissionReference(); // ManagementPermissionReference | 
    try {
      ManagementPermissionReference result = apiInstance.realmClientsIdManagementPermissionsPut(realm, id, managementPermissionReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdManagementPermissionsPut");
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

<a id="realmClientsIdNodesNodeDelete"></a>
# **realmClientsIdNodesNodeDelete**
> realmClientsIdNodesNodeDelete(realm, id, node)

Unregister a cluster node from the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String node = "node_example"; // String | 
    try {
      apiInstance.realmClientsIdNodesNodeDelete(realm, id, node);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdNodesNodeDelete");
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
| **node** | **String**|  | |

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

<a id="realmClientsIdNodesPost"></a>
# **realmClientsIdNodesPost**
> realmClientsIdNodesPost(realm, id, requestBody)

Register a cluster node with the client   Manually register cluster node to this client - usually it’s not needed to call this directly as adapter should handle  by sending registration request to Keycloak

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    Map<String, Object> requestBody = null; // Map<String, Object> | 
    try {
      apiInstance.realmClientsIdNodesPost(realm, id, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdNodesPost");
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

<a id="realmClientsIdOfflineSessionCountGet"></a>
# **realmClientsIdOfflineSessionCountGet**
> Map&lt;String, Object&gt; realmClientsIdOfflineSessionCountGet(realm, id)

Get application offline session count   Returns a number of offline user sessions associated with this client   {      \&quot;count\&quot;: number  }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      Map<String, Object> result = apiInstance.realmClientsIdOfflineSessionCountGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdOfflineSessionCountGet");
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

**Map&lt;String, Object&gt;**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdOfflineSessionsGet"></a>
# **realmClientsIdOfflineSessionsGet**
> List&lt;UserSessionRepresentation&gt; realmClientsIdOfflineSessionsGet(realm, id, first, max)

Get offline sessions for client   Returns a list of offline user sessions associated with this client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    Integer first = 56; // Integer | Paging offset
    Integer max = 56; // Integer | Maximum results size (defaults to 100)
    try {
      List<UserSessionRepresentation> result = apiInstance.realmClientsIdOfflineSessionsGet(realm, id, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdOfflineSessionsGet");
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
| **first** | **Integer**| Paging offset | [optional] |
| **max** | **Integer**| Maximum results size (defaults to 100) | [optional] |

### Return type

[**List&lt;UserSessionRepresentation&gt;**](UserSessionRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdOptionalClientScopesClientScopeIdDelete"></a>
# **realmClientsIdOptionalClientScopesClientScopeIdDelete**
> realmClientsIdOptionalClientScopesClientScopeIdDelete(realm, id, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmClientsIdOptionalClientScopesClientScopeIdDelete(realm, id, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdOptionalClientScopesClientScopeIdDelete");
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

<a id="realmClientsIdOptionalClientScopesClientScopeIdPut"></a>
# **realmClientsIdOptionalClientScopesClientScopeIdPut**
> realmClientsIdOptionalClientScopesClientScopeIdPut(realm, id, clientScopeId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    String clientScopeId = "clientScopeId_example"; // String | 
    try {
      apiInstance.realmClientsIdOptionalClientScopesClientScopeIdPut(realm, id, clientScopeId);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdOptionalClientScopesClientScopeIdPut");
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

<a id="realmClientsIdOptionalClientScopesGet"></a>
# **realmClientsIdOptionalClientScopesGet**
> List&lt;ClientScopeRepresentation&gt; realmClientsIdOptionalClientScopesGet(realm, id)

Get optional client scopes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      List<ClientScopeRepresentation> result = apiInstance.realmClientsIdOptionalClientScopesGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdOptionalClientScopesGet");
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

<a id="realmClientsIdPushRevocationPost"></a>
# **realmClientsIdPushRevocationPost**
> GlobalRequestResult realmClientsIdPushRevocationPost(realm, id)

Push the client’s revocation policy to its admin URL   If the client has an admin URL, push revocation policy to it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      GlobalRequestResult result = apiInstance.realmClientsIdPushRevocationPost(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdPushRevocationPost");
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

[**GlobalRequestResult**](GlobalRequestResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdPut"></a>
# **realmClientsIdPut**
> realmClientsIdPut(realm, id, clientRepresentation)

Update the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    ClientRepresentation clientRepresentation = new ClientRepresentation(); // ClientRepresentation | 
    try {
      apiInstance.realmClientsIdPut(realm, id, clientRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdPut");
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
| **clientRepresentation** | [**ClientRepresentation**](ClientRepresentation.md)|  | |

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

<a id="realmClientsIdRegistrationAccessTokenPost"></a>
# **realmClientsIdRegistrationAccessTokenPost**
> ClientRepresentation realmClientsIdRegistrationAccessTokenPost(realm, id)

Generate a new registration access token for the client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      ClientRepresentation result = apiInstance.realmClientsIdRegistrationAccessTokenPost(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdRegistrationAccessTokenPost");
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

[**ClientRepresentation**](ClientRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdServiceAccountUserGet"></a>
# **realmClientsIdServiceAccountUserGet**
> UserRepresentation realmClientsIdServiceAccountUserGet(realm, id)

Get a user dedicated to the service account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      UserRepresentation result = apiInstance.realmClientsIdServiceAccountUserGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdServiceAccountUserGet");
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

[**UserRepresentation**](UserRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdSessionCountGet"></a>
# **realmClientsIdSessionCountGet**
> Map&lt;String, Object&gt; realmClientsIdSessionCountGet(realm, id)

Get application session count   Returns a number of user sessions associated with this client   {      \&quot;count\&quot;: number  }

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      Map<String, Object> result = apiInstance.realmClientsIdSessionCountGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdSessionCountGet");
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

**Map&lt;String, Object&gt;**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdTestNodesAvailableGet"></a>
# **realmClientsIdTestNodesAvailableGet**
> GlobalRequestResult realmClientsIdTestNodesAvailableGet(realm, id)

Test if registered cluster nodes are available   Tests availability by sending &#39;ping&#39; request to all cluster nodes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    try {
      GlobalRequestResult result = apiInstance.realmClientsIdTestNodesAvailableGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdTestNodesAvailableGet");
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

[**GlobalRequestResult**](GlobalRequestResult.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsIdUserSessionsGet"></a>
# **realmClientsIdUserSessionsGet**
> List&lt;UserSessionRepresentation&gt; realmClientsIdUserSessionsGet(realm, id, first, max)

Get user sessions for client   Returns a list of user sessions associated with this client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | id of client (not client-id)
    Integer first = 56; // Integer | Paging offset
    Integer max = 56; // Integer | Maximum results size (defaults to 100)
    try {
      List<UserSessionRepresentation> result = apiInstance.realmClientsIdUserSessionsGet(realm, id, first, max);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsIdUserSessionsGet");
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
| **first** | **Integer**| Paging offset | [optional] |
| **max** | **Integer**| Maximum results size (defaults to 100) | [optional] |

### Return type

[**List&lt;UserSessionRepresentation&gt;**](UserSessionRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmClientsPost"></a>
# **realmClientsPost**
> realmClientsPost(realm, clientRepresentation)

Create a new client   Client’s client_id must be unique!

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ClientsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    ClientsApi apiInstance = new ClientsApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    ClientRepresentation clientRepresentation = new ClientRepresentation(); // ClientRepresentation | 
    try {
      apiInstance.realmClientsPost(realm, clientRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling ClientsApi#realmClientsPost");
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
| **clientRepresentation** | [**ClientRepresentation**](ClientRepresentation.md)|  | |

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

