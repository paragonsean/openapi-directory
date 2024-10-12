/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SparkMavenPackage model module.
 * @module model/SparkMavenPackage
 * @version 2019-08-01
 */
class SparkMavenPackage {
    /**
     * Constructs a new <code>SparkMavenPackage</code>.
     * @alias module:model/SparkMavenPackage
     */
    constructor() { 
        
        SparkMavenPackage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SparkMavenPackage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SparkMavenPackage} obj Optional instance to populate.
     * @return {module:model/SparkMavenPackage} The populated <code>SparkMavenPackage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SparkMavenPackage();

            if (data.hasOwnProperty('artifact')) {
                obj['artifact'] = ApiClient.convertToType(data['artifact'], 'String');
            }
            if (data.hasOwnProperty('group')) {
                obj['group'] = ApiClient.convertToType(data['group'], 'String');
            }
            if (data.hasOwnProperty('version')) {
                obj['version'] = ApiClient.convertToType(data['version'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SparkMavenPackage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SparkMavenPackage</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['artifact'] && !(typeof data['artifact'] === 'string' || data['artifact'] instanceof String)) {
            throw new Error("Expected the field `artifact` to be a primitive type in the JSON string but got " + data['artifact']);
        }
        // ensure the json data is a string
        if (data['group'] && !(typeof data['group'] === 'string' || data['group'] instanceof String)) {
            throw new Error("Expected the field `group` to be a primitive type in the JSON string but got " + data['group']);
        }
        // ensure the json data is a string
        if (data['version'] && !(typeof data['version'] === 'string' || data['version'] instanceof String)) {
            throw new Error("Expected the field `version` to be a primitive type in the JSON string but got " + data['version']);
        }

        return true;
    }


}



/**
 * @member {String} artifact
 */
SparkMavenPackage.prototype['artifact'] = undefined;

/**
 * @member {String} group
 */
SparkMavenPackage.prototype['group'] = undefined;

/**
 * @member {String} version
 */
SparkMavenPackage.prototype['version'] = undefined;






export default SparkMavenPackage;

