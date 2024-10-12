/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2018-02-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties from './ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties';

/**
 * The ListSiteIdentifiersAssignedToHostName200ResponseValueInner model module.
 * @module model/ListSiteIdentifiersAssignedToHostName200ResponseValueInner
 * @version 2018-02-01
 */
class ListSiteIdentifiersAssignedToHostName200ResponseValueInner {
    /**
     * Constructs a new <code>ListSiteIdentifiersAssignedToHostName200ResponseValueInner</code>.
     * A domain specific resource identifier.
     * @alias module:model/ListSiteIdentifiersAssignedToHostName200ResponseValueInner
     */
    constructor() { 
        
        ListSiteIdentifiersAssignedToHostName200ResponseValueInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListSiteIdentifiersAssignedToHostName200ResponseValueInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListSiteIdentifiersAssignedToHostName200ResponseValueInner} obj Optional instance to populate.
     * @return {module:model/ListSiteIdentifiersAssignedToHostName200ResponseValueInner} The populated <code>ListSiteIdentifiersAssignedToHostName200ResponseValueInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListSiteIdentifiersAssignedToHostName200ResponseValueInner();

            if (data.hasOwnProperty('properties')) {
                obj['properties'] = ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.constructFromObject(data['properties']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListSiteIdentifiersAssignedToHostName200ResponseValueInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListSiteIdentifiersAssignedToHostName200ResponseValueInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties.validateJSON(data['properties']);
        }

        return true;
    }


}



/**
 * @member {module:model/ListSiteIdentifiersAssignedToHostName200ResponseValueInnerProperties} properties
 */
ListSiteIdentifiersAssignedToHostName200ResponseValueInner.prototype['properties'] = undefined;






export default ListSiteIdentifiersAssignedToHostName200ResponseValueInner;

