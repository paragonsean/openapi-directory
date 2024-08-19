# ParametersApi

All URIs are relative to *https://api.mastercard.com/spendingpulse/v1/spulse.svc*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**parametersGet**](ParametersApi.md#parametersGet) | **GET** /parameters | Returns a distinct list of all reports are available and that one is subscribed to. |


<a id="parametersGet"></a>
# **parametersGet**
> ParameterListResponse parametersGet(currentRow, offset)

Returns a distinct list of all reports are available and that one is subscribed to.

Returns a distinct list of all reports are available and that one is subscribed to. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ParametersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.mastercard.com/spendingpulse/v1/spulse.svc");

    ParametersApi apiInstance = new ParametersApi(defaultClient);
    String currentRow = "1"; // String | Starting record number to return.
    String offset = "25"; // String | Used to restrict the number of records returned if needed to be less than max.
    try {
      ParameterListResponse result = apiInstance.parametersGet(currentRow, offset);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ParametersApi#parametersGet");
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
| **currentRow** | **String**| Starting record number to return. | [optional] |
| **offset** | **String**| Used to restrict the number of records returned if needed to be less than max. | [optional] |

### Return type

[**ParameterListResponse**](ParameterListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A List of Parameters |  -  |
| **0** | Unexpected errors |  -  |

