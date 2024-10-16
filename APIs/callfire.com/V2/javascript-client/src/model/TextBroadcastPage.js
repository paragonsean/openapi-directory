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
import Page from './Page';
import TextBroadcast from './TextBroadcast';

/**
 * The TextBroadcastPage model module.
 * @module model/TextBroadcastPage
 * @version V2
 */
class TextBroadcastPage {
    /**
     * Constructs a new <code>TextBroadcastPage</code>.
     * ~
     * @alias module:model/TextBroadcastPage
     * @implements module:model/Page
     */
    constructor() { 
        Page.initialize(this);
        TextBroadcastPage.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TextBroadcastPage</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TextBroadcastPage} obj Optional instance to populate.
     * @return {module:model/TextBroadcastPage} The populated <code>TextBroadcastPage</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TextBroadcastPage();
            Page.constructFromObject(data, obj);

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [TextBroadcast]);
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
     * Validates the JSON data with respect to <code>TextBroadcastPage</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TextBroadcastPage</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                TextBroadcast.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/TextBroadcast>} items
 */
TextBroadcastPage.prototype['items'] = undefined;

/**
 * A maximum number of returned items. If items.size() < limit assume no more items
 * @member {Number} limit
 */
TextBroadcastPage.prototype['limit'] = undefined;

/**
 * An offset from a start of paging source
 * @member {Number} offset
 */
TextBroadcastPage.prototype['offset'] = undefined;

/**
 * Total count of available results. -1 if unknown
 * @member {Number} totalCount
 */
TextBroadcastPage.prototype['totalCount'] = undefined;


// Implement Page interface:
/**
 * A list of returned items
 * @member {Array.<Object>} items
 */
Page.prototype['items'] = undefined;
/**
 * A maximum number of returned items. If items.size() < limit assume no more items
 * @member {Number} limit
 */
Page.prototype['limit'] = undefined;
/**
 * An offset from a start of paging source
 * @member {Number} offset
 */
Page.prototype['offset'] = undefined;
/**
 * Total count of available results. -1 if unknown
 * @member {Number} totalCount
 */
Page.prototype['totalCount'] = undefined;




export default TextBroadcastPage;

