# DefaultApi

All URIs are relative to *https://api.ecowetter.de*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**publicHistoryGet**](DefaultApi.md#publicHistoryGet) | **GET** /public/history | Wetter 2021 für Berlin, Reichstag |


<a id="publicHistoryGet"></a>
# **publicHistoryGet**
> Object publicHistoryGet(q, from, to)

Wetter 2021 für Berlin, Reichstag

Abfrage der Wettervorhersage für einen Ort, der entweder durch Angabe eines Suchbegriffs mit dem Parameter &#x60;q&#x60; oder durch Geo-Koordinaten in den Parametern &#x60;lat&#x60; und &#x60;lon&#x60; spezifiziert wird.

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
    defaultClient.setBasePath("https://api.ecowetter.de");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String q = "Berlin, Reichstag"; // String | Ortssuche mit Freitext
    String from = "2021-01-01"; // String | Startdatum der Abfrage im Format (JJJJ-MM-DD)
    String to = "2022-01-01"; // String | Enddatum der Abfrage im Format (JJJJ-MM-DD)
    try {
      Object result = apiInstance.publicHistoryGet(q, from, to);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#publicHistoryGet");
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
| **q** | **String**| Ortssuche mit Freitext | [optional] |
| **from** | **String**| Startdatum der Abfrage im Format (JJJJ-MM-DD) | [optional] |
| **to** | **String**| Enddatum der Abfrage im Format (JJJJ-MM-DD) | [optional] |

### Return type

**Object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  * CF-Cache-Status -  <br>  * CF-RAY -  <br>  * Connection -  <br>  * Content-Encoding -  <br>  * Content-Type -  <br>  * Date -  <br>  * NEL -  <br>  * Report-To -  <br>  * Server -  <br>  * Transfer-Encoding -  <br>  * access-control-allow-origin -  <br>  * alt-svc -  <br>  * etag -  <br>  * x-rate-limit-limit -  <br>  * x-rate-limit-remaining -  <br>  * x-rate-limit-reset -  <br>  * x-request-compute -  <br>  * x-request-id -  <br>  * x-request-transfer -  <br>  * x-served-by -  <br>  * x-sessioncredit-compute -  <br>  * x-sessioncredit-start -  <br>  * x-sessioncredit-transfer -  <br>  |

