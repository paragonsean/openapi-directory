# PubChemSubstancesApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubstancesUsingGET**](PubChemSubstancesApi.md#getSubstancesUsingGET) | **GET** /pubchem/substances | Get pubchem substances |


<a id="getSubstancesUsingGET"></a>
# **getSubstancesUsingGET**
> PubchemSubstances getSubstancesUsingGET(cid, limit, page, sid)

Get pubchem substances

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PubChemSubstancesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    PubChemSubstancesApi apiInstance = new PubChemSubstancesApi(defaultClient);
    List<String> cid = Arrays.asList(); // List<String> | cid
    Integer limit = 10; // Integer | limit
    Integer page = 0; // Integer | page
    List<String> sid = Arrays.asList(); // List<String> | sid
    try {
      PubchemSubstances result = apiInstance.getSubstancesUsingGET(cid, limit, page, sid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PubChemSubstancesApi#getSubstancesUsingGET");
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
| **cid** | [**List&lt;String&gt;**](String.md)| cid | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **sid** | [**List&lt;String&gt;**](String.md)| sid | [optional] |

### Return type

[**PubchemSubstances**](PubchemSubstances.md)

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

