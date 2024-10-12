/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
import AllEntityType from './AllEntityType';

/**
 * The SearchMembershipCriteria model module.
 * @module model/SearchMembershipCriteria
 * @version 1.0.0
 */
class SearchMembershipCriteria {
    /**
     * Constructs a new <code>SearchMembershipCriteria</code>.
     * @alias module:model/SearchMembershipCriteria
     */
    constructor() { 
        
        SearchMembershipCriteria.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SearchMembershipCriteria</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SearchMembershipCriteria} obj Optional instance to populate.
     * @return {module:model/SearchMembershipCriteria} The populated <code>SearchMembershipCriteria</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SearchMembershipCriteria();

            if (data.hasOwnProperty('entity_type')) {
                obj['entity_type'] = AllEntityType.constructFromObject(data['entity_type']);
            }
            if (data.hasOwnProperty('filter')) {
                obj['filter'] = ApiClient.convertToType(data['filter'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SearchMembershipCriteria</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SearchMembershipCriteria</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['filter'] && !(typeof data['filter'] === 'string' || data['filter'] instanceof String)) {
            throw new Error("Expected the field `filter` to be a primitive type in the JSON string but got " + data['filter']);
        }

        return true;
    }


}



/**
 * @member {module:model/AllEntityType} entity_type
 */
SearchMembershipCriteria.prototype['entity_type'] = undefined;

/**
 * As defined in search end point
 * @member {String} filter
 */
SearchMembershipCriteria.prototype['filter'] = undefined;






export default SearchMembershipCriteria;

