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
 * The StoresBasicDetails model module.
 * @module model/StoresBasicDetails
 * @version v0.1
 */
class StoresBasicDetails {
    /**
     * Constructs a new <code>StoresBasicDetails</code>.
     * @alias module:model/StoresBasicDetails
     */
    constructor() { 
        
        StoresBasicDetails.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StoresBasicDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StoresBasicDetails} obj Optional instance to populate.
     * @return {module:model/StoresBasicDetails} The populated <code>StoresBasicDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StoresBasicDetails();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('publishing_status')) {
                obj['publishing_status'] = ApiClient.convertToType(data['publishing_status'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StoresBasicDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StoresBasicDetails</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['publishing_status'] && !(typeof data['publishing_status'] === 'string' || data['publishing_status'] instanceof String)) {
            throw new Error("Expected the field `publishing_status` to be a primitive type in the JSON string but got " + data['publishing_status']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * ID identifying a unique distribution store.
 * @member {String} id
 */
StoresBasicDetails.prototype['id'] = undefined;

/**
 * A name identifying a unique distribution store.
 * @member {String} name
 */
StoresBasicDetails.prototype['name'] = undefined;

/**
 * publishing status of the release in the store.
 * @member {String} publishing_status
 */
StoresBasicDetails.prototype['publishing_status'] = undefined;

/**
 * type of the distribution store currently stores type can be intune or googleplay.
 * @member {module:model/StoresBasicDetails.TypeEnum} type
 */
StoresBasicDetails.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
StoresBasicDetails['TypeEnum'] = {

    /**
     * value: "intune"
     * @const
     */
    "intune": "intune",

    /**
     * value: "googleplay"
     * @const
     */
    "googleplay": "googleplay"
};



export default StoresBasicDetails;

