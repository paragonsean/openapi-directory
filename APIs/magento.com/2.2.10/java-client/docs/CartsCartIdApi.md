# CartsCartIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteCartManagementV1AssignCustomerPut**](CartsCartIdApi.md#quoteCartManagementV1AssignCustomerPut) | **PUT** /V1/carts/{cartId} | carts/{cartId} |
| [**quoteCartRepositoryV1GetGet**](CartsCartIdApi.md#quoteCartRepositoryV1GetGet) | **GET** /V1/carts/{cartId} | carts/{cartId} |


<a id="quoteCartManagementV1AssignCustomerPut"></a>
# **quoteCartManagementV1AssignCustomerPut**
> Boolean quoteCartManagementV1AssignCustomerPut(cartId, quoteCartManagementV1AssignCustomerPutRequest)

carts/{cartId}

Assigns a specified customer to a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdApi apiInstance = new CartsCartIdApi(defaultClient);
    Integer cartId = 56; // Integer | The cart ID.
    QuoteCartManagementV1AssignCustomerPutRequest quoteCartManagementV1AssignCustomerPutRequest = new QuoteCartManagementV1AssignCustomerPutRequest(); // QuoteCartManagementV1AssignCustomerPutRequest | 
    try {
      Boolean result = apiInstance.quoteCartManagementV1AssignCustomerPut(cartId, quoteCartManagementV1AssignCustomerPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdApi#quoteCartManagementV1AssignCustomerPut");
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
| **cartId** | **Integer**| The cart ID. | |
| **quoteCartManagementV1AssignCustomerPutRequest** | [**QuoteCartManagementV1AssignCustomerPutRequest**](QuoteCartManagementV1AssignCustomerPutRequest.md)|  | [optional] |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="quoteCartRepositoryV1GetGet"></a>
# **quoteCartRepositoryV1GetGet**
> QuoteDataCartInterface quoteCartRepositoryV1GetGet(cartId)

carts/{cartId}

Enables an administrative user to return information for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CartsCartIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CartsCartIdApi apiInstance = new CartsCartIdApi(defaultClient);
    Integer cartId = 56; // Integer | 
    try {
      QuoteDataCartInterface result = apiInstance.quoteCartRepositoryV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CartsCartIdApi#quoteCartRepositoryV1GetGet");
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
| **cartId** | **Integer**|  | |

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

