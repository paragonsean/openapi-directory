/**
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PdfWriteStringOptions from './PdfWriteStringOptions';

/**
 * The PdfWriteStringRequestDto model module.
 * @module model/PdfWriteStringRequestDto
 * @version v1
 */
class PdfWriteStringRequestDto {
    /**
     * Constructs a new <code>PdfWriteStringRequestDto</code>.
     * The request dto object to write a string on pdf page
     * @alias module:model/PdfWriteStringRequestDto
     */
    constructor() { 
        
        PdfWriteStringRequestDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PdfWriteStringRequestDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PdfWriteStringRequestDto} obj Optional instance to populate.
     * @return {module:model/PdfWriteStringRequestDto} The populated <code>PdfWriteStringRequestDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PdfWriteStringRequestDto();

            if (data.hasOwnProperty('fontFileBase64String')) {
                obj['fontFileBase64String'] = ApiClient.convertToType(data['fontFileBase64String'], 'String');
            }
            if (data.hasOwnProperty('options')) {
                obj['options'] = PdfWriteStringOptions.constructFromObject(data['options']);
            }
            if (data.hasOwnProperty('pdfFileBase64String')) {
                obj['pdfFileBase64String'] = ApiClient.convertToType(data['pdfFileBase64String'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PdfWriteStringRequestDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PdfWriteStringRequestDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['fontFileBase64String'] && !(typeof data['fontFileBase64String'] === 'string' || data['fontFileBase64String'] instanceof String)) {
            throw new Error("Expected the field `fontFileBase64String` to be a primitive type in the JSON string but got " + data['fontFileBase64String']);
        }
        // validate the optional field `options`
        if (data['options']) { // data not null
          PdfWriteStringOptions.validateJSON(data['options']);
        }
        // ensure the json data is a string
        if (data['pdfFileBase64String'] && !(typeof data['pdfFileBase64String'] === 'string' || data['pdfFileBase64String'] instanceof String)) {
            throw new Error("Expected the field `pdfFileBase64String` to be a primitive type in the JSON string but got " + data['pdfFileBase64String']);
        }

        return true;
    }


}



/**
 * System fonts are available, but you can provide your own font file to be embedded in the pdf document. Send font as Base64 encoded string.
 * @member {String} fontFileBase64String
 */
PdfWriteStringRequestDto.prototype['fontFileBase64String'] = undefined;

/**
 * @member {module:model/PdfWriteStringOptions} options
 */
PdfWriteStringRequestDto.prototype['options'] = undefined;

/**
 * The pdf file to add text to, as Base64 encoded string.
 * @member {String} pdfFileBase64String
 */
PdfWriteStringRequestDto.prototype['pdfFileBase64String'] = undefined;






export default PdfWriteStringRequestDto;

