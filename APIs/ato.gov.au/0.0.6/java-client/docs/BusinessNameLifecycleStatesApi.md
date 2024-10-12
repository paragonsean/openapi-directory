# BusinessNameLifecycleStatesApi

All URIs are relative to *http://api.abr.ato.gov.au*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**classificationsBusinessNameLifecycleStatesGet**](BusinessNameLifecycleStatesApi.md#classificationsBusinessNameLifecycleStatesGet) | **GET** /classifications/business-name-lifecycle-states | Retrieve a list of business name lifecycle states |


<a id="classificationsBusinessNameLifecycleStatesGet"></a>
# **classificationsBusinessNameLifecycleStatesGet**
> List&lt;BusinessNameLifecycleState&gt; classificationsBusinessNameLifecycleStatesGet(apiKey)

Retrieve a list of business name lifecycle states

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.BusinessNameLifecycleStatesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.abr.ato.gov.au");

    BusinessNameLifecycleStatesApi apiInstance = new BusinessNameLifecycleStatesApi(defaultClient);
    String apiKey = "apiKey_example"; // String | The API key.
    try {
      List<BusinessNameLifecycleState> result = apiInstance.classificationsBusinessNameLifecycleStatesGet(apiKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling BusinessNameLifecycleStatesApi#classificationsBusinessNameLifecycleStatesGet");
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
| **apiKey** | **String**| The API key. | |

### Return type

[**List&lt;BusinessNameLifecycleState&gt;**](BusinessNameLifecycleState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Business name lifecycle states were retrieved successfully |  * Link - Information about pagination is provided in the [Link](https://tools.ietf.org/html/rfc5988#page-6) header. For example:      Link: &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;2&gt;; rel&#x3D;\&quot;next\&quot;,           &lt;https://api.abr.ato.gov.au/individuals?page&#x3D;34&gt;; rel&#x3D;\&quot;last\&quot;  &#x60;rel&#x3D;\&quot;next\&quot;&#x60; states that the next page is &#x60;page&#x3D;2&#x60;. This makes sense, since by default, all paginated queries start at page &#x60;1&#x60;. &#x60;rel&#x3D;\&quot;last\&quot;&#x60; provides some more information, stating that the last page of results is on &#x60;page 34&#x60;. Accordingly, we have 33 more pages of information that we can consume.  <br>  |
| **401** | Request not authenticated due to missing, invalid, or expired token |  -  |
| **404** | The specified resource was not found |  -  |

