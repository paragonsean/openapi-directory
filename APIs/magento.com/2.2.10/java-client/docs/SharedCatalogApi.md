# SharedCatalogApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**sharedCatalogSharedCatalogRepositoryV1GetListGet**](SharedCatalogApi.md#sharedCatalogSharedCatalogRepositoryV1GetListGet) | **GET** /V1/sharedCatalog/ | sharedCatalog/ |
| [**sharedCatalogSharedCatalogRepositoryV1SavePost**](SharedCatalogApi.md#sharedCatalogSharedCatalogRepositoryV1SavePost) | **POST** /V1/sharedCatalog | sharedCatalog |


<a id="sharedCatalogSharedCatalogRepositoryV1GetListGet"></a>
# **sharedCatalogSharedCatalogRepositoryV1GetListGet**
> SharedCatalogDataSearchResultsInterface sharedCatalogSharedCatalogRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage)

sharedCatalog/

Return the list of shared catalogs and basic properties for each catalog.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogApi apiInstance = new SharedCatalogApi(defaultClient);
    String searchCriteriaFilterGroups0Filters0Field = "searchCriteriaFilterGroups0Filters0Field_example"; // String | Field
    String searchCriteriaFilterGroups0Filters0Value = "searchCriteriaFilterGroups0Filters0Value_example"; // String | Value
    String searchCriteriaFilterGroups0Filters0ConditionType = "searchCriteriaFilterGroups0Filters0ConditionType_example"; // String | Condition type
    String searchCriteriaSortOrders0Field = "searchCriteriaSortOrders0Field_example"; // String | Sorting field.
    String searchCriteriaSortOrders0Direction = "searchCriteriaSortOrders0Direction_example"; // String | Sorting direction.
    Integer searchCriteriaPageSize = 56; // Integer | Page size.
    Integer searchCriteriaCurrentPage = 56; // Integer | Current page.
    try {
      SharedCatalogDataSearchResultsInterface result = apiInstance.sharedCatalogSharedCatalogRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogApi#sharedCatalogSharedCatalogRepositoryV1GetListGet");
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
| **searchCriteriaFilterGroups0Filters0Field** | **String**| Field | [optional] |
| **searchCriteriaFilterGroups0Filters0Value** | **String**| Value | [optional] |
| **searchCriteriaFilterGroups0Filters0ConditionType** | **String**| Condition type | [optional] |
| **searchCriteriaSortOrders0Field** | **String**| Sorting field. | [optional] |
| **searchCriteriaSortOrders0Direction** | **String**| Sorting direction. | [optional] |
| **searchCriteriaPageSize** | **Integer**| Page size. | [optional] |
| **searchCriteriaCurrentPage** | **Integer**| Current page. | [optional] |

### Return type

[**SharedCatalogDataSearchResultsInterface**](SharedCatalogDataSearchResultsInterface.md)

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

<a id="sharedCatalogSharedCatalogRepositoryV1SavePost"></a>
# **sharedCatalogSharedCatalogRepositoryV1SavePost**
> Integer sharedCatalogSharedCatalogRepositoryV1SavePost(sharedCatalogSharedCatalogRepositoryV1SavePostRequest)

sharedCatalog

Create or update Shared Catalog service.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SharedCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    SharedCatalogApi apiInstance = new SharedCatalogApi(defaultClient);
    SharedCatalogSharedCatalogRepositoryV1SavePostRequest sharedCatalogSharedCatalogRepositoryV1SavePostRequest = new SharedCatalogSharedCatalogRepositoryV1SavePostRequest(); // SharedCatalogSharedCatalogRepositoryV1SavePostRequest | 
    try {
      Integer result = apiInstance.sharedCatalogSharedCatalogRepositoryV1SavePost(sharedCatalogSharedCatalogRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SharedCatalogApi#sharedCatalogSharedCatalogRepositoryV1SavePost");
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
| **sharedCatalogSharedCatalogRepositoryV1SavePostRequest** | [**SharedCatalogSharedCatalogRepositoryV1SavePostRequest**](SharedCatalogSharedCatalogRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

**Integer**

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
| **500** | Internal Server error |  -  |
| **0** | Unexpected error |  -  |

