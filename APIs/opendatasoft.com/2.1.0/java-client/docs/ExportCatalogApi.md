# ExportCatalogApi

All URIs are relative to *https://public.opendatasoft.com/api/v2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**exportDatasetsCSV**](ExportCatalogApi.md#exportDatasetsCSV) | **GET** /{source}/exports/csv |  |
| [**exportDatasetsJson**](ExportCatalogApi.md#exportDatasetsJson) | **GET** /{source}/exports/json |  |
| [**exportDatasetsRDF**](ExportCatalogApi.md#exportDatasetsRDF) | **GET** /{source}/exports/rdf |  |
| [**exportDatasetsRSS**](ExportCatalogApi.md#exportDatasetsRSS) | **GET** /{source}/exports/rss |  |
| [**exportDatasetsTTL**](ExportCatalogApi.md#exportDatasetsTTL) | **GET** /{source}/exports/ttl |  |
| [**exportDatasetsXLS**](ExportCatalogApi.md#exportDatasetsXLS) | **GET** /{source}/exports/xls |  |


<a id="exportDatasetsCSV"></a>
# **exportDatasetsCSV**
> File exportDatasetsCSV(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas, delimiter)



Export catalog (source) in CSV format 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ExportCatalogApi apiInstance = new ExportCatalogApi(defaultClient);
    String source = "catalog"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    List<String> where = Arrays.asList(); // List<String> | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    Integer limit = 10; // Integer | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    Integer offset = 0; // Integer | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    List<String> search = Arrays.asList(); // List<String> | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    List<String> facet = Arrays.asList(); // List<String> | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    List<String> refine = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    List<String> exclude = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    String timezone = "UTC"; // String | Set timezone for datetime fields
    Boolean includeAppMetas = false; // Boolean | Explicitely request application metas for each datasets. 
    String delimiter = ","; // String | Provide a different delimiter (default ',').
    try {
      File result = apiInstance.exportDatasetsCSV(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas, delimiter);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportCatalogApi#exportDatasetsCSV");
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
| **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to catalog] [enum: catalog, opendatasoft, monitoring] |
| **where** | [**List&lt;String&gt;**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] |
| **limit** | **Integer**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10] |
| **offset** | **Integer**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0] |
| **search** | [**List&lt;String&gt;**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] |
| **facet** | [**List&lt;String&gt;**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] |
| **refine** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] |
| **timezone** | **String**| Set timezone for datetime fields | [optional] [default to UTC] |
| **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false] |
| **delimiter** | **String**| Provide a different delimiter (default &#39;,&#39;). | [optional] [default to ;] [enum: ,, ;, |] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/csv

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a CSV file |  -  |

<a id="exportDatasetsJson"></a>
# **exportDatasetsJson**
> File exportDatasetsJson(source, where, limit, offset, search, facet, refine, exclude, pretty, timezone, includeAppMetas)



Export catalog (source) in JSON format 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ExportCatalogApi apiInstance = new ExportCatalogApi(defaultClient);
    String source = "catalog"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    List<String> where = Arrays.asList(); // List<String> | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    Integer limit = 10; // Integer | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    Integer offset = 0; // Integer | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    List<String> search = Arrays.asList(); // List<String> | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    List<String> facet = Arrays.asList(); // List<String> | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    List<String> refine = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    List<String> exclude = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    Boolean pretty = false; // Boolean | Activate pretty print
    String timezone = "UTC"; // String | Set timezone for datetime fields
    Boolean includeAppMetas = false; // Boolean | Explicitely request application metas for each datasets. 
    try {
      File result = apiInstance.exportDatasetsJson(source, where, limit, offset, search, facet, refine, exclude, pretty, timezone, includeAppMetas);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportCatalogApi#exportDatasetsJson");
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
| **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to catalog] [enum: catalog, opendatasoft, monitoring] |
| **where** | [**List&lt;String&gt;**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] |
| **limit** | **Integer**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10] |
| **offset** | **Integer**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0] |
| **search** | [**List&lt;String&gt;**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] |
| **facet** | [**List&lt;String&gt;**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] |
| **refine** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] |
| **pretty** | **Boolean**| Activate pretty print | [optional] [default to false] |
| **timezone** | **String**| Set timezone for datetime fields | [optional] [default to UTC] |
| **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a JSON file |  -  |

<a id="exportDatasetsRDF"></a>
# **exportDatasetsRDF**
> File exportDatasetsRDF(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas)



