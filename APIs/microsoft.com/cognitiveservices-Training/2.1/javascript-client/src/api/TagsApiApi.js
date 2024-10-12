/**
 * TrainingApi
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Tag from '../model/Tag';

/**
* TagsApi service.
* @module api/TagsApiApi
* @version 2.1
*/
export default class TagsApiApi {

    /**
    * Constructs a new TagsApiApi. 
    * @alias module:api/TagsApiApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createTag operation.
     * @callback module:api/TagsApiApi~createTagCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Tag} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a tag for the project
     * @param {String} projectId The project id
     * @param {String} name The tag name
     * @param {String} trainingKey 
     * @param {Object} opts Optional parameters
     * @param {String} [description] Optional description for the tag
     * @param {module:api/TagsApiApi~createTagCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Tag}
     */
    createTag(projectId, name, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling createTag");
      }
      // verify the required parameter 'name' is set
      if (name === undefined || name === null) {
        throw new Error("Missing the required parameter 'name' when calling createTag");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling createTag");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'name': name,
        'description': opts['description']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Tag;
      return this.apiClient.callApi(
        '/projects/{projectId}/tags', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteTag operation.
     * @callback module:api/TagsApiApi~deleteTagCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a tag from the project
     * @param {String} projectId The project id
     * @param {String} tagId Id of the tag to be deleted
     * @param {String} trainingKey 
     * @param {module:api/TagsApiApi~deleteTagCallback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteTag(projectId, tagId, trainingKey, callback) {
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling deleteTag");
      }
      // verify the required parameter 'tagId' is set
      if (tagId === undefined || tagId === null) {
        throw new Error("Missing the required parameter 'tagId' when calling deleteTag");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling deleteTag");
      }

      let pathParams = {
        'projectId': projectId,
        'tagId': tagId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/projects/{projectId}/tags/{tagId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTag operation.
     * @callback module:api/TagsApiApi~getTagCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Tag} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get information about a specific tag
     * @param {String} projectId The project this tag belongs to
     * @param {String} tagId The tag id
     * @param {String} trainingKey 
     * @param {Object} opts Optional parameters
     * @param {String} [iterationId] The iteration to retrieve this tag from. Optional, defaults to current training set
     * @param {module:api/TagsApiApi~getTagCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Tag}
     */
    getTag(projectId, tagId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getTag");
      }
      // verify the required parameter 'tagId' is set
      if (tagId === undefined || tagId === null) {
        throw new Error("Missing the required parameter 'tagId' when calling getTag");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getTag");
      }

      let pathParams = {
        'projectId': projectId,
        'tagId': tagId
      };
      let queryParams = {
        'iterationId': opts['iterationId']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Tag;
      return this.apiClient.callApi(
        '/projects/{projectId}/tags/{tagId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTags operation.
     * @callback module:api/TagsApiApi~getTagsCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/Tag>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the tags for a given project and iteration
     * @param {String} projectId The project id
     * @param {String} trainingKey 
     * @param {Object} opts Optional parameters
     * @param {String} [iterationId] The iteration id. Defaults to workspace
     * @param {module:api/TagsApiApi~getTagsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/Tag>}
     */
    getTags(projectId, trainingKey, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling getTags");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling getTags");
      }

      let pathParams = {
        'projectId': projectId
      };
      let queryParams = {
        'iterationId': opts['iterationId']
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = [Tag];
      return this.apiClient.callApi(
        '/projects/{projectId}/tags', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateTag operation.
     * @callback module:api/TagsApiApi~updateTagCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Tag} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a tag
     * @param {String} projectId The project id
     * @param {String} tagId The id of the target tag
     * @param {String} trainingKey 
     * @param {module:model/Tag} tag The updated tag model
     * @param {module:api/TagsApiApi~updateTagCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Tag}
     */
    updateTag(projectId, tagId, trainingKey, tag, callback) {
      let postBody = tag;
      // verify the required parameter 'projectId' is set
      if (projectId === undefined || projectId === null) {
        throw new Error("Missing the required parameter 'projectId' when calling updateTag");
      }
      // verify the required parameter 'tagId' is set
      if (tagId === undefined || tagId === null) {
        throw new Error("Missing the required parameter 'tagId' when calling updateTag");
      }
      // verify the required parameter 'trainingKey' is set
      if (trainingKey === undefined || trainingKey === null) {
        throw new Error("Missing the required parameter 'trainingKey' when calling updateTag");
      }
      // verify the required parameter 'tag' is set
      if (tag === undefined || tag === null) {
        throw new Error("Missing the required parameter 'tag' when calling updateTag");
      }

      let pathParams = {
        'projectId': projectId,
        'tagId': tagId
      };
      let queryParams = {
      };
      let headerParams = {
        'Training-Key': trainingKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = Tag;
      return this.apiClient.callApi(
        '/projects/{projectId}/tags/{tagId}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
