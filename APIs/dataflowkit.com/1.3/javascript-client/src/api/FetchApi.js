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
import Fetchrequest from '../model/Fetchrequest';

/**
* Fetch service.
* @module api/FetchApi
* @version 1.3
*/
export default class FetchApi {

    /**
    * Constructs a new FetchApi. 
    * @alias module:api/FetchApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the fetch operation.
     * @callback module:api/FetchApi~fetchCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Download web page content
     * Use fetch endpoint to download web pages.
     * @param {module:model/Fetchrequest} fetchrequest - _Base fetcher type_ is the right choice for fetching server-side rendered pages. It takes fewer resources and works faster than rendering HTML with _Chrome fetcher_ - But for rendering Angular, React, and Vue.js web sites, you should always specify _Chrome fetcher type_. In this case, headless chrome fetcher renders dynamic Javascript content in the same way as real web browsers would do it.  Generate ready-to-run code for your favorite language at [https://dataflowkit.com/render-web](https://dataflowkit.com/render-web) 
     * @param {module:api/FetchApi~fetchCallback} callback The callback function, accepting three arguments: error, data, response
     */
    fetch(fetchrequest, callback) {
      let postBody = fetchrequest;
      // verify the required parameter 'fetchrequest' is set
      if (fetchrequest === undefined || fetchrequest === null) {
        throw new Error("Missing the required parameter 'fetchrequest' when calling fetch");
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
      let accepts = ['text/html; charset=utf-8', 'text/plain; charset=utf-8'];
      let returnType = null;
      return this.apiClient.callApi(
        '/fetch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
