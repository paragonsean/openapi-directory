# DeedApi

All URIs are relative to *https://api.landregistry.gov.uk/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**deedDeedReferenceGet**](DeedApi.md#deedDeedReferenceGet) | **GET** /deed/{deed_reference} | Deed |


<a id="deedDeedReferenceGet"></a>
# **deedDeedReferenceGet**
> OperativeDeed deedDeedReferenceGet(deedReference)

Deed

The Deed endpoint returns details of a specific deed based on the unique deed reference. The response includes the Title Number, Property information, Borrower(s) information and deed information. 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DeedApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.landregistry.gov.uk/v1");

    DeedApi apiInstance = new DeedApi(defaultClient);
    String deedReference = "deedReference_example"; // String | Unique reference of the deed.
    try {
      OperativeDeed result = apiInstance.deedDeedReferenceGet(deedReference);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DeedApi#deedDeedReferenceGet");
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
| **deedReference** | **String**| Unique reference of the deed. | |

### Return type

[**OperativeDeed**](OperativeDeed.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A specific deed is returned |  -  |
| **404** | Deed not found |  -  |

