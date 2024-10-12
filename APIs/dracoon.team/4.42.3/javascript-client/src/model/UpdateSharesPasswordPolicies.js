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
import CharacterRules from './CharacterRules';

/**
 * The UpdateSharesPasswordPolicies model module.
 * @module model/UpdateSharesPasswordPolicies
 * @version 4.42.3
 */
class UpdateSharesPasswordPolicies {
    /**
     * Constructs a new <code>UpdateSharesPasswordPolicies</code>.
     * Request model for updating shares password policies
     * @alias module:model/UpdateSharesPasswordPolicies
     */
    constructor() { 
        
        UpdateSharesPasswordPolicies.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateSharesPasswordPolicies</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateSharesPasswordPolicies} obj Optional instance to populate.
     * @return {module:model/UpdateSharesPasswordPolicies} The populated <code>UpdateSharesPasswordPolicies</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateSharesPasswordPolicies();

            if (data.hasOwnProperty('characterRules')) {
                obj['characterRules'] = CharacterRules.constructFromObject(data['characterRules']);
            }
            if (data.hasOwnProperty('minLength')) {
                obj['minLength'] = ApiClient.convertToType(data['minLength'], 'Number');
            }
            if (data.hasOwnProperty('rejectDictionaryWords')) {
                obj['rejectDictionaryWords'] = ApiClient.convertToType(data['rejectDictionaryWords'], 'Boolean');
            }
            if (data.hasOwnProperty('rejectKeyboardPatterns')) {
                obj['rejectKeyboardPatterns'] = ApiClient.convertToType(data['rejectKeyboardPatterns'], 'Boolean');
            }
            if (data.hasOwnProperty('rejectUserInfo')) {
                obj['rejectUserInfo'] = ApiClient.convertToType(data['rejectUserInfo'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateSharesPasswordPolicies</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateSharesPasswordPolicies</code>.
     */
    static validateJSON(data) {
        // validate the optional field `characterRules`
        if (data['characterRules']) { // data not null
          CharacterRules.validateJSON(data['characterRules']);
        }

        return true;
    }


}



/**
 * @member {module:model/CharacterRules} characterRules
 */
UpdateSharesPasswordPolicies.prototype['characterRules'] = undefined;

/**
 * Minimum number of characters a password must contain
 * @member {Number} minLength
 */
UpdateSharesPasswordPolicies.prototype['minLength'] = undefined;

/**
 * Determines whether a password must NOT contain word(s) from a dictionary
 * @member {Boolean} rejectDictionaryWords
 */
UpdateSharesPasswordPolicies.prototype['rejectDictionaryWords'] = undefined;

/**
 * Determines whether a password must NOT contain keyboard patterns (e.g. `qwertz`, `asdf`)  (min. 4 character pattern)
 * @member {Boolean} rejectKeyboardPatterns
 */
UpdateSharesPasswordPolicies.prototype['rejectKeyboardPatterns'] = undefined;

/**
 * Determines whether a password must NOT contain user info (first name, last name, email, user name)
 * @member {Boolean} rejectUserInfo
 */
UpdateSharesPasswordPolicies.prototype['rejectUserInfo'] = undefined;






export default UpdateSharesPasswordPolicies;

