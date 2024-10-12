# ShipmentIdCommentsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesShipmentCommentRepositoryV1SavePost**](ShipmentIdCommentsApi.md#salesShipmentCommentRepositoryV1SavePost) | **POST** /V1/shipment/{id}/comments | shipment/{id}/comments |
| [**salesShipmentManagementV1GetCommentsListGet**](ShipmentIdCommentsApi.md#salesShipmentManagementV1GetCommentsListGet) | **GET** /V1/shipment/{id}/comments | shipment/{id}/comments |


<a id="salesShipmentCommentRepositoryV1SavePost"></a>
# **salesShipmentCommentRepositoryV1SavePost**
> SalesDataShipmentCommentInterface salesShipmentCommentRepositoryV1SavePost(id, salesShipmentCommentRepositoryV1SavePostRequest)

shipment/{id}/comments

Performs persist operations for a specified shipment comment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentIdCommentsApi apiInstance = new ShipmentIdCommentsApi(defaultClient);
    String id = "id_example"; // String | 
    SalesShipmentCommentRepositoryV1SavePostRequest salesShipmentCommentRepositoryV1SavePostRequest = new SalesShipmentCommentRepositoryV1SavePostRequest(); // SalesShipmentCommentRepositoryV1SavePostRequest | 
    try {
      SalesDataShipmentCommentInterface result = apiInstance.salesShipmentCommentRepositoryV1SavePost(id, salesShipmentCommentRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentIdCommentsApi#salesShipmentCommentRepositoryV1SavePost");
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
| **id** | **String**|  | |
| **salesShipmentCommentRepositoryV1SavePostRequest** | [**SalesShipmentCommentRepositoryV1SavePostRequest**](SalesShipmentCommentRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataShipmentCommentInterface**](SalesDataShipmentCommentInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **400** | 400 Bad Request |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

<a id="salesShipmentManagementV1GetCommentsListGet"></a>
# **salesShipmentManagementV1GetCommentsListGet**
> SalesDataShipmentCommentSearchResultInterface salesShipmentManagementV1GetCommentsListGet(id)

shipment/{id}/comments

Lists comments for a specified shipment.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ShipmentIdCommentsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ShipmentIdCommentsApi apiInstance = new ShipmentIdCommentsApi(defaultClient);
    Integer id = 56; // Integer | The shipment ID.
    try {
      SalesDataShipmentCommentSearchResultInterface result = apiInstance.salesShipmentManagementV1GetCommentsListGet(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ShipmentIdCommentsApi#salesShipmentManagementV1GetCommentsListGet");
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
| **id** | **Integer**| The shipment ID. | |

### Return type

[**SalesDataShipmentCommentSearchResultInterface**](SalesDataShipmentCommentSearchResultInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

