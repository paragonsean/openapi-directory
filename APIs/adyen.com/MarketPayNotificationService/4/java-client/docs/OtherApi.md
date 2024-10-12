# OtherApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postPAYMENTFAILURE**](OtherApi.md#postPAYMENTFAILURE) | **POST** /PAYMENT_FAILURE | Booking for a capture or refund failed |
| [**postREPORTAVAILABLE**](OtherApi.md#postREPORTAVAILABLE) | **POST** /REPORT_AVAILABLE | Report available |


<a id="postPAYMENTFAILURE"></a>
# **postPAYMENTFAILURE**
> NotificationResponse postPAYMENTFAILURE(paymentFailureNotification)

Booking for a capture or refund failed

Adyen sends this notification when a [split payment](https://docs.adyen.com/marketplaces-and-platforms/classic/processing-payments#providing-split-information) booking for a capture or refund fails. When a booking fails due to an invalid account status or an unknown &#x60;accountCode&#x60;, the funds are credited or debited to or fromyour platform&#39;s liable account instead of the account specified in the split data.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    OtherApi apiInstance = new OtherApi(defaultClient);
    PaymentFailureNotification paymentFailureNotification = new PaymentFailureNotification(); // PaymentFailureNotification | 
    try {
      NotificationResponse result = apiInstance.postPAYMENTFAILURE(paymentFailureNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#postPAYMENTFAILURE");
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
| **paymentFailureNotification** | [**PaymentFailureNotification**](PaymentFailureNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

<a id="postREPORTAVAILABLE"></a>
# **postREPORTAVAILABLE**
> NotificationResponse postREPORTAVAILABLE(reportAvailableNotification)

Report available

Adyen sends this notification when a report has been generated and it is available for download.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OtherApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");
    
    // Configure HTTP basic authorization: BasicAuth
    HttpBasicAuth BasicAuth = (HttpBasicAuth) defaultClient.getAuthentication("BasicAuth");
    BasicAuth.setUsername("YOUR USERNAME");
    BasicAuth.setPassword("YOUR PASSWORD");

    OtherApi apiInstance = new OtherApi(defaultClient);
    ReportAvailableNotification reportAvailableNotification = new ReportAvailableNotification(); // ReportAvailableNotification | 
    try {
      NotificationResponse result = apiInstance.postREPORTAVAILABLE(reportAvailableNotification);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OtherApi#postREPORTAVAILABLE");
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
| **reportAvailableNotification** | [**ReportAvailableNotification**](ReportAvailableNotification.md)|  | [optional] |

### Return type

[**NotificationResponse**](NotificationResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK - the request has succeeded. |  -  |

