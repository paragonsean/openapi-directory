/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AccountAttributesAllowedIpInner from './AccountAttributesAllowedIpInner';
import BrandingSettings from './BrandingSettings';
import PlanDetails from './PlanDetails';
import Quota from './Quota';

/**
 * The AccountAttributes model module.
 * @module model/AccountAttributes
 * @version 2.0
 */
class AccountAttributes {
    /**
     * Constructs a new <code>AccountAttributes</code>.
     * 
     * @alias module:model/AccountAttributes
     */
    constructor() { 
        
        AccountAttributes.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AccountAttributes</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountAttributes} obj Optional instance to populate.
     * @return {module:model/AccountAttributes} The populated <code>AccountAttributes</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountAttributes();

            if (data.hasOwnProperty('accountName')) {
                obj['accountName'] = ApiClient.convertToType(data['accountName'], 'String');
            }
            if (data.hasOwnProperty('accountOnboarding')) {
                obj['accountOnboarding'] = ApiClient.convertToType(data['accountOnboarding'], 'Boolean');
            }
            if (data.hasOwnProperty('allowedIp')) {
                obj['allowedIp'] = ApiClient.convertToType(data['allowedIp'], [AccountAttributesAllowedIpInner]);
            }
            if (data.hasOwnProperty('branding')) {
                obj['branding'] = ApiClient.convertToType(data['branding'], 'Boolean');
            }
            if (data.hasOwnProperty('brandingSettings')) {
                obj['brandingSettings'] = BrandingSettings.constructFromObject(data['brandingSettings']);
            }
            if (data.hasOwnProperty('clientId')) {
                obj['clientId'] = ApiClient.convertToType(data['clientId'], 'Number');
            }
            if (data.hasOwnProperty('complexPasswords')) {
                obj['complexPasswords'] = ApiClient.convertToType(data['complexPasswords'], 'Boolean');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('customDomain')) {
                obj['customDomain'] = ApiClient.convertToType(data['customDomain'], 'Boolean');
            }
            if (data.hasOwnProperty('customSignature')) {
                obj['customSignature'] = ApiClient.convertToType(data['customSignature'], 'String');
            }
            if (data.hasOwnProperty('externalDomains')) {
                obj['externalDomains'] = ApiClient.convertToType(data['externalDomains'], ['String']);
            }
            if (data.hasOwnProperty('maxUsers')) {
                obj['maxUsers'] = ApiClient.convertToType(data['maxUsers'], 'Number');
            }
            if (data.hasOwnProperty('modified')) {
                obj['modified'] = ApiClient.convertToType(data['modified'], 'Date');
            }
            if (data.hasOwnProperty('planDetails')) {
                obj['planDetails'] = PlanDetails.constructFromObject(data['planDetails']);
            }
            if (data.hasOwnProperty('quota')) {
                obj['quota'] = Quota.constructFromObject(data['quota']);
            }
            if (data.hasOwnProperty('secureOnly')) {
                obj['secureOnly'] = ApiClient.convertToType(data['secureOnly'], 'Boolean');
            }
            if (data.hasOwnProperty('showReferralLinks')) {
                obj['showReferralLinks'] = ApiClient.convertToType(data['showReferralLinks'], 'Boolean');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'Number');
            }
            if (data.hasOwnProperty('userCount')) {
                obj['userCount'] = ApiClient.convertToType(data['userCount'], 'Number');
            }
            if (data.hasOwnProperty('welcomeEmailContent')) {
                obj['welcomeEmailContent'] = ApiClient.convertToType(data['welcomeEmailContent'], 'String');
            }
            if (data.hasOwnProperty('welcomeEmailSubject')) {
                obj['welcomeEmailSubject'] = ApiClient.convertToType(data['welcomeEmailSubject'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountAttributes</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountAttributes</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['accountName'] && !(typeof data['accountName'] === 'string' || data['accountName'] instanceof String)) {
            throw new Error("Expected the field `accountName` to be a primitive type in the JSON string but got " + data['accountName']);
        }
        if (data['allowedIp']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['allowedIp'])) {
                throw new Error("Expected the field `allowedIp` to be an array in the JSON data but got " + data['allowedIp']);
            }
            // validate the optional field `allowedIp` (array)
            for (const item of data['allowedIp']) {
                AccountAttributesAllowedIpInner.validateJSON(item);
            };
        }
        // validate the optional field `brandingSettings`
        if (data['brandingSettings']) { // data not null
          BrandingSettings.validateJSON(data['brandingSettings']);
        }
        // ensure the json data is a string
        if (data['customSignature'] && !(typeof data['customSignature'] === 'string' || data['customSignature'] instanceof String)) {
            throw new Error("Expected the field `customSignature` to be a primitive type in the JSON string but got " + data['customSignature']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['externalDomains'])) {
            throw new Error("Expected the field `externalDomains` to be an array in the JSON data but got " + data['externalDomains']);
        }
        // validate the optional field `planDetails`
        if (data['planDetails']) { // data not null
          PlanDetails.validateJSON(data['planDetails']);
        }
        // validate the optional field `quota`
        if (data['quota']) { // data not null
          Quota.validateJSON(data['quota']);
        }
        // ensure the json data is a string
        if (data['welcomeEmailContent'] && !(typeof data['welcomeEmailContent'] === 'string' || data['welcomeEmailContent'] instanceof String)) {
            throw new Error("Expected the field `welcomeEmailContent` to be a primitive type in the JSON string but got " + data['welcomeEmailContent']);
        }
        // ensure the json data is a string
        if (data['welcomeEmailSubject'] && !(typeof data['welcomeEmailSubject'] === 'string' || data['welcomeEmailSubject'] instanceof String)) {
            throw new Error("Expected the field `welcomeEmailSubject` to be a primitive type in the JSON string but got " + data['welcomeEmailSubject']);
        }

        return true;
    }


}



