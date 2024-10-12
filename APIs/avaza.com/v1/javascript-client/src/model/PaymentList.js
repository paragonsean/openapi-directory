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
import Payment from './Payment';

/**
 * The PaymentList model module.
 * @module model/PaymentList
 * @version v1
 */
class PaymentList {
    /**
     * Constructs a new <code>PaymentList</code>.
     * @alias module:model/PaymentList
     */
    constructor() { 
        
        PaymentList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PaymentList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaymentList} obj Optional instance to populate.
     * @return {module:model/PaymentList} The populated <code>PaymentList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PaymentList();

            if (data.hasOwnProperty('PageNumber')) {
                obj['PageNumber'] = ApiClient.convertToType(data['PageNumber'], 'Number');
            }
            if (data.hasOwnProperty('PageSize')) {
                obj['PageSize'] = ApiClient.convertToType(data['PageSize'], 'Number');
            }
            if (data.hasOwnProperty('Payments')) {
                obj['Payments'] = ApiClient.convertToType(data['Payments'], [Payment]);
            }
            if (data.hasOwnProperty('TotalCount')) {
                obj['TotalCount'] = ApiClient.convertToType(data['TotalCount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PaymentList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaymentList</code>.
     */
    static validateJSON(data) {
        if (data['Payments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Payments'])) {
                throw new Error("Expected the field `Payments` to be an array in the JSON data but got " + data['Payments']);
            }
            // validate the optional field `Payments` (array)
            for (const item of data['Payments']) {
                Payment.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Number} PageNumber
 */
PaymentList.prototype['PageNumber'] = undefined;

/**
 * @member {Number} PageSize
 */
PaymentList.prototype['PageSize'] = undefined;

/**
 * @member {Array.<module:model/Payment>} Payments
 */
PaymentList.prototype['Payments'] = undefined;

/**
 * @member {Number} TotalCount
 */
PaymentList.prototype['TotalCount'] = undefined;






export default PaymentList;

