/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
 * The ResourceNameAvailability model module.
 * @module model/ResourceNameAvailability
 * @version 2019-08-01
 */
class ResourceNameAvailability {
    /**
     * Constructs a new <code>ResourceNameAvailability</code>.
     * Information regarding availability of a resource name.
     * @alias module:model/ResourceNameAvailability
     */
    constructor() { 
        
        ResourceNameAvailability.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ResourceNameAvailability</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ResourceNameAvailability} obj Optional instance to populate.
     * @return {module:model/ResourceNameAvailability} The populated <code>ResourceNameAvailability</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ResourceNameAvailability();

            if (data.hasOwnProperty('message')) {
                obj['message'] = ApiClient.convertToType(data['message'], 'String');
            }
            if (data.hasOwnProperty('nameAvailable')) {
                obj['nameAvailable'] = ApiClient.convertToType(data['nameAvailable'], 'Boolean');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ResourceNameAvailability</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ResourceNameAvailability</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['message'] && !(typeof data['message'] === 'string' || data['message'] instanceof String)) {
            throw new Error("Expected the field `message` to be a primitive type in the JSON string but got " + data['message']);
        }
        // ensure the json data is a string
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }

        return true;
    }


}



/**
 * If reason == invalid, provide the user with the reason why the given name is invalid, and provide the resource naming requirements so that the user can select a valid name. If reason == AlreadyExists, explain that resource name is already in use, and direct them to select a different name.
 * @member {String} message
 */
ResourceNameAvailability.prototype['message'] = undefined;

/**
 * <code>true</code> indicates name is valid and available. <code>false</code> indicates the name is invalid, unavailable, or both.
 * @member {Boolean} nameAvailable
 */
ResourceNameAvailability.prototype['nameAvailable'] = undefined;

/**
 * <code>Invalid</code> indicates the name provided does not match Azure App Service naming requirements. <code>AlreadyExists</code> indicates that the name is already in use and is therefore unavailable.
 * @member {module:model/ResourceNameAvailability.ReasonEnum} reason
 */
ResourceNameAvailability.prototype['reason'] = undefined;





/**
 * Allowed values for the <code>reason</code> property.
 * @enum {String}
 * @readonly
 */
ResourceNameAvailability['ReasonEnum'] = {

    /**
     * value: "Invalid"
     * @const
     */
    "Invalid": "Invalid",

    /**
     * value: "AlreadyExists"
     * @const
     */
    "AlreadyExists": "AlreadyExists"
};



export default ResourceNameAvailability;

