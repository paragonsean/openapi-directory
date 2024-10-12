/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Icon from './Icon';

/**
 * The ListIconsResponse model module.
 * @module model/ListIconsResponse
 * @version v3
 */
class ListIconsResponse {
    /**
     * Constructs a new <code>ListIconsResponse</code>.
     * Response message for IconService.ListIcons.
     * @alias module:model/ListIconsResponse
     */
    constructor() { 
        
        ListIconsResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListIconsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListIconsResponse} obj Optional instance to populate.
     * @return {module:model/ListIconsResponse} The populated <code>ListIconsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListIconsResponse();

            if (data.hasOwnProperty('icons')) {
                obj['icons'] = ApiClient.convertToType(data['icons'], [Icon]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListIconsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListIconsResponse</code>.
     */
    static validateJSON(data) {
        if (data['icons']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['icons'])) {
                throw new Error("Expected the field `icons` to be an array in the JSON data but got " + data['icons']);
            }
            // validate the optional field `icons` (array)
            for (const item of data['icons']) {
                Icon.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * A list of all icons associated with the queried partner account.
 * @member {Array.<module:model/Icon>} icons
 */
ListIconsResponse.prototype['icons'] = undefined;






export default ListIconsResponse;

