/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The AccountCartAddHybrisWebsitesInner model module.
 * @module model/AccountCartAddHybrisWebsitesInner
 * @version 1.1
 */
class AccountCartAddHybrisWebsitesInner {
    /**
     * Constructs a new <code>AccountCartAddHybrisWebsitesInner</code>.
     * @alias module:model/AccountCartAddHybrisWebsitesInner
     * @param storeIds {Array.<String>} 
     * @param uid {String} 
     * @param url {String} 
     */
    constructor(storeIds, uid, url) { 
        
        AccountCartAddHybrisWebsitesInner.initialize(this, storeIds, uid, url);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, storeIds, uid, url) { 
        obj['storeIds'] = storeIds;
        obj['uid'] = uid;
        obj['url'] = url;
    }

    /**
     * Constructs a <code>AccountCartAddHybrisWebsitesInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountCartAddHybrisWebsitesInner} obj Optional instance to populate.
     * @return {module:model/AccountCartAddHybrisWebsitesInner} The populated <code>AccountCartAddHybrisWebsitesInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountCartAddHybrisWebsitesInner();

            if (data.hasOwnProperty('storeIds')) {
                obj['storeIds'] = ApiClient.convertToType(data['storeIds'], ['String']);
            }
            if (data.hasOwnProperty('uid')) {
                obj['uid'] = ApiClient.convertToType(data['uid'], 'String');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountCartAddHybrisWebsitesInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountCartAddHybrisWebsitesInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccountCartAddHybrisWebsitesInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['storeIds'])) {
            throw new Error("Expected the field `storeIds` to be an array in the JSON data but got " + data['storeIds']);
        }
        // ensure the json data is a string
        if (data['uid'] && !(typeof data['uid'] === 'string' || data['uid'] instanceof String)) {
            throw new Error("Expected the field `uid` to be a primitive type in the JSON string but got " + data['uid']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}

AccountCartAddHybrisWebsitesInner.RequiredProperties = ["storeIds", "uid", "url"];

/**
 * @member {Array.<String>} storeIds
 */
AccountCartAddHybrisWebsitesInner.prototype['storeIds'] = undefined;

/**
 * @member {String} uid
 */
AccountCartAddHybrisWebsitesInner.prototype['uid'] = undefined;

/**
 * @member {String} url
 */
AccountCartAddHybrisWebsitesInner.prototype['url'] = undefined;






export default AccountCartAddHybrisWebsitesInner;