Export catalog (source) in RDF/XML format 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ExportCatalogApi apiInstance = new ExportCatalogApi(defaultClient);
    String source = "catalog"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    List<String> where = Arrays.asList(); // List<String> | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    Integer limit = 10; // Integer | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    Integer offset = 0; // Integer | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    List<String> search = Arrays.asList(); // List<String> | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    List<String> facet = Arrays.asList(); // List<String> | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    List<String> refine = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    List<String> exclude = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    String timezone = "UTC"; // String | Set timezone for datetime fields
    Boolean includeAppMetas = false; // Boolean | Explicitely request application metas for each datasets. 
    try {
      File result = apiInstance.exportDatasetsRDF(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportCatalogApi#exportDatasetsRDF");
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
| **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to catalog] [enum: catalog, opendatasoft, monitoring] |
| **where** | [**List&lt;String&gt;**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] |
| **limit** | **Integer**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10] |
| **offset** | **Integer**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0] |
| **search** | [**List&lt;String&gt;**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] |
| **facet** | [**List&lt;String&gt;**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] |
| **refine** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] |
| **timezone** | **String**| Set timezone for datetime fields | [optional] [default to UTC] |
| **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/rdf+xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a RDF XML file |  -  |

<a id="exportDatasetsRSS"></a>
# **exportDatasetsRSS**
> File exportDatasetsRSS(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas)



Export catalog (source) in RSS format 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ExportCatalogApi apiInstance = new ExportCatalogApi(defaultClient);
    String source = "catalog"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    List<String> where = Arrays.asList(); // List<String> | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    Integer limit = 10; // Integer | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    Integer offset = 0; // Integer | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    List<String> search = Arrays.asList(); // List<String> | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    List<String> facet = Arrays.asList(); // List<String> | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    List<String> refine = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    List<String> exclude = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    String timezone = "UTC"; // String | Set timezone for datetime fields
    Boolean includeAppMetas = false; // Boolean | Explicitely request application metas for each datasets. 
    try {
      File result = apiInstance.exportDatasetsRSS(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportCatalogApi#exportDatasetsRSS");
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
| **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to catalog] [enum: catalog, opendatasoft, monitoring] |
| **where** | [**List&lt;String&gt;**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] |
| **limit** | **Integer**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10] |
| **offset** | **Integer**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0] |
| **search** | [**List&lt;String&gt;**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] |
| **facet** | [**List&lt;String&gt;**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] |
| **refine** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] |
| **timezone** | **String**| Set timezone for datetime fields | [optional] [default to UTC] |
| **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a JSON file |  -  |

<a id="exportDatasetsTTL"></a>
# **exportDatasetsTTL**
> File exportDatasetsTTL(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas)



Export catalog (source) in TTL (turtle/rdf) format 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ExportCatalogApi apiInstance = new ExportCatalogApi(defaultClient);
    String source = "catalog"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    List<String> where = Arrays.asList(); // List<String> | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    Integer limit = 10; // Integer | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    Integer offset = 0; // Integer | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    List<String> search = Arrays.asList(); // List<String> | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    List<String> facet = Arrays.asList(); // List<String> | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    List<String> refine = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    List<String> exclude = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    String timezone = "UTC"; // String | Set timezone for datetime fields
    Boolean includeAppMetas = false; // Boolean | Explicitely request application metas for each datasets. 
    try {
      File result = apiInstance.exportDatasetsTTL(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportCatalogApi#exportDatasetsTTL");
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
| **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to catalog] [enum: catalog, opendatasoft, monitoring] |
| **where** | [**List&lt;String&gt;**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] |
| **limit** | **Integer**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10] |
| **offset** | **Integer**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0] |
| **search** | [**List&lt;String&gt;**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] |
| **facet** | [**List&lt;String&gt;**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] |
| **refine** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] |
| **timezone** | **String**| Set timezone for datetime fields | [optional] [default to UTC] |
| **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/turtle

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return a TTL file |  -  |

<a id="exportDatasetsXLS"></a>
# **exportDatasetsXLS**
> File exportDatasetsXLS(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas)



Export catalog (source) in XLS (Excel) format 

