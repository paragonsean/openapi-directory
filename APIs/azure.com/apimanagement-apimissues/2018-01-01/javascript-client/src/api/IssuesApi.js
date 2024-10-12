/**
 * ApiManagementClient
 * Use this REST API to get all the issues across an Azure Api Management service.
 *
 * The version of the OpenAPI document: 2018-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import IssueListByService200Response from '../model/IssueListByService200Response';
import IssueListByServiceDefaultResponse from '../model/IssueListByServiceDefaultResponse';

/**
* Issues service.
* @module api/IssuesApi
* @version 2018-01-01
*/
export default class IssuesApi {

    /**
    * Constructs a new IssuesApi. 
    * @alias module:api/IssuesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the issueListByService operation.
     * @callback module:api/IssuesApi~issueListByServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IssueListByService200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists a collection of issues in the specified service instance.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {Object} opts Optional parameters
     * @param {String} [filter] | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | state        | eq                     |                                   | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith |
     * @param {Number} [top] Number of records to return.
     * @param {Number} [skip] Number of records to skip.
     * @param {module:api/IssuesApi~issueListByServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IssueListByService200Response}
     */
    issueListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling issueListByService");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling issueListByService");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling issueListByService");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling issueListByService");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        '$filter': opts['filter'],
        '$top': opts['top'],
        '$skip': opts['skip'],
        'api-version': apiVersion
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = IssueListByService200Response;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/issues', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
