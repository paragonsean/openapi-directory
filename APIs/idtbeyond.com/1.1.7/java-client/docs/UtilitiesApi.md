# UtilitiesApi

All URIs are relative to *https://api.idtbeyond.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**iatuNumberValidatorGet**](UtilitiesApi.md#iatuNumberValidatorGet) | **GET** /iatu/number-validator | Mobile number validation |
| [**iatuProductsPromotionsGet**](UtilitiesApi.md#iatuProductsPromotionsGet) | **GET** /iatu/products/promotions | Current promotions |
| [**statusGet**](UtilitiesApi.md#statusGet) | **GET** /status | Status check |


<a id="iatuNumberValidatorGet"></a>
# **iatuNumberValidatorGet**
> iatuNumberValidatorGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, mobileNumber)

Mobile number validation

Checks to verify if the phone number is valid for the country supplied.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    String countryCode = "BR"; // String | 2-digit code of the country in ISO 3166 format. 'BR'
    String mobileNumber = "5521983115555"; // String | The mobile number you would like to validate. '5521983115555'
    try {
      apiInstance.iatuNumberValidatorGet(xIdtBeyondAppId, xIdtBeyondAppKey, countryCode, mobileNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#iatuNumberValidatorGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |
| **countryCode** | **String**| 2-digit code of the country in ISO 3166 format. &#39;BR&#39; | [default to BR] |
| **mobileNumber** | **String**| The mobile number you would like to validate. &#39;5521983115555&#39; | [default to 5521983115555] |

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
| **200** | Local value response |  -  |

<a id="iatuProductsPromotionsGet"></a>
# **iatuProductsPromotionsGet**
> iatuProductsPromotionsGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Current promotions

Returns a JSON of the current promotions.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    try {
      apiInstance.iatuProductsPromotionsGet(xIdtBeyondAppId, xIdtBeyondAppKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#iatuProductsPromotionsGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |

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
| **200** | Successful Promotions JSON response |  -  |

<a id="statusGet"></a>
# **statusGet**
> statusGet(xIdtBeyondAppId, xIdtBeyondAppKey)

Status check

Returns a JSON of the API status.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.UtilitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.idtbeyond.com/v1");

    UtilitiesApi apiInstance = new UtilitiesApi(defaultClient);
    String xIdtBeyondAppId = "APP_ID"; // String | Application ID you would like to use
    String xIdtBeyondAppKey = "APP_KEY"; // String | Application KEY you would like to use
    try {
      apiInstance.statusGet(xIdtBeyondAppId, xIdtBeyondAppKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling UtilitiesApi#statusGet");
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
| **xIdtBeyondAppId** | **String**| Application ID you would like to use | [default to APP_ID] |
| **xIdtBeyondAppKey** | **String**| Application KEY you would like to use | [default to APP_KEY] |

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
| **200** | Successful status JSON response |  -  |

