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
 * The AccountResourceLinks model module.
 * @module model/AccountResourceLinks
 * @version v1
 */
class AccountResourceLinks {
    /**
     * Constructs a new <code>AccountResourceLinks</code>.
     * @alias module:model/AccountResourceLinks
     * @param self {String} The canonical link to this resource within the API. 
     */
    constructor(self) { 
        
        AccountResourceLinks.initialize(this, self);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, self) { 
        obj['self'] = self;
    }

    /**
     * Constructs a <code>AccountResourceLinks</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccountResourceLinks} obj Optional instance to populate.
     * @return {module:model/AccountResourceLinks} The populated <code>AccountResourceLinks</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccountResourceLinks();

            if (data.hasOwnProperty('self')) {
                obj['self'] = ApiClient.convertToType(data['self'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccountResourceLinks</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccountResourceLinks</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccountResourceLinks.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['self'] && !(typeof data['self'] === 'string' || data['self'] instanceof String)) {
            throw new Error("Expected the field `self` to be a primitive type in the JSON string but got " + data['self']);
        }

        return true;
    }


}

AccountResourceLinks.RequiredProperties = ["self"];

/**
 * The canonical link to this resource within the API. 
 * @member {String} self
 */
AccountResourceLinks.prototype['self'] = undefined;






export default AccountResourceLinks;

