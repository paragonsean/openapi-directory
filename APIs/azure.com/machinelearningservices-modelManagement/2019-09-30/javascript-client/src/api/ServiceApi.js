/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import AuthKeys from '../model/AuthKeys';
import AuthToken from '../model/AuthToken';
import CreateServiceRequest from '../model/CreateServiceRequest';
import JsonPatchOperation from '../model/JsonPatchOperation';
import ModelErrorResponse from '../model/ModelErrorResponse';
import PaginatedServiceList from '../model/PaginatedServiceList';
import RegenerateServiceKeysRequest from '../model/RegenerateServiceKeysRequest';
import ServiceResponseBase from '../model/ServiceResponseBase';

/**
* Service service.
* @module api/ServiceApi
* @version 2019-09-30
*/
export default class ServiceApi {

    /**
    * Constructs a new ServiceApi. 
    * @alias module:api/ServiceApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the servicesCreate operation.
     * @callback module:api/ServiceApi~servicesCreateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a Service.
     * Create a Service with the specified payload.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {module:model/CreateServiceRequest} request The payload that is used to create the Service.
     * @param {module:api/ServiceApi~servicesCreateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    servicesCreate(subscriptionId, resourceGroup, workspace, request, callback) {
      let postBody = request;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesCreate");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesCreate");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesCreate");
      }
      // verify the required parameter 'request' is set
      if (request === undefined || request === null) {
        throw new Error("Missing the required parameter 'request' when calling servicesCreate");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesDelete operation.
     * @callback module:api/ServiceApi~servicesDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete a Service.
     * Delete a specific Service.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The Service Id.
     * @param {module:api/ServiceApi~servicesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    servicesDelete(subscriptionId, resourceGroup, workspace, id, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesDelete");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesDelete");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesDelete");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling servicesDelete");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesGetServiceToken operation.
     * @callback module:api/ServiceApi~servicesGetServiceTokenCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthToken} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Generate Service Access Token.
     * Gets access token that can be used for calling service.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The Service Id.
     * @param {module:api/ServiceApi~servicesGetServiceTokenCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthToken}
     */
    servicesGetServiceToken(subscriptionId, resourceGroup, workspace, id, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesGetServiceToken");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesGetServiceToken");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesGetServiceToken");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling servicesGetServiceToken");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AuthToken;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/token', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesListQuery operation.
     * @callback module:api/ServiceApi~servicesListQueryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaginatedServiceList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Query the list of Services in a Workspace.
     * If no filter is passed, the query lists all Services in the Workspace. The returned list is paginated and the count of item in each page is an optional parameter.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {Object} opts Optional parameters
     * @param {String} [imageId] The Image Id.
     * @param {String} [imageName] The Image name.
     * @param {String} [modelId] The Model Id.
     * @param {String} [modelName] The Model name.
     * @param {String} [name] The object name.
     * @param {Number} [count] The number of items to retrieve in a page.
     * @param {String} [computeType] The compute environment type.
     * @param {String} [skipToken] The continuation token to retrieve the next page.
     * @param {String} [tags] A set of tags with which to filter the returned models.              It is a comma separated string of tags key or tags key=value              Example: tagKey1,tagKey2,tagKey3=value3
     * @param {String} [properties] A set of properties with which to filter the returned models.              It is a comma separated string of properties key and/or properties key=value              Example: propKey1,propKey2,propKey3=value3
     * @param {Boolean} [expand = false)] Set to True to include Model details.
     * @param {module:model/String} [orderby = 'UpdatedAtDesc')] The option to order the response.
     * @param {module:api/ServiceApi~servicesListQueryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaginatedServiceList}
     */
    servicesListQuery(subscriptionId, resourceGroup, workspace, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesListQuery");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesListQuery");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesListQuery");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace
      };
      let queryParams = {
        'imageId': opts['imageId'],
        'imageName': opts['imageName'],
        'modelId': opts['modelId'],
        'modelName': opts['modelName'],
        'name': opts['name'],
        'count': opts['count'],
        'computeType': opts['computeType'],
        '$skipToken': opts['skipToken'],
        'tags': opts['tags'],
        'properties': opts['properties'],
        'expand': opts['expand'],
        'orderby': opts['orderby']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PaginatedServiceList;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesListServiceKeys operation.
     * @callback module:api/ServiceApi~servicesListServiceKeysCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthKeys} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists Service keys.
     * Gets a list of Service keys.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The Service Id.
     * @param {module:api/ServiceApi~servicesListServiceKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthKeys}
     */
    servicesListServiceKeys(subscriptionId, resourceGroup, workspace, id, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesListServiceKeys");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesListServiceKeys");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesListServiceKeys");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling servicesListServiceKeys");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = AuthKeys;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/listkeys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesPatch operation.
     * @callback module:api/ServiceApi~servicesPatchCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Patch a Service.
     * Patch a specific Service.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The Service Id.
     * @param {Array.<module:model/JsonPatchOperation>} patch The payload that is used to patch the Service.
     * @param {module:api/ServiceApi~servicesPatchCallback} callback The callback function, accepting three arguments: error, data, response
     */
    servicesPatch(subscriptionId, resourceGroup, workspace, id, patch, callback) {
      let postBody = patch;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesPatch");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesPatch");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesPatch");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling servicesPatch");
      }
      // verify the required parameter 'patch' is set
      if (patch === undefined || patch === null) {
        throw new Error("Missing the required parameter 'patch' when calling servicesPatch");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json-patch+json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesQueryById operation.
     * @callback module:api/ServiceApi~servicesQueryByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ServiceResponseBase} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a Service.
     * Get a Service by Id.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The Service Id.
     * @param {Object} opts Optional parameters
     * @param {Boolean} [expand = false)] Set to True to include Model details.
     * @param {module:api/ServiceApi~servicesQueryByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ServiceResponseBase}
     */
    servicesQueryById(subscriptionId, resourceGroup, workspace, id, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesQueryById");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesQueryById");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesQueryById");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling servicesQueryById");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
        'expand': opts['expand']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ServiceResponseBase;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the servicesRegenerateServiceKeys operation.
     * @callback module:api/ServiceApi~servicesRegenerateServiceKeysCallback
     * @param {String} error Error message, if any.
     * @param {module:model/AuthKeys} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Regenerate Service Keys.
     * Regenerate and return the Service keys.
     * @param {String} subscriptionId The Azure Subscription ID.
     * @param {String} resourceGroup The Name of the resource group in which the workspace is located.
     * @param {String} workspace The name of the workspace.
     * @param {String} id The Service Id.
     * @param {module:model/RegenerateServiceKeysRequest} request The payload that is used to regenerate keys.
     * @param {module:api/ServiceApi~servicesRegenerateServiceKeysCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AuthKeys}
     */
    servicesRegenerateServiceKeys(subscriptionId, resourceGroup, workspace, id, request, callback) {
      let postBody = request;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling servicesRegenerateServiceKeys");
      }
      // verify the required parameter 'resourceGroup' is set
      if (resourceGroup === undefined || resourceGroup === null) {
        throw new Error("Missing the required parameter 'resourceGroup' when calling servicesRegenerateServiceKeys");
      }
      // verify the required parameter 'workspace' is set
      if (workspace === undefined || workspace === null) {
        throw new Error("Missing the required parameter 'workspace' when calling servicesRegenerateServiceKeys");
      }
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling servicesRegenerateServiceKeys");
      }
      // verify the required parameter 'request' is set
      if (request === undefined || request === null) {
        throw new Error("Missing the required parameter 'request' when calling servicesRegenerateServiceKeys");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroup': resourceGroup,
        'workspace': workspace,
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = AuthKeys;
      return this.apiClient.callApi(
        '/modelmanagement/v1.0/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.MachineLearningServices/workspaces/{workspace}/services/{id}/regenerateKeys', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
