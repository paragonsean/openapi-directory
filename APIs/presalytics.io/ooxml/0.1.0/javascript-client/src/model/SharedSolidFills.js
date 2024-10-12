/**
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The SharedSolidFills model module.
 * @module model/SharedSolidFills
 * @version 0.1.0
 */
class SharedSolidFills {
    /**
     * Constructs a new <code>SharedSolidFills</code>.
     * @alias module:model/SharedSolidFills
     */
    constructor() { 
        
        SharedSolidFills.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SharedSolidFills</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SharedSolidFills} obj Optional instance to populate.
     * @return {module:model/SharedSolidFills} The populated <code>SharedSolidFills</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SharedSolidFills();

            if (data.hasOwnProperty('colorTypeId')) {
                obj['colorTypeId'] = ApiClient.convertToType(data['colorTypeId'], 'Number');
            }
            if (data.hasOwnProperty('fillMapId')) {
                obj['fillMapId'] = ApiClient.convertToType(data['fillMapId'], 'String');
            }
            if (data.hasOwnProperty('hexValue')) {
                obj['hexValue'] = ApiClient.convertToType(data['hexValue'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('isUserColor')) {
                obj['isUserColor'] = ApiClient.convertToType(data['isUserColor'], 'Boolean');
            }
            if (data.hasOwnProperty('parentGradientStopId')) {
                obj['parentGradientStopId'] = ApiClient.convertToType(data['parentGradientStopId'], 'String');
            }
            if (data.hasOwnProperty('parentLineId')) {
                obj['parentLineId'] = ApiClient.convertToType(data['parentLineId'], 'String');
            }
            if (data.hasOwnProperty('parentTextId')) {
                obj['parentTextId'] = ApiClient.convertToType(data['parentTextId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SharedSolidFills</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SharedSolidFills</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['fillMapId'] && !(typeof data['fillMapId'] === 'string' || data['fillMapId'] instanceof String)) {
            throw new Error("Expected the field `fillMapId` to be a primitive type in the JSON string but got " + data['fillMapId']);
        }
        // ensure the json data is a string
        if (data['hexValue'] && !(typeof data['hexValue'] === 'string' || data['hexValue'] instanceof String)) {
            throw new Error("Expected the field `hexValue` to be a primitive type in the JSON string but got " + data['hexValue']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['parentGradientStopId'] && !(typeof data['parentGradientStopId'] === 'string' || data['parentGradientStopId'] instanceof String)) {
            throw new Error("Expected the field `parentGradientStopId` to be a primitive type in the JSON string but got " + data['parentGradientStopId']);
        }
        // ensure the json data is a string
        if (data['parentLineId'] && !(typeof data['parentLineId'] === 'string' || data['parentLineId'] instanceof String)) {
            throw new Error("Expected the field `parentLineId` to be a primitive type in the JSON string but got " + data['parentLineId']);
        }
        // ensure the json data is a string
        if (data['parentTextId'] && !(typeof data['parentTextId'] === 'string' || data['parentTextId'] instanceof String)) {
            throw new Error("Expected the field `parentTextId` to be a primitive type in the JSON string but got " + data['parentTextId']);
        }

        return true;
    }


}



/**
 * @member {Number} colorTypeId
 */
SharedSolidFills.prototype['colorTypeId'] = undefined;

/**
 * @member {String} fillMapId
 */
SharedSolidFills.prototype['fillMapId'] = undefined;

/**
 * @member {String} hexValue
 */
SharedSolidFills.prototype['hexValue'] = undefined;

/**
 * @member {String} id
 */
SharedSolidFills.prototype['id'] = undefined;

/**
 * @member {Boolean} isUserColor
 */
SharedSolidFills.prototype['isUserColor'] = undefined;

/**
 * @member {String} parentGradientStopId
 */
SharedSolidFills.prototype['parentGradientStopId'] = undefined;

/**
 * @member {String} parentLineId
 */
SharedSolidFills.prototype['parentLineId'] = undefined;

/**
 * @member {String} parentTextId
 */
SharedSolidFills.prototype['parentTextId'] = undefined;






export default SharedSolidFills;

