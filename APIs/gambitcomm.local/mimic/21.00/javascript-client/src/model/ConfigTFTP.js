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
 * The ConfigTFTP model module.
 * @module model/ConfigTFTP
 * @version 21.00
 */
class ConfigTFTP {
    /**
     * Constructs a new <code>ConfigTFTP</code>.
     * @alias module:model/ConfigTFTP
     */
    constructor() { 
        
        ConfigTFTP.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ConfigTFTP</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConfigTFTP} obj Optional instance to populate.
     * @return {module:model/ConfigTFTP} The populated <code>ConfigTFTP</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConfigTFTP();

            if (data.hasOwnProperty('cache')) {
                obj['cache'] = ApiClient.convertToType(data['cache'], 'Number');
            }
            if (data.hasOwnProperty('client')) {
                obj['client'] = ApiClient.convertToType(data['client'], 'String');
            }
            if (data.hasOwnProperty('dstfile')) {
                obj['dstfile'] = ApiClient.convertToType(data['dstfile'], 'String');
            }
            if (data.hasOwnProperty('mode')) {
                obj['mode'] = ApiClient.convertToType(data['mode'], 'String');
            }
            if (data.hasOwnProperty('port')) {
                obj['port'] = ApiClient.convertToType(data['port'], 'Number');
            }
            if (data.hasOwnProperty('retries')) {
                obj['retries'] = ApiClient.convertToType(data['retries'], 'Number');
            }
            if (data.hasOwnProperty('script')) {
                obj['script'] = ApiClient.convertToType(data['script'], 'String');
            }
            if (data.hasOwnProperty('server')) {
                obj['server'] = ApiClient.convertToType(data['server'], 'String');
            }
            if (data.hasOwnProperty('srcfile')) {
                obj['srcfile'] = ApiClient.convertToType(data['srcfile'], 'String');
            }
            if (data.hasOwnProperty('timeout')) {
                obj['timeout'] = ApiClient.convertToType(data['timeout'], 'Number');
            }
            if (data.hasOwnProperty('trace')) {
                obj['trace'] = ApiClient.convertToType(data['trace'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConfigTFTP</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConfigTFTP</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['client'] && !(typeof data['client'] === 'string' || data['client'] instanceof String)) {
            throw new Error("Expected the field `client` to be a primitive type in the JSON string but got " + data['client']);
        }
        // ensure the json data is a string
        if (data['dstfile'] && !(typeof data['dstfile'] === 'string' || data['dstfile'] instanceof String)) {
            throw new Error("Expected the field `dstfile` to be a primitive type in the JSON string but got " + data['dstfile']);
        }
        // ensure the json data is a string
        if (data['mode'] && !(typeof data['mode'] === 'string' || data['mode'] instanceof String)) {
            throw new Error("Expected the field `mode` to be a primitive type in the JSON string but got " + data['mode']);
        }
        // ensure the json data is a string
        if (data['script'] && !(typeof data['script'] === 'string' || data['script'] instanceof String)) {
            throw new Error("Expected the field `script` to be a primitive type in the JSON string but got " + data['script']);
        }
        // ensure the json data is a string
        if (data['server'] && !(typeof data['server'] === 'string' || data['server'] instanceof String)) {
            throw new Error("Expected the field `server` to be a primitive type in the JSON string but got " + data['server']);
        }
        // ensure the json data is a string
        if (data['srcfile'] && !(typeof data['srcfile'] === 'string' || data['srcfile'] instanceof String)) {
            throw new Error("Expected the field `srcfile` to be a primitive type in the JSON string but got " + data['srcfile']);
        }
        // ensure the json data is a string
        if (data['trace'] && !(typeof data['trace'] === 'string' || data['trace'] instanceof String)) {
            throw new Error("Expected the field `trace` to be a primitive type in the JSON string but got " + data['trace']);
        }

        return true;
    }


}



/**
 * @member {Number} cache
 */
ConfigTFTP.prototype['cache'] = undefined;

/**
 * @member {String} client
 */
ConfigTFTP.prototype['client'] = undefined;

/**
 * @member {String} dstfile
 */
ConfigTFTP.prototype['dstfile'] = undefined;

/**
 * @member {String} mode
 */
ConfigTFTP.prototype['mode'] = undefined;

/**
 * @member {Number} port
 */
ConfigTFTP.prototype['port'] = undefined;

/**
 * @member {Number} retries
 */
ConfigTFTP.prototype['retries'] = undefined;

/**
 * @member {String} script
 */
ConfigTFTP.prototype['script'] = undefined;

/**
 * @member {String} server
 */
ConfigTFTP.prototype['server'] = undefined;

/**
 * @member {String} srcfile
 */
ConfigTFTP.prototype['srcfile'] = undefined;

/**
 * @member {Number} timeout
 */
ConfigTFTP.prototype['timeout'] = undefined;

/**
 * @member {String} trace
 */
ConfigTFTP.prototype['trace'] = undefined;






export default ConfigTFTP;

