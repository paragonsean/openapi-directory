# RegistrationApi

All URIs are relative to *http://whatsapp.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**registerAccount**](RegistrationApi.md#registerAccount) | **POST** /account/verify | Register-Account |
| [**requestCode**](RegistrationApi.md#requestCode) | **POST** /account | Request-Code |


<a id="registerAccount"></a>
# **registerAccount**
> registerAccount(registerAccountRequestBody)

Register-Account

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RegistrationApi apiInstance = new RegistrationApi(defaultClient);
    RegisterAccountRequestBody registerAccountRequestBody = new RegisterAccountRequestBody(); // RegisterAccountRequestBody | 
    try {
      apiInstance.registerAccount(registerAccountRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationApi#registerAccount");
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
| **registerAccountRequestBody** | [**RegisterAccountRequestBody**](RegisterAccountRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="requestCode"></a>
# **requestCode**
> requestCode(requestCodeRequestBody)

Request-Code

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
    defaultClient.setBasePath("http://whatsapp.local");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    RegistrationApi apiInstance = new RegistrationApi(defaultClient);
    RequestCodeRequestBody requestCodeRequestBody = new RequestCodeRequestBody(); // RequestCodeRequestBody | 
    try {
      apiInstance.requestCode(requestCodeRequestBody);
    } catch (ApiException e) {
      System.err.println("Exception when calling RegistrationApi#requestCode");
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
| **requestCodeRequestBody** | [**RequestCodeRequestBody**](RequestCodeRequestBody.md)|  | |

### Return type

null (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Created: the account already exists. You are already registered, so you do not need to do anything else. |  -  |
| **202** | Created: the account does not exist. Depending on the method selected in the request, check your SMS or voice number for the registration code. |  -  |

