/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreateOrganizationEarlyAccessFeaturesOptInRequest from '../model/CreateOrganizationEarlyAccessFeaturesOptInRequest';
import UpdateOrganizationEarlyAccessFeaturesOptInRequest from '../model/UpdateOrganizationEarlyAccessFeaturesOptInRequest';

/**
* Features service.
* @module api/FeaturesApi
* @version 1.32.0
*/
export default class FeaturesApi {

    /**
    * Constructs a new FeaturesApi. 
    * @alias module:api/FeaturesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the createOrganizationEarlyAccessFeaturesOptIn_2 operation.
     * @callback module:api/FeaturesApi~createOrganizationEarlyAccessFeaturesOptIn_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create a new early access feature opt-in for an organization
     * Create a new early access feature opt-in for an organization
     * @param {String} organizationId 
     * @param {module:model/CreateOrganizationEarlyAccessFeaturesOptInRequest} createOrganizationEarlyAccessFeaturesOptInRequest 
     * @param {module:api/FeaturesApi~createOrganizationEarlyAccessFeaturesOptIn_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    createOrganizationEarlyAccessFeaturesOptIn_2(organizationId, createOrganizationEarlyAccessFeaturesOptInRequest, callback) {
      let postBody = createOrganizationEarlyAccessFeaturesOptInRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling createOrganizationEarlyAccessFeaturesOptIn_2");
      }
      // verify the required parameter 'createOrganizationEarlyAccessFeaturesOptInRequest' is set
      if (createOrganizationEarlyAccessFeaturesOptInRequest === undefined || createOrganizationEarlyAccessFeaturesOptInRequest === null) {
        throw new Error("Missing the required parameter 'createOrganizationEarlyAccessFeaturesOptInRequest' when calling createOrganizationEarlyAccessFeaturesOptIn_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/earlyAccess/features/optIns', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteOrganizationEarlyAccessFeaturesOptIn_2 operation.
     * @callback module:api/FeaturesApi~deleteOrganizationEarlyAccessFeaturesOptIn_2Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete an early access feature opt-in
     * Delete an early access feature opt-in
     * @param {String} organizationId 
     * @param {String} optInId 
     * @param {module:api/FeaturesApi~deleteOrganizationEarlyAccessFeaturesOptIn_2Callback} callback The callback function, accepting three arguments: error, data, response
     */
    deleteOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling deleteOrganizationEarlyAccessFeaturesOptIn_2");
      }
      // verify the required parameter 'optInId' is set
      if (optInId === undefined || optInId === null) {
        throw new Error("Missing the required parameter 'optInId' when calling deleteOrganizationEarlyAccessFeaturesOptIn_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'optInId': optInId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationEarlyAccessFeaturesOptIn_2 operation.
     * @callback module:api/FeaturesApi~getOrganizationEarlyAccessFeaturesOptIn_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Show an early access feature opt-in for an organization
     * Show an early access feature opt-in for an organization
     * @param {String} organizationId 
     * @param {String} optInId 
     * @param {module:api/FeaturesApi~getOrganizationEarlyAccessFeaturesOptIn_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationEarlyAccessFeaturesOptIn_2");
      }
      // verify the required parameter 'optInId' is set
      if (optInId === undefined || optInId === null) {
        throw new Error("Missing the required parameter 'optInId' when calling getOrganizationEarlyAccessFeaturesOptIn_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'optInId': optInId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationEarlyAccessFeaturesOptIns_2 operation.
     * @callback module:api/FeaturesApi~getOrganizationEarlyAccessFeaturesOptIns_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the early access feature opt-ins for an organization
     * List the early access feature opt-ins for an organization
     * @param {String} organizationId 
     * @param {module:api/FeaturesApi~getOrganizationEarlyAccessFeaturesOptIns_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationEarlyAccessFeaturesOptIns_2(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationEarlyAccessFeaturesOptIns_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/earlyAccess/features/optIns', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationEarlyAccessFeatures_2 operation.
     * @callback module:api/FeaturesApi~getOrganizationEarlyAccessFeatures_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<Object>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the available early access features for organization
     * List the available early access features for organization
     * @param {String} organizationId 
     * @param {module:api/FeaturesApi~getOrganizationEarlyAccessFeatures_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<Object>}
     */
    getOrganizationEarlyAccessFeatures_2(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationEarlyAccessFeatures_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [Object];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/earlyAccess/features', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationEarlyAccessFeaturesOptIn_2 operation.
     * @callback module:api/FeaturesApi~updateOrganizationEarlyAccessFeaturesOptIn_2Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update an early access feature opt-in for an organization
     * Update an early access feature opt-in for an organization
     * @param {String} organizationId 
     * @param {String} optInId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationEarlyAccessFeaturesOptInRequest} [updateOrganizationEarlyAccessFeaturesOptInRequest] 
     * @param {module:api/FeaturesApi~updateOrganizationEarlyAccessFeaturesOptIn_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    updateOrganizationEarlyAccessFeaturesOptIn_2(organizationId, optInId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationEarlyAccessFeaturesOptInRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationEarlyAccessFeaturesOptIn_2");
      }
      // verify the required parameter 'optInId' is set
      if (optInId === undefined || optInId === null) {
        throw new Error("Missing the required parameter 'optInId' when calling updateOrganizationEarlyAccessFeaturesOptIn_2");
      }

      let pathParams = {
        'organizationId': organizationId,
        'optInId': optInId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/earlyAccess/features/optIns/{optInId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
