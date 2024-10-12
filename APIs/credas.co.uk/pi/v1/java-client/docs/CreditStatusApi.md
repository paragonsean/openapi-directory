# CreditStatusApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkCreditStatus**](CreditStatusApi.md#checkCreditStatus) | **POST** /api/credit-status/perform | Check includes identifying bankruptcy, insolvency, CCJ&#39;s or Company Directorship. |


<a id="checkCreditStatus"></a>
# **checkCreditStatus**
> CredasApiModelsStatusChecksStatusCheck checkCreditStatus(apikey, credasApiModelsStatusChecksStatusCheckRequest)

Check includes identifying bankruptcy, insolvency, CCJ&#39;s or Company Directorship.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditStatusApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    CreditStatusApi apiInstance = new CreditStatusApi(defaultClient);
    String apikey = "apikey_example"; // String | ApiKey supplied.
    CredasApiModelsStatusChecksStatusCheckRequest credasApiModelsStatusChecksStatusCheckRequest = new CredasApiModelsStatusChecksStatusCheckRequest(); // CredasApiModelsStatusChecksStatusCheckRequest | Object containing data required to perform the check.
    try {
      CredasApiModelsStatusChecksStatusCheck result = apiInstance.checkCreditStatus(apikey, credasApiModelsStatusChecksStatusCheckRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditStatusApi#checkCreditStatus");
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
| **credasApiModelsStatusChecksStatusCheckRequest** | [**CredasApiModelsStatusChecksStatusCheckRequest**](CredasApiModelsStatusChecksStatusCheckRequest.md)| Object containing data required to perform the check. | [optional] |

### Return type

[**CredasApiModelsStatusChecksStatusCheck**](CredasApiModelsStatusChecksStatusCheck.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/*+json, application/*+xml, application/json, application/json-patch+json, application/xml, text/json, text/xml
 - **Accept**: application/json, application/xml, text/json, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **400** | If the service was supplied invalid data. |  -  |
| **401** | If credentials supplied were invalid. |  -  |
| **402** | Error code meaning that the operation was aborted due to insufficient credits. |  -  |
| **500** | If an unexpected exception occurred whilst processing the request. |  -  |

