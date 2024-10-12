# SemanticApi.DefaultApi

All URIs are relative to *http://api.nytimes.com/svc/semantic/v2/concept*

Method | HTTP request | Description
------------- | ------------- | -------------
[**nameConceptTypeSpecificConceptJsonGet**](DefaultApi.md#nameConceptTypeSpecificConceptJsonGet) | **GET** /name/{concept-type}/{specific-concept}.json | 
[**searchJsonGet**](DefaultApi.md#searchJsonGet) | **GET** /search.json | 



## nameConceptTypeSpecificConceptJsonGet

> NameConceptTypeSpecificConceptJsonGet200Response nameConceptTypeSpecificConceptJsonGet(conceptType, specificConcept, query, opts)



### Example

```javascript
import SemanticApi from 'semantic_api';
let defaultClient = SemanticApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new SemanticApi.DefaultApi();
let conceptType = "conceptType_example"; // String | The type of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined as a name-value pair, as in \"concept_type=[nytd_geo|nytd_per|nytd_org|nytd_des]\". 
let specificConcept = "specificConcept_example"; // String | The name of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined in the URI path, as the element immediately preceding \".json\" like with \"Baseball.json\". 
let query = "query_example"; // String | Precedes the search term string. Used in a Search Query. Except for &lt;specific_concept_name&gt;, Search Query will take the required parameters listed above (&lt;concept_type&gt;, &lt;concept_uri&gt;, &lt;article_uri&gt;) as an optional_parameter in addition to the query=&lt;query_term&gt;.
let opts = {
  'fields': "fields_example" // String | \"all\" or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept. 
};
apiInstance.nameConceptTypeSpecificConceptJsonGet(conceptType, specificConcept, query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conceptType** | **String**| The type of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined as a name-value pair, as in \&quot;concept_type&#x3D;[nytd_geo|nytd_per|nytd_org|nytd_des]\&quot;.  | 
 **specificConcept** | **String**| The name of the concept, used for Constructing a Semantic API Request by Concept Type and Specific Concept Name. The parameter is defined in the URI path, as the element immediately preceding \&quot;.json\&quot; like with \&quot;Baseball.json\&quot;.  | 
 **query** | **String**| Precedes the search term string. Used in a Search Query. Except for &amp;lt;specific_concept_name&amp;gt;, Search Query will take the required parameters listed above (&amp;lt;concept_type&amp;gt;, &amp;lt;concept_uri&amp;gt;, &amp;lt;article_uri&amp;gt;) as an optional_parameter in addition to the query&#x3D;&amp;lt;query_term&amp;gt;. | 
 **fields** | **String**| \&quot;all\&quot; or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept.  | [optional] 

### Return type

[**NameConceptTypeSpecificConceptJsonGet200Response**](NameConceptTypeSpecificConceptJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## searchJsonGet

> SearchJsonGet200Response searchJsonGet(query, opts)



### Example

```javascript
import SemanticApi from 'semantic_api';
let defaultClient = SemanticApi.ApiClient.instance;
// Configure API key authorization: apikey
let apikey = defaultClient.authentications['apikey'];
apikey.apiKey = 'YOUR API KEY';
// Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
//apikey.apiKeyPrefix = 'Token';

let apiInstance = new SemanticApi.DefaultApi();
let query = "query_example"; // String | Precedes the search term string. Used in a Search Query. Except for &lt;specific_concept_name&gt;, Search Query will take the required parameters listed above (&lt;concept_type&gt;, &lt;concept_uri&gt;, &lt;article_uri&gt;) as an optional_parameter in addition to the query=&lt;query_term&gt;.
let opts = {
  'offset': 10, // Number | Integer value for the index count from the first concept to the last concept, sorted alphabetically. Used in a Search Query. A Search Query will return up to 10 concepts in its results.
  'fields': "fields_example" // String | \"all\" or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept. 
};
apiInstance.searchJsonGet(query, opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **String**| Precedes the search term string. Used in a Search Query. Except for &amp;lt;specific_concept_name&amp;gt;, Search Query will take the required parameters listed above (&amp;lt;concept_type&amp;gt;, &amp;lt;concept_uri&amp;gt;, &amp;lt;article_uri&amp;gt;) as an optional_parameter in addition to the query&#x3D;&amp;lt;query_term&amp;gt;. | 
 **offset** | **Number**| Integer value for the index count from the first concept to the last concept, sorted alphabetically. Used in a Search Query. A Search Query will return up to 10 concepts in its results. | [optional] [default to 10]
 **fields** | **String**| \&quot;all\&quot; or comma-separated list of specific optional fields: pages, ticker_symbol, links, taxonomy, combinations, geocodes, article_list, scope_notes, search_api_query  Optional fields are returned in result_set. They are briefly explained here:  pages: A list of topic pages associated with a specific concept. ticker_symbol: If this concept is a publicly traded company, this field contains the ticker symbol. links: A list of links from this concept to external data resources. taxonomy: For descriptor concepts, this field returns a list of taxonomic relations to other concepts. combinations: For descriptor concepts, this field returns a list of the specific meanings tis concept takes on when combined with other concepts. geocodes: For geographic concepts, the full GIS record from geonames. article_list: A list of up to 10 articles associated with this concept. scope_notes: Scope notes contains clarifications and meaning definitions that explicate the relationship between the concept and an article. search_api_query: Returns the request one would need to submit to the Article Search API to obtain a list of articles annotated with this concept.  | [optional] 

### Return type

[**SearchJsonGet200Response**](SearchJsonGet200Response.md)

### Authorization

[apikey](../README.md#apikey)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

