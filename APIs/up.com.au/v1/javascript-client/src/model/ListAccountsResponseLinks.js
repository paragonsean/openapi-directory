/**
 * Up API
 * The Up API gives you programmatic access to your balances and transaction data. You can request past transactions or set up webhooks to receive real-time events when new transactions hit your account. It’s new, it’s exciting and it’s just the beginning. 
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ListAccountsResponseLinks model module.
 * @module model/ListAccountsResponseLinks
 * @version v1
 */
class ListAccountsResponseLinks {
    /**
     * Constructs a new <code>ListAccountsResponseLinks</code>.
     * @alias module:model/ListAccountsResponseLinks
     * @param next {String} The link to the next page in the results. If this value is `null` there is no next page. 
     * @param prev {String} The link to the previous page in the results. If this value is `null` there is no previous page. 
     */
    constructor(next, prev) { 
        
        ListAccountsResponseLinks.initialize(this, next, prev);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, next, prev) { 
        obj['next'] = next;
        obj['prev'] = prev;
    }

    /**
     * Constructs a <code>ListAccountsResponseLinks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListAccountsResponseLinks} obj Optional instance to populate.
     * @return {module:model/ListAccountsResponseLinks} The populated <code>ListAccountsResponseLinks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListAccountsResponseLinks();

            if (data.hasOwnProperty('next')) {
                obj['next'] = ApiClient.convertToType(data['next'], 'String');
            }
            if (data.hasOwnProperty('prev')) {
                obj['prev'] = ApiClient.convertToType(data['prev'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListAccountsResponseLinks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListAccountsResponseLinks</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ListAccountsResponseLinks.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['next'] && !(typeof data['next'] === 'string' || data['next'] instanceof String)) {
            throw new Error("Expected the field `next` to be a primitive type in the JSON string but got " + data['next']);
        }
        // ensure the json data is a string
        if (data['prev'] && !(typeof data['prev'] === 'string' || data['prev'] instanceof String)) {
            throw new Error("Expected the field `prev` to be a primitive type in the JSON string but got " + data['prev']);
        }

        return true;
    }


}

ListAccountsResponseLinks.RequiredProperties = ["next", "prev"];

/**
 * The link to the next page in the results. If this value is `null` there is no next page. 
 * @member {String} next
 */
ListAccountsResponseLinks.prototype['next'] = undefined;

/**
 * The link to the previous page in the results. If this value is `null` there is no previous page. 
 * @member {String} prev
 */
ListAccountsResponseLinks.prototype['prev'] = undefined;






export default ListAccountsResponseLinks;

