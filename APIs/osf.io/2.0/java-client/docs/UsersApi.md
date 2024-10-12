# UsersApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**usersAddonAccountsList**](UsersApi.md#usersAddonAccountsList) | **GET** /users/{user_id}/addons/{provider}/accounts/ | List all addon accounts |
| [**usersAddonAccountsRead**](UsersApi.md#usersAddonAccountsRead) | **GET** /users/{user_id}/addons/{provider}/accounts/{account_id}/ | Retrieve an addon account |
| [**usersAddonsList**](UsersApi.md#usersAddonsList) | **GET** /users/{user_id}/addons/ | List all user addons |
| [**usersAddonsRead**](UsersApi.md#usersAddonsRead) | **GET** /users/{user_id}/addons/{provider}/ | Retrieve a user addon |
| [**usersInstitutionsList**](UsersApi.md#usersInstitutionsList) | **GET** /users/{user_id}/institutions/ | List all institutions |
| [**usersList**](UsersApi.md#usersList) | **GET** /users/ | List all users |
| [**usersNodesList**](UsersApi.md#usersNodesList) | **GET** /users/{user_id}/nodes/ | List all nodes |
| [**usersPartialUpdate**](UsersApi.md#usersPartialUpdate) | **PATCH** /users/{user_id}/ | Update a user |
| [**usersPreprintsList**](UsersApi.md#usersPreprintsList) | **GET** /users/{user_id}/preprints/ | List all preprints |
| [**usersRead**](UsersApi.md#usersRead) | **GET** /users/{user_id}/ | Retrieve a user |
| [**usersRegistrationsList**](UsersApi.md#usersRegistrationsList) | **GET** /users/{user_id}/registrations/ | List all registrations |


<a id="usersAddonAccountsList"></a>
# **usersAddonAccountsList**
> List&lt;AddonAccount&gt; usersAddonAccountsList(userId, provider)

List all addon accounts

 A paginated list of addon accounts authorized by this user.  #### Permissions  Addon accounts are visible only to the user that authorized the account.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of at most 10 addon account objects. Each resource in the array is a separate  addon account object and contains the full representation of the addon account.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    String provider = "provider_example"; // String | The unique identifier of the addon provider.
    try {
      List<AddonAccount> result = apiInstance.usersAddonAccountsList(userId, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersAddonAccountsList");
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
| **userId** | **String**| The unique identifier of the user. | |
| **provider** | **String**| The unique identifier of the addon provider. | |

### Return type

[**List&lt;AddonAccount&gt;**](AddonAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersAddonAccountsRead"></a>
# **usersAddonAccountsRead**
> AddonAccount usersAddonAccountsRead(userId, provider, accountId)

Retrieve an addon account

Retrieves the details of an addon account  #### Permissions  Addon accounts are visible only to the user that authorized the account.  #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested addon account, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    String provider = "provider_example"; // String | The unique identifier of the addon provider.
    String accountId = "accountId_example"; // String | The unique identifier of the addon account.
    try {
      AddonAccount result = apiInstance.usersAddonAccountsRead(userId, provider, accountId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersAddonAccountsRead");
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
| **userId** | **String**| The unique identifier of the user. | |
| **provider** | **String**| The unique identifier of the addon provider. | |
| **accountId** | **String**| The unique identifier of the addon account. | |

### Return type

[**AddonAccount**](AddonAccount.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersAddonsList"></a>
# **usersAddonsList**
> List&lt;UserAddon&gt; usersAddonsList(userId)

List all user addons

 A paginated list of authorized user addons  #### Permissions  User addons are visible only to the user that authorized the addon.  #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of up to 10 addons. Each resource in the array is a separate addon object.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      List<UserAddon> result = apiInstance.usersAddonsList(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersAddonsList");
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
| **userId** | **String**| The unique identifier of the user. | |

### Return type

[**List&lt;UserAddon&gt;**](UserAddon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersAddonsRead"></a>
# **usersAddonsRead**
> UserAddon usersAddonsRead(userId, provider)

Retrieve a user addon

Retrieves the details of an authorized user addon  #### Permissions  User addons are visible only to the user that authorized the addon.  #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested user addon, if the request was successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.  Attempting to request the accounts for an addon that is not enabled will result in a **404 Not Found** response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    String provider = "provider_example"; // String | The unique identifier of the addon provider.
    try {
      UserAddon result = apiInstance.usersAddonsRead(userId, provider);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersAddonsRead");
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
| **userId** | **String**| The unique identifier of the user. | |
| **provider** | **String**| The unique identifier of the addon provider. | |

### Return type

[**UserAddon**](UserAddon.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersInstitutionsList"></a>
# **usersInstitutionsList**
> List&lt;Institution&gt; usersInstitutionsList(userId)

List all institutions

A paginated list of institutions that the user is affiliated with. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 institutions. Each resource in the array is a complete institution object and contains the full representation of the institution, meaning additional requests to a institution&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      List<Institution> result = apiInstance.usersInstitutionsList(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersInstitutionsList");
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
| **userId** | **String**| The unique identifier of the user. | |

### Return type

[**List&lt;Institution&gt;**](Institution.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersList"></a>
# **usersList**
> List&lt;User&gt; usersList()

List all users

 A paginated list of all users registered on the OSF. The returned users are sorted by their &#x60;date_registered&#x60;, with the most recently registered users appearing first.  The subroute &#x60;/users/me/&#x60; is a special endpoint that always points to the currently logged-in user. #### Versioning As of version &#x60;2.3&#x60;, merged users will not be returned from this endpoint. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 users. Each resource in the array is a separate users object and contains the full representation of the user, meaning additional requests to a user&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  This request should never return an error. #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/users/?filter[family_name]&#x3D;Nosek.  Users may be filtered by their &#x60;id&#x60;, &#x60;full_name&#x60;, &#x60;given_name&#x60;, &#x60;middle_name&#x60;, or &#x60;family_name&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    try {
      List<User> result = apiInstance.usersList();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersList");
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

[**List&lt;User&gt;**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersNodesList"></a>
# **usersNodesList**
> List&lt;Node&gt; usersNodesList(userId)

List all nodes

A paginated list of nodes that the user is a contributor to. The returned nodes are sorted by their &#x60;date_modified&#x60;, with the most recently updated nodes appearing first.  If the user ID in the path is the same as the logged-in user, all nodes will be returned. Otherwise, only the user&#39;s public nodes will be returned.  User registrations are not available at this endpoint. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include nodes that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/users/cdi38/nodes/?filter[title]&#x3D;open.  Nodes may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;category&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, &#x60;preprint&#x60;, and &#x60;contributors&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      List<Node> result = apiInstance.usersNodesList(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersNodesList");
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
| **userId** | **String**| The unique identifier of the user. | |

### Return type

[**List&lt;Node&gt;**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersPartialUpdate"></a>
# **usersPartialUpdate**
> usersPartialUpdate(userId, user)

Update a user

Updates a user by setting the values of the attributes specified in the request body. Any unspecified attributes will be left unchanged.  Users can be updated with either a **PUT** or **PATCH** request. The &#x60;full_name&#x60; field is mandatory in a **PUT** request, and optional in a **PATCH**.  **Note**: if you make a PUT/PATCH request to the &#x60;/users/me/&#x60; endpoint, you must still provide your full user ID in the ID field of the request. We do not support using the &#x60;me&#x60; alias in request bodies at this time. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the new representation of the updated node, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    User user = new User(); // User | 
    try {
      apiInstance.usersPartialUpdate(userId, user);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPartialUpdate");
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
| **userId** | **String**| The unique identifier of the user. | |
| **user** | [**User**](User.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersPreprintsList"></a>
# **usersPreprintsList**
> List&lt;Preprint&gt; usersPreprintsList(userId)

List all preprints

A paginated list of preprints that the user contributes to. The returned preprints are sorted by their creation date, with the most recent preprints appearing first. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 preprints. Each resource in the array is a complete preprint object and contains the full representation of the preprint, meaning additional requests to a preprint&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include preprints that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/users/cdi38/preprints/?filter[provider]&#x3D;psyarxiv.  Preprints may be filtered by their &#x60;id&#x60;, &#x60;is_published&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, and &#x60;provider&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      List<Preprint> result = apiInstance.usersPreprintsList(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersPreprintsList");
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
| **userId** | **String**| The unique identifier of the user. | |

### Return type

[**List&lt;Preprint&gt;**](Preprint.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersRead"></a>
# **usersRead**
> User usersRead(userId)

Retrieve a user

Retrieves the details of a given users.  The returned information includes the user&#39;s bibliographic information and the date the user was registered.  Additionally, relationships to the list of institutions with which the user is affiliated, and to the list of nodes which the user contributes to (that the requesting user has permission to see) are returned.  If &#x60;me&#x60; is given as the &#x60;user_id&#x60; in the request path, the record of the currently logged-in user will be returned. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested user, if the request is successful.  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      User result = apiInstance.usersRead(userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersRead");
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
| **userId** | **String**| The unique identifier of the user. | |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="usersRegistrationsList"></a>
# **usersRegistrationsList**
> usersRegistrationsList(userId)

List all registrations

A paginated list of registrations that the user is a contributor to. The returned registrations are sorted by their &#x60;date_modified&#x60;, with the most recently updated registrations appearing first.  If the user ID in the path is the same as the logged-in user, all registrations will be returned. Otherwise, only the user&#39;s public registrations will be returned.  User nodes are not available at this endpoint. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys.  The &#x60;data&#x60; key contains an array of 10 registrations. Each resource in the array is a separate registration object and contains the full representation of the registration, meaning additional requests to a registration&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination). #### Filtering You can optionally request that the response only include registrations that match your filters by utilizing the &#x60;filter&#x60; query parameter, e.g. https://api.osf.io/v2/users/cdi38/registrations/?filter[title]&#x3D;replication.  Registrations may be filtered by their &#x60;id&#x60;, &#x60;title&#x60;, &#x60;category&#x60;, &#x60;description&#x60;, &#x60;public&#x60;, &#x60;tags&#x60;, &#x60;date_created&#x60;, &#x60;date_modified&#x60;, &#x60;root&#x60;, &#x60;parent&#x60;, and &#x60;contributors&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    UsersApi apiInstance = new UsersApi(defaultClient);
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      apiInstance.usersRegistrationsList(userId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersApi#usersRegistrationsList");
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
| **userId** | **String**| The unique identifier of the user. | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

