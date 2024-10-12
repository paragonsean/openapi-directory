# VerificationsApi

All URIs are relative to *https://api.mailscript.com/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addVerification**](VerificationsApi.md#addVerification) | **POST** /verifications | Start verification process for external email address or sms number |
| [**getAllVerifications**](VerificationsApi.md#getAllVerifications) | **GET** /verifications | Get all verificats for the user |
| [**verify**](VerificationsApi.md#verify) | **POST** /verifications/{verification}/verify | Verify an email address or sms number with a code |


<a id="addVerification"></a>
# **addVerification**
> AddVerificationResponse addVerification(addVerificationRequest)

Start verification process for external email address or sms number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VerificationsApi apiInstance = new VerificationsApi(defaultClient);
    AddVerificationRequest addVerificationRequest = new AddVerificationRequest(); // AddVerificationRequest | Key body
    try {
      AddVerificationResponse result = apiInstance.addVerification(addVerificationRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationsApi#addVerification");
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
| **addVerificationRequest** | [**AddVerificationRequest**](AddVerificationRequest.md)| Key body | |

### Return type

[**AddVerificationResponse**](AddVerificationResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** | Successful operation |  -  |
| **400** | Failure |  -  |
| **403** | Bad credentials |  -  |

<a id="getAllVerifications"></a>
# **getAllVerifications**
> GetAllVerificationsResponse getAllVerifications()

Get all verificats for the user

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VerificationsApi apiInstance = new VerificationsApi(defaultClient);
    try {
      GetAllVerificationsResponse result = apiInstance.getAllVerifications();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationsApi#getAllVerifications");
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

[**GetAllVerificationsResponse**](GetAllVerificationsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful operation |  -  |
| **403** | Bad credentials |  -  |

<a id="verify"></a>
# **verify**
> verify(verification, verifyRequest)

Verify an email address or sms number with a code

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mailscript.com/v2");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    VerificationsApi apiInstance = new VerificationsApi(defaultClient);
    String verification = "verification_example"; // String | ID of the verification entry
    VerifyRequest verifyRequest = new VerifyRequest(); // VerifyRequest | Verify action body
    try {
      apiInstance.verify(verification, verifyRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationsApi#verify");
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
| **verification** | **String**| ID of the verification entry | |
| **verifyRequest** | [**VerifyRequest**](VerifyRequest.md)| Verify action body | |

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
| **200** | Successful operation |  -  |
| **400** | Failure |  -  |
| **403** | Not authorized or bad code |  -  |
| **404** | Not found |  -  |

