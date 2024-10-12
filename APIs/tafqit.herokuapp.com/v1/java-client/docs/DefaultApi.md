# DefaultApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**convert**](DefaultApi.md#convert) | **POST** /convert |  |


<a id="convert"></a>
# **convert**
> convert(hundredsForm, theNumber, unit)



Convert the number into its Arabic text representation حول العدد إلى ما يقابله كتابة

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String hundredsForm = "hundredsForm_example"; // String | Some use مائة others use مئة , both works in Arabic. If left empty the default is مائة 
    String theNumber = "theNumber_example"; // String | Put the number here. Decimal is supported by most units.
    String unit = "unit_example"; // String | The counted subject, be it a currency like درهم إماراتي  or a size unit like متر مربع If the unit does not appear in the text result, it may not be supported. Please contact us to add it.
    try {
      apiInstance.convert(hundredsForm, theNumber, unit);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#convert");
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
| **hundredsForm** | **String**| Some use مائة others use مئة , both works in Arabic. If left empty the default is مائة  | [optional] |
| **theNumber** | **String**| Put the number here. Decimal is supported by most units. | [optional] |
| **unit** | **String**| The counted subject, be it a currency like درهم إماراتي  or a size unit like متر مربع If the unit does not appear in the text result, it may not be supported. Please contact us to add it. | [optional] |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | number converted to text successfully, تمت عملية التفقيط بنجاح |  -  |

