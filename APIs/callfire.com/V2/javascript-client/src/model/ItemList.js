/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ItemList model module.
 * @module model/ItemList
 * @version V2
 */
class ItemList {
    /**
     * Constructs a new <code>ItemList</code>.
     * ~
     * @alias module:model/ItemList
     */
    constructor() { 
        
        ItemList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ItemList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ItemList} obj Optional instance to populate.
     * @return {module:model/ItemList} The populated <code>ItemList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ItemList();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [Object]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ItemList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ItemList</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['items'])) {
            throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
        }

        return true;
    }


}



/**
 * ~
 * @member {Array.<Object>} items
 */
ItemList.prototype['items'] = undefined;






export default ItemList;

