/**
 * OpenFinTech.io
 * # Introduction [OpenFinTech.io](https://openfintech.io) is an open database that comprises of standardized primary data for FinTech industry.<br> It contains such information as geolocation data (countries, cities, regions), organizations, currencies (national, digital, virtual, crypto), banks, digital exchangers, payment providers (PSP), payment methods, etc.<br> It is created for communication of cross-integrated micro-services on \"one language\". This is achieved through standardization of entity identifiers that are used to exchange information among different services.<br>  ### UML UML Domain Model diagram you can find [here](https://api.openfintech.io/public_domain_model.png).<br>  ### Persistence Entities are updated not more than 1 time per day.<br>  ### Terms and Conditions This *OpenFinTech.io* is made available under the [Open Database License](http://opendatacommons.org/licenses/odbl/1.0/).<br> Any rights in individual contents of the database are licensed under the [Database Contents License](http://opendatacommons.org/licenses/dbcl/1.0/).<br>  ### Contacts For any questions, please email - info@openfintech.io<br> Or you can contact us at <a href=\"https://gitter.im/paymaxicom/openfintech.io\">Gitter</a><br>  Powered by [Paymaxi](https://www.paymaxi.com)  # Get Started  If you use [POSTMAN](https://www.getpostman.com) or similar program which can operate with swagger`s files - just [download](https://docs.openfintech.io) our spec and [import it](https://www.getpostman.com/docs/importing_swagger). Also you can try live [API demo](https://api.openfintech.io).  ## Overview  The OpenFinTech API is organized around [REST](https://en.wikipedia.org/wiki/Representational_state_transfer). Our API has predictable, resource-oriented URLs, and uses HTTP response codes to indicate API errors.<br> API is based on [JSON API](http://jsonapi.org) standard. JSON is returned by all API responses, including errors, although our API libraries convert responses to appropriate language-specific objects.<br> JSON API requires use of the JSON API media type (`application/vnd.api+json`) for exchanging data.<br> ### Additional Request Headers #### ACCEPT HEADER Your requests should always include the header: ```curl Accept: application/vnd.api+json ```  ## Authentication  To use OpenFinTech API no needed authorization.  ## Versioning  When we make changes to the API, we release new, dated versions. The current version is **2017-08-24**. Read our [API upgrades guide]() to see our API changelog and to learn more about backwards compatibility.  ## Pagination  OpenFinTech APIs to retrieve lists of banks, currencies and other resources - paginated to **100** items by default. The pagination information will be included in the list API response under the node name `meta` - contains information about listed objects [`total` - contains information about total count of listed objects, `pages` - count of pages], `links` - contain links to navigate between pages [`first` - link to first page, `prev` - link to previous page, `next` - link to next page, `last` - link to last page].<br> By default first page will be listed. For navigating through pages, use the page parameter (e.g. `page[number]`, `page[size]`).<br> The `page[size]` parameter can be used to set the number of records that you want to receive in the response.<br> The `page[number]` parameter can be used to set needed page number.<br> Example of response: ```json {   \"meta\": {     \"total\": 419,     \"pages\": 42   },   \"links\": {     \"first\": \"/v1/{path}?page[number]=1&page[size]=10\",     \"prev\": \"/v1/{path}?page[number]=39&page[size]=10\",     \"next\": \"/v1/{path}?page[number]=41&page[size]=10\",     \"last\": \"/v1/{path}?page[number]=42&page[size]=10\"   } ```  ### Sorting  OpenFinTech\\`s API supported query parameter to sort result collection [e.g. `?sort=code`]. Information about available parameters may be found in the endpoint description. Positive parameter [e.g. `?sort=code`] points to ascending sorting, negative  [e.g. `?sort=-code`] - to descending sorting. Also, supported multiple sorting parameters [e.g. `?sort=code, -name, id`, etc.] ```curl https://api.openfintech.io/v1/countries?sort=name,-area ```  ### Filtering  Filtering provided by unique query key `filter[*filtering_condition*]`. Information about available parameters may be found in the endpoint description. ```curl https://api.openfintech.io/v1/countries?filter[region]=europe ```  ## Images  OpenFinTech provides two types of images: icons and logos. To get one of those types you should to use next url pattern: ``` curl https://api.openfintech.io/v1/{path}/{id}/{icon/logo} ``` Also, images can be resized by adding next parameters: `h={height}&w={width}`. For example, you want to get organization icon with width equals to 20 pixels: ``` curl https://api.openfintech.io/v1/organizations/{id}/icon?w=20&h=20 ``` If argument height or width is missing API returns original image with real sizes.  ## Errors  API uses conventional HTTP response codes to indicate the success or failure of an API request. In general, codes in the `2xx` range indicate success, codes in the `4xx` range indicate an error that failed given the information provided (e.g., a required parameter was omitted, etc.), and codes in the `5xx` range indicate an error with OpenFinTech's servers (these are rare).  | Code | Description | |------|-------------| | 200 - OK | Everything worked as expected. | | 400 - Bad Request | The request was unacceptable, often due to missing a required parameter. | | 401 - Unauthorized | No valid API key provided. | | 402 - Request Failed | The parameters were valid but the request failed. | | 404 - Not Found | The requested resource doesn't exist. | | 409 - Conflict | The request conflicts with another request (perhaps due to using the same idempotent key). | | 429 - Too Many Requests | Too many requests hit the API too quickly. We recommend an exponential backoff of your requests. | | 500, 502, 503, 504 - Server Errors | Something went wrong on OpenFinTech's end. (These are rare.) | 
 *
 * The version of the OpenAPI document: 2017-08-24
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import DepositMethodResponse from '../model/DepositMethodResponse';
import DepositMethodsResponse from '../model/DepositMethodsResponse';

/**
* DepositMethods service.
* @module api/DepositMethodsApi
* @version 2017-08-24
*/
export default class DepositMethodsApi {

