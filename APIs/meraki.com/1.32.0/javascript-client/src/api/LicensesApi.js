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
import AssignOrganizationLicensesSeats200Response from '../model/AssignOrganizationLicensesSeats200Response';
import AssignOrganizationLicensesSeatsRequest from '../model/AssignOrganizationLicensesSeatsRequest';
import GetOrganizationLicenses200ResponseInner from '../model/GetOrganizationLicenses200ResponseInner';
import GetOrganizationLicensingCotermLicenses200ResponseInner from '../model/GetOrganizationLicensingCotermLicenses200ResponseInner';
import MoveOrganizationLicenses200Response from '../model/MoveOrganizationLicenses200Response';
import MoveOrganizationLicensesRequest from '../model/MoveOrganizationLicensesRequest';
import MoveOrganizationLicensesSeats200Response from '../model/MoveOrganizationLicensesSeats200Response';
import MoveOrganizationLicensesSeatsRequest from '../model/MoveOrganizationLicensesSeatsRequest';
import MoveOrganizationLicensingCotermLicenses200Response from '../model/MoveOrganizationLicensingCotermLicenses200Response';
import MoveOrganizationLicensingCotermLicensesRequest from '../model/MoveOrganizationLicensingCotermLicensesRequest';
import RenewOrganizationLicensesSeatsRequest from '../model/RenewOrganizationLicensesSeatsRequest';
import UpdateOrganizationLicenseRequest from '../model/UpdateOrganizationLicenseRequest';

/**
* Licenses service.
* @module api/LicensesApi
* @version 1.32.0
*/
export default class LicensesApi {

