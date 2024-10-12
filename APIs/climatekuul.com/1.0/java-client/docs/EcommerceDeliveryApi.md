# EcommerceDeliveryApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**confirmCarbonOffset1**](EcommerceDeliveryApi.md#confirmCarbonOffset1) | **PATCH** /ecommerceDelivery/confirmCarbonOffset | confirmCarbonOffset |
| [**confirmPayment1**](EcommerceDeliveryApi.md#confirmPayment1) | **PATCH** /ecommerceDelivery/confirmPayment | confirmPayment |
| [**confirmPaymentOfTransaction1**](EcommerceDeliveryApi.md#confirmPaymentOfTransaction1) | **PATCH** /ecommerceDelivery/confirmTransaction | confirmTransaction |
| [**confirmsPlanting2**](EcommerceDeliveryApi.md#confirmsPlanting2) | **PATCH** /ecommerceDelivery/confirmPlanting | confirmPlanting |
| [**ecommerceDelivery**](EcommerceDeliveryApi.md#ecommerceDelivery) | **POST** /ecommerceDelivery | ecommerceDelivery |


<a id="confirmCarbonOffset1"></a>
# **confirmCarbonOffset1**
> confirmCarbonOffset1(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName)

confirmCarbonOffset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EcommerceDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    EcommerceDeliveryApi apiInstance = new EcommerceDeliveryApi(defaultClient);
    String carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    String contactEmail = "contactEmail_example"; // String | Contact email
    String contactFirstName = "contactFirstName_example"; // String | Contact first name
    String contactLastName = "contactLastName_example"; // String | Contact last name
    try {
      apiInstance.confirmCarbonOffset1(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcommerceDeliveryApi#confirmCarbonOffset1");
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
| **carbonOffset** | **String**| Confirm Carbon Offset (Value &#x3D; y/n) | |
| **transactionId** | **String**| transaction_id | |
| **contactEmail** | **String**| Contact email | [optional] |
| **contactFirstName** | **String**| Contact first name | [optional] |
| **contactLastName** | **String**| Contact last name | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="confirmPayment1"></a>
# **confirmPayment1**
> confirmPayment1(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EcommerceDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    EcommerceDeliveryApi apiInstance = new EcommerceDeliveryApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
    Integer paymentID = 56; // Integer | Payment Id
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPayment1(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcommerceDeliveryApi#confirmPayment1");
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
| **apiKeyL1** | **String**| apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560) | |
| **apiKeyL2** | **String**| apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166) | |
| **confirmPayment** | **String**| Confirm Payment (Value &#x3D; y/n) | |
| **paymentID** | **Integer**| Payment Id | |
| **transactionId** | **String**| transaction_id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="confirmPaymentOfTransaction1"></a>
# **confirmPaymentOfTransaction1**
> confirmPaymentOfTransaction1(confirmTransaction, transactionId)

confirmTransaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EcommerceDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    EcommerceDeliveryApi apiInstance = new EcommerceDeliveryApi(defaultClient);
    String confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPaymentOfTransaction1(confirmTransaction, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcommerceDeliveryApi#confirmPaymentOfTransaction1");
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
| **confirmTransaction** | **String**| Confirm Payment Of Transaction (Value &#x3D; y/n) | |
| **transactionId** | **String**| transaction_id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="confirmsPlanting2"></a>
# **confirmsPlanting2**
> confirmsPlanting2(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EcommerceDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    EcommerceDeliveryApi apiInstance = new EcommerceDeliveryApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmsPlanting2(apiKeyL1, apiKeyL2, confirmPlanting, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcommerceDeliveryApi#confirmsPlanting2");
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
| **apiKeyL1** | **String**| apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560) | |
| **apiKeyL2** | **String**| apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166) | |
| **confirmPlanting** | **String**| Confirm Planting (Value &#x3D; y/n) | |
| **transactionId** | **String**| transaction_id | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="ecommerceDelivery"></a>
# **ecommerceDelivery**
> ecommerceDelivery(contentType, apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, originLatitude, originLongitude, volumetricWeight, waybillType, destinationAirportCode, originAirportCode)

ecommerceDelivery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EcommerceDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    EcommerceDeliveryApi apiInstance = new EcommerceDeliveryApi(defaultClient);
    String contentType = "application/x-www-form-urlencoded"; // String | 
    String apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
    String apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
    Double destinationLatitude = 3.4D; // Double | valid latitude of destination
    Double destinationLongitude = 3.4D; // Double | valid longitude of destination
    Double originLatitude = 3.4D; // Double | valid latitude of origin
    Double originLongitude = 3.4D; // Double | valid longitude of origin
    Double volumetricWeight = 3.4D; // Double | Volumetric weight' (like:2.70)
    String waybillType = "waybillType_example"; // String | this can be 'air only', 'road only' or 'air and road'
    String destinationAirportCode = "destinationAirportCode_example"; // String | valid airport code of destination
    String originAirportCode = "originAirportCode_example"; // String | valid airport code of origin
    try {
      apiInstance.ecommerceDelivery(contentType, apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, originLatitude, originLongitude, volumetricWeight, waybillType, destinationAirportCode, originAirportCode);
    } catch (ApiException e) {
      System.err.println("Exception when calling EcommerceDeliveryApi#ecommerceDelivery");
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
| **contentType** | **String**|  | |
| **apiKeyL1** | **String**| Client Api Key | |
| **apiKeyL2** | **String**| Integration Partner Api Key | |
| **destinationLatitude** | **Double**| valid latitude of destination | |
| **destinationLongitude** | **Double**| valid longitude of destination | |
| **originLatitude** | **Double**| valid latitude of origin | |
| **originLongitude** | **Double**| valid longitude of origin | |
| **volumetricWeight** | **Double**| Volumetric weight&#39; (like:2.70) | |
| **waybillType** | **String**| this can be &#39;air only&#39;, &#39;road only&#39; or &#39;air and road&#39; | |
| **destinationAirportCode** | **String**| valid airport code of destination | [optional] |
| **originAirportCode** | **String**| valid airport code of origin | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

