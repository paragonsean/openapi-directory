# FreightValuesApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createUpdateFreightValues**](FreightValuesApi.md#createUpdateFreightValues) | **POST** /api/logistics/pvt/configuration/freights/{carrierId}/values/update | Create/update freight values |
| [**freightValues**](FreightValuesApi.md#freightValues) | **GET** /api/logistics/pvt/configuration/freights/{carrierId}/{cep}/values | List freight values |


<a id="createUpdateFreightValues"></a>
# **createUpdateFreightValues**
> createUpdateFreightValues(contentType, accept, carrierId, createUpdateFreightValuesRequest)

Create/update freight values

Creates or updates the freight values of your store&#39;s carriers. Learn more in [Shipping rate template](https://help.vtex.com/en/tutorial/planilha-de-frete--tutorials_127#).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FreightValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    FreightValuesApi apiInstance = new FreightValuesApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String carrierId = "carrier123"; // String | 
    List<CreateUpdateFreightValuesRequest> createUpdateFreightValuesRequest = Arrays.asList(); // List<CreateUpdateFreightValuesRequest> | 
    try {
      apiInstance.createUpdateFreightValues(contentType, accept, carrierId, createUpdateFreightValuesRequest);
    } catch (ApiException e) {
      System.err.println("Exception when calling FreightValuesApi#createUpdateFreightValues");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **carrierId** | **String**|  | |
| **createUpdateFreightValuesRequest** | [**List&lt;CreateUpdateFreightValuesRequest&gt;**](CreateUpdateFreightValuesRequest.md)|  | |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: application/json; charset=utf-8
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="freightValues"></a>
# **freightValues**
> List&lt;FreightValues200ResponseInner&gt; freightValues(contentType, accept, carrierId, cep)

List freight values

Lists freight values apointed to your store&#39;s carriers, searching by carrier ID and postal code (&#x60;cep&#x60;).

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.FreightValuesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    FreightValuesApi apiInstance = new FreightValuesApi(defaultClient);
    String contentType = "application/json; charset=utf-8"; // String | Type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    String carrierId = "carrier-123"; // String | Carrier ID
    String cep = "12345000"; // String | Postal code.
    try {
      List<FreightValues200ResponseInner> result = apiInstance.freightValues(contentType, accept, carrierId, cep);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling FreightValuesApi#freightValues");
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
| **contentType** | **String**| Type of the content being sent | [default to application/json; charset&#x3D;utf-8] |
| **accept** | **String**| HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand | [default to application/json] |
| **carrierId** | **String**| Carrier ID | |
| **cep** | **String**| Postal code. | |

### Return type

[**List&lt;FreightValues200ResponseInner&gt;**](FreightValues200ResponseInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json; charset=utf-8

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * Cache-Control -  <br>  * Connection -  <br>  * Content-Length -  <br>  * Date -  <br>  * Expires -  <br>  * Pragma -  <br>  * Server -  <br>  * X-CDNIgnore -  <br>  * X-CacheServer -  <br>  * X-Powered-by-VTEX-Janus-ApiCache -  <br>  * X-Powered-by-VTEX-Janus-Edge -  <br>  * X-Powered-by-VTEX-Janus-Router -  <br>  * X-Track -  <br>  * X-VTEX-Cache-Status-Janus-ApiCache -  <br>  * X-VTEX-Janus-Router-Backend-App -  <br>  * x-vtex-operation-id -  <br>  |

