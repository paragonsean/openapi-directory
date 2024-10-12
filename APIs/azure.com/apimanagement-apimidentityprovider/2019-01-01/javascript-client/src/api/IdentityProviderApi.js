/**
 * ApiManagementClient
 * Use these REST APIs for performing operations on Identity Provider entity associated with your Azure API Management deployment. Setting up an external Identity Provider for authentication can help you manage the developer portal logins using the OAuth2 flow.
 *
 * The version of the OpenAPI document: 2019-01-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import IdentityProviderGet200Response from '../model/IdentityProviderGet200Response';
import IdentityProviderListByService200Response from '../model/IdentityProviderListByService200Response';
import IdentityProviderListByServiceDefaultResponse from '../model/IdentityProviderListByServiceDefaultResponse';
import IdentityProviderUpdateRequest from '../model/IdentityProviderUpdateRequest';

/**
* IdentityProvider service.
* @module api/IdentityProviderApi
* @version 2019-01-01
*/
export default class IdentityProviderApi {

    /**
    * Constructs a new IdentityProviderApi. 
    * @alias module:api/IdentityProviderApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the identityProviderCreateOrUpdate operation.
     * @callback module:api/IdentityProviderApi~identityProviderCreateOrUpdateCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IdentityProviderGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Creates or Updates the IdentityProvider configuration.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} identityProviderName Identity Provider Type identifier.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:model/IdentityProviderGet200Response} parameters Create parameters.
     * @param {Object} opts Optional parameters
     * @param {String} [ifMatch] ETag of the Entity. Not required when creating an entity, but required when updating an entity.
     * @param {module:api/IdentityProviderApi~identityProviderCreateOrUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IdentityProviderGet200Response}
     */
    identityProviderCreateOrUpdate(resourceGroupName, serviceName, identityProviderName, apiVersion, subscriptionId, parameters, opts, callback) {
      opts = opts || {};
      let postBody = parameters;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling identityProviderCreateOrUpdate");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling identityProviderCreateOrUpdate");
      }
      // verify the required parameter 'identityProviderName' is set
      if (identityProviderName === undefined || identityProviderName === null) {
        throw new Error("Missing the required parameter 'identityProviderName' when calling identityProviderCreateOrUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling identityProviderCreateOrUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling identityProviderCreateOrUpdate");
      }
      // verify the required parameter 'parameters' is set
      if (parameters === undefined || parameters === null) {
        throw new Error("Missing the required parameter 'parameters' when calling identityProviderCreateOrUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'identityProviderName': identityProviderName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
        'If-Match': opts['ifMatch']
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = IdentityProviderGet200Response;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the identityProviderDelete operation.
     * @callback module:api/IdentityProviderApi~identityProviderDeleteCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Deletes the specified identity provider configuration.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} identityProviderName Identity Provider Type identifier.
     * @param {String} ifMatch ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/IdentityProviderApi~identityProviderDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     */
    identityProviderDelete(resourceGroupName, serviceName, identityProviderName, ifMatch, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling identityProviderDelete");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling identityProviderDelete");
      }
      // verify the required parameter 'identityProviderName' is set
      if (identityProviderName === undefined || identityProviderName === null) {
        throw new Error("Missing the required parameter 'identityProviderName' when calling identityProviderDelete");
      }
      // verify the required parameter 'ifMatch' is set
      if (ifMatch === undefined || ifMatch === null) {
        throw new Error("Missing the required parameter 'ifMatch' when calling identityProviderDelete");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling identityProviderDelete");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling identityProviderDelete");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'identityProviderName': identityProviderName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
        'If-Match': ifMatch
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the identityProviderGet operation.
     * @callback module:api/IdentityProviderApi~identityProviderGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IdentityProviderGet200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the configuration details of the identity Provider configured in specified service instance.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} identityProviderName Identity Provider Type identifier.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/IdentityProviderApi~identityProviderGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IdentityProviderGet200Response}
     */
    identityProviderGet(resourceGroupName, serviceName, identityProviderName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling identityProviderGet");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling identityProviderGet");
      }
      // verify the required parameter 'identityProviderName' is set
      if (identityProviderName === undefined || identityProviderName === null) {
        throw new Error("Missing the required parameter 'identityProviderName' when calling identityProviderGet");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling identityProviderGet");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling identityProviderGet");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'identityProviderName': identityProviderName,
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
      let returnType = IdentityProviderGet200Response;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the identityProviderGetEntityTag operation.
     * @callback module:api/IdentityProviderApi~identityProviderGetEntityTagCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets the entity state (Etag) version of the identityProvider specified by its identifier.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} identityProviderName Identity Provider Type identifier.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/IdentityProviderApi~identityProviderGetEntityTagCallback} callback The callback function, accepting three arguments: error, data, response
     */
    identityProviderGetEntityTag(resourceGroupName, serviceName, identityProviderName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling identityProviderGetEntityTag");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling identityProviderGetEntityTag");
      }
      // verify the required parameter 'identityProviderName' is set
      if (identityProviderName === undefined || identityProviderName === null) {
        throw new Error("Missing the required parameter 'identityProviderName' when calling identityProviderGetEntityTag");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling identityProviderGetEntityTag");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling identityProviderGetEntityTag");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'identityProviderName': identityProviderName,
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
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}', 'HEAD',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the identityProviderListByService operation.
     * @callback module:api/IdentityProviderApi~identityProviderListByServiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/IdentityProviderListByService200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Lists a collection of Identity Provider configured in the specified service instance.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:api/IdentityProviderApi~identityProviderListByServiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/IdentityProviderListByService200Response}
     */
    identityProviderListByService(resourceGroupName, serviceName, apiVersion, subscriptionId, callback) {
      let postBody = null;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling identityProviderListByService");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling identityProviderListByService");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling identityProviderListByService");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling identityProviderListByService");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
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
      let returnType = IdentityProviderListByService200Response;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the identityProviderUpdate operation.
     * @callback module:api/IdentityProviderApi~identityProviderUpdateCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Updates an existing IdentityProvider configuration.
     * @param {String} resourceGroupName The name of the resource group.
     * @param {String} serviceName The name of the API Management service.
     * @param {module:model/String} identityProviderName Identity Provider Type identifier.
     * @param {String} ifMatch ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
     * @param {String} apiVersion Version of the API to be used with the client request.
     * @param {String} subscriptionId Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
     * @param {module:model/IdentityProviderUpdateRequest} parameters Update parameters.
     * @param {module:api/IdentityProviderApi~identityProviderUpdateCallback} callback The callback function, accepting three arguments: error, data, response
     */
    identityProviderUpdate(resourceGroupName, serviceName, identityProviderName, ifMatch, apiVersion, subscriptionId, parameters, callback) {
      let postBody = parameters;
      // verify the required parameter 'resourceGroupName' is set
      if (resourceGroupName === undefined || resourceGroupName === null) {
        throw new Error("Missing the required parameter 'resourceGroupName' when calling identityProviderUpdate");
      }
      // verify the required parameter 'serviceName' is set
      if (serviceName === undefined || serviceName === null) {
        throw new Error("Missing the required parameter 'serviceName' when calling identityProviderUpdate");
      }
      // verify the required parameter 'identityProviderName' is set
      if (identityProviderName === undefined || identityProviderName === null) {
        throw new Error("Missing the required parameter 'identityProviderName' when calling identityProviderUpdate");
      }
      // verify the required parameter 'ifMatch' is set
      if (ifMatch === undefined || ifMatch === null) {
        throw new Error("Missing the required parameter 'ifMatch' when calling identityProviderUpdate");
      }
      // verify the required parameter 'apiVersion' is set
      if (apiVersion === undefined || apiVersion === null) {
        throw new Error("Missing the required parameter 'apiVersion' when calling identityProviderUpdate");
      }
      // verify the required parameter 'subscriptionId' is set
      if (subscriptionId === undefined || subscriptionId === null) {
        throw new Error("Missing the required parameter 'subscriptionId' when calling identityProviderUpdate");
      }
      // verify the required parameter 'parameters' is set
      if (parameters === undefined || parameters === null) {
        throw new Error("Missing the required parameter 'parameters' when calling identityProviderUpdate");
      }

      let pathParams = {
        'resourceGroupName': resourceGroupName,
        'serviceName': serviceName,
        'identityProviderName': identityProviderName,
        'subscriptionId': subscriptionId
      };
      let queryParams = {
        'api-version': apiVersion
      };
      let headerParams = {
        'If-Match': ifMatch
      };
      let formParams = {
      };

      let authNames = ['azure_auth'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ApiManagement/service/{serviceName}/identityProviders/{identityProviderName}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
