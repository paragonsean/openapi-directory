# RefundsApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPaymentRefund**](RefundsApi.md#getPaymentRefund) | **GET** /v2/refunds/{refund_id} | GetPaymentRefund |
| [**listPaymentRefunds**](RefundsApi.md#listPaymentRefunds) | **GET** /v2/refunds | ListPaymentRefunds |
| [**refundPayment**](RefundsApi.md#refundPayment) | **POST** /v2/refunds | RefundPayment |


<a id="getPaymentRefund"></a>
# **getPaymentRefund**
> GetPaymentRefundResponse getPaymentRefund(refundId)

GetPaymentRefund

Retrieves a specific refund using the &#x60;refund_id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RefundsApi apiInstance = new RefundsApi(defaultClient);
    String refundId = "refundId_example"; // String | The unique ID for the desired `PaymentRefund`.
    try {
      GetPaymentRefundResponse result = apiInstance.getPaymentRefund(refundId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundsApi#getPaymentRefund");
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
| **refundId** | **String**| The unique ID for the desired &#x60;PaymentRefund&#x60;. | |

### Return type

[**GetPaymentRefundResponse**](GetPaymentRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="listPaymentRefunds"></a>
# **listPaymentRefunds**
> ListPaymentRefundsResponse listPaymentRefunds(beginTime, endTime, sortOrder, cursor, locationId, status, sourceType, limit)

ListPaymentRefunds

Retrieves a list of refunds for the account making the request.  Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.  The maximum results per page is 100.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RefundsApi apiInstance = new RefundsApi(defaultClient);
    String beginTime = "beginTime_example"; // String | The timestamp for the beginning of the requested reporting period, in RFC 3339 format.  Default: The current time minus one year.
    String endTime = "endTime_example"; // String | The timestamp for the end of the requested reporting period, in RFC 3339 format.  Default: The current time.
    String sortOrder = "sortOrder_example"; // String | The order in which results are listed: - `ASC` - Oldest to newest. - `DESC` - Newest to oldest (default).
    String cursor = "cursor_example"; // String | A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination).
    String locationId = "locationId_example"; // String | Limit results to the location supplied. By default, results are returned for all locations associated with the seller.
    String status = "status_example"; // String | If provided, only refunds with the given status are returned. For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).  Default: If omitted, refunds are returned regardless of their status.
    String sourceType = "sourceType_example"; // String | If provided, only refunds with the given source type are returned. - `CARD` - List refunds only for payments where `CARD` was specified as the payment source.  Default: If omitted, refunds are returned regardless of the source type.
    Integer limit = 56; // Integer | The maximum number of results to be returned in a single page.  It is possible to receive fewer results than the specified limit on a given page.  If the supplied value is greater than 100, no more than 100 results are returned.  Default: 100
    try {
      ListPaymentRefundsResponse result = apiInstance.listPaymentRefunds(beginTime, endTime, sortOrder, cursor, locationId, status, sourceType, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundsApi#listPaymentRefunds");
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
| **beginTime** | **String**| The timestamp for the beginning of the requested reporting period, in RFC 3339 format.  Default: The current time minus one year. | [optional] |
| **endTime** | **String**| The timestamp for the end of the requested reporting period, in RFC 3339 format.  Default: The current time. | [optional] |
| **sortOrder** | **String**| The order in which results are listed: - &#x60;ASC&#x60; - Oldest to newest. - &#x60;DESC&#x60; - Newest to oldest (default). | [optional] |
| **cursor** | **String**| A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for the original query.  For more information, see [Pagination](https://developer.squareup.com/docs/basics/api101/pagination). | [optional] |
| **locationId** | **String**| Limit results to the location supplied. By default, results are returned for all locations associated with the seller. | [optional] |
| **status** | **String**| If provided, only refunds with the given status are returned. For a list of refund status values, see [PaymentRefund](https://developer.squareup.com/reference/square_2021-08-18/objects/PaymentRefund).  Default: If omitted, refunds are returned regardless of their status. | [optional] |
| **sourceType** | **String**| If provided, only refunds with the given source type are returned. - &#x60;CARD&#x60; - List refunds only for payments where &#x60;CARD&#x60; was specified as the payment source.  Default: If omitted, refunds are returned regardless of the source type. | [optional] |
| **limit** | **Integer**| The maximum number of results to be returned in a single page.  It is possible to receive fewer results than the specified limit on a given page.  If the supplied value is greater than 100, no more than 100 results are returned.  Default: 100 | [optional] |

### Return type

[**ListPaymentRefundsResponse**](ListPaymentRefundsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="refundPayment"></a>
# **refundPayment**
> RefundPaymentResponse refundPayment(refundPaymentRequest)

RefundPayment

Refunds a payment. You can refund the entire payment amount or a portion of it. You can use this endpoint to refund a card payment or record a  refund of a cash or external payment. For more information, see [Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RefundsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    RefundsApi apiInstance = new RefundsApi(defaultClient);
    RefundPaymentRequest refundPaymentRequest = new RefundPaymentRequest(); // RefundPaymentRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      RefundPaymentResponse result = apiInstance.refundPayment(refundPaymentRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RefundsApi#refundPayment");
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
| **refundPaymentRequest** | [**RefundPaymentRequest**](RefundPaymentRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**RefundPaymentResponse**](RefundPaymentResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

