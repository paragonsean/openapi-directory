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
 * The TeamsUpdateRequest model module.
 * @module model/TeamsUpdateRequest
 * @version v0.1
 */
class TeamsUpdateRequest {
    /**
     * Constructs a new <code>TeamsUpdateRequest</code>.
     * @alias module:model/TeamsUpdateRequest
     * @param displayName {String} The new display name of the team
     */
    constructor(displayName) { 
        
        TeamsUpdateRequest.initialize(this, displayName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, displayName) { 
        obj['display_name'] = displayName;
    }

    /**
     * Constructs a <code>TeamsUpdateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TeamsUpdateRequest} obj Optional instance to populate.
     * @return {module:model/TeamsUpdateRequest} The populated <code>TeamsUpdateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TeamsUpdateRequest();

            if (data.hasOwnProperty('display_name')) {
                obj['display_name'] = ApiClient.convertToType(data['display_name'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TeamsUpdateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TeamsUpdateRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of TeamsUpdateRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['display_name'] && !(typeof data['display_name'] === 'string' || data['display_name'] instanceof String)) {
            throw new Error("Expected the field `display_name` to be a primitive type in the JSON string but got " + data['display_name']);
        }

        return true;
    }


}

TeamsUpdateRequest.RequiredProperties = ["display_name"];

/**
 * The new display name of the team
 * @member {String} display_name
 */
TeamsUpdateRequest.prototype['display_name'] = undefined;






export default TeamsUpdateRequest;

