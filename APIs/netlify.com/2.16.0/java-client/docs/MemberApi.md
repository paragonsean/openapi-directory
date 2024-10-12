# MemberApi

All URIs are relative to *https://api.netlify.com/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addMemberToAccount**](MemberApi.md#addMemberToAccount) | **POST** /{account_slug}/members |  |
| [**getAccountMember**](MemberApi.md#getAccountMember) | **GET** /{account_slug}/members/{member_id} |  |
| [**listMembersForAccount**](MemberApi.md#listMembersForAccount) | **GET** /{account_slug}/members |  |
| [**removeAccountMember**](MemberApi.md#removeAccountMember) | **DELETE** /{account_slug}/members/{member_id} |  |
| [**updateAccountMember**](MemberApi.md#updateAccountMember) | **PUT** /{account_slug}/members/{member_id} |  |


<a id="addMemberToAccount"></a>
# **addMemberToAccount**
> List&lt;Member&gt; addMemberToAccount(accountSlug, accountAddMemberSetup)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    AccountAddMemberSetup accountAddMemberSetup = new AccountAddMemberSetup(); // AccountAddMemberSetup | 
    try {
      List<Member> result = apiInstance.addMemberToAccount(accountSlug, accountAddMemberSetup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#addMemberToAccount");
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
| **accountSlug** | **String**|  | |
| **accountAddMemberSetup** | [**AccountAddMemberSetup**](AccountAddMemberSetup.md)|  | |

### Return type

[**List&lt;Member&gt;**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="getAccountMember"></a>
# **getAccountMember**
> Member getAccountMember(accountSlug, memberId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    String memberId = "memberId_example"; // String | 
    try {
      Member result = apiInstance.getAccountMember(accountSlug, memberId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#getAccountMember");
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
| **accountSlug** | **String**|  | |
| **memberId** | **String**|  | |

### Return type

[**Member**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="listMembersForAccount"></a>
# **listMembersForAccount**
> List&lt;Member&gt; listMembersForAccount(accountSlug)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    try {
      List<Member> result = apiInstance.listMembersForAccount(accountSlug);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#listMembersForAccount");
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
| **accountSlug** | **String**|  | |

### Return type

[**List&lt;Member&gt;**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

<a id="removeAccountMember"></a>
# **removeAccountMember**
> removeAccountMember(accountSlug, memberId)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    String memberId = "memberId_example"; // String | 
    try {
      apiInstance.removeAccountMember(accountSlug, memberId);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#removeAccountMember");
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
| **accountSlug** | **String**|  | |
| **memberId** | **String**|  | |

### Return type

null (empty response body)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** | Not Content |  -  |
| **0** | error |  -  |

<a id="updateAccountMember"></a>
# **updateAccountMember**
> Member updateAccountMember(accountSlug, memberId, accountUpdateMemberSetup)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.MemberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.netlify.com/api/v1");
    
    // Configure OAuth2 access token for authorization: netlifyAuth
    OAuth netlifyAuth = (OAuth) defaultClient.getAuthentication("netlifyAuth");
    netlifyAuth.setAccessToken("YOUR ACCESS TOKEN");

    MemberApi apiInstance = new MemberApi(defaultClient);
    String accountSlug = "accountSlug_example"; // String | 
    String memberId = "memberId_example"; // String | 
    AccountUpdateMemberSetup accountUpdateMemberSetup = new AccountUpdateMemberSetup(); // AccountUpdateMemberSetup | 
    try {
      Member result = apiInstance.updateAccountMember(accountSlug, memberId, accountUpdateMemberSetup);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling MemberApi#updateAccountMember");
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
| **accountSlug** | **String**|  | |
| **memberId** | **String**|  | |
| **accountUpdateMemberSetup** | [**AccountUpdateMemberSetup**](AccountUpdateMemberSetup.md)|  | |

### Return type

[**Member**](Member.md)

### Authorization

[netlifyAuth](../README.md#netlifyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | error |  -  |

