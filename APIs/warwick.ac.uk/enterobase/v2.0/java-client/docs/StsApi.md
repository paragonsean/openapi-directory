# StsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**apiV20DatabaseSchemeStsGet**](StsApi.md#apiV20DatabaseSchemeStsGet) | **GET** /api/v2.0/{database}/{scheme}/sts |  |


<a id="apiV20DatabaseSchemeStsGet"></a>
# **apiV20DatabaseSchemeStsGet**
> apiV20DatabaseSchemeStsGet(database, scheme2, barcode, stId, offset, showAlleles, onlyFields, reldate, limit, scheme)



ST profile data

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    StsApi apiInstance = new StsApi(defaultClient);
    String database = "database_example"; // String | Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
    String scheme2 = "scheme_example"; // String | 
    List<String> barcode = Arrays.asList(); // List<String> | Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
    String stId = "stId_example"; // String | 
    Integer offset = 0; // Integer | 
    Boolean showAlleles = true; // Boolean | 
    List<String> onlyFields = Arrays.asList(); // List<String> | 
    Integer reldate = 56; // Integer | 
    Integer limit = 50; // Integer | 
    String scheme = "scheme_example"; // String | 
    try {
      apiInstance.apiV20DatabaseSchemeStsGet(database, scheme2, barcode, stId, offset, showAlleles, onlyFields, reldate, limit, scheme);
    } catch (ApiException e) {
      System.err.println("Exception when calling StsApi#apiV20DatabaseSchemeStsGet");
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
| **database** | **String**| Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively | |
| **scheme2** | **String**|  | |
| **barcode** | [**List&lt;String&gt;**](String.md)| Unique barcode for Strain records, &lt;database prefix&gt;_&lt;ID code&gt; e.g. SAL_AA0001AA | [optional] |
| **stId** | **String**|  | [optional] |
| **offset** | **Integer**|  | [optional] [default to 0] |
| **showAlleles** | **Boolean**|  | [optional] |
| **onlyFields** | [**List&lt;String&gt;**](String.md)|  | [optional] |
| **reldate** | **Integer**|  | [optional] |
| **limit** | **Integer**|  | [optional] [default to 50] |
| **scheme** | **String**|  | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | List of sts objects |  -  |
| **400** | Malformed request, contains an error |  -  |
| **403** | Unauthorised access for this specific resource |  -  |

