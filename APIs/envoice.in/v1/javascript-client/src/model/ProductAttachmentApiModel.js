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

/**
 * The ProductAttachmentApiModel model module.
 * @module model/ProductAttachmentApiModel
 * @version v1
 */
class ProductAttachmentApiModel {
    /**
     * Constructs a new <code>ProductAttachmentApiModel</code>.
     * @alias module:model/ProductAttachmentApiModel
     */
    constructor() { 
        
        ProductAttachmentApiModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProductAttachmentApiModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProductAttachmentApiModel} obj Optional instance to populate.
     * @return {module:model/ProductAttachmentApiModel} The populated <code>ProductAttachmentApiModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProductAttachmentApiModel();

            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('Link')) {
                obj['Link'] = ApiClient.convertToType(data['Link'], 'String');
            }
            if (data.hasOwnProperty('ObfuscatedFileName')) {
                obj['ObfuscatedFileName'] = ApiClient.convertToType(data['ObfuscatedFileName'], 'String');
            }
            if (data.hasOwnProperty('OriginalFileName')) {
                obj['OriginalFileName'] = ApiClient.convertToType(data['OriginalFileName'], 'String');
            }
            if (data.hasOwnProperty('Size')) {
                obj['Size'] = ApiClient.convertToType(data['Size'], 'Number');
            }
            if (data.hasOwnProperty('Type')) {
                obj['Type'] = ApiClient.convertToType(data['Type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProductAttachmentApiModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProductAttachmentApiModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Link'] && !(typeof data['Link'] === 'string' || data['Link'] instanceof String)) {
            throw new Error("Expected the field `Link` to be a primitive type in the JSON string but got " + data['Link']);
        }
        // ensure the json data is a string
        if (data['ObfuscatedFileName'] && !(typeof data['ObfuscatedFileName'] === 'string' || data['ObfuscatedFileName'] instanceof String)) {
            throw new Error("Expected the field `ObfuscatedFileName` to be a primitive type in the JSON string but got " + data['ObfuscatedFileName']);
        }
        // ensure the json data is a string
        if (data['OriginalFileName'] && !(typeof data['OriginalFileName'] === 'string' || data['OriginalFileName'] instanceof String)) {
            throw new Error("Expected the field `OriginalFileName` to be a primitive type in the JSON string but got " + data['OriginalFileName']);
        }
        // ensure the json data is a string
        if (data['Type'] && !(typeof data['Type'] === 'string' || data['Type'] instanceof String)) {
            throw new Error("Expected the field `Type` to be a primitive type in the JSON string but got " + data['Type']);
        }

        return true;
    }


}



/**
 * Product attachment id
 * @member {Number} Id
 */
ProductAttachmentApiModel.prototype['Id'] = undefined;

/**
 * Link to the file
 * @member {String} Link
 */
ProductAttachmentApiModel.prototype['Link'] = undefined;

/**
 * Hashed file name to avoid url wildguessing
 * @member {String} ObfuscatedFileName
 */
ProductAttachmentApiModel.prototype['ObfuscatedFileName'] = undefined;

/**
 * Name of the file
 * @member {String} OriginalFileName
 */
ProductAttachmentApiModel.prototype['OriginalFileName'] = undefined;

/**
 * File size number in bytes
 * @member {Number} Size
 */
ProductAttachmentApiModel.prototype['Size'] = undefined;

/**
 * Type of the link (Attached or external)
 * @member {module:model/ProductAttachmentApiModel.TypeEnum} Type
 */
ProductAttachmentApiModel.prototype['Type'] = undefined;





/**
 * Allowed values for the <code>Type</code> property.
 * @enum {String}
 * @readonly
 */
ProductAttachmentApiModel['TypeEnum'] = {

    /**
     * value: "External"
     * @const
     */
    "External": "External",

    /**
     * value: "Uploaded"
     * @const
     */
    "Uploaded": "Uploaded"
};



export default ProductAttachmentApiModel;

