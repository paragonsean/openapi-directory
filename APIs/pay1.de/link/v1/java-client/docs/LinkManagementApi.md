# LinkManagementApi

All URIs are relative to *https://onelink.pay1.de/api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createPaymentLink**](LinkManagementApi.md#createPaymentLink) | **POST** /v1/payment-links | Create a payment link. |
| [**getPaymentLink**](LinkManagementApi.md#getPaymentLink) | **GET** /v1/payment-links/{linkId} | Get payment link by id. |
| [**getPaymentLinks**](LinkManagementApi.md#getPaymentLinks) | **GET** /v1/payment-links | List all payment links. |
| [**updatePaymentLink**](LinkManagementApi.md#updatePaymentLink) | **PUT** /v1/payment-links/{linkId} | Update a payment link. |


<a id="createPaymentLink"></a>
# **createPaymentLink**
> LinkResponse createPaymentLink(linkCreateRequest)

Create a payment link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://onelink.pay1.de/api");
    

    LinkManagementApi apiInstance = new LinkManagementApi(defaultClient);
    LinkCreateRequest linkCreateRequest = new LinkCreateRequest(); // LinkCreateRequest | 
    try {
      LinkResponse result = apiInstance.createPaymentLink(linkCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkManagementApi#createPaymentLink");
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
| **linkCreateRequest** | [**LinkCreateRequest**](LinkCreateRequest.md)|  | [optional] |

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[createAuth](../README.md#createAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default response |  -  |

<a id="getPaymentLink"></a>
# **getPaymentLink**
> LinkResponse getPaymentLink(linkId)

Get payment link by id.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://onelink.pay1.de/api");
    

    LinkManagementApi apiInstance = new LinkManagementApi(defaultClient);
    String linkId = "linkId_example"; // String | 
    try {
      LinkResponse result = apiInstance.getPaymentLink(linkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkManagementApi#getPaymentLink");
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
| **linkId** | **String**|  | |

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[getSingleAuth](../README.md#getSingleAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default response |  -  |

<a id="getPaymentLinks"></a>
# **getPaymentLinks**
> PageLinkResponse getPaymentLinks(merchantId, accountId, portalId, mode, page, limit)

List all payment links.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://onelink.pay1.de/api");
    

    LinkManagementApi apiInstance = new LinkManagementApi(defaultClient);
    String merchantId = "merchantId_example"; // String | 
    String accountId = "accountId_example"; // String | 
    String portalId = "portalId_example"; // String | 
    String mode = "mode_example"; // String | 
    Integer page = 0; // Integer | 
    Integer limit = 25; // Integer | 
    try {
      PageLinkResponse result = apiInstance.getPaymentLinks(merchantId, accountId, portalId, mode, page, limit);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkManagementApi#getPaymentLinks");
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
| **merchantId** | **String**|  | |
| **accountId** | **String**|  | |
| **portalId** | **String**|  | |
| **mode** | **String**|  | |
| **page** | **Integer**|  | [optional] [default to 0] |
| **limit** | **Integer**|  | [optional] [default to 25] |

### Return type

[**PageLinkResponse**](PageLinkResponse.md)

### Authorization

[getMultipleAuth](../README.md#getMultipleAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default response |  -  |

<a id="updatePaymentLink"></a>
# **updatePaymentLink**
> LinkResponse updatePaymentLink(linkId, linkCreateRequest)

Update a payment link.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LinkManagementApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://onelink.pay1.de/api");
    

    LinkManagementApi apiInstance = new LinkManagementApi(defaultClient);
    String linkId = "linkId_example"; // String | 
    LinkCreateRequest linkCreateRequest = new LinkCreateRequest(); // LinkCreateRequest | 
    try {
      LinkResponse result = apiInstance.updatePaymentLink(linkId, linkCreateRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LinkManagementApi#updatePaymentLink");
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
| **linkId** | **String**|  | |
| **linkCreateRequest** | [**LinkCreateRequest**](LinkCreateRequest.md)|  | [optional] |

### Return type

[**LinkResponse**](LinkResponse.md)

### Authorization

[createAuth](../README.md#createAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | default response |  -  |

