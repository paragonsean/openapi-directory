# ECommerceApi

All URIs are relative to *https://neutrinoapi.net*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**bINListDownload**](ECommerceApi.md#bINListDownload) | **GET** /bin-list-download | BIN List Download |
| [**bINLookup**](ECommerceApi.md#bINLookup) | **GET** /bin-lookup | BIN Lookup |
| [**convert**](ECommerceApi.md#convert) | **GET** /convert | Convert |


<a id="bINListDownload"></a>
# **bINListDownload**
> File bINListDownload(includeIso3, include8digit)

BIN List Download

Download our entire BIN database for direct use on your own systems

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ECommerceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ECommerceApi apiInstance = new ECommerceApi(defaultClient);
    Boolean includeIso3 = false; // Boolean | Include ISO 3-letter country codes and ISO 3-letter currency codes in the data. These will be added to columns 10 and 11 respectively
    Boolean include8digit = false; // Boolean | Include 8-digit and higher BIN codes. This option includes all 6-digit BINs and all 8-digit and higher BINs (including some 9, 10 and 11 digit BINs where available)
    try {
      File result = apiInstance.bINListDownload(includeIso3, include8digit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ECommerceApi#bINListDownload");
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
| **includeIso3** | **Boolean**| Include ISO 3-letter country codes and ISO 3-letter currency codes in the data. These will be added to columns 10 and 11 respectively | [optional] [default to false] |
| **include8digit** | **Boolean**| Include 8-digit and higher BIN codes. This option includes all 6-digit BINs and all 8-digit and higher BINs (including some 9, 10 and 11 digit BINs where available) | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="bINLookup"></a>
# **bINLookup**
> BINLookupResponse bINLookup(binNumber, customerIp)

BIN Lookup

Perform a BIN (Bank Identification Number) or IIN (Issuer Identification Number) lookup

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ECommerceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ECommerceApi apiInstance = new ECommerceApi(defaultClient);
    String binNumber = "binNumber_example"; // String | The BIN or IIN number. This is the first 6, 8 or 10 digits of a card number, use 8 (or more) digits for the highest level of accuracy
    String customerIp = "customerIp_example"; // String | Pass in the customers IP address and we will return some extra information about them
    try {
      BINLookupResponse result = apiInstance.bINLookup(binNumber, customerIp);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ECommerceApi#bINLookup");
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
| **binNumber** | **String**| The BIN or IIN number. This is the first 6, 8 or 10 digits of a card number, use 8 (or more) digits for the highest level of accuracy | |
| **customerIp** | **String**| Pass in the customers IP address and we will return some extra information about them | [optional] |

### Return type

[**BINLookupResponse**](BINLookupResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

<a id="convert"></a>
# **convert**
> ConvertResponse convert(fromValue, fromType, toType)

Convert

A currency and unit conversion tool

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ECommerceApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://neutrinoapi.net");
    
    // Configure API key authorization: api-key
    ApiKeyAuth api-key = (ApiKeyAuth) defaultClient.getAuthentication("api-key");
    api-key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api-key.setApiKeyPrefix("Token");

    // Configure API key authorization: user-id
    ApiKeyAuth user-id = (ApiKeyAuth) defaultClient.getAuthentication("user-id");
    user-id.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user-id.setApiKeyPrefix("Token");

    ECommerceApi apiInstance = new ECommerceApi(defaultClient);
    String fromValue = "fromValue_example"; // String | The value to convert from (e.g. 10.95)
    String fromType = "fromType_example"; // String | The type of the value to convert from (e.g. USD)
    String toType = "toType_example"; // String | The type to convert to (e.g. EUR)
    try {
      ConvertResponse result = apiInstance.convert(fromValue, fromType, toType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ECommerceApi#convert");
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
| **fromValue** | **String**| The value to convert from (e.g. 10.95) | |
| **fromType** | **String**| The type of the value to convert from (e.g. USD) | |
| **toType** | **String**| The type to convert to (e.g. EUR) | |

### Return type

[**ConvertResponse**](ConvertResponse.md)

### Authorization

[api-key](../README.md#api-key), [user-id](../README.md#user-id)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **400** | Your API request has been rejected. Check error code for details |  -  |
| **403** | You have failed to authenticate |  -  |
| **500** | We messed up, sorry! Your request has caused a fatal exception |  -  |
| **0** | We messed up, sorry! Your request has caused an error |  -  |

