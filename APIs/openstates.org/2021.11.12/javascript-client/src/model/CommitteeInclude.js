/**
 * Open States API v3
 *  * [More documentation](https://docs.openstates.org/en/latest/api/v3/index.html) * [Register for an account](https://openstates.org/accounts/signup/)   **We are currently working to restore experimental support for committees & events.**  During this period please note that data is not yet available for all states and the exact format of the new endpoints may change slightly depending on user feedback.  If you have any issues or questions use our [GitHub Issues](https://github.com/openstates/issues/issues) to give feedback. 
 *
 * The version of the OpenAPI document: 2021.11.12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class CommitteeInclude.
* @enum {}
* @readonly
*/
export default class CommitteeInclude {
    
        /**
         * value: "memberships"
         * @const
         */
        "memberships" = "memberships";

    
        /**
         * value: "links"
         * @const
         */
        "links" = "links";

    
        /**
         * value: "sources"
         * @const
         */
        "sources" = "sources";

    

    /**
    * Returns a <code>CommitteeInclude</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/CommitteeInclude} The enum <code>CommitteeInclude</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

