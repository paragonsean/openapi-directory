/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import WannabeEnv from './WannabeEnv';

/**
 * The LinkedAppEnv model module.
 * @module model/LinkedAppEnv
 * @version 1.0.0
 */
class LinkedAppEnv {
    /**
     * Constructs a new <code>LinkedAppEnv</code>.
     * @alias module:model/LinkedAppEnv
     * @param appId {String} 
     * @param appName {String} 
     * @param env {Array.<module:model/WannabeEnv>} 
     */
    constructor(appId, appName, env) { 
        
        LinkedAppEnv.initialize(this, appId, appName, env);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, appId, appName, env) { 
        obj['app_id'] = appId;
        obj['app_name'] = appName;
        obj['env'] = env;
    }

    /**
     * Constructs a <code>LinkedAppEnv</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LinkedAppEnv} obj Optional instance to populate.
     * @return {module:model/LinkedAppEnv} The populated <code>LinkedAppEnv</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LinkedAppEnv();

            if (data.hasOwnProperty('app_id')) {
                obj['app_id'] = ApiClient.convertToType(data['app_id'], 'String');
            }
            if (data.hasOwnProperty('app_name')) {
                obj['app_name'] = ApiClient.convertToType(data['app_name'], 'String');
            }
            if (data.hasOwnProperty('env')) {
                obj['env'] = ApiClient.convertToType(data['env'], [WannabeEnv]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LinkedAppEnv</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LinkedAppEnv</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of LinkedAppEnv.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['app_id'] && !(typeof data['app_id'] === 'string' || data['app_id'] instanceof String)) {
            throw new Error("Expected the field `app_id` to be a primitive type in the JSON string but got " + data['app_id']);
        }
        // ensure the json data is a string
        if (data['app_name'] && !(typeof data['app_name'] === 'string' || data['app_name'] instanceof String)) {
            throw new Error("Expected the field `app_name` to be a primitive type in the JSON string but got " + data['app_name']);
        }
        if (data['env']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['env'])) {
                throw new Error("Expected the field `env` to be an array in the JSON data but got " + data['env']);
            }
            // validate the optional field `env` (array)
            for (const item of data['env']) {
                WannabeEnv.validateJSON(item);
            };
        }

        return true;
    }


}

LinkedAppEnv.RequiredProperties = ["app_id", "app_name", "env"];

/**
 * @member {String} app_id
 */
LinkedAppEnv.prototype['app_id'] = undefined;

/**
 * @member {String} app_name
 */
LinkedAppEnv.prototype['app_name'] = undefined;

/**
 * @member {Array.<module:model/WannabeEnv>} env
 */
LinkedAppEnv.prototype['env'] = undefined;






export default LinkedAppEnv;

