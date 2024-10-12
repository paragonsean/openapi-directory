/**
 * Interactive documentation for your Premium plan
 *   This interactive documentation is using your API key which is filled in automatically, you can find and change this in [your dashboard](https://www.meteosource.com/client).  Using the `GET` button, open your selected endpoint and read the introduction. You will find a detailed description of available parameters. You can complete the `Parameters` section and hit `Execute` to view a full API response. You can then inspect the JSON response, copy the `curl` command to run it on your machine, or obtain a URL of the request. In this way, you can easily build request command for the data you need. 
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class Units.
* @enum {}
* @readonly
*/
export default class Units {
    
        /**
         * value: "auto"
         * @const
         */
        "auto" = "auto";

    
        /**
         * value: "metric"
         * @const
         */
        "metric" = "metric";

    
        /**
         * value: "us"
         * @const
         */
        "us" = "us";

    
        /**
         * value: "uk"
         * @const
         */
        "uk" = "uk";

    
        /**
         * value: "ca"
         * @const
         */
        "ca" = "ca";

    

    /**
    * Returns a <code>Units</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/Units} The enum <code>Units</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

