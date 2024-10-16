/**
 * Neblio REST API Suite
 * APIs for Interacting with NTP1 Tokens & The Neblio Blockchain
 *
 * The version of the OpenAPI document: 1.3.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The IssueTokenRequestMetadataRulesHoldersInner model module.
 * @module model/IssueTokenRequestMetadataRulesHoldersInner
 * @version 1.3.0
 */
class IssueTokenRequestMetadataRulesHoldersInner {
    /**
     * Constructs a new <code>IssueTokenRequestMetadataRulesHoldersInner</code>.
     * @alias module:model/IssueTokenRequestMetadataRulesHoldersInner
     */
    constructor() { 
        
        IssueTokenRequestMetadataRulesHoldersInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IssueTokenRequestMetadataRulesHoldersInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IssueTokenRequestMetadataRulesHoldersInner} obj Optional instance to populate.
     * @return {module:model/IssueTokenRequestMetadataRulesHoldersInner} The populated <code>IssueTokenRequestMetadataRulesHoldersInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IssueTokenRequestMetadataRulesHoldersInner();

            if (data.hasOwnProperty('address')) {
                obj['address'] = ApiClient.convertToType(data['address'], 'String');
            }
            if (data.hasOwnProperty('locked')) {
                obj['locked'] = ApiClient.convertToType(data['locked'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IssueTokenRequestMetadataRulesHoldersInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IssueTokenRequestMetadataRulesHoldersInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['address'] && !(typeof data['address'] === 'string' || data['address'] instanceof String)) {
            throw new Error("Expected the field `address` to be a primitive type in the JSON string but got " + data['address']);
        }

        return true;
    }


}



/**
 * Address that can hold the token
 * @member {String} address
 */
IssueTokenRequestMetadataRulesHoldersInner.prototype['address'] = undefined;

/**
 * Whether this rule can be modified in future transactions
 * @member {Boolean} locked
 */
IssueTokenRequestMetadataRulesHoldersInner.prototype['locked'] = undefined;






export default IssueTokenRequestMetadataRulesHoldersInner;

