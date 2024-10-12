# DefaultApi

All URIs are relative to *https://api.nexmo.com/ni*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getNumberInsightAdvanced**](DefaultApi.md#getNumberInsightAdvanced) | **GET** /advanced/{format} | Advanced Number Insight (sync) |
| [**getNumberInsightAsync**](DefaultApi.md#getNumberInsightAsync) | **GET** /advanced/async/{format} | Advanced Number Insight (async) |
| [**getNumberInsightBasic**](DefaultApi.md#getNumberInsightBasic) | **GET** /basic/{format} | Basic Number Insight |
| [**getNumberInsightStandard**](DefaultApi.md#getNumberInsightStandard) | **GET** /standard/{format} | Standard Number Insight |


<a id="getNumberInsightAdvanced"></a>
# **getNumberInsightAdvanced**
> GetNumberInsightAdvanced200Response getNumberInsightAdvanced(format, number, realTimeData, country, cnam, ip)

Advanced Number Insight (sync)

Provides [advanced number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number synchronously, in the same way that the basic and standard endpoints do.  Vonage recommends accessing the Advanced API **asynchronously** using the &#x60;/advanced/async&#x60; endpoint, to avoid timeouts.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/ni");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | The format of the response
    String number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
    Boolean realTimeData = true; // Boolean | A boolean to choose whether to get real time data back in the response.
    String country = "GB"; // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    Boolean cnam = false; // Boolean | Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
    String ip = "123.0.0.255"; // String | This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers. 
    try {
      GetNumberInsightAdvanced200Response result = apiInstance.getNumberInsightAdvanced(format, number, realTimeData, country, cnam, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNumberInsightAdvanced");
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
| **format** | **String**| The format of the response | [enum: json, xml] |
| **number** | **String**| A single phone number that you need insight about in national or international format. | |
| **realTimeData** | **Boolean**| A boolean to choose whether to get real time data back in the response. | [optional] |
| **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] |
| **cnam** | **Boolean**| Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge. | [optional] [default to false] |
| **ip** | **String**| This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers.  | [optional] |

### Return type

[**GetNumberInsightAdvanced200Response**](GetNumberInsightAdvanced200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getNumberInsightAsync"></a>
# **getNumberInsightAsync**
> GetNumberInsightAsync200Response getNumberInsightAsync(format, paramCallback, number, country, cnam, ip)

Advanced Number Insight (async)

Provides [advanced number insight](/number-insight/overview#basic-standard-and-advanced-apis) number information **asynchronously** using the URL specified in the &#x60;callback&#x60; parameter.  recommends asynchronous use of the Number Insight Advanced API, to avoid timeouts.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/ni");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | The format of the response
    String paramCallback = "https://example.com/callback"; // String | The callback URL
    String number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
    String country = "GB"; // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    Boolean cnam = false; // Boolean | Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
    String ip = "123.0.0.255"; // String | This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers. 
    try {
      GetNumberInsightAsync200Response result = apiInstance.getNumberInsightAsync(format, paramCallback, number, country, cnam, ip);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNumberInsightAsync");
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
| **format** | **String**| The format of the response | [enum: json, xml] |
| **paramCallback** | **String**| The callback URL | |
| **number** | **String**| A single phone number that you need insight about in national or international format. | |
| **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] |
| **cnam** | **Boolean**| Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge. | [optional] [default to false] |
| **ip** | **String**| This parameter is deprecated as we are no longer able to retrieve reliable IP data globally from carriers.  | [optional] |

### Return type

[**GetNumberInsightAsync200Response**](GetNumberInsightAsync200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getNumberInsightBasic"></a>
# **getNumberInsightBasic**
> NiResponseJsonBasic getNumberInsightBasic(format, number, country)

Basic Number Insight

Provides [basic number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/ni");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | The format of the response
    String number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
    String country = "GB"; // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    try {
      NiResponseJsonBasic result = apiInstance.getNumberInsightBasic(format, number, country);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNumberInsightBasic");
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
| **format** | **String**| The format of the response | [enum: json, xml] |
| **number** | **String**| A single phone number that you need insight about in national or international format. | |
| **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] |

### Return type

[**NiResponseJsonBasic**](NiResponseJsonBasic.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getNumberInsightStandard"></a>
# **getNumberInsightStandard**
> GetNumberInsightStandard200Response getNumberInsightStandard(format, number, country, cnam)

Standard Number Insight

Provides [standard number insight](/number-insight/overview#basic-standard-and-advanced-apis) information about a number.  Note that this endpoint also supports &#x60;POST&#x60; requests. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.nexmo.com/ni");
    
    // Configure API key authorization: apiKey
    ApiKeyAuth apiKey = (ApiKeyAuth) defaultClient.getAuthentication("apiKey");
    apiKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiKey.setApiKeyPrefix("Token");

    // Configure API key authorization: apiSecret
    ApiKeyAuth apiSecret = (ApiKeyAuth) defaultClient.getAuthentication("apiSecret");
    apiSecret.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apiSecret.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String format = "json"; // String | The format of the response
    String number = "447700900000"; // String | A single phone number that you need insight about in national or international format.
    String country = "GB"; // String | If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number.
    Boolean cnam = false; // Boolean | Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge.
    try {
      GetNumberInsightStandard200Response result = apiInstance.getNumberInsightStandard(format, number, country, cnam);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#getNumberInsightStandard");
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
| **format** | **String**| The format of the response | [enum: json, xml] |
| **number** | **String**| A single phone number that you need insight about in national or international format. | |
| **country** | **String**| If a number does not have a country code or is uncertain, set the two-character country code. This code must be in ISO 3166-1 alpha-2 format and in upper case. For example, GB or US. If you set country and number is already in [E.164](https://en.wikipedia.org/wiki/E.164) format, country must match the country code in number. | [optional] |
| **cnam** | **Boolean**| Indicates if the name of the person who owns the phone number should be looked up and returned in the response. Set to true to receive phone number owner name in the response. This features is available for US numbers only and incurs an additional charge. | [optional] [default to false] |

### Return type

[**GetNumberInsightStandard200Response**](GetNumberInsightStandard200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [apiSecret](../README.md#apiSecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

