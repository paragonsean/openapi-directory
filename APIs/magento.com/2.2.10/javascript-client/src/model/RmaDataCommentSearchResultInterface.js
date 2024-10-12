/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import FrameworkSearchCriteriaInterface from './FrameworkSearchCriteriaInterface';
import RmaDataCommentInterface from './RmaDataCommentInterface';

/**
 * The RmaDataCommentSearchResultInterface model module.
 * @module model/RmaDataCommentSearchResultInterface
 * @version 2.2.10
 */
class RmaDataCommentSearchResultInterface {
    /**
     * Constructs a new <code>RmaDataCommentSearchResultInterface</code>.
     * Interface CommentSearchResultInterface
     * @alias module:model/RmaDataCommentSearchResultInterface
     * @param items {Array.<module:model/RmaDataCommentInterface>} Rma Status History list
     * @param searchCriteria {module:model/FrameworkSearchCriteriaInterface} 
     * @param totalCount {Number} Total count.
     */
    constructor(items, searchCriteria, totalCount) { 
        
        RmaDataCommentSearchResultInterface.initialize(this, items, searchCriteria, totalCount);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, items, searchCriteria, totalCount) { 
        obj['items'] = items;
        obj['search_criteria'] = searchCriteria;
        obj['total_count'] = totalCount;
    }

    /**
     * Constructs a <code>RmaDataCommentSearchResultInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RmaDataCommentSearchResultInterface} obj Optional instance to populate.
     * @return {module:model/RmaDataCommentSearchResultInterface} The populated <code>RmaDataCommentSearchResultInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RmaDataCommentSearchResultInterface();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [RmaDataCommentInterface]);
            }
            if (data.hasOwnProperty('search_criteria')) {
                obj['search_criteria'] = FrameworkSearchCriteriaInterface.constructFromObject(data['search_criteria']);
            }
            if (data.hasOwnProperty('total_count')) {
                obj['total_count'] = ApiClient.convertToType(data['total_count'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RmaDataCommentSearchResultInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RmaDataCommentSearchResultInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RmaDataCommentSearchResultInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['items'])) {
                throw new Error("Expected the field `items` to be an array in the JSON data but got " + data['items']);
            }
            // validate the optional field `items` (array)
            for (const item of data['items']) {
                RmaDataCommentInterface.validateJSON(item);
            };
        }
        // validate the optional field `search_criteria`
        if (data['search_criteria']) { // data not null
          FrameworkSearchCriteriaInterface.validateJSON(data['search_criteria']);
        }

        return true;
    }


}

RmaDataCommentSearchResultInterface.RequiredProperties = ["items", "search_criteria", "total_count"];

/**
 * Rma Status History list
 * @member {Array.<module:model/RmaDataCommentInterface>} items
 */
RmaDataCommentSearchResultInterface.prototype['items'] = undefined;

/**
 * @member {module:model/FrameworkSearchCriteriaInterface} search_criteria
 */
RmaDataCommentSearchResultInterface.prototype['search_criteria'] = undefined;

/**
 * Total count.
 * @member {Number} total_count
 */
RmaDataCommentSearchResultInterface.prototype['total_count'] = undefined;






export default RmaDataCommentSearchResultInterface;

