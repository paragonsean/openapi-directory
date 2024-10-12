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

/**
 * The PdfConcatenationRequestDto model module.
 * @module model/PdfConcatenationRequestDto
 * @version v1
 */
class PdfConcatenationRequestDto {
    /**
     * Constructs a new <code>PdfConcatenationRequestDto</code>.
     * Request to concatenate a list of Pdf documents to a single Pdf document.
     * @alias module:model/PdfConcatenationRequestDto
     */
    constructor() { 
        
        PdfConcatenationRequestDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PdfConcatenationRequestDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PdfConcatenationRequestDto} obj Optional instance to populate.
     * @return {module:model/PdfConcatenationRequestDto} The populated <code>PdfConcatenationRequestDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PdfConcatenationRequestDto();

            if (data.hasOwnProperty('pdfDocumentsAsBase64String')) {
                obj['pdfDocumentsAsBase64String'] = ApiClient.convertToType(data['pdfDocumentsAsBase64String'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PdfConcatenationRequestDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PdfConcatenationRequestDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['pdfDocumentsAsBase64String'])) {
            throw new Error("Expected the field `pdfDocumentsAsBase64String` to be an array in the JSON data but got " + data['pdfDocumentsAsBase64String']);
        }

        return true;
    }


}



/**
 * The list of Pdf documents encoded as Base64 strings.
 * @member {Array.<String>} pdfDocumentsAsBase64String
 */
PdfConcatenationRequestDto.prototype['pdfDocumentsAsBase64String'] = undefined;






export default PdfConcatenationRequestDto;

