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
 * The CrashGroupsUpdateRequest model module.
 * @module model/CrashGroupsUpdateRequest
 * @version v0.1
 */
class CrashGroupsUpdateRequest {
    /**
     * Constructs a new <code>CrashGroupsUpdateRequest</code>.
     * @alias module:model/CrashGroupsUpdateRequest
     */
    constructor() { 
        
        CrashGroupsUpdateRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CrashGroupsUpdateRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CrashGroupsUpdateRequest} obj Optional instance to populate.
     * @return {module:model/CrashGroupsUpdateRequest} The populated <code>CrashGroupsUpdateRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CrashGroupsUpdateRequest();

            if (data.hasOwnProperty('annotation')) {
                obj['annotation'] = ApiClient.convertToType(data['annotation'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CrashGroupsUpdateRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CrashGroupsUpdateRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['annotation'] && !(typeof data['annotation'] === 'string' || data['annotation'] instanceof String)) {
            throw new Error("Expected the field `annotation` to be a primitive type in the JSON string but got " + data['annotation']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * @member {String} annotation
 */
CrashGroupsUpdateRequest.prototype['annotation'] = undefined;

/**
 * @member {module:model/CrashGroupsUpdateRequest.StatusEnum} status
 */
CrashGroupsUpdateRequest.prototype['status'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
CrashGroupsUpdateRequest['StatusEnum'] = {

    /**
     * value: "open"
     * @const
     */
    "open": "open",

    /**
     * value: "closed"
     * @const
     */
    "closed": "closed",

    /**
     * value: "ignored"
     * @const
     */
    "ignored": "ignored"
};



export default CrashGroupsUpdateRequest;

