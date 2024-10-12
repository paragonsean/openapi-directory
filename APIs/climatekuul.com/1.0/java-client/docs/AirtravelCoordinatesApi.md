# AirtravelCoordinatesApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airtravelCoordinates**](AirtravelCoordinatesApi.md#airtravelCoordinates) | **POST** /airtravelCoordinates | airtravelCoordinates |
| [**confirmCarbonOffset4**](AirtravelCoordinatesApi.md#confirmCarbonOffset4) | **PATCH** /airtravelCoordinates/confirmCarbonOffset | confirmCarbonOffset |
| [**confirmPayment4**](AirtravelCoordinatesApi.md#confirmPayment4) | **PATCH** /airtravelCoordinates/confirmPayment | confirmPayment |
| [**confirmPaymentOfTransaction4**](AirtravelCoordinatesApi.md#confirmPaymentOfTransaction4) | **PATCH** /airtravelCoordinates/confirmTransaction | confirmTransaction |
| [**confirmsPlanting4**](AirtravelCoordinatesApi.md#confirmsPlanting4) | **PATCH** /airtravelCoordinates/confirmPlanting | confirmPlanting |


<a id="airtravelCoordinates"></a>
# **airtravelCoordinates**
> airtravelCoordinates(contentType, apiKeyL1, apiKeyL2, destinationAirportLatitude, destinationAirportLongitude, numberOfPassengers, originAirportLatitude, originAirportLongitude, travelClass, travelMode)

airtravelCoordinates

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelCoordinatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelCoordinatesApi apiInstance = new AirtravelCoordinatesApi(defaultClient);
    String contentType = "application/x-www-form-urlencoded"; // String | 
    String apiKeyL1 = "apiKeyL1_example"; // String | Client Api Key
    String apiKeyL2 = "apiKeyL2_example"; // String | Integration Partner Api Key
    Double destinationAirportLatitude = 3.4D; // Double | Destination latitude (like:  50.870752, value = -90<=x<=90)
    Double destinationAirportLongitude = 3.4D; // Double | Destination longitude (like:  4.669490, value = -180<=x<=180)
    Integer numberOfPassengers = 56; // Integer | Number of passengers (like: 1, 2 ,3 )
    Double originAirportLatitude = 3.4D; // Double | Origin latitude (like: 23.372628 value = -90<=x<=90 )
    Double originAirportLongitude = 3.4D; // Double | Origin longitude (like: 113.159339, value = -180<=x<=180 )
    String travelClass = "travelClass_example"; // String | Travel class can be 'First Class', 'Economy', 'Business' or 'Premium Economy'
    String travelMode = "travelMode_example"; // String | Travel mode can be 'one way' or 'round trip'
    try {
      apiInstance.airtravelCoordinates(contentType, apiKeyL1, apiKeyL2, destinationAirportLatitude, destinationAirportLongitude, numberOfPassengers, originAirportLatitude, originAirportLongitude, travelClass, travelMode);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelCoordinatesApi#airtravelCoordinates");
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
| **destinationAirportLatitude** | **Double**| Destination latitude (like:  50.870752, value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90) | |
| **destinationAirportLongitude** | **Double**| Destination longitude (like:  4.669490, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180) | |
| **numberOfPassengers** | **Integer**| Number of passengers (like: 1, 2 ,3 ) | |
| **originAirportLatitude** | **Double**| Origin latitude (like: 23.372628 value &#x3D; -90&lt;&#x3D;x&lt;&#x3D;90 ) | |
| **originAirportLongitude** | **Double**| Origin longitude (like: 113.159339, value &#x3D; -180&lt;&#x3D;x&lt;&#x3D;180 ) | |
| **travelClass** | **String**| Travel class can be &#39;First Class&#39;, &#39;Economy&#39;, &#39;Business&#39; or &#39;Premium Economy&#39; | |
| **travelMode** | **String**| Travel mode can be &#39;one way&#39; or &#39;round trip&#39; | |

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

<a id="confirmCarbonOffset4"></a>
# **confirmCarbonOffset4**
> confirmCarbonOffset4(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName)

confirmCarbonOffset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelCoordinatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelCoordinatesApi apiInstance = new AirtravelCoordinatesApi(defaultClient);
    String carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    String contactEmail = "contactEmail_example"; // String | Contact email
    String contactFirstName = "contactFirstName_example"; // String | Contact first name
    String contactLastName = "contactLastName_example"; // String | Contact last name
    try {
      apiInstance.confirmCarbonOffset4(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelCoordinatesApi#confirmCarbonOffset4");
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

<a id="confirmPayment4"></a>
# **confirmPayment4**
> confirmPayment4(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelCoordinatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelCoordinatesApi apiInstance = new AirtravelCoordinatesApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
    Integer paymentID = 56; // Integer | Payment Id
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPayment4(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelCoordinatesApi#confirmPayment4");
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

<a id="confirmPaymentOfTransaction4"></a>
# **confirmPaymentOfTransaction4**
> confirmPaymentOfTransaction4(confirmTransaction, transactionId)

confirmTransaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelCoordinatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelCoordinatesApi apiInstance = new AirtravelCoordinatesApi(defaultClient);
    String confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPaymentOfTransaction4(confirmTransaction, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelCoordinatesApi#confirmPaymentOfTransaction4");
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

<a id="confirmsPlanting4"></a>
# **confirmsPlanting4**
> confirmsPlanting4(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelCoordinatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelCoordinatesApi apiInstance = new AirtravelCoordinatesApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmsPlanting4(apiKeyL1, apiKeyL2, confirmPlanting, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelCoordinatesApi#confirmsPlanting4");
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

