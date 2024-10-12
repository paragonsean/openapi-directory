# SearchApi

All URIs are relative to *https://vtex.local*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchdocuments**](SearchApi.md#searchdocuments) | **GET** /api/dataentities/{acronym}/search | Search documents |


<a id="searchdocuments"></a>
# **searchdocuments**
> searchdocuments(contentType, accept, reSTRange, acronym, fields, where, schema, keyword, sort)

Search documents

Search documents by the query parameters described below.    &gt; Avoid sending too many requests with wildcards (&#x60;*&#x60;) in the search parameters or that use the &#x60;keyword&#x60; parameter. This may lead to this endpoint being temporarily blocked for your account. If this happens you will receive an error with status code &#x60;503&#x60;.

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
    String contentType = "application/json"; // String | Type of the content being sent
    String accept = "application/vnd.vtex.ds.v10+json"; // String | HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand 
    String reSTRange = "resources=0-10"; // String | Range of documents to show
    String acronym = "{{acronym}}"; // String | Identifies the kind of data
    String fields = "email,firstName,document"; // String | Fields that will be returned by document
    String where = "firstName is not null"; // String | Specification of filters. As seen below
    String schema = "{{schema}}"; // String | Enter with the name of the schema to filter documents by compatibility of the schema.
    String keyword = "String to search"; // String | String to search
    String sort = "firstName ASC"; // String | Use ASC value to sort ascending or DESC value to sort descending. 
    try {
      apiInstance.searchdocuments(contentType, accept, reSTRange, acronym, fields, where, schema, keyword, sort);
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
| **contentType** | **String**| Type of the content being sent | [default to application/json] |
| **accept** | **String**| HTTP Client Negotiation _Accept_ Header. Indicates the types of responses the client can understand  | [default to application/vnd.vtex.ds.v10+json] |
| **reSTRange** | **String**| Range of documents to show | [default to resources&#x3D;0-10] |
| **acronym** | **String**| Identifies the kind of data | [default to {{acronym}}] |
| **fields** | **String**| Fields that will be returned by document | [optional] [default to email,firstName,document] |
| **where** | **String**| Specification of filters. As seen below | [optional] [default to firstName is not null] |
| **schema** | **String**| Enter with the name of the schema to filter documents by compatibility of the schema. | [optional] [default to {{schema}}] |
| **keyword** | **String**| String to search | [optional] [default to String to search] |
| **sort** | **String**| Use ASC value to sort ascending or DESC value to sort descending.  | [optional] [default to firstName ASC] |

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
| **200** | Use this endpoint to search Master Data v1 documents with highly customizable filters.    ## Headers    | Name |  |  | -------- | -------- |  | Content-Type | application/json |  | Accept | application/vnd.vtex.ds.v10+json |  | x-vtex-api-appKey | App Key |  | x-vtex-api-appToken | App Token |  | REST-Range | Defines the collection of documents to be returned. A range within the collection limited by 100 documents per query. |      ## Querystring    &gt; Learn more about [Master Data v1 search queries](https://developers.vtex.com/vtex-rest-api/docs/how-the-queries-in-master-data-v1-work).    | Attribute | What it does |  | -------- | -------- |  | _fields | Fields that will be returned by document |  | _where | Specification of filters |  | _keyword | Search in all fields marked as searchable |  | _sort | Sort order |    ## How to fill the querystring attributes    1. _fields: Use the field names separated by commas. Ex. &#x60;_fields&#x3D;email,firstName,document&#x60;.  2. _where: See the query examples below to learn how to use filters.  3. _keyword: Enter the value you want to query. Use quotes for a partial query. Ex. &#x60;_keyword&#x3D;Maria&#x60; or &#x60;_keyword&#x3D;*Maria*&#x60;  4. _sort: Use &#x60;ASC&#x60; value to sort ascending or &#x60;DESC&#x60; value to sort descending. Ex. &#x60;_sort&#x3D;firstName ASC&#x60;.  5. If you want to fetch all fields use the &#x60;_all&#x60; parameter in the list of response fields. Ex: &#x60;_fields&#x3D;_all&#x60;      ## Query Examples:      ### Simple filter    &#x60;&#x60;&#x60;  /dataentities/CL/search?email&#x3D;my@email.com  &#x60;&#x60;&#x60;    ### Complex filter    &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;(firstName&#x3D;Jon OR lastName&#x3D;Smith) OR (createdIn between 2001-01-01 AND 2016-01-01)  &#x60;&#x60;&#x60;    ### Filter by range    #### Date Range    &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;createdIn between 2001-01-01 AND 2016-01-01  &#x60;&#x60;&#x60;    #### Range numeric fields    &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;age between 18 AND 25  &#x60;&#x60;&#x60;    ### Partial filter    &#x60;&#x60;&#x60;  /dataentities/CL/search?firstName&#x3D;*Maria*  &#x60;&#x60;&#x60;    ### Filter for null values    &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;firstName is null  &#x60;&#x60;&#x60;    ### Filter for non-null values    &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;firstName is not null  &#x60;&#x60;&#x60;    ### Filter for difference  &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;firstName&lt;&gt;maria  &#x60;&#x60;&#x60;    ### Filter greater than or less than  &#x60;&#x60;&#x60;  /dataentities/CL/search?_where&#x3D;number&gt;5  /dataentities/CL/search?_where&#x3D;date&lt;2001-01-01  &#x60;&#x60;&#x60; |  -  |
| **503** | Service Unavailable |  -  |

