/**
 * Native Ads Publisher API
 * This is a Native Ads Publisher API it provides same functionality as Native Ads Publisher Account GUI. 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ReportsWidgetItem from './ReportsWidgetItem';
import Totals from './Totals';

/**
 * The ReportsWidgetResponse model module.
 * @module model/ReportsWidgetResponse
 * @version 1.0.0
 */
class ReportsWidgetResponse {
    /**
     * Constructs a new <code>ReportsWidgetResponse</code>.
     * @alias module:model/ReportsWidgetResponse
     */
    constructor() { 
        
        ReportsWidgetResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ReportsWidgetResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReportsWidgetResponse} obj Optional instance to populate.
     * @return {module:model/ReportsWidgetResponse} The populated <code>ReportsWidgetResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReportsWidgetResponse();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [ReportsWidgetItem]);
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
            if (data.hasOwnProperty('total_count')) {
                obj['total_count'] = ApiClient.convertToType(data['total_count'], 'Number');
            }
            if (data.hasOwnProperty('totals')) {
                obj['totals'] = Totals.constructFromObject(data['totals']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReportsWidgetResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReportsWidgetResponse</code>.
     */
    static validateJSON(data) {
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                ReportsWidgetItem.validateJSON(item);
            };
        }
        // validate the optional field `totals`
        if (data['totals']) { // data not null
          Totals.validateJSON(data['totals']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ReportsWidgetItem>} items
 */
ReportsWidgetResponse.prototype['items'] = undefined;

/**
 * @member {Boolean} success
 */
ReportsWidgetResponse.prototype['success'] = undefined;

/**
 * @member {Number} total_count
 */
ReportsWidgetResponse.prototype['total_count'] = undefined;

/**
 * @member {module:model/Totals} totals
 */
ReportsWidgetResponse.prototype['totals'] = undefined;






export default ReportsWidgetResponse;

