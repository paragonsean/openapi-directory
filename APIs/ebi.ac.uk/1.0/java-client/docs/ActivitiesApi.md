# ActivitiesApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getActivitiesUsingGET**](ActivitiesApi.md#getActivitiesUsingGET) | **GET** /activities | Get ChEMBL activities |


<a id="getActivitiesUsingGET"></a>
# **getActivitiesUsingGET**
> Activities getActivitiesUsingGET(assayChemblId, limit, moleculeChemblId, page, pchemblValue, targetChemblId)

Get ChEMBL activities

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ActivitiesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    ActivitiesApi apiInstance = new ActivitiesApi(defaultClient);
    List<String> assayChemblId = Arrays.asList(); // List<String> | assayChemblId
    Integer limit = 10; // Integer | limit
    List<String> moleculeChemblId = Arrays.asList(); // List<String> | moleculeChemblId
    Integer page = 0; // Integer | page
    Double pchemblValue = 3.4D; // Double | pchemblValue
    List<String> targetChemblId = Arrays.asList(); // List<String> | targetChemblId
    try {
      Activities result = apiInstance.getActivitiesUsingGET(assayChemblId, limit, moleculeChemblId, page, pchemblValue, targetChemblId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ActivitiesApi#getActivitiesUsingGET");
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
| **assayChemblId** | [**List&lt;String&gt;**](String.md)| assayChemblId | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **moleculeChemblId** | [**List&lt;String&gt;**](String.md)| moleculeChemblId | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **pchemblValue** | **Double**| pchemblValue | [optional] |
| **targetChemblId** | [**List&lt;String&gt;**](String.md)| targetChemblId | [optional] |

### Return type

[**Activities**](Activities.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **401** | Unauthorized |  -  |
| **403** | Forbidden |  -  |
| **404** | Not Found |  -  |

