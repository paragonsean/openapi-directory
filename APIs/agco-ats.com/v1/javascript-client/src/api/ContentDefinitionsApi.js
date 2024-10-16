/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import APIModelsApiError from '../model/APIModelsApiError';
import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition from '../model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition';
import APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute from '../model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute';
import ContentSubmissionSharedBusinessEntitiesContentDefinition from '../model/ContentSubmissionSharedBusinessEntitiesContentDefinition';
import ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute from '../model/ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute';

/**
* ContentDefinitions service.
* @module api/ContentDefinitionsApi
* @version v1
*/
export default class ContentDefinitionsApi {

    /**
    * Constructs a new ContentDefinitionsApi. 
    * @alias module:api/ContentDefinitionsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the contentDefinitionsDeleteContentDefinition operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsDeleteContentDefinitionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a ContentDefinition
     * Deletes an ContentDefinition. When successful, the response is empty.  If unsuccessful, an appropriate              ApiError is returned.
     * @param {Number} contentDefinitionID The ID of the ContentDefinition to delete
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsDeleteContentDefinitionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contentDefinitionsDeleteContentDefinition(contentDefinitionID, callback) {
      let postBody = null;
      // verify the required parameter 'contentDefinitionID' is set
      if (contentDefinitionID === undefined || contentDefinitionID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionID' when calling contentDefinitionsDeleteContentDefinition");
      }

      let pathParams = {
        'contentDefinitionID': contentDefinitionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions/{contentDefinitionID}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsDeleteContentDefinitionAttribute operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsDeleteContentDefinitionAttributeCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Remove an Attribute from a ContentDefinition
     * No Documentation Found.
     * @param {Number} contentDefinitionAttributeID The ID of the Attribute to remove.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsDeleteContentDefinitionAttributeCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contentDefinitionsDeleteContentDefinitionAttribute(contentDefinitionAttributeID, callback) {
      let postBody = null;
      // verify the required parameter 'contentDefinitionAttributeID' is set
      if (contentDefinitionAttributeID === undefined || contentDefinitionAttributeID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionAttributeID' when calling contentDefinitionsDeleteContentDefinitionAttribute");
      }

      let pathParams = {
        'contentDefinitionAttributeID': contentDefinitionAttributeID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitionAttributes/{contentDefinitionAttributeID}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsGetContentDefinition operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsGetContentDefinitionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ContentSubmissionSharedBusinessEntitiesContentDefinition} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a ContentDefinition by ID
     * Gets a ContentDefinition by ID. When successful, the response is the requested ContentDefinition.              If unsuccessful, an appropriate ApiError is returned.
     * @param {Number} contentDefinitionID The ID of the ContentDefinition to get.
     * @param {Object} opts Optional parameters
     * @param {String} [includeAttributes] Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsGetContentDefinitionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ContentSubmissionSharedBusinessEntitiesContentDefinition}
     */
    contentDefinitionsGetContentDefinition(contentDefinitionID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentDefinitionID' is set
      if (contentDefinitionID === undefined || contentDefinitionID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionID' when calling contentDefinitionsGetContentDefinition");
      }

      let pathParams = {
        'contentDefinitionID': contentDefinitionID
      };
      let queryParams = {
        'includeAttributes': opts['includeAttributes']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = ContentSubmissionSharedBusinessEntitiesContentDefinition;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions/{contentDefinitionID}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsGetContentDefinitionAttributes operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsGetContentDefinitionAttributesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Attributes for a ContentDefinition
     * No Documentation Found.
     * @param {Number} contentDefinitionID The ID of the ContentDefinition.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Optional. The page limit.  If not specified, the default page limit is 10.
     * @param {Number} [offset] Optional. The page offset.  If not specified, the default page offset is 0.
     * @param {String} [name] Optional. Filter the attributes by Name.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsGetContentDefinitionAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute}
     */
    contentDefinitionsGetContentDefinitionAttributes(contentDefinitionID, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'contentDefinitionID' is set
      if (contentDefinitionID === undefined || contentDefinitionID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionID' when calling contentDefinitionsGetContentDefinitionAttributes");
      }

      let pathParams = {
        'contentDefinitionID': contentDefinitionID
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'name': opts['name']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions/{contentDefinitionID}/Attributes', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsGetContentDefinitions operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsGetContentDefinitionsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get ContentDefinitions
     * Gets a collection of ContentDefinitions. When successful, the response is a PagedResponse of ContentDefinitions.              If unsuccessful, an appropriate ApiError is returned.
     * @param {Object} opts Optional parameters
     * @param {Number} [limit] Optional. The page limit.  If not specified, the default page limit is 10.
     * @param {Number} [offset] Optional. The page offset.  If not specified, the default page offset is 0.
     * @param {Number} [userID] Optional. Filter by UserID.
     * @param {String} [includeAttributes] Names of Attributes to include when retrieving this definition. This should be a comma-separated list. If not provided, Attributes are not included. If '*', all Attributes are included.
     * @param {String} [name] Optional. Filter by Name. Supports beginning and ending wildcard (*).
     * @param {Number} [typeID] Optional. Filter by TypeID.
     * @param {String} [packageTypeID] Optional. Filter by PackageTypeID.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsGetContentDefinitionsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition}
     */
    contentDefinitionsGetContentDefinitions(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'limit': opts['limit'],
        'offset': opts['offset'],
        'userID': opts['userID'],
        'includeAttributes': opts['includeAttributes'],
        'name': opts['name'],
        'typeID': opts['typeID'],
        'packageTypeID': opts['packageTypeID']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json'];
      let returnType = APIPagedResponseContentSubmissionSharedBusinessEntitiesContentDefinition;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsPostContentDefinition operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsPostContentDefinitionCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a ContentDefinition
     * Creates a ContentDefinition.  The body of the POST is the ContentDefinition to create.              The ContentDefinitionID will be assigned on creation of the Job.  When successful, the response              is the JobID.  If unsuccessful, an appropriate ApiError is returned.
     * @param {module:model/ContentSubmissionSharedBusinessEntitiesContentDefinition} contentSubmissionSharedBusinessEntitiesContentDefinition The ContentDefinition to create.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsPostContentDefinitionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    contentDefinitionsPostContentDefinition(contentSubmissionSharedBusinessEntitiesContentDefinition, callback) {
      let postBody = contentSubmissionSharedBusinessEntitiesContentDefinition;
      // verify the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinition' is set
      if (contentSubmissionSharedBusinessEntitiesContentDefinition === undefined || contentSubmissionSharedBusinessEntitiesContentDefinition === null) {
        throw new Error("Missing the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinition' when calling contentDefinitionsPostContentDefinition");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsPostContentDefinitionAttribute operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsPostContentDefinitionAttributeCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Add an Attribute to a ContentDefinition
     * No Documentation Found.
     * @param {Number} contentDefinitionID The ID of the ContentDefinition
     * @param {module:model/ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute} contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute The Attribute to add.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsPostContentDefinitionAttributeCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    contentDefinitionsPostContentDefinitionAttribute(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, callback) {
      let postBody = contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute;
      // verify the required parameter 'contentDefinitionID' is set
      if (contentDefinitionID === undefined || contentDefinitionID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionID' when calling contentDefinitionsPostContentDefinitionAttribute");
      }
      // verify the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' is set
      if (contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === undefined || contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === null) {
        throw new Error("Missing the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' when calling contentDefinitionsPostContentDefinitionAttribute");
      }

      let pathParams = {
        'contentDefinitionID': contentDefinitionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['application/json', 'application/xml', 'text/json', 'text/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions/{contentDefinitionID}/Attributes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsPostContentDefinitionAttributes operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsPostContentDefinitionAttributesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * No Documentation Found.
     * No Documentation Found.
     * @param {Number} contentDefinitionID 
     * @param {Array.<module:model/ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute>} contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute 
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsPostContentDefinitionAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contentDefinitionsPostContentDefinitionAttributes(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, callback) {
      let postBody = contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute;
      // verify the required parameter 'contentDefinitionID' is set
      if (contentDefinitionID === undefined || contentDefinitionID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionID' when calling contentDefinitionsPostContentDefinitionAttributes");
      }
      // verify the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' is set
      if (contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === undefined || contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === null) {
        throw new Error("Missing the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' when calling contentDefinitionsPostContentDefinitionAttributes");
      }

      let pathParams = {
        'contentDefinitionID': contentDefinitionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions/{contentDefinitionID}/Attributes/Batch', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsPutContentDefinition operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsPutContentDefinitionCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a ContentDefinition
     * Updates a ContentDefinition.  The body of the PUT is the updated ContentDefinition.                When successful, the response is empty.  If unsuccessful, an appropriate ApiError is returned.
     * @param {Number} contentDefinitionID The ID of the ContentDefinition to update
     * @param {module:model/ContentSubmissionSharedBusinessEntitiesContentDefinition} contentSubmissionSharedBusinessEntitiesContentDefinition The updated ContentDefinition
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsPutContentDefinitionCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contentDefinitionsPutContentDefinition(contentDefinitionID, contentSubmissionSharedBusinessEntitiesContentDefinition, callback) {
      let postBody = contentSubmissionSharedBusinessEntitiesContentDefinition;
      // verify the required parameter 'contentDefinitionID' is set
      if (contentDefinitionID === undefined || contentDefinitionID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionID' when calling contentDefinitionsPutContentDefinition");
      }
      // verify the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinition' is set
      if (contentSubmissionSharedBusinessEntitiesContentDefinition === undefined || contentSubmissionSharedBusinessEntitiesContentDefinition === null) {
        throw new Error("Missing the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinition' when calling contentDefinitionsPutContentDefinition");
      }

      let pathParams = {
        'contentDefinitionID': contentDefinitionID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitions/{contentDefinitionID}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsPutContentDefinitionAttributeAsync operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsPutContentDefinitionAttributeAsyncCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an Attribute for a ContentDefinition
     * No Documentation Found.
     * @param {Number} contentDefinitionAttributeID The ID of the Attribute to update.
     * @param {module:model/ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute} contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute The Attribute to update.
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsPutContentDefinitionAttributeAsyncCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contentDefinitionsPutContentDefinitionAttributeAsync(contentDefinitionAttributeID, contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, callback) {
      let postBody = contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute;
      // verify the required parameter 'contentDefinitionAttributeID' is set
      if (contentDefinitionAttributeID === undefined || contentDefinitionAttributeID === null) {
        throw new Error("Missing the required parameter 'contentDefinitionAttributeID' when calling contentDefinitionsPutContentDefinitionAttributeAsync");
      }
      // verify the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' is set
      if (contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === undefined || contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === null) {
        throw new Error("Missing the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' when calling contentDefinitionsPutContentDefinitionAttributeAsync");
      }

      let pathParams = {
        'contentDefinitionAttributeID': contentDefinitionAttributeID
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitionAttributes/{contentDefinitionAttributeID}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the contentDefinitionsPutContentDefinitionAttributes operation.
     * @callback module:api/ContentDefinitionsApi~contentDefinitionsPutContentDefinitionAttributesCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * No Documentation Found.
     * No Documentation Found.
     * @param {Array.<module:model/ContentSubmissionSharedBusinessEntitiesContentDefinitionAttribute>} contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute 
     * @param {module:api/ContentDefinitionsApi~contentDefinitionsPutContentDefinitionAttributesCallback} callback The callback function, accepting three arguments: error, data, response
     */
    contentDefinitionsPutContentDefinitionAttributes(contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute, callback) {
      let postBody = contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute;
      // verify the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' is set
      if (contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === undefined || contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute === null) {
        throw new Error("Missing the required parameter 'contentSubmissionSharedBusinessEntitiesContentDefinitionAttribute' when calling contentDefinitionsPutContentDefinitionAttributes");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/x-www-form-urlencoded', 'application/xml', 'text/json', 'text/xml'];
      let accepts = ['*/*'];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2/ContentDefinitionAttributes/Batch', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
