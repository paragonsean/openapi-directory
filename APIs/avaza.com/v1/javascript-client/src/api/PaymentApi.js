/**
 * Avaza API Documentation
 * Welcome to the autogenerated documentation & test tool for Avaza's API. <br/><br/><strong>API Security & Authentication</strong><br/>Authentication options include OAuth2 Implicit and Authorization Code flows, and Personal Access Token. All connections should be encrypted over SSL/TLS <br/><br/>You can set up and manage your api authentication credentials from within your Avaza account. (requires Administrator permissions on your Avaza account).<br/><br/> OAuth2 Authorization endpoint: https://any.avaza.com/oauth2/authorize  <br/>OAuth2 Token endpoint: https://any.avaza.com/oauth2/token<br/>Base URL for subsequent API Requests: https://api.avaza.com/ <br/><br/>Blogpost about authenticating with Avaza's API:  https://www.avaza.com/avaza-api-oauth2-authentication/ <br/>Blogpost on using Avaza's webhooks: https://www.avaza.com/avaza-api-webhook-notifications/<br/>The OAuth flow currently issues Access Tokens that last 1 day, and Refresh tokens that last 180 days<br/>The Api respects the security Roles assigned to the authenticating Avaza user and filters the data return appropriately. <br/><br><strong>Support</strong><br/>For API Support, and to request access please contact Avaza Support Team via our support chat. <br/><br/><strong>User Contributed Libraries:</strong><br/>Graciously contributed by 3rd party users like you. <br/>Note these are not tested or endorsesd by Avaza. We encourage you to review before use, and use at own risk.<br/> <ul><li> - <a target='blank' href='https://packagist.org/packages/debiprasad/oauth2-avaza'>PHP OAuth Client Package for Azava API (by Debiprasad Sahoo)</a></li></ul>
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import NewPayment from '../model/NewPayment';
import Payment from '../model/Payment';
import PaymentList from '../model/PaymentList';

/**
* Payment service.
* @module api/PaymentApi
* @version v1
*/
export default class PaymentApi {

    /**
    * Constructs a new PaymentApi. 
    * @alias module:api/PaymentApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the paymentGet operation.
     * @callback module:api/PaymentApi~paymentGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PaymentList} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets list of Payments
     * @param {Object} opts Optional parameters
     * @param {Number} [invoiceTransactionID] Filter for Payments that have at least one allocation against a given Invoice Transaction ID
     * @param {Date} [updatedAfter] Filter for Payments updated after a given date
     * @param {Number} [pageSize] Number of items per page (max 1000)
     * @param {Number} [pageNumber] Page to display. Starts from 1.
     * @param {module:api/PaymentApi~paymentGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PaymentList}
     */
    paymentGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'InvoiceTransactionID': opts['invoiceTransactionID'],
        'UpdatedAfter': opts['updatedAfter'],
        'pageSize': opts['pageSize'],
        'pageNumber': opts['pageNumber']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = PaymentList;
      return this.apiClient.callApi(
        '/api/Payment', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the paymentGetByID operation.
     * @callback module:api/PaymentApi~paymentGetByIDCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Payment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Gets Payment by Payment Transaction ID
     * @param {Number} id Invoice Transaction ID Number
     * @param {module:api/PaymentApi~paymentGetByIDCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Payment}
     */
    paymentGetByID(id, callback) {
      let postBody = null;
      // verify the required parameter 'id' is set
      if (id === undefined || id === null) {
        throw new Error("Missing the required parameter 'id' when calling paymentGetByID");
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

      let authNames = ['oauth2'];
      let contentTypes = [];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Payment;
      return this.apiClient.callApi(
        '/api/Payment/{id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the paymentPost operation.
     * @callback module:api/PaymentApi~paymentPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Payment} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Create new Payment and optionally assign payment allocations to Invoices
     * @param {module:model/NewPayment} model 
     * @param {module:api/PaymentApi~paymentPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Payment}
     */
    paymentPost(model, callback) {
      let postBody = model;
      // verify the required parameter 'model' is set
      if (model === undefined || model === null) {
        throw new Error("Missing the required parameter 'model' when calling paymentPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['oauth2'];
      let contentTypes = ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'];
      let accepts = ['application/json', 'text/json', 'application/xml', 'text/xml'];
      let returnType = Payment;
      return this.apiClient.callApi(
        '/api/Payment', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
