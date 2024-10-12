/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ExpressRouteGateway from '../model/ExpressRouteGateway';
import ExpressRouteGatewayList from '../model/ExpressRouteGatewayList';

/**
* ExpressRouteGateways service.
* @module api/ExpressRouteGatewaysApi
* @version 2019-02-01
*/
export default class ExpressRouteGatewaysApi {

    /**
    * Constructs a new ExpressRouteGatewaysApi. 
    * @alias module:api/ExpressRouteGatewaysApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the expressRouteGatewaysCreateOrUpdate operation.
     * @callback module:api/ExpressRouteGatewaysApi~expressRouteGatewaysCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteGateway} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates or updates a ExpressRoute gateway in a specified resource group.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:model/ExpressRouteGateway} putExpressRouteGatewayParameters Parameters required in an ExpressRoute gateway PUT operation.
     * @param {module:api/ExpressRouteGatewaysApi~expressRouteGatewaysCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteGateway}
     */
    expressRouteGatewaysCreateOrUpdate(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId, putExpressRouteGatewayParameters, callback) {
      let postBody = putExpressRouteGatewayParameters;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteGatewaysCreateOrUpdate");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteGatewaysCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteGatewaysCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteGatewaysCreateOrUpdate");
      }
      // verify the required parameter 'putExpressRouteGatewayParameters' is set
      if (putExpressRouteGatewayParameters === undefined || putExpressRouteGatewayParameters === null) {
        throw new Error("Missing the required parameter 'putExpressRouteGatewayParameters' when calling expressRouteGatewaysCreateOrUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
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
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = ExpressRouteGateway;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteGatewaysDelete operation.
     * @callback module:api/ExpressRouteGatewaysApi~expressRouteGatewaysDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteGatewaysApi~expressRouteGatewaysDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    expressRouteGatewaysDelete(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteGatewaysDelete");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteGatewaysDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteGatewaysDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteGatewaysDelete");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
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
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteGatewaysGet operation.
     * @callback module:api/ExpressRouteGatewaysApi~expressRouteGatewaysGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteGateway} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Fetches the details of a ExpressRoute gateway in a resource group.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} expressRouteGatewayName The name of the ExpressRoute gateway.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteGatewaysApi~expressRouteGatewaysGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteGateway}
     */
    expressRouteGatewaysGet(resourceGroupName, expressRouteGatewayName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteGatewaysGet");
      }
      // verify the required parameter 'expressRouteGatewayName' is set
      if (expressRouteGatewayName === undefined || expressRouteGatewayName === null) {
        throw new Error("Missing the required parameter 'expressRouteGatewayName' when calling expressRouteGatewaysGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteGatewaysGet");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteGatewaysGet");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'expressRouteGatewayName': expressRouteGatewayName,
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
      let returnType = ExpressRouteGateway;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways/{expressRouteGatewayName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteGatewaysListByResourceGroup operation.
     * @callback module:api/ExpressRouteGatewaysApi~expressRouteGatewaysListByResourceGroupCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteGatewayList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists ExpressRoute gateways in a given resource group.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteGatewaysApi~expressRouteGatewaysListByResourceGroupCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteGatewayList}
     */
    expressRouteGatewaysListByResourceGroup(resourceGroupName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling expressRouteGatewaysListByResourceGroup");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteGatewaysListByResourceGroup");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteGatewaysListByResourceGroup");
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
      let returnType = ExpressRouteGatewayList;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/expressRouteGateways', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the expressRouteGatewaysListBySubscription operation.
     * @callback module:api/ExpressRouteGatewaysApi~expressRouteGatewaysListBySubscriptionCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExpressRouteGatewayList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists ExpressRoute gateways under a given subscription.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/ExpressRouteGatewaysApi~expressRouteGatewaysListBySubscriptionCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExpressRouteGatewayList}
     */
    expressRouteGatewaysListBySubscription(apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling expressRouteGatewaysListBySubscription");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling expressRouteGatewaysListBySubscription");
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
      let returnType = ExpressRouteGatewayList;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/providers/Microsoft.Network/expressRouteGateways', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
