# PasswordApi

All URIs are relative to *https://demo.uat.naviplancentral.com/plan*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**passwordHasUserSetPassword**](PasswordApi.md#passwordHasUserSetPassword) | **POST** /api/Password/HasUserSetPassword | Determines if the currently logged in user has set their own password |
| [**passwordPasswordRequirements**](PasswordApi.md#passwordPasswordRequirements) | **GET** /api/Password/PasswordRequirements | Gets the password complexity requirements |
| [**passwordResetByModel**](PasswordApi.md#passwordResetByModel) | **POST** /api/Password/Reset | Resets the password for the supplied user name |
| [**passwordSetByModel**](PasswordApi.md#passwordSetByModel) | **POST** /api/Password/Set | Sets the password for the currently logged in user |


<a id="passwordHasUserSetPassword"></a>
# **passwordHasUserSetPassword**
> passwordHasUserSetPassword()

Determines if the currently logged in user has set their own password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PasswordApi apiInstance = new PasswordApi(defaultClient);
    try {
      apiInstance.passwordHasUserSetPassword();
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordApi#passwordHasUserSetPassword");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |

<a id="passwordPasswordRequirements"></a>
# **passwordPasswordRequirements**
> passwordPasswordRequirements()

Gets the password complexity requirements

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PasswordApi apiInstance = new PasswordApi(defaultClient);
    try {
      apiInstance.passwordPasswordRequirements();
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordApi#passwordPasswordRequirements");
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

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **500** | InternalServerError |  -  |

<a id="passwordResetByModel"></a>
# **passwordResetByModel**
> passwordResetByModel(model)

Resets the password for the supplied user name

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PasswordApi apiInstance = new PasswordApi(defaultClient);
    ResetPasswordModel model = new ResetPasswordModel(); // ResetPasswordModel | 
    try {
      apiInstance.passwordResetByModel(model);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordApi#passwordResetByModel");
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
| **model** | [**ResetPasswordModel**](ResetPasswordModel.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |

<a id="passwordSetByModel"></a>
# **passwordSetByModel**
> passwordSetByModel(model)

Sets the password for the currently logged in user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PasswordApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://demo.uat.naviplancentral.com/plan");

    PasswordApi apiInstance = new PasswordApi(defaultClient);
    SetPasswordModel model = new SetPasswordModel(); // SetPasswordModel | 
    try {
      apiInstance.passwordSetByModel(model);
    } catch (ApiException e) {
      System.err.println("Exception when calling PasswordApi#passwordSetByModel");
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
| **model** | [**SetPasswordModel**](SetPasswordModel.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | BadRequest |  -  |
| **401** | Unauthorized |  -  |

