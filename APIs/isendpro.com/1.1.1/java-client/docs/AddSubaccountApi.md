# AddSubaccountApi

All URIs are relative to *https://apirest.isendpro.com/cgi-bin*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**subaccountAdd**](AddSubaccountApi.md#subaccountAdd) | **POST** /subaccount | Ajoute un sous compte |


<a id="subaccountAdd"></a>
# **subaccountAdd**
> SubaccountAddResponse subaccountAdd(subaccountAddRequest)

Ajoute un sous compte

Ajoute un sous compte

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.AddSubaccountApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://apirest.isendpro.com/cgi-bin");

    AddSubaccountApi apiInstance = new AddSubaccountApi(defaultClient);
    SubaccountAddRequest subaccountAddRequest = new SubaccountAddRequest(); // SubaccountAddRequest | add sub account request
    try {
      SubaccountAddResponse result = apiInstance.subaccountAdd(subaccountAddRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling AddSubaccountApi#subaccountAdd");
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
| **subaccountAddRequest** | [**SubaccountAddRequest**](SubaccountAddRequest.md)| add sub account request | |

### Return type

[**SubaccountAddResponse**](SubaccountAddResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, exemple1

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Reponse OK |  -  |
| **400** | Dysfonctionnement |  -  |

