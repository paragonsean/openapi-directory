/*
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiCallback;
import org.openapitools.client.ApiClient;
import org.openapitools.client.ApiException;
import org.openapitools.client.ApiResponse;
import org.openapitools.client.Configuration;
import org.openapitools.client.Pair;
import org.openapitools.client.ProgressRequestBody;
import org.openapitools.client.ProgressResponseBody;

import com.google.gson.reflect.TypeToken;

import java.io.IOException;


import org.openapitools.client.model.Serprequest;

import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SerpApi {
    private ApiClient localVarApiClient;
    private int localHostIndex;
    private String localCustomBaseUrl;

    public SerpApi() {
        this(Configuration.getDefaultApiClient());
    }

    public SerpApi(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public ApiClient getApiClient() {
        return localVarApiClient;
    }

    public void setApiClient(ApiClient apiClient) {
        this.localVarApiClient = apiClient;
    }

    public int getHostIndex() {
        return localHostIndex;
    }

    public void setHostIndex(int hostIndex) {
        this.localHostIndex = hostIndex;
    }

    public String getCustomBaseUrl() {
        return localCustomBaseUrl;
    }

    public void setCustomBaseUrl(String customBaseUrl) {
        this.localCustomBaseUrl = customBaseUrl;
    }

    /**
     * Build call for serp
     * @param serprequest &lt;h2&gt;Search parameters&lt;/h2&gt;  &gt; In most cases, you don&#39;t need to customize parameters by hand. Use &lt;a href&#x3D;\&quot;https://dataflowkit.com/serp\&quot; target&#x3D;\&quot;_blank\&quot;&gt;SERP extraction Code generator&lt;/a&gt;. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  &lt;h3&gt;URL GET parameters&lt;/h3&gt;  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, &lt;ul&gt; &lt;li&gt;&lt;code&gt;link:dataflowkit.com&lt;/code&gt;,&lt;/li&gt; &lt;li&gt;&lt;code&gt;site:twitter.com Bratislava&lt;/code&gt;,&lt;/li&gt;&lt;li&gt;&lt;code&gt;inurl:view/view.shtml&lt;/code&gt;, etc.)&lt;/li&gt;&lt;/ul&gt; See The Complete List of 42 Advanced &lt;a href&#x3D;\&quot;https://ahrefs.com/blog/google-advanced-search-operators/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Search Operators&lt;/a&gt;|&lt;ul&gt; &lt;li&gt;&lt;code&gt;q&lt;/code&gt; parameter is used by google, Bing, DuckDuckGo.&lt;/li&gt;&lt;li&gt; &lt;code&gt;text&lt;/code&gt; is used as query holder by Yandex SE.&lt;/li&gt;&lt;li&gt; Chineese Baidu uses &lt;code&gt;wd&lt;/code&gt; for this purpose.&lt;/li&gt;&lt;/ul&gt;| |tbm| &lt;code&gt;tbm&lt;/code&gt; is a special Google parameter used to differentiate between search types|  &lt;ul&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;isch&lt;/code&gt; - Google Images,&lt;/li&gt; &lt;li&gt; &lt;code&gt;tbm&#x3D;nws&lt;/code&gt; - Google News&lt;/li&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;shop&lt;/code&gt; - Google Shopping&lt;/li&gt; &lt;/ul&gt;| |lr|Restricts the search to documents written in a particular languages.|&lt;ul&gt;&lt;li&gt;Google uses &lt;code&gt;lang_{two-letter lang code}&lt;/code&gt; to specify languages and &lt;code&gt;&amp;#124;&lt;/code&gt; as a delimiter. (e.g., &lt;code&gt;lang_sk&amp;#124;lang_de&lt;/code&gt; will only search Slovak and German pages). See the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/v1/cse/list\&quot;&gt;full list&lt;/a&gt; of possible values for Google. &lt;/li&gt;&lt;li&gt;For Bing specify &lt;code&gt;setLang&#x3D;en&lt;/code&gt; parameter.&lt;/li&gt;&lt;li&gt; In Yandex use &lt;code&gt;lang&#x3D;ca&lt;/code&gt; parameter&lt;/li&gt;&lt;/ul&gt;| |gl|Specify the country to search from. It&#39;s a two-letter country code. (e.g., &lt;code&gt;sk&lt;/code&gt; for Slovakia, or &lt;code&gt;us&lt;/code&gt; for the United States).| For Google see the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\&quot;&gt;Country Codes&lt;/a&gt; page for a list of valid values. For Bing &lt;code&gt;cc&#x3D;at&lt;/code&gt; parameter is used.|  (required)
     * @param _callback Callback for upload/download progress
     * @return Call to execute
     * @throws ApiException If fail to serialize the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns data in the one of the follwing formats - JSON, JSON Lines, CSV, MS Excel, XML </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. Invalid payload specified. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call serpCall(Serprequest serprequest, final ApiCallback _callback) throws ApiException {
        String basePath = null;
        // Operation Servers
        String[] localBasePaths = new String[] {  };

        // Determine Base Path to Use
        if (localCustomBaseUrl != null){
            basePath = localCustomBaseUrl;
        } else if ( localBasePaths.length > 0 ) {
            basePath = localBasePaths[localHostIndex];
        } else {
            basePath = null;
        }

        Object localVarPostBody = serprequest;

        // create path and map variables
        String localVarPath = "/serp";

        List<Pair> localVarQueryParams = new ArrayList<Pair>();
        List<Pair> localVarCollectionQueryParams = new ArrayList<Pair>();
        Map<String, String> localVarHeaderParams = new HashMap<String, String>();
        Map<String, String> localVarCookieParams = new HashMap<String, String>();
        Map<String, Object> localVarFormParams = new HashMap<String, Object>();

        final String[] localVarAccepts = {
            "application/json",
            "application/x-ndjson",
            "text/csv",
            "text/plain; charset=utf-8"
        };
        final String localVarAccept = localVarApiClient.selectHeaderAccept(localVarAccepts);
        if (localVarAccept != null) {
            localVarHeaderParams.put("Accept", localVarAccept);
        }

        final String[] localVarContentTypes = {
            "application/json"
        };
        final String localVarContentType = localVarApiClient.selectHeaderContentType(localVarContentTypes);
        if (localVarContentType != null) {
            localVarHeaderParams.put("Content-Type", localVarContentType);
        }

        String[] localVarAuthNames = new String[] { "ApiKeyAuth" };
        return localVarApiClient.buildCall(basePath, localVarPath, "POST", localVarQueryParams, localVarCollectionQueryParams, localVarPostBody, localVarHeaderParams, localVarCookieParams, localVarFormParams, localVarAuthNames, _callback);
    }

    @SuppressWarnings("rawtypes")
    private okhttp3.Call serpValidateBeforeCall(Serprequest serprequest, final ApiCallback _callback) throws ApiException {
        // verify the required parameter 'serprequest' is set
        if (serprequest == null) {
            throw new ApiException("Missing the required parameter 'serprequest' when calling serp(Async)");
        }

        return serpCall(serprequest, _callback);

    }

    /**
     * Collect search results from search engines
     * To crawl search engine result pages, you can use &#x60;/serp&#x60; endpoint. SERP collection service extracts a list of organic results, news, images, and more.  Specify configuration parameters, such as country or languages, to customize output SERP data. The following search engines are supported  - google - google-image - google-news - google-shopping - bing - duckduckgo - baidu - yandex   Generate ready-to-run code for your favorite language at [https://dataflowkit.com/serp](https://dataflowkit.com/serp)
     * @param serprequest &lt;h2&gt;Search parameters&lt;/h2&gt;  &gt; In most cases, you don&#39;t need to customize parameters by hand. Use &lt;a href&#x3D;\&quot;https://dataflowkit.com/serp\&quot; target&#x3D;\&quot;_blank\&quot;&gt;SERP extraction Code generator&lt;/a&gt;. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  &lt;h3&gt;URL GET parameters&lt;/h3&gt;  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, &lt;ul&gt; &lt;li&gt;&lt;code&gt;link:dataflowkit.com&lt;/code&gt;,&lt;/li&gt; &lt;li&gt;&lt;code&gt;site:twitter.com Bratislava&lt;/code&gt;,&lt;/li&gt;&lt;li&gt;&lt;code&gt;inurl:view/view.shtml&lt;/code&gt;, etc.)&lt;/li&gt;&lt;/ul&gt; See The Complete List of 42 Advanced &lt;a href&#x3D;\&quot;https://ahrefs.com/blog/google-advanced-search-operators/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Search Operators&lt;/a&gt;|&lt;ul&gt; &lt;li&gt;&lt;code&gt;q&lt;/code&gt; parameter is used by google, Bing, DuckDuckGo.&lt;/li&gt;&lt;li&gt; &lt;code&gt;text&lt;/code&gt; is used as query holder by Yandex SE.&lt;/li&gt;&lt;li&gt; Chineese Baidu uses &lt;code&gt;wd&lt;/code&gt; for this purpose.&lt;/li&gt;&lt;/ul&gt;| |tbm| &lt;code&gt;tbm&lt;/code&gt; is a special Google parameter used to differentiate between search types|  &lt;ul&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;isch&lt;/code&gt; - Google Images,&lt;/li&gt; &lt;li&gt; &lt;code&gt;tbm&#x3D;nws&lt;/code&gt; - Google News&lt;/li&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;shop&lt;/code&gt; - Google Shopping&lt;/li&gt; &lt;/ul&gt;| |lr|Restricts the search to documents written in a particular languages.|&lt;ul&gt;&lt;li&gt;Google uses &lt;code&gt;lang_{two-letter lang code}&lt;/code&gt; to specify languages and &lt;code&gt;&amp;#124;&lt;/code&gt; as a delimiter. (e.g., &lt;code&gt;lang_sk&amp;#124;lang_de&lt;/code&gt; will only search Slovak and German pages). See the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/v1/cse/list\&quot;&gt;full list&lt;/a&gt; of possible values for Google. &lt;/li&gt;&lt;li&gt;For Bing specify &lt;code&gt;setLang&#x3D;en&lt;/code&gt; parameter.&lt;/li&gt;&lt;li&gt; In Yandex use &lt;code&gt;lang&#x3D;ca&lt;/code&gt; parameter&lt;/li&gt;&lt;/ul&gt;| |gl|Specify the country to search from. It&#39;s a two-letter country code. (e.g., &lt;code&gt;sk&lt;/code&gt; for Slovakia, or &lt;code&gt;us&lt;/code&gt; for the United States).| For Google see the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\&quot;&gt;Country Codes&lt;/a&gt; page for a list of valid values. For Bing &lt;code&gt;cc&#x3D;at&lt;/code&gt; parameter is used.|  (required)
     * @return Object
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns data in the one of the follwing formats - JSON, JSON Lines, CSV, MS Excel, XML </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. Invalid payload specified. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. </td><td>  -  </td></tr>
     </table>
     */
    public Object serp(Serprequest serprequest) throws ApiException {
        ApiResponse<Object> localVarResp = serpWithHttpInfo(serprequest);
        return localVarResp.getData();
    }

    /**
     * Collect search results from search engines
     * To crawl search engine result pages, you can use &#x60;/serp&#x60; endpoint. SERP collection service extracts a list of organic results, news, images, and more.  Specify configuration parameters, such as country or languages, to customize output SERP data. The following search engines are supported  - google - google-image - google-news - google-shopping - bing - duckduckgo - baidu - yandex   Generate ready-to-run code for your favorite language at [https://dataflowkit.com/serp](https://dataflowkit.com/serp)
     * @param serprequest &lt;h2&gt;Search parameters&lt;/h2&gt;  &gt; In most cases, you don&#39;t need to customize parameters by hand. Use &lt;a href&#x3D;\&quot;https://dataflowkit.com/serp\&quot; target&#x3D;\&quot;_blank\&quot;&gt;SERP extraction Code generator&lt;/a&gt;. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  &lt;h3&gt;URL GET parameters&lt;/h3&gt;  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, &lt;ul&gt; &lt;li&gt;&lt;code&gt;link:dataflowkit.com&lt;/code&gt;,&lt;/li&gt; &lt;li&gt;&lt;code&gt;site:twitter.com Bratislava&lt;/code&gt;,&lt;/li&gt;&lt;li&gt;&lt;code&gt;inurl:view/view.shtml&lt;/code&gt;, etc.)&lt;/li&gt;&lt;/ul&gt; See The Complete List of 42 Advanced &lt;a href&#x3D;\&quot;https://ahrefs.com/blog/google-advanced-search-operators/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Search Operators&lt;/a&gt;|&lt;ul&gt; &lt;li&gt;&lt;code&gt;q&lt;/code&gt; parameter is used by google, Bing, DuckDuckGo.&lt;/li&gt;&lt;li&gt; &lt;code&gt;text&lt;/code&gt; is used as query holder by Yandex SE.&lt;/li&gt;&lt;li&gt; Chineese Baidu uses &lt;code&gt;wd&lt;/code&gt; for this purpose.&lt;/li&gt;&lt;/ul&gt;| |tbm| &lt;code&gt;tbm&lt;/code&gt; is a special Google parameter used to differentiate between search types|  &lt;ul&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;isch&lt;/code&gt; - Google Images,&lt;/li&gt; &lt;li&gt; &lt;code&gt;tbm&#x3D;nws&lt;/code&gt; - Google News&lt;/li&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;shop&lt;/code&gt; - Google Shopping&lt;/li&gt; &lt;/ul&gt;| |lr|Restricts the search to documents written in a particular languages.|&lt;ul&gt;&lt;li&gt;Google uses &lt;code&gt;lang_{two-letter lang code}&lt;/code&gt; to specify languages and &lt;code&gt;&amp;#124;&lt;/code&gt; as a delimiter. (e.g., &lt;code&gt;lang_sk&amp;#124;lang_de&lt;/code&gt; will only search Slovak and German pages). See the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/v1/cse/list\&quot;&gt;full list&lt;/a&gt; of possible values for Google. &lt;/li&gt;&lt;li&gt;For Bing specify &lt;code&gt;setLang&#x3D;en&lt;/code&gt; parameter.&lt;/li&gt;&lt;li&gt; In Yandex use &lt;code&gt;lang&#x3D;ca&lt;/code&gt; parameter&lt;/li&gt;&lt;/ul&gt;| |gl|Specify the country to search from. It&#39;s a two-letter country code. (e.g., &lt;code&gt;sk&lt;/code&gt; for Slovakia, or &lt;code&gt;us&lt;/code&gt; for the United States).| For Google see the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\&quot;&gt;Country Codes&lt;/a&gt; page for a list of valid values. For Bing &lt;code&gt;cc&#x3D;at&lt;/code&gt; parameter is used.|  (required)
     * @return ApiResponse&lt;Object&gt;
     * @throws ApiException If fail to call the API, e.g. server error or cannot deserialize the response body
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns data in the one of the follwing formats - JSON, JSON Lines, CSV, MS Excel, XML </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. Invalid payload specified. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. </td><td>  -  </td></tr>
     </table>
     */
    public ApiResponse<Object> serpWithHttpInfo(Serprequest serprequest) throws ApiException {
        okhttp3.Call localVarCall = serpValidateBeforeCall(serprequest, null);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        return localVarApiClient.execute(localVarCall, localVarReturnType);
    }

    /**
     * Collect search results from search engines (asynchronously)
     * To crawl search engine result pages, you can use &#x60;/serp&#x60; endpoint. SERP collection service extracts a list of organic results, news, images, and more.  Specify configuration parameters, such as country or languages, to customize output SERP data. The following search engines are supported  - google - google-image - google-news - google-shopping - bing - duckduckgo - baidu - yandex   Generate ready-to-run code for your favorite language at [https://dataflowkit.com/serp](https://dataflowkit.com/serp)
     * @param serprequest &lt;h2&gt;Search parameters&lt;/h2&gt;  &gt; In most cases, you don&#39;t need to customize parameters by hand. Use &lt;a href&#x3D;\&quot;https://dataflowkit.com/serp\&quot; target&#x3D;\&quot;_blank\&quot;&gt;SERP extraction Code generator&lt;/a&gt;. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  &lt;h3&gt;URL GET parameters&lt;/h3&gt;  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, &lt;ul&gt; &lt;li&gt;&lt;code&gt;link:dataflowkit.com&lt;/code&gt;,&lt;/li&gt; &lt;li&gt;&lt;code&gt;site:twitter.com Bratislava&lt;/code&gt;,&lt;/li&gt;&lt;li&gt;&lt;code&gt;inurl:view/view.shtml&lt;/code&gt;, etc.)&lt;/li&gt;&lt;/ul&gt; See The Complete List of 42 Advanced &lt;a href&#x3D;\&quot;https://ahrefs.com/blog/google-advanced-search-operators/\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Google Search Operators&lt;/a&gt;|&lt;ul&gt; &lt;li&gt;&lt;code&gt;q&lt;/code&gt; parameter is used by google, Bing, DuckDuckGo.&lt;/li&gt;&lt;li&gt; &lt;code&gt;text&lt;/code&gt; is used as query holder by Yandex SE.&lt;/li&gt;&lt;li&gt; Chineese Baidu uses &lt;code&gt;wd&lt;/code&gt; for this purpose.&lt;/li&gt;&lt;/ul&gt;| |tbm| &lt;code&gt;tbm&lt;/code&gt; is a special Google parameter used to differentiate between search types|  &lt;ul&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;isch&lt;/code&gt; - Google Images,&lt;/li&gt; &lt;li&gt; &lt;code&gt;tbm&#x3D;nws&lt;/code&gt; - Google News&lt;/li&gt; &lt;li&gt;&lt;code&gt;tbm&#x3D;shop&lt;/code&gt; - Google Shopping&lt;/li&gt; &lt;/ul&gt;| |lr|Restricts the search to documents written in a particular languages.|&lt;ul&gt;&lt;li&gt;Google uses &lt;code&gt;lang_{two-letter lang code}&lt;/code&gt; to specify languages and &lt;code&gt;&amp;#124;&lt;/code&gt; as a delimiter. (e.g., &lt;code&gt;lang_sk&amp;#124;lang_de&lt;/code&gt; will only search Slovak and German pages). See the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/v1/cse/list\&quot;&gt;full list&lt;/a&gt; of possible values for Google. &lt;/li&gt;&lt;li&gt;For Bing specify &lt;code&gt;setLang&#x3D;en&lt;/code&gt; parameter.&lt;/li&gt;&lt;li&gt; In Yandex use &lt;code&gt;lang&#x3D;ca&lt;/code&gt; parameter&lt;/li&gt;&lt;/ul&gt;| |gl|Specify the country to search from. It&#39;s a two-letter country code. (e.g., &lt;code&gt;sk&lt;/code&gt; for Slovakia, or &lt;code&gt;us&lt;/code&gt; for the United States).| For Google see the &lt;a href&#x3D;\&quot;https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\&quot;&gt;Country Codes&lt;/a&gt; page for a list of valid values. For Bing &lt;code&gt;cc&#x3D;at&lt;/code&gt; parameter is used.|  (required)
     * @param _callback The callback to be executed when the API call finishes
     * @return The request call
     * @throws ApiException If fail to process the API call, e.g. serializing the request body object
     * @http.response.details
     <table summary="Response Details" border="1">
        <tr><td> Status Code </td><td> Description </td><td> Response Headers </td></tr>
        <tr><td> 200 </td><td> Returns data in the one of the follwing formats - JSON, JSON Lines, CSV, MS Excel, XML </td><td>  -  </td></tr>
        <tr><td> 400 </td><td> Bad Request. Invalid payload specified. </td><td>  -  </td></tr>
        <tr><td> 401 </td><td> Unauthorized. &#x60;api_key&#x60; parameter is missed or incorrect </td><td>  -  </td></tr>
        <tr><td> 500 </td><td> Internal Server Error is a very general HTTP status code that means something has gone wrong on the web site&#39;s server. </td><td>  -  </td></tr>
     </table>
     */
    public okhttp3.Call serpAsync(Serprequest serprequest, final ApiCallback<Object> _callback) throws ApiException {

        okhttp3.Call localVarCall = serpValidateBeforeCall(serprequest, _callback);
        Type localVarReturnType = new TypeToken<Object>(){}.getType();
        localVarApiClient.executeAsync(localVarCall, localVarReturnType, _callback);
        return localVarCall;
    }
}
