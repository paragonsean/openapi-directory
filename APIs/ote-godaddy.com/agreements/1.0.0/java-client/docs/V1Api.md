# V1Api

All URIs are relative to *http://api.ote-godaddy.com*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**get**](V1Api.md#get) | **GET** /v1/agreements | Retrieve Legal Agreements for provided agreements keys |


<a id="get"></a>
# **get**
> List&lt;LegalAgreement&gt; get(keys, xPrivateLabelId, xMarketId)

Retrieve Legal Agreements for provided agreements keys

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.V1Api;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.ote-godaddy.com");

    V1Api apiInstance = new V1Api(defaultClient);
    List<String> keys = Arrays.asList(); // List<String> | Keys for Agreements whose details are to be retrieved
    Integer xPrivateLabelId = 56; // Integer | PrivateLabelId to operate as, if different from JWT
    String xMarketId = "en-US"; // String | Unique identifier of the Market used to retrieve/translate Legal Agreements
    try {
      List<LegalAgreement> result = apiInstance.get(keys, xPrivateLabelId, xMarketId);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling V1Api#get");
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
| **keys** | [**List&lt;String&gt;**](String.md)| Keys for Agreements whose details are to be retrieved | |
| **xPrivateLabelId** | **Integer**| PrivateLabelId to operate as, if different from JWT | [optional] |
| **xMarketId** | **String**| Unique identifier of the Market used to retrieve/translate Legal Agreements | [optional] [default to en-US] |

### Return type

[**List&lt;LegalAgreement&gt;**](LegalAgreement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/javascript, application/json, application/xml, text/javascript, text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Request was successful |  -  |
| **400** | Request was malformed |  -  |
| **401** | Authentication info not sent or invalid |  -  |
| **403** | Authenticated user is not allowed access |  -  |
| **429** | Too many requests received within interval |  -  |
| **500** | Internal server error |  -  |