/**
 * Name of the account
 * @member {String} accountName
 */
AccountAttributes.prototype['accountName'] = undefined;

/**
 * Whether the web application onboarding help is enabled for new users in the account.
 * @member {Boolean} accountOnboarding
 */
AccountAttributes.prototype['accountOnboarding'] = undefined;

/**
 * Range of IP addresses allowed to access this account.
 * @member {Array.<module:model/AccountAttributesAllowedIpInner>} allowedIp
 */
AccountAttributes.prototype['allowedIp'] = undefined;

/**
 * Branding flag. Set to `true` if the account has branding functionality enabled.
 * @member {Boolean} branding
 */
AccountAttributes.prototype['branding'] = undefined;

/**
 * @member {module:model/BrandingSettings} brandingSettings
 */
AccountAttributes.prototype['brandingSettings'] = undefined;

/**
 * (ExaVault Use Only) Internal ID of the account in CMS.
 * @member {Number} clientId
 */
AccountAttributes.prototype['clientId'] = undefined;

/**
 * Flag to indicate whether the account requires complex passwords. Set to `true` to require complex passwords on all users and shares.
 * @member {Boolean} complexPasswords
 */
AccountAttributes.prototype['complexPasswords'] = undefined;

/**
 * Timestamp of account creation.
 * @member {Date} created
 */
AccountAttributes.prototype['created'] = undefined;

/**
 * Custom domain flag. Set to `true` if account type allows custom domain functionality.
 * @member {Boolean} customDomain
 */
AccountAttributes.prototype['customDomain'] = undefined;

/**
 * Custom signature for all account emails users or recipients will receive.
 * @member {String} customSignature
 */
AccountAttributes.prototype['customSignature'] = undefined;

/**
 * Custom domain used to brand this account.
 * @member {Array.<String>} externalDomains
 */
AccountAttributes.prototype['externalDomains'] = undefined;

/**
 * Maximum number of users the account can have. This can be increased by contacting ExaVault Support.
 * @member {Number} maxUsers
 */
AccountAttributes.prototype['maxUsers'] = undefined;

/**
 * Timestamp of account modification.
 * @member {Date} modified
 */
AccountAttributes.prototype['modified'] = undefined;

/**
 * @member {module:model/PlanDetails} planDetails
 */
AccountAttributes.prototype['planDetails'] = undefined;

/**
 * @member {module:model/Quota} quota
 */
AccountAttributes.prototype['quota'] = undefined;

/**
 * Flag to indicate whether the account disables connections via insecure protocols (e.g. FTP). Set to `true` to disable all traffic over port 21.
 * @member {Boolean} secureOnly
 */
AccountAttributes.prototype['secureOnly'] = undefined;

/**
 * Flag to indicate showing of referrals links in the account. Set to `true` to include marketing messages in share invitations.
 * @member {Boolean} showReferralLinks
 */
AccountAttributes.prototype['showReferralLinks'] = undefined;

/**
 * Account status flag. A one (1) means the account is active; zero (0) means it is suspended.
 * @member {module:model/AccountAttributes.StatusEnum} status
 */
AccountAttributes.prototype['status'] = undefined;

/**
 * Current number of users on the account.
 * @member {Number} userCount
 */
AccountAttributes.prototype['userCount'] = undefined;

/**
 * Content of welcome email each new user will receive.
 * @member {String} welcomeEmailContent
 */
AccountAttributes.prototype['welcomeEmailContent'] = undefined;

/**
 * Subject of welcome email each new user will receive.
 * @member {String} welcomeEmailSubject
 */
AccountAttributes.prototype['welcomeEmailSubject'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {Number}
 * @readonly
 */
AccountAttributes['StatusEnum'] = {

    /**
     * value: 1
     * @const
     */
    "1": 1,

    /**
     * value: 0
     * @const
     */
    "0": 0
};



export default AccountAttributes;

