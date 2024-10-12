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
import TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest from '../model/TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest';

/**
* TemandoRmaRmaIdShipments service.
* @module api/TemandoRmaRmaIdShipmentsApi
* @version 2.2.10
*/
export default class TemandoRmaRmaIdShipmentsApi {

    /**
    * Constructs a new TemandoRmaRmaIdShipmentsApi. 
    * @alias module:api/TemandoRmaRmaIdShipmentsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut operation.
     * @callback module:api/TemandoRmaRmaIdShipmentsApi~temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutCallback
     * @param {String} error Error message, if any.
     * @param {Number} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * temando/rma/{rmaId}/shipments
     * Assign platform shipment IDs to a core RMA entity.
     * @param {Number} rmaId 
     * @param {Object} opts Optional parameters
     * @param {module:model/TemandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest} [temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest] 
     * @param {module:api/TemandoRmaRmaIdShipmentsApi~temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Number}
     */
    temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut(rmaId, opts, callback) {
      opts = opts || {};
      let postBody = opts['temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPutRequest'];
      // verify the required parameter 'rmaId' is set
      if (rmaId === undefined || rmaId === null) {
        throw new Error("Missing the required parameter 'rmaId' when calling temandoShippingRmaRmaShipmentManagementV1AssignShipmentIdsPut");
      }

      let pathParams = {
        'rmaId': rmaId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json', 'application/xml'];
      let accepts = ['application/json', 'application/xml'];
      let returnType = 'Number';
      return this.apiClient.callApi(
        '/V1/temando/rma/{rmaId}/shipments', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
