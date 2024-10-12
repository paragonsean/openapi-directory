/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CloudError from '../model/CloudError';
import EnvironmentSetting from '../model/EnvironmentSetting';
import EnvironmentSettingFragment from '../model/EnvironmentSettingFragment';
import PublishPayload from '../model/PublishPayload';
import ResponseWithContinuationEnvironmentSetting from '../model/ResponseWithContinuationEnvironmentSetting';

/**
* EnvironmentSettings service.
* @module api/EnvironmentSettingsApi
* @version 2018-10-15
*/
export default class EnvironmentSettingsApi {

    /**
    * Constructs a new EnvironmentSettingsApi. 
    * @alias module:api/EnvironmentSettingsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the environmentSettingsClaimAny operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsClaimAnyCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Claims a random environment for a user in an environment settings
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsClaimAnyCallback} callback The callback function, accepting three arguments: error, data, response
     */
    environmentSettingsClaimAny(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsClaimAny");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsClaimAny");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsClaimAny");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsClaimAny");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsClaimAny");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsClaimAny");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/claimAny', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsCreateOrUpdate operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EnvironmentSetting} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or replace an existing Environment Setting. This operation can take a while to complete
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:model/EnvironmentSetting} environmentSetting Represents settings of an environment, from which environment instances would be created
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EnvironmentSetting}
     */
    environmentSettingsCreateOrUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting, callback) {
      let postBody = environmentSetting;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsCreateOrUpdate");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsCreateOrUpdate");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsCreateOrUpdate");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsCreateOrUpdate");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsCreateOrUpdate");
      }
      // verify the required parameter 'environmentSetting' is set
      if (environmentSetting === undefined || environmentSetting === null) {
        throw new Error("Missing the required parameter 'environmentSetting' when calling environmentSettingsCreateOrUpdate");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EnvironmentSetting;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsDelete operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete environment setting. This operation can take a while to complete
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    environmentSettingsDelete(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsDelete");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsDelete");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsDelete");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsDelete");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsDelete");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsGet operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EnvironmentSetting} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get environment setting
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {Object} opts Optional parameters
     * @param {String} [expand] Specify the $expand query. Example: 'properties($select=publishingState)'
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EnvironmentSetting}
     */
    environmentSettingsGet(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsGet");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsGet");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsGet");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsGet");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsGet");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        '$expand': opts['expand'],
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = EnvironmentSetting;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsList operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ResponseWithContinuationEnvironmentSetting} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List environment setting in a given lab.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} apiVersion Client API version.
     * @param {Object} opts Optional parameters
     * @param {String} [expand] Specify the $expand query. Example: 'properties($select=publishingState)'
     * @param {String} [filter] The filter to apply to the operation.
     * @param {Number} [top] The maximum number of resources to return from the operation.
     * @param {String} [orderby] The ordering expression for the results, using OData notation.
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ResponseWithContinuationEnvironmentSetting}
     */
    environmentSettingsList(subscriptionId, resourceGroupName, labAccountName, labName, apiVersion, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsList");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsList");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsList");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsList");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsList");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName
      };
      let queryParams = {
        '$expand': opts['expand'],
        '$filter': opts['filter'],
        '$top': opts['top'],
        '$orderby': opts['orderby'],
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ResponseWithContinuationEnvironmentSetting;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsPublish operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsPublishCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Provisions/deprovisions required resources for an environment setting based on current state of the lab/environment setting.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:model/PublishPayload} publishPayload Payload for Publish operation on EnvironmentSetting.
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsPublishCallback} callback The callback function, accepting three arguments: error, data, response
     */
    environmentSettingsPublish(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, publishPayload, callback) {
      let postBody = publishPayload;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsPublish");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsPublish");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsPublish");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsPublish");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsPublish");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsPublish");
      }
      // verify the required parameter 'publishPayload' is set
      if (publishPayload === undefined || publishPayload === null) {
        throw new Error("Missing the required parameter 'publishPayload' when calling environmentSettingsPublish");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/publish', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsStart operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsStartCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Starts a template by starting all resources inside the template. This operation can take a while to complete
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsStartCallback} callback The callback function, accepting three arguments: error, data, response
     */
    environmentSettingsStart(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsStart");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsStart");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsStart");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsStart");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsStart");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsStart");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/start', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsStop operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsStopCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Starts a template by starting all resources inside the template. This operation can take a while to complete
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsStopCallback} callback The callback function, accepting three arguments: error, data, response
     */
    environmentSettingsStop(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, callback) {
      let postBody = null;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsStop");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsStop");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsStop");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsStop");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsStop");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsStop");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
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
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}/stop', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the environmentSettingsUpdate operation.
     * @callback module:api/EnvironmentSettingsApi~environmentSettingsUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EnvironmentSetting} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Modify properties of environment setting.
     * @param {String} subscriptionId The subscription ID.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} labAccountName The name of the lab Account.
     * @param {String} labName The name of the lab.
     * @param {String} environmentSettingName The name of the environment Setting.
     * @param {String} apiVersion Client API version.
     * @param {module:model/EnvironmentSettingFragment} environmentSetting Represents settings of an environment, from which environment instances would be created
     * @param {module:api/EnvironmentSettingsApi~environmentSettingsUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EnvironmentSetting}
     */
    environmentSettingsUpdate(subscriptionId, resourceGroupName, labAccountName, labName, environmentSettingName, apiVersion, environmentSetting, callback) {
      let postBody = environmentSetting;
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling environmentSettingsUpdate");
      }
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling environmentSettingsUpdate");
      }
      // verify the required parameter 'labAccountName' is set
      if (labAccountName === undefined || labAccountName === null) {
        throw new Error("Missing the required parameter 'labAccountName' when calling environmentSettingsUpdate");
      }
      // verify the required parameter 'labName' is set
      if (labName === undefined || labName === null) {
        throw new Error("Missing the required parameter 'labName' when calling environmentSettingsUpdate");
      }
      // verify the required parameter 'environmentSettingName' is set
      if (environmentSettingName === undefined || environmentSettingName === null) {
        throw new Error("Missing the required parameter 'environmentSettingName' when calling environmentSettingsUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling environmentSettingsUpdate");
      }
      // verify the required parameter 'environmentSetting' is set
      if (environmentSetting === undefined || environmentSetting === null) {
        throw new Error("Missing the required parameter 'environmentSetting' when calling environmentSettingsUpdate");
      }

      let pathParams = {
        'subscriptionId': subscriptionId,
        'resourceGroupName': resourceGroupName,
        'labAccountName': labAccountName,
        'labName': labName,
        'environmentSettingName': environmentSettingName
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EnvironmentSetting;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.LabServices/labaccounts/{labAccountName}/labs/{labName}/environmentsettings/{environmentSettingName}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
