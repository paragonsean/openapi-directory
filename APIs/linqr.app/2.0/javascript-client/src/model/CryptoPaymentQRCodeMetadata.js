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
import CryptoPaymentData from './CryptoPaymentData';
import EmbeddedImageMultipart from './EmbeddedImageMultipart';
import OutputFile from './OutputFile';
import SizeMultipart from './SizeMultipart';
import Style from './Style';

/**
 * The CryptoPaymentQRCodeMetadata model module.
 * @module model/CryptoPaymentQRCodeMetadata
 * @version 2.0
 */
class CryptoPaymentQRCodeMetadata {
    /**
     * Constructs a new <code>CryptoPaymentQRCodeMetadata</code>.
     * @alias module:model/CryptoPaymentQRCodeMetadata
     * @param data {module:model/CryptoPaymentData} `data` property allows you to specify cryptocurrency payment parameters.
     */
    constructor(data) { 
        
        CryptoPaymentQRCodeMetadata.initialize(this, data);
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
     * Constructs a <code>CryptoPaymentQRCodeMetadata</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CryptoPaymentQRCodeMetadata} obj Optional instance to populate.
     * @return {module:model/CryptoPaymentQRCodeMetadata} The populated <code>CryptoPaymentQRCodeMetadata</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CryptoPaymentQRCodeMetadata();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], CryptoPaymentData);
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
     * Validates the JSON data with respect to <code>CryptoPaymentQRCodeMetadata</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CryptoPaymentQRCodeMetadata</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CryptoPaymentQRCodeMetadata.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `data`
        if (data['data']) { // data not null
          CryptoPaymentData.validateJSON(data['data']);
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

CryptoPaymentQRCodeMetadata.RequiredProperties = ["data"];

/**
 * `data` property allows you to specify cryptocurrency payment parameters.
 * @member {module:model/CryptoPaymentData} data
 */
CryptoPaymentQRCodeMetadata.prototype['data'] = undefined;

/**
 * `image` property allows you to set parameters of a custom image (e.g. your company logo, icon etc.) placed in the center of the generated QR Code.
 * @member {module:model/EmbeddedImageMultipart} image
 */
CryptoPaymentQRCodeMetadata.prototype['image'] = undefined;

/**
 * `output` property allows you to specify the name and extension (type) of the file returned by the API
 * @member {module:model/OutputFile} output
 */
CryptoPaymentQRCodeMetadata.prototype['output'] = undefined;

/**
 * `size` property allows you to set the values that define the sizes of the generated QR Code.
 * @member {module:model/SizeMultipart} size
 */
CryptoPaymentQRCodeMetadata.prototype['size'] = undefined;

/**
 * `style` property allows you to select the appearance parameters of the modules and eyes of the generated QR Code.  All color specifications can be defined via: * CSS3 name: `Black`, `azure`, ... * hex value: `0x000`, `#FFFFFF`, `7fffd4`, ... * RGB/RGBA strings: `rgb(255, 255, 255)`, `rgba(255, 255, 255, 0.5)`, ... * HSL strings: `hsl(270, 60%, 70%)`, `hsl(270, 60%, 70%, .5)`, ...  Color values can be obtained from any online color picker like <a href=\"https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Colors/Color_picker_tool\" rel=\"noopener noreferrer\" target=\"_blank\" >developer.mozilla.org</a>.
 * @member {module:model/Style} style
 */
CryptoPaymentQRCodeMetadata.prototype['style'] = undefined;






export default CryptoPaymentQRCodeMetadata;

