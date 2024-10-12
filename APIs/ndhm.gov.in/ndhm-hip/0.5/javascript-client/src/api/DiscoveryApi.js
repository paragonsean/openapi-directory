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
import ErrorResponse from '../model/ErrorResponse';
import PatientDiscoveryRequest from '../model/PatientDiscoveryRequest';

/**
* Discovery service.
* @module api/DiscoveryApi
* @version 0.5
*/
export default class DiscoveryApi {

    /**
    * Constructs a new DiscoveryApi. 
    * @alias module:api/DiscoveryApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v05CareContextsDiscoverPost operation.
     * @callback module:api/DiscoveryApi~v05CareContextsDiscoverPostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Discover patient's accounts
     * Request for patient care context discover, made by Gateway intended for a specific HIP. It is expected that HIP will subsequently return either zero or one patient record with (potentially masked) associated care contexts   1. **At least one of the verified identifier matches**   2. **Name (fuzzy), gender matches**   3. **If YoB was given, age band(+-2) matches**   4. **If unverified identifiers were given, one of them matches**   5. **If more than one patient records would be found after aforementioned steps, then patient who matches most verified and unverified identifiers would be returned.**   6. **If there would be still more than one patients (after ranking) error would be returned**   7. **Intended HIP should be able to resolve and identify results returned in the subsequent link confirmation request via the specified transactionId**   8. **Intended HIP should store the discovery results with transactionId and care contexts discovered for subsequent link initiation** 
     * @param {String} authorization Access token which was issued after successful login with gateway auth server, which will be sent by gateway to authenticate itself with API bridge.
     * @param {String} X_HIP_ID Identifier of the health information provider to which the request was intended.
     * @param {module:model/PatientDiscoveryRequest} patientDiscoveryRequest 
     * @param {module:api/DiscoveryApi~v05CareContextsDiscoverPostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    v05CareContextsDiscoverPost(authorization, X_HIP_ID, patientDiscoveryRequest, opts, callback) {
      opts = opts || {};
      let postBody = patientDiscoveryRequest;
      // verify the required parameter 'authorization' is set
      if (authorization === undefined || authorization === null) {
        throw new Error("Missing the required parameter 'authorization' when calling v05CareContextsDiscoverPost");
      }
      // verify the required parameter 'X_HIP_ID' is set
      if (X_HIP_ID === undefined || X_HIP_ID === null) {
        throw new Error("Missing the required parameter 'X_HIP_ID' when calling v05CareContextsDiscoverPost");
      }
      // verify the required parameter 'patientDiscoveryRequest' is set
      if (patientDiscoveryRequest === undefined || patientDiscoveryRequest === null) {
        throw new Error("Missing the required parameter 'patientDiscoveryRequest' when calling v05CareContextsDiscoverPost");
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
      let basePaths = ['https://your-hrp-server.com'];
      let basePath = basePaths[0]; // by default use the first one in "servers" defined in OpenAPI
      if (typeof opts['_base_path_index'] !== 'undefined') {
        if (opts['_base_path_index']  >= basePaths.length || opts['_base_path_index'] <  0) {
          throw new Error("Invalid index " + opts['_base_path_index'] + " when selecting the host settings. Must be less than " + basePaths.length);
        }
        basePath = basePaths[opts['_base_path_index']];
      }

      return this.apiClient.callApi(
        '/v0.5/care-contexts/discover', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, basePath, callback
      );
    }


}
