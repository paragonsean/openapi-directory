# OrganizersApi

All URIs are relative to *https://api.getgo.com/G2T/rest*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getAllOrganisers**](OrganizersApi.md#getAllOrganisers) | **GET** /accounts/{accountKey}/organizers | DEPRECATED: Get Organizers |


<a id="getAllOrganisers"></a>
# **getAllOrganisers**
> List&lt;Organizer&gt; getAllOrganisers(authorization, accountKey)

DEPRECATED: Get Organizers

DEPRECATED: Please use the Admin API call &#39;Get all users&#39; instead. For details see https://goto-developer.logmein.com/get-all-users.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OrganizersApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.getgo.com/G2T/rest");

    OrganizersApi apiInstance = new OrganizersApi(defaultClient);
    String authorization = "authorization_example"; // String | Access token
    Long accountKey = 56L; // Long | The key of the multi-user account
    try {
      List<Organizer> result = apiInstance.getAllOrganisers(authorization, accountKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling OrganizersApi#getAllOrganisers");
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
| **authorization** | **String**| Access token | |
| **accountKey** | **Long**| The key of the multi-user account | |

### Return type

[**List&lt;Organizer&gt;**](Organizer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **400** | Bad Request |  -  |
| **403** | Forbidden |  -  |

