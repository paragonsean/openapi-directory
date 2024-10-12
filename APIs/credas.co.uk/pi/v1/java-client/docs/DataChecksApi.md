# DataChecksApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addDataCheck**](DataChecksApi.md#addDataCheck) | **POST** /api/datachecks | Creates new data check against a specified registration. |


<a id="addDataCheck"></a>
# **addDataCheck**
> CredasApiModelsDataCheckAddDataCheckResponse addDataCheck(apikey, credasApiModelsDataCheckAddDataCheckRequest)

Creates new data check against a specified registration.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DataChecksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    DataChecksApi apiInstance = new DataChecksApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsDataCheckAddDataCheckRequest credasApiModelsDataCheckAddDataCheckRequest = new CredasApiModelsDataCheckAddDataCheckRequest(); // CredasApiModelsDataCheckAddDataCheckRequest | Object containing data check details.
    try {
      CredasApiModelsDataCheckAddDataCheckResponse result = apiInstance.addDataCheck(apikey, credasApiModelsDataCheckAddDataCheckRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DataChecksApi#addDataCheck");
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
| **apikey** | **String**| ApiKey supplied. | |
| **credasApiModelsDataCheckAddDataCheckRequest** | [**CredasApiModelsDataCheckAddDataCheckRequest**](CredasApiModelsDataCheckAddDataCheckRequest.md)| Object containing data check details. | [optional] |

### Return type

[**CredasApiModelsDataCheckAddDataCheckResponse**](CredasApiModelsDataCheckAddDataCheckResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Details of newly added data check. |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | Error code meaning that the operation was aborted due to insufficient credits. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

