# DefaultApi

All URIs are relative to *https://api.fraudlabspro.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**v1OrderFeedbackPost**](DefaultApi.md#v1OrderFeedbackPost) | **POST** /v1/order/feedback |  |
| [**v1OrderScreenPost**](DefaultApi.md#v1OrderScreenPost) | **POST** /v1/order/screen |  |


<a id="v1OrderFeedbackPost"></a>
# **v1OrderFeedbackPost**
> String v1OrderFeedbackPost(id, key, action, format, notes)



Feedback the status of an order transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fraudlabspro.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String id = "id_example"; // String | 
    String key = "key_example"; // String | 
    String action = "APPROVE"; // String | 
    String format = "json"; // String | 
    String notes = "notes_example"; // String | 
    try {
      String result = apiInstance.v1OrderFeedbackPost(id, key, action, format, notes);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1OrderFeedbackPost");
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
| **id** | **String**|  | |
| **key** | **String**|  | |
| **action** | **String**|  | [enum: APPROVE, REJECT, REJECT_BLACKLIST] |
| **format** | **String**|  | [optional] [enum: json, xml] |
| **notes** | **String**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Feedback order response |  -  |

<a id="v1OrderScreenPost"></a>
# **v1OrderScreenPost**
> String v1OrderScreenPost(ip, key, format, lastName, firstName, billAddr, billCity, billState, billCountry, billZipCode, shipAddr, shipCity, shipState, shipCountry, shipZipCode, emailDomain, userPhone, email, emailHash, usernameHash, passwordHash, binNo, cardHash, avsResult, cvvResult, userOrderId, userOrderMemo, amount, quantity, currency, department, paymentMode, flpChecksum)



Screen order for payment fraud.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.fraudlabspro.com");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String ip = "ip_example"; // String | 
    String key = "key_example"; // String | 
    String format = "json"; // String | 
    String lastName = "lastName_example"; // String | 
    String firstName = "firstName_example"; // String | 
    String billAddr = "billAddr_example"; // String | 
    String billCity = "billCity_example"; // String | 
    String billState = "billState_example"; // String | 
    String billCountry = "billCountry_example"; // String | 
    String billZipCode = "billZipCode_example"; // String | 
    String shipAddr = "shipAddr_example"; // String | 
    String shipCity = "shipCity_example"; // String | 
    String shipState = "shipState_example"; // String | 
    String shipCountry = "shipCountry_example"; // String | 
    String shipZipCode = "shipZipCode_example"; // String | 
    String emailDomain = "emailDomain_example"; // String | 
    String userPhone = "userPhone_example"; // String | 
    String email = "email_example"; // String | 
    String emailHash = "emailHash_example"; // String | 
    String usernameHash = "usernameHash_example"; // String | 
    String passwordHash = "passwordHash_example"; // String | 
    String binNo = "binNo_example"; // String | 
    String cardHash = "cardHash_example"; // String | 
    String avsResult = "avsResult_example"; // String | 
    String cvvResult = "cvvResult_example"; // String | 
    String userOrderId = "userOrderId_example"; // String | 
    String userOrderMemo = "userOrderMemo_example"; // String | 
    BigDecimal amount = new BigDecimal(78); // BigDecimal | 
    Integer quantity = 56; // Integer | 
    String currency = "currency_example"; // String | 
    String department = "department_example"; // String | 
    String paymentMode = "paymentMode_example"; // String | 
    String flpChecksum = "flpChecksum_example"; // String | 
    try {
      String result = apiInstance.v1OrderScreenPost(ip, key, format, lastName, firstName, billAddr, billCity, billState, billCountry, billZipCode, shipAddr, shipCity, shipState, shipCountry, shipZipCode, emailDomain, userPhone, email, emailHash, usernameHash, passwordHash, binNo, cardHash, avsResult, cvvResult, userOrderId, userOrderMemo, amount, quantity, currency, department, paymentMode, flpChecksum);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#v1OrderScreenPost");
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
| **ip** | **String**|  | |
| **key** | **String**|  | |
| **format** | **String**|  | [optional] [enum: json, xml] |
| **lastName** | **String**|  | [optional] |
| **firstName** | **String**|  | [optional] |
| **billAddr** | **String**|  | [optional] |
| **billCity** | **String**|  | [optional] |
| **billState** | **String**|  | [optional] |
| **billCountry** | **String**|  | [optional] |
| **billZipCode** | **String**|  | [optional] |
| **shipAddr** | **String**|  | [optional] |
| **shipCity** | **String**|  | [optional] |
| **shipState** | **String**|  | [optional] |
| **shipCountry** | **String**|  | [optional] |
| **shipZipCode** | **String**|  | [optional] |
| **emailDomain** | **String**|  | [optional] |
| **userPhone** | **String**|  | [optional] |
| **email** | **String**|  | [optional] |
| **emailHash** | **String**|  | [optional] |
| **usernameHash** | **String**|  | [optional] |
| **passwordHash** | **String**|  | [optional] |
| **binNo** | **String**|  | [optional] |
| **cardHash** | **String**|  | [optional] |
| **avsResult** | **String**|  | [optional] |
| **cvvResult** | **String**|  | [optional] |
| **userOrderId** | **String**|  | [optional] |
| **userOrderMemo** | **String**|  | [optional] |
| **amount** | **BigDecimal**|  | [optional] |
| **quantity** | **Integer**|  | [optional] |
| **currency** | **String**|  | [optional] |
| **department** | **String**|  | [optional] |
| **paymentMode** | **String**|  | [optional] |
| **flpChecksum** | **String**|  | [optional] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Screen order response |  -  |

