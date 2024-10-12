/**
 * API v1.0.0
 * [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/80638214aa04722c9203)  <span style='margin-left: 0.5em;'>or</span>  <a href='https://documenter.getpostman.com/view/3559821/TVeqcn2L' class='openapi-button' _ngcontent-c6>View Postman docs</a>    # Quickstart    Visit [github](https://github.com/EmitKnowledge/Envoice) to view the quickstart tutorial.    <div class='postman-tutorial'>    # Tutorial for running the API in postman    Click on \"\"Run in Postman\"\" button  <br /><br />  ![postman - tutorial - 1](/Assets/images/api/postman-tutorial/postman-tutorial-1.png)     ---     A new page will open.  Click the \"\"Postman for windows\"\" to run postman as a desktop app.  Make sure you have already [installed](https://www.getpostman.com/docs/postman/launching_postman/installation_and_updates) Postman.  <br /><br />  ![postman - tutorial - 2](/Assets/images/api/postman-tutorial/postman-tutorial-2.png)     ---     In chrome an alert might show up to set a default app for opening postman links. Click on \"\"Open Postman\"\".  <br /><br />  ![postman - tutorial - 3](/Assets/images/api/postman-tutorial/postman-tutorial-3.png)     ---     The OpenAPI specification will be imported in Postman as a new collection named \"\"Envoice api\"\"  <br /><br />  ![postman - tutorial - 4](/Assets/images/api/postman-tutorial/postman-tutorial-4.png)     ---     When testing be sure to check and modify the environment variables to suit your api key and secret. The domain is set to envoice's endpoint so you don't really need to change that.    <sub>\\*Eye button in top right corner </sub>  <br /><br />   ![postman - tutorial - 5](/Assets/images/api/postman-tutorial/postman-tutorial-5.png)  <br /><br />   ![postman - tutorial - 6](/Assets/images/api/postman-tutorial/postman-tutorial-6.png)     ---     You don't need to change the values of the header parameters, because they will be replaced automatically when you send a request with real values from the environment configured in the previous step.  <br /><br />  ![postman - tutorial - 7](/Assets/images/api/postman-tutorial/postman-tutorial-7.png)     ---     Modify the example data to suit your needs and send a request.  <br /><br />  ![postman - tutorial - 8](/Assets/images/api/postman-tutorial/postman-tutorial-8.png)  </div>    # Webhooks    Webhooks allow you to build or set up Envoice Apps which subscribe to invoice activities.   When one of those events is triggered, we'll send a HTTP POST payload to the webhook's configured URL.   Webhooks can be used to update an external invoice data storage.    In order to use webhooks visit [this link](/account/settings#api-tab) and add upto 10 webhook urls that will return status `200` in order to signal that the webhook is working.  All nonworking webhooks will be ignored after a certain period of time and several retry attempts.  If after several attempts the webhook starts to work, we will send you all activities, both past and present, in chronological order.    The payload of the webhook is in format:  ```  {      Signature: \"\"sha256 string\"\",      Timestamp: \"\"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"\",      Activity: {          Message: \"string\",          Link: \"share url\",          Type: int,                  InvoiceNumber: \"string\",          InvoiceId: int,                  OrderNumber: \"string\",          OrderId: int,          Id: int,          CreatedOn: \"YYYY-MM-DDTHH:mm:ss.FFFFFFFZ\"      }  }  ```            
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
import PaymentGatewayDetailsApiModel from '../model/PaymentGatewayDetailsApiModel';

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
     * Callback function to receive the result of the paymentApiSupported operation.
     * @callback module:api/PaymentApi~paymentApiSupportedCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/PaymentGatewayDetailsApiModel>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Return all supported payment gateways (no currencies means all are supported)
     * @param {String} xAuthKey 
     * @param {String} xAuthSecret 
     * @param {module:api/PaymentApi~paymentApiSupportedCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/PaymentGatewayDetailsApiModel>}
     */
    paymentApiSupported(xAuthKey, xAuthSecret, callback) {
      let postBody = null;
      // verify the required parameter 'xAuthKey' is set
      if (xAuthKey === undefined || xAuthKey === null) {
        throw new Error("Missing the required parameter 'xAuthKey' when calling paymentApiSupported");
      }
      // verify the required parameter 'xAuthSecret' is set
      if (xAuthSecret === undefined || xAuthSecret === null) {
        throw new Error("Missing the required parameter 'xAuthSecret' when calling paymentApiSupported");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'x-auth-key': xAuthKey,
        'x-auth-secret': xAuthSecret
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json', 'application/xml', 'text/html', 'text/json', 'text/xml'];
      let returnType = [PaymentGatewayDetailsApiModel];
      return this.apiClient.callApi(
        '/api/payment/supported', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
