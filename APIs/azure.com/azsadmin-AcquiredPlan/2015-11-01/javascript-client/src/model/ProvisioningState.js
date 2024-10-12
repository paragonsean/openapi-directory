/**
 * SubscriptionsManagementClient
 * The Admin Subscriptions Management Client.
 *
 * The version of the OpenAPI document: 2015-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class ProvisioningState.
* @enum {}
* @readonly
*/
export default class ProvisioningState {
    
        /**
         * value: "NotSpecified"
         * @const
         */
        "NotSpecified" = "NotSpecified";

    
        /**
         * value: "Accepted"
         * @const
         */
        "Accepted" = "Accepted";

    
        /**
         * value: "Failed"
         * @const
         */
        "Failed" = "Failed";

    
        /**
         * value: "Succeeded"
         * @const
         */
        "Succeeded" = "Succeeded";

    

    /**
    * Returns a <code>ProvisioningState</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/ProvisioningState} The enum <code>ProvisioningState</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

