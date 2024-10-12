# PhoneApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiPhoneCountriesGet**](PhoneApi.md#apiPhoneCountriesGet) | **GET** /api/Phone/Countries | Get available countries |
| [**apiPhoneGenerateGet**](PhoneApi.md#apiPhoneGenerateGet) | **GET** /api/Phone/Generate | Get bulk telephone numbers for a country |
| [**apiPhoneIMEIGet**](PhoneApi.md#apiPhoneIMEIGet) | **GET** /api/Phone/IMEI | Get bulk imeis |
| [**apiPhoneValidateGet**](PhoneApi.md#apiPhoneValidateGet) | **GET** /api/Phone/Validate | Validate a phone number |


<a id="apiPhoneCountriesGet"></a>
# **apiPhoneCountriesGet**
> apiPhoneCountriesGet(xApiKey)

Get available countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PhoneApi apiInstance = new PhoneApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiPhoneCountriesGet(xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneApi#apiPhoneCountriesGet");
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
| **xApiKey** | **String**| Enter your key | [optional] |

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
| **200** | Success |  -  |

<a id="apiPhoneGenerateGet"></a>
# **apiPhoneGenerateGet**
> apiPhoneGenerateGet(countryCode, quantity, xApiKey)

Get bulk telephone numbers for a country

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PhoneApi apiInstance = new PhoneApi(defaultClient);
    String countryCode = "countryCode_example"; // String | 
    Integer quantity = 56; // Integer | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiPhoneGenerateGet(countryCode, quantity, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneApi#apiPhoneGenerateGet");
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
| **countryCode** | **String**|  | |
| **quantity** | **Integer**|  | |
| **xApiKey** | **String**| Enter your key | [optional] |

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
| **200** | Success |  -  |

<a id="apiPhoneIMEIGet"></a>
# **apiPhoneIMEIGet**
> apiPhoneIMEIGet(quantity, xApiKey)

Get bulk imeis

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PhoneApi apiInstance = new PhoneApi(defaultClient);
    Integer quantity = 56; // Integer | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiPhoneIMEIGet(quantity, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneApi#apiPhoneIMEIGet");
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
| **quantity** | **Integer**|  | |
| **xApiKey** | **String**| Enter your key | [optional] |

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
| **200** | Success |  -  |

<a id="apiPhoneValidateGet"></a>
# **apiPhoneValidateGet**
> apiPhoneValidateGet(telephone, countryCode, xApiKey)

Validate a phone number

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PhoneApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    PhoneApi apiInstance = new PhoneApi(defaultClient);
    String telephone = "telephone_example"; // String | 
    String countryCode = "countryCode_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiPhoneValidateGet(telephone, countryCode, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling PhoneApi#apiPhoneValidateGet");
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
| **telephone** | **String**|  | |
| **countryCode** | **String**|  | [optional] |
| **xApiKey** | **String**| Enter your key | [optional] |

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
| **200** | Success |  -  |

