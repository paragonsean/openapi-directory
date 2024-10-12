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
import SalesDataOrderInterface from './SalesDataOrderInterface';

/**
 * The SalesDataOrderSearchResultInterface model module.
 * @module model/SalesDataOrderSearchResultInterface
 * @version 2.2.10
 */
class SalesDataOrderSearchResultInterface {
    /**
     * Constructs a new <code>SalesDataOrderSearchResultInterface</code>.
     * Order search result interface. An order is a document that a web store issues to a customer. Magento generates a sales order that lists the product items, billing and shipping addresses, and shipping and payment methods. A corresponding external document, known as a purchase order, is emailed to the customer.
     * @alias module:model/SalesDataOrderSearchResultInterface
     * @param items {Array.<module:model/SalesDataOrderInterface>} Array of collection items.
     * @param searchCriteria {module:model/FrameworkSearchCriteriaInterface} 
     * @param totalCount {Number} Total count.
     */
    constructor(items, searchCriteria, totalCount) { 
        
        SalesDataOrderSearchResultInterface.initialize(this, items, searchCriteria, totalCount);
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
     * Constructs a <code>SalesDataOrderSearchResultInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesDataOrderSearchResultInterface} obj Optional instance to populate.
     * @return {module:model/SalesDataOrderSearchResultInterface} The populated <code>SalesDataOrderSearchResultInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesDataOrderSearchResultInterface();

            if (data.hasOwnProperty('items')) {
                obj['items'] = ApiClient.convertToType(data['items'], [SalesDataOrderInterface]);
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
     * Validates the JSON data with respect to <code>SalesDataOrderSearchResultInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesDataOrderSearchResultInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SalesDataOrderSearchResultInterface.RequiredProperties) {
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
                SalesDataOrderInterface.validateJSON(item);
            };
        }
        // validate the optional field `search_criteria`
        if (data['search_criteria']) { // data not null
          FrameworkSearchCriteriaInterface.validateJSON(data['search_criteria']);
        }

        return true;
    }


}

SalesDataOrderSearchResultInterface.RequiredProperties = ["items", "search_criteria", "total_count"];

/**
 * Array of collection items.
 * @member {Array.<module:model/SalesDataOrderInterface>} items
 */
SalesDataOrderSearchResultInterface.prototype['items'] = undefined;

/**
 * @member {module:model/FrameworkSearchCriteriaInterface} search_criteria
 */
SalesDataOrderSearchResultInterface.prototype['search_criteria'] = undefined;

/**
 * Total count.
 * @member {Number} total_count
 */
SalesDataOrderSearchResultInterface.prototype['total_count'] = undefined;






export default SalesDataOrderSearchResultInterface;

