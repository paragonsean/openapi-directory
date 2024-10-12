# GiftWrappingsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**giftWrappingWrappingRepositoryV1GetListGet**](GiftWrappingsApi.md#giftWrappingWrappingRepositoryV1GetListGet) | **GET** /V1/gift-wrappings | gift-wrappings |
| [**giftWrappingWrappingRepositoryV1SavePost**](GiftWrappingsApi.md#giftWrappingWrappingRepositoryV1SavePost) | **POST** /V1/gift-wrappings | gift-wrappings |


<a id="giftWrappingWrappingRepositoryV1GetListGet"></a>
# **giftWrappingWrappingRepositoryV1GetListGet**
> GiftWrappingDataWrappingSearchResultsInterface giftWrappingWrappingRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage)

gift-wrappings

Return list of gift wrapping data objects based on search criteria

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftWrappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GiftWrappingsApi apiInstance = new GiftWrappingsApi(defaultClient);
    String searchCriteriaFilterGroups0Filters0Field = "searchCriteriaFilterGroups0Filters0Field_example"; // String | Field
    String searchCriteriaFilterGroups0Filters0Value = "searchCriteriaFilterGroups0Filters0Value_example"; // String | Value
    String searchCriteriaFilterGroups0Filters0ConditionType = "searchCriteriaFilterGroups0Filters0ConditionType_example"; // String | Condition type
    String searchCriteriaSortOrders0Field = "searchCriteriaSortOrders0Field_example"; // String | Sorting field.
    String searchCriteriaSortOrders0Direction = "searchCriteriaSortOrders0Direction_example"; // String | Sorting direction.
    Integer searchCriteriaPageSize = 56; // Integer | Page size.
    Integer searchCriteriaCurrentPage = 56; // Integer | Current page.
    try {
      GiftWrappingDataWrappingSearchResultsInterface result = apiInstance.giftWrappingWrappingRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftWrappingsApi#giftWrappingWrappingRepositoryV1GetListGet");
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

[**GiftWrappingDataWrappingSearchResultsInterface**](GiftWrappingDataWrappingSearchResultsInterface.md)

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

<a id="giftWrappingWrappingRepositoryV1SavePost"></a>
# **giftWrappingWrappingRepositoryV1SavePost**
> GiftWrappingDataWrappingInterface giftWrappingWrappingRepositoryV1SavePost(giftWrappingWrappingRepositoryV1SavePostRequest)

gift-wrappings

Create/Update new gift wrapping with data object values

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.GiftWrappingsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    GiftWrappingsApi apiInstance = new GiftWrappingsApi(defaultClient);
    GiftWrappingWrappingRepositoryV1SavePostRequest giftWrappingWrappingRepositoryV1SavePostRequest = new GiftWrappingWrappingRepositoryV1SavePostRequest(); // GiftWrappingWrappingRepositoryV1SavePostRequest | 
    try {
      GiftWrappingDataWrappingInterface result = apiInstance.giftWrappingWrappingRepositoryV1SavePost(giftWrappingWrappingRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling GiftWrappingsApi#giftWrappingWrappingRepositoryV1SavePost");
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
| **giftWrappingWrappingRepositoryV1SavePostRequest** | [**GiftWrappingWrappingRepositoryV1SavePostRequest**](GiftWrappingWrappingRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**GiftWrappingDataWrappingInterface**](GiftWrappingDataWrappingInterface.md)

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

