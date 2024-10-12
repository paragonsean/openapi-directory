/**
 * MySQLManagementClient
 * The Microsoft Azure management API provides create, read, update, and delete functionality for Azure MySQL resources including servers, databases, firewall rules, VNET rules, security alert policies, log files and configurations with new business model.
 *
 * The version of the OpenAPI document: 2018-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import QueryStatistic from './QueryStatistic';

/**
 * The TopQueryStatisticsResultList model module.
 * @module model/TopQueryStatisticsResultList
 * @version 2018-06-01
 */
class TopQueryStatisticsResultList {
    /**
     * Constructs a new <code>TopQueryStatisticsResultList</code>.
     * A list of query statistics.
     * @alias module:model/TopQueryStatisticsResultList
     */
    constructor() { 
        
        TopQueryStatisticsResultList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TopQueryStatisticsResultList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TopQueryStatisticsResultList} obj Optional instance to populate.
     * @return {module:model/TopQueryStatisticsResultList} The populated <code>TopQueryStatisticsResultList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TopQueryStatisticsResultList();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [QueryStatistic]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TopQueryStatisticsResultList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TopQueryStatisticsResultList</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['nextLink'] && !(typeof data['nextLink'] === 'string' || data['nextLink'] instanceof String)) {
            throw new Error("Expected the field `nextLink` to be a primitive type in the JSON string but got " + data['nextLink']);
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                QueryStatistic.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Link to retrieve next page of results.
 * @member {String} nextLink
 */
TopQueryStatisticsResultList.prototype['nextLink'] = undefined;

/**
 * The list of top query statistics.
 * @member {Array.<module:model/QueryStatistic>} value
 */
TopQueryStatisticsResultList.prototype['value'] = undefined;






export default TopQueryStatisticsResultList;

