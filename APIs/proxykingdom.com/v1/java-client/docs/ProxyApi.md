# ProxyApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**proxyGet**](ProxyApi.md#proxyGet) | **GET** /proxy | Gets a random proxy for chosen parameters. |


<a id="proxyGet"></a>
# **proxyGet**
> Proxy proxyGet(correlationId, token, address, port, protocol, accessType, responseTime, isSsl, uptime, country, continent, timezone, lastTested)

Gets a random proxy for chosen parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProxyApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    ProxyApi apiInstance = new ProxyApi(defaultClient);
    String correlationId = "049d3e5c-f02a-4568-a1f4-7bd182668b1b"; // String | Correlation Id header field
    String token = "token_example"; // String | 
    String address = "address_example"; // String | 
    String port = "port_example"; // String | 
    String protocol = "protocol_example"; // String | 
    String accessType = "accessType_example"; // String | 
    String responseTime = "responseTime_example"; // String | 
    String isSsl = "isSsl_example"; // String | 
    String uptime = "uptime_example"; // String | 
    String country = "country_example"; // String | 
    String continent = "continent_example"; // String | 
    String timezone = "timezone_example"; // String | 
    String lastTested = "lastTested_example"; // String | 
    try {
      Proxy result = apiInstance.proxyGet(correlationId, token, address, port, protocol, accessType, responseTime, isSsl, uptime, country, continent, timezone, lastTested);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProxyApi#proxyGet");
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
| **correlationId** | **String**| Correlation Id header field | [default to 049d3e5c-f02a-4568-a1f4-7bd182668b1b] |
| **token** | **String**|  | [optional] |
| **address** | **String**|  | [optional] |
| **port** | **String**|  | [optional] |
| **protocol** | **String**|  | [optional] |
| **accessType** | **String**|  | [optional] |
| **responseTime** | **String**|  | [optional] |
| **isSsl** | **String**|  | [optional] |
| **uptime** | **String**|  | [optional] |
| **country** | **String**|  | [optional] |
| **continent** | **String**|  | [optional] |
| **timezone** | **String**|  | [optional] |
| **lastTested** | **String**|  | [optional] |

### Return type

[**Proxy**](Proxy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, text/plain

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | Invalid proxy filter provided. |  -  |
| **404** | No Proxy found for GetProxy by filter. |  -  |
| **429** | Subscription limit reached. |  -  |
| **500** | Technical Error. |  -  |

