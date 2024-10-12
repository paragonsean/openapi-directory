# CreditmemoIdEmailsApi

All URIs are relative to *https://example.com/rest/default*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**salesCreditmemoManagementV1NotifyPost**](CreditmemoIdEmailsApi.md#salesCreditmemoManagementV1NotifyPost) | **POST** /V1/creditmemo/{id}/emails | creditmemo/{id}/emails |


<a id="salesCreditmemoManagementV1NotifyPost"></a>
# **salesCreditmemoManagementV1NotifyPost**
> Boolean salesCreditmemoManagementV1NotifyPost(id)

creditmemo/{id}/emails

Emails a user a specified credit memo.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.CreditmemoIdEmailsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://example.com/rest/default");

    CreditmemoIdEmailsApi apiInstance = new CreditmemoIdEmailsApi(defaultClient);
    Integer id = 56; // Integer | The credit memo ID.
    try {
      Boolean result = apiInstance.salesCreditmemoManagementV1NotifyPost(id);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling CreditmemoIdEmailsApi#salesCreditmemoManagementV1NotifyPost");
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
| **id** | **Integer**| The credit memo ID. | |

### Return type

**Boolean**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | 200 Success. |  -  |
| **401** | 401 Unauthorized |  -  |
| **0** | Unexpected error |  -  |

