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
* Enum class Protocol.
* @enum {}
* @readonly
*/
export default class Protocol {
    
        /**
         * value: "TCP"
         * @const
         */
        "TCP" = "TCP";

    
        /**
         * value: "UDP"
         * @const
         */
        "UDP" = "UDP";

    
        /**
         * value: "OTHER"
         * @const
         */
        "OTHER" = "OTHER";

    

    /**
    * Returns a <code>Protocol</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/Protocol} The enum <code>Protocol</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

