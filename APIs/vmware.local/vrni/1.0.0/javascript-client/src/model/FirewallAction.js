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
* Enum class FirewallAction.
* @enum {}
* @readonly
*/
export default class FirewallAction {
    
        /**
         * value: "ALLOW"
         * @const
         */
        "ALLOW" = "ALLOW";

    
        /**
         * value: "ACCEPT"
         * @const
         */
        "ACCEPT" = "ACCEPT";

    
        /**
         * value: "DENY"
         * @const
         */
        "DENY" = "DENY";

    
        /**
         * value: "DROP"
         * @const
         */
        "DROP" = "DROP";

    
        /**
         * value: "REJECT"
         * @const
         */
        "REJECT" = "REJECT";

    
        /**
         * value: "REDIRECT"
         * @const
         */
        "REDIRECT" = "REDIRECT";

    
        /**
         * value: "DO_NOT_REDIRECT"
         * @const
         */
        "DO_NOT_REDIRECT" = "DO_NOT_REDIRECT";

    

    /**
    * Returns a <code>FirewallAction</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/FirewallAction} The enum <code>FirewallAction</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

