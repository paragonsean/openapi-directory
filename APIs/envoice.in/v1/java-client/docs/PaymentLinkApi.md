# PaymentLinkApi

All URIs are relative to *https://www.envoice.in*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**paymentLinkApiAll**](PaymentLinkApi.md#paymentLinkApiAll) | **GET** /api/paymentlink/all | Create a payment link |
| [**paymentLinkApiDelete**](PaymentLinkApi.md#paymentLinkApiDelete) | **POST** /api/paymentlink/delete | Delete an existing payment link |
| [**paymentLinkApiNew**](PaymentLinkApi.md#paymentLinkApiNew) | **POST** /api/paymentlink/new | Create a payment link |
| [**paymentLinkApiUri**](PaymentLinkApi.md#paymentLinkApiUri) | **GET** /api/paymentlink/uri | Return the unique url to the client&#39;s payment link |


<a id="paymentLinkApiAll"></a>
# **paymentLinkApiAll**
> ListResultPaymentLink paymentLinkApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize)

Create a payment link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    PaymentLinkApi apiInstance = new PaymentLinkApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    Integer queryOptionsPage = 56; // Integer | 
    Integer queryOptionsPageSize = 56; // Integer | 
    try {
      ListResultPaymentLink result = apiInstance.paymentLinkApiAll(xAuthKey, xAuthSecret, queryOptionsPage, queryOptionsPageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinkApi#paymentLinkApiAll");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **queryOptionsPage** | **Integer**|  | [optional] |
| **queryOptionsPageSize** | **Integer**|  | [optional] |

### Return type

[**ListResultPaymentLink**](ListResultPaymentLink.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="paymentLinkApiDelete"></a>
# **paymentLinkApiDelete**
> Integer paymentLinkApiDelete(xAuthKey, xAuthSecret, paymentLink)

Delete an existing payment link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    PaymentLinkApi apiInstance = new PaymentLinkApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    PaymentLink paymentLink = new PaymentLink(); // PaymentLink | 
    try {
      Integer result = apiInstance.paymentLinkApiDelete(xAuthKey, xAuthSecret, paymentLink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinkApi#paymentLinkApiDelete");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **paymentLink** | [**PaymentLink**](PaymentLink.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="paymentLinkApiNew"></a>
# **paymentLinkApiNew**
> Integer paymentLinkApiNew(xAuthKey, xAuthSecret, paymentLink)

Create a payment link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    PaymentLinkApi apiInstance = new PaymentLinkApi(defaultClient);
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    PaymentLink paymentLink = new PaymentLink(); // PaymentLink | 
    try {
      Integer result = apiInstance.paymentLinkApiNew(xAuthKey, xAuthSecret, paymentLink);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinkApi#paymentLinkApiNew");
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
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |
| **paymentLink** | [**PaymentLink**](PaymentLink.md)|  | |

### Return type

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, application/xml, text/html, text/json, text/xml
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="paymentLinkApiUri"></a>
# **paymentLinkApiUri**
> PaymentLinkUriApiModel paymentLinkApiUri(id, xAuthKey, xAuthSecret)

Return the unique url to the client&#39;s payment link

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentLinkApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://www.envoice.in");

    PaymentLinkApi apiInstance = new PaymentLinkApi(defaultClient);
    Integer id = 56; // Integer | 
    String xAuthKey = "[authentication key]"; // String | 
    String xAuthSecret = "[authentication secret]"; // String | 
    try {
      PaymentLinkUriApiModel result = apiInstance.paymentLinkApiUri(id, xAuthKey, xAuthSecret);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentLinkApi#paymentLinkApiUri");
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
| **id** | **Integer**|  | |
| **xAuthKey** | **String**|  | [default to [authentication key]] |
| **xAuthSecret** | **String**|  | [default to [authentication secret]] |

### Return type

[**PaymentLinkUriApiModel**](PaymentLinkUriApiModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/html, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