    /**
    * Constructs a new LicensesApi. 
    * @alias module:api/LicensesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the assignOrganizationLicensesSeats_1 operation.
     * @callback module:api/LicensesApi~assignOrganizationLicensesSeats_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/AssignOrganizationLicensesSeats200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Assign SM seats to a network
     * Assign SM seats to a network. This will increase the managed SM device limit of the network
     * @param {String} organizationId 
     * @param {module:model/AssignOrganizationLicensesSeatsRequest} assignOrganizationLicensesSeatsRequest 
     * @param {module:api/LicensesApi~assignOrganizationLicensesSeats_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AssignOrganizationLicensesSeats200Response}
     */
    assignOrganizationLicensesSeats_1(organizationId, assignOrganizationLicensesSeatsRequest, callback) {
      let postBody = assignOrganizationLicensesSeatsRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling assignOrganizationLicensesSeats_1");
      }
      // verify the required parameter 'assignOrganizationLicensesSeatsRequest' is set
      if (assignOrganizationLicensesSeatsRequest === undefined || assignOrganizationLicensesSeatsRequest === null) {
        throw new Error("Missing the required parameter 'assignOrganizationLicensesSeatsRequest' when calling assignOrganizationLicensesSeats_1");
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
      let returnType = AssignOrganizationLicensesSeats200Response;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/assignSeats', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationLicense_1 operation.
     * @callback module:api/LicensesApi~getOrganizationLicense_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetOrganizationLicenses200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Display a license
     * Display a license
     * @param {String} organizationId 
     * @param {String} licenseId 
     * @param {module:api/LicensesApi~getOrganizationLicense_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetOrganizationLicenses200ResponseInner}
     */
    getOrganizationLicense_1(organizationId, licenseId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationLicense_1");
      }
      // verify the required parameter 'licenseId' is set
      if (licenseId === undefined || licenseId === null) {
        throw new Error("Missing the required parameter 'licenseId' when calling getOrganizationLicense_1");
      }

      let pathParams = {
        'organizationId': organizationId,
        'licenseId': licenseId
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
      let returnType = GetOrganizationLicenses200ResponseInner;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/{licenseId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationLicensesOverview_1 operation.
     * @callback module:api/LicensesApi~getOrganizationLicensesOverview_1Callback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return an overview of the license state for an organization
     * Return an overview of the license state for an organization
     * @param {String} organizationId 
     * @param {module:api/LicensesApi~getOrganizationLicensesOverview_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getOrganizationLicensesOverview_1(organizationId, callback) {
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationLicensesOverview_1");
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
      let returnType = Object;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/overview', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationLicenses_1 operation.
     * @callback module:api/LicensesApi~getOrganizationLicenses_1Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationLicenses200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the licenses for an organization
     * List the licenses for an organization
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [deviceSerial] Filter the licenses to those assigned to a particular device. Returned in the same order that they are queued to the device.
     * @param {String} [networkId] Filter the licenses to those assigned in a particular network
     * @param {module:model/String} [state] Filter the licenses to those in a particular state. Can be one of 'active', 'expired', 'expiring', 'recentlyQueued', 'unused' or 'unusedActive'
     * @param {module:api/LicensesApi~getOrganizationLicenses_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationLicenses200ResponseInner>}
     */
    getOrganizationLicenses_1(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationLicenses_1");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'perPage': opts['perPage'],
        'startingAfter': opts['startingAfter'],
        'endingBefore': opts['endingBefore'],
        'deviceSerial': opts['deviceSerial'],
        'networkId': opts['networkId'],
        'state': opts['state']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationLicenses200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getOrganizationLicensingCotermLicenses_2 operation.
     * @callback module:api/LicensesApi~getOrganizationLicensingCotermLicenses_2Callback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/GetOrganizationLicensingCotermLicenses200ResponseInner>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * List the licenses in a coterm organization
     * List the licenses in a coterm organization
     * @param {String} organizationId 
     * @param {Object} opts Optional parameters
     * @param {Number} [perPage] The number of entries per page returned. Acceptable range is 3 - 1000. Default is 1000.
     * @param {String} [startingAfter] A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {String} [endingBefore] A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it.
     * @param {Boolean} [invalidated] Filter for licenses that are invalidated
     * @param {Boolean} [expired] Filter for licenses that are expired
     * @param {module:api/LicensesApi~getOrganizationLicensingCotermLicenses_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/GetOrganizationLicensingCotermLicenses200ResponseInner>}
     */
    getOrganizationLicensingCotermLicenses_2(organizationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling getOrganizationLicensingCotermLicenses_2");
      }

      let pathParams = {
        'organizationId': organizationId
      };
      let queryParams = {
        'perPage': opts['perPage'],
        'startingAfter': opts['startingAfter'],
        'endingBefore': opts['endingBefore'],
        'invalidated': opts['invalidated'],
        'expired': opts['expired']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['meraki_api_key'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [GetOrganizationLicensingCotermLicenses200ResponseInner];
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licensing/coterm/licenses', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the moveOrganizationLicensesSeats_1 operation.
     * @callback module:api/LicensesApi~moveOrganizationLicensesSeats_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/MoveOrganizationLicensesSeats200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Move SM seats to another organization
     * Move SM seats to another organization
     * @param {String} organizationId 
     * @param {module:model/MoveOrganizationLicensesSeatsRequest} moveOrganizationLicensesSeatsRequest 
     * @param {module:api/LicensesApi~moveOrganizationLicensesSeats_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MoveOrganizationLicensesSeats200Response}
     */
    moveOrganizationLicensesSeats_1(organizationId, moveOrganizationLicensesSeatsRequest, callback) {
      let postBody = moveOrganizationLicensesSeatsRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling moveOrganizationLicensesSeats_1");
      }
      // verify the required parameter 'moveOrganizationLicensesSeatsRequest' is set
      if (moveOrganizationLicensesSeatsRequest === undefined || moveOrganizationLicensesSeatsRequest === null) {
        throw new Error("Missing the required parameter 'moveOrganizationLicensesSeatsRequest' when calling moveOrganizationLicensesSeats_1");
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
      let returnType = MoveOrganizationLicensesSeats200Response;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/moveSeats', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the moveOrganizationLicenses_1 operation.
     * @callback module:api/LicensesApi~moveOrganizationLicenses_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/MoveOrganizationLicenses200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Move licenses to another organization
     * Move licenses to another organization. This will also move any devices that the licenses are assigned to
     * @param {String} organizationId 
     * @param {module:model/MoveOrganizationLicensesRequest} moveOrganizationLicensesRequest 
     * @param {module:api/LicensesApi~moveOrganizationLicenses_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MoveOrganizationLicenses200Response}
     */
    moveOrganizationLicenses_1(organizationId, moveOrganizationLicensesRequest, callback) {
      let postBody = moveOrganizationLicensesRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling moveOrganizationLicenses_1");
      }
      // verify the required parameter 'moveOrganizationLicensesRequest' is set
      if (moveOrganizationLicensesRequest === undefined || moveOrganizationLicensesRequest === null) {
        throw new Error("Missing the required parameter 'moveOrganizationLicensesRequest' when calling moveOrganizationLicenses_1");
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
      let returnType = MoveOrganizationLicenses200Response;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/move', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the moveOrganizationLicensingCotermLicenses_2 operation.
     * @callback module:api/LicensesApi~moveOrganizationLicensingCotermLicenses_2Callback
     * @param {String} error Error message, if any.
     * @param {module:model/MoveOrganizationLicensingCotermLicenses200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Moves a license to a different organization (coterm only)
     * Moves a license to a different organization (coterm only)
     * @param {String} organizationId 
     * @param {module:model/MoveOrganizationLicensingCotermLicensesRequest} moveOrganizationLicensingCotermLicensesRequest 
     * @param {module:api/LicensesApi~moveOrganizationLicensingCotermLicenses_2Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/MoveOrganizationLicensingCotermLicenses200Response}
     */
    moveOrganizationLicensingCotermLicenses_2(organizationId, moveOrganizationLicensingCotermLicensesRequest, callback) {
      let postBody = moveOrganizationLicensingCotermLicensesRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling moveOrganizationLicensingCotermLicenses_2");
      }
      // verify the required parameter 'moveOrganizationLicensingCotermLicensesRequest' is set
      if (moveOrganizationLicensingCotermLicensesRequest === undefined || moveOrganizationLicensingCotermLicensesRequest === null) {
        throw new Error("Missing the required parameter 'moveOrganizationLicensingCotermLicensesRequest' when calling moveOrganizationLicensingCotermLicenses_2");
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
      let returnType = MoveOrganizationLicensingCotermLicenses200Response;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licensing/coterm/licenses/move', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the renewOrganizationLicensesSeats_1 operation.
     * @callback module:api/LicensesApi~renewOrganizationLicensesSeats_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/AssignOrganizationLicensesSeats200Response} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Renew SM seats of a license
     * Renew SM seats of a license. This will extend the license expiration date of managed SM devices covered by this license
     * @param {String} organizationId 
     * @param {module:model/RenewOrganizationLicensesSeatsRequest} renewOrganizationLicensesSeatsRequest 
     * @param {module:api/LicensesApi~renewOrganizationLicensesSeats_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/AssignOrganizationLicensesSeats200Response}
     */
    renewOrganizationLicensesSeats_1(organizationId, renewOrganizationLicensesSeatsRequest, callback) {
      let postBody = renewOrganizationLicensesSeatsRequest;
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling renewOrganizationLicensesSeats_1");
      }
      // verify the required parameter 'renewOrganizationLicensesSeatsRequest' is set
      if (renewOrganizationLicensesSeatsRequest === undefined || renewOrganizationLicensesSeatsRequest === null) {
        throw new Error("Missing the required parameter 'renewOrganizationLicensesSeatsRequest' when calling renewOrganizationLicensesSeats_1");
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
      let returnType = AssignOrganizationLicensesSeats200Response;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/renewSeats', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the updateOrganizationLicense_1 operation.
     * @callback module:api/LicensesApi~updateOrganizationLicense_1Callback
     * @param {String} error Error message, if any.
     * @param {module:model/GetOrganizationLicenses200ResponseInner} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Update a license
     * Update a license
     * @param {String} organizationId 
     * @param {String} licenseId 
     * @param {Object} opts Optional parameters
     * @param {module:model/UpdateOrganizationLicenseRequest} [updateOrganizationLicenseRequest] 
     * @param {module:api/LicensesApi~updateOrganizationLicense_1Callback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetOrganizationLicenses200ResponseInner}
     */
    updateOrganizationLicense_1(organizationId, licenseId, opts, callback) {
      opts = opts || {};
      let postBody = opts['updateOrganizationLicenseRequest'];
      // verify the required parameter 'organizationId' is set
      if (organizationId === undefined || organizationId === null) {
        throw new Error("Missing the required parameter 'organizationId' when calling updateOrganizationLicense_1");
      }
      // verify the required parameter 'licenseId' is set
      if (licenseId === undefined || licenseId === null) {
        throw new Error("Missing the required parameter 'licenseId' when calling updateOrganizationLicense_1");
      }

      let pathParams = {
        'organizationId': organizationId,
        'licenseId': licenseId
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
      let returnType = GetOrganizationLicenses200ResponseInner;
      return this.apiClient.callApi(
        '/organizations/{organizationId}/licenses/{licenseId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
