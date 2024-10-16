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
 * The SymbolUploadLocation model module.
 * @module model/SymbolUploadLocation
 * @version v0.1
 */
class SymbolUploadLocation {
    /**
     * Constructs a new <code>SymbolUploadLocation</code>.
     * Location for downloading symbol upload
     * @alias module:model/SymbolUploadLocation
     * @param uri {String} 
     */
    constructor(uri) { 
        
        SymbolUploadLocation.initialize(this, uri);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, uri) { 
        obj['uri'] = uri;
    }

    /**
     * Constructs a <code>SymbolUploadLocation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SymbolUploadLocation} obj Optional instance to populate.
     * @return {module:model/SymbolUploadLocation} The populated <code>SymbolUploadLocation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SymbolUploadLocation();

            if (data.hasOwnProperty('uri')) {
                obj['uri'] = ApiClient.convertToType(data['uri'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SymbolUploadLocation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SymbolUploadLocation</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SymbolUploadLocation.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['uri'] && !(typeof data['uri'] === 'string' || data['uri'] instanceof String)) {
            throw new Error("Expected the field `uri` to be a primitive type in the JSON string but got " + data['uri']);
        }

        return true;
    }


}

SymbolUploadLocation.RequiredProperties = ["uri"];

/**
 * @member {String} uri
 */
SymbolUploadLocation.prototype['uri'] = undefined;






export default SymbolUploadLocation;

