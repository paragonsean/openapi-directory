# TerminalApi

All URIs are relative to *https://connect.squareup.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**cancelTerminalCheckout**](TerminalApi.md#cancelTerminalCheckout) | **POST** /v2/terminals/checkouts/{checkout_id}/cancel | CancelTerminalCheckout |
| [**cancelTerminalRefund**](TerminalApi.md#cancelTerminalRefund) | **POST** /v2/terminals/refunds/{terminal_refund_id}/cancel | CancelTerminalRefund |
| [**createTerminalCheckout**](TerminalApi.md#createTerminalCheckout) | **POST** /v2/terminals/checkouts | CreateTerminalCheckout |
| [**createTerminalRefund**](TerminalApi.md#createTerminalRefund) | **POST** /v2/terminals/refunds | CreateTerminalRefund |
| [**getTerminalCheckout**](TerminalApi.md#getTerminalCheckout) | **GET** /v2/terminals/checkouts/{checkout_id} | GetTerminalCheckout |
| [**getTerminalRefund**](TerminalApi.md#getTerminalRefund) | **GET** /v2/terminals/refunds/{terminal_refund_id} | GetTerminalRefund |
| [**searchTerminalCheckouts**](TerminalApi.md#searchTerminalCheckouts) | **POST** /v2/terminals/checkouts/search | SearchTerminalCheckouts |
| [**searchTerminalRefunds**](TerminalApi.md#searchTerminalRefunds) | **POST** /v2/terminals/refunds/search | SearchTerminalRefunds |


<a id="cancelTerminalCheckout"></a>
# **cancelTerminalCheckout**
> CancelTerminalCheckoutResponse cancelTerminalCheckout(checkoutId)

CancelTerminalCheckout

Cancels a Terminal checkout request if the status of the request permits it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    String checkoutId = "checkoutId_example"; // String | The unique ID for the desired `TerminalCheckout`.
    try {
      CancelTerminalCheckoutResponse result = apiInstance.cancelTerminalCheckout(checkoutId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#cancelTerminalCheckout");
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
| **checkoutId** | **String**| The unique ID for the desired &#x60;TerminalCheckout&#x60;. | |

### Return type

[**CancelTerminalCheckoutResponse**](CancelTerminalCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="cancelTerminalRefund"></a>
# **cancelTerminalRefund**
> CancelTerminalRefundResponse cancelTerminalRefund(terminalRefundId)

CancelTerminalRefund

Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    String terminalRefundId = "terminalRefundId_example"; // String | The unique ID for the desired `TerminalRefund`.
    try {
      CancelTerminalRefundResponse result = apiInstance.cancelTerminalRefund(terminalRefundId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#cancelTerminalRefund");
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
| **terminalRefundId** | **String**| The unique ID for the desired &#x60;TerminalRefund&#x60;. | |

### Return type

[**CancelTerminalRefundResponse**](CancelTerminalRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createTerminalCheckout"></a>
# **createTerminalCheckout**
> CreateTerminalCheckoutResponse createTerminalCheckout(createTerminalCheckoutRequest)

CreateTerminalCheckout

Creates a Terminal checkout request and sends it to the specified device to take a payment for the requested amount.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    CreateTerminalCheckoutRequest createTerminalCheckoutRequest = new CreateTerminalCheckoutRequest(); // CreateTerminalCheckoutRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateTerminalCheckoutResponse result = apiInstance.createTerminalCheckout(createTerminalCheckoutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#createTerminalCheckout");
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
| **createTerminalCheckoutRequest** | [**CreateTerminalCheckoutRequest**](CreateTerminalCheckoutRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateTerminalCheckoutResponse**](CreateTerminalCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="createTerminalRefund"></a>
# **createTerminalRefund**
> CreateTerminalRefundResponse createTerminalRefund(createTerminalRefundRequest)

CreateTerminalRefund

Creates a request to refund an Interac payment completed on a Square Terminal.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    CreateTerminalRefundRequest createTerminalRefundRequest = new CreateTerminalRefundRequest(); // CreateTerminalRefundRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      CreateTerminalRefundResponse result = apiInstance.createTerminalRefund(createTerminalRefundRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#createTerminalRefund");
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
| **createTerminalRefundRequest** | [**CreateTerminalRefundRequest**](CreateTerminalRefundRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**CreateTerminalRefundResponse**](CreateTerminalRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getTerminalCheckout"></a>
# **getTerminalCheckout**
> GetTerminalCheckoutResponse getTerminalCheckout(checkoutId)

GetTerminalCheckout

Retrieves a Terminal checkout request by &#x60;checkout_id&#x60;.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    String checkoutId = "checkoutId_example"; // String | The unique ID for the desired `TerminalCheckout`.
    try {
      GetTerminalCheckoutResponse result = apiInstance.getTerminalCheckout(checkoutId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#getTerminalCheckout");
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
| **checkoutId** | **String**| The unique ID for the desired &#x60;TerminalCheckout&#x60;. | |

### Return type

[**GetTerminalCheckoutResponse**](GetTerminalCheckoutResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="getTerminalRefund"></a>
# **getTerminalRefund**
> GetTerminalRefundResponse getTerminalRefund(terminalRefundId)

GetTerminalRefund

Retrieves an Interac Terminal refund object by ID.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    String terminalRefundId = "terminalRefundId_example"; // String | The unique ID for the desired `TerminalRefund`.
    try {
      GetTerminalRefundResponse result = apiInstance.getTerminalRefund(terminalRefundId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#getTerminalRefund");
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
| **terminalRefundId** | **String**| The unique ID for the desired &#x60;TerminalRefund&#x60;. | |

### Return type

[**GetTerminalRefundResponse**](GetTerminalRefundResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="searchTerminalCheckouts"></a>
# **searchTerminalCheckouts**
> SearchTerminalCheckoutsResponse searchTerminalCheckouts(searchTerminalCheckoutsRequest)

SearchTerminalCheckouts

Retrieves a filtered list of Terminal checkout requests created by the account making the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    SearchTerminalCheckoutsRequest searchTerminalCheckoutsRequest = new SearchTerminalCheckoutsRequest(); // SearchTerminalCheckoutsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      SearchTerminalCheckoutsResponse result = apiInstance.searchTerminalCheckouts(searchTerminalCheckoutsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#searchTerminalCheckouts");
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
| **searchTerminalCheckoutsRequest** | [**SearchTerminalCheckoutsRequest**](SearchTerminalCheckoutsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**SearchTerminalCheckoutsResponse**](SearchTerminalCheckoutsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

<a id="searchTerminalRefunds"></a>
# **searchTerminalRefunds**
> SearchTerminalRefundsResponse searchTerminalRefunds(searchTerminalRefundsRequest)

SearchTerminalRefunds

Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.TerminalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://connect.squareup.com");
    
    // Configure OAuth2 access token for authorization: oauth2
    OAuth oauth2 = (OAuth) defaultClient.getAuthentication("oauth2");
    oauth2.setAccessToken("YOUR ACCESS TOKEN");

    TerminalApi apiInstance = new TerminalApi(defaultClient);
    SearchTerminalRefundsRequest searchTerminalRefundsRequest = new SearchTerminalRefundsRequest(); // SearchTerminalRefundsRequest | An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    try {
      SearchTerminalRefundsResponse result = apiInstance.searchTerminalRefunds(searchTerminalRefundsRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling TerminalApi#searchTerminalRefunds");
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
| **searchTerminalRefundsRequest** | [**SearchTerminalRefundsRequest**](SearchTerminalRefundsRequest.md)| An object containing the fields to POST for the request.  See the corresponding object definition for field details. | |

### Return type

[**SearchTerminalRefundsResponse**](SearchTerminalRefundsResponse.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

