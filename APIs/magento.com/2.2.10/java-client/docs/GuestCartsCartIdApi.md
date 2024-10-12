# GuestCartsCartIdApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**quoteGuestCartManagementV1AssignCustomerPut**](GuestCartsCartIdApi.md#quoteGuestCartManagementV1AssignCustomerPut) | **PUT** /V1/guest-carts/{cartId} | guest-carts/{cartId} |
| [**quoteGuestCartRepositoryV1GetGet**](GuestCartsCartIdApi.md#quoteGuestCartRepositoryV1GetGet) | **GET** /V1/guest-carts/{cartId} | guest-carts/{cartId} |


<a id="quoteGuestCartManagementV1AssignCustomerPut"></a>
# **quoteGuestCartManagementV1AssignCustomerPut**
> Boolean quoteGuestCartManagementV1AssignCustomerPut(cartId, quoteCartManagementV1AssignCustomerPutRequest)

guest-carts/{cartId}

Assign a specified customer to a specified shopping cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdApi apiInstance = new GuestCartsCartIdApi(defaultClient);
    String cartId = "cartId_example"; // String | The cart ID.
    QuoteCartManagementV1AssignCustomerPutRequest quoteCartManagementV1AssignCustomerPutRequest = new QuoteCartManagementV1AssignCustomerPutRequest(); // QuoteCartManagementV1AssignCustomerPutRequest | 
    try {
      Boolean result = apiInstance.quoteGuestCartManagementV1AssignCustomerPut(cartId, quoteCartManagementV1AssignCustomerPutRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdApi#quoteGuestCartManagementV1AssignCustomerPut");
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
| **cartId** | **String**| The cart ID. | |
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

<a id="quoteGuestCartRepositoryV1GetGet"></a>
# **quoteGuestCartRepositoryV1GetGet**
> QuoteDataCartInterface quoteGuestCartRepositoryV1GetGet(cartId)

guest-carts/{cartId}

Enable a guest user to return information for a specified cart.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GuestCartsCartIdApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GuestCartsCartIdApi apiInstance = new GuestCartsCartIdApi(defaultClient);
    String cartId = "cartId_example"; // String | 
    try {
      QuoteDataCartInterface result = apiInstance.quoteGuestCartRepositoryV1GetGet(cartId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GuestCartsCartIdApi#quoteGuestCartRepositoryV1GetGet");
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
| **cartId** | **String**|  | |

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
| **0** | Unexpected error |  -  |

