# ApplicationApi

All URIs are relative to *http://localhost:8080/exist/apps/WeGA-WebApp/api/v1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**applicationNewIDGet**](ApplicationApi.md#applicationNewIDGet) | **GET** /application/newID | Create a new WeGA ID |
| [**applicationStatusGet**](ApplicationApi.md#applicationStatusGet) | **GET** /application/status | Get status information about the running WeGA-WebApp |


<a id="applicationNewIDGet"></a>
# **applicationNewIDGet**
> ApplicationNewIDGet200Response applicationNewIDGet(docType)

Create a new WeGA ID

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    List<String> docType = Arrays.asList(); // List<String> | The WeGA document type
    try {
      ApplicationNewIDGet200Response result = apiInstance.applicationNewIDGet(docType);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationNewIDGet");
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
| **docType** | [**List&lt;String&gt;**](String.md)| The WeGA document type | [enum: biblio, diaries, documents, letters, news, orgs, persons, places, thematicCommentaries, var, works, writings] |

### Return type

[**ApplicationNewIDGet200Response**](ApplicationNewIDGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | A single object with a fresh WeGA ID |  -  |
| **403** | The creation of new IDs is only available in the development environment |  -  |
| **0** | Unexpected error |  -  |

<a id="applicationStatusGet"></a>
# **applicationStatusGet**
> ApplicationStatusGet200Response applicationStatusGet()

Get status information about the running WeGA-WebApp

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ApplicationApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://localhost:8080/exist/apps/WeGA-WebApp/api/v1");

    ApplicationApi apiInstance = new ApplicationApi(defaultClient);
    try {
      ApplicationStatusGet200Response result = apiInstance.applicationStatusGet();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ApplicationApi#applicationStatusGet");
      System.err.println("Status code: " + e.getCode());
      System.err.println("Reason: " + e.getResponseBody());
      System.err.println("Response headers: " + e.getResponseHeaders());
      e.printStackTrace();
    }
  }
}
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApplicationStatusGet200Response**](ApplicationStatusGet200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Healthy – A single object with status information |  -  |
| **500** | Unhealthy – A single object with status information |  -  |
| **0** | Unexpected error |  -  |

