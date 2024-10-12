# RepositoryCredentialsApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**addRepository**](RepositoryCredentialsApi.md#addRepository) | **POST** /repositories | Add repository to watch |


<a id="addRepository"></a>
# **addRepository**
> List&lt;Subscription&gt; addRepository(repository, autosubscribe, dryrun, xAnchoreAccount)

Add repository to watch



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.RepositoryCredentialsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost");

    RepositoryCredentialsApi apiInstance = new RepositoryCredentialsApi(defaultClient);
    String repository = "repository_example"; // String | full repository to add e.g. docker.io/library/alpine
    Boolean autosubscribe = true; // Boolean | flag to enable/disable auto tag_update activation when new images from a repo are added
    Boolean dryrun = true; // Boolean | flag to return tags in the repository without actually watching the repository, default is false
    String xAnchoreAccount = "xAnchoreAccount_example"; // String | An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    try {
      List<Subscription> result = apiInstance.addRepository(repository, autosubscribe, dryrun, xAnchoreAccount);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling RepositoryCredentialsApi#addRepository");
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
| **repository** | **String**| full repository to add e.g. docker.io/library/alpine | |
| **autosubscribe** | **Boolean**| flag to enable/disable auto tag_update activation when new images from a repo are added | [optional] |
| **dryrun** | **Boolean**| flag to return tags in the repository without actually watching the repository, default is false | [optional] |
| **xAnchoreAccount** | **String**| An account name to change the resource scope of the request to that account, if permissions allow (admin only) | [optional] |

### Return type

[**List&lt;Subscription&gt;**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Repository and discovered tags added |  -  |

