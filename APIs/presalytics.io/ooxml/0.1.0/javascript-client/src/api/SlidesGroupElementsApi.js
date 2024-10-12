/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import SlideGroupElements from '../model/SlideGroupElements';

/**
* SlidesGroupElements service.
* @module api/SlidesGroupElementsApi
* @version 0.1.0
*/
export default class SlidesGroupElementsApi {

    /**
    * Constructs a new SlidesGroupElementsApi. 
    * @alias module:api/SlidesGroupElementsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the slidesGroupelementsGetId operation.
     * @callback module:api/SlidesGroupElementsApi~slidesGroupelementsGetIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/SlideGroupElements} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * GroupElements: Get by Id
     * Get by Id: Use this method to retrieve a GroupElements object by its primary key (id)
     * @param {String} id 
     * @param {module:api/SlidesGroupElementsApi~slidesGroupelementsGetIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/SlideGroupElements}
     */
    slidesGroupelementsGetId(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling slidesGroupelementsGetId");
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
      let accepts = ['application/json'];
      let returnType = SlideGroupElements;
      return this.apiClient.callApi(
        '/Slides/GroupElements/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
