# CartsMineApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartManagementV1CreateEmptyCartForCustomerPost**](CartsMineApi.md#quoteCartManagementV1CreateEmptyCartForCustomerPost) | **POST** /V1/carts/mine | carts/mine |
| [**quoteCartManagementV1GetCartForCustomerGet**](CartsMineApi.md#quoteCartManagementV1GetCartForCustomerGet) | **GET** /V1/carts/mine | carts/mine |
| [**quoteCartRepositoryV1SavePut**](CartsMineApi.md#quoteCartRepositoryV1SavePut) | **PUT** /V1/carts/mine | carts/mine |


<a id="quoteCartManagementV1CreateEmptyCartForCustomerPost"></a>
# **quoteCartManagementV1CreateEmptyCartForCustomerPost**
> Integer quoteCartManagementV1CreateEmptyCartForCustomerPost()

carts/mine

Creates an empty cart and quote for a specified customer if customer does not have a cart yet.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineApi apiInstance = new CartsMineApi(defaultClient);
    try {
      Integer result = apiInstance.quoteCartManagementV1CreateEmptyCartForCustomerPost();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineApi#quoteCartManagementV1CreateEmptyCartForCustomerPost");
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

**Integer**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="quoteCartManagementV1GetCartForCustomerGet"></a>
# **quoteCartManagementV1GetCartForCustomerGet**
> QuoteDataCartInterface quoteCartManagementV1GetCartForCustomerGet()

carts/mine

Returns information for the cart for a specified customer.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineApi apiInstance = new CartsMineApi(defaultClient);
    try {
      QuoteDataCartInterface result = apiInstance.quoteCartManagementV1GetCartForCustomerGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineApi#quoteCartManagementV1GetCartForCustomerGet");
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

[**QuoteDataCartInterface**](QuoteDataCartInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="quoteCartRepositoryV1SavePut"></a>
# **quoteCartRepositoryV1SavePut**
> ErrorResponse quoteCartRepositoryV1SavePut(quoteCartRepositoryV1SavePutRequest)

carts/mine

Save quote

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsMineApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsMineApi apiInstance = new CartsMineApi(defaultClient);
    QuoteCartRepositoryV1SavePutRequest quoteCartRepositoryV1SavePutRequest = new QuoteCartRepositoryV1SavePutRequest(); // QuoteCartRepositoryV1SavePutRequest | 
    try {
      ErrorResponse result = apiInstance.quoteCartRepositoryV1SavePut(quoteCartRepositoryV1SavePutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsMineApi#quoteCartRepositoryV1SavePut");
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
| **quoteCartRepositoryV1SavePutRequest** | [**QuoteCartRepositoryV1SavePutRequest**](QuoteCartRepositoryV1SavePutRequest.md)|  | [optional] |

### Return type

[**ErrorResponse**](ErrorResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

