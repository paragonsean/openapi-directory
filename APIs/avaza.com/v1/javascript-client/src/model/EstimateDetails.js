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

import ApiClient from '../ApiClient';
import EstimateLineItemDetails from './EstimateLineItemDetails';
import EstimateLinks from './EstimateLinks';
import IssuerDetails from './IssuerDetails';
import RecipientDetails from './RecipientDetails';

/**
 * The EstimateDetails model module.
 * @module model/EstimateDetails
 * @version v1
 */
class EstimateDetails {
    /**
     * Constructs a new <code>EstimateDetails</code>.
     * @alias module:model/EstimateDetails
     */
    constructor() { 
        
        EstimateDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EstimateDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EstimateDetails} obj Optional instance to populate.
     * @return {module:model/EstimateDetails} The populated <code>EstimateDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EstimateDetails();

            if (data.hasOwnProperty('AccountIDFK')) {
                obj['AccountIDFK'] = ApiClient.convertToType(data['AccountIDFK'], 'Number');
            }
            if (data.hasOwnProperty('Balance')) {
                obj['Balance'] = ApiClient.convertToType(data['Balance'], 'Number');
            }
            if (data.hasOwnProperty('CompanyIDFK')) {
                obj['CompanyIDFK'] = ApiClient.convertToType(data['CompanyIDFK'], 'Number');
            }
            if (data.hasOwnProperty('CompanyName')) {
                obj['CompanyName'] = ApiClient.convertToType(data['CompanyName'], 'String');
            }
            if (data.hasOwnProperty('CurrencyCode')) {
                obj['CurrencyCode'] = ApiClient.convertToType(data['CurrencyCode'], 'String');
            }
            if (data.hasOwnProperty('DateCreated')) {
                obj['DateCreated'] = ApiClient.convertToType(data['DateCreated'], 'Date');
            }
            if (data.hasOwnProperty('DateIssued')) {
                obj['DateIssued'] = ApiClient.convertToType(data['DateIssued'], 'Date');
            }
            if (data.hasOwnProperty('DateSent')) {
                obj['DateSent'] = ApiClient.convertToType(data['DateSent'], 'Date');
            }
            if (data.hasOwnProperty('DateUpdated')) {
                obj['DateUpdated'] = ApiClient.convertToType(data['DateUpdated'], 'Date');
            }
            if (data.hasOwnProperty('DueDate')) {
                obj['DueDate'] = ApiClient.convertToType(data['DueDate'], 'Date');
            }
            if (data.hasOwnProperty('EstimateID')) {
                obj['EstimateID'] = ApiClient.convertToType(data['EstimateID'], 'Number');
            }
            if (data.hasOwnProperty('EstimateItemNumber')) {
                obj['EstimateItemNumber'] = ApiClient.convertToType(data['EstimateItemNumber'], 'String');
            }
            if (data.hasOwnProperty('EstimatePrefix')) {
                obj['EstimatePrefix'] = ApiClient.convertToType(data['EstimatePrefix'], 'String');
            }
            if (data.hasOwnProperty('EstimateStatusCode')) {
                obj['EstimateStatusCode'] = ApiClient.convertToType(data['EstimateStatusCode'], 'String');
            }
            if (data.hasOwnProperty('EstimateTaxConfigCode')) {
                obj['EstimateTaxConfigCode'] = ApiClient.convertToType(data['EstimateTaxConfigCode'], 'String');
            }
            if (data.hasOwnProperty('ExchangeRate')) {
                obj['ExchangeRate'] = ApiClient.convertToType(data['ExchangeRate'], 'Number');
            }
            if (data.hasOwnProperty('Issuer')) {
                obj['Issuer'] = IssuerDetails.constructFromObject(data['Issuer']);
            }
            if (data.hasOwnProperty('LineItems')) {
                obj['LineItems'] = ApiClient.convertToType(data['LineItems'], [EstimateLineItemDetails]);
            }
            if (data.hasOwnProperty('Links')) {
                obj['Links'] = EstimateLinks.constructFromObject(data['Links']);
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('Recipient')) {
                obj['Recipient'] = RecipientDetails.constructFromObject(data['Recipient']);
            }
            if (data.hasOwnProperty('Subject')) {
                obj['Subject'] = ApiClient.convertToType(data['Subject'], 'String');
            }
            if (data.hasOwnProperty('TaxAmount')) {
                obj['TaxAmount'] = ApiClient.convertToType(data['TaxAmount'], 'Number');
            }
            if (data.hasOwnProperty('TotalAmount')) {
                obj['TotalAmount'] = ApiClient.convertToType(data['TotalAmount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EstimateDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EstimateDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['CompanyName'] && !(typeof data['CompanyName'] === 'string' || data['CompanyName'] instanceof String)) {
            throw new Error("Expected the field `CompanyName` to be a primitive type in the JSON string but got " + data['CompanyName']);
        }
        // ensure the json data is a string
        if (data['CurrencyCode'] && !(typeof data['CurrencyCode'] === 'string' || data['CurrencyCode'] instanceof String)) {
            throw new Error("Expected the field `CurrencyCode` to be a primitive type in the JSON string but got " + data['CurrencyCode']);
        }
        // ensure the json data is a string
        if (data['EstimateItemNumber'] && !(typeof data['EstimateItemNumber'] === 'string' || data['EstimateItemNumber'] instanceof String)) {
            throw new Error("Expected the field `EstimateItemNumber` to be a primitive type in the JSON string but got " + data['EstimateItemNumber']);
        }
        // ensure the json data is a string
        if (data['EstimatePrefix'] && !(typeof data['EstimatePrefix'] === 'string' || data['EstimatePrefix'] instanceof String)) {
            throw new Error("Expected the field `EstimatePrefix` to be a primitive type in the JSON string but got " + data['EstimatePrefix']);
        }
        // ensure the json data is a string
        if (data['EstimateStatusCode'] && !(typeof data['EstimateStatusCode'] === 'string' || data['EstimateStatusCode'] instanceof String)) {
            throw new Error("Expected the field `EstimateStatusCode` to be a primitive type in the JSON string but got " + data['EstimateStatusCode']);
        }
        // ensure the json data is a string
        if (data['EstimateTaxConfigCode'] && !(typeof data['EstimateTaxConfigCode'] === 'string' || data['EstimateTaxConfigCode'] instanceof String)) {
            throw new Error("Expected the field `EstimateTaxConfigCode` to be a primitive type in the JSON string but got " + data['EstimateTaxConfigCode']);
        }
        // validate the optional field `Issuer`
        if (data['Issuer']) { // data not null
          IssuerDetails.validateJSON(data['Issuer']);
        }
        if (data['LineItems']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['LineItems'])) {
                throw new Error("Expected the field `LineItems` to be an array in the JSON data but got " + data['LineItems']);
            }
            // validate the optional field `LineItems` (array)
            for (const item of data['LineItems']) {
                EstimateLineItemDetails.validateJSON(item);
            };
        }
        // validate the optional field `Links`
        if (data['Links']) { // data not null
          EstimateLinks.validateJSON(data['Links']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // validate the optional field `Recipient`
        if (data['Recipient']) { // data not null
          RecipientDetails.validateJSON(data['Recipient']);
        }
        // ensure the json data is a string
        if (data['Subject'] && !(typeof data['Subject'] === 'string' || data['Subject'] instanceof String)) {
            throw new Error("Expected the field `Subject` to be a primitive type in the JSON string but got " + data['Subject']);
        }

        return true;
    }


}



/**
 * @member {Number} AccountIDFK
 */
EstimateDetails.prototype['AccountIDFK'] = undefined;

/**
 * @member {Number} Balance
 */
EstimateDetails.prototype['Balance'] = undefined;

/**
 * @member {Number} CompanyIDFK
 */
EstimateDetails.prototype['CompanyIDFK'] = undefined;

/**
 * @member {String} CompanyName
 */
EstimateDetails.prototype['CompanyName'] = undefined;

/**
 * @member {String} CurrencyCode
 */
EstimateDetails.prototype['CurrencyCode'] = undefined;

/**
 * @member {Date} DateCreated
 */
EstimateDetails.prototype['DateCreated'] = undefined;

/**
 * @member {Date} DateIssued
 */
EstimateDetails.prototype['DateIssued'] = undefined;

/**
 * @member {Date} DateSent
 */
EstimateDetails.prototype['DateSent'] = undefined;

/**
 * @member {Date} DateUpdated
 */
EstimateDetails.prototype['DateUpdated'] = undefined;

/**
 * @member {Date} DueDate
 */
EstimateDetails.prototype['DueDate'] = undefined;

/**
 * @member {Number} EstimateID
 */
EstimateDetails.prototype['EstimateID'] = undefined;

/**
 * @member {String} EstimateItemNumber
 */
EstimateDetails.prototype['EstimateItemNumber'] = undefined;

/**
 * @member {String} EstimatePrefix
 */
EstimateDetails.prototype['EstimatePrefix'] = undefined;

/**
 * @member {String} EstimateStatusCode
 */
EstimateDetails.prototype['EstimateStatusCode'] = undefined;

/**
 * @member {String} EstimateTaxConfigCode
 */
EstimateDetails.prototype['EstimateTaxConfigCode'] = undefined;

/**
 * @member {Number} ExchangeRate
 */
EstimateDetails.prototype['ExchangeRate'] = undefined;

/**
 * @member {module:model/IssuerDetails} Issuer
 */
EstimateDetails.prototype['Issuer'] = undefined;

/**
 * @member {Array.<module:model/EstimateLineItemDetails>} LineItems
 */
EstimateDetails.prototype['LineItems'] = undefined;

/**
 * @member {module:model/EstimateLinks} Links
 */
EstimateDetails.prototype['Links'] = undefined;

/**
 * @member {String} Notes
 */
EstimateDetails.prototype['Notes'] = undefined;

/**
 * @member {module:model/RecipientDetails} Recipient
 */
EstimateDetails.prototype['Recipient'] = undefined;

/**
 * @member {String} Subject
 */
EstimateDetails.prototype['Subject'] = undefined;

/**
 * @member {Number} TaxAmount
 */
EstimateDetails.prototype['TaxAmount'] = undefined;

/**
 * @member {Number} TotalAmount
 */
EstimateDetails.prototype['TotalAmount'] = undefined;






export default EstimateDetails;

