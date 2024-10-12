# ScrollApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**scrolldocuments**](ScrollApi.md#scrolldocuments) | **GET** /api/dataentities/{dataEntityName}/scroll | Scroll documents |


<a id="scrolldocuments"></a>
# **scrolldocuments**
> scrolldocuments(dataEntityName, contentType, accept, reSTRange, token, fields, where, schema, keyword, sort)

Scroll documents

In the first request, the &#x60;X-VTEX-MD-TOKEN&#x60; token will be returned in the header. This token must be passed to the next request in the query string &#x60;_token&#x60; parameter. The token has a timeout of 10 minutes, which refreshes after each request.    After the token is obtained it is no longer necessary to send the filter or document size per page parameters. You only need to resend the token until the document collection is empty.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;429&#x60;.    ## Request examples    First request:  &#x60;&#x60;&#x60;  /dataentities/Client/scroll?isCluster&#x3D;true&amp;_size&#x3D;250&amp;_fields&#x3D;email,firstName  &#x60;&#x60;&#x60;    Retrieve the token in the header &#x60;X-VTEX-MD-TOKEN&#x60; from the first request&#39;s response and use it to make the next requests.    Subsequent requests:  &#x60;&#x60;&#x60;  /dataentities/Client/scroll?_token&#x3D;{tokenValueExample}  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ScrollApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://vtex.local");
    
    // Configure API key authorization: appToken
    ApiKeyAuth appToken = (ApiKeyAuth) defaultClient.getAuthentication("appToken");
    appToken.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appToken.setApiKeyPrefix("Token");

    // Configure API key authorization: appKey
    ApiKeyAuth appKey = (ApiKeyAuth) defaultClient.getAuthentication("appKey");
    appKey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //appKey.setApiKeyPrefix("Token");

    ScrollApi apiInstance = new ScrollApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String reSTRange = "resources=0-10"; // String | Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query.
    String token = "{tokenValueExample}"; // String | Value of the header `X-VTEX-MD-TOKEN` returned in your first request. Send its value in this query string in the subsequent requests. The token has a timeout of 10 minutes, which refreshes after each new request.
    String fields = "email,firstName,document"; // String | Fields that should be returned by document. Separate fields' names with commas. For example `_fields=email,firstName,document`. You can also use `_all` to fetch all fields.
    String where = "firstName is not null."; // String | Filter specification.
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    String keyword = "String to search"; // String | String to search. Use quotes for a partial query. For example, `_keyword=Maria` or `_keyword=\"Maria\"`.
    String sort = "firstName ASC"; // String | Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use `ASC` for ascending or `DESC` for descending.
    try {
      apiInstance.scrolldocuments(dataEntityName, contentType, accept, reSTRange, token, fields, where, schema, keyword, sort);
    } catch (ApiException e) {
      System.err.println("Exception when calling ScrollApi#scrolldocuments");
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
| **dataEntityName** | **String**| Name of the data entity. Defined by the api. Examples of native data entities you can use are &#x60;CL&#x60; for client profiles and &#x60;AD&#x60; for client addresses. | |
| **contentType** | **String**| Type of the content being sent. | |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand. | |
| **reSTRange** | **String**| Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query. | |
| **token** | **String**| Value of the header &#x60;X-VTEX-MD-TOKEN&#x60; returned in your first request. Send its value in this query string in the subsequent requests. The token has a timeout of 10 minutes, which refreshes after each new request. | [optional] [default to {tokenValueExample}] |
| **fields** | **String**| Fields that should be returned by document. Separate fields&#39; names with commas. For example &#x60;_fields&#x3D;email,firstName,document&#x60;. You can also use &#x60;_all&#x60; to fetch all fields. | [optional] [default to email,firstName,document] |
| **where** | **String**| Filter specification. | [optional] |
| **schema** | **String**| Name of the schema the document to be created needs to be compliant with. | [optional] |
| **keyword** | **String**| String to search. Use quotes for a partial query. For example, &#x60;_keyword&#x3D;Maria&#x60; or &#x60;_keyword&#x3D;\&quot;Maria\&quot;&#x60;. | [optional] |
| **sort** | **String**| Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use &#x60;ASC&#x60; for ascending or &#x60;DESC&#x60; for descending. | [optional] [default to firstName ASC] |

### Return type

null (empty response body)

### Authorization

[appToken](../README.md#appToken), [appKey](../README.md#appKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | OK |  -  |
| **429** | Too Many Requests |  -  |

