# LabelsApi

All URIs are relative to *https://azure.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**checkLabels**](LabelsApi.md#checkLabels) | **HEAD** /labels | Requests the headers and status of the given resource. |
| [**getLabels**](LabelsApi.md#getLabels) | **GET** /labels | Gets a list of labels. |


<a id="checkLabels"></a>
# **checkLabels**
> checkLabels(apiVersion, name, syncToken, after, acceptDatetime, $select)

Requests the headers and status of the given resource.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String name = "name_example"; // String | A filter for the name of the returned labels.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      apiInstance.checkLabels(apiVersion, name, syncToken, after, acceptDatetime, $select);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#checkLabels");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **name** | **String**| A filter for the name of the returned labels. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: name] |

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
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

<a id="getLabels"></a>
# **getLabels**
> LabelListResult getLabels(apiVersion, name, syncToken, after, acceptDatetime, $select)

Gets a list of labels.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.LabelsApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://azure.local");

    LabelsApi apiInstance = new LabelsApi(defaultClient);
    String apiVersion = "apiVersion_example"; // String | The API version to be used with the HTTP request.
    String name = "name_example"; // String | A filter for the name of the returned labels.
    String syncToken = "syncToken_example"; // String | Used to guarantee real-time consistency between requests.
    String after = "after_example"; // String | Instructs the server to return elements that appear after the element referred to by the specified token.
    String acceptDatetime = "acceptDatetime_example"; // String | Requests the server to respond with the state of the resource at the specified time.
    List<String> $select = Arrays.asList(); // List<String> | Used to select what fields are present in the returned resource(s).
    try {
      LabelListResult result = apiInstance.getLabels(apiVersion, name, syncToken, after, acceptDatetime, $select);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling LabelsApi#getLabels");
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
| **apiVersion** | **String**| The API version to be used with the HTTP request. | |
| **name** | **String**| A filter for the name of the returned labels. | [optional] |
| **syncToken** | **String**| Used to guarantee real-time consistency between requests. | [optional] |
| **after** | **String**| Instructs the server to return elements that appear after the element referred to by the specified token. | [optional] |
| **acceptDatetime** | **String**| Requests the server to respond with the state of the resource at the specified time. | [optional] |
| **$select** | [**List&lt;String&gt;**](String.md)| Used to select what fields are present in the returned resource(s). | [optional] [enum: name] |

### Return type

[**LabelListResult**](LabelListResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.microsoft.appconfig.labelset+json, application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  * Sync-Token - Enables real-time consistency between requests by providing the returned value in the next request made to the server. <br>  |
| **0** | Error response describing why the operation failed |  -  |

