# SystemApi

All URIs are relative to *http://demo.akeneo.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**getSystemInformation**](SystemApi.md#getSystemInformation) | **GET** /api/rest/v1/system-information | Get system information |


<a id="getSystemInformation"></a>
# **getSystemInformation**
> GetSystemInformation200Response getSystemInformation()

Get system information

This endpoint allows you to get the version and the edition of the PIM. Example of what you can get &lt;table class&#x3D;\&quot;description-table\&quot;&gt; &lt;thead&gt; &lt;tr&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Environment&lt;/th&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Edition&lt;/th&gt; &lt;th align&#x3D;\&quot;center\&quot;&gt;Version&lt;/th&gt; &lt;/tr&gt; &lt;/thead&gt; &lt;tbody&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;SaaS EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;Serenity&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;v20230112013744&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;SaaS CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;GE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;v20210526040645&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;PaaS or onPrem EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;EE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;5.0.28&lt;/td&gt; &lt;/tr&gt; &lt;tr&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;PaaS or onPrem CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;CE&lt;/td&gt; &lt;td align&#x3D;\&quot;center\&quot;&gt;5.0.28&lt;/td&gt; &lt;/tr&gt; &lt;/tbody&gt; &lt;/table&gt;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SystemApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://demo.akeneo.com");

    SystemApi apiInstance = new SystemApi(defaultClient);
    try {
      GetSystemInformation200Response result = apiInstance.getSystemInformation();
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SystemApi#getSystemInformation");
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

[**GetSystemInformation200Response**](GetSystemInformation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, edition, version, code, message

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return the version and the edition of the PIM. |  -  |
| **406** | Not Acceptable |  -  |

