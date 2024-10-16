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
 * The AvailableVersions model module.
 * @module model/AvailableVersions
 * @version v0.1
 */
class AvailableVersions {
    /**
     * Constructs a new <code>AvailableVersions</code>.
     * @alias module:model/AvailableVersions
     */
    constructor() { 
        
        AvailableVersions.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>AvailableVersions</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailableVersions} obj Optional instance to populate.
     * @return {module:model/AvailableVersions} The populated <code>AvailableVersions</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailableVersions();

            if (data.hasOwnProperty('total_count')) {
                obj['total_count'] = ApiClient.convertToType(data['total_count'], 'Number');
            }
            if (data.hasOwnProperty('versions')) {
                obj['versions'] = ApiClient.convertToType(data['versions'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailableVersions</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailableVersions</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['versions'])) {
            throw new Error("Expected the field `versions` to be an array in the JSON data but got " + data['versions']);
        }

        return true;
    }


}



/**
 * The full number of versions across all pages.
 * @member {Number} total_count
 */
AvailableVersions.prototype['total_count'] = undefined;

/**
 * List of available versions.
 * @member {Array.<String>} versions
 */
AvailableVersions.prototype['versions'] = undefined;






export default AvailableVersions;

