# DefaultApi

All URIs are relative to *https://api.vonage.com/t/vbc.prod/provisioning*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**userCtrlGetUserByID**](DefaultApi.md#userCtrlGetUserByID) | **GET** /api/accounts/{account_id}/users/{user_id} | Get user data by account ID and user ID |
| [**userCtrlGetUsers**](DefaultApi.md#userCtrlGetUsers) | **GET** /api/accounts/{account_id}/users | Get account users data by account ID |


<a id="userCtrlGetUserByID"></a>
# **userCtrlGetUserByID**
> UserHalResponse userCtrlGetUserByID(accountId, userId)

Get user data by account ID and user ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/provisioning");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "451496"; // String | The Vonage Business Cloud account ID
    BigDecimal userId = new BigDecimal(78); // BigDecimal | The Vonage Business Cloud user ID
    try {
      UserHalResponse result = apiInstance.userCtrlGetUserByID(accountId, userId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userCtrlGetUserByID");
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
| **accountId** | **String**| The Vonage Business Cloud account ID | |
| **userId** | **BigDecimal**| The Vonage Business Cloud user ID | |

### Return type

[**UserHalResponse**](UserHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | User not found |  -  |

<a id="userCtrlGetUsers"></a>
# **userCtrlGetUsers**
> UsersHalResponse userCtrlGetUsers(accountId, pageSize, page, firstName, lastName, loginName, email)

Get account users data by account ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.vonage.com/t/vbc.prod/provisioning");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String accountId = "451496"; // String | The Vonage Business Cloud account ID
    BigDecimal pageSize = new BigDecimal("10"); // BigDecimal | Number of records per page
    BigDecimal page = new BigDecimal("10"); // BigDecimal | Current page number
    String firstName = "John"; // String | Filter by first name
    String lastName = "Smith"; // String | Filter by last name
    String loginName = "jsmith"; // String | Filter by login name
    String email = "john.smith@example.com"; // String | Filter by email address
    try {
      UsersHalResponse result = apiInstance.userCtrlGetUsers(accountId, pageSize, page, firstName, lastName, loginName, email);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#userCtrlGetUsers");
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
| **accountId** | **String**| The Vonage Business Cloud account ID | |
| **pageSize** | **BigDecimal**| Number of records per page | [optional] |
| **page** | **BigDecimal**| Current page number | [optional] |
| **firstName** | **String**| Filter by first name | [optional] |
| **lastName** | **String**| Filter by last name | [optional] |
| **loginName** | **String**| Filter by login name | [optional] |
| **email** | **String**| Filter by email address | [optional] |

### Return type

[**UsersHalResponse**](UsersHalResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid parameters given |  -  |

