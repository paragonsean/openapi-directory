# StoriesApi

All URIs are relative to *http://api.nytimes.com/svc/search/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**articlesearchJsonGet**](StoriesApi.md#articlesearchJsonGet) | **GET** /articlesearch.json | Article Search |


<a id="articlesearchJsonGet"></a>
# **articlesearchJsonGet**
> ArticlesearchJsonGet200Response articlesearchJsonGet(q, fq, beginDate, endDate, sort, fl, hl, page, facetField, facetFilter)

Article Search

Article Search requests use the following URI structure: 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.StoriesApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/search/v2");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    StoriesApi apiInstance = new StoriesApi(defaultClient);
    String q = "q_example"; // String | Search query term. Search is performed on the article body, headline and byline. 
    String fq = "fq_example"; // String | \"Filtered search query using standard Lucene syntax.   The filter query can be specified with or without a limiting field: label.   See Filtering Your Search for more information about filtering.\" 
    String beginDate = "beginDate_example"; // String | \"Format: YYYYMMDD   Restricts responses to results with publication dates of the date specified or later.\" 
    String endDate = "endDate_example"; // String | \"Format: YYYYMMDD   Restricts responses to results with publication dates of the date specified or earlier.\" 
    String sort = "newest"; // String | \"By default, search results are sorted by their relevance to the query term (q). Use the sort parameter to sort by pub_date.\" 
    String fl = "fl_example"; // String | \"Comma-delimited list of fields (no limit)    Limits the fields returned in your search results. By default (unless you include an fl list in your request), the following fields are returned:       web_url      snippet      lead_paragraph      abstract      print_page      blog      source      multimedia      headline      keywords      pub_date      document_type      news_desk      byline      type_of_material      _id      word_count\" 
    Boolean hl = false; // Boolean | Enables highlighting in search results. When set to true, the query term (q) is highlighted in the headline and lead_paragraph fields.  Note: If highlighting is enabled, snippet will be returned even if it is not specified in your fl list.\" 
    Integer page = 0; // Integer | \"The value of page corresponds to a set of 10 results (it does not indicate the starting number of the result set). For example, page=0 corresponds to records 0-9. To return records 10-19, set page to 1, not 10.\" 
    String facetField = "facetField_example"; // String | Comma-delimited list of facets  Specifies the sets of facet values to include in the facets array at the end of response, which collects the facet values from all the search results. By default no facet fields will be returned. Below is the list of valid facets:  section_name  document_type  type_of_material  source  day_of_week  To learn more about using facets, see Using Facets. 
    Boolean facetFilter = false; // Boolean | When set to true, facet counts will respect any applied filters (fq, date range, etc.) in addition to the main query term. To filter facet counts, specifying at least one facet_field is required. To learn more about using facets, see Using Facets. 
    try {
      ArticlesearchJsonGet200Response result = apiInstance.articlesearchJsonGet(q, fq, beginDate, endDate, sort, fl, hl, page, facetField, facetFilter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling StoriesApi#articlesearchJsonGet");
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
| **q** | **String**| Search query term. Search is performed on the article body, headline and byline.  | [optional] |
| **fq** | **String**| \&quot;Filtered search query using standard Lucene syntax.   The filter query can be specified with or without a limiting field: label.   See Filtering Your Search for more information about filtering.\&quot;  | [optional] |
| **beginDate** | **String**| \&quot;Format: YYYYMMDD   Restricts responses to results with publication dates of the date specified or later.\&quot;  | [optional] |
| **endDate** | **String**| \&quot;Format: YYYYMMDD   Restricts responses to results with publication dates of the date specified or earlier.\&quot;  | [optional] |
| **sort** | **String**| \&quot;By default, search results are sorted by their relevance to the query term (q). Use the sort parameter to sort by pub_date.\&quot;  | [optional] [enum: newest, oldest] |
| **fl** | **String**| \&quot;Comma-delimited list of fields (no limit)    Limits the fields returned in your search results. By default (unless you include an fl list in your request), the following fields are returned:       web_url      snippet      lead_paragraph      abstract      print_page      blog      source      multimedia      headline      keywords      pub_date      document_type      news_desk      byline      type_of_material      _id      word_count\&quot;  | [optional] |
| **hl** | **Boolean**| Enables highlighting in search results. When set to true, the query term (q) is highlighted in the headline and lead_paragraph fields.  Note: If highlighting is enabled, snippet will be returned even if it is not specified in your fl list.\&quot;  | [optional] [default to false] |
| **page** | **Integer**| \&quot;The value of page corresponds to a set of 10 results (it does not indicate the starting number of the result set). For example, page&#x3D;0 corresponds to records 0-9. To return records 10-19, set page to 1, not 10.\&quot;  | [optional] [default to 0] |
| **facetField** | **String**| Comma-delimited list of facets  Specifies the sets of facet values to include in the facets array at the end of response, which collects the facet values from all the search results. By default no facet fields will be returned. Below is the list of valid facets:  section_name  document_type  type_of_material  source  day_of_week  To learn more about using facets, see Using Facets.  | [optional] |
| **facetFilter** | **Boolean**| When set to true, facet counts will respect any applied filters (fq, date range, etc.) in addition to the main query term. To filter facet counts, specifying at least one facet_field is required. To learn more about using facets, see Using Facets.  | [optional] [default to false] |

### Return type

[**ArticlesearchJsonGet200Response**](ArticlesearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | The docs requested by the article search. |  -  |

