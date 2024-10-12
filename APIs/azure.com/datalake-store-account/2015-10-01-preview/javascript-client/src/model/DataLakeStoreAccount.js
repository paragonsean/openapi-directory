/**
 * DataLakeStoreAccountManagementClient
 * Creates an Azure Data Lake Store account management client.
 *
 * The version of the OpenAPI document: 2015-10-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import DataLakeStoreAccountProperties from './DataLakeStoreAccountProperties';
import EncryptionIdentity from './EncryptionIdentity';

/**
 * The DataLakeStoreAccount model module.
 * @module model/DataLakeStoreAccount
 * @version 2015-10-01-preview
 */
class DataLakeStoreAccount {
    /**
     * Constructs a new <code>DataLakeStoreAccount</code>.
     * Data Lake Store account information
     * @alias module:model/DataLakeStoreAccount
     */
    constructor() { 
        
        DataLakeStoreAccount.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DataLakeStoreAccount</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DataLakeStoreAccount} obj Optional instance to populate.
     * @return {module:model/DataLakeStoreAccount} The populated <code>DataLakeStoreAccount</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DataLakeStoreAccount();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('identity')) {
                obj['identity'] = EncryptionIdentity.constructFromObject(data['identity']);
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = ApiClient.convertToType(data['location'], 'String');
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('properties')) {
                obj['properties'] = DataLakeStoreAccountProperties.constructFromObject(data['properties']);
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], {'String': 'String'});
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DataLakeStoreAccount</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DataLakeStoreAccount</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `identity`
        if (data['identity']) { // data not null
          EncryptionIdentity.validateJSON(data['identity']);
        }
        // ensure the json data is a string
        if (data['location'] && !(typeof data['location'] === 'string' || data['location'] instanceof String)) {
            throw new Error("Expected the field `location` to be a primitive type in the JSON string but got " + data['location']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // validate the optional field `properties`
        if (data['properties']) { // data not null
          DataLakeStoreAccountProperties.validateJSON(data['properties']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * the account subscription ID.
 * @member {String} id
 */
DataLakeStoreAccount.prototype['id'] = undefined;

/**
 * @member {module:model/EncryptionIdentity} identity
 */
DataLakeStoreAccount.prototype['identity'] = undefined;

/**
 * the account regional location.
 * @member {String} location
 */
DataLakeStoreAccount.prototype['location'] = undefined;

/**
 * the account name.
 * @member {String} name
 */
DataLakeStoreAccount.prototype['name'] = undefined;

/**
 * @member {module:model/DataLakeStoreAccountProperties} properties
 */
DataLakeStoreAccount.prototype['properties'] = undefined;

/**
 * the value of custom properties.
 * @member {Object.<String, String>} tags
 */
DataLakeStoreAccount.prototype['tags'] = undefined;

/**
 * the namespace and type of the account.
 * @member {String} type
 */
DataLakeStoreAccount.prototype['type'] = undefined;






export default DataLakeStoreAccount;

