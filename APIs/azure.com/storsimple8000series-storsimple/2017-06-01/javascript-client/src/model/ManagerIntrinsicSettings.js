/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ManagerIntrinsicSettings model module.
 * @module model/ManagerIntrinsicSettings
 * @version 2017-06-01
 */
class ManagerIntrinsicSettings {
    /**
     * Constructs a new <code>ManagerIntrinsicSettings</code>.
     * Intrinsic settings which refers to the type of the StorSimple Manager.
     * @alias module:model/ManagerIntrinsicSettings
     * @param type {module:model/ManagerIntrinsicSettings.TypeEnum} The type of StorSimple Manager.
     */
    constructor(type) { 
        
        ManagerIntrinsicSettings.initialize(this, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, type) { 
        obj['type'] = type;
    }

    /**
     * Constructs a <code>ManagerIntrinsicSettings</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ManagerIntrinsicSettings} obj Optional instance to populate.
     * @return {module:model/ManagerIntrinsicSettings} The populated <code>ManagerIntrinsicSettings</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ManagerIntrinsicSettings();

            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ManagerIntrinsicSettings</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ManagerIntrinsicSettings</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ManagerIntrinsicSettings.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

ManagerIntrinsicSettings.RequiredProperties = ["type"];

/**
 * The type of StorSimple Manager.
 * @member {module:model/ManagerIntrinsicSettings.TypeEnum} type
 */
ManagerIntrinsicSettings.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
ManagerIntrinsicSettings['TypeEnum'] = {

    /**
     * value: "GardaV1"
     * @const
     */
    "GardaV1": "GardaV1",

    /**
     * value: "HelsinkiV1"
     * @const
     */
    "HelsinkiV1": "HelsinkiV1"
};



export default ManagerIntrinsicSettings;

