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
import AccountResourceAttributes from './AccountResourceAttributes';
import AccountResourceLinks from './AccountResourceLinks';
import AccountResourceRelationships from './AccountResourceRelationships';

/**
 * The AccountResource model module.
 * @module model/AccountResource
 * @version v1
 */
class AccountResource {
    /**
     * Constructs a new <code>AccountResource</code>.
     * Provides information about an Up bank account. 
     * @alias module:model/AccountResource
     * @param attributes {module:model/AccountResourceAttributes} 
     * @param id {String} The unique identifier for this account. 
     * @param relationships {module:model/AccountResourceRelationships} 
     * @param type {String} The type of this resource: `accounts`
     */
    constructor(attributes, id, relationships, type) { 
        
        AccountResource.initialize(this, attributes, id, relationships, type);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, attributes, id, relationships, type) { 
        obj['attributes'] = attributes;
        obj['id'] = id;
        obj['relationships'] = relationships;
        obj['type'] = type;
    }

    /**
     * Constructs a <code>AccountResource</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountResource} obj Optional instance to populate.
     * @return {module:model/AccountResource} The populated <code>AccountResource</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountResource();

            if (data.hasOwnProperty('attributes')) {
                obj['attributes'] = AccountResourceAttributes.constructFromObject(data['attributes']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('links')) {
                obj['links'] = AccountResourceLinks.constructFromObject(data['links']);
            }
            if (data.hasOwnProperty('relationships')) {
                obj['relationships'] = AccountResourceRelationships.constructFromObject(data['relationships']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountResource</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountResource</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccountResource.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `attributes`
        if (data['attributes']) { // data not null
          AccountResourceAttributes.validateJSON(data['attributes']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `links`
        if (data['links']) { // data not null
          AccountResourceLinks.validateJSON(data['links']);
        }
        // validate the optional field `relationships`
        if (data['relationships']) { // data not null
          AccountResourceRelationships.validateJSON(data['relationships']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

AccountResource.RequiredProperties = ["attributes", "id", "relationships", "type"];

/**
 * @member {module:model/AccountResourceAttributes} attributes
 */
AccountResource.prototype['attributes'] = undefined;

/**
 * The unique identifier for this account. 
 * @member {String} id
 */
AccountResource.prototype['id'] = undefined;

/**
 * @member {module:model/AccountResourceLinks} links
 */
AccountResource.prototype['links'] = undefined;

/**
 * @member {module:model/AccountResourceRelationships} relationships
 */
AccountResource.prototype['relationships'] = undefined;

/**
 * The type of this resource: `accounts`
 * @member {String} type
 */
AccountResource.prototype['type'] = undefined;






export default AccountResource;

