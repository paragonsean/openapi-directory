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
 * The SlideSmartArts model module.
 * @module model/SlideSmartArts
 * @version 0.1.0
 */
class SlideSmartArts {
    /**
     * Constructs a new <code>SlideSmartArts</code>.
     * @alias module:model/SlideSmartArts
     */
    constructor() { 
        
        SlideSmartArts.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SlideSmartArts</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SlideSmartArts} obj Optional instance to populate.
     * @return {module:model/SlideSmartArts} The populated <code>SlideSmartArts</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SlideSmartArts();

            if (data.hasOwnProperty('baseElementBlobUrl')) {
                obj['baseElementBlobUrl'] = ApiClient.convertToType(data['baseElementBlobUrl'], 'String');
            }
            if (data.hasOwnProperty('changedBaseElementBlobUrl')) {
                obj['changedBaseElementBlobUrl'] = ApiClient.convertToType(data['changedBaseElementBlobUrl'], 'String');
            }
            if (data.hasOwnProperty('graphicsId')) {
                obj['graphicsId'] = ApiClient.convertToType(data['graphicsId'], 'String');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('packageUri')) {
                obj['packageUri'] = ApiClient.convertToType(data['packageUri'], 'String');
            }
            if (data.hasOwnProperty('svgBlobUrl')) {
                obj['svgBlobUrl'] = ApiClient.convertToType(data['svgBlobUrl'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SlideSmartArts</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SlideSmartArts</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['baseElementBlobUrl'] && !(typeof data['baseElementBlobUrl'] === 'string' || data['baseElementBlobUrl'] instanceof String)) {
            throw new Error("Expected the field `baseElementBlobUrl` to be a primitive type in the JSON string but got " + data['baseElementBlobUrl']);
        }
        // ensure the json data is a string
        if (data['changedBaseElementBlobUrl'] && !(typeof data['changedBaseElementBlobUrl'] === 'string' || data['changedBaseElementBlobUrl'] instanceof String)) {
            throw new Error("Expected the field `changedBaseElementBlobUrl` to be a primitive type in the JSON string but got " + data['changedBaseElementBlobUrl']);
        }
        // ensure the json data is a string
        if (data['graphicsId'] && !(typeof data['graphicsId'] === 'string' || data['graphicsId'] instanceof String)) {
            throw new Error("Expected the field `graphicsId` to be a primitive type in the JSON string but got " + data['graphicsId']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['packageUri'] && !(typeof data['packageUri'] === 'string' || data['packageUri'] instanceof String)) {
            throw new Error("Expected the field `packageUri` to be a primitive type in the JSON string but got " + data['packageUri']);
        }
        // ensure the json data is a string
        if (data['svgBlobUrl'] && !(typeof data['svgBlobUrl'] === 'string' || data['svgBlobUrl'] instanceof String)) {
            throw new Error("Expected the field `svgBlobUrl` to be a primitive type in the JSON string but got " + data['svgBlobUrl']);
        }

        return true;
    }


}



/**
 * @member {String} baseElementBlobUrl
 */
SlideSmartArts.prototype['baseElementBlobUrl'] = undefined;

/**
 * @member {String} changedBaseElementBlobUrl
 */
SlideSmartArts.prototype['changedBaseElementBlobUrl'] = undefined;

/**
 * @member {String} graphicsId
 */
SlideSmartArts.prototype['graphicsId'] = undefined;

/**
 * @member {String} id
 */
SlideSmartArts.prototype['id'] = undefined;

/**
 * @member {String} name
 */
SlideSmartArts.prototype['name'] = undefined;

/**
 * @member {String} packageUri
 */
SlideSmartArts.prototype['packageUri'] = undefined;

/**
 * @member {String} svgBlobUrl
 */
SlideSmartArts.prototype['svgBlobUrl'] = undefined;






export default SlideSmartArts;

