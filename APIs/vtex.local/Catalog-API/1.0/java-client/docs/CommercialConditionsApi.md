# CommercialConditionsApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllCommercialConditions**](CommercialConditionsApi.md#getAllCommercialConditions) | **GET** /api/catalog_system/pvt/commercialcondition/list | Get all commercial conditions |
| [**getCommercialConditions**](CommercialConditionsApi.md#getCommercialConditions) | **GET** /api/catalog_system/pvt/commercialcondition/{commercialConditionId} | Get commercial condition |


<a id="getAllCommercialConditions"></a>
# **getAllCommercialConditions**
> List&lt;ArrayWithInformationOfAllTheCommercialConditionsInner&gt; getAllCommercialConditions(contentType, accept)

Get all commercial conditions

Lists all commercial conditions on the store.   ## Response body example    &#x60;&#x60;&#x60;json  [      {          \&quot;Id\&quot;: 1,          \&quot;Name\&quot;: \&quot;Padrão\&quot;,          \&quot;IsDefault\&quot;: true      },      {          \&quot;Id\&quot;: 2,          \&quot;Name\&quot;: \&quot;Teste Fast\&quot;,          \&quot;IsDefault\&quot;: false      }  ]  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommercialConditionsApi;

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

    CommercialConditionsApi apiInstance = new CommercialConditionsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    try {
      List<ArrayWithInformationOfAllTheCommercialConditionsInner> result = apiInstance.getAllCommercialConditions(contentType, accept);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommercialConditionsApi#getAllCommercialConditions");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |

### Return type

[**List&lt;ArrayWithInformationOfAllTheCommercialConditionsInner&gt;**](ArrayWithInformationOfAllTheCommercialConditionsInner.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="getCommercialConditions"></a>
# **getCommercialConditions**
> GetCommercialConditions200Response getCommercialConditions(contentType, accept, commercialConditionId)

Get commercial condition

Retrieves information of a commercial condition by its ID.   ## Response body example    &#x60;&#x60;&#x60;json  {      \&quot;Id\&quot;: 1,      \&quot;Name\&quot;: \&quot;Padrão\&quot;,      \&quot;IsDefault\&quot;: true  }  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CommercialConditionsApi;

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

    CommercialConditionsApi apiInstance = new CommercialConditionsApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    Integer commercialConditionId = 1; // Integer | Commercial condition unique numerical identifier.
    try {
      GetCommercialConditions200Response result = apiInstance.getCommercialConditions(contentType, accept, commercialConditionId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CommercialConditionsApi#getCommercialConditions");
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
| **contentType** | **String**| Describes the type of the content being sent. | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | [default to application/json] |
| **commercialConditionId** | **Integer**| Commercial condition unique numerical identifier. | |

### Return type

[**GetCommercialConditions200Response**](GetCommercialConditions200Response.md)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

