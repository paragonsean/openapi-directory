/**
 * Pims
 *  Hereafter is the documentation of the private API of [Pims: Pointages Intelligents pour le Monde du Spectacle](https://pims.io). This API is designed for 3rd-party softwares, editors and partners. Its main purpose is to give access the core data of a Pims customer (i.e. events, ticket counts and promotions).  ## Authentication The API uses [basic access authentication](https://en.wikipedia.org/wiki/Basic_access_authentication), meaning you will need a username and password to get authorized.  As each customer in Pims has its own domain (e.g. caramba.pims.io, gdp.pims.io...), each credentials will be valid for one domain/customer only. If you need dedicated credentials for one domain, please contact us. (In any case, we will need an explicit agreement from the customer before we create these credentials.)  <div class=\"info\"> To make your life easy, you can try all endpoints with the public credentials below, pointing to our [demo domain](https://demo.pims.io):   <ul>     <li>Base path: `https://demo.pims.io/api`</li>     <li>Username: `demo`</li>     <li>Password: `q83792db2GCvgYVdKpU3yG3R`</li>   </ul> </div>  ## Response format The API returns JSON and matches the [HAL specification](http://stateless.co/hal_specification.html). The `Content-Type` of each response will be `application/hal+json`, unless an error occurs.  Please note that this documentation describes all responses “as if” they were plain JSON. The specificities of HAL are ignored on purpose, in order to remain compact and avoid repetition. <div style=\"-webkit-column-count: 2; -moz-column-count: 2; column-count: 2; -webkit-column-rule: 1px dotted #e0e0e0; -moz-column-rule: 1px dotted #e0e0e0; column-rule: 1px dotted #e0e0e0;\">  <div style=\"display: inline-block; width:100%;\">   <strong>So when you read in the doc:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property1\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"object\"</span>: {   <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,   <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>  } }</code></pre>  </div>  <div style=\"display: inline-block; width:100%;\">   <strong>... you'll get in the Real World®:</strong> <pre><code class=\"lang-json\">{  <span class=\"token string\">\"id\"</span>: <span class=\"token number\">123</span>,  <span class=\"token string\">\"property2\"</span>: <span class=\"token string\">\"Lorem ipsum\"</span>,  <span class=\"token string\">\"_embedded\"</span>: {   <span class=\"token string\">\"object\"</span>: {    <span class=\"token string\">\"id\"</span>: <span class=\"token number\">456</span>,    <span class=\"token string\">\"property2\"</span>: <span class=\"token number\">7.89</span>,    <span class=\"token string\">\"_links\"</span>: {     <span class=\"token string\">\"self\"</span>: {      <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/other-item/456\"</span>     }    }   }  }  <span class=\"token string\">\"_links\"</span>: {   <span class=\"token string\">\"self\"</span>: {    <span class=\"token string\">\"href\"</span>: <span class=\"token string\">\"https://api.mydomain.com/item/123\"</span>   }  } }</code></pre>  </div> </div>  ### Errors Errors return JSON too and tries to match the [Problem Details for HTTP APIs specification](https://tools.ietf.org/html/rfc7807). If it does not match this spec, that's either a bug or a compatibility issue. Please contact us to solve the problem.  The `Content-Type` of errors will be `application/problem+json`. The content will match the following JSON: ```json {  \"type\": \"https://tools.ietf.org/html/rfc2616#section-10\",     \"title\": \"Not Found\",  \"status\": 404,     \"detail\": \"Entity not found\" } ```  ## Versioning The API is fully versionned, using an URL-versioning scheme: `https://demo.pims.io/api/v1/events`, `https://demo.pims.io/api/v2/events`,...  The version part of the URL is optional, and will be completed with the last stable version if omitted.  ## Pagination All responses corresponding to a collection of resources (e.g. `/venues` or `/series/:id/events`) are paginated. When so, you will only get the first 25 resources you asked for.  If you need to get more resources in one call, you can use the `page_size` query parameter. E.g. `/venues?page_size=50` to get the 50 first venues.  Also note that with HAL, the navigation in paginated responses is a piece of cake, as you can see below: ```json {  \"_links\": {   \"self\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=1\"   },   \"first\": {    \"href\": \"https://demo.pims.io/api/v1/events\"   },   \"last\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=14\"   },   \"next\": {    \"href\": \"https://demo.pims.io/api/v1/events?page=2\"   }  },  \"_embedded\": {    ... // data content goes here  },  \"page_count\": 14,  \"page_size\": 25,  \"total_items\": 331,  \"page\": 1 } ```  ## Filtering and sorting Every textual filter (e.g. `/events?label=U2`) and/or sort (e.g. `/events?sort=label`) performed with the API uses UTF8_UNICODE_CI collation, meaning it is: - Case insensitive: “Chloé” will be considered the same as “CHLOÉ”; - Diacritic insensitive: “Chloé” will be considered the same as “Chloe”.  When performing a sort, it will always be *ascending* by default. To make it *descending*, just use a minus sign (`-`) in front of the parameter value (e.g. `/events?sort=-label`).  ## I18n In responses, some labels can be translated (e.g. promotion types, event input types, etc.). These translatable labels are clearly indicated in the documentation below.  By default, they will be displayed in English, but you can change this behaviour via the `Accept-Language` header. E.g., use `fr` as a value for French.  ## PHP SDK We provide a simple yet convenient SDK for the PHP language, see [the Github page of the project](https://github.com/pimssas/pims-api-client-php).  ## And now? Generaly, you will start by [fetching one or more events](#tag/Events). An <span class=\"definition\">event</span> can be anything that occurs in one venue at one given date and time: a concert, a play, a match, a conference, etc. Additionnally, you can explore the [series](#tag/Series): a <span class=\"definition\">series</span> is just a group of events (e.g. a tour or a festival).  Once you retrieved the events you were interested in, you can look for the sales (<span class=\"definition\">ticket counts</span>): - Get a quick overview with [`/events/:id/ticket-counts`](#operation/fetchAllTicketCounts) - Or get a full insight by calling these endpoints:     1. [`/events/:id/categories`](#operation/fetchAllEventsCategories)     2. [`/events/:id/channels`](#operation/fetchAllEventsChannels)     3. [`/events/:id/ticket-counts/detailed`](#operation/fetchAllDetailedTicketCounts)  Eventually, you may also want to fetch the [promotions](#tag/Promotions). A <span class=\"definition\">promotion</span> can be anything meant to leverage the sales: ads, marketing campaigns, buzz or news around the event, etc. A promotion can be linked to any combination of events and/or series.
 *
 * The version of the OpenAPI document: 1.0
 * Contact: support@pims.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CategoriesEntity from '../model/CategoriesEntity';
import Error401 from '../model/Error401';
import Error403 from '../model/Error403';
import Error404 from '../model/Error404';
import Error422 from '../model/Error422';
import Error500 from '../model/Error500';
import EventsCategoriesEntity from '../model/EventsCategoriesEntity';

/**
* Categories service.
* @module api/CategoriesApi
* @version 1.0
*/
export default class CategoriesApi {

