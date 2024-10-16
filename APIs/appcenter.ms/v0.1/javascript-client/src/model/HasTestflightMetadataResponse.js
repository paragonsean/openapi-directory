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

/**
 * The HasTestflightMetadataResponse model module.
 * @module model/HasTestflightMetadataResponse
 * @version v0.1
 */
class HasTestflightMetadataResponse {
    /**
     * Constructs a new <code>HasTestflightMetadataResponse</code>.
     * The response for the testflight metadata check.
     * @alias module:model/HasTestflightMetadataResponse
     */
    constructor() { 
        
        HasTestflightMetadataResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>HasTestflightMetadataResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HasTestflightMetadataResponse} obj Optional instance to populate.
     * @return {module:model/HasTestflightMetadataResponse} The populated <code>HasTestflightMetadataResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HasTestflightMetadataResponse();

            if (data.hasOwnProperty('has_testflight_metadata')) {
                obj['has_testflight_metadata'] = ApiClient.convertToType(data['has_testflight_metadata'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HasTestflightMetadataResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HasTestflightMetadataResponse</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * true if the app has the testflight metadata, false otherwise
 * @member {Boolean} has_testflight_metadata
 */
HasTestflightMetadataResponse.prototype['has_testflight_metadata'] = undefined;






export default HasTestflightMetadataResponse;

