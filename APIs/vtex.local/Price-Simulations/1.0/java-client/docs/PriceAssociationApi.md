# PriceAssociationApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**vCustomPricesRulesPost**](PriceAssociationApi.md#vCustomPricesRulesPost) | **POST** /_v/custom-prices/rules | Create price association |
| [**vCustomPricesRulesPriceAssociationIdDelete**](PriceAssociationApi.md#vCustomPricesRulesPriceAssociationIdDelete) | **DELETE** /_v/custom-prices/rules/{priceAssociationId} | Disassociate price association by ID |
| [**vCustomPricesRulesPriceAssociationIdGet**](PriceAssociationApi.md#vCustomPricesRulesPriceAssociationIdGet) | **GET** /_v/custom-prices/rules/{priceAssociationId} | Get price association by ID |
| [**vCustomPricesRulesPriceAssociationIdPut**](PriceAssociationApi.md#vCustomPricesRulesPriceAssociationIdPut) | **PUT** /_v/custom-prices/rules/{priceAssociationId} | Update price association by ID |


<a id="vCustomPricesRulesPost"></a>
# **vCustomPricesRulesPost**
> VCustomPricesRulesPost200Response vCustomPricesRulesPost(contentType, accept, vcustomPricesRulesPostRequest)

Create price association

Creates a new price association for a shopping scenario

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PriceAssociationApi apiInstance = new PriceAssociationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    VCustomPricesRulesPostRequest vcustomPricesRulesPostRequest = new VCustomPricesRulesPostRequest(); // VCustomPricesRulesPostRequest | 
    try {
      VCustomPricesRulesPost200Response result = apiInstance.vCustomPricesRulesPost(contentType, accept, vcustomPricesRulesPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceAssociationApi#vCustomPricesRulesPost");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |
| **vcustomPricesRulesPostRequest** | [**VCustomPricesRulesPostRequest**](VCustomPricesRulesPostRequest.md)|  | [optional] |

### Return type

[**VCustomPricesRulesPost200Response**](VCustomPricesRulesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vCustomPricesRulesPriceAssociationIdDelete"></a>
# **vCustomPricesRulesPriceAssociationIdDelete**
> String vCustomPricesRulesPriceAssociationIdDelete(contentType, accept, priceAssociationId)

Disassociate price association by ID

Disassociates a price association from a shopping scenario by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PriceAssociationApi apiInstance = new PriceAssociationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    Integer priceAssociationId = 1; // Integer | Price Association unique identifier
    try {
      String result = apiInstance.vCustomPricesRulesPriceAssociationIdDelete(contentType, accept, priceAssociationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceAssociationApi#vCustomPricesRulesPriceAssociationIdDelete");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |
| **priceAssociationId** | **Integer**| Price Association unique identifier | [default to 1] |

### Return type

**String**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vCustomPricesRulesPriceAssociationIdGet"></a>
# **vCustomPricesRulesPriceAssociationIdGet**
> VCustomPricesRulesPost200Response vCustomPricesRulesPriceAssociationIdGet(contentType, accept, priceAssociationId)

Get price association by ID

Retrieves price association for a shopping scenario by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PriceAssociationApi apiInstance = new PriceAssociationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    Integer priceAssociationId = 1; // Integer | Price Association unique identifier
    try {
      VCustomPricesRulesPost200Response result = apiInstance.vCustomPricesRulesPriceAssociationIdGet(contentType, accept, priceAssociationId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceAssociationApi#vCustomPricesRulesPriceAssociationIdGet");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |
| **priceAssociationId** | **Integer**| Price Association unique identifier | [default to 1] |

### Return type

[**VCustomPricesRulesPost200Response**](VCustomPricesRulesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="vCustomPricesRulesPriceAssociationIdPut"></a>
# **vCustomPricesRulesPriceAssociationIdPut**
> VCustomPricesRulesPost200Response vCustomPricesRulesPriceAssociationIdPut(contentType, accept, priceAssociationId, requestBody)

Update price association by ID

Updates a price association for a shopping scenario by its ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PriceAssociationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");

    PriceAssociationApi apiInstance = new PriceAssociationApi(defaultClient);
    String contentType = "application/json"; // String | Describes the type of the content being sent
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand
    Integer priceAssociationId = 1; // Integer | Price Association unique identifier
    RequestBody requestBody = new RequestBody(); // RequestBody | 
    try {
      VCustomPricesRulesPost200Response result = apiInstance.vCustomPricesRulesPriceAssociationIdPut(contentType, accept, priceAssociationId, requestBody);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PriceAssociationApi#vCustomPricesRulesPriceAssociationIdPut");
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
| **contentType** | **String**| Describes the type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand | [default to application/json] |
| **priceAssociationId** | **Integer**| Price Association unique identifier | [default to 1] |
| **requestBody** | [**RequestBody**](RequestBody.md)|  | [optional] |

### Return type

[**VCustomPricesRulesPost200Response**](VCustomPricesRulesPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

