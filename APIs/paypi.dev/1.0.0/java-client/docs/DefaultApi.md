# DefaultApi

All URIs are relative to *https://ev.apis.paypi.dev*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkCodePost**](DefaultApi.md#checkCodePost) | **POST** /checkCode | Check verification code |
| [**sendCodePost**](DefaultApi.md#sendCodePost) | **POST** /sendCode | Send verification code |


<a id="checkCodePost"></a>
# **checkCodePost**
> CheckCodePost200Response checkCodePost(checkCodePostRequest)

Check verification code

Checks the user&#39;s emailed code is valid.  If this returns success&#x3D;true, you can safely assume the user you are interacting with is the owner of that email address. 

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
    defaultClient.setBasePath("https://ev.apis.paypi.dev");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    CheckCodePostRequest checkCodePostRequest = new CheckCodePostRequest(); // CheckCodePostRequest | 
    try {
      CheckCodePost200Response result = apiInstance.checkCodePost(checkCodePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#checkCodePost");
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
| **checkCodePostRequest** | [**CheckCodePostRequest**](CheckCodePostRequest.md)|  | |

### Return type

[**CheckCodePost200Response**](CheckCodePost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | If success is true, the user has given the correct code. If not the code is incorrect. \\ Check the message for more information  |  -  |
| **401** | #### Invalid API key  |  -  |
| **403** | #### Tries for this email exceeded.  To prevent abuse and brute forcing, we limit the number of checkCode requests for each email address to 20. \\ This means if more than 20 requests are made you will have to send another code to your user, this will reset the limit.  |  -  |

<a id="sendCodePost"></a>
# **sendCodePost**
> SendCodePost200Response sendCodePost(sendCodePostRequest)

Send verification code

This request send&#39;s a code to the given email address, which should be returned to check it is correct.

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
    defaultClient.setBasePath("https://ev.apis.paypi.dev");
    
    // Configure HTTP bearer authorization: bearerAuth
    HttpBearerAuth bearerAuth = (HttpBearerAuth) defaultClient.getAuthentication("bearerAuth");
    bearerAuth.setBearerToken("BEARER TOKEN");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    SendCodePostRequest sendCodePostRequest = new SendCodePostRequest(); // SendCodePostRequest | 
    try {
      SendCodePost200Response result = apiInstance.sendCodePost(sendCodePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#sendCodePost");
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
| **sendCodePostRequest** | [**SendCodePostRequest**](SendCodePostRequest.md)|  | |

### Return type

[**SendCodePost200Response**](SendCodePost200Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success - Email sent |  -  |
| **400** | Invalid or incorrectly formatted email given |  -  |
| **401** | Invalid API key |  -  |

