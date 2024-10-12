/**
 * Flight Offers Price
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.2.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class PhoneDeviceType.
* @enum {}
* @readonly
*/
export default class PhoneDeviceType {
    
        /**
         * value: "MOBILE"
         * @const
         */
        "MOBILE" = "MOBILE";

    
        /**
         * value: "LANDLINE"
         * @const
         */
        "LANDLINE" = "LANDLINE";

    
        /**
         * value: "FAX"
         * @const
         */
        "FAX" = "FAX";

    

    /**
    * Returns a <code>PhoneDeviceType</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/PhoneDeviceType} The enum <code>PhoneDeviceType</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

