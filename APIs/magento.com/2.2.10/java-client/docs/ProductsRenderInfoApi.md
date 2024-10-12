# ProductsRenderInfoApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**catalogProductRenderListV1GetListGet**](ProductsRenderInfoApi.md#catalogProductRenderListV1GetListGet) | **GET** /V1/products-render-info | products-render-info |


<a id="catalogProductRenderListV1GetListGet"></a>
# **catalogProductRenderListV1GetListGet**
> CatalogDataProductRenderSearchResultsInterface catalogProductRenderListV1GetListGet(storeId, currencyCode, searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage)

products-render-info

Collect and retrieve the list of product render info This info contains raw prices and formated prices, product name, stock status, store_id, etc

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ProductsRenderInfoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    ProductsRenderInfoApi apiInstance = new ProductsRenderInfoApi(defaultClient);
    Integer storeId = 56; // Integer | 
    String currencyCode = "currencyCode_example"; // String | 
    String searchCriteriaFilterGroups0Filters0Field = "searchCriteriaFilterGroups0Filters0Field_example"; // String | Field
    String searchCriteriaFilterGroups0Filters0Value = "searchCriteriaFilterGroups0Filters0Value_example"; // String | Value
    String searchCriteriaFilterGroups0Filters0ConditionType = "searchCriteriaFilterGroups0Filters0ConditionType_example"; // String | Condition type
    String searchCriteriaSortOrders0Field = "searchCriteriaSortOrders0Field_example"; // String | Sorting field.
    String searchCriteriaSortOrders0Direction = "searchCriteriaSortOrders0Direction_example"; // String | Sorting direction.
    Integer searchCriteriaPageSize = 56; // Integer | Page size.
    Integer searchCriteriaCurrentPage = 56; // Integer | Current page.
    try {
      CatalogDataProductRenderSearchResultsInterface result = apiInstance.catalogProductRenderListV1GetListGet(storeId, currencyCode, searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ProductsRenderInfoApi#catalogProductRenderListV1GetListGet");
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
| **storeId** | **Integer**|  | |
| **currencyCode** | **String**|  | |
| **searchCriteriaFilterGroups0Filters0Field** | **String**| Field | [optional] |
| **searchCriteriaFilterGroups0Filters0Value** | **String**| Value | [optional] |
| **searchCriteriaFilterGroups0Filters0ConditionType** | **String**| Condition type | [optional] |
| **searchCriteriaSortOrders0Field** | **String**| Sorting field. | [optional] |
| **searchCriteriaSortOrders0Direction** | **String**| Sorting direction. | [optional] |
| **searchCriteriaPageSize** | **Integer**| Page size. | [optional] |
| **searchCriteriaCurrentPage** | **Integer**| Current page. | [optional] |

### Return type

[**CatalogDataProductRenderSearchResultsInterface**](CatalogDataProductRenderSearchResultsInterface.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **0** | Unexpected error |  -  |

