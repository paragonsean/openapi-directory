/**
 * Storage Cache Mgmt Client
 * A Storage Cache provides scalable caching service for NAS clients, serving data from either NFSv3 or Blob at-rest storage (referred to as \"Storage Targets\"). These operations allow you to manage Caches.
 *
 * The version of the OpenAPI document: 2019-11-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CloudErrorBody from './CloudErrorBody';

/**
 * The CloudError model module.
 * @module model/CloudError
 * @version 2019-11-01
 */
class CloudError {
    /**
     * Constructs a new <code>CloudError</code>.
     * An error response.
     * @alias module:model/CloudError
     */
    constructor() { 
        
        CloudError.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CloudError</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CloudError} obj Optional instance to populate.
     * @return {module:model/CloudError} The populated <code>CloudError</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CloudError();

            if (data.hasOwnProperty('error')) {
                obj['error'] = CloudErrorBody.constructFromObject(data['error']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CloudError</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CloudError</code>.
     */
    static validateJSON(data) {
        // validate the optional field `error`
        if (data['error']) { // data not null
          CloudErrorBody.validateJSON(data['error']);
        }

        return true;
    }


}



/**
 * @member {module:model/CloudErrorBody} error
 */
CloudError.prototype['error'] = undefined;






export default CloudError;

