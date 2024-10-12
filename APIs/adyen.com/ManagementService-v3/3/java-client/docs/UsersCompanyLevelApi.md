# UsersCompanyLevelApi

All URIs are relative to *https://management-test.adyen.com/v3*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getCompaniesCompanyIdUsers**](UsersCompanyLevelApi.md#getCompaniesCompanyIdUsers) | **GET** /companies/{companyId}/users | Get a list of users |
| [**getCompaniesCompanyIdUsersUserId**](UsersCompanyLevelApi.md#getCompaniesCompanyIdUsersUserId) | **GET** /companies/{companyId}/users/{userId} | Get user details |
| [**patchCompaniesCompanyIdUsersUserId**](UsersCompanyLevelApi.md#patchCompaniesCompanyIdUsersUserId) | **PATCH** /companies/{companyId}/users/{userId} | Update user details |
| [**postCompaniesCompanyIdUsers**](UsersCompanyLevelApi.md#postCompaniesCompanyIdUsers) | **POST** /companies/{companyId}/users | Create a new user |


<a id="getCompaniesCompanyIdUsers"></a>
# **getCompaniesCompanyIdUsers**
> ListCompanyUsersResponse getCompaniesCompanyIdUsers(companyId, pageNumber, pageSize, username)

Get a list of users

Returns the list of users for the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersCompanyLevelApi;

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

    UsersCompanyLevelApi apiInstance = new UsersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    Integer pageNumber = 56; // Integer | The number of the page to return.
    Integer pageSize = 56; // Integer | The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page.
    String username = "username_example"; // String | The partial or complete username to select all users that match.
    try {
      ListCompanyUsersResponse result = apiInstance.getCompaniesCompanyIdUsers(companyId, pageNumber, pageSize, username);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersCompanyLevelApi#getCompaniesCompanyIdUsers");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **pageNumber** | **Integer**| The number of the page to return. | [optional] |
| **pageSize** | **Integer**| The number of items to have on a page. Maximum value is **100**. The default is **10** items on a page. | [optional] |
| **username** | **String**| The partial or complete username to select all users that match. | [optional] |

### Return type

[**ListCompanyUsersResponse**](ListCompanyUsersResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="getCompaniesCompanyIdUsersUserId"></a>
# **getCompaniesCompanyIdUsersUserId**
> CompanyUser getCompaniesCompanyIdUsersUserId(companyId, userId)

Get user details

Returns user details for the &#x60;userId&#x60; and the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersCompanyLevelApi;

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

    UsersCompanyLevelApi apiInstance = new UsersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String userId = "userId_example"; // String | The unique identifier of the user.
    try {
      CompanyUser result = apiInstance.getCompaniesCompanyIdUsersUserId(companyId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersCompanyLevelApi#getCompaniesCompanyIdUsersUserId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **userId** | **String**| The unique identifier of the user. | |

### Return type

[**CompanyUser**](CompanyUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="patchCompaniesCompanyIdUsersUserId"></a>
# **patchCompaniesCompanyIdUsersUserId**
> CompanyUser patchCompaniesCompanyIdUsersUserId(companyId, userId, updateCompanyUserRequest)

Update user details

Updates user details for the &#x60;userId&#x60; and the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersCompanyLevelApi;

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

    UsersCompanyLevelApi apiInstance = new UsersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    String userId = "userId_example"; // String | The unique identifier of the user.
    UpdateCompanyUserRequest updateCompanyUserRequest = new UpdateCompanyUserRequest(); // UpdateCompanyUserRequest | 
    try {
      CompanyUser result = apiInstance.patchCompaniesCompanyIdUsersUserId(companyId, userId, updateCompanyUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersCompanyLevelApi#patchCompaniesCompanyIdUsersUserId");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **userId** | **String**| The unique identifier of the user. | |
| **updateCompanyUserRequest** | [**UpdateCompanyUserRequest**](UpdateCompanyUserRequest.md)|  | [optional] |

### Return type

[**CompanyUser**](CompanyUser.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

<a id="postCompaniesCompanyIdUsers"></a>
# **postCompaniesCompanyIdUsers**
> CreateCompanyUserResponse postCompaniesCompanyIdUsers(companyId, createCompanyUserRequest)

Create a new user

Creates the user for the &#x60;companyId&#x60; identified in the path.  To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions): * Management API—Users read and write 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UsersCompanyLevelApi;

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

    UsersCompanyLevelApi apiInstance = new UsersCompanyLevelApi(defaultClient);
    String companyId = "companyId_example"; // String | The unique identifier of the company account.
    CreateCompanyUserRequest createCompanyUserRequest = new CreateCompanyUserRequest(); // CreateCompanyUserRequest | 
    try {
      CreateCompanyUserResponse result = apiInstance.postCompaniesCompanyIdUsers(companyId, createCompanyUserRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling UsersCompanyLevelApi#postCompaniesCompanyIdUsers");
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
| **companyId** | **String**| The unique identifier of the company account. | |
| **createCompanyUserRequest** | [**CreateCompanyUserRequest**](CreateCompanyUserRequest.md)|  | [optional] |

### Return type

[**CreateCompanyUserResponse**](CreateCompanyUserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth), [ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |
| **400** | Bad Request - a problem reading or understanding the request. |  -  |
| **401** | Unauthorized - authentication required. |  -  |
| **403** | Forbidden - insufficient permissions to process the request. |  -  |
| **422** | Unprocessable Entity - a request validation error. |  -  |
| **500** | Internal Server Error - the server could not process the request. |  -  |

