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
import URL from './URL';
import WannabeConsumerRights from './WannabeConsumerRights';

/**
 * The WannabeConsumer model module.
 * @module model/WannabeConsumer
 * @version 1.0.0
 */
class WannabeConsumer {
    /**
     * Constructs a new <code>WannabeConsumer</code>.
     * @alias module:model/WannabeConsumer
     * @param baseUrl {module:model/URL} 
     * @param name {String} 
     * @param rights {module:model/WannabeConsumerRights} 
     * @param url {module:model/URL} 
     */
    constructor(baseUrl, name, rights, url) { 
        
        WannabeConsumer.initialize(this, baseUrl, name, rights, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, baseUrl, name, rights, url) { 
        obj['baseUrl'] = baseUrl;
        obj['name'] = name;
        obj['rights'] = rights;
        obj['url'] = url;
    }

    /**
     * Constructs a <code>WannabeConsumer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/WannabeConsumer} obj Optional instance to populate.
     * @return {module:model/WannabeConsumer} The populated <code>WannabeConsumer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new WannabeConsumer();

            if (data.hasOwnProperty('baseUrl')) {
                obj['baseUrl'] = URL.constructFromObject(data['baseUrl']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('picture')) {
                obj['picture'] = ApiClient.convertToType(data['picture'], 'String');
            }
            if (data.hasOwnProperty('rights')) {
                obj['rights'] = WannabeConsumerRights.constructFromObject(data['rights']);
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = URL.constructFromObject(data['url']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>WannabeConsumer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>WannabeConsumer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of WannabeConsumer.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `baseUrl`
        if (data['baseUrl']) { // data not null
          URL.validateJSON(data['baseUrl']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
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
          WannabeConsumerRights.validateJSON(data['rights']);
        }
        // validate the optional field `url`
        if (data['url']) { // data not null
          URL.validateJSON(data['url']);
        }

        return true;
    }


}

WannabeConsumer.RequiredProperties = ["baseUrl", "name", "rights", "url"];

/**
 * @member {module:model/URL} baseUrl
 */
WannabeConsumer.prototype['baseUrl'] = undefined;

/**
 * @member {String} description
 */
WannabeConsumer.prototype['description'] = undefined;

/**
 * @member {String} name
 */
WannabeConsumer.prototype['name'] = undefined;

/**
 * 
 * @member {String} picture
 */
WannabeConsumer.prototype['picture'] = undefined;

/**
 * @member {module:model/WannabeConsumerRights} rights
 */
WannabeConsumer.prototype['rights'] = undefined;

/**
 * @member {module:model/URL} url
 */
WannabeConsumer.prototype['url'] = undefined;






export default WannabeConsumer;

