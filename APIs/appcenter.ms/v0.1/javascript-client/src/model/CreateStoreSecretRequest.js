/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import StoresCreateRequestIntuneDetailsSecretJson from './StoresCreateRequestIntuneDetailsSecretJson';

/**
 * The CreateStoreSecretRequest model module.
 * @module model/CreateStoreSecretRequest
 * @version v0.1
 */
class CreateStoreSecretRequest {
    /**
     * Constructs a new <code>CreateStoreSecretRequest</code>.
     * @alias module:model/CreateStoreSecretRequest
     */
    constructor() { 
        
        CreateStoreSecretRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateStoreSecretRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateStoreSecretRequest} obj Optional instance to populate.
     * @return {module:model/CreateStoreSecretRequest} The populated <code>CreateStoreSecretRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateStoreSecretRequest();

            if (data.hasOwnProperty('secret_json')) {
                obj['secret_json'] = StoresCreateRequestIntuneDetailsSecretJson.constructFromObject(data['secret_json']);
            }
            if (data.hasOwnProperty('tenant_id')) {
                obj['tenant_id'] = ApiClient.convertToType(data['tenant_id'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateStoreSecretRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateStoreSecretRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `secret_json`
        if (data['secret_json']) { // data not null
          StoresCreateRequestIntuneDetailsSecretJson.validateJSON(data['secret_json']);
        }
        // ensure the json data is a string
        if (data['tenant_id'] && !(typeof data['tenant_id'] === 'string' || data['tenant_id'] instanceof String)) {
            throw new Error("Expected the field `tenant_id` to be a primitive type in the JSON string but got " + data['tenant_id']);
        }

        return true;
    }


}



/**
 * @member {module:model/StoresCreateRequestIntuneDetailsSecretJson} secret_json
 */
CreateStoreSecretRequest.prototype['secret_json'] = undefined;

/**
 * the tenant id for user
 * @member {String} tenant_id
 */
CreateStoreSecretRequest.prototype['tenant_id'] = undefined;






export default CreateStoreSecretRequest;

