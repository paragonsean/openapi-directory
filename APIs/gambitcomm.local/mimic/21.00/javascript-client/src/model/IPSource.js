/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The IPSource model module.
 * @module model/IPSource
 * @version 21.00
 */
class IPSource {
    /**
     * Constructs a new <code>IPSource</code>.
     * @alias module:model/IPSource
     */
    constructor() { 
        
        IPSource.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IPSource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IPSource} obj Optional instance to populate.
     * @return {module:model/IPSource} The populated <code>IPSource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IPSource();

            if (data.hasOwnProperty('IP')) {
                obj['IP'] = ApiClient.convertToType(data['IP'], 'String');
            }
            if (data.hasOwnProperty('port')) {
                obj['port'] = ApiClient.convertToType(data['port'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IPSource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IPSource</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['IP'] && !(typeof data['IP'] === 'string' || data['IP'] instanceof String)) {
            throw new Error("Expected the field `IP` to be a primitive type in the JSON string but got " + data['IP']);
        }

        return true;
    }


}



/**
 * @member {String} IP
 */
IPSource.prototype['IP'] = undefined;

/**
 * @member {Number} port
 */
IPSource.prototype['port'] = undefined;






export default IPSource;

