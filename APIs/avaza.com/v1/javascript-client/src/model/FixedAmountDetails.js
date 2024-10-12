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
 * The FixedAmountDetails model module.
 * @module model/FixedAmountDetails
 * @version v1
 */
class FixedAmountDetails {
    /**
     * Constructs a new <code>FixedAmountDetails</code>.
     * @alias module:model/FixedAmountDetails
     */
    constructor() { 
        
        FixedAmountDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FixedAmountDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FixedAmountDetails} obj Optional instance to populate.
     * @return {module:model/FixedAmountDetails} The populated <code>FixedAmountDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FixedAmountDetails();

            if (data.hasOwnProperty('Amount')) {
                obj['Amount'] = ApiClient.convertToType(data['Amount'], 'Number');
            }
            if (data.hasOwnProperty('DateCreated')) {
                obj['DateCreated'] = ApiClient.convertToType(data['DateCreated'], 'Date');
            }
            if (data.hasOwnProperty('DateUpdated')) {
                obj['DateUpdated'] = ApiClient.convertToType(data['DateUpdated'], 'Date');
            }
            if (data.hasOwnProperty('FixedAmountID')) {
                obj['FixedAmountID'] = ApiClient.convertToType(data['FixedAmountID'], 'Number');
            }
            if (data.hasOwnProperty('InventoryItemIDFK')) {
                obj['InventoryItemIDFK'] = ApiClient.convertToType(data['InventoryItemIDFK'], 'Number');
            }
            if (data.hasOwnProperty('InventoryItemName')) {
                obj['InventoryItemName'] = ApiClient.convertToType(data['InventoryItemName'], 'String');
            }
            if (data.hasOwnProperty('Notes')) {
                obj['Notes'] = ApiClient.convertToType(data['Notes'], 'String');
            }
            if (data.hasOwnProperty('ProjectCode')) {
                obj['ProjectCode'] = ApiClient.convertToType(data['ProjectCode'], 'String');
            }
            if (data.hasOwnProperty('ProjectIDFK')) {
                obj['ProjectIDFK'] = ApiClient.convertToType(data['ProjectIDFK'], 'Number');
            }
            if (data.hasOwnProperty('ProjectTitle')) {
                obj['ProjectTitle'] = ApiClient.convertToType(data['ProjectTitle'], 'String');
            }
            if (data.hasOwnProperty('TaskIDFK')) {
                obj['TaskIDFK'] = ApiClient.convertToType(data['TaskIDFK'], 'Number');
            }
            if (data.hasOwnProperty('TaskTitle')) {
                obj['TaskTitle'] = ApiClient.convertToType(data['TaskTitle'], 'String');
            }
            if (data.hasOwnProperty('UpdatedByUserIDFK')) {
                obj['UpdatedByUserIDFK'] = ApiClient.convertToType(data['UpdatedByUserIDFK'], 'Number');
            }
            if (data.hasOwnProperty('isInvoiced')) {
                obj['isInvoiced'] = ApiClient.convertToType(data['isInvoiced'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FixedAmountDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FixedAmountDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['InventoryItemName'] && !(typeof data['InventoryItemName'] === 'string' || data['InventoryItemName'] instanceof String)) {
            throw new Error("Expected the field `InventoryItemName` to be a primitive type in the JSON string but got " + data['InventoryItemName']);
        }
        // ensure the json data is a string
        if (data['Notes'] && !(typeof data['Notes'] === 'string' || data['Notes'] instanceof String)) {
            throw new Error("Expected the field `Notes` to be a primitive type in the JSON string but got " + data['Notes']);
        }
        // ensure the json data is a string
        if (data['ProjectCode'] && !(typeof data['ProjectCode'] === 'string' || data['ProjectCode'] instanceof String)) {
            throw new Error("Expected the field `ProjectCode` to be a primitive type in the JSON string but got " + data['ProjectCode']);
        }
        // ensure the json data is a string
        if (data['ProjectTitle'] && !(typeof data['ProjectTitle'] === 'string' || data['ProjectTitle'] instanceof String)) {
            throw new Error("Expected the field `ProjectTitle` to be a primitive type in the JSON string but got " + data['ProjectTitle']);
        }
        // ensure the json data is a string
        if (data['TaskTitle'] && !(typeof data['TaskTitle'] === 'string' || data['TaskTitle'] instanceof String)) {
            throw new Error("Expected the field `TaskTitle` to be a primitive type in the JSON string but got " + data['TaskTitle']);
        }

        return true;
    }


}



/**
 * @member {Number} Amount
 */
FixedAmountDetails.prototype['Amount'] = undefined;

/**
 * @member {Date} DateCreated
 */
FixedAmountDetails.prototype['DateCreated'] = undefined;

/**
 * @member {Date} DateUpdated
 */
FixedAmountDetails.prototype['DateUpdated'] = undefined;

/**
 * @member {Number} FixedAmountID
 */
FixedAmountDetails.prototype['FixedAmountID'] = undefined;

/**
 * @member {Number} InventoryItemIDFK
 */
FixedAmountDetails.prototype['InventoryItemIDFK'] = undefined;

/**
 * @member {String} InventoryItemName
 */
FixedAmountDetails.prototype['InventoryItemName'] = undefined;

/**
 * @member {String} Notes
 */
FixedAmountDetails.prototype['Notes'] = undefined;

/**
 * @member {String} ProjectCode
 */
FixedAmountDetails.prototype['ProjectCode'] = undefined;

/**
 * @member {Number} ProjectIDFK
 */
FixedAmountDetails.prototype['ProjectIDFK'] = undefined;

/**
 * @member {String} ProjectTitle
 */
FixedAmountDetails.prototype['ProjectTitle'] = undefined;

/**
 * @member {Number} TaskIDFK
 */
FixedAmountDetails.prototype['TaskIDFK'] = undefined;

/**
 * @member {String} TaskTitle
 */
FixedAmountDetails.prototype['TaskTitle'] = undefined;

/**
 * @member {Number} UpdatedByUserIDFK
 */
FixedAmountDetails.prototype['UpdatedByUserIDFK'] = undefined;

/**
 * @member {Boolean} isInvoiced
 */
FixedAmountDetails.prototype['isInvoiced'] = undefined;






export default FixedAmountDetails;

