# Class3ImproveYourResultsApi

All URIs are relative to *https://api.taggun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postApiAccountV1Feedback**](Class3ImproveYourResultsApi.md#postApiAccountV1Feedback) | **POST** /api/account/v1/feedback | Add manually verified receipt data to a given receipt for feedback and training purposes |
| [**postApiAccountV1MerchantnameAdd**](Class3ImproveYourResultsApi.md#postApiAccountV1MerchantnameAdd) | **POST** /api/account/v1/merchantname/add | Add a keyword to your account&#39;s model to predict merchant name. Changes in your account&#39;s model are updated daily. |


<a id="postApiAccountV1Feedback"></a>
# **postApiAccountV1Feedback**
> Result postApiAccountV1Feedback(apikey, body)

Add manually verified receipt data to a given receipt for feedback and training purposes

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3ImproveYourResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class3ImproveYourResultsApi apiInstance = new Class3ImproveYourResultsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    ReceiptFeedbackAddPayload body = new ReceiptFeedbackAddPayload(); // ReceiptFeedbackAddPayload | 
    try {
      Result result = apiInstance.postApiAccountV1Feedback(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3ImproveYourResultsApi#postApiAccountV1Feedback");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**ReceiptFeedbackAddPayload**](ReceiptFeedbackAddPayload.md)|  | [optional] |

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiAccountV1MerchantnameAdd"></a>
# **postApiAccountV1MerchantnameAdd**
> Result postApiAccountV1MerchantnameAdd(apikey, body)

Add a keyword to your account&#39;s model to predict merchant name. Changes in your account&#39;s model are updated daily.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class3ImproveYourResultsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class3ImproveYourResultsApi apiInstance = new Class3ImproveYourResultsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    MerchantNameAddPayload body = new MerchantNameAddPayload(); // MerchantNameAddPayload | 
    try {
      Result result = apiInstance.postApiAccountV1MerchantnameAdd(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class3ImproveYourResultsApi#postApiAccountV1MerchantnameAdd");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**MerchantNameAddPayload**](MerchantNameAddPayload.md)|  | [optional] |

### Return type

[**Result**](Result.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

