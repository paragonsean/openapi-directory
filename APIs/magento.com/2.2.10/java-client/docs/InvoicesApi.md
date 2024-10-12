# InvoicesApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesInvoiceRepositoryV1GetListGet**](InvoicesApi.md#salesInvoiceRepositoryV1GetListGet) | **GET** /V1/invoices | invoices |
| [**salesInvoiceRepositoryV1SavePost**](InvoicesApi.md#salesInvoiceRepositoryV1SavePost) | **POST** /V1/invoices/ | invoices/ |


<a id="salesInvoiceRepositoryV1GetListGet"></a>
# **salesInvoiceRepositoryV1GetListGet**
> SalesDataInvoiceSearchResultInterface salesInvoiceRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage)

invoices

Lists invoices that match specified search criteria. This call returns an array of objects, but detailed information about each object’s attributes might not be included. See https://devdocs.magento.com/codelinks/attributes.html#InvoiceRepositoryInterface to determine which call to use to get detailed information about all attributes for an object.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    String searchCriteriaFilterGroups0Filters0Field = "searchCriteriaFilterGroups0Filters0Field_example"; // String | Field
    String searchCriteriaFilterGroups0Filters0Value = "searchCriteriaFilterGroups0Filters0Value_example"; // String | Value
    String searchCriteriaFilterGroups0Filters0ConditionType = "searchCriteriaFilterGroups0Filters0ConditionType_example"; // String | Condition type
    String searchCriteriaSortOrders0Field = "searchCriteriaSortOrders0Field_example"; // String | Sorting field.
    String searchCriteriaSortOrders0Direction = "searchCriteriaSortOrders0Direction_example"; // String | Sorting direction.
    Integer searchCriteriaPageSize = 56; // Integer | Page size.
    Integer searchCriteriaCurrentPage = 56; // Integer | Current page.
    try {
      SalesDataInvoiceSearchResultInterface result = apiInstance.salesInvoiceRepositoryV1GetListGet(searchCriteriaFilterGroups0Filters0Field, searchCriteriaFilterGroups0Filters0Value, searchCriteriaFilterGroups0Filters0ConditionType, searchCriteriaSortOrders0Field, searchCriteriaSortOrders0Direction, searchCriteriaPageSize, searchCriteriaCurrentPage);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#salesInvoiceRepositoryV1GetListGet");
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

[**SalesDataInvoiceSearchResultInterface**](SalesDataInvoiceSearchResultInterface.md)

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

<a id="salesInvoiceRepositoryV1SavePost"></a>
# **salesInvoiceRepositoryV1SavePost**
> SalesDataInvoiceInterface salesInvoiceRepositoryV1SavePost(salesInvoiceRepositoryV1SavePostRequest)

invoices/

Performs persist operations for a specified invoice.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.InvoicesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    InvoicesApi apiInstance = new InvoicesApi(defaultClient);
    SalesInvoiceRepositoryV1SavePostRequest salesInvoiceRepositoryV1SavePostRequest = new SalesInvoiceRepositoryV1SavePostRequest(); // SalesInvoiceRepositoryV1SavePostRequest | 
    try {
      SalesDataInvoiceInterface result = apiInstance.salesInvoiceRepositoryV1SavePost(salesInvoiceRepositoryV1SavePostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling InvoicesApi#salesInvoiceRepositoryV1SavePost");
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
| **salesInvoiceRepositoryV1SavePostRequest** | [**SalesInvoiceRepositoryV1SavePostRequest**](SalesInvoiceRepositoryV1SavePostRequest.md)|  | [optional] |

### Return type

[**SalesDataInvoiceInterface**](SalesDataInvoiceInterface.md)

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

