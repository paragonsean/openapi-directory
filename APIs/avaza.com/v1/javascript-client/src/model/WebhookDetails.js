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
 * The WebhookDetails model module.
 * @module model/WebhookDetails
 * @version v1
 */
class WebhookDetails {
    /**
     * Constructs a new <code>WebhookDetails</code>.
     * @alias module:model/WebhookDetails
     */
    constructor() { 
        
        WebhookDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>WebhookDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WebhookDetails} obj Optional instance to populate.
     * @return {module:model/WebhookDetails} The populated <code>WebhookDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WebhookDetails();

            if (data.hasOwnProperty('EventCode')) {
                obj['EventCode'] = ApiClient.convertToType(data['EventCode'], 'String');
            }
            if (data.hasOwnProperty('NotificationURL')) {
                obj['NotificationURL'] = ApiClient.convertToType(data['NotificationURL'], 'String');
            }
            if (data.hasOwnProperty('SubscriptionID')) {
                obj['SubscriptionID'] = ApiClient.convertToType(data['SubscriptionID'], 'Number');
            }
            if (data.hasOwnProperty('UserIDFK')) {
                obj['UserIDFK'] = ApiClient.convertToType(data['UserIDFK'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WebhookDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WebhookDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['EventCode'] && !(typeof data['EventCode'] === 'string' || data['EventCode'] instanceof String)) {
            throw new Error("Expected the field `EventCode` to be a primitive type in the JSON string but got " + data['EventCode']);
        }
        // ensure the json data is a string
        if (data['NotificationURL'] && !(typeof data['NotificationURL'] === 'string' || data['NotificationURL'] instanceof String)) {
            throw new Error("Expected the field `NotificationURL` to be a primitive type in the JSON string but got " + data['NotificationURL']);
        }

        return true;
    }


}



/**
 * @member {String} EventCode
 */
WebhookDetails.prototype['EventCode'] = undefined;

/**
 * @member {String} NotificationURL
 */
WebhookDetails.prototype['NotificationURL'] = undefined;

/**
 * @member {Number} SubscriptionID
 */
WebhookDetails.prototype['SubscriptionID'] = undefined;

/**
 * @member {Number} UserIDFK
 */
WebhookDetails.prototype['UserIDFK'] = undefined;






export default WebhookDetails;

