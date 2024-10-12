# UsersApi

All URIs are relative to *http://keycloak.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**realmUsersCountGet**](UsersApi.md#realmUsersCountGet) | **GET** /{realm}/users/count | Returns the number of users that match the given criteria. |
| [**realmUsersGet**](UsersApi.md#realmUsersGet) | **GET** /{realm}/users | Get users   Returns a list of users, filtered according to query parameters |
| [**realmUsersIdConfiguredUserStorageCredentialTypesGet**](UsersApi.md#realmUsersIdConfiguredUserStorageCredentialTypesGet) | **GET** /{realm}/users/{id}/configured-user-storage-credential-types | Return credential types, which are provided by the user storage where user is stored. |
| [**realmUsersIdConsentsClientDelete**](UsersApi.md#realmUsersIdConsentsClientDelete) | **DELETE** /{realm}/users/{id}/consents/{client} | Revoke consent and offline tokens for particular client from user |
| [**realmUsersIdConsentsGet**](UsersApi.md#realmUsersIdConsentsGet) | **GET** /{realm}/users/{id}/consents | Get consents granted by the user |
| [**realmUsersIdCredentialsCredentialIdDelete**](UsersApi.md#realmUsersIdCredentialsCredentialIdDelete) | **DELETE** /{realm}/users/{id}/credentials/{credentialId} | Remove a credential for a user |
| [**realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost**](UsersApi.md#realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost) | **POST** /{realm}/users/{id}/credentials/{credentialId}/moveAfter/{newPreviousCredentialId} | Move a credential to a position behind another credential |
| [**realmUsersIdCredentialsCredentialIdMoveToFirstPost**](UsersApi.md#realmUsersIdCredentialsCredentialIdMoveToFirstPost) | **POST** /{realm}/users/{id}/credentials/{credentialId}/moveToFirst | Move a credential to a first position in the credentials list of the user |
| [**realmUsersIdCredentialsCredentialIdUserLabelPut**](UsersApi.md#realmUsersIdCredentialsCredentialIdUserLabelPut) | **PUT** /{realm}/users/{id}/credentials/{credentialId}/userLabel | Update a credential label for a user |
| [**realmUsersIdCredentialsGet**](UsersApi.md#realmUsersIdCredentialsGet) | **GET** /{realm}/users/{id}/credentials |  |
| [**realmUsersIdDelete**](UsersApi.md#realmUsersIdDelete) | **DELETE** /{realm}/users/{id} | Delete the user |
| [**realmUsersIdDisableCredentialTypesPut**](UsersApi.md#realmUsersIdDisableCredentialTypesPut) | **PUT** /{realm}/users/{id}/disable-credential-types | Disable all credentials for a user of a specific type |
| [**realmUsersIdExecuteActionsEmailPut**](UsersApi.md#realmUsersIdExecuteActionsEmailPut) | **PUT** /{realm}/users/{id}/execute-actions-email | Send a update account email to the user   An email contains a link the user can click to perform a set of required actions. |
| [**realmUsersIdFederatedIdentityGet**](UsersApi.md#realmUsersIdFederatedIdentityGet) | **GET** /{realm}/users/{id}/federated-identity | Get social logins associated with the user |
| [**realmUsersIdFederatedIdentityProviderDelete**](UsersApi.md#realmUsersIdFederatedIdentityProviderDelete) | **DELETE** /{realm}/users/{id}/federated-identity/{provider} | Remove a social login provider from user |
| [**realmUsersIdFederatedIdentityProviderPost**](UsersApi.md#realmUsersIdFederatedIdentityProviderPost) | **POST** /{realm}/users/{id}/federated-identity/{provider} | Add a social login provider to the user |
| [**realmUsersIdGet**](UsersApi.md#realmUsersIdGet) | **GET** /{realm}/users/{id} | Get representation of the user |
| [**realmUsersIdGroupsCountGet**](UsersApi.md#realmUsersIdGroupsCountGet) | **GET** /{realm}/users/{id}/groups/count |  |
| [**realmUsersIdGroupsGet**](UsersApi.md#realmUsersIdGroupsGet) | **GET** /{realm}/users/{id}/groups |  |
| [**realmUsersIdGroupsGroupIdDelete**](UsersApi.md#realmUsersIdGroupsGroupIdDelete) | **DELETE** /{realm}/users/{id}/groups/{groupId} |  |
| [**realmUsersIdGroupsGroupIdPut**](UsersApi.md#realmUsersIdGroupsGroupIdPut) | **PUT** /{realm}/users/{id}/groups/{groupId} |  |
| [**realmUsersIdImpersonationPost**](UsersApi.md#realmUsersIdImpersonationPost) | **POST** /{realm}/users/{id}/impersonation | Impersonate the user |
| [**realmUsersIdLogoutPost**](UsersApi.md#realmUsersIdLogoutPost) | **POST** /{realm}/users/{id}/logout | Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user. |
| [**realmUsersIdOfflineSessionsClientIdGet**](UsersApi.md#realmUsersIdOfflineSessionsClientIdGet) | **GET** /{realm}/users/{id}/offline-sessions/{clientId} | Get offline sessions associated with the user and client |
| [**realmUsersIdPut**](UsersApi.md#realmUsersIdPut) | **PUT** /{realm}/users/{id} | Update the user |
| [**realmUsersIdResetPasswordPut**](UsersApi.md#realmUsersIdResetPasswordPut) | **PUT** /{realm}/users/{id}/reset-password | Set up a new password for the user. |
| [**realmUsersIdSendVerifyEmailPut**](UsersApi.md#realmUsersIdSendVerifyEmailPut) | **PUT** /{realm}/users/{id}/send-verify-email | Send an email-verification email to the user   An email contains a link the user can click to verify their email address. |
| [**realmUsersIdSessionsGet**](UsersApi.md#realmUsersIdSessionsGet) | **GET** /{realm}/users/{id}/sessions | Get sessions associated with the user |
| [**realmUsersPost**](UsersApi.md#realmUsersPost) | **POST** /{realm}/users | Create a new user   Username must be unique. |


<a id="realmUsersCountGet"></a>
# **realmUsersCountGet**
> Integer realmUsersCountGet(realm, email, firstName, lastName, search, username)

Returns the number of users that match the given criteria.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String email = "email_example"; // String | email filter
    String firstName = "firstName_example"; // String | first name filter
    String lastName = "lastName_example"; // String | last name filter
    String search = "search_example"; // String | arbitrary search string for all the fields below
    String username = "username_example"; // String | username filter
    try {
      Integer result = apiInstance.realmUsersCountGet(realm, email, firstName, lastName, search, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersCountGet");
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
| **email** | **String**| email filter | [optional] |
| **firstName** | **String**| first name filter | [optional] |
| **lastName** | **String**| last name filter | [optional] |
| **search** | **String**| arbitrary search string for all the fields below | [optional] |
| **username** | **String**| username filter | [optional] |

### Return type

**Integer**

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersGet"></a>
# **realmUsersGet**
> List&lt;UserRepresentation&gt; realmUsersGet(realm, briefRepresentation, email, first, firstName, lastName, max, search, username)

Get users   Returns a list of users, filtered according to query parameters

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    Boolean briefRepresentation = true; // Boolean | 
    String email = "email_example"; // String | 
    Integer first = 56; // Integer | 
    String firstName = "firstName_example"; // String | 
    String lastName = "lastName_example"; // String | 
    Integer max = 56; // Integer | Maximum results size (defaults to 100)
    String search = "search_example"; // String | A String contained in username, first or last name, or email
    String username = "username_example"; // String | 
    try {
      List<UserRepresentation> result = apiInstance.realmUsersGet(realm, briefRepresentation, email, first, firstName, lastName, max, search, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersGet");
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
| **email** | **String**|  | [optional] |
| **first** | **Integer**|  | [optional] |
| **firstName** | **String**|  | [optional] |
| **lastName** | **String**|  | [optional] |
| **max** | **Integer**| Maximum results size (defaults to 100) | [optional] |
| **search** | **String**| A String contained in username, first or last name, or email | [optional] |
| **username** | **String**|  | [optional] |

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

<a id="realmUsersIdConfiguredUserStorageCredentialTypesGet"></a>
# **realmUsersIdConfiguredUserStorageCredentialTypesGet**
> List&lt;String&gt; realmUsersIdConfiguredUserStorageCredentialTypesGet(realm, id)

Return credential types, which are provided by the user storage where user is stored.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<String> result = apiInstance.realmUsersIdConfiguredUserStorageCredentialTypesGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdConfiguredUserStorageCredentialTypesGet");
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

<a id="realmUsersIdConsentsClientDelete"></a>
# **realmUsersIdConsentsClientDelete**
> realmUsersIdConsentsClientDelete(realm, id, client)

Revoke consent and offline tokens for particular client from user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String client = "client_example"; // String | Client id
    try {
      apiInstance.realmUsersIdConsentsClientDelete(realm, id, client);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdConsentsClientDelete");
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
| **client** | **String**| Client id | |

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

<a id="realmUsersIdConsentsGet"></a>
# **realmUsersIdConsentsGet**
> List&lt;Map&lt;String, Object&gt;&gt; realmUsersIdConsentsGet(realm, id)

Get consents granted by the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<Map<String, Object>> result = apiInstance.realmUsersIdConsentsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdConsentsGet");
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

<a id="realmUsersIdCredentialsCredentialIdDelete"></a>
# **realmUsersIdCredentialsCredentialIdDelete**
> realmUsersIdCredentialsCredentialIdDelete(realm, id, credentialId)

Remove a credential for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String credentialId = "credentialId_example"; // String | 
    try {
      apiInstance.realmUsersIdCredentialsCredentialIdDelete(realm, id, credentialId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdCredentialsCredentialIdDelete");
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
| **credentialId** | **String**|  | |

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

<a id="realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost"></a>
# **realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost**
> realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost(realm, id, credentialId, newPreviousCredentialId)

Move a credential to a position behind another credential

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String credentialId = "credentialId_example"; // String | The credential to move
    String newPreviousCredentialId = "newPreviousCredentialId_example"; // String | The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list.
    try {
      apiInstance.realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost(realm, id, credentialId, newPreviousCredentialId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdCredentialsCredentialIdMoveAfterNewPreviousCredentialIdPost");
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
| **credentialId** | **String**| The credential to move | |
| **newPreviousCredentialId** | **String**| The credential that will be the previous element in the list. If set to null, the moved credential will be the first element in the list. | |

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

<a id="realmUsersIdCredentialsCredentialIdMoveToFirstPost"></a>
# **realmUsersIdCredentialsCredentialIdMoveToFirstPost**
> realmUsersIdCredentialsCredentialIdMoveToFirstPost(realm, id, credentialId)

Move a credential to a first position in the credentials list of the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String credentialId = "credentialId_example"; // String | The credential to move
    try {
      apiInstance.realmUsersIdCredentialsCredentialIdMoveToFirstPost(realm, id, credentialId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdCredentialsCredentialIdMoveToFirstPost");
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
| **credentialId** | **String**| The credential to move | |

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

<a id="realmUsersIdCredentialsCredentialIdUserLabelPut"></a>
# **realmUsersIdCredentialsCredentialIdUserLabelPut**
> realmUsersIdCredentialsCredentialIdUserLabelPut(realm, id, credentialId, body)

Update a credential label for a user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String credentialId = "credentialId_example"; // String | 
    String body = "body_example"; // String | 
    try {
      apiInstance.realmUsersIdCredentialsCredentialIdUserLabelPut(realm, id, credentialId, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdCredentialsCredentialIdUserLabelPut");
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
| **credentialId** | **String**|  | |
| **body** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdCredentialsGet"></a>
# **realmUsersIdCredentialsGet**
> List&lt;CredentialRepresentation&gt; realmUsersIdCredentialsGet(realm, id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<CredentialRepresentation> result = apiInstance.realmUsersIdCredentialsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdCredentialsGet");
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

### Return type

[**List&lt;CredentialRepresentation&gt;**](CredentialRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdDelete"></a>
# **realmUsersIdDelete**
> realmUsersIdDelete(realm, id)

Delete the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      apiInstance.realmUsersIdDelete(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdDelete");
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

<a id="realmUsersIdDisableCredentialTypesPut"></a>
# **realmUsersIdDisableCredentialTypesPut**
> realmUsersIdDisableCredentialTypesPut(realm, id, requestBody)

Disable all credentials for a user of a specific type

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    List<String> requestBody = Arrays.asList(); // List<String> | 
    try {
      apiInstance.realmUsersIdDisableCredentialTypesPut(realm, id, requestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdDisableCredentialTypesPut");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)|  | |

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

<a id="realmUsersIdExecuteActionsEmailPut"></a>
# **realmUsersIdExecuteActionsEmailPut**
> realmUsersIdExecuteActionsEmailPut(realm, id, requestBody, clientId, lifespan, redirectUri)

Send a update account email to the user   An email contains a link the user can click to perform a set of required actions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    List<String> requestBody = Arrays.asList(); // List<String> | required actions the user needs to complete
    String clientId = "clientId_example"; // String | Client id
    Integer lifespan = 56; // Integer | Number of seconds after which the generated token expires
    String redirectUri = "redirectUri_example"; // String | Redirect uri
    try {
      apiInstance.realmUsersIdExecuteActionsEmailPut(realm, id, requestBody, clientId, lifespan, redirectUri);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdExecuteActionsEmailPut");
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
| **requestBody** | [**List&lt;String&gt;**](String.md)| required actions the user needs to complete | |
| **clientId** | **String**| Client id | [optional] |
| **lifespan** | **Integer**| Number of seconds after which the generated token expires | [optional] |
| **redirectUri** | **String**| Redirect uri | [optional] |

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

<a id="realmUsersIdFederatedIdentityGet"></a>
# **realmUsersIdFederatedIdentityGet**
> List&lt;FederatedIdentityRepresentation&gt; realmUsersIdFederatedIdentityGet(realm, id)

Get social logins associated with the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<FederatedIdentityRepresentation> result = apiInstance.realmUsersIdFederatedIdentityGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdFederatedIdentityGet");
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

### Return type

[**List&lt;FederatedIdentityRepresentation&gt;**](FederatedIdentityRepresentation.md)

### Authorization

[access_token](../README.md#access_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **2XX** | success |  -  |

<a id="realmUsersIdFederatedIdentityProviderDelete"></a>
# **realmUsersIdFederatedIdentityProviderDelete**
> realmUsersIdFederatedIdentityProviderDelete(realm, id, provider)

Remove a social login provider from user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String provider = "provider_example"; // String | Social login provider id
    try {
      apiInstance.realmUsersIdFederatedIdentityProviderDelete(realm, id, provider);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdFederatedIdentityProviderDelete");
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
| **provider** | **String**| Social login provider id | |

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

<a id="realmUsersIdFederatedIdentityProviderPost"></a>
# **realmUsersIdFederatedIdentityProviderPost**
> realmUsersIdFederatedIdentityProviderPost(realm, id, provider, federatedIdentityRepresentation)

Add a social login provider to the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String provider = "provider_example"; // String | Social login provider id
    FederatedIdentityRepresentation federatedIdentityRepresentation = new FederatedIdentityRepresentation(); // FederatedIdentityRepresentation | 
    try {
      apiInstance.realmUsersIdFederatedIdentityProviderPost(realm, id, provider, federatedIdentityRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdFederatedIdentityProviderPost");
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
| **provider** | **String**| Social login provider id | |
| **federatedIdentityRepresentation** | [**FederatedIdentityRepresentation**](FederatedIdentityRepresentation.md)|  | |

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

<a id="realmUsersIdGet"></a>
# **realmUsersIdGet**
> UserRepresentation realmUsersIdGet(realm, id)

Get representation of the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      UserRepresentation result = apiInstance.realmUsersIdGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdGet");
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

<a id="realmUsersIdGroupsCountGet"></a>
# **realmUsersIdGroupsCountGet**
> Map&lt;String, Object&gt; realmUsersIdGroupsCountGet(realm, id, search)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String search = "search_example"; // String | 
    try {
      Map<String, Object> result = apiInstance.realmUsersIdGroupsCountGet(realm, id, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdGroupsCountGet");
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
| **search** | **String**|  | [optional] |

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

<a id="realmUsersIdGroupsGet"></a>
# **realmUsersIdGroupsGet**
> List&lt;GroupRepresentation&gt; realmUsersIdGroupsGet(realm, id, briefRepresentation, first, max, search)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    Boolean briefRepresentation = true; // Boolean | 
    Integer first = 56; // Integer | 
    Integer max = 56; // Integer | 
    String search = "search_example"; // String | 
    try {
      List<GroupRepresentation> result = apiInstance.realmUsersIdGroupsGet(realm, id, briefRepresentation, first, max, search);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdGroupsGet");
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
| **briefRepresentation** | **Boolean**|  | [optional] |
| **first** | **Integer**|  | [optional] |
| **max** | **Integer**|  | [optional] |
| **search** | **String**|  | [optional] |

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

<a id="realmUsersIdGroupsGroupIdDelete"></a>
# **realmUsersIdGroupsGroupIdDelete**
> realmUsersIdGroupsGroupIdDelete(realm, id, groupId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.realmUsersIdGroupsGroupIdDelete(realm, id, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdGroupsGroupIdDelete");
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

<a id="realmUsersIdGroupsGroupIdPut"></a>
# **realmUsersIdGroupsGroupIdPut**
> realmUsersIdGroupsGroupIdPut(realm, id, groupId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String groupId = "groupId_example"; // String | 
    try {
      apiInstance.realmUsersIdGroupsGroupIdPut(realm, id, groupId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdGroupsGroupIdPut");
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

<a id="realmUsersIdImpersonationPost"></a>
# **realmUsersIdImpersonationPost**
> Map&lt;String, Object&gt; realmUsersIdImpersonationPost(realm, id)

Impersonate the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      Map<String, Object> result = apiInstance.realmUsersIdImpersonationPost(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdImpersonationPost");
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

<a id="realmUsersIdLogoutPost"></a>
# **realmUsersIdLogoutPost**
> realmUsersIdLogoutPost(realm, id)

Remove all user sessions associated with the user   Also send notification to all clients that have an admin URL to invalidate the sessions for the particular user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      apiInstance.realmUsersIdLogoutPost(realm, id);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdLogoutPost");
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

<a id="realmUsersIdOfflineSessionsClientIdGet"></a>
# **realmUsersIdOfflineSessionsClientIdGet**
> List&lt;UserSessionRepresentation&gt; realmUsersIdOfflineSessionsClientIdGet(realm, id, clientId)

Get offline sessions associated with the user and client

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String clientId = "clientId_example"; // String | 
    try {
      List<UserSessionRepresentation> result = apiInstance.realmUsersIdOfflineSessionsClientIdGet(realm, id, clientId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdOfflineSessionsClientIdGet");
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
| **clientId** | **String**|  | |

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

<a id="realmUsersIdPut"></a>
# **realmUsersIdPut**
> realmUsersIdPut(realm, id, userRepresentation)

Update the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    UserRepresentation userRepresentation = new UserRepresentation(); // UserRepresentation | 
    try {
      apiInstance.realmUsersIdPut(realm, id, userRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdPut");
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
| **userRepresentation** | [**UserRepresentation**](UserRepresentation.md)|  | |

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

<a id="realmUsersIdResetPasswordPut"></a>
# **realmUsersIdResetPasswordPut**
> realmUsersIdResetPasswordPut(realm, id, credentialRepresentation)

Set up a new password for the user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    CredentialRepresentation credentialRepresentation = new CredentialRepresentation(); // CredentialRepresentation | The representation must contain a rawPassword with the plain-text password
    try {
      apiInstance.realmUsersIdResetPasswordPut(realm, id, credentialRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdResetPasswordPut");
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
| **credentialRepresentation** | [**CredentialRepresentation**](CredentialRepresentation.md)| The representation must contain a rawPassword with the plain-text password | |

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

<a id="realmUsersIdSendVerifyEmailPut"></a>
# **realmUsersIdSendVerifyEmailPut**
> realmUsersIdSendVerifyEmailPut(realm, id, clientId, redirectUri)

Send an email-verification email to the user   An email contains a link the user can click to verify their email address.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    String clientId = "clientId_example"; // String | Client id
    String redirectUri = "redirectUri_example"; // String | Redirect uri
    try {
      apiInstance.realmUsersIdSendVerifyEmailPut(realm, id, clientId, redirectUri);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdSendVerifyEmailPut");
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
| **clientId** | **String**| Client id | [optional] |
| **redirectUri** | **String**| Redirect uri | [optional] |

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

<a id="realmUsersIdSessionsGet"></a>
# **realmUsersIdSessionsGet**
> List&lt;UserSessionRepresentation&gt; realmUsersIdSessionsGet(realm, id)

Get sessions associated with the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    String id = "id_example"; // String | User id
    try {
      List<UserSessionRepresentation> result = apiInstance.realmUsersIdSessionsGet(realm, id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersIdSessionsGet");
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

<a id="realmUsersPost"></a>
# **realmUsersPost**
> realmUsersPost(realm, userRepresentation)

Create a new user   Username must be unique.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://keycloak.local");
    
    // Configure HTTP bearer authorization: access_token
    HttpBearerAuth access_token = (HttpBearerAuth) defaultClient.getAuthentication("access_token");
    access_token.setBearerToken("BEARER TOKEN");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String realm = "realm_example"; // String | realm name (not id!)
    UserRepresentation userRepresentation = new UserRepresentation(); // UserRepresentation | 
    try {
      apiInstance.realmUsersPost(realm, userRepresentation);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#realmUsersPost");
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
| **userRepresentation** | [**UserRepresentation**](UserRepresentation.md)|  | |

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

