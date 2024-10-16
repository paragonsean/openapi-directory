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
 * The AppleMappingTestFlightGroups200ResponseInner model module.
 * @module model/AppleMappingTestFlightGroups200ResponseInner
 * @version v0.1
 */
class AppleMappingTestFlightGroups200ResponseInner {
    /**
     * Constructs a new <code>AppleMappingTestFlightGroups200ResponseInner</code>.
     * Apple Test Flight Groups Response Type
     * @alias module:model/AppleMappingTestFlightGroups200ResponseInner
     */
    constructor() { 
        
        AppleMappingTestFlightGroups200ResponseInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AppleMappingTestFlightGroups200ResponseInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AppleMappingTestFlightGroups200ResponseInner} obj Optional instance to populate.
     * @return {module:model/AppleMappingTestFlightGroups200ResponseInner} The populated <code>AppleMappingTestFlightGroups200ResponseInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AppleMappingTestFlightGroups200ResponseInner();

            if (data.hasOwnProperty('appleId')) {
                obj['appleId'] = ApiClient.convertToType(data['appleId'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('providerId')) {
                obj['providerId'] = ApiClient.convertToType(data['providerId'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AppleMappingTestFlightGroups200ResponseInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AppleMappingTestFlightGroups200ResponseInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }

        return true;
    }


}



/**
 * apple id of the group.
 * @member {Number} appleId
 */
AppleMappingTestFlightGroups200ResponseInner.prototype['appleId'] = undefined;

/**
 * id of the group.
 * @member {String} id
 */
AppleMappingTestFlightGroups200ResponseInner.prototype['id'] = undefined;

/**
 * name of the group.
 * @member {String} name
 */
AppleMappingTestFlightGroups200ResponseInner.prototype['name'] = undefined;

/**
 * provider id of the group.
 * @member {Number} providerId
 */
AppleMappingTestFlightGroups200ResponseInner.prototype['providerId'] = undefined;






export default AppleMappingTestFlightGroups200ResponseInner;

