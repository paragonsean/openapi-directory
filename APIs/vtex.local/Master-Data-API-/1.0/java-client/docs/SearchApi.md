# SearchApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchdocuments**](SearchApi.md#searchdocuments) | **GET** /api/dataentities/{dataEntityName}/search | Search documents |


<a id="searchdocuments"></a>
# **searchdocuments**
> searchdocuments(dataEntityName, contentType, accept, reSTRange, fields, where, schema, keyword, sort)

Search documents

Retrieves documents&#39; information, while choosing which fields will be returned and filtering documents by specific fields.    &gt; The response header &#x60;REST-Content-Range&#x60; indicates the total amount of results for that specific search. For example, it may return &#x60;resources 0-100/136108&#x60;, which indicates it has returned results from 0 to 100 of a total 136108.    Below you can see some query examples and learn more about each query parameter.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;503&#x60;.    ## Query examples    ### Simple filter    &#x60;&#x60;&#x60;  /dataentities/Client/search?email&#x3D;my@email.com  &#x60;&#x60;&#x60;    ### Complex filter    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;(firstName&#x3D;Jon OR lastName&#x3D;Smith) OR (createdIn between 2001-01-01 AND 2016-01-01)  &#x60;&#x60;&#x60;    ### Date Range    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;createdIn between 2001-01-01 AND 2016-01-01  &#x60;&#x60;&#x60;    ### Range numeric fields    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;age between 18 AND 25  &#x60;&#x60;&#x60;    ### Partial filter    &#x60;&#x60;&#x60;  /dataentities/Client/search?firstName&#x3D;*Maria*  &#x60;&#x60;&#x60;    ### Filter for null values    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;firstName is null  &#x60;&#x60;&#x60;    ### Filter for non-null values    &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;firstName is not null  &#x60;&#x60;&#x60;    ### Filter for difference  &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;firstName&lt;&gt;maria  &#x60;&#x60;&#x60;    ### Filter greater than or less than  &#x60;&#x60;&#x60;  /dataentities/Client/search?_where&#x3D;number&gt;5  /dataentities/Client/search?_where&#x3D;date&lt;2001-01-01  &#x60;&#x60;&#x60;

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.SearchApi;

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

    SearchApi apiInstance = new SearchApi(defaultClient);
    String dataEntityName = "Client"; // String | Name of the data entity. Defined by the api. Examples of native data entities you can use are `CL` for client profiles and `AD` for client addresses.
    String contentType = "application/json"; // String | Type of the content being sent.
    String accept = "application/json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand.
    String reSTRange = "resources=0-10"; // String | Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query.
    String fields = "email,firstName,document"; // String | Fields that should be returned by document. Separate fields' names with commas. For example `_fields=email,firstName,document`. You can also use `_all` to fetch all fields.
    String where = "firstName is not null."; // String | Filter specification.
    String schema = "schema"; // String | Name of the schema the document to be created needs to be compliant with.
    String keyword = "String to search"; // String | String to search. Use quotes for a partial query. For example, `_keyword=Maria` or `_keyword=\"Maria\"`.
    String sort = "firstName ASC"; // String | Sets sorting mode in two parts. The first part is the name of the field you want to sort by. In the second part, use `ASC` for ascending or `DESC` for descending.
    try {
      apiInstance.searchdocuments(dataEntityName, contentType, accept, reSTRange, fields, where, schema, keyword, sort);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchdocuments");
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
| **503** | Service Unavailable |  -  |

