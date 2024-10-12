# AirtravelMultilegApi

All URIs are relative to *http://api.climatekuul.com:8000/footprint*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**airtravelMultileg**](AirtravelMultilegApi.md#airtravelMultileg) | **POST** /airtravelMultileg | airtravelMultileg |
| [**confirmCarbonOffset3**](AirtravelMultilegApi.md#confirmCarbonOffset3) | **PATCH** /airtravelMultileg/confirmCarbonOffset | confirmCarbonOffset |
| [**confirmPayment3**](AirtravelMultilegApi.md#confirmPayment3) | **PATCH** /airtravelMultileg/confirmPayment | confirmPayment |
| [**confirmPaymentOfTransaction3**](AirtravelMultilegApi.md#confirmPaymentOfTransaction3) | **PATCH** /airtravelMultileg/confirmTransaction | confirmTransaction |
| [**confirmsPlanting3**](AirtravelMultilegApi.md#confirmsPlanting3) | **PATCH** /airtravelMultileg/confirmPlanting | confirmPlanting |


<a id="airtravelMultileg"></a>
# **airtravelMultileg**
> airtravelMultileg(airtravelMultilegRequest)

airtravelMultileg

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelMultilegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelMultilegApi apiInstance = new AirtravelMultilegApi(defaultClient);
    AirtravelMultilegRequest airtravelMultilegRequest = new AirtravelMultilegRequest(); // AirtravelMultilegRequest | 
    try {
      apiInstance.airtravelMultileg(airtravelMultilegRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelMultilegApi#airtravelMultileg");
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
| **airtravelMultilegRequest** | [**AirtravelMultilegRequest**](AirtravelMultilegRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="confirmCarbonOffset3"></a>
# **confirmCarbonOffset3**
> confirmCarbonOffset3(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName)

confirmCarbonOffset

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelMultilegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelMultilegApi apiInstance = new AirtravelMultilegApi(defaultClient);
    String carbonOffset = "carbonOffset_example"; // String | Confirm Carbon Offset (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    String contactEmail = "contactEmail_example"; // String | Contact email
    String contactFirstName = "contactFirstName_example"; // String | Contact first name
    String contactLastName = "contactLastName_example"; // String | Contact last name
    try {
      apiInstance.confirmCarbonOffset3(carbonOffset, transactionId, contactEmail, contactFirstName, contactLastName);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelMultilegApi#confirmCarbonOffset3");
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

<a id="confirmPayment3"></a>
# **confirmPayment3**
> confirmPayment3(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId)

confirmPayment

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelMultilegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelMultilegApi apiInstance = new AirtravelMultilegApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPayment = "confirmPayment_example"; // String | Confirm Payment (Value = y/n)
    Integer paymentID = 56; // Integer | Payment Id
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPayment3(apiKeyL1, apiKeyL2, confirmPayment, paymentID, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelMultilegApi#confirmPayment3");
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

<a id="confirmPaymentOfTransaction3"></a>
# **confirmPaymentOfTransaction3**
> confirmPaymentOfTransaction3(confirmTransaction, transactionId)

confirmTransaction

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelMultilegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelMultilegApi apiInstance = new AirtravelMultilegApi(defaultClient);
    String confirmTransaction = "confirmTransaction_example"; // String | Confirm Payment Of Transaction (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmPaymentOfTransaction3(confirmTransaction, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelMultilegApi#confirmPaymentOfTransaction3");
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

<a id="confirmsPlanting3"></a>
# **confirmsPlanting3**
> confirmsPlanting3(apiKeyL1, apiKeyL2, confirmPlanting, transactionId)

confirmPlanting

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AirtravelMultilegApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.climatekuul.com:8000/footprint");

    AirtravelMultilegApi apiInstance = new AirtravelMultilegApi(defaultClient);
    String apiKeyL1 = "apiKeyL1_example"; // String | apikey_l1 (Like: d95fead6-e8a6-4247-9fb9-7835101a4560)
    String apiKeyL2 = "apiKeyL2_example"; // String | apikey_l2 (Like: c60f8db5-7904-4227-960d-27400c38b166)
    String confirmPlanting = "confirmPlanting_example"; // String | Confirm Planting (Value = y/n)
    String transactionId = "transactionId_example"; // String | transaction_id
    try {
      apiInstance.confirmsPlanting3(apiKeyL1, apiKeyL2, confirmPlanting, transactionId);
    } catch (ApiException e) {
      System.err.println("Exception when calling AirtravelMultilegApi#confirmsPlanting3");
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

