# AccountsApi

All URIs are relative to *http://mastodon.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV1AccountsIdBlockPost**](AccountsApi.md#apiV1AccountsIdBlockPost) | **POST** /api/v1/accounts/{id}/block |  |
| [**apiV1AccountsIdFeaturedTagsGet**](AccountsApi.md#apiV1AccountsIdFeaturedTagsGet) | **GET** /api/v1/accounts/{id}/featured_tags |  |
| [**apiV1AccountsIdFollowPost**](AccountsApi.md#apiV1AccountsIdFollowPost) | **POST** /api/v1/accounts/{id}/follow |  |
| [**apiV1AccountsIdFollowersGet**](AccountsApi.md#apiV1AccountsIdFollowersGet) | **GET** /api/v1/accounts/{id}/followers |  |
| [**apiV1AccountsIdFollowingGet**](AccountsApi.md#apiV1AccountsIdFollowingGet) | **GET** /api/v1/accounts/{id}/following |  |
| [**apiV1AccountsIdGet**](AccountsApi.md#apiV1AccountsIdGet) | **GET** /api/v1/accounts/{id} |  |
| [**apiV1AccountsIdIdentityProofsGet**](AccountsApi.md#apiV1AccountsIdIdentityProofsGet) | **GET** /api/v1/accounts/{id}/identity_proofs |  |
| [**apiV1AccountsIdListsGet**](AccountsApi.md#apiV1AccountsIdListsGet) | **GET** /api/v1/accounts/{id}/lists |  |
| [**apiV1AccountsIdMutePost**](AccountsApi.md#apiV1AccountsIdMutePost) | **POST** /api/v1/accounts/{id}/mute |  |
| [**apiV1AccountsIdNotePost**](AccountsApi.md#apiV1AccountsIdNotePost) | **POST** /api/v1/accounts/{id}/note |  |
| [**apiV1AccountsIdPinPost**](AccountsApi.md#apiV1AccountsIdPinPost) | **POST** /api/v1/accounts/{id}/pin |  |
| [**apiV1AccountsIdStatusesGet**](AccountsApi.md#apiV1AccountsIdStatusesGet) | **GET** /api/v1/accounts/{id}/statuses |  |
| [**apiV1AccountsIdUnblockPost**](AccountsApi.md#apiV1AccountsIdUnblockPost) | **POST** /api/v1/accounts/{id}/unblock |  |
| [**apiV1AccountsIdUnfollowPost**](AccountsApi.md#apiV1AccountsIdUnfollowPost) | **POST** /api/v1/accounts/{id}/unfollow |  |
| [**apiV1AccountsIdUnmutePost**](AccountsApi.md#apiV1AccountsIdUnmutePost) | **POST** /api/v1/accounts/{id}/unmute |  |
| [**apiV1AccountsIdUnpinPost**](AccountsApi.md#apiV1AccountsIdUnpinPost) | **POST** /api/v1/accounts/{id}/unpin |  |
| [**apiV1AccountsPost_0**](AccountsApi.md#apiV1AccountsPost_0) | **POST** /api/v1/accounts |  |
| [**apiV1AccountsRelationshipsGet**](AccountsApi.md#apiV1AccountsRelationshipsGet) | **GET** /api/v1/accounts/relationships |  |
| [**apiV1AccountsSearchGet**](AccountsApi.md#apiV1AccountsSearchGet) | **GET** /api/v1/accounts/search |  |
| [**apiV1AccountsUpdateCredentialsPatch**](AccountsApi.md#apiV1AccountsUpdateCredentialsPatch) | **PATCH** /api/v1/accounts/update_credentials |  |
| [**apiV1AccountsVerifyCredentialsGet**](AccountsApi.md#apiV1AccountsVerifyCredentialsGet) | **GET** /api/v1/accounts/verify_credentials |  |


<a id="apiV1AccountsIdBlockPost"></a>
# **apiV1AccountsIdBlockPost**
> Relationship apiV1AccountsIdBlockPost(id)



Block the given account. Clients should filter statuses from this account if received (e.g. due to a boost in the Home timeline).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1AccountsIdBlockPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdBlockPost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully blocked, or account was already blocked |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1AccountsIdFeaturedTagsGet"></a>
# **apiV1AccountsIdFeaturedTagsGet**
> List&lt;FeaturedTag&gt; apiV1AccountsIdFeaturedTagsGet(id)



Tags featured by this account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      List<FeaturedTag> result = apiInstance.apiV1AccountsIdFeaturedTagsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdFeaturedTagsGet");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**List&lt;FeaturedTag&gt;**](FeaturedTag.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header, or instance is in whitelist mode and your token is not authorized with a user |  -  |

<a id="apiV1AccountsIdFollowPost"></a>
# **apiV1AccountsIdFollowPost**
> Relationship apiV1AccountsIdFollowPost(id, apiV1AccountsIdFollowPostRequest)



Follow the given account. Can also be used to update whether to show reblogs or enable notifications.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    ApiV1AccountsIdFollowPostRequest apiV1AccountsIdFollowPostRequest = new ApiV1AccountsIdFollowPostRequest(); // ApiV1AccountsIdFollowPostRequest | 
    try {
      Relationship result = apiInstance.apiV1AccountsIdFollowPost(id, apiV1AccountsIdFollowPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdFollowPost");
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
| **id** | **String**| The id of the account in the database | |
| **apiV1AccountsIdFollowPostRequest** | [**ApiV1AccountsIdFollowPostRequest**](ApiV1AccountsIdFollowPostRequest.md)|  | [optional] |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully followed, or account was already followed |  -  |
| **403** | Trying to follow someone that you block or that blocks you |  -  |

<a id="apiV1AccountsIdFollowersGet"></a>
# **apiV1AccountsIdFollowersGet**
> List&lt;Account&gt; apiV1AccountsIdFollowersGet(id, maxId, sinceId, limit)



Accounts which follow the given account, if network is not hidden by the account owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    String maxId = "maxId_example"; // String | Internal parameter. Use HTTP `Link` header for pagination.
    String sinceId = "sinceId_example"; // String | Internal parameter. Use HTTP `Link` header for pagination.
    Integer limit = 40; // Integer | Maximum number of results to return. Defaults to 40.
    try {
      List<Account> result = apiInstance.apiV1AccountsIdFollowersGet(id, maxId, sinceId, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdFollowersGet");
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
| **id** | **String**| The id of the account in the database | |
| **maxId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] |
| **sinceId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] |
| **limit** | **Integer**| Maximum number of results to return. Defaults to 40. | [optional] [default to 40] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header, or instance is in whitelist mode and your token is not authorized with a user |  -  |
| **404** | Account is deleted or does not exist |  -  |
| **410** | Account is suspended |  -  |

<a id="apiV1AccountsIdFollowingGet"></a>
# **apiV1AccountsIdFollowingGet**
> List&lt;Account&gt; apiV1AccountsIdFollowingGet(id, maxId, sinceId, limit)



Accounts which the given account is following, if network is not hidden by the account owner.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    String maxId = "maxId_example"; // String | Internal parameter. Use HTTP `Link` header for pagination.
    String sinceId = "sinceId_example"; // String | Internal parameter. Use HTTP `Link` header for pagination.
    Integer limit = 40; // Integer | Maximum number of results to return. Defaults to 40.
    try {
      List<Account> result = apiInstance.apiV1AccountsIdFollowingGet(id, maxId, sinceId, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdFollowingGet");
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
| **id** | **String**| The id of the account in the database | |
| **maxId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] |
| **sinceId** | **String**| Internal parameter. Use HTTP &#x60;Link&#x60; header for pagination. | [optional] |
| **limit** | **Integer**| Maximum number of results to return. Defaults to 40. | [optional] [default to 40] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header, or instance is in whitelist mode and your token is not authorized with a user |  -  |
| **404** | Account is deleted or does not exist |  -  |
| **410** | Account is suspended |  -  |

<a id="apiV1AccountsIdGet"></a>
# **apiV1AccountsIdGet**
> Account apiV1AccountsIdGet(id)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Account result = apiInstance.apiV1AccountsIdGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdGet");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account record will be returned. Note that &#x60;acct&#x60; of local users does not include the domain name. |  -  |
| **401** | If the instance is in whitelist mode and the Authorization header is missing or invalid |  -  |
| **404** | Account does not exist |  -  |
| **410** | Account is suspended |  -  |

<a id="apiV1AccountsIdIdentityProofsGet"></a>
# **apiV1AccountsIdIdentityProofsGet**
> List&lt;IdentityProof&gt; apiV1AccountsIdIdentityProofsGet(id)



Array of IdentityProof

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      List<IdentityProof> result = apiInstance.apiV1AccountsIdIdentityProofsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdIdentityProofsGet");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**List&lt;IdentityProof&gt;**](IdentityProof.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Account is deleted or does not exist |  -  |
| **410** | Account with given id is suspended |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1AccountsIdListsGet"></a>
# **apiV1AccountsIdListsGet**
> List&lt;ModelList&gt; apiV1AccountsIdListsGet(id)



User lists that you have added this account to.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      List<ModelList> result = apiInstance.apiV1AccountsIdListsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdListsGet");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**List&lt;ModelList&gt;**](ModelList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Invalid or missing Authorization header, or instance is in whitelist mode and your token is not authorized with a user |  -  |
| **404** | Account is deleted or does not exist |  -  |
| **410** | Account is suspended |  -  |

<a id="apiV1AccountsIdMutePost"></a>
# **apiV1AccountsIdMutePost**
> Relationship apiV1AccountsIdMutePost(id, apiV1AccountsIdMutePostRequest)



Mute the given account. Clients should filter statuses and notifications from this account, if received (e.g. due to a boost in the Home timeline).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    ApiV1AccountsIdMutePostRequest apiV1AccountsIdMutePostRequest = new ApiV1AccountsIdMutePostRequest(); // ApiV1AccountsIdMutePostRequest | 
    try {
      Relationship result = apiInstance.apiV1AccountsIdMutePost(id, apiV1AccountsIdMutePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdMutePost");
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
| **id** | **String**| The id of the account in the database | |
| **apiV1AccountsIdMutePostRequest** | [**ApiV1AccountsIdMutePostRequest**](ApiV1AccountsIdMutePostRequest.md)|  | [optional] |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully muted, or account was already muted. Note that you can call this API method again with notifications&#x3D;false to update the relationship so that only statuses are muted. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1AccountsIdNotePost"></a>
# **apiV1AccountsIdNotePost**
> Relationship apiV1AccountsIdNotePost(id, apiV1AccountsIdNotePostRequest)



Sets a private note on a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    ApiV1AccountsIdNotePostRequest apiV1AccountsIdNotePostRequest = new ApiV1AccountsIdNotePostRequest(); // ApiV1AccountsIdNotePostRequest | 
    try {
      Relationship result = apiInstance.apiV1AccountsIdNotePost(id, apiV1AccountsIdNotePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdNotePost");
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
| **id** | **String**| The id of the account in the database | |
| **apiV1AccountsIdNotePostRequest** | [**ApiV1AccountsIdNotePostRequest**](ApiV1AccountsIdNotePostRequest.md)|  | [optional] |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unmuted, or account was already unmuted. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1AccountsIdPinPost"></a>
# **apiV1AccountsIdPinPost**
> Relationship apiV1AccountsIdPinPost(id)



Add the given account to the user&#39;s featured profiles. (Featured profiles are currently shown on the user&#39;s own public profile.)

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1AccountsIdPinPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdPinPost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unmuted, or account was already unmuted. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **403** | Token is not authorized with a valid user or is missing a required scope |  -  |
| **422** | You are not following this account |  -  |
| **500** | Account already endorsed |  -  |

<a id="apiV1AccountsIdStatusesGet"></a>
# **apiV1AccountsIdStatusesGet**
> List&lt;Status&gt; apiV1AccountsIdStatusesGet(id)



Statuses posted to the given account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      List<Status> result = apiInstance.apiV1AccountsIdStatusesGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdStatusesGet");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**List&lt;Status&gt;**](Status.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Statuses posted to the given account. Public (for public statuses only), or user token + read:statuses (for private statuses the user is authorized to see) |  -  |
| **401** | Instance is in whitelist mode or running a version of Mastodon older than 2.7.0, and the Authorization header is invalid or missing |  -  |
| **404** | Account is deleted or does not exist |  -  |
| **410** | Account is suspended |  -  |

<a id="apiV1AccountsIdUnblockPost"></a>
# **apiV1AccountsIdUnblockPost**
> Relationship apiV1AccountsIdUnblockPost(id)



Block the given account. Clients should filter statuses from this account if received (e.g. due to a boost in the Home timeline).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1AccountsIdUnblockPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdUnblockPost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unblocked, or account was already not blocked |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1AccountsIdUnfollowPost"></a>
# **apiV1AccountsIdUnfollowPost**
> Relationship apiV1AccountsIdUnfollowPost(id)



Unfollow the given account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1AccountsIdUnfollowPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdUnfollowPost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unfollowed, or account was already not followed |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1AccountsIdUnmutePost"></a>
# **apiV1AccountsIdUnmutePost**
> Relationship apiV1AccountsIdUnmutePost(id)



Unmute the given account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1AccountsIdUnmutePost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdUnmutePost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unmuted, or account was already unmuted. |  -  |
| **401** | Invalid or missing Authorization header |  -  |

<a id="apiV1AccountsIdUnpinPost"></a>
# **apiV1AccountsIdUnpinPost**
> Relationship apiV1AccountsIdUnpinPost(id)



Remove the given account from the user&#39;s featured profiles.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String id = "id_example"; // String | The id of the account in the database
    try {
      Relationship result = apiInstance.apiV1AccountsIdUnpinPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsIdUnpinPost");
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
| **id** | **String**| The id of the account in the database | |

### Return type

[**Relationship**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successfully unmuted, or account was already unmuted. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1AccountsPost_0"></a>
# **apiV1AccountsPost_0**
> apiV1AccountsPost_0(apiV1AccountsPostRequest)



Creates a user and account records. Returns an account access token for the app that initiated the request. The app should save this token for later, and should wait for the user to confirm their account by clicking a link in their email inbox.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    ApiV1AccountsPostRequest apiV1AccountsPostRequest = new ApiV1AccountsPostRequest(); // ApiV1AccountsPostRequest | 
    try {
      apiInstance.apiV1AccountsPost_0(apiV1AccountsPostRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsPost_0");
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
| **apiV1AccountsPostRequest** | [**ApiV1AccountsPostRequest**](ApiV1AccountsPostRequest.md)|  | [optional] |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **401** | Unauthorized |  -  |

<a id="apiV1AccountsRelationshipsGet"></a>
# **apiV1AccountsRelationshipsGet**
> List&lt;Relationship&gt; apiV1AccountsRelationshipsGet(id)



Sets a private note on a user.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    List<String> id = Arrays.asList(); // List<String> | Array of account IDs to check
    try {
      List<Relationship> result = apiInstance.apiV1AccountsRelationshipsGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsRelationshipsGet");
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
| **id** | [**List&lt;String&gt;**](String.md)| Array of account IDs to check | |

### Return type

[**List&lt;Relationship&gt;**](Relationship.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success. |  -  |
| **401** | Invalid or missing Authorization header |  -  |
| **422** | Unprocessable Entity |  -  |

<a id="apiV1AccountsSearchGet"></a>
# **apiV1AccountsSearchGet**
> List&lt;Account&gt; apiV1AccountsSearchGet(q, limit, resolve, following)



Search for matching accounts by username or display name.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    String q = "q_example"; // String | What to search for
    Integer limit = 40; // Integer | Maximum number of results. Defaults to 40.
    String resolve = "resolve_example"; // String | Attempt WebFinger lookup. Defaults to false. Use this when `q` is an exact address.
    Boolean following = true; // Boolean | Only who the user is following. Defaults to false.
    try {
      List<Account> result = apiInstance.apiV1AccountsSearchGet(q, limit, resolve, following);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsSearchGet");
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
| **q** | **String**| What to search for | |
| **limit** | **Integer**| Maximum number of results. Defaults to 40. | [optional] [default to 40] |
| **resolve** | **String**| Attempt WebFinger lookup. Defaults to false. Use this when &#x60;q&#x60; is an exact address. | [optional] |
| **following** | **Boolean**| Only who the user is following. Defaults to false. | [optional] |

### Return type

[**List&lt;Account&gt;**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Accounts matching &#x60;q&#x60; in username or display name |  -  |
| **503** | resolve&#x3D;true, but the domain part of the user@domain address is not a currently live website |  -  |

<a id="apiV1AccountsUpdateCredentialsPatch"></a>
# **apiV1AccountsUpdateCredentialsPatch**
> Account apiV1AccountsUpdateCredentialsPatch(apiV1AccountsUpdateCredentialsPatchRequest)



Update the user&#39;s display and preferences.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    ApiV1AccountsUpdateCredentialsPatchRequest apiV1AccountsUpdateCredentialsPatchRequest = new ApiV1AccountsUpdateCredentialsPatchRequest(); // ApiV1AccountsUpdateCredentialsPatchRequest | 
    try {
      Account result = apiInstance.apiV1AccountsUpdateCredentialsPatch(apiV1AccountsUpdateCredentialsPatchRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsUpdateCredentialsPatch");
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
| **apiV1AccountsUpdateCredentialsPatchRequest** | [**ApiV1AccountsUpdateCredentialsPatchRequest**](ApiV1AccountsUpdateCredentialsPatchRequest.md)|  | [optional] |

### Return type

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | You should use &#x60;accounts/verify_credentials&#x60; to first obtain plaintext representations from within the &#x60;source&#x60; parameter, then allow the user to edit these plaintext representations before submitting them through this API. The server will generate the corresponding HTML. |  -  |
| **401** | Unauthorized |  -  |

<a id="apiV1AccountsVerifyCredentialsGet"></a>
# **apiV1AccountsVerifyCredentialsGet**
> Account apiV1AccountsVerifyCredentialsGet()



Test to make sure that the user token works.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://mastodon.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    AccountsApi apiInstance = new AccountsApi(defaultClient);
    try {
      Account result = apiInstance.apiV1AccountsVerifyCredentialsGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountsApi#apiV1AccountsVerifyCredentialsGet");
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

[**Account**](Account.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Note the extra &#x60;source&#x60; property, which is not visible on accounts other than your own. Also note that plain-text is used within &#x60;source&#x60; and HTML is used for their corresponding properties such as &#x60;note&#x60; and &#x60;fields&#x60;. |  -  |
| **401** | Your credential verification will fail if the token is invalid or incorrect. |  -  |
| **403** | Your user account is currently disabled, missing a confirmed email address, or pending approval. |  -  |

