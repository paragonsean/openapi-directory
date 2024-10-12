/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class EC2FirewallDirection.
* @enum {}
* @readonly
*/
export default class EC2FirewallDirection {
    
        /**
         * value: "INBOUND"
         * @const
         */
        "INBOUND" = "INBOUND";

    
        /**
         * value: "OUTBOUND"
         * @const
         */
        "OUTBOUND" = "OUTBOUND";

    

    /**
    * Returns a <code>EC2FirewallDirection</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/EC2FirewallDirection} The enum <code>EC2FirewallDirection</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

