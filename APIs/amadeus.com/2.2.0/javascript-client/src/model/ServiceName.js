/**
 * Flight Offers Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 2.2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class ServiceName.
* @enum {}
* @readonly
*/
export default class ServiceName {
    
        /**
         * value: "PRIORITY_BOARDING"
         * @const
         */
        "PRIORITY_BOARDING" = "PRIORITY_BOARDING";

    
        /**
         * value: "AIRPORT_CHECKIN"
         * @const
         */
        "AIRPORT_CHECKIN" = "AIRPORT_CHECKIN";

    

    /**
    * Returns a <code>ServiceName</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ServiceName} The enum <code>ServiceName</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

