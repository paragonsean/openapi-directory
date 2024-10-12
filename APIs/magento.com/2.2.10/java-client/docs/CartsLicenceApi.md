# CartsLicenceApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet**](CartsLicenceApi.md#checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet) | **GET** /V1/carts/licence | carts/licence |


<a id="checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet"></a>
# **checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet**
> List&lt;CheckoutAgreementsDataAgreementInterface&gt; checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet()

carts/licence

Lists active checkout agreements.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsLicenceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsLicenceApi apiInstance = new CartsLicenceApi(defaultClient);
    try {
      List<CheckoutAgreementsDataAgreementInterface> result = apiInstance.checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsLicenceApi#checkoutAgreementsCheckoutAgreementsRepositoryV1GetListGet");
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

[**List&lt;CheckoutAgreementsDataAgreementInterface&gt;**](CheckoutAgreementsDataAgreementInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

