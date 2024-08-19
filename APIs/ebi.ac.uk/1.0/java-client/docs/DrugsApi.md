# DrugsApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDrugsUsingGET**](DrugsApi.md#getDrugsUsingGET) | **GET** /drugs | drugs collected from Drugbank |


<a id="getDrugsUsingGET"></a>
# **getDrugsUsingGET**
> Drugs getDrugsUsingGET(accession, chemblId, identifier, limit, name, page, pubchemCid)

drugs collected from Drugbank

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DrugsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    DrugsApi apiInstance = new DrugsApi(defaultClient);
    List<String> accession = Arrays.asList(); // List<String> | accession
    List<String> chemblId = Arrays.asList(); // List<String> | chemblId
    List<String> identifier = Arrays.asList(); // List<String> | identifier
    Integer limit = 10; // Integer | limit
    List<String> name = Arrays.asList(); // List<String> | name
    Integer page = 0; // Integer | page
    List<String> pubchemCid = Arrays.asList(); // List<String> | pubchemCid
    try {
      Drugs result = apiInstance.getDrugsUsingGET(accession, chemblId, identifier, limit, name, page, pubchemCid);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DrugsApi#getDrugsUsingGET");
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
| **accession** | [**List&lt;String&gt;**](String.md)| accession | [optional] |
| **chemblId** | [**List&lt;String&gt;**](String.md)| chemblId | [optional] |
| **identifier** | [**List&lt;String&gt;**](String.md)| identifier | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **name** | [**List&lt;String&gt;**](String.md)| name | [optional] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **pubchemCid** | [**List&lt;String&gt;**](String.md)| pubchemCid | [optional] |

### Return type

[**Drugs**](Drugs.md)

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

