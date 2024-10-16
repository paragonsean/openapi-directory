/**
 * Bufferapp
 * Social media management for marketers and agencies
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ProfilesInnerSchedulesInner model module.
 * @module model/ProfilesInnerSchedulesInner
 * @version 1
 */
class ProfilesInnerSchedulesInner {
    /**
     * Constructs a new <code>ProfilesInnerSchedulesInner</code>.
     * @alias module:model/ProfilesInnerSchedulesInner
     */
    constructor() { 
        
        ProfilesInnerSchedulesInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ProfilesInnerSchedulesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ProfilesInnerSchedulesInner} obj Optional instance to populate.
     * @return {module:model/ProfilesInnerSchedulesInner} The populated <code>ProfilesInnerSchedulesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ProfilesInnerSchedulesInner();

            if (data.hasOwnProperty('days')) {
                obj['days'] = ApiClient.convertToType(data['days'], ['String']);
            }
            if (data.hasOwnProperty('times')) {
                obj['times'] = ApiClient.convertToType(data['times'], [Object]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ProfilesInnerSchedulesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ProfilesInnerSchedulesInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['days'])) {
            throw new Error("Expected the field `days` to be an array in the JSON data but got " + data['days']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['times'])) {
            throw new Error("Expected the field `times` to be an array in the JSON data but got " + data['times']);
        }

        return true;
    }


}



/**
 * @member {Array.<String>} days
 */
ProfilesInnerSchedulesInner.prototype['days'] = undefined;

/**
 * @member {Array.<Object>} times
 */
ProfilesInnerSchedulesInner.prototype['times'] = undefined;






export default ProfilesInnerSchedulesInner;

