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
import ItemList from './ItemList';
import Text from './Text';

/**
 * The TextList model module.
 * @module model/TextList
 * @version V2
 */
class TextList {
    /**
     * Constructs a new <code>TextList</code>.
     * ~
     * @alias module:model/TextList
     * @implements module:model/ItemList
     */
    constructor() { 
        ItemList.initialize(this);
        TextList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TextList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TextList} obj Optional instance to populate.
     * @return {module:model/TextList} The populated <code>TextList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TextList();
            ItemList.constructFromObject(data, obj);

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [Text]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TextList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TextList</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                Text.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/Text>} items
 */
TextList.prototype['items'] = undefined;


// Implement ItemList interface:
/**
 * ~
 * @member {Array.<Object>} items
 */
ItemList.prototype['items'] = undefined;




export default TextList;

