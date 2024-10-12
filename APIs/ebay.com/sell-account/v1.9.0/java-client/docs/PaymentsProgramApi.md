# PaymentsProgramApi

All URIs are relative to *https://api.ebay.com/sell/account/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPaymentsProgram**](PaymentsProgramApi.md#getPaymentsProgram) | **GET** /payments_program/{marketplace_id}/{payments_program_type} |  |


<a id="getPaymentsProgram"></a>
# **getPaymentsProgram**
> PaymentsProgramResponse getPaymentsProgram(marketplaceId, paymentsProgramType)



&lt;span class&#x3D;\&quot;tablenote\&quot;&gt;&lt;b&gt;Note:&lt;/b&gt; This method is no longer applicable, as all seller accounts globally have been enabled for the new eBay payment and checkout flow.&lt;/span&gt;&lt;br/&gt;&lt;br/&gt;This method returns whether or not the user is opted-in to the specified payments program. Sellers opt-in to payments programs by marketplace and you use the &lt;b&gt;marketplace_id&lt;/b&gt; path parameter to specify the marketplace of the status flag you want returned.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentsProgramApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ebay.com/sell/account/v1");
    
    // Configure OAuth2 access token for authorization: api_auth
    OAuth api_auth = (OAuth) defaultClient.getAuthentication("api_auth");
    api_auth.setAccessToken("YOUR ACCESS TOKEN");

    PaymentsProgramApi apiInstance = new PaymentsProgramApi(defaultClient);
    String marketplaceId = "marketplaceId_example"; // String | This path parameter specifies the eBay marketplace of the payments program for which you want to retrieve the seller's status.
    String paymentsProgramType = "paymentsProgramType_example"; // String | This path parameter specifies the payments program whose status is returned by the call.
    try {
      PaymentsProgramResponse result = apiInstance.getPaymentsProgram(marketplaceId, paymentsProgramType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentsProgramApi#getPaymentsProgram");
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
| **marketplaceId** | **String**| This path parameter specifies the eBay marketplace of the payments program for which you want to retrieve the seller&#39;s status. | |
| **paymentsProgramType** | **String**| This path parameter specifies the payments program whose status is returned by the call. | |

### Return type

[**PaymentsProgramResponse**](PaymentsProgramResponse.md)

### Authorization

[api_auth](../README.md#api_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |
| **404** | Not Found |  -  |
| **500** | Internal Server Error |  -  |

