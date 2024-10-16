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
import UniversalDoNotContact from './UniversalDoNotContact';

/**
 * The ItemListUniversalDoNotContact model module.
 * @module model/ItemListUniversalDoNotContact
 * @version V2
 */
class ItemListUniversalDoNotContact {
    /**
     * Constructs a new <code>ItemListUniversalDoNotContact</code>.
     * ~
     * @alias module:model/ItemListUniversalDoNotContact
     */
    constructor() { 
        
        ItemListUniversalDoNotContact.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ItemListUniversalDoNotContact</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ItemListUniversalDoNotContact} obj Optional instance to populate.
     * @return {module:model/ItemListUniversalDoNotContact} The populated <code>ItemListUniversalDoNotContact</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ItemListUniversalDoNotContact();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [UniversalDoNotContact]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ItemListUniversalDoNotContact</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ItemListUniversalDoNotContact</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                UniversalDoNotContact.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * ~
 * @member {Array.<module:model/UniversalDoNotContact>} items
 */
ItemListUniversalDoNotContact.prototype['items'] = undefined;






export default ItemListUniversalDoNotContact;

