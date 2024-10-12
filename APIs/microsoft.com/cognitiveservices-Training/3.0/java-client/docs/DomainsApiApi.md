# DomainsApiApi

All URIs are relative to *https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getDomain**](DomainsApiApi.md#getDomain) | **GET** /domains/{domainId} | Get information about a specific domain. |
| [**getDomains**](DomainsApiApi.md#getDomains) | **GET** /domains | Get a list of the available domains. |


<a id="getDomain"></a>
# **getDomain**
> Domain getDomain(domainId, trainingKey)

Get information about a specific domain.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    UUID domainId = UUID.fromString("b30a91ae-e3c1-4f73-a81e-c270bff27c39"); // UUID | The id of the domain to get information about.
    String trainingKey = "{API Key}"; // String | API key.
    try {
      Domain result = apiInstance.getDomain(domainId, trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#getDomain");
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
| **domainId** | **UUID**| The id of the domain to get information about. | |
| **trainingKey** | **String**| API key. | |

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

<a id="getDomains"></a>
# **getDomains**
> List&lt;Domain&gt; getDomains(trainingKey)

Get a list of the available domains.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DomainsApiApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://southcentralus.api.cognitive.microsoft.com/customvision/v3.0/training");

    DomainsApiApi apiInstance = new DomainsApiApi(defaultClient);
    String trainingKey = "{API Key}"; // String | API key.
    try {
      List<Domain> result = apiInstance.getDomains(trainingKey);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DomainsApiApi#getDomains");
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
| **trainingKey** | **String**| API key. | |

### Return type

[**List&lt;Domain&gt;**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **0** | Error response |  -  |

