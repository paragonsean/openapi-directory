# DigitalAccountReferenceNumberApi

All URIs are relative to *https://api.mastercard.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**createDigitalAccntRefNum**](DigitalAccountReferenceNumberApi.md#createDigitalAccntRefNum) | **POST** /send/v1/{partnerId}/digital-account | Used to create a digital account reference number from Incontrol  |


<a id="createDigitalAccntRefNum"></a>
# **createDigitalAccntRefNum**
> DigitalAccount87Wrapper createDigitalAccntRefNum(partnerId, digitalAccount)

Used to create a digital account reference number from Incontrol 

Used to create a digital account reference number from Incontrol 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DigitalAccountReferenceNumberApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com");

    DigitalAccountReferenceNumberApi apiInstance = new DigitalAccountReferenceNumberApi(defaultClient);
    String partnerId = "ptnr_A37V2q91WUqSonkfEG29Q-Bf4s9"; // String | Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32
    DigitalAccount86Wrapper digitalAccount = new DigitalAccount86Wrapper(); // DigitalAccount86Wrapper | Contains the details of the request message.
    try {
      DigitalAccount87Wrapper result = apiInstance.createDigitalAccntRefNum(partnerId, digitalAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DigitalAccountReferenceNumberApi#createDigitalAccntRefNum");
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
| **partnerId** | **String**| Path Param - Provider assigned partner id.   Type: Alphanumeric Special  [a-zA-Z0-9_-], Length: 32 | |
| **digitalAccount** | [**DigitalAccount86Wrapper**](DigitalAccount86Wrapper.md)| Contains the details of the request message. | [optional] |

### Return type

[**DigitalAccount87Wrapper**](DigitalAccount87Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Response details for a create digital account reference number |  -  |

