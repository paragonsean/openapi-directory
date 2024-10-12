/**
 * StorSimple8000SeriesManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2017-06-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import AccessControlRecord from './AccessControlRecord';

/**
 * The AccessControlRecordList model module.
 * @module model/AccessControlRecordList
 * @version 2017-06-01
 */
class AccessControlRecordList {
    /**
     * Constructs a new <code>AccessControlRecordList</code>.
     * The collection of access control records.
     * @alias module:model/AccessControlRecordList
     * @param value {Array.<module:model/AccessControlRecord>} The value.
     */
    constructor(value) { 
        
        AccessControlRecordList.initialize(this, value);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, value) { 
        obj['value'] = value;
    }

    /**
     * Constructs a <code>AccessControlRecordList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccessControlRecordList} obj Optional instance to populate.
     * @return {module:model/AccessControlRecordList} The populated <code>AccessControlRecordList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccessControlRecordList();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [AccessControlRecord]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccessControlRecordList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccessControlRecordList</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccessControlRecordList.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                AccessControlRecord.validateJSON(item);
            };
        }

        return true;
    }


}

AccessControlRecordList.RequiredProperties = ["value"];

/**
 * The value.
 * @member {Array.<module:model/AccessControlRecord>} value
 */
AccessControlRecordList.prototype['value'] = undefined;






export default AccessControlRecordList;