    /**
    * Constructs a new DepositMethodsApi. 
    * @alias module:api/DepositMethodsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the depositMethodsGet operation.
     * @callback module:api/DepositMethodsApi~depositMethodsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DepositMethodsResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List of deposit methods
     * Returns list of deposit methods. Each object contains information about deposit method such as name and category, also related link to deposit method issuer (which processing it). 
     * @param {Object} opts Optional parameters
     * @param {Number} [pageNumber] Current page number.
     * @param {Number} [pageSize] Page size.<br>*Default value: 100* 
     * @param {String} [filterSearch] Full text search with id, name, code, category.
     * @param {String} [filterName] Filtering by name.
     * @param {String} [filterCode] Filtering by code.
     * @param {String} [filterProcessorName] Filtering by processor_name.
     * @param {Array.<module:model/String>} [filterCategory] Filtering by category.
     * @param {Array.<module:model/String>} [sort] Sort params:<br>  | ASC | DESC | |-----|------| | name | -name | | code | -code | | processor_name | -processor_name | | category | -category | 
     * @param {module:api/DepositMethodsApi~depositMethodsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DepositMethodsResponse}
     */
    depositMethodsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'page[number]': opts['pageNumber'],
        'page[size]': opts['pageSize'],
        'filter[search]': opts['filterSearch'],
        'filter[name]': opts['filterName'],
        'filter[code]': opts['filterCode'],
        'filter[processor_name]': opts['filterProcessorName'],
        'filter[category]': this.apiClient.buildCollectionParam(opts['filterCategory'], 'csv'),
        'sort': this.apiClient.buildCollectionParam(opts['sort'], 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/vnd.api+json'];
      let returnType = DepositMethodsResponse;
      return this.apiClient.callApi(
        '/deposit-methods', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the depositMethodsIdGet operation.
     * @callback module:api/DepositMethodsApi~depositMethodsIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/DepositMethodResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deposit method by ID
     * Returns deposit method with specific ID. 
     * @param {String} id Unique ID.
     * @param {module:api/DepositMethodsApi~depositMethodsIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/DepositMethodResponse}
     */
    depositMethodsIdGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling depositMethodsIdGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/vnd.api+json'];
      let returnType = DepositMethodResponse;
      return this.apiClient.callApi(
        '/deposit-methods/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
