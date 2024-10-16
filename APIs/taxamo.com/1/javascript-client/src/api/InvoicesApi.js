/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import EmailInvoiceIn from '../model/EmailInvoiceIn';
import EmailInvoiceOut from '../model/EmailInvoiceOut';
import EmailRefundIn from '../model/EmailRefundIn';
import EmailRefundOut from '../model/EmailRefundOut';

/**
* Invoices service.
* @module api/InvoicesApi
* @version 1
*/
export default class InvoicesApi {

    /**
    * Constructs a new InvoicesApi. 
    * @alias module:api/InvoicesApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the emailInvoice operation.
     * @callback module:api/InvoicesApi~emailInvoiceCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmailInvoiceOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Email invoice
     * @param {String} key Transaction key.
     * @param {module:model/EmailInvoiceIn} input Input
     * @param {module:api/InvoicesApi~emailInvoiceCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmailInvoiceOut}
     */
    emailInvoice(key, input, callback) {
      let postBody = input;
      // verify the required parameter 'key' is set
      if (key === undefined || key === null) {
        throw new Error("Missing the required parameter 'key' when calling emailInvoice");
      }
      // verify the required parameter 'input' is set
      if (input === undefined || input === null) {
        throw new Error("Missing the required parameter 'input' when calling emailInvoice");
      }

      let pathParams = {
        'key': key
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EmailInvoiceOut;
      return this.apiClient.callApi(
        '/api/v1/transactions/{key}/invoice/send_email', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the emailRefund operation.
     * @callback module:api/InvoicesApi~emailRefundCallback
     * @param {String} error Error message, if any.
     * @param {module:model/EmailRefundOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Email credit note
     * @param {String} key Transaction key.
     * @param {String} refundNoteNumber Refund note id.
     * @param {module:model/EmailRefundIn} input Input
     * @param {module:api/InvoicesApi~emailRefundCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/EmailRefundOut}
     */
    emailRefund(key, refundNoteNumber, input, callback) {
      let postBody = input;
      // verify the required parameter 'key' is set
      if (key === undefined || key === null) {
        throw new Error("Missing the required parameter 'key' when calling emailRefund");
      }
      // verify the required parameter 'refundNoteNumber' is set
      if (refundNoteNumber === undefined || refundNoteNumber === null) {
        throw new Error("Missing the required parameter 'refundNoteNumber' when calling emailRefund");
      }
      // verify the required parameter 'input' is set
      if (input === undefined || input === null) {
        throw new Error("Missing the required parameter 'input' when calling emailRefund");
      }

      let pathParams = {
        'key': key,
        'refund_note_number': refundNoteNumber
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = EmailRefundOut;
      return this.apiClient.callApi(
        '/api/v1/transactions/{key}/invoice/refunds/{refund_note_number}/send_email', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
