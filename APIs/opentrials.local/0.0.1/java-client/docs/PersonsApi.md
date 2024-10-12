# PersonsApi

All URIs are relative to *http://opentrials.local/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getPerson**](PersonsApi.md#getPerson) | **GET** /persons/{id} |  |


<a id="getPerson"></a>
# **getPerson**
> Person getPerson(id)



Returns person details

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PersonsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://opentrials.local/v1");

    PersonsApi apiInstance = new PersonsApi(defaultClient);
    String id = "id_example"; // String | ID of the person
    try {
      Person result = apiInstance.getPerson(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling PersonsApi#getPerson");
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
| **id** | **String**| ID of the person | |

### Return type

[**Person**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |
| **404** | Person not found |  -  |
| **0** | Error |  -  |

