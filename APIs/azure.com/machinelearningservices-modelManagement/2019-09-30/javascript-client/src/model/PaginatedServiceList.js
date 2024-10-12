/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-09-30
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ServiceResponseBase from './ServiceResponseBase';

/**
 * The PaginatedServiceList model module.
 * @module model/PaginatedServiceList
 * @version 2019-09-30
 */
class PaginatedServiceList {
    /**
     * Constructs a new <code>PaginatedServiceList</code>.
     * A paginated list of Services.
     * @alias module:model/PaginatedServiceList
     */
    constructor() { 
        
        PaginatedServiceList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PaginatedServiceList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PaginatedServiceList} obj Optional instance to populate.
     * @return {module:model/PaginatedServiceList} The populated <code>PaginatedServiceList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PaginatedServiceList();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [ServiceResponseBase]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PaginatedServiceList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PaginatedServiceList</code>.
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
                ServiceResponseBase.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * A continuation link (absolute URI) to the next page of results in the list.
 * @member {String} nextLink
 */
PaginatedServiceList.prototype['nextLink'] = undefined;

/**
 * An array of objects of type Service.
 * @member {Array.<module:model/ServiceResponseBase>} value
 */
PaginatedServiceList.prototype['value'] = undefined;






export default PaginatedServiceList;

