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
import BaseModel from './BaseModel';
import UpdatesProperties from './UpdatesProperties';

/**
 * The Updates model module.
 * @module model/Updates
 * @version 2017-06-01
 */
class Updates {
    /**
     * Constructs a new <code>Updates</code>.
     * The updates profile of a device.
     * @alias module:model/Updates
     * @implements module:model/BaseModel
     */
    constructor() { 
        BaseModel.initialize(this);
        Updates.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
        obj['properties'] = properties;
    }

    /**
     * Constructs a <code>Updates</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Updates} obj Optional instance to populate.
     * @return {module:model/Updates} The populated <code>Updates</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Updates();
            BaseModel.constructFromObject(data, obj);

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = UpdatesProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('kind')) {
                obj['kind'] = ApiClient.convertToType(data['kind'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Updates</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Updates</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Updates.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          UpdatesProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['kind'] && !(typeof data['kind'] === 'string' || data['kind'] instanceof String)) {
            throw new Error("Expected the field `kind` to be a primitive type in the JSON string but got " + data['kind']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

Updates.RequiredProperties = ["properties"];

/**
 * @member {module:model/UpdatesProperties} properties
 */
Updates.prototype['properties'] = undefined;

/**
 * The path ID that uniquely identifies the object.
 * @member {String} id
 */
Updates.prototype['id'] = undefined;

/**
 * The Kind of the object. Currently only Series8000 is supported
 * @member {module:model/Updates.KindEnum} kind
 */
Updates.prototype['kind'] = undefined;

/**
 * The name of the object.
 * @member {String} name
 */
Updates.prototype['name'] = undefined;

/**
 * The hierarchical type of the object.
 * @member {String} type
 */
Updates.prototype['type'] = undefined;


// Implement BaseModel interface:
/**
 * The path ID that uniquely identifies the object.
 * @member {String} id
 */
BaseModel.prototype['id'] = undefined;
/**
 * The Kind of the object. Currently only Series8000 is supported
 * @member {module:model/BaseModel.KindEnum} kind
 */
BaseModel.prototype['kind'] = undefined;
/**
 * The name of the object.
 * @member {String} name
 */
BaseModel.prototype['name'] = undefined;
/**
 * The hierarchical type of the object.
 * @member {String} type
 */
BaseModel.prototype['type'] = undefined;



/**
 * Allowed values for the <code>kind</code> property.
 * @enum {String}
 * @readonly
 */
Updates['KindEnum'] = {

    /**
     * value: "Series8000"
     * @const
     */
    "Series8000": "Series8000"
};



export default Updates;

