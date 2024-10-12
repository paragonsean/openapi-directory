# UsersMerchantLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getMerchantsMerchantIdUsers**](UsersMerchantLevelApi.md#getMerchantsMerchantIdUsers) | **GET** /merchants/{merchantId}/users | Get a list of users |
| [**getMerchantsMerchantIdUsersUserId**](UsersMerchantLevelApi.md#getMerchantsMerchantIdUsersUserId) | **GET** /merchants/{merchantId}/users/{userId} | Get user details |
| [**patchMerchantsMerchantIdUsersUserId**](UsersMerchantLevelApi.md#patchMerchantsMerchantIdUsersUserId) | **PATCH** /merchants/{merchantId}/users/{userId} | Update a user |
| [**postMerchantsMerchantIdUsers**](UsersMerchantLevelApi.md#postMerchantsMerchantIdUsers) | **POST** /merchants/{merchantId}/users | Create a new user |


<a id="getMerchantsMerchantIdUsers"></a>
# **getMerchantsMerchantIdUsers**
> ListMerchantUsersResponse getMerchantsMerchantIdUsers(merchantId, pageNumber, pageSize, username)

Get a list of users

Returns a list of users associated with the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UsersMerchantLevelApi apiInstance = new UsersMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
    Integer pageNumber = 56; // Integer | The number of the page to fetch.
    Integer pageSize = 56; // Integer | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page.
    String username = "username_example"; // String | The partial or complete username to select all users that match.
    try {
      ListMerchantUsersResponse result = apiInstance.getMerchantsMerchantIdUsers(merchantId, pageNumber, pageSize, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersMerchantLevelApi#getMerchantsMerchantIdUsers");
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
| **merchantId** | **String**| Unique identifier of the merchant. | |
| **pageNumber** | **Integer**| The number of the page to fetch. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. | [optional] |
| **username** | **String**| The partial or complete username to select all users that match. | [optional] |

### Return type

[**ListMerchantUsersResponse**](ListMerchantUsersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getMerchantsMerchantIdUsersUserId"></a>
# **getMerchantsMerchantIdUsersUserId**
> User getMerchantsMerchantIdUsersUserId(merchantId, userId)

Get user details

Returns user details for the &#x60;userId&#x60; and the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UsersMerchantLevelApi apiInstance = new UsersMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
    String userId = "userId_example"; // String | Unique identifier of the user.
    try {
      User result = apiInstance.getMerchantsMerchantIdUsersUserId(merchantId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersMerchantLevelApi#getMerchantsMerchantIdUsersUserId");
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
| **merchantId** | **String**| Unique identifier of the merchant. | |
| **userId** | **String**| Unique identifier of the user. | |

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchMerchantsMerchantIdUsersUserId"></a>
# **patchMerchantsMerchantIdUsersUserId**
> User patchMerchantsMerchantIdUsersUserId(merchantId, userId, updateMerchantUserRequest)

Update a user

Updates user details for the &#x60;userId&#x60; and the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UsersMerchantLevelApi apiInstance = new UsersMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
    String userId = "userId_example"; // String | Unique identifier of the user.
    UpdateMerchantUserRequest updateMerchantUserRequest = new UpdateMerchantUserRequest(); // UpdateMerchantUserRequest | 
    try {
      User result = apiInstance.patchMerchantsMerchantIdUsersUserId(merchantId, userId, updateMerchantUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersMerchantLevelApi#patchMerchantsMerchantIdUsersUserId");
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
| **merchantId** | **String**| Unique identifier of the merchant. | |
| **userId** | **String**| Unique identifier of the user. | |
| **updateMerchantUserRequest** | [**UpdateMerchantUserRequest**](UpdateMerchantUserRequest.md)|  | [optional] |

### Return type

[**User**](User.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postMerchantsMerchantIdUsers"></a>
# **postMerchantsMerchantIdUsers**
> CreateUserResponse postMerchantsMerchantIdUsers(merchantId, createMerchantUserRequest)

Create a new user

Creates a user for the &#x60;merchantId&#x60; specified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersMerchantLevelApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://management-test.adyen.com/v3");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    // Configure API key authorization: ApiKeyAuth
    ApiKeyAuth ApiKeyAuth = (ApiKeyAuth) defaultClient.getAuthentication("ApiKeyAuth");
    ApiKeyAuth.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //ApiKeyAuth.setApiKeyPrefix("Token");

    UsersMerchantLevelApi apiInstance = new UsersMerchantLevelApi(defaultClient);
    String merchantId = "merchantId_example"; // String | Unique identifier of the merchant.
    CreateMerchantUserRequest createMerchantUserRequest = new CreateMerchantUserRequest(); // CreateMerchantUserRequest | 
    try {
      CreateUserResponse result = apiInstance.postMerchantsMerchantIdUsers(merchantId, createMerchantUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersMerchantLevelApi#postMerchantsMerchantIdUsers");
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
| **merchantId** | **String**| Unique identifier of the merchant. | |
| **createMerchantUserRequest** | [**CreateMerchantUserRequest**](CreateMerchantUserRequest.md)|  | [optional] |

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **204** | No Content - the request has been successfully processed, but there is no additional content. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

