# UrbanDeliveryApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**confirmCarbonOffset**](UrbanDeliveryApi.md#confirmCarbonOffset) | **PATCH** /urbanDelivery/confirmCarbonOffset | confirmCarbonOffset |
| [**confirmPayment**](UrbanDeliveryApi.md#confirmPayment) | **PATCH** /urbanDelivery/confirmPayment | confirmPayment |
| [**confirmPaymentOfTransaction**](UrbanDeliveryApi.md#confirmPaymentOfTransaction) | **PATCH** /urbanDelivery/confirmTransaction | confirmTransaction |
| [**confirmsPlanting**](UrbanDeliveryApi.md#confirmsPlanting) | **PATCH** /urbanDelivery/confirmPlanting | confirmPlanting |
| [**urbanDelivery**](UrbanDeliveryApi.md#urbanDelivery) | **POST** /urbanDelivery | urbanDelivery |


<a id="confirmCarbonOffset"></a>
# **confirmCarbonOffset**
> confirmCarbonOffset(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName)

confirmCarbonOffset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrbanDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    UrbanDeliveryApi apiInstance = new UrbanDeliveryApi(defaultClient);
    String carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    String contactEmail = "contactEmail_example"; // String | Contact email
    String contactFirstName = "contactFirstName_example"; // String | Contact first name
    String contactLastName = "contactLastName_example"; // String | Contact last name
    try {
      apiInstance.confirmCarbonOffset(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrbanDeliveryApi#confirmCarbonOffset");
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

<a id="confirmPayment"></a>
# **confirmPayment**
> confirmPayment(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrbanDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    UrbanDeliveryApi apiInstance = new UrbanDeliveryApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
    Integer paymentID = 56; // Integer | Payment Id
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPayment(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrbanDeliveryApi#confirmPayment");
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

<a id="confirmPaymentOfTransaction"></a>
# **confirmPaymentOfTransaction**
> confirmPaymentOfTransaction(confirmTransaction, transactionId)

confirmTransaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrbanDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    UrbanDeliveryApi apiInstance = new UrbanDeliveryApi(defaultClient);
    String confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPaymentOfTransaction(confirmTransaction, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrbanDeliveryApi#confirmPaymentOfTransaction");
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

<a id="confirmsPlanting"></a>
# **confirmsPlanting**
> confirmsPlanting(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrbanDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    UrbanDeliveryApi apiInstance = new UrbanDeliveryApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmsPlanting(apiKeyL1, apiKeyL2, confirmPlanting, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrbanDeliveryApi#confirmsPlanting");
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

<a id="urbanDelivery"></a>
# **urbanDelivery**
> urbanDelivery(apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, itemCount, originLatitude, originLongitude, vehicleType)

urbanDelivery

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UrbanDeliveryApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    UrbanDeliveryApi apiInstance = new UrbanDeliveryApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
    String apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
    Double destinationLatitude = 3.4D; // Double | Destination latitude (like: 50.870752, value = -90<=x<=90)
    Double destinationLongitude = 3.4D; // Double | Destination longitude (like: 4.669490, value = -180<=x<=180)
    Integer itemCount = 56; // Integer | item_count' (like:2, value = 0<x<=100)
    Double originLatitude = 3.4D; // Double | Origin latitude (like: 23.372628, value = -90<=x<=90)
    Double originLongitude = 3.4D; // Double | Origin longitude (like: 113.159339, value = -180<=x<=180)
    String vehicleType = "vehicleType_example"; // String | Vehicle type (like: private car, motorcycle,cargo van,zero-emission)
    try {
      apiInstance.urbanDelivery(apiKeyL1, apiKeyL2, destinationLatitude, destinationLongitude, itemCount, originLatitude, originLongitude, vehicleType);
    } catch (ApiException e) {
      System.err.println("Exception when calling UrbanDeliveryApi#urbanDelivery");
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
| **apiKeyL1** | **String**| Client Api Key | |
| **apiKeyL2** | **String**| Integration Partner Api Key | |
| **destinationLatitude** | **Double**| Destination latitude (like: 50.870752, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90) | |
| **destinationLongitude** | **Double**| Destination longitude (like: 4.669490, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180) | |
| **itemCount** | **Integer**| item_count&#39; (like:2, value &#x3D; 0&lt;x&lt;&#x3D;100) | |
| **originLatitude** | **Double**| Origin latitude (like: 23.372628, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90) | |
| **originLongitude** | **Double**| Origin longitude (like: 113.159339, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180) | |
| **vehicleType** | **String**| Vehicle type (like: private car, motorcycle,cargo van,zero-emission) | |

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

