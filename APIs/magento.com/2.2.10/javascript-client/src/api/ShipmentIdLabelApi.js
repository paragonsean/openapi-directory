/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';

/**
* ShipmentIdLabel service.
* @module api/ShipmentIdLabelApi
* @version 2.2.10
*/
export default class ShipmentIdLabelApi {

    /**
    * Constructs a new ShipmentIdLabelApi. 
    * @alias module:api/ShipmentIdLabelApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the salesShipmentManagementV1GetLabelGet operation.
     * @callback module:api/ShipmentIdLabelApi~salesShipmentManagementV1GetLabelGetCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * shipment/{id}/label
     * Gets a specified shipment label.
     * @param {Number} id The shipment label ID.
     * @param {module:api/ShipmentIdLabelApi~salesShipmentManagementV1GetLabelGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    salesShipmentManagementV1GetLabelGet(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling salesShipmentManagementV1GetLabelGet");
      }

      let pathParams = {
        'id': id
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/V1/shipment/{id}/label', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