    /**
    * Constructs a new CategoriesApi. 
    * @alias module:api/CategoriesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the fetchAllCategories operation.
     * @callback module:api/CategoriesApi~fetchAllCategoriesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/CategoriesEntity>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find all categories
     * @param {Object} opts Optional parameters
     * @param {String} [label] Find only the categories whose label/short label contains this value.
     * @param {Boolean} [showIgnored = false)] If set to `false`, show only the categories which are not ignored. If set to `true`, show all categories.
     * @param {module:model/String} [sort = 'order')] Sort the categories in the corresponding order.
     * @param {Number} [pageSize = 25)] Pagination size, i.e. maximum number of items to be displayed in the response.
     * @param {module:model/String} [acceptLanguage = 'en')] Language used for the translatable labels.
     * @param {module:api/CategoriesApi~fetchAllCategoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/CategoriesEntity>}
     */
    fetchAllCategories(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'label': opts['label'],
        'show_ignored': opts['showIgnored'],
        'sort': opts['sort'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
        'Accept-Language': opts['acceptLanguage']
      };
      let formParams = {
      };

      let authNames = ['Basic Auth'];
      let contentTypes = [];
      let accepts = ['application/hal+json'];
      let returnType = [CategoriesEntity];
      return this.apiClient.callApi(
        '/categories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchAllEventsCategories operation.
     * @callback module:api/CategoriesApi~fetchAllEventsCategoriesCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/EventsCategoriesEntity>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Find all categories for one event
     * @param {Number} eventId ID of the targeted event.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [showIgnored = false)] If set to `false`, show only the [event-]categories/[event-]price ranges which are not ignored. If set to `true`, show everything.
     * @param {Number} [pageSize = 25)] Pagination size, i.e. maximum number of items to be displayed in the response.
     * @param {module:api/CategoriesApi~fetchAllEventsCategoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/EventsCategoriesEntity>}
     */
    fetchAllEventsCategories(eventId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling fetchAllEventsCategories");
      }

