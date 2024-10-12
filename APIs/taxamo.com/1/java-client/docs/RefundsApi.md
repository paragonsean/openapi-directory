# RefundsApi

All URIs are relative to *https://api.taxamo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createRefund**](RefundsApi.md#createRefund) | **POST** /api/v1/transactions/{key}/refunds | Create a refund |
| [**listRefunds**](RefundsApi.md#listRefunds) | **GET** /api/v1/transactions/{key}/refunds | Get transaction refunds |


<a id="createRefund"></a>
# **createRefund**
> CreateRefundOut createRefund(key, input)

Create a refund

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    RefundsApi apiInstance = new RefundsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    CreateRefundIn input = new CreateRefundIn(); // CreateRefundIn | Input
    try {
      CreateRefundOut result = apiInstance.createRefund(key, input);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundsApi#createRefund");
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
| **key** | **String**| Transaction key. | |
| **input** | [**CreateRefundIn**](CreateRefundIn.md)| Input | |

### Return type

[**CreateRefundOut**](CreateRefundOut.md)

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

<a id="listRefunds"></a>
# **listRefunds**
> ListRefundsOut listRefunds(key)

Get transaction refunds

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taxamo.com");

    RefundsApi apiInstance = new RefundsApi(defaultClient);
    String key = "key_example"; // String | Transaction key.
    try {
      ListRefundsOut result = apiInstance.listRefunds(key);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundsApi#listRefunds");
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
| **key** | **String**| Transaction key. | |

### Return type

[**ListRefundsOut**](ListRefundsOut.md)

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

