/**
 * Custom Vision Training Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 3.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CustomVisionError from '../model/CustomVisionError';
import SuggestedTagAndRegion from '../model/SuggestedTagAndRegion';

/**
* SuggestTagsAndRegionsApi service.
* @module api/SuggestTagsAndRegionsApiApi
* @version 3.2
*/
export default class SuggestTagsAndRegionsApiApi {

    /**
    * Constructs a new SuggestTagsAndRegionsApiApi. 
    * @alias module:api/SuggestTagsAndRegionsApiApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the suggestTagsAndRegions operation.
     * @callback module:api/SuggestTagsAndRegionsApiApi~suggestTagsAndRegionsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/SuggestedTagAndRegion>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found.
     * This API will get suggested tags and regions for an array/batch of untagged images along with confidences for the tags. It returns an empty array if no tags are found.  There is a limit of 64 images in the batch.
     * @param {String} projectId The project id.
     * @param {String} iterationId IterationId to use for tag and region suggestion.
     * @param {Array.<String>} imageIds Array of image ids tag suggestion are needed for. Use GetUntaggedImages API to get imageIds.
     * @param {module:api/SuggestTagsAndRegionsApiApi~suggestTagsAndRegionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/SuggestedTagAndRegion>}
     */
    suggestTagsAndRegions(projectId, iterationId, imageIds, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling suggestTagsAndRegions");
      }
      // verify the required parameter 'iterationId' is set
      if (iterationId === undefined || iterationId === null) {
        throw new Error("Missing the required parameter 'iterationId' when calling suggestTagsAndRegions");
      }
      // verify the required parameter 'imageIds' is set
      if (imageIds === undefined || imageIds === null) {
        throw new Error("Missing the required parameter 'imageIds' when calling suggestTagsAndRegions");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'iterationId': iterationId,
        'imageIds': this.apiClient.buildCollectionParam(imageIds, 'csv')
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apim_key'];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/xml'];
      let returnType = [SuggestedTagAndRegion];
      return this.apiClient.callApi(
        '/projects/{projectId}/tagsandregions/suggestions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
