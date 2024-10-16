/**
 * Dataflow Kit Web Scraper
 * Render Javascript driven pages, while we internally manage Headless Chrome and proxies for you.   - Build a custom web scraper with our Visual point-and-click toolkit. - Scrape the most popular Search engines result pages (SERP). - Convert web pages to PDF and capture screenshots. *** ### Authentication Dataflow Kit API require you to sign up for an API key in order to use the API.   The API key can be found in the [DFK Dashboard](https://account.dataflowkit.com) after _free registration_.  Pass a secret API Key to all API requests to the server as the `api_key` query parameter.  
 *
 * The version of the OpenAPI document: 1.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Serprequest from '../model/Serprequest';

/**
* Serp service.
* @module api/SerpApi
* @version 1.3
*/
export default class SerpApi {

    /**
    * Constructs a new SerpApi. 
    * @alias module:api/SerpApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the serp operation.
     * @callback module:api/SerpApi~serpCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Collect search results from search engines
     * To crawl search engine result pages, you can use `/serp` endpoint. SERP collection service extracts a list of organic results, news, images, and more.  Specify configuration parameters, such as country or languages, to customize output SERP data. The following search engines are supported  - google - google-image - google-news - google-shopping - bing - duckduckgo - baidu - yandex   Generate ready-to-run code for your favorite language at [https://dataflowkit.com/serp](https://dataflowkit.com/serp)
     * @param {module:model/Serprequest} serprequest <h2>Search parameters</h2>  > In most cases, you don't need to customize parameters by hand. Use <a href=\"https://dataflowkit.com/serp\" target=\"_blank\">SERP extraction Code generator</a>. It is the easiest way to generate a payload for launching in the Dataflow kit cloud.  <h3>URL GET parameters</h3>  |||| |-|-|-| |q| Parameter defines encoded search term. You can use anything that you would use in a regular Search engines search. (e.g. for Google, <ul> <li><code>link:dataflowkit.com</code>,</li> <li><code>site:twitter.com Bratislava</code>,</li><li><code>inurl:view/view.shtml</code>, etc.)</li></ul> See The Complete List of 42 Advanced <a href=\"https://ahrefs.com/blog/google-advanced-search-operators/\" target=\"_blank\">Google Search Operators</a>|<ul> <li><code>q</code> parameter is used by google, Bing, DuckDuckGo.</li><li> <code>text</code> is used as query holder by Yandex SE.</li><li> Chineese Baidu uses <code>wd</code> for this purpose.</li></ul>| |tbm| <code>tbm</code> is a special Google parameter used to differentiate between search types|  <ul> <li><code>tbm=isch</code> - Google Images,</li> <li> <code>tbm=nws</code> - Google News</li> <li><code>tbm=shop</code> - Google Shopping</li> </ul>| |lr|Restricts the search to documents written in a particular languages.|<ul><li>Google uses <code>lang_{two-letter lang code}</code> to specify languages and <code>&#124;</code> as a delimiter. (e.g., <code>lang_sk&#124;lang_de</code> will only search Slovak and German pages). See the <a href=\"https://developers.google.com/custom-search/v1/cse/list\">full list</a> of possible values for Google. </li><li>For Bing specify <code>setLang=en</code> parameter.</li><li> In Yandex use <code>lang=ca</code> parameter</li></ul>| |gl|Specify the country to search from. It's a two-letter country code. (e.g., <code>sk</code> for Slovakia, or <code>us</code> for the United States).| For Google see the <a href=\"https://developers.google.com/custom-search/docs/xml_results_appendices#countryCodes\">Country Codes</a> page for a list of valid values. For Bing <code>cc=at</code> parameter is used.| 
     * @param {module:api/SerpApi~serpCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    serp(serprequest, callback) {
      let postBody = serprequest;
      // verify the required parameter 'serprequest' is set
      if (serprequest === undefined || serprequest === null) {
        throw new Error("Missing the required parameter 'serprequest' when calling serp");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['ApiKeyAuth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json', 'application/x-ndjson', 'text/csv', 'text/plain; charset=utf-8'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/serp', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
