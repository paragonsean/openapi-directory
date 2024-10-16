/**
 * Test the ExhibitDay API with Swagger
 * This API can be used to programmatically pull data out of ExhibitDay or push data into ExhibitDay -- allowing for automation between ExhibitDay and your internal systems (or other third-party software). To use the API, you'll need working knowledge of consuming REST APIs.<br /><br />Docs: https://api.exhibitday.com/swagger/docs/v1
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";

/**
* Swagger service.
* @module api/SwaggerApi
* @version v1
*/
export default class SwaggerApi {

    /**
    * Constructs a new SwaggerApi. 
    * @alias module:api/SwaggerApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the swaggerGet operation.
     * @callback module:api/SwaggerApi~swaggerGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * @param {module:api/SwaggerApi~swaggerGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    swaggerGet(callback) {
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/api/docs/Swagger', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
