# PeopleApi

All URIs are relative to *https://etmdb.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**peopleSearchRead**](PeopleApi.md#peopleSearchRead) | **GET** /api/v1/people/search/{user} | Return cast search result |


<a id="peopleSearchRead"></a>
# **peopleSearchRead**
> peopleSearchRead(user)

Return cast search result

Return cast search result  ### Response Class (Status 200) __{param}__ argument can be * artist first name * artist last name * artist username  For more details on how cast are listed [see here][ref]. [ref]: https://etmdb.com/en/cast-list/-updated_date

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.PeopleApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://etmdb.com");

    PeopleApi apiInstance = new PeopleApi(defaultClient);
    String user = "user_example"; // String | 
    try {
      apiInstance.peopleSearchRead(user);
    } catch (ApiException e) {
      System.err.println("Exception when calling PeopleApi#peopleSearchRead");
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
| **user** | **String**|  | |

### Return type

null (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** |  |  -  |

