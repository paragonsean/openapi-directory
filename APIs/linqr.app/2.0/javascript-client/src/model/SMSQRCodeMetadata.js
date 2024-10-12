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
import EmbeddedImageMultipart from './EmbeddedImageMultipart';
import OutputFile from './OutputFile';
import SMSData from './SMSData';
import SizeMultipart from './SizeMultipart';
import Style from './Style';

/**
 * The SMSQRCodeMetadata model module.
 * @module model/SMSQRCodeMetadata
 * @version 2.0
 */
class SMSQRCodeMetadata {
    /**
     * Constructs a new <code>SMSQRCodeMetadata</code>.
     * @alias module:model/SMSQRCodeMetadata
     * @param data {module:model/SMSData} `data` property allows you to specify SMS template.
     */
    constructor(data) { 
        
        SMSQRCodeMetadata.initialize(this, data);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, data) { 
        obj['data'] = data;
    }

    /**
     * Constructs a <code>SMSQRCodeMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SMSQRCodeMetadata} obj Optional instance to populate.
     * @return {module:model/SMSQRCodeMetadata} The populated <code>SMSQRCodeMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SMSQRCodeMetadata();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], SMSData);
            }
            if (data.hasOwnProperty('image')) {
                obj['image'] = ApiClient.convertToType(data['image'], EmbeddedImageMultipart);
            }
            if (data.hasOwnProperty('output')) {
                obj['output'] = ApiClient.convertToType(data['output'], OutputFile);
            }
            if (data.hasOwnProperty('size')) {
                obj['size'] = ApiClient.convertToType(data['size'], SizeMultipart);
            }
            if (data.hasOwnProperty('style')) {
                obj['style'] = ApiClient.convertToType(data['style'], Style);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SMSQRCodeMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SMSQRCodeMetadata</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SMSQRCodeMetadata.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          SMSData.validateJSON(data['data']);
        }
        // validate the optional field `image`
        if (data['image']) { // data not null
          EmbeddedImageMultipart.validateJSON(data['image']);
        }
        // validate the optional field `output`
        if (data['output']) { // data not null
          OutputFile.validateJSON(data['output']);
        }
        // validate the optional field `size`
        if (data['size']) { // data not null
          SizeMultipart.validateJSON(data['size']);
        }
        // validate the optional field `style`
        if (data['style']) { // data not null
          Style.validateJSON(data['style']);
        }

        return true;
    }


}

SMSQRCodeMetadata.RequiredProperties = ["data"];

/**
 * `data` property allows you to specify SMS template.
 * @member {module:model/SMSData} data
 */
SMSQRCodeMetadata.prototype['data'] = undefined;

/**
 * `image` property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.
 * @member {module:model/EmbeddedImageMultipart} image
 */
SMSQRCodeMetadata.prototype['image'] = undefined;

/**
 * `output` property allows you to specify the name and extension (type) of the file returned by the API
 * @member {module:model/OutputFile} output
 */
SMSQRCodeMetadata.prototype['output'] = undefined;

/**
 * `size` property allows you to set the values that define the sizes of the generated QR Code.
 * @member {module:model/SizeMultipart} size
 */
SMSQRCodeMetadata.prototype['size'] = undefined;

/**
 * `style` property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: `Black`, `azure`, ... * hex value: `0x000`, `#FFFFFF`, `7fffd4`, ... * RGB/RGBA strings: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`, ... * HSL strings: `hsl(270, 60%, 70%)`, `hsl(270, 60%, 70%, .5)`, ...  Color values can be obtained from any online color picker like <a href=\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\" rel=\"noopener noreferrer\" target=\"_blank\" >developer.mozilla.org</a>.
 * @member {module:model/Style} style
 */
SMSQRCodeMetadata.prototype['style'] = undefined;






export default SMSQRCodeMetadata;

