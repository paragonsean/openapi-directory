/**
 * Transportation Laws and Incentives
 * Query our database of federal and state laws and incentives for alternative fuels and vehicles, air quality, fuel efficiency, and other transportation-related topics. This dataset powers the <a href=\"https://afdc.energy.gov/laws\">Federal and State Laws and Incentives</a> on the Alternative Fuels Data Center.
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
 * The Poc model module.
 * @module model/Poc
 * @version 0.1.0
 */
class Poc {
    /**
     * Constructs a new <code>Poc</code>.
     * @alias module:model/Poc
     * @param name {String} The name of the contact
     * @param state {String} The state in which the contact is based ('US' for Federal laws and 'DC' for the District of Columbia)
     */
    constructor(name, state) { 
        
        Poc.initialize(this, name, state);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, state) { 
        obj['name'] = name;
        obj['state'] = state;
    }

    /**
     * Constructs a <code>Poc</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Poc} obj Optional instance to populate.
     * @return {module:model/Poc} The populated <code>Poc</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Poc();

            if (data.hasOwnProperty('agency')) {
                obj['agency'] = ApiClient.convertToType(data['agency'], 'String');
            }
            if (data.hasOwnProperty('email')) {
                obj['email'] = ApiClient.convertToType(data['email'], 'String');
            }
            if (data.hasOwnProperty('fax')) {
                obj['fax'] = ApiClient.convertToType(data['fax'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('state')) {
                obj['state'] = ApiClient.convertToType(data['state'], 'String');
            }
            if (data.hasOwnProperty('telephone')) {
                obj['telephone'] = ApiClient.convertToType(data['telephone'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('web_page')) {
                obj['web_page'] = ApiClient.convertToType(data['web_page'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Poc</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Poc</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Poc.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['agency'] && !(typeof data['agency'] === 'string' || data['agency'] instanceof String)) {
            throw new Error("Expected the field `agency` to be a primitive type in the JSON string but got " + data['agency']);
        }
        // ensure the json data is a string
        if (data['email'] && !(typeof data['email'] === 'string' || data['email'] instanceof String)) {
            throw new Error("Expected the field `email` to be a primitive type in the JSON string but got " + data['email']);
        }
        // ensure the json data is a string
        if (data['fax'] && !(typeof data['fax'] === 'string' || data['fax'] instanceof String)) {
            throw new Error("Expected the field `fax` to be a primitive type in the JSON string but got " + data['fax']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['state'] && !(typeof data['state'] === 'string' || data['state'] instanceof String)) {
            throw new Error("Expected the field `state` to be a primitive type in the JSON string but got " + data['state']);
        }
        // ensure the json data is a string
        if (data['telephone'] && !(typeof data['telephone'] === 'string' || data['telephone'] instanceof String)) {
            throw new Error("Expected the field `telephone` to be a primitive type in the JSON string but got " + data['telephone']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }
        // ensure the json data is a string
        if (data['web_page'] && !(typeof data['web_page'] === 'string' || data['web_page'] instanceof String)) {
            throw new Error("Expected the field `web_page` to be a primitive type in the JSON string but got " + data['web_page']);
        }

        return true;
    }


}

Poc.RequiredProperties = ["name", "state"];

/**
 * The agency that the contact represents
 * @member {String} agency
 */
Poc.prototype['agency'] = undefined;

/**
 * The contacts email address
 * @member {String} email
 */
Poc.prototype['email'] = undefined;

/**
 * The contacts fax number
 * @member {String} fax
 */
Poc.prototype['fax'] = undefined;

/**
 * The name of the contact
 * @member {String} name
 */
Poc.prototype['name'] = undefined;

/**
 * The state in which the contact is based ('US' for Federal laws and 'DC' for the District of Columbia)
 * @member {String} state
 */
Poc.prototype['state'] = undefined;

/**
 * The contacts phone number
 * @member {String} telephone
 */
Poc.prototype['telephone'] = undefined;

/**
 * The job title of the contact
 * @member {String} title
 */
Poc.prototype['title'] = undefined;

/**
 * The contacts webpage
 * @member {String} web_page
 */
Poc.prototype['web_page'] = undefined;






export default Poc;

