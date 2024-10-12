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

import ApiClient from '../ApiClient';
import IErrorInfo from './IErrorInfo';
import ProductDetailsApiModel from './ProductDetailsApiModel';

/**
 * The ListResultProductDetailsApiModel model module.
 * @module model/ListResultProductDetailsApiModel
 * @version v1
 */
class ListResultProductDetailsApiModel {
    /**
     * Constructs a new <code>ListResultProductDetailsApiModel</code>.
     * @alias module:model/ListResultProductDetailsApiModel
     */
    constructor() { 
        
        ListResultProductDetailsApiModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListResultProductDetailsApiModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListResultProductDetailsApiModel} obj Optional instance to populate.
     * @return {module:model/ListResultProductDetailsApiModel} The populated <code>ListResultProductDetailsApiModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListResultProductDetailsApiModel();

            if (data.hasOwnProperty('Count')) {
                obj['Count'] = ApiClient.convertToType(data['Count'], 'Number');
            }
            if (data.hasOwnProperty('ErrorMessages')) {
                obj['ErrorMessages'] = ApiClient.convertToType(data['ErrorMessages'], [IErrorInfo]);
            }
            if (data.hasOwnProperty('IsFaulted')) {
                obj['IsFaulted'] = ApiClient.convertToType(data['IsFaulted'], 'Boolean');
            }
            if (data.hasOwnProperty('Result')) {
                obj['Result'] = ApiClient.convertToType(data['Result'], [ProductDetailsApiModel]);
            }
            if (data.hasOwnProperty('TotalCount')) {
                obj['TotalCount'] = ApiClient.convertToType(data['TotalCount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListResultProductDetailsApiModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListResultProductDetailsApiModel</code>.
     */
    static validateJSON(data) {
        if (data['ErrorMessages']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['ErrorMessages'])) {
                throw new Error("Expected the field `ErrorMessages` to be an array in the JSON data but got " + data['ErrorMessages']);
            }
            // validate the optional field `ErrorMessages` (array)
            for (const item of data['ErrorMessages']) {
                IErrorInfo.validateJSON(item);
            };
        }
        if (data['Result']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Result'])) {
                throw new Error("Expected the field `Result` to be an array in the JSON data but got " + data['Result']);
            }
            // validate the optional field `Result` (array)
            for (const item of data['Result']) {
                ProductDetailsApiModel.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} Count
 */
ListResultProductDetailsApiModel.prototype['Count'] = undefined;

/**
 * @member {Array.<module:model/IErrorInfo>} ErrorMessages
 */
ListResultProductDetailsApiModel.prototype['ErrorMessages'] = undefined;

/**
 * @member {Boolean} IsFaulted
 */
ListResultProductDetailsApiModel.prototype['IsFaulted'] = undefined;

/**
 * @member {Array.<module:model/ProductDetailsApiModel>} Result
 */
ListResultProductDetailsApiModel.prototype['Result'] = undefined;

/**
 * @member {Number} TotalCount
 */
ListResultProductDetailsApiModel.prototype['TotalCount'] = undefined;






export default ListResultProductDetailsApiModel;

