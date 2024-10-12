/**
 * DataBoxEdgeManagementClient
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 2019-03-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import StorageAccountCredential from './StorageAccountCredential';

/**
 * The StorageAccountCredentialList model module.
 * @module model/StorageAccountCredentialList
 * @version 2019-03-01
 */
class StorageAccountCredentialList {
    /**
     * Constructs a new <code>StorageAccountCredentialList</code>.
     * The collection of storage account credentials.
     * @alias module:model/StorageAccountCredentialList
     */
    constructor() { 
        
        StorageAccountCredentialList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>StorageAccountCredentialList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/StorageAccountCredentialList} obj Optional instance to populate.
     * @return {module:model/StorageAccountCredentialList} The populated <code>StorageAccountCredentialList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new StorageAccountCredentialList();

            if (data.hasOwnProperty('nextLink')) {
                obj['nextLink'] = ApiClient.convertToType(data['nextLink'], 'String');
            }
            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [StorageAccountCredential]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>StorageAccountCredentialList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>StorageAccountCredentialList</code>.
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
                StorageAccountCredential.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Link to the next set of results.
 * @member {String} nextLink
 */
StorageAccountCredentialList.prototype['nextLink'] = undefined;

/**
 * The value.
 * @member {Array.<module:model/StorageAccountCredential>} value
 */
StorageAccountCredentialList.prototype['value'] = undefined;






export default StorageAccountCredentialList;

