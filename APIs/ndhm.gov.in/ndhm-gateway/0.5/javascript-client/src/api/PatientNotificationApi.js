/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
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
import PatientSMSNotifcationRequest from '../model/PatientSMSNotifcationRequest';
import PatientSMSNotifcationResponse from '../model/PatientSMSNotifcationResponse';

/**
* PatientNotification service.
* @module api/PatientNotificationApi
* @version 0.5
*/
export default class PatientNotificationApi {

    /**
    * Constructs a new PatientNotificationApi. 
    * @alias module:api/PatientNotificationApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v05PatientsSmsNotifyPost_0 operation.
     * @callback module:api/PatientNotificationApi~v05PatientsSmsNotifyPost_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * API for HIP to send SMS notifications to patients
     * API to send SMS notifications to patient with custom deeplink. 
     * @param {String} authorization Access token which was issued after successful login with gateway auth server.
     * @param {String} X_CM_ID Suffix of the consent manager to which the request was intended.
     * @param {module:model/PatientSMSNotifcationRequest} patientSMSNotifcationRequest 
     * @param {module:api/PatientNotificationApi~v05PatientsSmsNotifyPost_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    v05PatientsSmsNotifyPost_0(authorization, X_CM_ID, patientSMSNotifcationRequest, callback) {
      let postBody = patientSMSNotifcationRequest;
      // verify the required parameter 'authorization' is set
      if (authorization === undefined || authorization === null) {
        throw new Error("Missing the required parameter 'authorization' when calling v05PatientsSmsNotifyPost_0");
      }
      // verify the required parameter 'X_CM_ID' is set
      if (X_CM_ID === undefined || X_CM_ID === null) {
        throw new Error("Missing the required parameter 'X_CM_ID' when calling v05PatientsSmsNotifyPost_0");
      }
      // verify the required parameter 'patientSMSNotifcationRequest' is set
      if (patientSMSNotifcationRequest === undefined || patientSMSNotifcationRequest === null) {
        throw new Error("Missing the required parameter 'patientSMSNotifcationRequest' when calling v05PatientsSmsNotifyPost_0");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Authorization': authorization,
        'X-CM-ID': X_CM_ID
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = null;
      return this.apiClient.callApi(
        '/v0.5/patients/sms/notify', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v05PatientsSmsOnNotifyPost_0 operation.
     * @callback module:api/PatientNotificationApi~v05PatientsSmsOnNotifyPost_0Callback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Acknowledgment response for SMS notification sent to patient by HIP
     * If the SMS notification is successfully sent to patient then \"status\" will be \"ACKNOWLEDGED\" with no error. If the SMS notification is failed then \"status\" will be \"ERRORED\" with error. 
     * @param {String} authorization Access token which was issued after successful login with gateway auth server.
     * @param {String} X_HIP_ID Identifier of the health information provider to which the request was intended.
     * @param {module:model/PatientSMSNotifcationResponse} patientSMSNotifcationResponse 
     * @param {module:api/PatientNotificationApi~v05PatientsSmsOnNotifyPost_0Callback} callback The callback function, accepting three arguments: error, data, response
     */
    v05PatientsSmsOnNotifyPost_0(authorization, X_HIP_ID, patientSMSNotifcationResponse, callback) {
      let postBody = patientSMSNotifcationResponse;
      // verify the required parameter 'authorization' is set
      if (authorization === undefined || authorization === null) {
        throw new Error("Missing the required parameter 'authorization' when calling v05PatientsSmsOnNotifyPost_0");
      }
      // verify the required parameter 'X_HIP_ID' is set
      if (X_HIP_ID === undefined || X_HIP_ID === null) {
        throw new Error("Missing the required parameter 'X_HIP_ID' when calling v05PatientsSmsOnNotifyPost_0");
      }
      // verify the required parameter 'patientSMSNotifcationResponse' is set
      if (patientSMSNotifcationResponse === undefined || patientSMSNotifcationResponse === null) {
        throw new Error("Missing the required parameter 'patientSMSNotifcationResponse' when calling v05PatientsSmsOnNotifyPost_0");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'Authorization': authorization,
        'X-HIP-ID': X_HIP_ID
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = null;
      return this.apiClient.callApi(
        '/v0.5/patients/sms/on-notify', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
