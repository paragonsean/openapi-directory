/**
 * KeyServ
 * KeyServ API
 *
 * The version of the OpenAPI document: 1.4.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The KeyView model module.
 * @module model/KeyView
 * @version 1.4.5
 */
class KeyView {
    /**
     * Constructs a new <code>KeyView</code>.
     * @alias module:model/KeyView
     * @param action {String} 
     * @param callbackOnModify {Boolean} 
     * @param commenced {Date} 
     * @param frequency {String} 
     */
    constructor(action, callbackOnModify, commenced, frequency) { 
        
        KeyView.initialize(this, action, callbackOnModify, commenced, frequency);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, action, callbackOnModify, commenced, frequency) { 
        obj['action'] = action;
        obj['callbackOnModify'] = callbackOnModify;
        obj['commenced'] = commenced;
        obj['frequency'] = frequency;
    }

    /**
     * Constructs a <code>KeyView</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/KeyView} obj Optional instance to populate.
     * @return {module:model/KeyView} The populated <code>KeyView</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new KeyView();

            if (data.hasOwnProperty('action')) {
                obj['action'] = ApiClient.convertToType(data['action'], 'String');
            }
            if (data.hasOwnProperty('callbackOnModify')) {
                obj['callbackOnModify'] = ApiClient.convertToType(data['callbackOnModify'], 'Boolean');
            }
            if (data.hasOwnProperty('callbackUrl')) {
                obj['callbackUrl'] = ApiClient.convertToType(data['callbackUrl'], 'String');
            }
            if (data.hasOwnProperty('commenced')) {
                obj['commenced'] = ApiClient.convertToType(data['commenced'], 'Date');
            }
            if (data.hasOwnProperty('created')) {
                obj['created'] = ApiClient.convertToType(data['created'], 'Date');
            }
            if (data.hasOwnProperty('current')) {
                obj['current'] = ApiClient.convertToType(data['current'], 'Boolean');
            }
            if (data.hasOwnProperty('custom')) {
                obj['custom'] = ApiClient.convertToType(data['custom'], Object);
            }
            if (data.hasOwnProperty('frequency')) {
                obj['frequency'] = ApiClient.convertToType(data['frequency'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('serial')) {
                obj['serial'] = ApiClient.convertToType(data['serial'], 'String');
            }
            if (data.hasOwnProperty('updated')) {
                obj['updated'] = ApiClient.convertToType(data['updated'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>KeyView</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>KeyView</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of KeyView.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['action'] && !(typeof data['action'] === 'string' || data['action'] instanceof String)) {
            throw new Error("Expected the field `action` to be a primitive type in the JSON string but got " + data['action']);
        }
        // ensure the json data is a string
        if (data['callbackUrl'] && !(typeof data['callbackUrl'] === 'string' || data['callbackUrl'] instanceof String)) {
            throw new Error("Expected the field `callbackUrl` to be a primitive type in the JSON string but got " + data['callbackUrl']);
        }
        // ensure the json data is a string
        if (data['frequency'] && !(typeof data['frequency'] === 'string' || data['frequency'] instanceof String)) {
            throw new Error("Expected the field `frequency` to be a primitive type in the JSON string but got " + data['frequency']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['serial'] && !(typeof data['serial'] === 'string' || data['serial'] instanceof String)) {
            throw new Error("Expected the field `serial` to be a primitive type in the JSON string but got " + data['serial']);
        }

        return true;
    }


}

KeyView.RequiredProperties = ["action", "callbackOnModify", "commenced", "frequency"];

/**
 * @member {String} action
 */
KeyView.prototype['action'] = undefined;

/**
 * @member {Boolean} callbackOnModify
 */
KeyView.prototype['callbackOnModify'] = undefined;

/**
 * @member {String} callbackUrl
 */
KeyView.prototype['callbackUrl'] = undefined;

/**
 * @member {Date} commenced
 */
KeyView.prototype['commenced'] = undefined;

/**
 * @member {Date} created
 */
KeyView.prototype['created'] = undefined;

/**
 * @member {Boolean} current
 */
KeyView.prototype['current'] = undefined;

/**
 * @member {Object} custom
 */
KeyView.prototype['custom'] = undefined;

/**
 * @member {String} frequency
 */
KeyView.prototype['frequency'] = undefined;

/**
 * @member {String} name
 */
KeyView.prototype['name'] = undefined;

/**
 * @member {String} serial
 */
KeyView.prototype['serial'] = undefined;

/**
 * @member {Date} updated
 */
KeyView.prototype['updated'] = undefined;






export default KeyView;

