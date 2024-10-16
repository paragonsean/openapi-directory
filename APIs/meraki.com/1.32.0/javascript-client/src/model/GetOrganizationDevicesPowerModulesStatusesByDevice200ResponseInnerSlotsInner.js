/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner model module.
 * @module model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner
 * @version 1.32.0
 */
class GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner {
    /**
     * Constructs a new <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner</code>.
     * @alias module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner
     */
    constructor() { 
        
        GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner} obj Optional instance to populate.
     * @return {module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner} The populated <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner();

            if (data.hasOwnProperty('model')) {
                obj['model'] = ApiClient.convertToType(data['model'], 'String');
            }
            if (data.hasOwnProperty('number')) {
                obj['number'] = ApiClient.convertToType(data['number'], 'Number');
            }
            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['model'] && !(typeof data['model'] === 'string' || data['model'] instanceof String)) {
            throw new Error("Expected the field `model` to be a primitive type in the JSON string but got " + data['model']);
        }
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }

        return true;
    }


}



/**
 * The power supply unit model.
 * @member {String} model
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.prototype['model'] = undefined;

/**
 * Which slot the AC power supply occupies. Possible values are: 0, 1, 2.
 * @member {module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.NumberEnum} number
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.prototype['number'] = undefined;

/**
 * The power supply unit serial number.
 * @member {String} serial
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.prototype['serial'] = undefined;

/**
 * Status of the power supply unit. Possible values are: connected, not connected, powering.
 * @member {module:model/GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.StatusEnum} status
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner.prototype['status'] = undefined;





/**
 * Allowed values for the <code>number</code> property.
 * @enum {Number}
 * @readonly
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner['NumberEnum'] = {

    /**
     * value: 0
     * @const
     */
    "0": 0,

    /**
     * value: 1
     * @const
     */
    "1": 1,

    /**
     * value: 2
     * @const
     */
    "2": 2
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner['StatusEnum'] = {

    /**
     * value: "connected"
     * @const
     */
    "connected": "connected",

    /**
     * value: "not connected"
     * @const
     */
    "not connected": "not connected",

    /**
     * value: "powering"
     * @const
     */
    "powering": "powering"
};



export default GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInnerSlotsInner;

