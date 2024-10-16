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
 * The LegacyUpdateInfoData model module.
 * @module model/LegacyUpdateInfoData
 * @version v0.1
 */
class LegacyUpdateInfoData {
    /**
     * Constructs a new <code>LegacyUpdateInfoData</code>.
     * @alias module:model/LegacyUpdateInfoData
     * @param isAvailable {Boolean} 
     */
    constructor(isAvailable) { 
        
        LegacyUpdateInfoData.initialize(this, isAvailable);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, isAvailable) { 
        obj['isAvailable'] = isAvailable;
    }

    /**
     * Constructs a <code>LegacyUpdateInfoData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/LegacyUpdateInfoData} obj Optional instance to populate.
     * @return {module:model/LegacyUpdateInfoData} The populated <code>LegacyUpdateInfoData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new LegacyUpdateInfoData();

            if (data.hasOwnProperty('appVersion')) {
                obj['appVersion'] = ApiClient.convertToType(data['appVersion'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('isDisabled')) {
                obj['isDisabled'] = ApiClient.convertToType(data['isDisabled'], 'Boolean');
            }
            if (data.hasOwnProperty('isMandatory')) {
                obj['isMandatory'] = ApiClient.convertToType(data['isMandatory'], 'Boolean');
            }
            if (data.hasOwnProperty('rollout')) {
                obj['rollout'] = ApiClient.convertToType(data['rollout'], 'Number');
            }
            if (data.hasOwnProperty('downloadURL')) {
                obj['downloadURL'] = ApiClient.convertToType(data['downloadURL'], 'String');
            }
            if (data.hasOwnProperty('isAvailable')) {
                obj['isAvailable'] = ApiClient.convertToType(data['isAvailable'], 'Boolean');
            }
            if (data.hasOwnProperty('label')) {
                obj['label'] = ApiClient.convertToType(data['label'], 'String');
            }
            if (data.hasOwnProperty('packageHash')) {
                obj['packageHash'] = ApiClient.convertToType(data['packageHash'], 'String');
            }
            if (data.hasOwnProperty('packageSize')) {
                obj['packageSize'] = ApiClient.convertToType(data['packageSize'], 'Number');
            }
            if (data.hasOwnProperty('shouldRunBinaryVersion')) {
                obj['shouldRunBinaryVersion'] = ApiClient.convertToType(data['shouldRunBinaryVersion'], 'Boolean');
            }
            if (data.hasOwnProperty('updateAppVersion')) {
                obj['updateAppVersion'] = ApiClient.convertToType(data['updateAppVersion'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>LegacyUpdateInfoData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>LegacyUpdateInfoData</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of LegacyUpdateInfoData.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['appVersion'] && !(typeof data['appVersion'] === 'string' || data['appVersion'] instanceof String)) {
            throw new Error("Expected the field `appVersion` to be a primitive type in the JSON string but got " + data['appVersion']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['downloadURL'] && !(typeof data['downloadURL'] === 'string' || data['downloadURL'] instanceof String)) {
            throw new Error("Expected the field `downloadURL` to be a primitive type in the JSON string but got " + data['downloadURL']);
        }
        // ensure the json data is a string
        if (data['label'] && !(typeof data['label'] === 'string' || data['label'] instanceof String)) {
            throw new Error("Expected the field `label` to be a primitive type in the JSON string but got " + data['label']);
        }
        // ensure the json data is a string
        if (data['packageHash'] && !(typeof data['packageHash'] === 'string' || data['packageHash'] instanceof String)) {
            throw new Error("Expected the field `packageHash` to be a primitive type in the JSON string but got " + data['packageHash']);
        }

        return true;
    }


}

LegacyUpdateInfoData.RequiredProperties = ["isAvailable"];

/**
 * @member {String} appVersion
 */
LegacyUpdateInfoData.prototype['appVersion'] = undefined;

/**
 * @member {String} description
 */
LegacyUpdateInfoData.prototype['description'] = undefined;

/**
 * @member {Boolean} isDisabled
 */
LegacyUpdateInfoData.prototype['isDisabled'] = undefined;

/**
 * @member {Boolean} isMandatory
 */
LegacyUpdateInfoData.prototype['isMandatory'] = undefined;

/**
 * @member {Number} rollout
 */
LegacyUpdateInfoData.prototype['rollout'] = undefined;

/**
 * @member {String} downloadURL
 */
LegacyUpdateInfoData.prototype['downloadURL'] = undefined;

/**
 * @member {Boolean} isAvailable
 */
LegacyUpdateInfoData.prototype['isAvailable'] = undefined;

/**
 * @member {String} label
 */
LegacyUpdateInfoData.prototype['label'] = undefined;

/**
 * @member {String} packageHash
 */
LegacyUpdateInfoData.prototype['packageHash'] = undefined;

/**
 * @member {Number} packageSize
 */
LegacyUpdateInfoData.prototype['packageSize'] = undefined;

/**
 * @member {Boolean} shouldRunBinaryVersion
 */
LegacyUpdateInfoData.prototype['shouldRunBinaryVersion'] = undefined;

/**
 * @member {Boolean} updateAppVersion
 */
LegacyUpdateInfoData.prototype['updateAppVersion'] = undefined;






export default LegacyUpdateInfoData;

