# IbanapiApi

All URIs are relative to *https://api.ibanapi.com/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getBalance**](IbanapiApi.md#getBalance) | **GET** /balance | Get Account Balance |
| [**validateIBAN**](IbanapiApi.md#validateIBAN) | **GET** /validate | Validate IBAN |
| [**validateIBANBasic**](IbanapiApi.md#validateIBANBasic) | **GET** /validate-basic | Validate IBAN Basic |


<a id="getBalance"></a>
# **getBalance**
> BalanceResponse getBalance()

Get Account Balance

Returns the account balance and expiry

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IbanapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ibanapi.com/v1");
    
    // Configure API key authorization: api_key_security
    ApiKeyAuth api_key_security = (ApiKeyAuth) defaultClient.getAuthentication("api_key_security");
    api_key_security.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key_security.setApiKeyPrefix("Token");

    IbanapiApi apiInstance = new IbanapiApi(defaultClient);
    try {
      BalanceResponse result = apiInstance.getBalance();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IbanapiApi#getBalance");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BalanceResponse**](BalanceResponse.md)

### Authorization

[api_key_security](../README.md#api_key_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | SUCCESS |  -  |
| **400** | Your balance is exhausted or bad request |  -  |
| **401** | Package expired or account was blocked |  -  |
| **403** | Invalid API Key |  -  |
| **422** | API key is missing |  -  |

<a id="validateIBAN"></a>
# **validateIBAN**
> IBANResult validateIBAN(iban)

Validate IBAN

Returns the validation results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IbanapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ibanapi.com/v1");
    
    // Configure API key authorization: api_key_security
    ApiKeyAuth api_key_security = (ApiKeyAuth) defaultClient.getAuthentication("api_key_security");
    api_key_security.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key_security.setApiKeyPrefix("Token");

    IbanapiApi apiInstance = new IbanapiApi(defaultClient);
    String iban = "iban_example"; // String | The IBAN
    try {
      IBANResult result = apiInstance.validateIBAN(iban);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IbanapiApi#validateIBAN");
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
| **iban** | **String**| The IBAN | |

### Return type

[**IBANResult**](IBANResult.md)

### Authorization

[api_key_security](../README.md#api_key_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid IBAN response |  -  |
| **400** | Your balance is exhausted or bad request |  -  |
| **401** | Package expired or account was blocked |  -  |
| **403** | Invalid API Key |  -  |
| **422** | API key is missing |  -  |

<a id="validateIBANBasic"></a>
# **validateIBANBasic**
> IBANResultBasic validateIBANBasic(iban)

Validate IBAN Basic

Returns the basic validation results

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.IbanapiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ibanapi.com/v1");
    
    // Configure API key authorization: api_key_security
    ApiKeyAuth api_key_security = (ApiKeyAuth) defaultClient.getAuthentication("api_key_security");
    api_key_security.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key_security.setApiKeyPrefix("Token");

    IbanapiApi apiInstance = new IbanapiApi(defaultClient);
    String iban = "iban_example"; // String | The IBAN
    try {
      IBANResultBasic result = apiInstance.validateIBANBasic(iban);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling IbanapiApi#validateIBANBasic");
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
| **iban** | **String**| The IBAN | |

### Return type

[**IBANResultBasic**](IBANResultBasic.md)

### Authorization

[api_key_security](../README.md#api_key_security)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Valid IBAN response |  -  |
| **400** | Your balance is exhausted or bad request |  -  |
| **401** | Package expired or account was blocked |  -  |
| **403** | Invalid API Key |  -  |
| **422** | API key is missing |  -  |

