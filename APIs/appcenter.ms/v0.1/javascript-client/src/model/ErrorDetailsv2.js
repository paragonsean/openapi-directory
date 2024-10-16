/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ErrorDetailsv2 model module.
 * @module model/ErrorDetailsv2
 * @version v0.1
 */
class ErrorDetailsv2 {
    /**
     * Constructs a new <code>ErrorDetailsv2</code>.
     * @alias module:model/ErrorDetailsv2
     * @param code {module:model/ErrorDetailsv2.CodeEnum} 
     * @param message {String} 
     */
    constructor(code, message) { 
        
        ErrorDetailsv2.initialize(this, code, message);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, code, message) { 
        obj['code'] = code;
        obj['message'] = message;
    }

    /**
     * Constructs a <code>ErrorDetailsv2</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ErrorDetailsv2} obj Optional instance to populate.
     * @return {module:model/ErrorDetailsv2} The populated <code>ErrorDetailsv2</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ErrorDetailsv2();

            if (data.hasOwnProperty('code')) {
                obj['code'] = ApiClient.convertToType(data['code'], 'String');
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ErrorDetailsv2</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ErrorDetailsv2</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ErrorDetailsv2.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['code'] && !(typeof data['code'] === 'string' || data['code'] instanceof String)) {
            throw new Error("Expected the field `code` to be a primitive type in the JSON string but got " + data['code']);
        }
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }

        return true;
    }


}

ErrorDetailsv2.RequiredProperties = ["code", "message"];

/**
 * @member {module:model/ErrorDetailsv2.CodeEnum} code
 */
ErrorDetailsv2.prototype['code'] = undefined;

/**
 * @member {String} message
 */
ErrorDetailsv2.prototype['message'] = undefined;





/**
 * Allowed values for the <code>code</code> property.
 * @enum {String}
 * @readonly
 */
ErrorDetailsv2['CodeEnum'] = {

    /**
     * value: "BadRequest"
     * @const
     */
    "BadRequest": "BadRequest",

    /**
     * value: "Conflict"
     * @const
     */
    "Conflict": "Conflict",

    /**
     * value: "NotAcceptable"
     * @const
     */
    "NotAcceptable": "NotAcceptable",

    /**
     * value: "NotFound"
     * @const
     */
    "NotFound": "NotFound",

    /**
     * value: "InternalServerError"
     * @const
     */
    "InternalServerError": "InternalServerError",

    /**
     * value: "Unauthorized"
     * @const
     */
    "Unauthorized": "Unauthorized"
};



export default ErrorDetailsv2;

