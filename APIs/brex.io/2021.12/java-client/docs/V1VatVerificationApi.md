# V1VatVerificationApi

All URIs are relative to *https://api.kompany.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vatBasic**](V1VatVerificationApi.md#vatBasic) | **POST** /api/v1/vat-verification/basic-check/{country} | Returns a verification result |
| [**vatComprehensive**](V1VatVerificationApi.md#vatComprehensive) | **POST** /api/v1/vat-verification/comprehensive-check/{country} | Returns a verification result and company data |
| [**vatLevelTwo**](V1VatVerificationApi.md#vatLevelTwo) | **POST** /api/v1/vat-verification/leveltwo-check/{country} | Returns a level two verification result |
| [**vatLookup**](V1VatVerificationApi.md#vatLookup) | **POST** /api/v1/vat-verification/lookup/{country} | Returns a list of vat numbers with additional data |


<a id="vatBasic"></a>
# **vatBasic**
> VatBasic200Response vatBasic(country, vatNumber, companyAddress, companyName, companyNumber)

Returns a verification result

Basic verification of given VAT number against VIES. Optional parameters may help to build a better confidence score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1VatVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1VatVerificationApi apiInstance = new V1VatVerificationApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String vatNumber = "vatNumber_example"; // String | VAT number to validate
    String companyAddress = "companyAddress_example"; // String | company address lines
    String companyName = "companyName_example"; // String | Company name
    String companyNumber = "companyNumber_example"; // String | official company number
    try {
      VatBasic200Response result = apiInstance.vatBasic(country, vatNumber, companyAddress, companyName, companyNumber);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1VatVerificationApi#vatBasic");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **vatNumber** | **String**| VAT number to validate | |
| **companyAddress** | **String**| company address lines | [optional] |
| **companyName** | **String**| Company name | [optional] |
| **companyNumber** | **String**| official company number | [optional] |

### Return type

[**VatBasic200Response**](VatBasic200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Denotes validity of checked VAT |  -  |
| **0** |  |  -  |

<a id="vatComprehensive"></a>
# **vatComprehensive**
> vatComprehensive(country, vatNumber, companyAddress, companyName, companyNumber)

Returns a verification result and company data

Extended verification of given VAT number against VIES. Optional parameters may help to build a better confidence score.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1VatVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1VatVerificationApi apiInstance = new V1VatVerificationApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String vatNumber = "vatNumber_example"; // String | VAT number to validate
    String companyAddress = "companyAddress_example"; // String | company address lines
    String companyName = "companyName_example"; // String | Company name
    String companyNumber = "companyNumber_example"; // String | official company number
    try {
      apiInstance.vatComprehensive(country, vatNumber, companyAddress, companyName, companyNumber);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1VatVerificationApi#vatComprehensive");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **vatNumber** | **String**| VAT number to validate | |
| **companyAddress** | **String**| company address lines | [optional] |
| **companyName** | **String**| Company name | [optional] |
| **companyNumber** | **String**| official company number | [optional] |

### Return type

null (empty response body)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |
| **0** |  |  -  |

<a id="vatLevelTwo"></a>
# **vatLevelTwo**
> VatLevelTwo200Response vatLevelTwo(country, vatNumber, confirmation)

Returns a level two verification result

Second Level Verification of VAT number against BMF Austria. Optional confirmation parameter can be provided to order a Confirmation Report.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1VatVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1VatVerificationApi apiInstance = new V1VatVerificationApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String vatNumber = "vatNumber_example"; // String | VAT number to validate
    Boolean confirmation = true; // Boolean | If a confirmation document should be ordered
    try {
      VatLevelTwo200Response result = apiInstance.vatLevelTwo(country, vatNumber, confirmation);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1VatVerificationApi#vatLevelTwo");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **vatNumber** | **String**| VAT number to validate | |
| **confirmation** | **Boolean**| If a confirmation document should be ordered | [optional] |

### Return type

[**VatLevelTwo200Response**](VatLevelTwo200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Denotes second level validity result of checked VAT |  -  |
| **0** |  |  -  |

<a id="vatLookup"></a>
# **vatLookup**
> VatLookup200Response vatLookup(country, name, address)

Returns a list of vat numbers with additional data

Reverse VAT Lookup: Search for companies and their VAT numbers by company name. Search is forwarded to a provider.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1VatVerificationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.kompany.com");
    
    // Configure API key authorization: user_key
    ApiKeyAuth user_key = (ApiKeyAuth) defaultClient.getAuthentication("user_key");
    user_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //user_key.setApiKeyPrefix("Token");

    V1VatVerificationApi apiInstance = new V1VatVerificationApi(defaultClient);
    String country = "country_example"; // String | ISO_3166-1_alpha-2 representation of a country name - 2 chars
    String name = "name_example"; // String | Company name
    String address = "address_example"; // String | Company address
    try {
      VatLookup200Response result = apiInstance.vatLookup(country, name, address);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1VatVerificationApi#vatLookup");
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
| **country** | **String**| ISO_3166-1_alpha-2 representation of a country name - 2 chars | |
| **name** | **String**| Company name | |
| **address** | **String**| Company address | [optional] |

### Return type

[**VatLookup200Response**](VatLookup200Response.md)

### Authorization

[user_key](../README.md#user_key)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Result of a VAT number reverse Lookup |  -  |
| **0** |  |  -  |

