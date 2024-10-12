/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2015-10-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FirewallRuleProperties model module.
 * @module model/FirewallRuleProperties
 * @version 2015-10-01-preview
 */
class FirewallRuleProperties {
    /**
     * Constructs a new <code>FirewallRuleProperties</code>.
     * Data Lake Store firewall rule properties information
     * @alias module:model/FirewallRuleProperties
     */
    constructor() { 
        
        FirewallRuleProperties.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FirewallRuleProperties</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FirewallRuleProperties} obj Optional instance to populate.
     * @return {module:model/FirewallRuleProperties} The populated <code>FirewallRuleProperties</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FirewallRuleProperties();

            if (data.hasOwnProperty('endIpAddress')) {
                obj['endIpAddress'] = ApiClient.convertToType(data['endIpAddress'], 'String');
            }
            if (data.hasOwnProperty('startIpAddress')) {
                obj['startIpAddress'] = ApiClient.convertToType(data['startIpAddress'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FirewallRuleProperties</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FirewallRuleProperties</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['endIpAddress'] && !(typeof data['endIpAddress'] === 'string' || data['endIpAddress'] instanceof String)) {
            throw new Error("Expected the field `endIpAddress` to be a primitive type in the JSON string but got " + data['endIpAddress']);
        }
        // ensure the json data is a string
        if (data['startIpAddress'] && !(typeof data['startIpAddress'] === 'string' || data['startIpAddress'] instanceof String)) {
            throw new Error("Expected the field `startIpAddress` to be a primitive type in the JSON string but got " + data['startIpAddress']);
        }

        return true;
    }


}



/**
 * the end IP address for the firewall rule.
 * @member {String} endIpAddress
 */
FirewallRuleProperties.prototype['endIpAddress'] = undefined;

/**
 * the start IP address for the firewall rule.
 * @member {String} startIpAddress
 */
FirewallRuleProperties.prototype['startIpAddress'] = undefined;






export default FirewallRuleProperties;

