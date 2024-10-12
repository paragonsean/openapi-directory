/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class TravelerType.
* @enum {}
* @readonly
*/
export default class TravelerType {
    
        /**
         * value: "ADULT"
         * @const
         */
        "ADULT" = "ADULT";

    
        /**
         * value: "CHILD"
         * @const
         */
        "CHILD" = "CHILD";

    
        /**
         * value: "SENIOR"
         * @const
         */
        "SENIOR" = "SENIOR";

    
        /**
         * value: "YOUNG"
         * @const
         */
        "YOUNG" = "YOUNG";

    
        /**
         * value: "HELD_INFANT"
         * @const
         */
        "HELD_INFANT" = "HELD_INFANT";

    
        /**
         * value: "SEATED_INFANT"
         * @const
         */
        "SEATED_INFANT" = "SEATED_INFANT";

    
        /**
         * value: "STUDENT"
         * @const
         */
        "STUDENT" = "STUDENT";

    

    /**
    * Returns a <code>TravelerType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/TravelerType} The enum <code>TravelerType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

