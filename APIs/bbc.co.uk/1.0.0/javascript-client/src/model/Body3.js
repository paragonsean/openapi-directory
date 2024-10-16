/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
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

/**
 * The Body3 model module.
 * @module model/Body3
 * @version 1.0.0
 */
class Body3 {
    /**
     * Constructs a new <code>Body3</code>.
     * @alias module:model/Body3
     * @param platform {module:model/Body3.PlatformEnum} 
     * @param serviceId {String} 
     */
    constructor(platform, serviceId) { 
        
        Body3.initialize(this, platform, serviceId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, platform, serviceId) { 
        obj['platform'] = platform;
        obj['service_id'] = serviceId;
    }

    /**
     * Constructs a <code>Body3</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Body3} obj Optional instance to populate.
     * @return {module:model/Body3} The populated <code>Body3</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Body3();

            if (data.hasOwnProperty('platform')) {
                obj['platform'] = ApiClient.convertToType(data['platform'], 'String');
            }
            if (data.hasOwnProperty('service_id')) {
                obj['service_id'] = ApiClient.convertToType(data['service_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Body3</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Body3</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Body3.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['platform'] && !(typeof data['platform'] === 'string' || data['platform'] instanceof String)) {
            throw new Error("Expected the field `platform` to be a primitive type in the JSON string but got " + data['platform']);
        }
        // ensure the json data is a string
        if (data['service_id'] && !(typeof data['service_id'] === 'string' || data['service_id'] instanceof String)) {
            throw new Error("Expected the field `service_id` to be a primitive type in the JSON string but got " + data['service_id']);
        }

        return true;
    }


}

Body3.RequiredProperties = ["platform", "service_id"];

/**
 * @member {module:model/Body3.PlatformEnum} platform
 */
Body3.prototype['platform'] = undefined;

/**
 * @member {String} service_id
 */
Body3.prototype['service_id'] = undefined;





/**
 * Allowed values for the <code>platform</code> property.
 * @enum {String}
 * @readonly
 */
Body3['PlatformEnum'] = {

    /**
     * value: "responsiveweb"
     * @const
     */
    "responsiveweb": "responsiveweb",

    /**
     * value: "app"
     * @const
     */
    "app": "app"
};



export default Body3;

