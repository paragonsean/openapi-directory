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
import CloudError from '../model/CloudError';
import ResourceSkusResult from '../model/ResourceSkusResult';

/**
* SKUs service.
* @module api/SKUsApi
* @version 2019-11-01
*/
export default class SKUsApi {

    /**
    * Constructs a new SKUsApi. 
    * @alias module:api/SKUsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the skusList operation.
     * @callback module:api/SKUsApi~skusListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ResourceSkusResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get the list of StorageCache.Cache SKUs available to this subscription.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/SKUsApi~skusListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ResourceSkusResult}
     */
    skusList(apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling skusList");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling skusList");
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
      let returnType = ResourceSkusResult;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/providers/Microsoft.StorageCache/skus', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
