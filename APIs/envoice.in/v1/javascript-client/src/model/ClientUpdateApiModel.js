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
import AdditionalClientEmailApiModel from './AdditionalClientEmailApiModel';

/**
 * The ClientUpdateApiModel model module.
 * @module model/ClientUpdateApiModel
 * @version v1
 */
class ClientUpdateApiModel {
    /**
     * Constructs a new <code>ClientUpdateApiModel</code>.
     * @alias module:model/ClientUpdateApiModel
     */
    constructor() { 
        
        ClientUpdateApiModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ClientUpdateApiModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ClientUpdateApiModel} obj Optional instance to populate.
     * @return {module:model/ClientUpdateApiModel} The populated <code>ClientUpdateApiModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ClientUpdateApiModel();

            if (data.hasOwnProperty('AdditionalEmails')) {
                obj['AdditionalEmails'] = ApiClient.convertToType(data['AdditionalEmails'], [AdditionalClientEmailApiModel]);
            }
            if (data.hasOwnProperty('Address')) {
                obj['Address'] = ApiClient.convertToType(data['Address'], 'String');
            }
            if (data.hasOwnProperty('ClientCountryId')) {
                obj['ClientCountryId'] = ApiClient.convertToType(data['ClientCountryId'], 'Number');
            }
            if (data.hasOwnProperty('ClientCurrencyId')) {
                obj['ClientCurrencyId'] = ApiClient.convertToType(data['ClientCurrencyId'], 'Number');
            }
            if (data.hasOwnProperty('CompanyRegistrationNumber')) {
                obj['CompanyRegistrationNumber'] = ApiClient.convertToType(data['CompanyRegistrationNumber'], 'String');
            }
            if (data.hasOwnProperty('DefaultDueDateInDays')) {
                obj['DefaultDueDateInDays'] = ApiClient.convertToType(data['DefaultDueDateInDays'], 'Number');
            }
            if (data.hasOwnProperty('Email')) {
                obj['Email'] = ApiClient.convertToType(data['Email'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('Name')) {
                obj['Name'] = ApiClient.convertToType(data['Name'], 'String');
            }
            if (data.hasOwnProperty('PhoneNumber')) {
                obj['PhoneNumber'] = ApiClient.convertToType(data['PhoneNumber'], 'String');
            }
            if (data.hasOwnProperty('UiLanguageId')) {
                obj['UiLanguageId'] = ApiClient.convertToType(data['UiLanguageId'], 'Number');
            }
            if (data.hasOwnProperty('Vat')) {
                obj['Vat'] = ApiClient.convertToType(data['Vat'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ClientUpdateApiModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ClientUpdateApiModel</code>.
     */
    static validateJSON(data) {
        if (data['AdditionalEmails']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['AdditionalEmails'])) {
                throw new Error("Expected the field `AdditionalEmails` to be an array in the JSON data but got " + data['AdditionalEmails']);
            }
            // validate the optional field `AdditionalEmails` (array)
            for (const item of data['AdditionalEmails']) {
                AdditionalClientEmailApiModel.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Address'] && !(typeof data['Address'] === 'string' || data['Address'] instanceof String)) {
            throw new Error("Expected the field `Address` to be a primitive type in the JSON string but got " + data['Address']);
        }
        // ensure the json data is a string
        if (data['CompanyRegistrationNumber'] && !(typeof data['CompanyRegistrationNumber'] === 'string' || data['CompanyRegistrationNumber'] instanceof String)) {
            throw new Error("Expected the field `CompanyRegistrationNumber` to be a primitive type in the JSON string but got " + data['CompanyRegistrationNumber']);
        }
        // ensure the json data is a string
        if (data['Email'] && !(typeof data['Email'] === 'string' || data['Email'] instanceof String)) {
            throw new Error("Expected the field `Email` to be a primitive type in the JSON string but got " + data['Email']);
        }
        // ensure the json data is a string
        if (data['Name'] && !(typeof data['Name'] === 'string' || data['Name'] instanceof String)) {
            throw new Error("Expected the field `Name` to be a primitive type in the JSON string but got " + data['Name']);
        }
        // ensure the json data is a string
        if (data['PhoneNumber'] && !(typeof data['PhoneNumber'] === 'string' || data['PhoneNumber'] instanceof String)) {
            throw new Error("Expected the field `PhoneNumber` to be a primitive type in the JSON string but got " + data['PhoneNumber']);
        }
        // ensure the json data is a string
        if (data['Vat'] && !(typeof data['Vat'] === 'string' || data['Vat'] instanceof String)) {
            throw new Error("Expected the field `Vat` to be a primitive type in the JSON string but got " + data['Vat']);
        }

        return true;
    }


}



/**
 * Client additional emails contact for CC
 * @member {Array.<module:model/AdditionalClientEmailApiModel>} AdditionalEmails
 */
ClientUpdateApiModel.prototype['AdditionalEmails'] = undefined;

/**
 * Client business address
 * @member {String} Address
 */
ClientUpdateApiModel.prototype['Address'] = undefined;

/**
 * Indicates the country where the clients is from
 * @member {Number} ClientCountryId
 */
ClientUpdateApiModel.prototype['ClientCountryId'] = undefined;

/**
 * Indicates the default system currency used by the user for the client
 * @member {Number} ClientCurrencyId
 */
ClientUpdateApiModel.prototype['ClientCurrencyId'] = undefined;

/**
 * Client's Company Registration Number
 * @member {String} CompanyRegistrationNumber
 */
ClientUpdateApiModel.prototype['CompanyRegistrationNumber'] = undefined;

/**
 * Client custom payment terms
 * @member {Number} DefaultDueDateInDays
 */
ClientUpdateApiModel.prototype['DefaultDueDateInDays'] = undefined;

/**
 * Client email
 * @member {String} Email
 */
ClientUpdateApiModel.prototype['Email'] = undefined;

/**
 * Entity id
 * @member {Number} Id
 */
ClientUpdateApiModel.prototype['Id'] = undefined;

/**
 * Name of the client
 * @member {String} Name
 */
ClientUpdateApiModel.prototype['Name'] = undefined;

/**
 * Client phone numer
 * @member {String} PhoneNumber
 */
ClientUpdateApiModel.prototype['PhoneNumber'] = undefined;

/**
 * Hold a value of the language in which the invoice will be sent
 * @member {Number} UiLanguageId
 */
ClientUpdateApiModel.prototype['UiLanguageId'] = undefined;

/**
 * Client's VAT number
 * @member {String} Vat
 */
ClientUpdateApiModel.prototype['Vat'] = undefined;






export default ClientUpdateApiModel;

