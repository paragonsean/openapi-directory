# HpoApi

All URIs are relative to *http://www.ebi.ac.uk/Tools/crossbar*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getHpoUsingGET**](HpoApi.md#getHpoUsingGET) | **GET** /hpo | Get HPO phenotypes data |


<a id="getHpoUsingGET"></a>
# **getHpoUsingGET**
> HpoEntities getHpoUsingGET(genesymbol, hpotermname, limit, page, synonym)

Get HPO phenotypes data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.HpoApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://www.ebi.ac.uk/Tools/crossbar");

    HpoApi apiInstance = new HpoApi(defaultClient);
    List<String> genesymbol = Arrays.asList(); // List<String> | genesymbol
    List<String> hpotermname = Arrays.asList(); // List<String> | hpotermname
    Integer limit = 10; // Integer | limit
    Integer page = 0; // Integer | page
    List<String> synonym = Arrays.asList(); // List<String> | synonym
    try {
      HpoEntities result = apiInstance.getHpoUsingGET(genesymbol, hpotermname, limit, page, synonym);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling HpoApi#getHpoUsingGET");
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
| **genesymbol** | [**List&lt;String&gt;**](String.md)| genesymbol | [optional] |
| **hpotermname** | [**List&lt;String&gt;**](String.md)| hpotermname | [optional] |
| **limit** | **Integer**| limit | [optional] [default to 10] |
| **page** | **Integer**| page | [optional] [default to 0] |
| **synonym** | [**List&lt;String&gt;**](String.md)| synonym | [optional] |

### Return type

[**HpoEntities**](HpoEntities.md)

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

