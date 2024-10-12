/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The FileUpload model module.
 * @module model/FileUpload
 * @version 1.0.0
 */
class FileUpload {
    /**
     * Constructs a new <code>FileUpload</code>.
     * @alias module:model/FileUpload
     */
    constructor() { 
        
        FileUpload.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>FileUpload</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/FileUpload} obj Optional instance to populate.
     * @return {module:model/FileUpload} The populated <code>FileUpload</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new FileUpload();

            if (data.hasOwnProperty('Content-Type')) {
                obj['Content-Type'] = ApiClient.convertToType(data['Content-Type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>FileUpload</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>FileUpload</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Content-Type'] && !(typeof data['Content-Type'] === 'string' || data['Content-Type'] instanceof String)) {
            throw new Error("Expected the field `Content-Type` to be a primitive type in the JSON string but got " + data['Content-Type']);
        }

        return true;
    }


}



/**
 * The mime type of the file e.g. image/jpg, image/jpeg, image/png, application/pdf.
 * @member {String} Content-Type
 */
FileUpload.prototype['Content-Type'] = undefined;






export default FileUpload;

