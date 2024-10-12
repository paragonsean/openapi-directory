# VerificationApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createSMSToken**](VerificationApi.md#createSMSToken) | **POST** /api/v1/verification/sms | Create SMS token |
| [**verifySMSToken**](VerificationApi.md#verifySMSToken) | **GET** /api/v1/verification/sms/{token} | Verify SMS token |


<a id="createSMSToken"></a>
# **createSMSToken**
> CreateSMSTokenOut createSMSToken(input)

Create SMS token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    CreateSMSTokenIn input = new CreateSMSTokenIn(); // CreateSMSTokenIn | Input
    try {
      CreateSMSTokenOut result = apiInstance.createSMSToken(input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#createSMSToken");
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
| **input** | [**CreateSMSTokenIn**](CreateSMSTokenIn.md)| Input | |

### Return type

[**CreateSMSTokenOut**](CreateSMSTokenOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

<a id="verifySMSToken"></a>
# **verifySMSToken**
> VerifySMSTokenOut verifySMSToken(token)

Verify SMS token

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.VerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    VerificationApi apiInstance = new VerificationApi(defaultClient);
    String token = "token_example"; // String | Provided token.
    try {
      VerifySMSTokenOut result = apiInstance.verifySMSToken(token);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling VerificationApi#verifySMSToken");
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
| **token** | **String**| Provided token. | |

### Return type

[**VerifySMSTokenOut**](VerifySMSTokenOut.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Validation failed, see JSON body response for details. |  -  |
| **401** | Incorrect token |  -  |

