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

/**
 * The CreditNoteLineItem model module.
 * @module model/CreditNoteLineItem
 * @version v1
 */
class CreditNoteLineItem {
    /**
     * Constructs a new <code>CreditNoteLineItem</code>.
     * @alias module:model/CreditNoteLineItem
     */
    constructor() { 
        
        CreditNoteLineItem.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreditNoteLineItem</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreditNoteLineItem} obj Optional instance to populate.
     * @return {module:model/CreditNoteLineItem} The populated <code>CreditNoteLineItem</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreditNoteLineItem();

            if (data.hasOwnProperty('Amount')) {
                obj['Amount'] = ApiClient.convertToType(data['Amount'], 'Number');
            }
            if (data.hasOwnProperty('Description')) {
                obj['Description'] = ApiClient.convertToType(data['Description'], 'String');
            }
            if (data.hasOwnProperty('Discount')) {
                obj['Discount'] = ApiClient.convertToType(data['Discount'], 'Number');
            }
            if (data.hasOwnProperty('Quantity')) {
                obj['Quantity'] = ApiClient.convertToType(data['Quantity'], 'Number');
            }
            if (data.hasOwnProperty('TaxAmount')) {
                obj['TaxAmount'] = ApiClient.convertToType(data['TaxAmount'], 'Number');
            }
            if (data.hasOwnProperty('TaxIDFK')) {
                obj['TaxIDFK'] = ApiClient.convertToType(data['TaxIDFK'], 'Number');
            }
            if (data.hasOwnProperty('TransactionLineItemID')) {
                obj['TransactionLineItemID'] = ApiClient.convertToType(data['TransactionLineItemID'], 'Number');
            }
            if (data.hasOwnProperty('UnitPrice')) {
                obj['UnitPrice'] = ApiClient.convertToType(data['UnitPrice'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreditNoteLineItem</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreditNoteLineItem</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Description'] && !(typeof data['Description'] === 'string' || data['Description'] instanceof String)) {
            throw new Error("Expected the field `Description` to be a primitive type in the JSON string but got " + data['Description']);
        }

        return true;
    }


}



/**
 * @member {Number} Amount
 */
CreditNoteLineItem.prototype['Amount'] = undefined;

/**
 * @member {String} Description
 */
CreditNoteLineItem.prototype['Description'] = undefined;

/**
 * @member {Number} Discount
 */
CreditNoteLineItem.prototype['Discount'] = undefined;

/**
 * @member {Number} Quantity
 */
CreditNoteLineItem.prototype['Quantity'] = undefined;

/**
 * @member {Number} TaxAmount
 */
CreditNoteLineItem.prototype['TaxAmount'] = undefined;

/**
 * @member {Number} TaxIDFK
 */
CreditNoteLineItem.prototype['TaxIDFK'] = undefined;

/**
 * @member {Number} TransactionLineItemID
 */
CreditNoteLineItem.prototype['TransactionLineItemID'] = undefined;

/**
 * @member {Number} UnitPrice
 */
CreditNoteLineItem.prototype['UnitPrice'] = undefined;






export default CreditNoteLineItem;