### Example
```java
// Import classes:
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.Configuration;
import org.openapitools.client.auth.*;
import org.openapitools.client.models.*;
import org.openapitools.client.api.ExportCatalogApi;

public class Example {
  public static void main(String[] args) {
    ApiClient defaultClient = Configuration.getDefaultApiClient();
    defaultClient.setBasePath("https://public.opendatasoft.com/api/v2");
    
    // Configure API key authorization: api_key
    ApiKeyAuth api_key = (ApiKeyAuth) defaultClient.getAuthentication("api_key");
    api_key.setApiKey("YOUR API KEY");
    // Uncomment the following line to set a prefix for the API key, e.g. "Token" (defaults to null)
    //api_key.setApiKeyPrefix("Token");

    // Configure HTTP basic authorization: basic
    HttpBasicAuth basic = (HttpBasicAuth) defaultClient.getAuthentication("basic");
    basic.setUsername("YOUR USERNAME");
    basic.setPassword("YOUR PASSWORD");

    ExportCatalogApi apiInstance = new ExportCatalogApi(defaultClient);
    String source = "catalog"; // String | Each source represents a different catalog of datasets you'll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft's repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/) 
    List<String> where = Arrays.asList(); // List<String> | An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details. 
    Integer limit = 10; // Integer | Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10. 
    Integer offset = 0; // Integer | Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination. 
    List<String> search = Arrays.asList(); // List<String> | An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset. 
    List<String> facet = Arrays.asList(); // List<String> | A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint `/facets`).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details. 
    List<String> refine = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources* 
    List<String> exclude = Arrays.asList(); // List<String> | An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources* 
    String timezone = "UTC"; // String | Set timezone for datetime fields
    Boolean includeAppMetas = false; // Boolean | Explicitely request application metas for each datasets. 
    try {
      File result = apiInstance.exportDatasetsXLS(source, where, limit, offset, search, facet, refine, exclude, timezone, includeAppMetas);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling ExportCatalogApi#exportDatasetsXLS");
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
| **source** | **String**| Each source represents a different catalog of datasets you&#39;ll be able to query.  There are 2 sources available:  * catalog: the catalog of datasets on your portal * opendatasoft: Opendatasoft&#39;s repository of public datasets, also available at   [data.opendatasoft.com](https://data.opendatasoft.com/page/home/)  | [default to catalog] [enum: catalog, opendatasoft, monitoring] |
| **where** | [**List&lt;String&gt;**](String.md)| An array of filters.  A filter is a text expression performing a simple full-text search that can also include logical operations (NOT, AND, OR...) as well as lots of other functions, thus performing more complex and more precise searches.  Read [the query language reference](https://docs.opendatasoft.com/api/explore/v2.html#where-clause) for more details.  | [optional] |
| **limit** | **Integer**| Number of items to return.  To use in conjonction with offset to implement pagination.  Limit maximum value is 100. To retrive more data use export entry points. The default value is 10.  | [optional] [default to 10] |
| **offset** | **Integer**| Index of the first item to return (starting at 0).  To use in conjonction with limit to implement pagination.  | [optional] [default to 0] |
| **search** | [**List&lt;String&gt;**](String.md)| An array of full text search.  A full text search performs a prefixed text search for each provided terms in all visible fields of a catalog/dataset.  | [optional] |
| **facet** | [**List&lt;String&gt;**](String.md)| A facet is a field used for simple filtering (through the parameters refine and exclude) or exploration (with the endpoint &#x60;/facets&#x60;).  Facets can be configured in the back-office or with this parameter.  Read [the facets documentation](https://help.opendatasoft.com/apis/ods-search-v2/#facets) for more details.  | [optional] |
| **refine** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will only include the selected facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Refining with a facet is equivalent to selecting an entry in the left navigation panel.*  *refine is not available for monitoring sources*  | [optional] |
| **exclude** | [**List&lt;String&gt;**](String.md)| An array of facet filters. For example **city:Paris** or **modified:2019/12**. The request will exclude the defined facet value.  Read [filtering with facets value](https://help.opendatasoft.com/apis/ods-search-v2/#filtering-with-facets-values) for more details.  *Not to be confused with a where filter. Excluding a facet value is equivalent to removing an entry in the left navigation panel.*  *exclude is not available for monitoring sources*  | [optional] |
| **timezone** | **String**| Set timezone for datetime fields | [optional] [default to UTC] |
| **includeAppMetas** | **Boolean**| Explicitely request application metas for each datasets.  | [optional] [default to false] |

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [basic](../README.md#basic)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: xls

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Return an XLS file |  -  |

