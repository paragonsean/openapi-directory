# ViewOnlyLinksApi

All URIs are relative to *https://api.test.osf.io/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**viewOnlyLinksNodeList**](ViewOnlyLinksApi.md#viewOnlyLinksNodeList) | **GET** /view_only_links/{link_id}/nodes/ | List all nodes |
| [**viewOnlyLinksRead**](ViewOnlyLinksApi.md#viewOnlyLinksRead) | **GET** /view_only_links/{link_id}/ | Retrieve a view only link |


<a id="viewOnlyLinksNodeList"></a>
# **viewOnlyLinksNodeList**
> List&lt;Node&gt; viewOnlyLinksNodeList(linkId)

List all nodes

 The list of nodes which this view only link gives read-only access to. #### Permissions Only project administrators may retrieve the nodes of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object containing &#x60;data&#x60; and &#x60;links&#x60; keys. The &#x60;data&#x60; key contains an array of up to 10 nodes. Each resource in the array is a separate node object and contains the full representation of the node, meaning additional requests to a node&#39;s detail view are not necessary.  The &#x60;links&#x60; key contains a dictionary of links that can be used for [pagination](#tag/Pagination).  If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewOnlyLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    ViewOnlyLinksApi apiInstance = new ViewOnlyLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | The unique identifier of the view only link.
    try {
      List<Node> result = apiInstance.viewOnlyLinksNodeList(linkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewOnlyLinksApi#viewOnlyLinksNodeList");
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
| **linkId** | **String**| The unique identifier of the view only link. | |

### Return type

[**List&lt;Node&gt;**](Node.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

<a id="viewOnlyLinksRead"></a>
# **viewOnlyLinksRead**
> ViewOnlyLinks viewOnlyLinksRead(linkId)

Retrieve a view only link

Retrieves details about a specific view only link. #### Permissions Only project administrators may retrieve the details of a view only link. Attempting to retrieve a view only link without appropriate permissions will result in a 403 Forbidden response. #### Returns Returns a JSON object with a &#x60;data&#x60; key containing the representation of the requested view only link, if the request is successful. If the request is unsuccessful, an &#x60;errors&#x60; key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ViewOnlyLinksApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.test.osf.io/v2");

    ViewOnlyLinksApi apiInstance = new ViewOnlyLinksApi(defaultClient);
    String linkId = "linkId_example"; // String | The unique identifier of the view only link.
    try {
      ViewOnlyLinks result = apiInstance.viewOnlyLinksRead(linkId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ViewOnlyLinksApi#viewOnlyLinksRead");
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
| **linkId** | **String**| The unique identifier of the view only link. | |

### Return type

[**ViewOnlyLinks**](ViewOnlyLinks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |

