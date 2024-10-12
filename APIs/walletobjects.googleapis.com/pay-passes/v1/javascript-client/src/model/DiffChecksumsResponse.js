/**
 * Google Pay Passes API
 * API for issuers to save and manage Google Wallet Objects.
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import CompositeMedia from './CompositeMedia';

/**
 * The DiffChecksumsResponse model module.
 * @module model/DiffChecksumsResponse
 * @version v1
 */
class DiffChecksumsResponse {
    /**
     * Constructs a new <code>DiffChecksumsResponse</code>.
     * Backend response for a Diff get checksums response. For details on the Scotty Diff protocol, visit http://go/scotty-diff-protocol.
     * @alias module:model/DiffChecksumsResponse
     */
    constructor() { 
        
        DiffChecksumsResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DiffChecksumsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DiffChecksumsResponse} obj Optional instance to populate.
     * @return {module:model/DiffChecksumsResponse} The populated <code>DiffChecksumsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DiffChecksumsResponse();

            if (data.hasOwnProperty('checksumsLocation')) {
                obj['checksumsLocation'] = CompositeMedia.constructFromObject(data['checksumsLocation']);
            }
            if (data.hasOwnProperty('chunkSizeBytes')) {
                obj['chunkSizeBytes'] = ApiClient.convertToType(data['chunkSizeBytes'], 'String');
            }
            if (data.hasOwnProperty('objectLocation')) {
                obj['objectLocation'] = CompositeMedia.constructFromObject(data['objectLocation']);
            }
            if (data.hasOwnProperty('objectSizeBytes')) {
                obj['objectSizeBytes'] = ApiClient.convertToType(data['objectSizeBytes'], 'String');
            }
            if (data.hasOwnProperty('objectVersion')) {
                obj['objectVersion'] = ApiClient.convertToType(data['objectVersion'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DiffChecksumsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DiffChecksumsResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `checksumsLocation`
        if (data['checksumsLocation']) { // data not null
          CompositeMedia.validateJSON(data['checksumsLocation']);
        }
        // ensure the json data is a string
        if (data['chunkSizeBytes'] && !(typeof data['chunkSizeBytes'] === 'string' || data['chunkSizeBytes'] instanceof String)) {
            throw new Error("Expected the field `chunkSizeBytes` to be a primitive type in the JSON string but got " + data['chunkSizeBytes']);
        }
        // validate the optional field `objectLocation`
        if (data['objectLocation']) { // data not null
          CompositeMedia.validateJSON(data['objectLocation']);
        }
        // ensure the json data is a string
        if (data['objectSizeBytes'] && !(typeof data['objectSizeBytes'] === 'string' || data['objectSizeBytes'] instanceof String)) {
            throw new Error("Expected the field `objectSizeBytes` to be a primitive type in the JSON string but got " + data['objectSizeBytes']);
        }
        // ensure the json data is a string
        if (data['objectVersion'] && !(typeof data['objectVersion'] === 'string' || data['objectVersion'] instanceof String)) {
            throw new Error("Expected the field `objectVersion` to be a primitive type in the JSON string but got " + data['objectVersion']);
        }

        return true;
    }


}



/**
 * @member {module:model/CompositeMedia} checksumsLocation
 */
DiffChecksumsResponse.prototype['checksumsLocation'] = undefined;

/**
 * The chunk size of checksums. Must be a multiple of 256KB.
 * @member {String} chunkSizeBytes
 */
DiffChecksumsResponse.prototype['chunkSizeBytes'] = undefined;

/**
 * @member {module:model/CompositeMedia} objectLocation
 */
DiffChecksumsResponse.prototype['objectLocation'] = undefined;

/**
 * The total size of the server object.
 * @member {String} objectSizeBytes
 */
DiffChecksumsResponse.prototype['objectSizeBytes'] = undefined;

/**
 * The object version of the object the checksums are being returned for.
 * @member {String} objectVersion
 */
DiffChecksumsResponse.prototype['objectVersion'] = undefined;






export default DiffChecksumsResponse;

