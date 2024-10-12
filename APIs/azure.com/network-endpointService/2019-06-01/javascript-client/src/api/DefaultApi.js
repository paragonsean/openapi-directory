/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import EndpointServicesListResult from '../model/EndpointServicesListResult';

/**
* Default service.
* @module api/DefaultApi
* @version 2019-06-01
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the availableEndpointServicesList operation.
     * @callback module:api/DefaultApi~availableEndpointServicesListCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EndpointServicesListResult} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List what values of endpoint services are available for use.
     * @param {String} location The location to check available endpoint services.
     * @param {String} apiVersion Client API version.
     * @param {String} subscriptionId The subscription credentials which uniquely identify the Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/DefaultApi~availableEndpointServicesListCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EndpointServicesListResult}
     */
    availableEndpointServicesList(location, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'location' is set
      if (location === undefined || location === null) {
        throw new Error("Missing the required parameter 'location' when calling availableEndpointServicesList");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling availableEndpointServicesList");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling availableEndpointServicesList");
      }

      let pathParams = {
        'location': location,
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
      let returnType = EndpointServicesListResult;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/providers/Microsoft.Network/locations/{location}/virtualNetworkAvailableEndpointServices', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
