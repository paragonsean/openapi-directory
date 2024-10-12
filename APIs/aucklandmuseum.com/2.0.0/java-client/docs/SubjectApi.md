# SubjectApi

All URIs are relative to *http://api.aucklandmuseum.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSubject**](SubjectApi.md#getSubject) | **GET** /id/{identifier} | Explore details about a given subject node |


<a id="getSubject"></a>
# **getSubject**
> getSubject(identifier)

Explore details about a given subject node

Gets information about a &#x60;subject&#x60; identified by the &#x60;identifier&#x60;.  The response format depends upon the &#x60;Accept&#x60; header.   - &#x60;text/html&#x60; - the default response type. Returned data can be easily viewed in any modern Internet Browser   - &#x60;application/ld+json&#x60; - the response will be in [JSON-LD](http://json-ld.org/)   - &#x60;application/json&#x60; - the response will be a simple JSON Object with keys (predicates) and values (objects). 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SubjectApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.aucklandmuseum.com");

    SubjectApi apiInstance = new SubjectApi(defaultClient);
    String identifier = "identifier_example"; // String | The identifier path of the `subject` you're looking for 
    try {
      apiInstance.getSubject(identifier);
    } catch (ApiException e) {
      System.err.println("Exception when calling SubjectApi#getSubject");
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
| **identifier** | **String**| The identifier path of the &#x60;subject&#x60; you&#39;re looking for  | |

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
| **200** | &#x60;subject&#x60; found  |  -  |
| **404** | &#x60;subject&#x60; not found  |  -  |

