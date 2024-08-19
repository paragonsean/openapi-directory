# DigitalAccountReferenceNumberRetrievalApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**retrieveDigitalAccntRefNumList**](DigitalAccountReferenceNumberRetrievalApi.md#retrieveDigitalAccntRefNumList) | **POST** /send/v1/{partnerId}/digital-account/search | Used to retreive a digital account reference list from Incontrol  |


<a id="retrieveDigitalAccntRefNumList"></a>
# **retrieveDigitalAccntRefNumList**
> DigitalAccount90Wrapper retrieveDigitalAccntRefNumList(partnerId, digitalAccount)

Used to retreive a digital account reference list from Incontrol 

Used to retreive a digital account reference list from Incontrol 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalAccountReferenceNumberRetrievalApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    DigitalAccountReferenceNumberRetrievalApi apiInstance = new DigitalAccountReferenceNumberRetrievalApi(defaultClient);
    String partnerId = "partnerId_example"; // String | Path Param - Provider assigned partner id. Details - string, 32
    DigitalAccount89Wrapper digitalAccount = new DigitalAccount89Wrapper(); // DigitalAccount89Wrapper | Contains the details of the request message.
    try {
      DigitalAccount90Wrapper result = apiInstance.retrieveDigitalAccntRefNumList(partnerId, digitalAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalAccountReferenceNumberRetrievalApi#retrieveDigitalAccntRefNumList");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id. Details - string, 32 | |
| **digitalAccount** | [**DigitalAccount89Wrapper**](DigitalAccount89Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**DigitalAccount90Wrapper**](DigitalAccount90Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a retrieve digital account reference number |  -  |

