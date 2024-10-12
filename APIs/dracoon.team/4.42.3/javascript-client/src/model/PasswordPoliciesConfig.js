/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EncryptionPasswordPolicies from './EncryptionPasswordPolicies';
import LoginPasswordPolicies from './LoginPasswordPolicies';
import SharesPasswordPolicies from './SharesPasswordPolicies';

/**
 * The PasswordPoliciesConfig model module.
 * @module model/PasswordPoliciesConfig
 * @version 4.42.3
 */
class PasswordPoliciesConfig {
    /**
     * Constructs a new <code>PasswordPoliciesConfig</code>.
     * Set of password policies
     * @alias module:model/PasswordPoliciesConfig
     */
    constructor() { 
        
        PasswordPoliciesConfig.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PasswordPoliciesConfig</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PasswordPoliciesConfig} obj Optional instance to populate.
     * @return {module:model/PasswordPoliciesConfig} The populated <code>PasswordPoliciesConfig</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PasswordPoliciesConfig();

            if (data.hasOwnProperty('encryptionPasswordPolicies')) {
                obj['encryptionPasswordPolicies'] = EncryptionPasswordPolicies.constructFromObject(data['encryptionPasswordPolicies']);
            }
            if (data.hasOwnProperty('loginPasswordPolicies')) {
                obj['loginPasswordPolicies'] = LoginPasswordPolicies.constructFromObject(data['loginPasswordPolicies']);
            }
            if (data.hasOwnProperty('sharesPasswordPolicies')) {
                obj['sharesPasswordPolicies'] = SharesPasswordPolicies.constructFromObject(data['sharesPasswordPolicies']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PasswordPoliciesConfig</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PasswordPoliciesConfig</code>.
     */
    static validateJSON(data) {
        // validate the optional field `encryptionPasswordPolicies`
        if (data['encryptionPasswordPolicies']) { // data not null
          EncryptionPasswordPolicies.validateJSON(data['encryptionPasswordPolicies']);
        }
        // validate the optional field `loginPasswordPolicies`
        if (data['loginPasswordPolicies']) { // data not null
          LoginPasswordPolicies.validateJSON(data['loginPasswordPolicies']);
        }
        // validate the optional field `sharesPasswordPolicies`
        if (data['sharesPasswordPolicies']) { // data not null
          SharesPasswordPolicies.validateJSON(data['sharesPasswordPolicies']);
        }

        return true;
    }


}



/**
 * @member {module:model/EncryptionPasswordPolicies} encryptionPasswordPolicies
 */
PasswordPoliciesConfig.prototype['encryptionPasswordPolicies'] = undefined;

/**
 * @member {module:model/LoginPasswordPolicies} loginPasswordPolicies
 */
PasswordPoliciesConfig.prototype['loginPasswordPolicies'] = undefined;

/**
 * @member {module:model/SharesPasswordPolicies} sharesPasswordPolicies
 */
PasswordPoliciesConfig.prototype['sharesPasswordPolicies'] = undefined;






export default PasswordPoliciesConfig;

