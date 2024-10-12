# EditSubaccountApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subaccountEdit**](EditSubaccountApi.md#subaccountEdit) | **PUT** /subaccount | Edit a subaccount |


<a id="subaccountEdit"></a>
# **subaccountEdit**
> SubaccountResponse subaccountEdit(subaccountRequest)

Edit a subaccount

Edit a subaccount

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.EditSubaccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    EditSubaccountApi apiInstance = new EditSubaccountApi(defaultClient);
    SubaccountRequest subaccountRequest = new SubaccountRequest(); // SubaccountRequest | edit sub account request
    try {
      SubaccountResponse result = apiInstance.subaccountEdit(subaccountRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling EditSubaccountApi#subaccountEdit");
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
| **subaccountRequest** | [**SubaccountRequest**](SubaccountRequest.md)| edit sub account request | |

### Return type

[**SubaccountResponse**](SubaccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

