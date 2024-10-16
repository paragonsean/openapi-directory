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
import LegacyCodePushReleaseResponsePackage from './LegacyCodePushReleaseResponsePackage';

/**
 * The LegacyDeployment model module.
 * @module model/LegacyDeployment
 * @version v0.1
 */
class LegacyDeployment {
    /**
     * Constructs a new <code>LegacyDeployment</code>.
     * @alias module:model/LegacyDeployment
     * @param name {String} Updated deployment name
     */
    constructor(name) { 
        
        LegacyDeployment.initialize(this, name);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name) { 
        obj['name'] = name;
    }

    /**
     * Constructs a <code>LegacyDeployment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LegacyDeployment} obj Optional instance to populate.
     * @return {module:model/LegacyDeployment} The populated <code>LegacyDeployment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LegacyDeployment();

            if (data.hasOwnProperty('createdTime')) {
                obj['createdTime'] = ApiClient.convertToType(data['createdTime'], 'Number');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('package')) {
                obj['package'] = LegacyCodePushReleaseResponsePackage.constructFromObject(data['package']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LegacyDeployment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LegacyDeployment</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of LegacyDeployment.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `package`
        if (data['package']) { // data not null
          LegacyCodePushReleaseResponsePackage.validateJSON(data['package']);
        }

        return true;
    }


}

LegacyDeployment.RequiredProperties = ["name"];

/**
 * Time at which the deployment was created as a Unix timestamp.
 * @member {Number} createdTime
 */
LegacyDeployment.prototype['createdTime'] = undefined;

/**
 * The ID of the deployment (internal use only).
 * @member {String} id
 */
LegacyDeployment.prototype['id'] = undefined;

/**
 * Deployment key (aka Deployment Id)
 * @member {String} key
 */
LegacyDeployment.prototype['key'] = undefined;

/**
 * Updated deployment name
 * @member {String} name
 */
LegacyDeployment.prototype['name'] = undefined;

/**
 * @member {module:model/LegacyCodePushReleaseResponsePackage} package
 */
LegacyDeployment.prototype['package'] = undefined;






export default LegacyDeployment;

