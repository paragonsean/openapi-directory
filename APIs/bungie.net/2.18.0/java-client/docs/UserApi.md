# UserApi

All URIs are relative to *https://www.bungie.net/Platform*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userGetAvailableThemes**](UserApi.md#userGetAvailableThemes) | **GET** /User/GetAvailableThemes/ |  |
| [**userGetBungieNetUserById**](UserApi.md#userGetBungieNetUserById) | **GET** /User/GetBungieNetUserById/{id}/ |  |
| [**userGetCredentialTypesForTargetAccount**](UserApi.md#userGetCredentialTypesForTargetAccount) | **GET** /User/GetCredentialTypesForTargetAccount/{membershipId}/ |  |
| [**userGetMembershipDataById**](UserApi.md#userGetMembershipDataById) | **GET** /User/GetMembershipsById/{membershipId}/{membershipType}/ |  |
| [**userGetMembershipDataForCurrentUser**](UserApi.md#userGetMembershipDataForCurrentUser) | **GET** /User/GetMembershipsForCurrentUser/ |  |
| [**userGetMembershipFromHardLinkedCredential**](UserApi.md#userGetMembershipFromHardLinkedCredential) | **GET** /User/GetMembershipFromHardLinkedCredential/{crType}/{credential}/ |  |
| [**userGetSanitizedPlatformDisplayNames**](UserApi.md#userGetSanitizedPlatformDisplayNames) | **GET** /User/GetSanitizedPlatformDisplayNames/{membershipId}/ |  |
| [**userSearchByGlobalNamePost**](UserApi.md#userSearchByGlobalNamePost) | **POST** /User/Search/GlobalName/{page}/ |  |
| [**userSearchByGlobalNamePrefix**](UserApi.md#userSearchByGlobalNamePrefix) | **GET** /User/Search/Prefix/{displayNamePrefix}/{page}/ |  |


<a id="userGetAvailableThemes"></a>
# **userGetAvailableThemes**
> UserGetAvailableThemes200Response userGetAvailableThemes()



Returns a list of all available user themes.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      UserGetAvailableThemes200Response result = apiInstance.userGetAvailableThemes();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetAvailableThemes");
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

[**UserGetAvailableThemes200Response**](UserGetAvailableThemes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userGetBungieNetUserById"></a>
# **userGetBungieNetUserById**
> UserGetBungieNetUserById200Response userGetBungieNetUserById(id)



Loads a bungienet user by membership id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    Long id = 56L; // Long | The requested Bungie.net membership id.
    try {
      UserGetBungieNetUserById200Response result = apiInstance.userGetBungieNetUserById(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetBungieNetUserById");
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
| **id** | **Long**| The requested Bungie.net membership id. | |

### Return type

[**UserGetBungieNetUserById200Response**](UserGetBungieNetUserById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userGetCredentialTypesForTargetAccount"></a>
# **userGetCredentialTypesForTargetAccount**
> UserGetCredentialTypesForTargetAccount200Response userGetCredentialTypesForTargetAccount(membershipId)



Returns a list of credential types attached to the requested account

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    Long membershipId = 56L; // Long | The user's membership id
    try {
      UserGetCredentialTypesForTargetAccount200Response result = apiInstance.userGetCredentialTypesForTargetAccount(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetCredentialTypesForTargetAccount");
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
| **membershipId** | **Long**| The user&#39;s membership id | |

### Return type

[**UserGetCredentialTypesForTargetAccount200Response**](UserGetCredentialTypesForTargetAccount200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userGetMembershipDataById"></a>
# **userGetMembershipDataById**
> UserGetMembershipDataById200Response userGetMembershipDataById(membershipId, membershipType)



Returns a list of accounts associated with the supplied membership ID and membership type. This will include all linked accounts (even when hidden) if supplied credentials permit it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    Long membershipId = 56L; // Long | The membership ID of the target user.
    Integer membershipType = 56; // Integer | Type of the supplied membership ID.
    try {
      UserGetMembershipDataById200Response result = apiInstance.userGetMembershipDataById(membershipId, membershipType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetMembershipDataById");
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
| **membershipId** | **Long**| The membership ID of the target user. | |
| **membershipType** | **Integer**| Type of the supplied membership ID. | |

### Return type

[**UserGetMembershipDataById200Response**](UserGetMembershipDataById200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userGetMembershipDataForCurrentUser"></a>
# **userGetMembershipDataForCurrentUser**
> UserGetMembershipDataById200Response userGetMembershipDataForCurrentUser()



Returns a list of accounts associated with signed in user. This is useful for OAuth implementations that do not give you access to the token response.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    UserApi apiInstance = new UserApi(defaultClient);
    try {
      UserGetMembershipDataById200Response result = apiInstance.userGetMembershipDataForCurrentUser();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetMembershipDataForCurrentUser");
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

[**UserGetMembershipDataById200Response**](UserGetMembershipDataById200Response.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userGetMembershipFromHardLinkedCredential"></a>
# **userGetMembershipFromHardLinkedCredential**
> UserGetMembershipFromHardLinkedCredential200Response userGetMembershipFromHardLinkedCredential(credential, crType)



Gets any hard linked membership given a credential. Only works for credentials that are public (just SteamID64 right now). Cross Save aware.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    String credential = "credential_example"; // String | The credential to look up. Must be a valid SteamID64.
    Integer crType = 56; // Integer | The credential type. 'SteamId' is the only valid value at present.
    try {
      UserGetMembershipFromHardLinkedCredential200Response result = apiInstance.userGetMembershipFromHardLinkedCredential(credential, crType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetMembershipFromHardLinkedCredential");
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
| **credential** | **String**| The credential to look up. Must be a valid SteamID64. | |
| **crType** | **Integer**| The credential type. &#39;SteamId&#39; is the only valid value at present. | |

### Return type

[**UserGetMembershipFromHardLinkedCredential200Response**](UserGetMembershipFromHardLinkedCredential200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userGetSanitizedPlatformDisplayNames"></a>
# **userGetSanitizedPlatformDisplayNames**
> GetAvailableLocales200Response userGetSanitizedPlatformDisplayNames(membershipId)



Gets a list of all display names linked to this membership id but sanitized (profanity filtered). Obeys all visibility rules of calling user and is heavily cached.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    Long membershipId = 56L; // Long | The requested membership id to load.
    try {
      GetAvailableLocales200Response result = apiInstance.userGetSanitizedPlatformDisplayNames(membershipId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userGetSanitizedPlatformDisplayNames");
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
| **membershipId** | **Long**| The requested membership id to load. | |

### Return type

[**GetAvailableLocales200Response**](GetAvailableLocales200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userSearchByGlobalNamePost"></a>
# **userSearchByGlobalNamePost**
> UserSearchByGlobalNamePost200Response userSearchByGlobalNamePost(page)



Given the prefix of a global display name, returns all users who share that name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    Integer page = 56; // Integer | The zero-based page of results you desire.
    try {
      UserSearchByGlobalNamePost200Response result = apiInstance.userSearchByGlobalNamePost(page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userSearchByGlobalNamePost");
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
| **page** | **Integer**| The zero-based page of results you desire. | |

### Return type

[**UserSearchByGlobalNamePost200Response**](UserSearchByGlobalNamePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

<a id="userSearchByGlobalNamePrefix"></a>
# **userSearchByGlobalNamePrefix**
> UserSearchByGlobalNamePost200Response userSearchByGlobalNamePrefix(displayNamePrefix, page)



[OBSOLETE] Do not use this to search users, use SearchByGlobalNamePost instead.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UserApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.bungie.net/Platform");

    UserApi apiInstance = new UserApi(defaultClient);
    String displayNamePrefix = "displayNamePrefix_example"; // String | The display name prefix you're looking for.
    Integer page = 56; // Integer | The zero-based page of results you desire.
    try {
      UserSearchByGlobalNamePost200Response result = apiInstance.userSearchByGlobalNamePrefix(displayNamePrefix, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UserApi#userSearchByGlobalNamePrefix");
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
| **displayNamePrefix** | **String**| The display name prefix you&#39;re looking for. | |
| **page** | **Integer**| The zero-based page of results you desire. | |

### Return type

[**UserSearchByGlobalNamePost200Response**](UserSearchByGlobalNamePost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Look at the Response property for more information about the nature of this response |  -  |