      let pathParams = {
        'event_id': eventId
      };
      let queryParams = {
        'show_ignored': opts['showIgnored'],
        'page_size': opts['pageSize']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Basic Auth'];
      let contentTypes = [];
      let accepts = ['application/hal+json'];
      let returnType = [EventsCategoriesEntity];
      return this.apiClient.callApi(
        '/events/{event_id}/categories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchOneCategory operation.
     * @callback module:api/CategoriesApi~fetchOneCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CategoriesEntity} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get one category by ID
     * @param {Number} categoryId ID of the targeted category.
     * @param {Object} opts Optional parameters
     * @param {module:model/String} [acceptLanguage = 'en')] Language used for the translatable labels.
     * @param {module:api/CategoriesApi~fetchOneCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CategoriesEntity}
     */
    fetchOneCategory(categoryId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling fetchOneCategory");
      }

      let pathParams = {
        'category_id': categoryId
      };
      let queryParams = {
      };
      let headerParams = {
        'Accept-Language': opts['acceptLanguage']
      };
      let formParams = {
      };

      let authNames = ['Basic Auth'];
      let contentTypes = [];
      let accepts = ['application/hal+json'];
      let returnType = CategoriesEntity;
      return this.apiClient.callApi(
        '/categories/{category_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchOneEventCategory operation.
     * @callback module:api/CategoriesApi~fetchOneEventCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EventsCategoriesEntity} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get one event category by ID
     * @param {Number} eventId ID of the targeted event.
     * @param {Number} categoryId ID of the targeted event category.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [showIgnored = false)] If set to `false`, show only the embedded [event-]price ranges which are not ignored. If set to `true`, show everything.
     * @param {module:api/CategoriesApi~fetchOneEventCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EventsCategoriesEntity}
     */
    fetchOneEventCategory(eventId, categoryId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'eventId' is set
      if (eventId === undefined || eventId === null) {
        throw new Error("Missing the required parameter 'eventId' when calling fetchOneEventCategory");
      }
      // verify the required parameter 'categoryId' is set
      if (categoryId === undefined || categoryId === null) {
        throw new Error("Missing the required parameter 'categoryId' when calling fetchOneEventCategory");
      }

      let pathParams = {
        'event_id': eventId,
        'category_id': categoryId
      };
      let queryParams = {
        'show_ignored': opts['showIgnored']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['Basic Auth'];
      let contentTypes = [];
      let accepts = ['application/hal+json'];
      let returnType = EventsCategoriesEntity;
      return this.apiClient.callApi(
        '/events/{event_id}/categories/{category_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
