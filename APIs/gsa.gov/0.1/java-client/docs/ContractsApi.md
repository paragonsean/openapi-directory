# ContractsApi

All URIs are relative to *https://discovery.gsa.gov*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**listContractsGET**](ContractsApi.md#listContractsGET) | **GET** /api/contracts/ | This endpoint returns contract history from FPDS for a specific vendor |


<a id="listContractsGET"></a>
# **listContractsGET**
> Object listContractsGET(duns, naics, sort, direction, page)

This endpoint returns contract history from FPDS for a specific vendor

&lt;p&gt;This endpoint returns contract history from FPDS for a specific vendor. The vendor&#39;s DUNS number is a required parameter. You can also filter contracts by their NAICS code to find contracts relevant to a particular category.&lt;/p&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ContractsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://discovery.gsa.gov");

    ContractsApi apiInstance = new ContractsApi(defaultClient);
    String duns = "duns_example"; // String | A 9-digit DUNS number that uniquely identifies a vendor (required).
    String naics = "naics_example"; // String | a six digit NAICS code used to filter by contracts with a certain NAICS
    String sort = "sort_example"; // String | a field to sort on. Choices are date, status, agency, and amount
    String direction = "direction_example"; // String | The sort direction of the results. Choices are asc or desc.
    String page = "page_example"; // String | the page to start on. Results are paginated in increments of 100. Begins at page=1.
    try {
      Object result = apiInstance.listContractsGET(duns, naics, sort, direction, page);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ContractsApi#listContractsGET");
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
| **duns** | **String**| A 9-digit DUNS number that uniquely identifies a vendor (required). | |
| **naics** | **String**| a six digit NAICS code used to filter by contracts with a certain NAICS | [optional] |
| **sort** | **String**| a field to sort on. Choices are date, status, agency, and amount | [optional] |
| **direction** | **String**| The sort direction of the results. Choices are asc or desc. | [optional] |
| **page** | **String**| the page to start on. Results are paginated in increments of 100. Begins at page&#x3D;1. | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | No response was specified |  -  |

