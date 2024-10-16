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
 * The DiagnosticIdResponse model module.
 * @module model/DiagnosticIdResponse
 * @version v0.1
 */
class DiagnosticIdResponse {
    /**
     * Constructs a new <code>DiagnosticIdResponse</code>.
     * The diagnostic id for the given publish action
     * @alias module:model/DiagnosticIdResponse
     */
    constructor() { 
        
        DiagnosticIdResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DiagnosticIdResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DiagnosticIdResponse} obj Optional instance to populate.
     * @return {module:model/DiagnosticIdResponse} The populated <code>DiagnosticIdResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DiagnosticIdResponse();

            if (data.hasOwnProperty('diagnostic_id')) {
                obj['diagnostic_id'] = ApiClient.convertToType(data['diagnostic_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DiagnosticIdResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DiagnosticIdResponse</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['diagnostic_id'] && !(typeof data['diagnostic_id'] === 'string' || data['diagnostic_id'] instanceof String)) {
            throw new Error("Expected the field `diagnostic_id` to be a primitive type in the JSON string but got " + data['diagnostic_id']);
        }

        return true;
    }


}



/**
 * diagnostic id
 * @member {String} diagnostic_id
 */
DiagnosticIdResponse.prototype['diagnostic_id'] = undefined;






export default DiagnosticIdResponse;

