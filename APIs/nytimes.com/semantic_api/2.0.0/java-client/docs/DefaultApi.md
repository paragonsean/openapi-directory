# DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/semantic/v2/concept*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**nameConceptTypeSpecificConceptJsonGet**](DefaultApi.md#nameConceptTypeSpecificConceptJsonGet) | **GET** /name/{concept-type}/{specific-concept}.json |  |
| [**searchJsonGet**](DefaultApi.md#searchJsonGet) | **GET** /search.json |  |


<a id="nameConceptTypeSpecificConceptJsonGet"></a>
# **nameConceptTypeSpecificConceptJsonGet**
> NameConceptTypeSpecificConceptJsonGet200Response nameConceptTypeSpecificConceptJsonGet(conceptType, specificConcept, query, fields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/semantic/v2/concept");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String conceptType = "nytd_geo"; // String | The type of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined as a name-value pair, as in \"concept_type=[nytd_geo|nytd_per|nytd_org|nytd_des]\". 
    String specificConcept = "specificConcept_example"; // String | The name of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined in the URI path, as the element immediately preceding \".json\" like with \"Baseball.json\". 
    String query = "query_example"; // String | Precedes the search term string. Used in a Search Query. Except for &lt;specific_concept_name&gt;, Search Query will take the required parameters listed above (&lt;concept_type&gt;, &lt;concept_uri&gt;, &lt;article_uri&gt;) as an optional_parameter in addition to the query=&lt;query_term&gt;.
    String fields = "all"; // String | \"all\" or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept. 
    try {
      NameConceptTypeSpecificConceptJsonGet200Response result = apiInstance.nameConceptTypeSpecificConceptJsonGet(conceptType, specificConcept, query, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#nameConceptTypeSpecificConceptJsonGet");
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
| **conceptType** | **String**| The type of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined as a name-value pair, as in \&quot;concept_type&#x3D;[nytd_geo|nytd_per|nytd_org|nytd_des]\&quot;.  | [enum: nytd_geo, nytd_per, nytd_org, nytd_des] |
| **specificConcept** | **String**| The name of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined in the URI path, as the element immediately preceding \&quot;.json\&quot; like with \&quot;Baseball.json\&quot;.  | |
| **query** | **String**| Precedes the search term string. Used in a Search Query. Except for &amp;lt;specific_concept_name&amp;gt;, Search Query will take the required parameters listed above (&amp;lt;concept_type&amp;gt;, &amp;lt;concept_uri&amp;gt;, &amp;lt;article_uri&amp;gt;) as an optional_parameter in addition to the query&#x3D;&amp;lt;query_term&amp;gt;. | |
| **fields** | **String**| \&quot;all\&quot; or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept.  | [optional] [enum: all, pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query] |

### Return type

[**NameConceptTypeSpecificConceptJsonGet200Response**](NameConceptTypeSpecificConceptJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Concepts |  -  |

<a id="searchJsonGet"></a>
# **searchJsonGet**
> SearchJsonGet200Response searchJsonGet(query, offset, fields)



### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.DefaultApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("http://api.nytimes.com/svc/semantic/v2/concept");
    
    // Configure API key authorization: apikey
    ApiKeyAuth apikey = (ApiKeyAuth) defaultClient.getAuthentication("apikey");
    apikey.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //apikey.setApiKeyPrefix("Token");

    DefaultApi apiInstance = new DefaultApi(defaultClient);
    String query = "query_example"; // String | Precedes the search term string. Used in a Search Query. Except for &lt;specific_concept_name&gt;, Search Query will take the required parameters listed above (&lt;concept_type&gt;, &lt;concept_uri&gt;, &lt;article_uri&gt;) as an optional_parameter in addition to the query=&lt;query_term&gt;.
    Integer offset = 10; // Integer | Integer value for the index count from the first concept to the last concept, sorted alphabetically. Used in a Search Query. A Search Query will return up to 10 concepts in its results.
    String fields = "all"; // String | \"all\" or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept. 
    try {
      SearchJsonGet200Response result = apiInstance.searchJsonGet(query, offset, fields);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling DefaultApi#searchJsonGet");
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
| **query** | **String**| Precedes the search term string. Used in a Search Query. Except for &amp;lt;specific_concept_name&amp;gt;, Search Query will take the required parameters listed above (&amp;lt;concept_type&amp;gt;, &amp;lt;concept_uri&amp;gt;, &amp;lt;article_uri&amp;gt;) as an optional_parameter in addition to the query&#x3D;&amp;lt;query_term&amp;gt;. | |
| **offset** | **Integer**| Integer value for the index count from the first concept to the last concept, sorted alphabetically. Used in a Search Query. A Search Query will return up to 10 concepts in its results. | [optional] [default to 10] |
| **fields** | **String**| \&quot;all\&quot; or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept.  | [optional] [enum: all, pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query] |

### Return type

[**SearchJsonGet200Response**](SearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | An array of Concepts |  -  |

