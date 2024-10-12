# AuthenticationManagementApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmAuthenticationAuthenticatorProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationAuthenticatorProvidersGet) | **GET** /{realm}/authentication/authenticator-providers | Get authenticator providers   Returns a list of authenticator providers. |
| [**realmAuthenticationClientAuthenticatorProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationClientAuthenticatorProvidersGet) | **GET** /{realm}/authentication/client-authenticator-providers | Get client authenticator providers   Returns a list of client authenticator providers. |
| [**realmAuthenticationConfigDescriptionProviderIdGet**](AuthenticationManagementApi.md#realmAuthenticationConfigDescriptionProviderIdGet) | **GET** /{realm}/authentication/config-description/{providerId} | Get authenticator provider’s configuration description |
| [**realmAuthenticationConfigIdDelete**](AuthenticationManagementApi.md#realmAuthenticationConfigIdDelete) | **DELETE** /{realm}/authentication/config/{id} | Delete authenticator configuration |
| [**realmAuthenticationConfigIdGet**](AuthenticationManagementApi.md#realmAuthenticationConfigIdGet) | **GET** /{realm}/authentication/config/{id} | Get authenticator configuration |
| [**realmAuthenticationConfigIdPut**](AuthenticationManagementApi.md#realmAuthenticationConfigIdPut) | **PUT** /{realm}/authentication/config/{id} | Update authenticator configuration |
| [**realmAuthenticationExecutionsExecutionIdConfigPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdConfigPost) | **POST** /{realm}/authentication/executions/{executionId}/config | Update execution with new configuration |
| [**realmAuthenticationExecutionsExecutionIdDelete**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdDelete) | **DELETE** /{realm}/authentication/executions/{executionId} | Delete execution |
| [**realmAuthenticationExecutionsExecutionIdGet**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdGet) | **GET** /{realm}/authentication/executions/{executionId} | Get Single Execution |
| [**realmAuthenticationExecutionsExecutionIdLowerPriorityPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdLowerPriorityPost) | **POST** /{realm}/authentication/executions/{executionId}/lower-priority | Lower execution’s priority |
| [**realmAuthenticationExecutionsExecutionIdRaisePriorityPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsExecutionIdRaisePriorityPost) | **POST** /{realm}/authentication/executions/{executionId}/raise-priority | Raise execution’s priority |
| [**realmAuthenticationExecutionsPost**](AuthenticationManagementApi.md#realmAuthenticationExecutionsPost) | **POST** /{realm}/authentication/executions | Add new authentication execution |
| [**realmAuthenticationFlowsFlowAliasCopyPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasCopyPost) | **POST** /{realm}/authentication/flows/{flowAlias}/copy | Copy existing authentication flow under a new name   The new name is given as &#39;newName&#39; attribute of the passed JSON object |
| [**realmAuthenticationFlowsFlowAliasExecutionsExecutionPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsExecutionPost) | **POST** /{realm}/authentication/flows/{flowAlias}/executions/execution | Add new authentication execution to a flow |
| [**realmAuthenticationFlowsFlowAliasExecutionsFlowPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsFlowPost) | **POST** /{realm}/authentication/flows/{flowAlias}/executions/flow | Add new flow with new execution to existing flow |
| [**realmAuthenticationFlowsFlowAliasExecutionsGet**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsGet) | **GET** /{realm}/authentication/flows/{flowAlias}/executions | Get authentication executions for a flow |
| [**realmAuthenticationFlowsFlowAliasExecutionsPut**](AuthenticationManagementApi.md#realmAuthenticationFlowsFlowAliasExecutionsPut) | **PUT** /{realm}/authentication/flows/{flowAlias}/executions | Update authentication executions of a flow |
| [**realmAuthenticationFlowsGet**](AuthenticationManagementApi.md#realmAuthenticationFlowsGet) | **GET** /{realm}/authentication/flows | Get authentication flows   Returns a list of authentication flows. |
| [**realmAuthenticationFlowsIdDelete**](AuthenticationManagementApi.md#realmAuthenticationFlowsIdDelete) | **DELETE** /{realm}/authentication/flows/{id} | Delete an authentication flow |
| [**realmAuthenticationFlowsIdGet**](AuthenticationManagementApi.md#realmAuthenticationFlowsIdGet) | **GET** /{realm}/authentication/flows/{id} | Get authentication flow for id |
| [**realmAuthenticationFlowsIdPut**](AuthenticationManagementApi.md#realmAuthenticationFlowsIdPut) | **PUT** /{realm}/authentication/flows/{id} | Update an authentication flow |
| [**realmAuthenticationFlowsPost**](AuthenticationManagementApi.md#realmAuthenticationFlowsPost) | **POST** /{realm}/authentication/flows | Create a new authentication flow |
| [**realmAuthenticationFormActionProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationFormActionProvidersGet) | **GET** /{realm}/authentication/form-action-providers | Get form action providers   Returns a list of form action providers. |
| [**realmAuthenticationFormProvidersGet**](AuthenticationManagementApi.md#realmAuthenticationFormProvidersGet) | **GET** /{realm}/authentication/form-providers | Get form providers   Returns a list of form providers. |
| [**realmAuthenticationPerClientConfigDescriptionGet**](AuthenticationManagementApi.md#realmAuthenticationPerClientConfigDescriptionGet) | **GET** /{realm}/authentication/per-client-config-description | Get configuration descriptions for all clients |
| [**realmAuthenticationRegisterRequiredActionPost**](AuthenticationManagementApi.md#realmAuthenticationRegisterRequiredActionPost) | **POST** /{realm}/authentication/register-required-action | Register a new required actions |
| [**realmAuthenticationRequiredActionsAliasDelete**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasDelete) | **DELETE** /{realm}/authentication/required-actions/{alias} | Delete required action |
| [**realmAuthenticationRequiredActionsAliasGet**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasGet) | **GET** /{realm}/authentication/required-actions/{alias} | Get required action for alias |
| [**realmAuthenticationRequiredActionsAliasLowerPriorityPost**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasLowerPriorityPost) | **POST** /{realm}/authentication/required-actions/{alias}/lower-priority | Lower required action’s priority |
| [**realmAuthenticationRequiredActionsAliasPut**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasPut) | **PUT** /{realm}/authentication/required-actions/{alias} | Update required action |
| [**realmAuthenticationRequiredActionsAliasRaisePriorityPost**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsAliasRaisePriorityPost) | **POST** /{realm}/authentication/required-actions/{alias}/raise-priority | Raise required action’s priority |
| [**realmAuthenticationRequiredActionsGet**](AuthenticationManagementApi.md#realmAuthenticationRequiredActionsGet) | **GET** /{realm}/authentication/required-actions | Get required actions   Returns a list of required actions. |
| [**realmAuthenticationUnregisteredRequiredActionsGet**](AuthenticationManagementApi.md#realmAuthenticationUnregisteredRequiredActionsGet) | **GET** /{realm}/authentication/unregistered-required-actions | Get unregistered required actions   Returns a list of unregistered required actions. |


<a id="realmAuthenticationAuthenticatorProvidersGet"></a>
# **realmAuthenticationAuthenticatorProvidersGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmAuthenticationAuthenticatorProvidersGet(realm)

Get authenticator providers   Returns a list of authenticator providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<Map<String, Object>> result = apiInstance.realmAuthenticationAuthenticatorProvidersGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationAuthenticatorProvidersGet");
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

<a id="realmAuthenticationClientAuthenticatorProvidersGet"></a>
# **realmAuthenticationClientAuthenticatorProvidersGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmAuthenticationClientAuthenticatorProvidersGet(realm)

Get client authenticator providers   Returns a list of client authenticator providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<Map<String, Object>> result = apiInstance.realmAuthenticationClientAuthenticatorProvidersGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationClientAuthenticatorProvidersGet");
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

<a id="realmAuthenticationConfigDescriptionProviderIdGet"></a>
# **realmAuthenticationConfigDescriptionProviderIdGet**
> AuthenticatorConfigInfoRepresentation realmAuthenticationConfigDescriptionProviderIdGet(realm, providerId)

Get authenticator provider’s configuration description

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String providerId = "providerId_example"; // String | 
    try {
      AuthenticatorConfigInfoRepresentation result = apiInstance.realmAuthenticationConfigDescriptionProviderIdGet(realm, providerId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationConfigDescriptionProviderIdGet");
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
| **providerId** | **String**|  | |

### Return type

[**AuthenticatorConfigInfoRepresentation**](AuthenticatorConfigInfoRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAuthenticationConfigIdDelete"></a>
# **realmAuthenticationConfigIdDelete**
> realmAuthenticationConfigIdDelete(realm, id)

Delete authenticator configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | Configuration id
    try {
      apiInstance.realmAuthenticationConfigIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationConfigIdDelete");
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
| **id** | **String**| Configuration id | |

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

<a id="realmAuthenticationConfigIdGet"></a>
# **realmAuthenticationConfigIdGet**
> AuthenticatorConfigRepresentation realmAuthenticationConfigIdGet(realm, id)

Get authenticator configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | Configuration id
    try {
      AuthenticatorConfigRepresentation result = apiInstance.realmAuthenticationConfigIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationConfigIdGet");
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
| **id** | **String**| Configuration id | |

### Return type

[**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAuthenticationConfigIdPut"></a>
# **realmAuthenticationConfigIdPut**
> realmAuthenticationConfigIdPut(realm, id, authenticatorConfigRepresentation)

Update authenticator configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | Configuration id
    AuthenticatorConfigRepresentation authenticatorConfigRepresentation = new AuthenticatorConfigRepresentation(); // AuthenticatorConfigRepresentation | JSON describing new state of authenticator configuration
    try {
      apiInstance.realmAuthenticationConfigIdPut(realm, id, authenticatorConfigRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationConfigIdPut");
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
| **id** | **String**| Configuration id | |
| **authenticatorConfigRepresentation** | [**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)| JSON describing new state of authenticator configuration | |

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

<a id="realmAuthenticationExecutionsExecutionIdConfigPost"></a>
# **realmAuthenticationExecutionsExecutionIdConfigPost**
> realmAuthenticationExecutionsExecutionIdConfigPost(realm, executionId, authenticatorConfigRepresentation)

Update execution with new configuration

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String executionId = "executionId_example"; // String | Execution id
    AuthenticatorConfigRepresentation authenticatorConfigRepresentation = new AuthenticatorConfigRepresentation(); // AuthenticatorConfigRepresentation | JSON with new configuration
    try {
      apiInstance.realmAuthenticationExecutionsExecutionIdConfigPost(realm, executionId, authenticatorConfigRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationExecutionsExecutionIdConfigPost");
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
| **executionId** | **String**| Execution id | |
| **authenticatorConfigRepresentation** | [**AuthenticatorConfigRepresentation**](AuthenticatorConfigRepresentation.md)| JSON with new configuration | |

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

<a id="realmAuthenticationExecutionsExecutionIdDelete"></a>
# **realmAuthenticationExecutionsExecutionIdDelete**
> realmAuthenticationExecutionsExecutionIdDelete(realm, executionId)

Delete execution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String executionId = "executionId_example"; // String | Execution id
    try {
      apiInstance.realmAuthenticationExecutionsExecutionIdDelete(realm, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationExecutionsExecutionIdDelete");
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
| **executionId** | **String**| Execution id | |

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

<a id="realmAuthenticationExecutionsExecutionIdGet"></a>
# **realmAuthenticationExecutionsExecutionIdGet**
> realmAuthenticationExecutionsExecutionIdGet(realm, executionId)

Get Single Execution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String executionId = "executionId_example"; // String | Execution id
    try {
      apiInstance.realmAuthenticationExecutionsExecutionIdGet(realm, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationExecutionsExecutionIdGet");
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
| **executionId** | **String**| Execution id | |

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

<a id="realmAuthenticationExecutionsExecutionIdLowerPriorityPost"></a>
# **realmAuthenticationExecutionsExecutionIdLowerPriorityPost**
> realmAuthenticationExecutionsExecutionIdLowerPriorityPost(realm, executionId)

Lower execution’s priority

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String executionId = "executionId_example"; // String | Execution id
    try {
      apiInstance.realmAuthenticationExecutionsExecutionIdLowerPriorityPost(realm, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationExecutionsExecutionIdLowerPriorityPost");
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
| **executionId** | **String**| Execution id | |

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

<a id="realmAuthenticationExecutionsExecutionIdRaisePriorityPost"></a>
# **realmAuthenticationExecutionsExecutionIdRaisePriorityPost**
> realmAuthenticationExecutionsExecutionIdRaisePriorityPost(realm, executionId)

Raise execution’s priority

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String executionId = "executionId_example"; // String | Execution id
    try {
      apiInstance.realmAuthenticationExecutionsExecutionIdRaisePriorityPost(realm, executionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationExecutionsExecutionIdRaisePriorityPost");
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
| **executionId** | **String**| Execution id | |

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

<a id="realmAuthenticationExecutionsPost"></a>
# **realmAuthenticationExecutionsPost**
> realmAuthenticationExecutionsPost(realm, authenticationExecutionRepresentation)

Add new authentication execution

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    AuthenticationExecutionRepresentation authenticationExecutionRepresentation = new AuthenticationExecutionRepresentation(); // AuthenticationExecutionRepresentation | JSON model describing authentication execution
    try {
      apiInstance.realmAuthenticationExecutionsPost(realm, authenticationExecutionRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationExecutionsPost");
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
| **authenticationExecutionRepresentation** | [**AuthenticationExecutionRepresentation**](AuthenticationExecutionRepresentation.md)| JSON model describing authentication execution | |

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

<a id="realmAuthenticationFlowsFlowAliasCopyPost"></a>
# **realmAuthenticationFlowsFlowAliasCopyPost**
> realmAuthenticationFlowsFlowAliasCopyPost(realm, flowAlias, requestBody)

Copy existing authentication flow under a new name   The new name is given as &#39;newName&#39; attribute of the passed JSON object

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String flowAlias = "flowAlias_example"; // String | Name of the existing authentication flow
    Map<String, Object> requestBody = null; // Map<String, Object> | JSON containing 'newName' attribute
    try {
      apiInstance.realmAuthenticationFlowsFlowAliasCopyPost(realm, flowAlias, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsFlowAliasCopyPost");
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
| **flowAlias** | **String**| Name of the existing authentication flow | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| JSON containing &#39;newName&#39; attribute | |

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

<a id="realmAuthenticationFlowsFlowAliasExecutionsExecutionPost"></a>
# **realmAuthenticationFlowsFlowAliasExecutionsExecutionPost**
> realmAuthenticationFlowsFlowAliasExecutionsExecutionPost(realm, flowAlias, requestBody)

Add new authentication execution to a flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String flowAlias = "flowAlias_example"; // String | Alias of parent flow
    Map<String, Object> requestBody = null; // Map<String, Object> | New execution JSON data containing 'provider' attribute
    try {
      apiInstance.realmAuthenticationFlowsFlowAliasExecutionsExecutionPost(realm, flowAlias, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsFlowAliasExecutionsExecutionPost");
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
| **flowAlias** | **String**| Alias of parent flow | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| New execution JSON data containing &#39;provider&#39; attribute | |

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

<a id="realmAuthenticationFlowsFlowAliasExecutionsFlowPost"></a>
# **realmAuthenticationFlowsFlowAliasExecutionsFlowPost**
> realmAuthenticationFlowsFlowAliasExecutionsFlowPost(realm, flowAlias, requestBody)

Add new flow with new execution to existing flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String flowAlias = "flowAlias_example"; // String | Alias of parent authentication flow
    Map<String, Object> requestBody = null; // Map<String, Object> | New authentication flow / execution JSON data containing 'alias', 'type', 'provider', and 'description' attributes
    try {
      apiInstance.realmAuthenticationFlowsFlowAliasExecutionsFlowPost(realm, flowAlias, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsFlowAliasExecutionsFlowPost");
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
| **flowAlias** | **String**| Alias of parent authentication flow | |
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| New authentication flow / execution JSON data containing &#39;alias&#39;, &#39;type&#39;, &#39;provider&#39;, and &#39;description&#39; attributes | |

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

<a id="realmAuthenticationFlowsFlowAliasExecutionsGet"></a>
# **realmAuthenticationFlowsFlowAliasExecutionsGet**
> realmAuthenticationFlowsFlowAliasExecutionsGet(realm, flowAlias)

Get authentication executions for a flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String flowAlias = "flowAlias_example"; // String | Flow alias
    try {
      apiInstance.realmAuthenticationFlowsFlowAliasExecutionsGet(realm, flowAlias);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsFlowAliasExecutionsGet");
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
| **flowAlias** | **String**| Flow alias | |

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

<a id="realmAuthenticationFlowsFlowAliasExecutionsPut"></a>
# **realmAuthenticationFlowsFlowAliasExecutionsPut**
> realmAuthenticationFlowsFlowAliasExecutionsPut(realm, flowAlias, authenticationExecutionInfoRepresentation)

Update authentication executions of a flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String flowAlias = "flowAlias_example"; // String | Flow alias
    AuthenticationExecutionInfoRepresentation authenticationExecutionInfoRepresentation = new AuthenticationExecutionInfoRepresentation(); // AuthenticationExecutionInfoRepresentation | 
    try {
      apiInstance.realmAuthenticationFlowsFlowAliasExecutionsPut(realm, flowAlias, authenticationExecutionInfoRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsFlowAliasExecutionsPut");
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
| **flowAlias** | **String**| Flow alias | |
| **authenticationExecutionInfoRepresentation** | [**AuthenticationExecutionInfoRepresentation**](AuthenticationExecutionInfoRepresentation.md)|  | |

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

<a id="realmAuthenticationFlowsGet"></a>
# **realmAuthenticationFlowsGet**
> List&lt;AuthenticationFlowRepresentation&gt; realmAuthenticationFlowsGet(realm)

Get authentication flows   Returns a list of authentication flows.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<AuthenticationFlowRepresentation> result = apiInstance.realmAuthenticationFlowsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsGet");
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

[**List&lt;AuthenticationFlowRepresentation&gt;**](AuthenticationFlowRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAuthenticationFlowsIdDelete"></a>
# **realmAuthenticationFlowsIdDelete**
> realmAuthenticationFlowsIdDelete(realm, id)

Delete an authentication flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | Flow id
    try {
      apiInstance.realmAuthenticationFlowsIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsIdDelete");
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
| **id** | **String**| Flow id | |

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

<a id="realmAuthenticationFlowsIdGet"></a>
# **realmAuthenticationFlowsIdGet**
> AuthenticationFlowRepresentation realmAuthenticationFlowsIdGet(realm, id)

Get authentication flow for id

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | Flow id
    try {
      AuthenticationFlowRepresentation result = apiInstance.realmAuthenticationFlowsIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsIdGet");
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
| **id** | **String**| Flow id | |

### Return type

[**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAuthenticationFlowsIdPut"></a>
# **realmAuthenticationFlowsIdPut**
> realmAuthenticationFlowsIdPut(realm, id, authenticationFlowRepresentation)

Update an authentication flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | Flow id
    AuthenticationFlowRepresentation authenticationFlowRepresentation = new AuthenticationFlowRepresentation(); // AuthenticationFlowRepresentation | Authentication flow representation
    try {
      apiInstance.realmAuthenticationFlowsIdPut(realm, id, authenticationFlowRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsIdPut");
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
| **id** | **String**| Flow id | |
| **authenticationFlowRepresentation** | [**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)| Authentication flow representation | |

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

<a id="realmAuthenticationFlowsPost"></a>
# **realmAuthenticationFlowsPost**
> realmAuthenticationFlowsPost(realm, authenticationFlowRepresentation)

Create a new authentication flow

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    AuthenticationFlowRepresentation authenticationFlowRepresentation = new AuthenticationFlowRepresentation(); // AuthenticationFlowRepresentation | Authentication flow representation
    try {
      apiInstance.realmAuthenticationFlowsPost(realm, authenticationFlowRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFlowsPost");
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
| **authenticationFlowRepresentation** | [**AuthenticationFlowRepresentation**](AuthenticationFlowRepresentation.md)| Authentication flow representation | |

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

<a id="realmAuthenticationFormActionProvidersGet"></a>
# **realmAuthenticationFormActionProvidersGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmAuthenticationFormActionProvidersGet(realm)

Get form action providers   Returns a list of form action providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<Map<String, Object>> result = apiInstance.realmAuthenticationFormActionProvidersGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFormActionProvidersGet");
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

<a id="realmAuthenticationFormProvidersGet"></a>
# **realmAuthenticationFormProvidersGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmAuthenticationFormProvidersGet(realm)

Get form providers   Returns a list of form providers.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<Map<String, Object>> result = apiInstance.realmAuthenticationFormProvidersGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationFormProvidersGet");
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

<a id="realmAuthenticationPerClientConfigDescriptionGet"></a>
# **realmAuthenticationPerClientConfigDescriptionGet**
> Map&lt;String, Object&gt; realmAuthenticationPerClientConfigDescriptionGet(realm)

Get configuration descriptions for all clients

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      Map<String, Object> result = apiInstance.realmAuthenticationPerClientConfigDescriptionGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationPerClientConfigDescriptionGet");
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

<a id="realmAuthenticationRegisterRequiredActionPost"></a>
# **realmAuthenticationRegisterRequiredActionPost**
> realmAuthenticationRegisterRequiredActionPost(realm, requestBody)

Register a new required actions

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    Map<String, Object> requestBody = null; // Map<String, Object> | JSON containing 'providerId', and 'name' attributes.
    try {
      apiInstance.realmAuthenticationRegisterRequiredActionPost(realm, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRegisterRequiredActionPost");
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
| **requestBody** | [**Map&lt;String, Object&gt;**](Object.md)| JSON containing &#39;providerId&#39;, and &#39;name&#39; attributes. | |

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

<a id="realmAuthenticationRequiredActionsAliasDelete"></a>
# **realmAuthenticationRequiredActionsAliasDelete**
> realmAuthenticationRequiredActionsAliasDelete(realm, alias)

Delete required action

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | Alias of required action
    try {
      apiInstance.realmAuthenticationRequiredActionsAliasDelete(realm, alias);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRequiredActionsAliasDelete");
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
| **alias** | **String**| Alias of required action | |

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

<a id="realmAuthenticationRequiredActionsAliasGet"></a>
# **realmAuthenticationRequiredActionsAliasGet**
> RequiredActionProviderRepresentation realmAuthenticationRequiredActionsAliasGet(realm, alias)

Get required action for alias

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | Alias of required action
    try {
      RequiredActionProviderRepresentation result = apiInstance.realmAuthenticationRequiredActionsAliasGet(realm, alias);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRequiredActionsAliasGet");
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
| **alias** | **String**| Alias of required action | |

### Return type

[**RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAuthenticationRequiredActionsAliasLowerPriorityPost"></a>
# **realmAuthenticationRequiredActionsAliasLowerPriorityPost**
> realmAuthenticationRequiredActionsAliasLowerPriorityPost(realm, alias)

Lower required action’s priority

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | Alias of required action
    try {
      apiInstance.realmAuthenticationRequiredActionsAliasLowerPriorityPost(realm, alias);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRequiredActionsAliasLowerPriorityPost");
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
| **alias** | **String**| Alias of required action | |

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

<a id="realmAuthenticationRequiredActionsAliasPut"></a>
# **realmAuthenticationRequiredActionsAliasPut**
> realmAuthenticationRequiredActionsAliasPut(realm, alias, requiredActionProviderRepresentation)

Update required action

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | Alias of required action
    RequiredActionProviderRepresentation requiredActionProviderRepresentation = new RequiredActionProviderRepresentation(); // RequiredActionProviderRepresentation | JSON describing new state of required action
    try {
      apiInstance.realmAuthenticationRequiredActionsAliasPut(realm, alias, requiredActionProviderRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRequiredActionsAliasPut");
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
| **alias** | **String**| Alias of required action | |
| **requiredActionProviderRepresentation** | [**RequiredActionProviderRepresentation**](RequiredActionProviderRepresentation.md)| JSON describing new state of required action | |

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

<a id="realmAuthenticationRequiredActionsAliasRaisePriorityPost"></a>
# **realmAuthenticationRequiredActionsAliasRaisePriorityPost**
> realmAuthenticationRequiredActionsAliasRaisePriorityPost(realm, alias)

Raise required action’s priority

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String alias = "alias_example"; // String | Alias of required action
    try {
      apiInstance.realmAuthenticationRequiredActionsAliasRaisePriorityPost(realm, alias);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRequiredActionsAliasRaisePriorityPost");
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
| **alias** | **String**| Alias of required action | |

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

<a id="realmAuthenticationRequiredActionsGet"></a>
# **realmAuthenticationRequiredActionsGet**
> List&lt;RequiredActionProviderRepresentation&gt; realmAuthenticationRequiredActionsGet(realm)

Get required actions   Returns a list of required actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<RequiredActionProviderRepresentation> result = apiInstance.realmAuthenticationRequiredActionsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationRequiredActionsGet");
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

[**List&lt;RequiredActionProviderRepresentation&gt;**](RequiredActionProviderRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmAuthenticationUnregisteredRequiredActionsGet"></a>
# **realmAuthenticationUnregisteredRequiredActionsGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmAuthenticationUnregisteredRequiredActionsGet(realm)

Get unregistered required actions   Returns a list of unregistered required actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AuthenticationManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    AuthenticationManagementApi apiInstance = new AuthenticationManagementApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    try {
      List<Map<String, Object>> result = apiInstance.realmAuthenticationUnregisteredRequiredActionsGet(realm);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AuthenticationManagementApi#realmAuthenticationUnregisteredRequiredActionsGet");
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

