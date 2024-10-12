/**
 * Azure Machine Learning Model Management Service
 * These APIs allow end users to manage Azure Machine Learning Models, Images, Profiles, and Services.
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The EnvironmentImageAsset model module.
 * @module model/EnvironmentImageAsset
 * @version 2019-08-01
 */
class EnvironmentImageAsset {
    /**
     * Constructs a new <code>EnvironmentImageAsset</code>.
     * An Image asset.
     * @alias module:model/EnvironmentImageAsset
     */
    constructor() { 
        
        EnvironmentImageAsset.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EnvironmentImageAsset</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EnvironmentImageAsset} obj Optional instance to populate.
     * @return {module:model/EnvironmentImageAsset} The populated <code>EnvironmentImageAsset</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EnvironmentImageAsset();

            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('mimeType')) {
                obj['mimeType'] = ApiClient.convertToType(data['mimeType'], 'String');
            }
            if (data.hasOwnProperty('unpack')) {
                obj['unpack'] = ApiClient.convertToType(data['unpack'], 'Boolean');
            }
            if (data.hasOwnProperty('url')) {
                obj['url'] = ApiClient.convertToType(data['url'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EnvironmentImageAsset</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EnvironmentImageAsset</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // ensure the json data is a string
        if (data['mimeType'] && !(typeof data['mimeType'] === 'string' || data['mimeType'] instanceof String)) {
            throw new Error("Expected the field `mimeType` to be a primitive type in the JSON string but got " + data['mimeType']);
        }
        // ensure the json data is a string
        if (data['url'] && !(typeof data['url'] === 'string' || data['url'] instanceof String)) {
            throw new Error("Expected the field `url` to be a primitive type in the JSON string but got " + data['url']);
        }

        return true;
    }


}



/**
 * The Asset Id.
 * @member {String} id
 */
EnvironmentImageAsset.prototype['id'] = undefined;

/**
 * The mime type.
 * @member {String} mimeType
 */
EnvironmentImageAsset.prototype['mimeType'] = undefined;

/**
 * Whether the Asset is unpacked.
 * @member {Boolean} unpack
 */
EnvironmentImageAsset.prototype['unpack'] = undefined;

/**
 * The Url of the Asset.
 * @member {String} url
 */
EnvironmentImageAsset.prototype['url'] = undefined;






export default EnvironmentImageAsset;

