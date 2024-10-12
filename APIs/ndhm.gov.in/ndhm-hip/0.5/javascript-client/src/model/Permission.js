/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PermissionDateRange from './PermissionDateRange';
import PermissionFrequency from './PermissionFrequency';

/**
 * The Permission model module.
 * @module model/Permission
 * @version 0.5
 */
class Permission {
    /**
     * Constructs a new <code>Permission</code>.
     * @alias module:model/Permission
     * @param accessMode {module:model/Permission.AccessModeEnum} 
     * @param dataEraseAt {Date} 
     * @param dateRange {module:model/PermissionDateRange} 
     * @param frequency {module:model/PermissionFrequency} 
     */
    constructor(accessMode, dataEraseAt, dateRange, frequency) { 
        
        Permission.initialize(this, accessMode, dataEraseAt, dateRange, frequency);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accessMode, dataEraseAt, dateRange, frequency) { 
        obj['accessMode'] = accessMode;
        obj['dataEraseAt'] = dataEraseAt;
        obj['dateRange'] = dateRange;
        obj['frequency'] = frequency;
    }

    /**
     * Constructs a <code>Permission</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Permission} obj Optional instance to populate.
     * @return {module:model/Permission} The populated <code>Permission</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Permission();

            if (data.hasOwnProperty('accessMode')) {
                obj['accessMode'] = ApiClient.convertToType(data['accessMode'], 'String');
            }
            if (data.hasOwnProperty('dataEraseAt')) {
                obj['dataEraseAt'] = ApiClient.convertToType(data['dataEraseAt'], 'Date');
            }
            if (data.hasOwnProperty('dateRange')) {
                obj['dateRange'] = PermissionDateRange.constructFromObject(data['dateRange']);
            }
            if (data.hasOwnProperty('frequency')) {
                obj['frequency'] = PermissionFrequency.constructFromObject(data['frequency']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Permission</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Permission</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Permission.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['accessMode'] && !(typeof data['accessMode'] === 'string' || data['accessMode'] instanceof String)) {
            throw new Error("Expected the field `accessMode` to be a primitive type in the JSON string but got " + data['accessMode']);
        }
        // validate the optional field `dateRange`
        if (data['dateRange']) { // data not null
          PermissionDateRange.validateJSON(data['dateRange']);
        }
        // validate the optional field `frequency`
        if (data['frequency']) { // data not null
          PermissionFrequency.validateJSON(data['frequency']);
        }

        return true;
    }


}

Permission.RequiredProperties = ["accessMode", "dataEraseAt", "dateRange", "frequency"];

/**
 * @member {module:model/Permission.AccessModeEnum} accessMode
 */
Permission.prototype['accessMode'] = undefined;

/**
 * @member {Date} dataEraseAt
 */
Permission.prototype['dataEraseAt'] = undefined;

/**
 * @member {module:model/PermissionDateRange} dateRange
 */
Permission.prototype['dateRange'] = undefined;

/**
 * @member {module:model/PermissionFrequency} frequency
 */
Permission.prototype['frequency'] = undefined;





/**
 * Allowed values for the <code>accessMode</code> property.
 * @enum {String}
 * @readonly
 */
Permission['AccessModeEnum'] = {

    /**
     * value: "VIEW"
     * @const
     */
    "VIEW": "VIEW",

    /**
     * value: "STORE"
     * @const
     */
    "STORE": "STORE",

    /**
     * value: "QUERY"
     * @const
     */
    "QUERY": "QUERY",

    /**
     * value: "STREAM"
     * @const
     */
    "STREAM": "STREAM"
};



export default Permission;

