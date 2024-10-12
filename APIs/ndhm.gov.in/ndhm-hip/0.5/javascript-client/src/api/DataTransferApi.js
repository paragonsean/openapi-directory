/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
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
import DataNotification from '../model/DataNotification';
import ErrorResponse from '../model/ErrorResponse';

/**
* DataTransfer service.
* @module api/DataTransferApi
* @version 0.5
*/
export default class DataTransferApi {

    /**
    * Constructs a new DataTransferApi. 
    * @alias module:api/DataTransferApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v05HealthInformationTransferPost operation.
     * @callback module:api/DataTransferApi~v05HealthInformationTransferPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * health information transfer API
     * **NOTE**: This API is actually the callback URL that is passed as **dataPushUrl** in the data request API - /v0.5/health-information/hip/request. This API is directly called by HIP Data Bridge and is not mediated via CM, and hence not routed through the Gateway.    1. This API should be implemented at HIU side. It maybe implemented by the Data Bridge representing the HIU.    2. Entry elements maybe ***content*** or ***link***, although for version 1, entry ***content*** is preferred.    3. Entry ***content*** (or even link reference content) must be encrypted by means of Elliptic-curve Diffie–Hellman Key Exchange, utilizing the HIU keymaterials that are passed through the data request API - /v0.5/health-information/hip/request.    4. Media contains the mimetype of content, and for v1, it is \"application/fhir+json\"   5. checksum is Md5 checksum of the data conent, before encryption   6. Please refer to the NDHM Sandbox Documentation for the format of FHIR bundle that is passed through content  
     * @param {String} authorization Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
     * @param {module:model/DataNotification} dataNotification 
     * @param {module:api/DataTransferApi~v05HealthInformationTransferPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    v05HealthInformationTransferPost(authorization, dataNotification, opts, callback) {
      opts = opts || {};
      let postBody = dataNotification;
      // verify the required parameter 'authorization' is set
      if (authorization === undefined || authorization === null) {
        throw new Error("Missing the required parameter 'authorization' when calling v05HealthInformationTransferPost");
      }
      // verify the required parameter 'dataNotification' is set
      if (dataNotification === undefined || dataNotification === null) {
        throw new Error("Missing the required parameter 'dataNotification' when calling v05HealthInformationTransferPost");
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
      let basePaths = ['https://dev.ndhm.gov.in/patient-hiu'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/v0.5/health-information/transfer', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }


}
