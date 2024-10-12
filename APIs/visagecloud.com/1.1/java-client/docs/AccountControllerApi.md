# AccountControllerApi

All URIs are relative to *https://visagecloud.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**changePasswordUsingPOST**](AccountControllerApi.md#changePasswordUsingPOST) | **POST** /rest/v1.1/account/changePassword | Change password for an account using old password |
| [**getAccountByAccessKeyUsingGET**](AccountControllerApi.md#getAccountByAccessKeyUsingGET) | **GET** /rest/v1.1/account/account | Get account information by accessKey and secretKey |
| [**getBillingPerAccountUsingGET**](AccountControllerApi.md#getBillingPerAccountUsingGET) | **GET** /rest/v1.1/account/billing | Get billing information by accessKey and secretKey |
| [**loginWithEmailUsingPOST**](AccountControllerApi.md#loginWithEmailUsingPOST) | **POST** /rest/v1.1/account/login | Get account information including accessKey and secretKey by email and password |


<a id="changePasswordUsingPOST"></a>
# **changePasswordUsingPOST**
> RestResponse changePasswordUsingPOST(email, oldPassword, newPassword)

Change password for an account using old password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AccountControllerApi apiInstance = new AccountControllerApi(defaultClient);
    String email = "email_example"; // String | email
    String oldPassword = "oldPassword_example"; // String | oldPassword
    String newPassword = "newPassword_example"; // String | newPassword
    try {
      RestResponse result = apiInstance.changePasswordUsingPOST(email, oldPassword, newPassword);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountControllerApi#changePasswordUsingPOST");
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
| **email** | **String**| email | |
| **oldPassword** | **String**| oldPassword | |
| **newPassword** | **String**| newPassword | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getAccountByAccessKeyUsingGET"></a>
# **getAccountByAccessKeyUsingGET**
> RestResponse getAccountByAccessKeyUsingGET(accessKey, secretKey)

Get account information by accessKey and secretKey

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AccountControllerApi apiInstance = new AccountControllerApi(defaultClient);
    String accessKey = "accessKey_example"; // String | accessKey
    String secretKey = "secretKey_example"; // String | secretKey
    try {
      RestResponse result = apiInstance.getAccountByAccessKeyUsingGET(accessKey, secretKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountControllerApi#getAccountByAccessKeyUsingGET");
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
| **accessKey** | **String**| accessKey | |
| **secretKey** | **String**| secretKey | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="getBillingPerAccountUsingGET"></a>
# **getBillingPerAccountUsingGET**
> RestResponse getBillingPerAccountUsingGET(accessKey, secretKey, startDateTime, endDateTime, dateTemplate)

Get billing information by accessKey and secretKey

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AccountControllerApi apiInstance = new AccountControllerApi(defaultClient);
    String accessKey = "accessKey_example"; // String | accessKey
    String secretKey = "secretKey_example"; // String | secretKey
    OffsetDateTime startDateTime = OffsetDateTime.now(); // OffsetDateTime | startDateTime
    OffsetDateTime endDateTime = OffsetDateTime.now(); // OffsetDateTime | endDateTime
    String dateTemplate = "dateTemplate_example"; // String | dateTemplate
    try {
      RestResponse result = apiInstance.getBillingPerAccountUsingGET(accessKey, secretKey, startDateTime, endDateTime, dateTemplate);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountControllerApi#getBillingPerAccountUsingGET");
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
| **accessKey** | **String**| accessKey | |
| **secretKey** | **String**| secretKey | |
| **startDateTime** | **OffsetDateTime**| startDateTime | [optional] |
| **endDateTime** | **OffsetDateTime**| endDateTime | [optional] |
| **dateTemplate** | **String**| dateTemplate | [optional] |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

<a id="loginWithEmailUsingPOST"></a>
# **loginWithEmailUsingPOST**
> RestResponse loginWithEmailUsingPOST(email, password)

Get account information including accessKey and secretKey by email and password

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AccountControllerApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://visagecloud.com");

    AccountControllerApi apiInstance = new AccountControllerApi(defaultClient);
    String email = "email_example"; // String | email
    String password = "password_example"; // String | password
    try {
      RestResponse result = apiInstance.loginWithEmailUsingPOST(email, password);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AccountControllerApi#loginWithEmailUsingPOST");
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
| **email** | **String**| email | |
| **password** | **String**| password | |

### Return type

[**RestResponse**](RestResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **201** | Created |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

