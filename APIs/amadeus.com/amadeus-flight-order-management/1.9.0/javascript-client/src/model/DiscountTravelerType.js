/**
 * Flight Order Management
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
* Enum class DiscountTravelerType.
* @enum {}
* @readonly
*/
export default class DiscountTravelerType {
    
        /**
         * value: "SPANISH_CITIZEN"
         * @const
         */
        "SPANISH_CITIZEN" = "SPANISH_CITIZEN";

    
        /**
         * value: "EUROPEAN_CITIZEN"
         * @const
         */
        "EUROPEAN_CITIZEN" = "EUROPEAN_CITIZEN";

    
        /**
         * value: "GOVERNMENT_WORKER"
         * @const
         */
        "GOVERNMENT_WORKER" = "GOVERNMENT_WORKER";

    
        /**
         * value: "MILITARY"
         * @const
         */
        "MILITARY" = "MILITARY";

    
        /**
         * value: "MINOR_WITHOUT_ID"
         * @const
         */
        "MINOR_WITHOUT_ID" = "MINOR_WITHOUT_ID";

    

    /**
    * Returns a <code>DiscountTravelerType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/DiscountTravelerType} The enum <code>DiscountTravelerType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

