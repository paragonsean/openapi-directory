# PaymentMethodApi

All URIs are relative to *https://go.netlicensing.io/core/v2/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPaymentMethod**](PaymentMethodApi.md#getPaymentMethod) | **GET** /paymentmethod/{paymentMethodNumber} | Get Payment Method |
| [**listPaymentMethods**](PaymentMethodApi.md#listPaymentMethods) | **GET** /paymentmethod | List Payment Methods |
| [**updatePaymentMethod**](PaymentMethodApi.md#updatePaymentMethod) | **POST** /paymentmethod/{paymentMethodNumber} | Update Payment Method |


<a id="getPaymentMethod"></a>
# **getPaymentMethod**
> Netlicensing getPaymentMethod(paymentMethodNumber)

Get Payment Method

Return a Payment Method info by &#39;paymentMethodNumber&#39;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentMethodApi apiInstance = new PaymentMethodApi(defaultClient);
    String paymentMethodNumber = "paymentMethodNumber_example"; // String | Payment method number
    try {
      Netlicensing result = apiInstance.getPaymentMethod(paymentMethodNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodApi#getPaymentMethod");
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
| **paymentMethodNumber** | **String**| Payment method number | |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="listPaymentMethods"></a>
# **listPaymentMethods**
> List&lt;Netlicensing&gt; listPaymentMethods()

List Payment Methods

Return a list of all Payment Methods for the current Vendor

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentMethodApi apiInstance = new PaymentMethodApi(defaultClient);
    try {
      List<Netlicensing> result = apiInstance.listPaymentMethods();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodApi#listPaymentMethods");
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

[**List&lt;Netlicensing&gt;**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

<a id="updatePaymentMethod"></a>
# **updatePaymentMethod**
> Netlicensing updatePaymentMethod(paymentMethodNumber, active, paypalSubject)

Update Payment Method

Sets the provided properties to a Payment Method. Return an updated Payment Method

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PaymentMethodApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://go.netlicensing.io/core/v2/rest");
    
    // Configure HTTP basic authorization: basicAuth
    HttpBasicAuth basicAuth = (HttpBasicAuth) defaultClient.getAuthentication("basicAuth");
    basicAuth.setUsername("YOUR USERNAME");
    basicAuth.setPassword("YOUR PASSWORD");

    PaymentMethodApi apiInstance = new PaymentMethodApi(defaultClient);
    String paymentMethodNumber = "paymentMethodNumber_example"; // String | Payment method number
    Boolean active = true; // Boolean | If set to 'false', the Payment Method is disabled.
    String paypalSubject = "paypalSubject_example"; // String | The e-mail address of the PayPal account for which you are making the API calls.
    try {
      Netlicensing result = apiInstance.updatePaymentMethod(paymentMethodNumber, active, paypalSubject);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PaymentMethodApi#updatePaymentMethod");
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
| **paymentMethodNumber** | **String**| Payment method number | |
| **active** | **Boolean**| If set to &#39;false&#39;, the Payment Method is disabled. | [optional] |
| **paypalSubject** | **String**| The e-mail address of the PayPal account for which you are making the API calls. | [optional] |

### Return type

[**Netlicensing**](Netlicensing.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Successful request |  -  |
| **400** | Malformed or illegal request |  -  |
| **403** | Access is denied |  -  |
| **404** | Resource not found |  -  |
| **500** | Internal service error |  -  |

