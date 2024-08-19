# Class2TryOtherInputFormatEndpointsApi

All URIs are relative to *https://api.taggun.io*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**postApiReceiptV1SimpleEncoded**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1SimpleEncoded) | **POST** /api/receipt/v1/simple/encoded | transcribe a receipt using base64 encoded image in json payload |
| [**postApiReceiptV1SimpleUrl**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1SimpleUrl) | **POST** /api/receipt/v1/simple/url | transcribe a receipt from URL |
| [**postApiReceiptV1VerboseEncoded**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1VerboseEncoded) | **POST** /api/receipt/v1/verbose/encoded | transcribe a receipt using base64 encoded image in json payload and return detailed result |
| [**postApiReceiptV1VerboseUrl**](Class2TryOtherInputFormatEndpointsApi.md#postApiReceiptV1VerboseUrl) | **POST** /api/receipt/v1/verbose/url | transcribe a receipt from URL and return detailed result |


<a id="postApiReceiptV1SimpleEncoded"></a>
# **postApiReceiptV1SimpleEncoded**
> ReceiptResult postApiReceiptV1SimpleEncoded(apikey, body)

transcribe a receipt using base64 encoded image in json payload

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2TryOtherInputFormatEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class2TryOtherInputFormatEndpointsApi apiInstance = new Class2TryOtherInputFormatEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    JsonPayload body = new JsonPayload(); // JsonPayload | 
    try {
      ReceiptResult result = apiInstance.postApiReceiptV1SimpleEncoded(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2TryOtherInputFormatEndpointsApi#postApiReceiptV1SimpleEncoded");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**JsonPayload**](JsonPayload.md)|  | [optional] |

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiReceiptV1SimpleUrl"></a>
# **postApiReceiptV1SimpleUrl**
> ReceiptResult postApiReceiptV1SimpleUrl(apikey, body)

transcribe a receipt from URL

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2TryOtherInputFormatEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class2TryOtherInputFormatEndpointsApi apiInstance = new Class2TryOtherInputFormatEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    UrlPayload body = new UrlPayload(); // UrlPayload | 
    try {
      ReceiptResult result = apiInstance.postApiReceiptV1SimpleUrl(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2TryOtherInputFormatEndpointsApi#postApiReceiptV1SimpleUrl");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**UrlPayload**](UrlPayload.md)|  | [optional] |

### Return type

[**ReceiptResult**](ReceiptResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiReceiptV1VerboseEncoded"></a>
# **postApiReceiptV1VerboseEncoded**
> ReceiptVerboseResult postApiReceiptV1VerboseEncoded(apikey, body)

transcribe a receipt using base64 encoded image in json payload and return detailed result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2TryOtherInputFormatEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class2TryOtherInputFormatEndpointsApi apiInstance = new Class2TryOtherInputFormatEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    JsonPayload body = new JsonPayload(); // JsonPayload | 
    try {
      ReceiptVerboseResult result = apiInstance.postApiReceiptV1VerboseEncoded(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2TryOtherInputFormatEndpointsApi#postApiReceiptV1VerboseEncoded");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**JsonPayload**](JsonPayload.md)|  | [optional] |

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

<a id="postApiReceiptV1VerboseUrl"></a>
# **postApiReceiptV1VerboseUrl**
> ReceiptVerboseResult postApiReceiptV1VerboseUrl(apikey, body)

transcribe a receipt from URL and return detailed result

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.Class2TryOtherInputFormatEndpointsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.taggun.io");

    Class2TryOtherInputFormatEndpointsApi apiInstance = new Class2TryOtherInputFormatEndpointsApi(defaultClient);
    String apikey = "apikey_example"; // String | API authentication key.
    UrlPayload body = new UrlPayload(); // UrlPayload | 
    try {
      ReceiptVerboseResult result = apiInstance.postApiReceiptV1VerboseUrl(apikey, body);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling Class2TryOtherInputFormatEndpointsApi#postApiReceiptV1VerboseUrl");
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
| **apikey** | **String**| API authentication key. | |
| **body** | [**UrlPayload**](UrlPayload.md)|  | [optional] |

### Return type

[**ReceiptVerboseResult**](ReceiptVerboseResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Bad Request |  -  |

