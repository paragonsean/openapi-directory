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
 * The AvailabilityOfDevicesResponseIpads model module.
 * @module model/AvailabilityOfDevicesResponseIpads
 * @version v0.1
 */
class AvailabilityOfDevicesResponseIpads {
    /**
     * Constructs a new <code>AvailabilityOfDevicesResponseIpads</code>.
     * ...
     * @alias module:model/AvailabilityOfDevicesResponseIpads
     * @param available {Number} 
     * @param maximum {Number} 
     * @param registered {Number} 
     */
    constructor(available, maximum, registered) { 
        
        AvailabilityOfDevicesResponseIpads.initialize(this, available, maximum, registered);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, available, maximum, registered) { 
        obj['available'] = available;
        obj['maximum'] = maximum;
        obj['registered'] = registered;
    }

    /**
     * Constructs a <code>AvailabilityOfDevicesResponseIpads</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AvailabilityOfDevicesResponseIpads} obj Optional instance to populate.
     * @return {module:model/AvailabilityOfDevicesResponseIpads} The populated <code>AvailabilityOfDevicesResponseIpads</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AvailabilityOfDevicesResponseIpads();

            if (data.hasOwnProperty('available')) {
                obj['available'] = ApiClient.convertToType(data['available'], 'Number');
            }
            if (data.hasOwnProperty('maximum')) {
                obj['maximum'] = ApiClient.convertToType(data['maximum'], 'Number');
            }
            if (data.hasOwnProperty('registered')) {
                obj['registered'] = ApiClient.convertToType(data['registered'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AvailabilityOfDevicesResponseIpads</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AvailabilityOfDevicesResponseIpads</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AvailabilityOfDevicesResponseIpads.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

AvailabilityOfDevicesResponseIpads.RequiredProperties = ["available", "maximum", "registered"];

/**
 * @member {Number} available
 */
AvailabilityOfDevicesResponseIpads.prototype['available'] = undefined;

/**
 * @member {Number} maximum
 */
AvailabilityOfDevicesResponseIpads.prototype['maximum'] = undefined;

/**
 * @member {Number} registered
 */
AvailabilityOfDevicesResponseIpads.prototype['registered'] = undefined;






export default AvailabilityOfDevicesResponseIpads;

