# FinanceApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiFinanceCountriesGet**](FinanceApi.md#apiFinanceCountriesGet) | **GET** /api/Finance/Countries | Get available countries |
| [**apiFinanceCryptoAddressGet**](FinanceApi.md#apiFinanceCryptoAddressGet) | **GET** /api/Finance/CryptoAddress | Get crypto address |
| [**apiFinanceCryptoAddressTypesGet**](FinanceApi.md#apiFinanceCryptoAddressTypesGet) | **GET** /api/Finance/CryptoAddress/Types | Get available crypto types |
| [**apiFinanceIbanCountryCodeGet**](FinanceApi.md#apiFinanceIbanCountryCodeGet) | **GET** /api/Finance/Iban/{countryCode} | Get IBAN by countryCode |
| [**apiFinanceVatValidatorPost**](FinanceApi.md#apiFinanceVatValidatorPost) | **POST** /api/Finance/Vat/Validator |  |


<a id="apiFinanceCountriesGet"></a>
# **apiFinanceCountriesGet**
> apiFinanceCountriesGet(xApiKey)

Get available countries

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FinanceApi apiInstance = new FinanceApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiFinanceCountriesGet(xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinanceApi#apiFinanceCountriesGet");
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

<a id="apiFinanceCryptoAddressGet"></a>
# **apiFinanceCryptoAddressGet**
> apiFinanceCryptoAddressGet(cryptoType, xApiKey)

Get crypto address

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FinanceApi apiInstance = new FinanceApi(defaultClient);
    String cryptoType = "cryptoType_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiFinanceCryptoAddressGet(cryptoType, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinanceApi#apiFinanceCryptoAddressGet");
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
| **cryptoType** | **String**|  | [optional] |
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

<a id="apiFinanceCryptoAddressTypesGet"></a>
# **apiFinanceCryptoAddressTypesGet**
> apiFinanceCryptoAddressTypesGet(xApiKey)

Get available crypto types

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FinanceApi apiInstance = new FinanceApi(defaultClient);
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiFinanceCryptoAddressTypesGet(xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinanceApi#apiFinanceCryptoAddressTypesGet");
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

<a id="apiFinanceIbanCountryCodeGet"></a>
# **apiFinanceIbanCountryCodeGet**
> apiFinanceIbanCountryCodeGet(countryCode, xApiKey)

Get IBAN by countryCode

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FinanceApi apiInstance = new FinanceApi(defaultClient);
    String countryCode = "countryCode_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiFinanceIbanCountryCodeGet(countryCode, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinanceApi#apiFinanceIbanCountryCodeGet");
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

<a id="apiFinanceVatValidatorPost"></a>
# **apiFinanceVatValidatorPost**
> apiFinanceVatValidatorPost(country, vat, xApiKey)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FinanceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    FinanceApi apiInstance = new FinanceApi(defaultClient);
    String country = "country_example"; // String | 
    String vat = "vat_example"; // String | 
    String xApiKey = "xApiKey_example"; // String | Enter your key
    try {
      apiInstance.apiFinanceVatValidatorPost(country, vat, xApiKey);
    } catch (ApiException e) {
      System.err.println("Exception when calling FinanceApi#apiFinanceVatValidatorPost");
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
| **country** | **String**|  | |
| **vat** | **String**|  | |
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

