/**
 * Clever-Cloud API
 * Public API for managing Clever-Cloud data and products
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
import ConsumerRights from './ConsumerRights';

/**
 * The Consumer model module.
 * @module model/Consumer
 * @version 1.0.0
 */
class Consumer {
    /**
     * Constructs a new <code>Consumer</code>.
     * @alias module:model/Consumer
     * @param baseUrl {String} 
     * @param description {String} 
     * @param name {String} 
     * @param rights {module:model/ConsumerRights} 
     * @param url {String} 
     */
    constructor(baseUrl, description, name, rights, url) { 
        
        Consumer.initialize(this, baseUrl, description, name, rights, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, baseUrl, description, name, rights, url) { 
        obj['baseUrl'] = baseUrl;
        obj['description'] = description;
        obj['name'] = name;
        obj['rights'] = rights;
        obj['url'] = url;
    }

    /**
     * Constructs a <code>Consumer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Consumer} obj Optional instance to populate.
     * @return {module:model/Consumer} The populated <code>Consumer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Consumer();

            if (data.hasOwnProperty('baseUrl')) {
                obj['baseUrl'] = ApiClient.convertToType(data['baseUrl'], 'String');
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('key')) {
                obj['key'] = ApiClient.convertToType(data['key'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('picture')) {
                obj['picture'] = ApiClient.convertToType(data['picture'], 'String');
            }
            if (data.hasOwnProperty('rights')) {
                obj['rights'] = ConsumerRights.constructFromObject(data['rights']);
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Consumer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Consumer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Consumer.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['baseUrl'] && !(typeof data['baseUrl'] === 'string' || data['baseUrl'] instanceof String)) {
            throw new Error("Expected the field `baseUrl` to be a primitive type in the JSON string but got " + data['baseUrl']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is a string
        if (data['key'] && !(typeof data['key'] === 'string' || data['key'] instanceof String)) {
            throw new Error("Expected the field `key` to be a primitive type in the JSON string but got " + data['key']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['picture'] && !(typeof data['picture'] === 'string' || data['picture'] instanceof String)) {
            throw new Error("Expected the field `picture` to be a primitive type in the JSON string but got " + data['picture']);
        }
        // validate the optional field `rights`
        if (data['rights']) { // data not null
          ConsumerRights.validateJSON(data['rights']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

Consumer.RequiredProperties = ["baseUrl", "description", "name", "rights", "url"];

/**
 * @member {String} baseUrl
 */
Consumer.prototype['baseUrl'] = undefined;

/**
 * @member {String} description
 */
Consumer.prototype['description'] = undefined;

/**
 * @member {String} key
 */
Consumer.prototype['key'] = undefined;

/**
 * @member {String} name
 */
Consumer.prototype['name'] = undefined;

/**
 * @member {String} picture
 */
Consumer.prototype['picture'] = undefined;

/**
 * @member {module:model/ConsumerRights} rights
 */
Consumer.prototype['rights'] = undefined;

/**
 * @member {String} url
 */
Consumer.prototype['url'] = undefined;






export default Consumer;

