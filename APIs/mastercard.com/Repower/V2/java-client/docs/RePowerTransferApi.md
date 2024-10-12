# RePowerTransferApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**repowerPost2**](RePowerTransferApi.md#repowerPost2) | **POST** /repower/v2/repower |  |


<a id="repowerPost2"></a>
# **repowerPost2**
> Repower5Wrapper repowerPost2(repowerRequest)



Mastercard rePower empowers consumers to instantly add money to eligible Mastercard cards. Money is available immediately for expenditures anywhere Mastercard prepaid account is accepted. The ease with which cardholders can convert cash to prepaid card funds turns their reloadable prepaid cards into valuable and practical financial tools. Making the reload process simple and accessible provides merchants with an opportunity to increase cardholder traffic. Unlike other top-up services, merchants have the flexibility to set their own reload fees.  This resource streamlines development efforts to offer Mastercard rePower services, through quick and convenient web services with the following benefits: 1)Savings in development and operational costs associated with implementing a standard MIP connection.  2)Requires support for only a single acquiring interface.  3)Leverages existing processing messages and transaction codes  4)Mastercard provides a net settlement guarantee for each reload transaction  5)Supports EMV, PayPass &amp; MDES transactions.  This resource facilitates the ability for cardholders to reload their prepaid cards easily and securely.   

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RePowerTransferApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    RePowerTransferApi apiInstance = new RePowerTransferApi(defaultClient);
    Repowerrequest1Wrapper repowerRequest = new Repowerrequest1Wrapper(); // Repowerrequest1Wrapper | Contains the details of the repower request message.
    try {
      Repower5Wrapper result = apiInstance.repowerPost2(repowerRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RePowerTransferApi#repowerPost2");
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
| **repowerRequest** | [**Repowerrequest1Wrapper**](Repowerrequest1Wrapper.md)| Contains the details of the repower request message. | [optional] |

### Return type

[**Repower5Wrapper**](Repower5Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

