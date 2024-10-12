/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import Cache from '../model/Cache';
import CachesListResult from '../model/CachesListResult';
import CloudError from '../model/CloudError';

/**
* Caches service.
* @module api/CachesApi
* @version 2019-11-01
*/
export default class CachesApi {

    /**
    * Constructs a new CachesApi. 
    * @alias module:api/CachesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the cachesCreateOrUpdate operation.
     * @callback module:api/CachesApi~cachesCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Cache} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create or update a Cache.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} cacheName Name of Cache.
     * @param {Object} opts Optional parameters
     * @param {module:model/Cache} [cache] Object containing the user-selectable properties of the new Cache. If read-only properties are included, they must match the existing values of those properties.
     * @param {module:api/CachesApi~cachesCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Cache}
     */
    cachesCreateOrUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, opts, callback) {
      opts = opts || {};
      let postBody = opts['cache'];
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesCreateOrUpdate");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesCreateOrUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId,
        'cacheName': cacheName
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
      let returnType = Cache;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesDelete operation.
     * @callback module:api/CachesApi~cachesDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Schedules a Cache for deletion.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} cacheName Name of Cache.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/CachesApi~cachesDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cachesDelete(resourceGroupName, cacheName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesDelete");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesDelete");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'cacheName': cacheName,
        'subscriptionId': subscriptionId
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesFlush operation.
     * @callback module:api/CachesApi~cachesFlushCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Tells a Cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} cacheName Name of Cache.
     * @param {module:api/CachesApi~cachesFlushCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cachesFlush(resourceGroupName, apiVersion, subscriptionId, cacheName, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesFlush");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesFlush");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesFlush");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesFlush");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId,
        'cacheName': cacheName
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/flush', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesGet operation.
     * @callback module:api/CachesApi~cachesGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Cache} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns a Cache.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} cacheName Name of Cache.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/CachesApi~cachesGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Cache}
     */
    cachesGet(resourceGroupName, cacheName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesGet");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesGet");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesGet");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'cacheName': cacheName,
        'subscriptionId': subscriptionId
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
      let returnType = Cache;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesList operation.
     * @callback module:api/CachesApi~cachesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CachesListResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns all Caches the user has access to under a subscription.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/CachesApi~cachesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CachesListResult}
     */
    cachesList(apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesList");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesList");
      }

      let pathParams = {
        'subscriptionId': subscriptionId
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
      let returnType = CachesListResult;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/caches', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesListByResourceGroup operation.
     * @callback module:api/CachesApi~cachesListByResourceGroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CachesListResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Returns all Caches the user has access to under a resource group.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/CachesApi~cachesListByResourceGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CachesListResult}
     */
    cachesListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesListByResourceGroup");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesListByResourceGroup");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesListByResourceGroup");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId
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
      let returnType = CachesListResult;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesStart operation.
     * @callback module:api/CachesApi~cachesStartCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Tells a Stopped state Cache to transition to Active state.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} cacheName Name of Cache.
     * @param {module:api/CachesApi~cachesStartCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cachesStart(resourceGroupName, apiVersion, subscriptionId, cacheName, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesStart");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesStart");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesStart");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesStart");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId,
        'cacheName': cacheName
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/start', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesStop operation.
     * @callback module:api/CachesApi~cachesStopCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Tells an Active Cache to transition to Stopped state.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} cacheName Name of Cache.
     * @param {module:api/CachesApi~cachesStopCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cachesStop(resourceGroupName, apiVersion, subscriptionId, cacheName, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesStop");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesStop");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesStop");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesStop");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId,
        'cacheName': cacheName
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/stop', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesUpdate operation.
     * @callback module:api/CachesApi~cachesUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Cache} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a Cache instance.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} cacheName Name of Cache.
     * @param {Object} opts Optional parameters
     * @param {module:model/Cache} [cache] Object containing the user-selectable properties of the Cache. If read-only properties are included, they must match the existing values of those properties.
     * @param {module:api/CachesApi~cachesUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Cache}
     */
    cachesUpdate(resourceGroupName, apiVersion, subscriptionId, cacheName, opts, callback) {
      opts = opts || {};
      let postBody = opts['cache'];
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesUpdate");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId,
        'cacheName': cacheName
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
      let returnType = Cache;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the cachesUpgradeFirmware operation.
     * @callback module:api/CachesApi~cachesUpgradeFirmwareCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upgrade a Cache's firmware if a new version is available. Otherwise, this operation has no effect.
     * @param {String} resourceGroupName Target resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {String} cacheName Name of Cache.
     * @param {module:api/CachesApi~cachesUpgradeFirmwareCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    cachesUpgradeFirmware(resourceGroupName, apiVersion, subscriptionId, cacheName, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling cachesUpgradeFirmware");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling cachesUpgradeFirmware");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling cachesUpgradeFirmware");
      }
      // verify the required parameter 'cacheName' is set
      if (cacheName === undefined || cacheName === null) {
        throw new Error("Missing the required parameter 'cacheName' when calling cachesUpgradeFirmware");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'subscriptionId': subscriptionId,
        'cacheName': cacheName
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourcegroups/{resourceGroupName}/providers/Microsoft.StorageCache/caches/{cacheName}/upgrade', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
