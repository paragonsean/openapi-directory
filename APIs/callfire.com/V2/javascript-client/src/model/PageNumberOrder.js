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
import NumberOrder from './NumberOrder';

/**
 * The PageNumberOrder model module.
 * @module model/PageNumberOrder
 * @version V2
 */
class PageNumberOrder {
    /**
     * Constructs a new <code>PageNumberOrder</code>.
     * ~
     * @alias module:model/PageNumberOrder
     */
    constructor() { 
        
        PageNumberOrder.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PageNumberOrder</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PageNumberOrder} obj Optional instance to populate.
     * @return {module:model/PageNumberOrder} The populated <code>PageNumberOrder</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PageNumberOrder();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [NumberOrder]);
            }
            if (data.hasOwnProperty('limit')) {
                obj['limit'] = ApiClient.convertToType(data['limit'], 'Number');
            }
            if (data.hasOwnProperty('offset')) {
                obj['offset'] = ApiClient.convertToType(data['offset'], 'Number');
            }
            if (data.hasOwnProperty('totalCount')) {
                obj['totalCount'] = ApiClient.convertToType(data['totalCount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PageNumberOrder</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PageNumberOrder</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                NumberOrder.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * ~
 * @member {Array.<module:model/NumberOrder>} items
 */
PageNumberOrder.prototype['items'] = undefined;

/**
 * ~
 * @member {Number} limit
 */
PageNumberOrder.prototype['limit'] = undefined;

/**
 * ~
 * @member {Number} offset
 */
PageNumberOrder.prototype['offset'] = undefined;

/**
 * ~
 * @member {Number} totalCount
 */
PageNumberOrder.prototype['totalCount'] = undefined;






export default PageNumberOrder;

