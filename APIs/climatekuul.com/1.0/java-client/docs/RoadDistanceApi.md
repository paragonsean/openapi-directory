# RoadDistanceApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**confirmCarbonOffset5**](RoadDistanceApi.md#confirmCarbonOffset5) | **PATCH** /roadDistance/confirmCarbonOffset | confirmCarbonOffset |
| [**confirmPayment5**](RoadDistanceApi.md#confirmPayment5) | **PATCH** /roadDistance/confirmPayment | confirmPayment |
| [**confirmPaymentOfTransaction5**](RoadDistanceApi.md#confirmPaymentOfTransaction5) | **PATCH** /roadDistance/confirmTransaction | confirmTransaction |
| [**confirmsPlanting5**](RoadDistanceApi.md#confirmsPlanting5) | **PATCH** /roadDistance/confirmPlanting | confirmPlanting |
| [**roadDistance**](RoadDistanceApi.md#roadDistance) | **POST** /roadDistance | RoadDistance |


<a id="confirmCarbonOffset5"></a>
# **confirmCarbonOffset5**
> confirmCarbonOffset5(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName)

confirmCarbonOffset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoadDistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    RoadDistanceApi apiInstance = new RoadDistanceApi(defaultClient);
    String carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    String contactEmail = "contactEmail_example"; // String | Contact email
    String contactFirstName = "contactFirstName_example"; // String | Contact first name
    String contactLastName = "contactLastName_example"; // String | Contact last name
    try {
      apiInstance.confirmCarbonOffset5(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoadDistanceApi#confirmCarbonOffset5");
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

<a id="confirmPayment5"></a>
# **confirmPayment5**
> confirmPayment5(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoadDistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    RoadDistanceApi apiInstance = new RoadDistanceApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
    Integer paymentID = 56; // Integer | Payment Id
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPayment5(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoadDistanceApi#confirmPayment5");
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

<a id="confirmPaymentOfTransaction5"></a>
# **confirmPaymentOfTransaction5**
> confirmPaymentOfTransaction5(confirmTransaction, transactionId)

confirmTransaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoadDistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    RoadDistanceApi apiInstance = new RoadDistanceApi(defaultClient);
    String confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPaymentOfTransaction5(confirmTransaction, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoadDistanceApi#confirmPaymentOfTransaction5");
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

<a id="confirmsPlanting5"></a>
# **confirmsPlanting5**
> confirmsPlanting5(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoadDistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    RoadDistanceApi apiInstance = new RoadDistanceApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmsPlanting5(apiKeyL1, apiKeyL2, confirmPlanting, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoadDistanceApi#confirmsPlanting5");
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

<a id="roadDistance"></a>
# **roadDistance**
> roadDistance(apiKeyL1, apiKeyL2, travelDistance, tripEnd, tripStart, vehicleType, vehicleMake, vehicleYear)

RoadDistance

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RoadDistanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    RoadDistanceApi apiInstance = new RoadDistanceApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
    String apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
    Integer travelDistance = 56; // Integer | 
    Integer tripEnd = 56; // Integer | timestamp in epoch time (like: 1606780799)
    Integer tripStart = 56; // Integer | timestamp in epoch time (like: 1604188800)
    String vehicleType = "vehicleType_example"; // String | Vehicle type can be 'personal car', 'light truck' or 'heavy-duty truck'
    String vehicleMake = "vehicleMake_example"; // String | vehicle make (like: Honda, Toyota, Smart), Required only when vehicle_type is 'personal car' 
    Integer vehicleYear = 56; // Integer | vehicle year (like: 2010, 2015, 2019), Required only when vehicle_type is 'personal car' 
    try {
      apiInstance.roadDistance(apiKeyL1, apiKeyL2, travelDistance, tripEnd, tripStart, vehicleType, vehicleMake, vehicleYear);
    } catch (ApiException e) {
      System.err.println("Exception when calling RoadDistanceApi#roadDistance");
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
| **travelDistance** | **Integer**|  | |
| **tripEnd** | **Integer**| timestamp in epoch time (like: 1606780799) | |
| **tripStart** | **Integer**| timestamp in epoch time (like: 1604188800) | |
| **vehicleType** | **String**| Vehicle type can be &#39;personal car&#39;, &#39;light truck&#39; or &#39;heavy-duty truck&#39; | |
| **vehicleMake** | **String**| vehicle make (like: Honda, Toyota, Smart), Required only when vehicle_type is &#39;personal car&#39;  | [optional] |
| **vehicleYear** | **Integer**| vehicle year (like: 2010, 2015, 2019), Required only when vehicle_type is &#39;personal car&#39;  | [optional] |

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

