# SearchApi

All URIs are relative to *https://api.ideaconsult.net/nanoreg1*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**solrqueryGet**](SearchApi.md#solrqueryGet) | **GET** /select | Apache Solr powered search |
| [**solrqueryPost**](SearchApi.md#solrqueryPost) | **POST** /select | Apache Solr powered search |


<a id="solrqueryGet"></a>
# **solrqueryGet**
> SolrResponse solrqueryGet(q, start, rows, wt)

Apache Solr powered search

GET is simpler to use, but imposes restrictions on the complexity and the lenght of the parameters.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String q = "*:*"; // String | The query
    Integer start = 0; // Integer | Starting page
    Integer rows = 10; // Integer | Page size
    String wt = "json"; // String | Response format
    try {
      SolrResponse result = apiInstance.solrqueryGet(q, start, rows, wt);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#solrqueryGet");
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
| **q** | **String**| The query | [optional] |
| **start** | **Integer**| Starting page | [optional] |
| **rows** | **Integer**| Page size | [optional] |
| **wt** | **String**| Response format | [optional] [default to xml] [enum: json, xml] |

### Return type

[**SolrResponse**](SolrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query performed successfully |  -  |
| **400** | BAD_REQUEST |  -  |
| **401** | UNAUTHORIZED |  -  |
| **403** | FORBIDDEN |  -  |
| **404** | NOT_FOUND |  -  |
| **409** | CONFLICT |  -  |
| **415** | UNSUPPORTED_MEDIA_TYPE |  -  |
| **500** | SERVER_ERROR |  -  |
| **503** | SERVICE_UNAVAILABLE |  -  |
| **510** | INVALID_STATE           |  -  |

<a id="solrqueryPost"></a>
# **solrqueryPost**
> SolrResponse solrqueryPost(wt, solrqueryPostRequest)

Apache Solr powered search

POST is more complex to use, but also allows for much for complex and lengthy queries.

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://api.ideaconsult.net/nanoreg1");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String wt = "json"; // String | Response format
    SolrqueryPostRequest solrqueryPostRequest = new SolrqueryPostRequest(); // SolrqueryPostRequest | a JSON object with Solr query parameters
    try {
      SolrResponse result = apiInstance.solrqueryPost(wt, solrqueryPostRequest);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#solrqueryPost");
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
| **wt** | **String**| Response format | [optional] [default to xml] [enum: json, xml] |
| **solrqueryPostRequest** | [**SolrqueryPostRequest**](SolrqueryPostRequest.md)| a JSON object with Solr query parameters | [optional] |

### Return type

[**SolrResponse**](SolrResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Query performed successfully |  -  |
| **400** | BAD_REQUEST |  -  |
| **401** | UNAUTHORIZED |  -  |
| **403** | FORBIDDEN |  -  |
| **404** | NOT_FOUND |  -  |
| **409** | CONFLICT |  -  |
| **415** | UNSUPPORTED_MEDIA_TYPE |  -  |
| **500** | SERVER_ERROR |  -  |
| **503** | SERVICE_UNAVAILABLE |  -  |
| **510** | INVALID_STATE |  -  |

