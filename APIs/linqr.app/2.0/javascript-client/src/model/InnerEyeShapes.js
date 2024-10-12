/**
 * LinQR
 * This is LinQR QR Code API documentation. This API allows you to generate custom, visually attractive QR Codes. The cloud infrastructure guarantees high availability and autoscalability of the service. You can generate hundreds of thousands of images this way and use them however you like.  We realize that your API use case may require custom solutions, and perhaps we lack functionality that is very important to you. In that case feel free to write an email to our support and tell us about it. We have repeatedly added new functions of our service directly after the requests of our users.  **General remarks:**  - maximum request size is fixed at 32MB.  - request timeout is fixed at 180 seconds.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@linqr.app
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
/**
* Enum class InnerEyeShapes.
* @enum {}
* @readonly
*/
export default class InnerEyeShapes {
    
        /**
         * value: "circle"
         * @const
         */
        "circle" = "circle";

    
        /**
         * value: "cushion"
         * @const
         */
        "cushion" = "cushion";

    
        /**
         * value: "default"
         * @const
         */
        "default" = "default";

    
        /**
         * value: "diamond"
         * @const
         */
        "diamond" = "diamond";

    
        /**
         * value: "dots"
         * @const
         */
        "dots" = "dots";

    
        /**
         * value: "heavyround"
         * @const
         */
        "heavyround" = "heavyround";

    
        /**
         * value: "horizontal_lines"
         * @const
         */
        "horizontal_lines" = "horizontal_lines";

    
        /**
         * value: "leaf"
         * @const
         */
        "leaf" = "leaf";

    
        /**
         * value: "left_eye"
         * @const
         */
        "left_eye" = "left_eye";

    
        /**
         * value: "lightround"
         * @const
         */
        "lightround" = "lightround";

    
        /**
         * value: "right_eye"
         * @const
         */
        "right_eye" = "right_eye";

    
        /**
         * value: "shield"
         * @const
         */
        "shield" = "shield";

    
        /**
         * value: "sieve"
         * @const
         */
        "sieve" = "sieve";

    
        /**
         * value: "star"
         * @const
         */
        "star" = "star";

    
        /**
         * value: "vertical_lines"
         * @const
         */
        "vertical_lines" = "vertical_lines";

    

    /**
    * Returns a <code>InnerEyeShapes</code> enum value from a Javascript object name.
    * @param {Object} data The plain JavaScript object containing the name of the enum value.
    * @return {module:model/InnerEyeShapes} The enum <code>InnerEyeShapes</code> value.
    */
    static constructFromObject(object) {
        return object;
    }
}

