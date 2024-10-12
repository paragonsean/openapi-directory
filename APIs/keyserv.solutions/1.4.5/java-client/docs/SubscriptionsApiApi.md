# SubscriptionsApiApi

All URIs are relative to *https://keyserv.solutions*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subscriptionsApiCount**](SubscriptionsApiApi.md#subscriptionsApiCount) | **POST** /v1/SubscriptionsApi/Count |  |
| [**subscriptionsApiDeleteSubscription**](SubscriptionsApiApi.md#subscriptionsApiDeleteSubscription) | **DELETE** /v1/SubscriptionsApi/{serial} |  |
| [**subscriptionsApiDeleteSubscription2**](SubscriptionsApiApi.md#subscriptionsApiDeleteSubscription2) | **POST** /v1/SubscriptionsApi/{serial} |  |
| [**subscriptionsApiDisable**](SubscriptionsApiApi.md#subscriptionsApiDisable) | **PATCH** /v1/SubscriptionsApi/Disable |  |
| [**subscriptionsApiDisable2**](SubscriptionsApiApi.md#subscriptionsApiDisable2) | **POST** /v1/SubscriptionsApi/Disable |  |
| [**subscriptionsApiEnable**](SubscriptionsApiApi.md#subscriptionsApiEnable) | **PATCH** /v1/SubscriptionsApi/Enable |  |
| [**subscriptionsApiEnable2**](SubscriptionsApiApi.md#subscriptionsApiEnable2) | **POST** /v1/SubscriptionsApi/Enable |  |
| [**subscriptionsApiFind**](SubscriptionsApiApi.md#subscriptionsApiFind) | **POST** /v1/SubscriptionsApi/Find |  |
| [**subscriptionsApiList**](SubscriptionsApiApi.md#subscriptionsApiList) | **POST** /v1/SubscriptionsApi/List |  |
| [**subscriptionsApiPutSubscription**](SubscriptionsApiApi.md#subscriptionsApiPutSubscription) | **PUT** /v1/SubscriptionsApi |  |
| [**subscriptionsApiPutSubscription2**](SubscriptionsApiApi.md#subscriptionsApiPutSubscription2) | **POST** /v1/SubscriptionsApi |  |
| [**subscriptionsApiSave**](SubscriptionsApiApi.md#subscriptionsApiSave) | **POST** /v1/SubscriptionsApi/Save |  |


<a id="subscriptionsApiCount"></a>
# **subscriptionsApiCount**
> ProductsApiCount200Response subscriptionsApiCount(subscriptionsApiCountRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    SubscriptionsApiCountRequest subscriptionsApiCountRequest = new SubscriptionsApiCountRequest(); // SubscriptionsApiCountRequest | 
    try {
      ProductsApiCount200Response result = apiInstance.subscriptionsApiCount(subscriptionsApiCountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiCount");
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
| **subscriptionsApiCountRequest** | [**SubscriptionsApiCountRequest**](SubscriptionsApiCountRequest.md)|  | |

### Return type

[**ProductsApiCount200Response**](ProductsApiCount200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="subscriptionsApiDeleteSubscription"></a>
# **subscriptionsApiDeleteSubscription**
> subscriptionsApiDeleteSubscription(xApiKey, serial, keep)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | 
    String serial = "serial_example"; // String | 
    Boolean keep = true; // Boolean | 
    try {
      apiInstance.subscriptionsApiDeleteSubscription(xApiKey, serial, keep);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiDeleteSubscription");
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
| **xApiKey** | **String**|  | |
| **serial** | **String**|  | |
| **keep** | **Boolean**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="subscriptionsApiDeleteSubscription2"></a>
# **subscriptionsApiDeleteSubscription2**
> subscriptionsApiDeleteSubscription2(xApiKey, serial, keep)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | 
    String serial = "serial_example"; // String | 
    Boolean keep = true; // Boolean | 
    try {
      apiInstance.subscriptionsApiDeleteSubscription2(xApiKey, serial, keep);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiDeleteSubscription2");
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
| **xApiKey** | **String**|  | |
| **serial** | **String**|  | |
| **keep** | **Boolean**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **204** |  |  -  |

<a id="subscriptionsApiDisable"></a>
# **subscriptionsApiDisable**
> subscriptionsApiDisable(productsApiFindRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    try {
      apiInstance.subscriptionsApiDisable(productsApiFindRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiDisable");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |

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
| **204** |  |  -  |

<a id="subscriptionsApiDisable2"></a>
# **subscriptionsApiDisable2**
> subscriptionsApiDisable2(productsApiFindRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    try {
      apiInstance.subscriptionsApiDisable2(productsApiFindRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiDisable2");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |

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
| **204** |  |  -  |

<a id="subscriptionsApiEnable"></a>
# **subscriptionsApiEnable**
> subscriptionsApiEnable(productsApiFindRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    try {
      apiInstance.subscriptionsApiEnable(productsApiFindRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiEnable");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |

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
| **204** |  |  -  |

<a id="subscriptionsApiEnable2"></a>
# **subscriptionsApiEnable2**
> subscriptionsApiEnable2(productsApiFindRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    try {
      apiInstance.subscriptionsApiEnable2(productsApiFindRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiEnable2");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |

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
| **204** |  |  -  |

<a id="subscriptionsApiFind"></a>
# **subscriptionsApiFind**
> SubscriptionsApiFind200Response subscriptionsApiFind(productsApiFindRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    try {
      SubscriptionsApiFind200Response result = apiInstance.subscriptionsApiFind(productsApiFindRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiFind");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |

### Return type

[**SubscriptionsApiFind200Response**](SubscriptionsApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="subscriptionsApiList"></a>
# **subscriptionsApiList**
> List&lt;SubscriptionView&gt; subscriptionsApiList(productsApiFindRequest, page)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    ProductsApiFindRequest productsApiFindRequest = new ProductsApiFindRequest(); // ProductsApiFindRequest | 
    Integer page = 56; // Integer | 
    try {
      List<SubscriptionView> result = apiInstance.subscriptionsApiList(productsApiFindRequest, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiList");
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
| **productsApiFindRequest** | [**ProductsApiFindRequest**](ProductsApiFindRequest.md)|  | |
| **page** | **Integer**|  | [optional] |

### Return type

[**List&lt;SubscriptionView&gt;**](SubscriptionView.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

<a id="subscriptionsApiPutSubscription"></a>
# **subscriptionsApiPutSubscription**
> subscriptionsApiPutSubscription(subscriptionsApiPutSubscriptionRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    SubscriptionsApiPutSubscriptionRequest subscriptionsApiPutSubscriptionRequest = new SubscriptionsApiPutSubscriptionRequest(); // SubscriptionsApiPutSubscriptionRequest | 
    try {
      apiInstance.subscriptionsApiPutSubscription(subscriptionsApiPutSubscriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiPutSubscription");
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
| **subscriptionsApiPutSubscriptionRequest** | [**SubscriptionsApiPutSubscriptionRequest**](SubscriptionsApiPutSubscriptionRequest.md)|  | |

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
| **204** |  |  -  |

<a id="subscriptionsApiPutSubscription2"></a>
# **subscriptionsApiPutSubscription2**
> subscriptionsApiPutSubscription2(subscriptionsApiPutSubscriptionRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    SubscriptionsApiPutSubscriptionRequest subscriptionsApiPutSubscriptionRequest = new SubscriptionsApiPutSubscriptionRequest(); // SubscriptionsApiPutSubscriptionRequest | 
    try {
      apiInstance.subscriptionsApiPutSubscription2(subscriptionsApiPutSubscriptionRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiPutSubscription2");
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
| **subscriptionsApiPutSubscriptionRequest** | [**SubscriptionsApiPutSubscriptionRequest**](SubscriptionsApiPutSubscriptionRequest.md)|  | |

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
| **204** |  |  -  |

<a id="subscriptionsApiSave"></a>
# **subscriptionsApiSave**
> KeysApiFind200Response subscriptionsApiSave(subscriptionsApiPutSubscriptionRequest)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubscriptionsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://keyserv.solutions");

    SubscriptionsApiApi apiInstance = new SubscriptionsApiApi(defaultClient);
    SubscriptionsApiPutSubscriptionRequest subscriptionsApiPutSubscriptionRequest = new SubscriptionsApiPutSubscriptionRequest(); // SubscriptionsApiPutSubscriptionRequest | 
    try {
      KeysApiFind200Response result = apiInstance.subscriptionsApiSave(subscriptionsApiPutSubscriptionRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubscriptionsApiApi#subscriptionsApiSave");
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
| **subscriptionsApiPutSubscriptionRequest** | [**SubscriptionsApiPutSubscriptionRequest**](SubscriptionsApiPutSubscriptionRequest.md)|  | |

### Return type

[**KeysApiFind200Response**](KeysApiFind200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **201** |  |  -  |

