/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The Version model module.
 * @module model/Version
 * @version 0.4.27
 */
class Version {
    /**
     * Constructs a new <code>Version</code>.
     * @alias module:model/Version
     */
    constructor() { 
        
        Version.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Version</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Version} obj Optional instance to populate.
     * @return {module:model/Version} The populated <code>Version</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Version();

            if (data.hasOwnProperty('build')) {
                obj['build'] = ApiClient.convertToType(data['build'], 'String');
            }
            if (data.hasOwnProperty('commitsha')) {
                obj['commitsha'] = ApiClient.convertToType(data['commitsha'], 'String');
            }
            if (data.hasOwnProperty('latest')) {
                obj['latest'] = ApiClient.convertToType(data['latest'], 'String');
            }
            if (data.hasOwnProperty('outdated')) {
                obj['outdated'] = ApiClient.convertToType(data['outdated'], 'Boolean');
            }
            if (data.hasOwnProperty('release_channel')) {
                obj['release_channel'] = ApiClient.convertToType(data['release_channel'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Version</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Version</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['build'] && !(typeof data['build'] === 'string' || data['build'] instanceof String)) {
            throw new Error("Expected the field `build` to be a primitive type in the JSON string but got " + data['build']);
        }
        // ensure the json data is a string
        if (data['commitsha'] && !(typeof data['commitsha'] === 'string' || data['commitsha'] instanceof String)) {
            throw new Error("Expected the field `commitsha` to be a primitive type in the JSON string but got " + data['commitsha']);
        }
        // ensure the json data is a string
        if (data['latest'] && !(typeof data['latest'] === 'string' || data['latest'] instanceof String)) {
            throw new Error("Expected the field `latest` to be a primitive type in the JSON string but got " + data['latest']);
        }
        // ensure the json data is a string
        if (data['release_channel'] && !(typeof data['release_channel'] === 'string' || data['release_channel'] instanceof String)) {
            throw new Error("Expected the field `release_channel` to be a primitive type in the JSON string but got " + data['release_channel']);
        }

        return true;
    }


}



/**
 * @member {String} build
 */
Version.prototype['build'] = undefined;

/**
 * @member {String} commitsha
 */
Version.prototype['commitsha'] = undefined;

/**
 * @member {String} latest
 */
Version.prototype['latest'] = undefined;

/**
 * @member {Boolean} outdated
 */
Version.prototype['outdated'] = undefined;

/**
 * @member {String} release_channel
 */
Version.prototype['release_channel'] = undefined;






export default Version;

