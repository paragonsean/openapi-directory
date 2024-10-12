# OntolIdentifierApi

All URIs are relative to */api*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getOntolIdentifierResource**](OntolIdentifierApi.md#getOntolIdentifierResource) | **GET** /ontol/identifier/ | Fetches a map from CURIEs/IDs to labels |
| [**postOntolIdentifierResource**](OntolIdentifierApi.md#postOntolIdentifierResource) | **POST** /ontol/identifier/ | Fetches a map from CURIEs/IDs to labels |


<a id="getOntolIdentifierResource"></a>
# **getOntolIdentifierResource**
> getOntolIdentifierResource(label)

Fetches a map from CURIEs/IDs to labels

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntolIdentifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntolIdentifierApi apiInstance = new OntolIdentifierApi(defaultClient);
    List<String> label = Arrays.asList(); // List<String> | List of labels
    try {
      apiInstance.getOntolIdentifierResource(label);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntolIdentifierApi#getOntolIdentifierResource");
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
| **label** | [**List&lt;String&gt;**](String.md)| List of labels | |

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
| **200** | Success |  -  |

<a id="postOntolIdentifierResource"></a>
# **postOntolIdentifierResource**
> postOntolIdentifierResource(label)

Fetches a map from CURIEs/IDs to labels

Takes &#39;label&#39; list argument either as a querystring argument or as a key in the POST body when content-type is application/json.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.OntolIdentifierApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("/api");

    OntolIdentifierApi apiInstance = new OntolIdentifierApi(defaultClient);
    List<String> label = Arrays.asList(); // List<String> | List of labels
    try {
      apiInstance.postOntolIdentifierResource(label);
    } catch (ApiException e) {
      System.err.println("Exception when calling OntolIdentifierApi#postOntolIdentifierResource");
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
| **label** | [**List&lt;String&gt;**](String.md)| List of labels | |

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
| **200** | Success |  -  |

