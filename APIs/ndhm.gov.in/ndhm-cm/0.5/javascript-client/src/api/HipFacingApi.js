/**
 * Health Data Consent Manager
 * Entity which provides health information aggregation services to customers of health care services. It enables customers to fetch their health information from one or more Health Information Providers (e.g., Hospitals, Diagnostic Labs, Medical Device Companies), based on their explicit Consent and to share such aggregated information with Health Information Users i.e. entities in need of such data (e.g., Insurers, Doctors, Medical Researchers).  # Specifications 1. This document maintains only the Health Information Gateway relevant APIs.  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import PatientAuthModeQueryRequest from '../model/PatientAuthModeQueryRequest';
import PatientAuthNotificationAcknowledgement from '../model/PatientAuthNotificationAcknowledgement';

/**
* HipFacing service.
* @module api/HipFacingApi
* @version 0.5
*/
export default class HipFacingApi {

    /**
    * Constructs a new HipFacingApi. 
    * @alias module:api/HipFacingApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v05UsersAuthFetchModesPost_0 operation.
     * @callback module:api/HipFacingApi~v05UsersAuthFetchModesPost_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get a patient's authentication modes relevant to specified purpose
     * This API is meant for identify supported authentication modes for a patient given a specific purpose 
     * @param {String} authorization Access token which was issued after successful login with gateway auth server.
     * @param {module:model/PatientAuthModeQueryRequest} patientAuthModeQueryRequest 
     * @param {module:api/HipFacingApi~v05UsersAuthFetchModesPost_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    v05UsersAuthFetchModesPost_0(authorization, patientAuthModeQueryRequest, callback) {
      let postBody = patientAuthModeQueryRequest;
      // verify the required parameter 'authorization' is set
      if (authorization === undefined || authorization === null) {
        throw new Error("Missing the required parameter 'authorization' when calling v05UsersAuthFetchModesPost_0");
      }
      // verify the required parameter 'patientAuthModeQueryRequest' is set
      if (patientAuthModeQueryRequest === undefined || patientAuthModeQueryRequest === null) {
        throw new Error("Missing the required parameter 'patientAuthModeQueryRequest' when calling v05UsersAuthFetchModesPost_0");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Authorization': authorization
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = null;
      return this.apiClient.callApi(
        '/v0.5/users/auth/fetch-modes', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v05UsersAuthOnNotifyPost_0 operation.
     * @callback module:api/HipFacingApi~v05UsersAuthOnNotifyPost_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * callback API from HIU/HIPs as acknowledgement of auth notification (in case of DIRECT auth)
     * This API is called by HIU/HIPs to confirm acknowledgement for receipt of auth notification is case of DIRECT authentication.  
     * @param {String} authorization Access token which was issued after successful login with gateway auth server.
     * @param {module:model/PatientAuthNotificationAcknowledgement} patientAuthNotificationAcknowledgement 
     * @param {module:api/HipFacingApi~v05UsersAuthOnNotifyPost_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    v05UsersAuthOnNotifyPost_0(authorization, patientAuthNotificationAcknowledgement, callback) {
      let postBody = patientAuthNotificationAcknowledgement;
      // verify the required parameter 'authorization' is set
      if (authorization === undefined || authorization === null) {
        throw new Error("Missing the required parameter 'authorization' when calling v05UsersAuthOnNotifyPost_0");
      }
      // verify the required parameter 'patientAuthNotificationAcknowledgement' is set
      if (patientAuthNotificationAcknowledgement === undefined || patientAuthNotificationAcknowledgement === null) {
        throw new Error("Missing the required parameter 'patientAuthNotificationAcknowledgement' when calling v05UsersAuthOnNotifyPost_0");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Authorization': authorization
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = null;
      return this.apiClient.callApi(
        '/v0.5/users/auth/on-notify', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
