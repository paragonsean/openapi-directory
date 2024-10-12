# SubscriptionIpnRequestsApi

All URIs are relative to *https://eu.eth.chaingateway.io/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listFailedIPNs**](SubscriptionIpnRequestsApi.md#listFailedIPNs) | **POST** /listFailedIPNs | listFailedIPNs |
| [**listSubscribedAddresses**](SubscriptionIpnRequestsApi.md#listSubscribedAddresses) | **POST** /listSubscribedAddresses | listSubscribedAddresses |
| [**resendFailedIPN**](SubscriptionIpnRequestsApi.md#resendFailedIPN) | **POST** /resendFailedIPN | resendFailedIPN |
| [**subscribeAddress**](SubscriptionIpnRequestsApi.md#subscribeAddress) | **POST** /subscribeAddress | subscribeAddress |
| [**unsubscribeAddress**](SubscriptionIpnRequestsApi.md#unsubscribeAddress) | **POST** /unsubscribeAddress | unsubscribeAddress |


<a id="listFailedIPNs"></a>
# **listFailedIPNs**
> ListFailedIPNs listFailedIPNs(contentType, authorization)

listFailedIPNs

Returns all subscriptions/IPNs created with an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionIpnRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    SubscriptionIpnRequestsApi apiInstance = new SubscriptionIpnRequestsApi(defaultClient);
    String contentType = "application/json"; // String | 
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    try {
      ListFailedIPNs result = apiInstance.listFailedIPNs(contentType, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionIpnRequestsApi#listFailedIPNs");
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
| **authorization** | **String**| API Key | |

### Return type

[**ListFailedIPNs**](ListFailedIPNs.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="listSubscribedAddresses"></a>
# **listSubscribedAddresses**
> ListSubscribedAddresses listSubscribedAddresses(contentType, authorization)

listSubscribedAddresses

Returns all subscriptions/IPNs created with an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionIpnRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    SubscriptionIpnRequestsApi apiInstance = new SubscriptionIpnRequestsApi(defaultClient);
    String contentType = "application/json"; // String | 
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    try {
      ListSubscribedAddresses result = apiInstance.listSubscribedAddresses(contentType, authorization);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionIpnRequestsApi#listSubscribedAddresses");
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
| **authorization** | **String**| API Key | |

### Return type

[**ListSubscribedAddresses**](ListSubscribedAddresses.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="resendFailedIPN"></a>
# **resendFailedIPN**
> ResendFailedIPN resendFailedIPN(authorization, resendFailedIPNRequest)

resendFailedIPN

Returns all subscriptions/IPNs created with an account.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionIpnRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    SubscriptionIpnRequestsApi apiInstance = new SubscriptionIpnRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    ResendFailedIPNRequest resendFailedIPNRequest = new ResendFailedIPNRequest(); // ResendFailedIPNRequest | 
    try {
      ResendFailedIPN result = apiInstance.resendFailedIPN(authorization, resendFailedIPNRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionIpnRequestsApi#resendFailedIPN");
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
| **authorization** | **String**| API Key | |
| **resendFailedIPNRequest** | [**ResendFailedIPNRequest**](ResendFailedIPNRequest.md)|  | |

### Return type

[**ResendFailedIPN**](ResendFailedIPN.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="subscribeAddress"></a>
# **subscribeAddress**
> SubscribeAddress subscribeAddress(authorization, subscribeAddressRequest)

subscribeAddress

Creates a new subscription/IPN for the given address (and contractaddress). You will receive a notification to the given url every time a deposit is received. Unsubscribe the address before sending tokens/ETH from it or you won&#39;t get reliable notifications anymore.  

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionIpnRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    SubscriptionIpnRequestsApi apiInstance = new SubscriptionIpnRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    SubscribeAddressRequest subscribeAddressRequest = new SubscribeAddressRequest(); // SubscribeAddressRequest | 
    try {
      SubscribeAddress result = apiInstance.subscribeAddress(authorization, subscribeAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionIpnRequestsApi#subscribeAddress");
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
| **authorization** | **String**| API Key | |
| **subscribeAddressRequest** | [**SubscribeAddressRequest**](SubscribeAddressRequest.md)|  | |

### Return type

[**SubscribeAddress**](SubscribeAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="unsubscribeAddress"></a>
# **unsubscribeAddress**
> UnsubscribeAddress unsubscribeAddress(authorization, unsubscribeAddressRequest)

unsubscribeAddress

Deletes an existing subscription/IPN for the given address (and contractaddress).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionIpnRequestsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://eu.eth.chaingateway.io/v1");

    SubscriptionIpnRequestsApi apiInstance = new SubscriptionIpnRequestsApi(defaultClient);
    String authorization = "q9PdaWuD4j6DK6vsUgehhL8pgarSrS9m"; // String | API Key
    UnsubscribeAddressRequest unsubscribeAddressRequest = new UnsubscribeAddressRequest(); // UnsubscribeAddressRequest | 
    try {
      UnsubscribeAddress result = apiInstance.unsubscribeAddress(authorization, unsubscribeAddressRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionIpnRequestsApi#unsubscribeAddress");
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
| **authorization** | **String**| API Key | |
| **unsubscribeAddressRequest** | [**UnsubscribeAddressRequest**](UnsubscribeAddressRequest.md)|  | |

### Return type

[**UnsubscribeAddress**](UnsubscribeAddress.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

