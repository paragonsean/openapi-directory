# SearchApi

All URIs are relative to *http://www.freesound.org/apiv2*

| Method | HTTP request | Description |
|------------- | ------------- | -------------|
| [**searchText**](SearchApi.md#searchText) | **GET** /search/text | Search sounds |


<a id="searchText"></a>
# **searchText**
> List&lt;Sound&gt; searchText(query, filter, sort, groupByPack, page, pageSize)

Search sounds

This resource allows searching sounds in Freesound by matching their tags and other kinds of metadata.

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
    defaultClient.setBasePath("http://www.freesound.org/apiv2");

    SearchApi apiInstance = new SearchApi(defaultClient);
    String query = "query_example"; // String | The query! The query is the main parameter used to define a query. You can type several terms separated by spaces or phrases wrapped inside quote ‘”’ characters. For every term, you can also use ‘+’ and ‘-‘ modifier characters to indicate that a term is “mandatory” or “prohibited” (by default, terms are considered to be “mandatory”). For example, in a query such as query=term_a -term_b, sounds including term_b will not match the search criteria. The query does a weighted search over some sound properties including sound tags, the sound name, its description, pack name and the sound id. Therefore, searching for query=123 will find you sounds with id 1234, sounds that have 1234 in the description, in the tags, etc. You’ll find some examples below. Using an empty query (query= or query=\"\") will return all Freeosund sounds.
    String filter = "filter_example"; // String | Allows filtering query results. See below for more information.
    String sort = "score"; // String | Indicates how query results should be sorted. See below for a list of the sorting options. By default `sort=score`. <p> <table>   <tr>     <th>Option</th>     <th>Explanation</th>   </tr>   <tr>     <td>score</td>     <td>Sort by a relevance score returned by our search engine (default).</td>   </tr>   <tr>     <td>duration_desc     <td>Sort by the duration of the sounds, longest sounds first.   </tr>   <tr>     <td>duration_asc     <td>Same as above, but shortest sounds first.   </tr>   <tr>     <td>created_desc     <td>Sort by the date of when the sound was added. newest sounds first.   </tr>   <tr>     <td>created_asc     <td>Same as above, but oldest sounds first.   </tr>   <tr>     <td>downloads_desc     <td>Sort by the number of downloads, most downloaded sounds first.   </tr>   <tr>     <td>downloads_asc     <td>Same as above, but least downloaded sounds first.   </tr>   <tr>     <td>rating_desc     <td>Sort by the average rating given to the sounds, highest rated first.   </tr>   <tr>     <td>rating_asc     <td>Same as above, but lowest rated sounds first.   </tr> </table> </p>
    Integer groupByPack = 56; // Integer | This parameter represents a boolean option to indicate whether to collapse results belonging to sounds of the same pack into single entries in the results list. If `group_by_pack=1` and search results contain more than one sound that belongs to the same pack, only one sound for each distinct pack is returned (sounds with no packs are returned as well). However, the returned sound will feature two extra properties to access these other sounds omitted from the results list: `n_from_same_pack`: indicates how many other results belong to the same pack (and have not been returned) `more_from_same_pack`: uri pointing to the list of omitted sound results of the same pack (also including the result which has already been returned). See examples below. By default `group_by_pack=0`.
    Integer page = 1; // Integer | Query results are paginated, this parameter indicates what page should be returned. By default `page=1`.
    Integer pageSize = 15; // Integer | Indicates the number of sounds per page to include in the result. By default `page_size=15`, and the maximum is `page_size=150`. Not that with bigger `page_size`, more data will need to be transferred.
    try {
      List<Sound> result = apiInstance.searchText(query, filter, sort, groupByPack, page, pageSize);
      System.out.println(result);
    } catch (ApiException e) {
      System.err.println("Exception when calling SearchApi#searchText");
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
| **query** | **String**| The query! The query is the main parameter used to define a query. You can type several terms separated by spaces or phrases wrapped inside quote ‘”’ characters. For every term, you can also use ‘+’ and ‘-‘ modifier characters to indicate that a term is “mandatory” or “prohibited” (by default, terms are considered to be “mandatory”). For example, in a query such as query&#x3D;term_a -term_b, sounds including term_b will not match the search criteria. The query does a weighted search over some sound properties including sound tags, the sound name, its description, pack name and the sound id. Therefore, searching for query&#x3D;123 will find you sounds with id 1234, sounds that have 1234 in the description, in the tags, etc. You’ll find some examples below. Using an empty query (query&#x3D; or query&#x3D;\&quot;\&quot;) will return all Freeosund sounds. | [optional] |
| **filter** | **String**| Allows filtering query results. See below for more information. | [optional] |
| **sort** | **String**| Indicates how query results should be sorted. See below for a list of the sorting options. By default &#x60;sort&#x3D;score&#x60;. &lt;p&gt; &lt;table&gt;   &lt;tr&gt;     &lt;th&gt;Option&lt;/th&gt;     &lt;th&gt;Explanation&lt;/th&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;score&lt;/td&gt;     &lt;td&gt;Sort by a relevance score returned by our search engine (default).&lt;/td&gt;   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;duration_desc     &lt;td&gt;Sort by the duration of the sounds, longest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;duration_asc     &lt;td&gt;Same as above, but shortest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;created_desc     &lt;td&gt;Sort by the date of when the sound was added. newest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;created_asc     &lt;td&gt;Same as above, but oldest sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;downloads_desc     &lt;td&gt;Sort by the number of downloads, most downloaded sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;downloads_asc     &lt;td&gt;Same as above, but least downloaded sounds first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;rating_desc     &lt;td&gt;Sort by the average rating given to the sounds, highest rated first.   &lt;/tr&gt;   &lt;tr&gt;     &lt;td&gt;rating_asc     &lt;td&gt;Same as above, but lowest rated sounds first.   &lt;/tr&gt; &lt;/table&gt; &lt;/p&gt; | [optional] [enum: score, duration_desc, duration_asc, created_desc, created_asc, downloads_desc, downloads_asc, rating_desc, rating_asc] |
| **groupByPack** | **Integer**| This parameter represents a boolean option to indicate whether to collapse results belonging to sounds of the same pack into single entries in the results list. If &#x60;group_by_pack&#x3D;1&#x60; and search results contain more than one sound that belongs to the same pack, only one sound for each distinct pack is returned (sounds with no packs are returned as well). However, the returned sound will feature two extra properties to access these other sounds omitted from the results list: &#x60;n_from_same_pack&#x60;: indicates how many other results belong to the same pack (and have not been returned) &#x60;more_from_same_pack&#x60;: uri pointing to the list of omitted sound results of the same pack (also including the result which has already been returned). See examples below. By default &#x60;group_by_pack&#x3D;0&#x60;. | [optional] |
| **page** | **Integer**| Query results are paginated, this parameter indicates what page should be returned. By default &#x60;page&#x3D;1&#x60;. | [optional] [default to 1] |
| **pageSize** | **Integer**| Indicates the number of sounds per page to include in the result. By default &#x60;page_size&#x3D;15&#x60;, and the maximum is &#x60;page_size&#x3D;150&#x60;. Not that with bigger &#x60;page_size&#x60;, more data will need to be transferred. | [optional] [default to 15] |

### Return type

[**List&lt;Sound&gt;**](Sound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | successful operation |  -  |
| **400** | Invalid status value |  -  |

