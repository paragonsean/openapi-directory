# RegistrationApi

All URIs are relative to *https://api.nextauth.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getQrEnrol**](RegistrationApi.md#getQrEnrol) | **GET** /servers/{serverid}/sessions/qr/enrol | Generate data for an enrol qr code |
| [**getServerVash**](RegistrationApi.md#getServerVash) | **GET** /servers/{serverid}/vash | Visual hash of this server |
| [**registerUser_0**](RegistrationApi.md#registerUser_0) | **POST** /servers/{serverid}/sessions/registeruser | Register a userid for the currently logged in account. |
| [**updateAccountUser_0**](RegistrationApi.md#updateAccountUser_0) | **PUT** /servers/{serverid}/accounts/{accountid}/user | Update user of the given account. |


<a id="getQrEnrol"></a>
# **getQrEnrol**
> File getQrEnrol(serverid, xNonce, name, userid, img, s)

Generate data for an enrol qr code

Returns the data for an enrol qr code. Required permission: &#39;sessions&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    RegistrationApi apiInstance = new RegistrationApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    String name = "name_example"; // String | Name to forward to the nextAuth app for this account
    String userid = "userid_example"; // String | User name to register this user under
    String img = "img_example"; // String | 'png' for a PNG image, not set for raw data in the qr code
    Integer s = 56; // Integer | size in pixels of the qr code, defaults to 500
    try {
      File result = apiInstance.getQrEnrol(serverid, xNonce, name, userid, img, s);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationApi#getQrEnrol");
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
| **serverid** | **String**| Base64 encoded server id | |
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **name** | **String**| Name to forward to the nextAuth app for this account | |
| **userid** | **String**| User name to register this user under | [optional] |
| **img** | **String**| &#39;png&#39; for a PNG image, not set for raw data in the qr code | [optional] |
| **s** | **Integer**| size in pixels of the qr code, defaults to 500 | [optional] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw byte array containing the enrol qr code data (either raw or as a PNG image). |  -  |

<a id="getServerVash"></a>
# **getServerVash**
> File getServerVash(serverid)

Visual hash of this server

Returns a PNG of the visual hash corresponding to this server. This visual hash is used during the registration process (optional), for the user to verify that (s)he is registering with the right server in the nextAuth app. For single-server nextAuth-enabled apps (white label or mobile SDK), the public key of the server is typically pinned within the app and hence this visual hash is not displayed to the user. Required permission: &#39;sessions&#39; or &#39;servers&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    RegistrationApi apiInstance = new RegistrationApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    try {
      File result = apiInstance.getServerVash(serverid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationApi#getServerVash");
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
| **serverid** | **String**| Base64 encoded server id | |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Raw byte array containing the visual hash of this server as a PNG image. |  -  |
| **404** | Server not found |  -  |

<a id="registerUser_0"></a>
# **registerUser_0**
> registerUser_0(serverid, xNonce, userid)

Register a userid for the currently logged in account.

Register a user for the currently logged in account. You can also directly pass a user name when generating an ENROL qr code. Required permission: &#39;users&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    RegistrationApi apiInstance = new RegistrationApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    String xNonce = "xNonce_example"; // String | Nonce to identify the browser/webserver session
    String userid = "userid_example"; // String | Username to register
    try {
      apiInstance.registerUser_0(serverid, xNonce, userid);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationApi#registerUser_0");
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
| **serverid** | **String**| Base64 encoded server id | |
| **xNonce** | **String**| Nonce to identify the browser/webserver session | |
| **userid** | **String**| Username to register | |

### Return type

null (empty response body)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="updateAccountUser_0"></a>
# **updateAccountUser_0**
> Account updateAccountUser_0(serverid, accountid, userid)

Update user of the given account.

Update the user of the given account. Required permission: &#39;accounts&#39;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nextauth.com");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure API key authorization: role_id
    ApiKeyAuth role_id = (ApiKeyAuth) defaultClient.getAuthentication("role_id");
    role_id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //role_id.setApiKeyPrefix("Token");

    RegistrationApi apiInstance = new RegistrationApi(defaultClient);
    String serverid = "serverid_example"; // String | Base64 encoded server id
    Integer accountid = 56; // Integer | Account id
    String userid = "userid_example"; // String | User name
    try {
      Account result = apiInstance.updateAccountUser_0(serverid, accountid, userid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationApi#updateAccountUser_0");
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
| **serverid** | **String**| Base64 encoded server id | |
| **accountid** | **Integer**| Account id | |
| **userid** | **String**| User name | |

### Return type

[**Account**](Account.md)

### Authorization

[api_key](../README.md#api_key), [role_id](../README.md#role_id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Account after update |  -  |
| **403** | Invalid user name |  -  |
| **404** | Account not found |  -  |

