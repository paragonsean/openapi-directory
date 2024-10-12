# TransferNotificationRegistrationApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createTransferNotificationRegistration**](TransferNotificationRegistrationApi.md#createTransferNotificationRegistration) | **POST** /send/v1/partners/{partnerId}/notification-registries | This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction. |
| [**deleteTransferNotificationRegistration**](TransferNotificationRegistrationApi.md#deleteTransferNotificationRegistration) | **DELETE** /send/v1/partners/{partnerId}/notification-registries/{account-reg-ref} | This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications.  |
| [**notificationRegistrationAPIReadBy**](TransferNotificationRegistrationApi.md#notificationRegistrationAPIReadBy) | **GET** /send/v1/partners/{partnerId}/notification-registries/{account-reg-ref} | This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications.  |
| [**notificationRegistrationAPIUpdate**](TransferNotificationRegistrationApi.md#notificationRegistrationAPIUpdate) | **PUT** /send/v1/partners/{partnerId}/notification-registries/{account-reg-ref} | This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN. |


<a id="createTransferNotificationRegistration"></a>
# **createTransferNotificationRegistration**
> Accountregistration168Wrapper createTransferNotificationRegistration(partnerId, accountregistration)

This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.

This service allows Mastercard Merchant QR originating and receiving partners to register a PAN and service provider to receive notifications on an inbound Merchant Refund or Merchant Payment Transaction.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransferNotificationRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TransferNotificationRegistrationApi apiInstance = new TransferNotificationRegistrationApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    Accountregistration167Wrapper accountregistration = new Accountregistration167Wrapper(); // Accountregistration167Wrapper | Contains the details of the request message.
    try {
      Accountregistration168Wrapper result = apiInstance.createTransferNotificationRegistration(partnerId, accountregistration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransferNotificationRegistrationApi#createTransferNotificationRegistration");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | |
| **accountregistration** | [**Accountregistration167Wrapper**](Accountregistration167Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**Accountregistration168Wrapper**](Accountregistration168Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

<a id="deleteTransferNotificationRegistration"></a>
# **deleteTransferNotificationRegistration**
> Accountregistration171Wrapper deleteTransferNotificationRegistration(partnerId, accountRegRef)

This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 

This service allows Mastercard Merchant QR originating and receiving partners to delete a registered PAN for notifications. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransferNotificationRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TransferNotificationRegistrationApi apiInstance = new TransferNotificationRegistrationApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    String accountRegRef = "areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF"; // String | Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40
    try {
      Accountregistration171Wrapper result = apiInstance.deleteTransferNotificationRegistration(partnerId, accountRegRef);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransferNotificationRegistrationApi#deleteTransferNotificationRegistration");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | |
| **accountRegRef** | **String**| Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40 | |

### Return type

[**Accountregistration171Wrapper**](Accountregistration171Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

<a id="notificationRegistrationAPIReadBy"></a>
# **notificationRegistrationAPIReadBy**
> Accountregistration172Wrapper notificationRegistrationAPIReadBy(partnerId, accountRegRef)

This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 

This service allows Mastercard Merchant QR originating and receiving partners to retrieve the service provider&#39;s information for a registered PAN for notifications. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransferNotificationRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TransferNotificationRegistrationApi apiInstance = new TransferNotificationRegistrationApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    String accountRegRef = "areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF"; // String | Path Param - System generated unique account registration identifier. Type: Alphanumberic Special Length: 40
    try {
      Accountregistration172Wrapper result = apiInstance.notificationRegistrationAPIReadBy(partnerId, accountRegRef);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransferNotificationRegistrationApi#notificationRegistrationAPIReadBy");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | |
| **accountRegRef** | **String**| Path Param - System generated unique account registration identifier. Type: Alphanumberic Special Length: 40 | |

### Return type

[**Accountregistration172Wrapper**](Accountregistration172Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

<a id="notificationRegistrationAPIUpdate"></a>
# **notificationRegistrationAPIUpdate**
> Accountregistration170Wrapper notificationRegistrationAPIUpdate(partnerId, accountRegRef, accountregistration)

This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.

This service allows Mastercard Merchant QR originating and receiving partners to update the notitification service provider for a registered PAN.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TransferNotificationRegistrationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    TransferNotificationRegistrationApi apiInstance = new TransferNotificationRegistrationApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40
    String accountRegRef = "areg_GDVUiwh1bXzA_xVdDXn4ctJEKOF"; // String | Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40
    Accountregistration169Wrapper accountregistration = new Accountregistration169Wrapper(); // Accountregistration169Wrapper | Contains the details of the request message.
    try {
      Accountregistration170Wrapper result = apiInstance.notificationRegistrationAPIUpdate(partnerId, accountRegRef, accountregistration);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TransferNotificationRegistrationApi#notificationRegistrationAPIUpdate");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Type: Alphanumeric Special Length: 40 | |
| **accountRegRef** | **String**| Path Param - System generated unique account registration identifier. Type: Alphanumeric Special Length: 40 | |
| **accountregistration** | [**Accountregistration169Wrapper**](Accountregistration169Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**Accountregistration170Wrapper**](Accountregistration170Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details |  -  |

