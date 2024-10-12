/**
 * Flinkster_API_NG
 * This REST-API enables you to query for private transport sharing offers provided by companies and cities in Germany, Netherland and Austria.  You can search for informations about the rental stations (points or areas) where you can find the rentals by utilizing the /areas/ ressource.  With the help of the proximity search in the /bookingproposals/ URI you can request the availabilities of the rentalobjects for spontaneous or planed usage in the future.   Feel free to browse through data by setting the parameter 'providernetwork' to the value:   1: Search for car sharing offers provided by the Flinkster platform (http://www.flinkster.de) 2: Finding bike rental offers from Call a Bike (http://www.callabike.de)   You can find more details in the documentation section (Unfortunately only available in german language).  Have lots of fun and we are lucky to take notice of your products or getting your feedback.
 *
 * The version of the OpenAPI document: v1
 * Contact: partner@flinkster.de
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CategoryJO from '../model/CategoryJO';
import ErrorJO from '../model/ErrorJO';

/**
* Categories service.
* @module api/CategoriesApi
* @version v1
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
     * Callback function to receive the result of the getCategory operation.
     * @callback module:api/CategoriesApi~getCategoryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CategoryJO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Category by UID
     * Search for categorie.
     * @param {String} providernetworkUID Provider Network UID
     * @param {String} categoryUID 
     * @param {Object} opts Optional parameters
     * @param {String} [expand] 
     * @param {module:api/CategoriesApi~getCategoryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CategoryJO}
     */
    getCategory(providernetworkUID, categoryUID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'providernetworkUID' is set
      if (providernetworkUID === undefined || providernetworkUID === null) {
        throw new Error("Missing the required parameter 'providernetworkUID' when calling getCategory");
      }
      // verify the required parameter 'categoryUID' is set
      if (categoryUID === undefined || categoryUID === null) {
        throw new Error("Missing the required parameter 'categoryUID' when calling getCategory");
      }

      let pathParams = {
        'providernetworkUID': providernetworkUID,
        'categoryUID': categoryUID
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CategoryJO;
      return this.apiClient.callApi(
        '/providernetworks/{providernetworkUID}/categories/{categoryUID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the listCategories operation.
     * @callback module:api/CategoriesApi~listCategoriesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CategoryJO} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists all categories
     * Search for categorie.
     * @param {String} providernetworkUID 
     * @param {Object} opts Optional parameters
     * @param {String} [expand] 
     * @param {module:api/CategoriesApi~listCategoriesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CategoryJO}
     */
    listCategories(providernetworkUID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'providernetworkUID' is set
      if (providernetworkUID === undefined || providernetworkUID === null) {
        throw new Error("Missing the required parameter 'providernetworkUID' when calling listCategories");
      }

      let pathParams = {
        'providernetworkUID': providernetworkUID
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = CategoryJO;
      return this.apiClient.callApi(
        '/providernetworks/{providernetworkUID}/categories', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
