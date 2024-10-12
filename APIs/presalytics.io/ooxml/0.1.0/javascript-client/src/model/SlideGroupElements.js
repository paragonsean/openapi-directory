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
 * The SlideGroupElements model module.
 * @module model/SlideGroupElements
 * @version 0.1.0
 */
class SlideGroupElements {
    /**
     * Constructs a new <code>SlideGroupElements</code>.
     * @alias module:model/SlideGroupElements
     */
    constructor() { 
        
        SlideGroupElements.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SlideGroupElements</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SlideGroupElements} obj Optional instance to populate.
     * @return {module:model/SlideGroupElements} The populated <code>SlideGroupElements</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SlideGroupElements();

            if (data.hasOwnProperty('groupElementTypeId')) {
                obj['groupElementTypeId'] = ApiClient.convertToType(data['groupElementTypeId'], 'Number');
            }
            if (data.hasOwnProperty('groupElementTypePk')) {
                obj['groupElementTypePk'] = ApiClient.convertToType(data['groupElementTypePk'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('parentGroupElementId')) {
                obj['parentGroupElementId'] = ApiClient.convertToType(data['parentGroupElementId'], 'String');
            }
            if (data.hasOwnProperty('shapeTreeId')) {
                obj['shapeTreeId'] = ApiClient.convertToType(data['shapeTreeId'], 'String');
            }
            if (data.hasOwnProperty('ultimateParentShapeTreeId')) {
                obj['ultimateParentShapeTreeId'] = ApiClient.convertToType(data['ultimateParentShapeTreeId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SlideGroupElements</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SlideGroupElements</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['groupElementTypePk'] && !(typeof data['groupElementTypePk'] === 'string' || data['groupElementTypePk'] instanceof String)) {
            throw new Error("Expected the field `groupElementTypePk` to be a primitive type in the JSON string but got " + data['groupElementTypePk']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['parentGroupElementId'] && !(typeof data['parentGroupElementId'] === 'string' || data['parentGroupElementId'] instanceof String)) {
            throw new Error("Expected the field `parentGroupElementId` to be a primitive type in the JSON string but got " + data['parentGroupElementId']);
        }
        // ensure the json data is a string
        if (data['shapeTreeId'] && !(typeof data['shapeTreeId'] === 'string' || data['shapeTreeId'] instanceof String)) {
            throw new Error("Expected the field `shapeTreeId` to be a primitive type in the JSON string but got " + data['shapeTreeId']);
        }
        // ensure the json data is a string
        if (data['ultimateParentShapeTreeId'] && !(typeof data['ultimateParentShapeTreeId'] === 'string' || data['ultimateParentShapeTreeId'] instanceof String)) {
            throw new Error("Expected the field `ultimateParentShapeTreeId` to be a primitive type in the JSON string but got " + data['ultimateParentShapeTreeId']);
        }

        return true;
    }


}



/**
 * @member {Number} groupElementTypeId
 */
SlideGroupElements.prototype['groupElementTypeId'] = undefined;

/**
 * @member {String} groupElementTypePk
 */
SlideGroupElements.prototype['groupElementTypePk'] = undefined;

/**
 * @member {String} id
 */
SlideGroupElements.prototype['id'] = undefined;

/**
 * @member {String} parentGroupElementId
 */
SlideGroupElements.prototype['parentGroupElementId'] = undefined;

/**
 * @member {String} shapeTreeId
 */
SlideGroupElements.prototype['shapeTreeId'] = undefined;

/**
 * @member {String} ultimateParentShapeTreeId
 */
SlideGroupElements.prototype['ultimateParentShapeTreeId'] = undefined;






export default SlideGroupElements;

