# Class5AdminApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addUser**](Class5AdminApi.md#addUser) | **POST** /admin/addUser |  |
| [**changePassword**](Class5AdminApi.md#changePassword) | **POST** /admin/changePassword |  |


<a id="addUser"></a>
# **addUser**
> addUser(authorization, body)



Add new user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class5AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class5AdminApi apiInstance = new Class5AdminApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    NewUser body = new NewUser(); // NewUser | Details of a new user including first name, last name, desired username and a password
    try {
      apiInstance.addUser(authorization, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class5AdminApi#addUser");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **body** | [**NewUser**](NewUser.md)| Details of a new user including first name, last name, desired username and a password | |

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
| **200** | Successful operation |  -  |
| **400** | Unauthorized request |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Error creating user |  -  |

<a id="changePassword"></a>
# **changePassword**
> changePassword(authorization, body)



Change user password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class5AdminApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    Class5AdminApi apiInstance = new Class5AdminApi(defaultClient);
    String authorization = "authorization_example"; // String | Authorization token (provided upon successful login)
    ChangePassword body = new ChangePassword(); // ChangePassword | Information about the user password to be changed including id and new password
    try {
      apiInstance.changePassword(authorization, body);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class5AdminApi#changePassword");
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
| **authorization** | **String**| Authorization token (provided upon successful login) | |
| **body** | [**ChangePassword**](ChangePassword.md)| Information about the user password to be changed including id and new password | |

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
| **200** | Successful operation |  -  |
| **400** | Unauthorized request |  -  |
| **401** | Unauthorized request |  -  |
| **500** | Error in changing the username password |  -  |

