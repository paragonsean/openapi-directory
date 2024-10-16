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
 * The DestinationDetails model module.
 * @module model/DestinationDetails
 * @version v0.1
 */
class DestinationDetails {
    /**
     * Constructs a new <code>DestinationDetails</code>.
     * Destination details for distributing build releases
     * @alias module:model/DestinationDetails
     * @param id {String} 
     * @param type {module:model/DestinationDetails.TypeEnum} 
     */
    constructor(id, type) { 
        
        DestinationDetails.initialize(this, id, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, id, type) { 
        obj['id'] = id;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>DestinationDetails</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DestinationDetails} obj Optional instance to populate.
     * @return {module:model/DestinationDetails} The populated <code>DestinationDetails</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DestinationDetails();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DestinationDetails</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DestinationDetails</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of DestinationDetails.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

DestinationDetails.RequiredProperties = ["id", "type"];

/**
 * @member {String} id
 */
DestinationDetails.prototype['id'] = undefined;

/**
 * @member {module:model/DestinationDetails.TypeEnum} type
 */
DestinationDetails.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
DestinationDetails['TypeEnum'] = {

    /**
     * value: "store"
     * @const
     */
    "store": "store",

    /**
     * value: "group"
     * @const
     */
    "group": "group",

    /**
     * value: "tester"
     * @const
     */
    "tester": "tester"
};



export default DestinationDetails;

