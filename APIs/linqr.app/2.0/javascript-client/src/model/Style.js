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
import BackgroundStyle from './BackgroundStyle';
import InnerEyeStyle from './InnerEyeStyle';
import ModuleStyle from './ModuleStyle';
import OuterEyeStyle from './OuterEyeStyle';

/**
 * The Style model module.
 * @module model/Style
 * @version 2.0
 */
class Style {
    /**
     * Constructs a new <code>Style</code>.
     * @alias module:model/Style
     */
    constructor() { 
        
        Style.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Style</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Style} obj Optional instance to populate.
     * @return {module:model/Style} The populated <code>Style</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Style();

            if (data.hasOwnProperty('background')) {
                obj['background'] = ApiClient.convertToType(data['background'], BackgroundStyle);
            }
            if (data.hasOwnProperty('inner_eye')) {
                obj['inner_eye'] = ApiClient.convertToType(data['inner_eye'], InnerEyeStyle);
            }
            if (data.hasOwnProperty('module')) {
                obj['module'] = ApiClient.convertToType(data['module'], ModuleStyle);
            }
            if (data.hasOwnProperty('outer_eye')) {
                obj['outer_eye'] = ApiClient.convertToType(data['outer_eye'], OuterEyeStyle);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Style</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Style</code>.
     */
    static validateJSON(data) {
        // validate the optional field `background`
        if (data['background']) { // data not null
          BackgroundStyle.validateJSON(data['background']);
        }
        // validate the optional field `inner_eye`
        if (data['inner_eye']) { // data not null
          InnerEyeStyle.validateJSON(data['inner_eye']);
        }
        // validate the optional field `module`
        if (data['module']) { // data not null
          ModuleStyle.validateJSON(data['module']);
        }
        // validate the optional field `outer_eye`
        if (data['outer_eye']) { // data not null
          OuterEyeStyle.validateJSON(data['outer_eye']);
        }

        return true;
    }


}



/**
 * `background` property allows you to select color of the background of the generated QR Code.
 * @member {module:model/BackgroundStyle} background
 */
Style.prototype['background'] = undefined;

/**
 * `inner_eye` property allows you to select shape and color of the inner eyes of the generated QR Code.
 * @member {module:model/InnerEyeStyle} inner_eye
 */
Style.prototype['inner_eye'] = undefined;

/**
 * `module` property allows you to select shape and color of the modules of the generated QR Code.
 * @member {module:model/ModuleStyle} module
 */
Style.prototype['module'] = undefined;

/**
 * `outer_eye` property allows you to select shape and color of the outer eyes of the generated QR Code.
 * @member {module:model/OuterEyeStyle} outer_eye
 */
Style.prototype['outer_eye'] = undefined;






export default Style;

