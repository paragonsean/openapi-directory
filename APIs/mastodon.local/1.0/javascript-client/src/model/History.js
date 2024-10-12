/**
 * Mastodon API Specification (https://github.com/mastodon/mastodon)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
 * Contact: sardo@hey.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The History model module.
 * @module model/History
 * @version 1.0
 */
class History {
    /**
     * Constructs a new <code>History</code>.
     * Represents daily usage history of a hashtag.
     * @alias module:model/History
     * @param accounts {String} the total of accounts using the tag within that day. Cast from an integer.
     * @param day {String} UNIX timestamp on midnight of the given day.
     * @param uses {String} the counted usage of the tag within that day. Cast from an integer.
     */
    constructor(accounts, day, uses) { 
        
        History.initialize(this, accounts, day, uses);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, accounts, day, uses) { 
        obj['accounts'] = accounts;
        obj['day'] = day;
        obj['uses'] = uses;
    }

    /**
     * Constructs a <code>History</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/History} obj Optional instance to populate.
     * @return {module:model/History} The populated <code>History</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new History();

            if (data.hasOwnProperty('accounts')) {
                obj['accounts'] = ApiClient.convertToType(data['accounts'], 'String');
            }
            if (data.hasOwnProperty('day')) {
                obj['day'] = ApiClient.convertToType(data['day'], 'String');
            }
            if (data.hasOwnProperty('uses')) {
                obj['uses'] = ApiClient.convertToType(data['uses'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>History</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>History</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of History.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['accounts'] && !(typeof data['accounts'] === 'string' || data['accounts'] instanceof String)) {
            throw new Error("Expected the field `accounts` to be a primitive type in the JSON string but got " + data['accounts']);
        }
        // ensure the json data is a string
        if (data['day'] && !(typeof data['day'] === 'string' || data['day'] instanceof String)) {
            throw new Error("Expected the field `day` to be a primitive type in the JSON string but got " + data['day']);
        }
        // ensure the json data is a string
        if (data['uses'] && !(typeof data['uses'] === 'string' || data['uses'] instanceof String)) {
            throw new Error("Expected the field `uses` to be a primitive type in the JSON string but got " + data['uses']);
        }

        return true;
    }


}

History.RequiredProperties = ["accounts", "day", "uses"];

/**
 * the total of accounts using the tag within that day. Cast from an integer.
 * @member {String} accounts
 */
History.prototype['accounts'] = undefined;

/**
 * UNIX timestamp on midnight of the given day.
 * @member {String} day
 */
History.prototype['day'] = undefined;

/**
 * the counted usage of the tag within that day. Cast from an integer.
 * @member {String} uses
 */
History.prototype['uses'] = undefined;






export default History;

