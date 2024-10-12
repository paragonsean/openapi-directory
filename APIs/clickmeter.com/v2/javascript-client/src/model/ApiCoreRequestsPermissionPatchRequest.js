/**
 * ClickMeter API
 * Api dashboard for ClickMeter API
 *
 * The version of the OpenAPI document: v2
 * Contact: api@clickmeter.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApiCoreRequestsPermissionPatchRequest model module.
 * @module model/ApiCoreRequestsPermissionPatchRequest
 * @version v2
 */
class ApiCoreRequestsPermissionPatchRequest {
    /**
     * Constructs a new <code>ApiCoreRequestsPermissionPatchRequest</code>.
     * @alias module:model/ApiCoreRequestsPermissionPatchRequest
     */
    constructor() { 
        
        ApiCoreRequestsPermissionPatchRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApiCoreRequestsPermissionPatchRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApiCoreRequestsPermissionPatchRequest} obj Optional instance to populate.
     * @return {module:model/ApiCoreRequestsPermissionPatchRequest} The populated <code>ApiCoreRequestsPermissionPatchRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApiCoreRequestsPermissionPatchRequest();

            if (data.hasOwnProperty('Action')) {
                obj['Action'] = ApiClient.convertToType(data['Action'], 'String');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('Verb')) {
                obj['Verb'] = ApiClient.convertToType(data['Verb'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApiCoreRequestsPermissionPatchRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApiCoreRequestsPermissionPatchRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['Action'] && !(typeof data['Action'] === 'string' || data['Action'] instanceof String)) {
            throw new Error("Expected the field `Action` to be a primitive type in the JSON string but got " + data['Action']);
        }
        // ensure the json data is a string
        if (data['Verb'] && !(typeof data['Verb'] === 'string' || data['Verb'] instanceof String)) {
            throw new Error("Expected the field `Verb` to be a primitive type in the JSON string but got " + data['Verb']);
        }

        return true;
    }


}



/**
 * @member {String} Action
 */
ApiCoreRequestsPermissionPatchRequest.prototype['Action'] = undefined;

/**
 * @member {Number} Id
 */
ApiCoreRequestsPermissionPatchRequest.prototype['Id'] = undefined;

/**
 * @member {String} Verb
 */
ApiCoreRequestsPermissionPatchRequest.prototype['Verb'] = undefined;






export default ApiCoreRequestsPermissionPatchRequest;

