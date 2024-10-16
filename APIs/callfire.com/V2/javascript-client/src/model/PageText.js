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
import Text from './Text';

/**
 * The PageText model module.
 * @module model/PageText
 * @version V2
 */
class PageText {
    /**
     * Constructs a new <code>PageText</code>.
     * ~
     * @alias module:model/PageText
     */
    constructor() { 
        
        PageText.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PageText</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PageText} obj Optional instance to populate.
     * @return {module:model/PageText} The populated <code>PageText</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PageText();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [Text]);
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
     * Validates the JSON data with respect to <code>PageText</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PageText</code>.
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
 * ~
 * @member {Array.<module:model/Text>} items
 */
PageText.prototype['items'] = undefined;

/**
 * ~
 * @member {Number} limit
 */
PageText.prototype['limit'] = undefined;

/**
 * ~
 * @member {Number} offset
 */
PageText.prototype['offset'] = undefined;

/**
 * ~
 * @member {Number} totalCount
 */
PageText.prototype['totalCount'] = undefined;






export default PageText;

