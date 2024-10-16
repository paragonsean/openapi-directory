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
* References service.
* @module api/ReferencesApi
* @version v1
*/
export default class ReferencesApi {

    /**
    * Constructs a new ReferencesApi. 
    * @alias module:api/ReferencesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the referencesEventCostTypes0Get operation.
     * @callback module:api/ReferencesApi~referencesEventCostTypes0GetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event Cost Types
     * @param {String} apiKey 
     * @param {module:api/ReferencesApi~referencesEventCostTypes0GetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    referencesEventCostTypes0Get(apiKey, callback) {
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling referencesEventCostTypes0Get");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'api_key': apiKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v1/references/event_cost_types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesEventCustomFields0Get operation.
     * @callback module:api/ReferencesApi~referencesEventCustomFields0GetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event Custom Fields
     * @param {String} apiKey 
     * @param {module:api/ReferencesApi~referencesEventCustomFields0GetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    referencesEventCustomFields0Get(apiKey, callback) {
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling referencesEventCustomFields0Get");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'api_key': apiKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v1/references/event_custom_fields', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesEventParticipationTypes0Get operation.
     * @callback module:api/ReferencesApi~referencesEventParticipationTypes0GetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event Participation Types
     * @param {String} apiKey 
     * @param {module:api/ReferencesApi~referencesEventParticipationTypes0GetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    referencesEventParticipationTypes0Get(apiKey, callback) {
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling referencesEventParticipationTypes0Get");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'api_key': apiKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v1/references/event_participation_types', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesEventTags0Get operation.
     * @callback module:api/ReferencesApi~referencesEventTags0GetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Event Tags
     * @param {String} apiKey 
     * @param {module:api/ReferencesApi~referencesEventTags0GetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    referencesEventTags0Get(apiKey, callback) {
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling referencesEventTags0Get");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'api_key': apiKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v1/references/event_tags', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the referencesUsersAndResources0Get operation.
     * @callback module:api/ReferencesApi~referencesUsersAndResources0GetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * User and Resources
     * @param {String} apiKey 
     * @param {module:api/ReferencesApi~referencesUsersAndResources0GetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    referencesUsersAndResources0Get(apiKey, callback) {
      let postBody = null;
      // verify the required parameter 'apiKey' is set
      if (apiKey === undefined || apiKey === null) {
        throw new Error("Missing the required parameter 'apiKey' when calling referencesUsersAndResources0Get");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'api_key': apiKey
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v1/references/users_and_resources', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
