# RePowerTransferReversalApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repowerReversalPost2**](RePowerTransferReversalApi.md#repowerReversalPost2) | **POST** /repower/v2/repowerreversal |  |


<a id="repowerReversalPost2"></a>
# **repowerReversalPost2**
> Repowerreversal11Wrapper repowerReversalPost2(repowerReversalRequest)



A Transfer Reversal is a request to reverse a previously submitted Mastercard rePower Transfer, and is only available in extremely limited circumstances.  Reversal Processing : A rePower transaction reversal may be submitted in the event of a documented clerical error. The rePower transaction reversal must be submitted within 15 minutes of the time the original rePower transaction was authorized.  Use this resource to reverse a previously submitted rePower Transfer. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RePowerTransferReversalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    RePowerTransferReversalApi apiInstance = new RePowerTransferReversalApi(defaultClient);
    Repowerreversalrequest10Wrapper repowerReversalRequest = new Repowerreversalrequest10Wrapper(); // Repowerreversalrequest10Wrapper | Contains the details of the repower reversal request message.
    try {
      Repowerreversal11Wrapper result = apiInstance.repowerReversalPost2(repowerReversalRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RePowerTransferReversalApi#repowerReversalPost2");
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
| **repowerReversalRequest** | [**Repowerreversalrequest10Wrapper**](Repowerreversalrequest10Wrapper.md)| Contains the details of the repower reversal request message. | [optional] |

### Return type

[**Repowerreversal11Wrapper**](Repowerreversal11Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

