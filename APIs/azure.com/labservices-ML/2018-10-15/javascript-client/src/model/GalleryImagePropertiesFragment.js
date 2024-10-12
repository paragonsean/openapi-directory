/**
 * ManagedLabsClient
 * The Managed Labs Client.
 *
 * The version of the OpenAPI document: 2018-10-15
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The GalleryImagePropertiesFragment model module.
 * @module model/GalleryImagePropertiesFragment
 * @version 2018-10-15
 */
class GalleryImagePropertiesFragment {
    /**
     * Constructs a new <code>GalleryImagePropertiesFragment</code>.
     * The gallery image properties
     * @alias module:model/GalleryImagePropertiesFragment
     */
    constructor() { 
        
        GalleryImagePropertiesFragment.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GalleryImagePropertiesFragment</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GalleryImagePropertiesFragment} obj Optional instance to populate.
     * @return {module:model/GalleryImagePropertiesFragment} The populated <code>GalleryImagePropertiesFragment</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GalleryImagePropertiesFragment();

            if (data.hasOwnProperty('isEnabled')) {
                obj['isEnabled'] = ApiClient.convertToType(data['isEnabled'], 'Boolean');
            }
            if (data.hasOwnProperty('isOverride')) {
                obj['isOverride'] = ApiClient.convertToType(data['isOverride'], 'Boolean');
            }
            if (data.hasOwnProperty('isPlanAuthorized')) {
                obj['isPlanAuthorized'] = ApiClient.convertToType(data['isPlanAuthorized'], 'Boolean');
            }
            if (data.hasOwnProperty('provisioningState')) {
                obj['provisioningState'] = ApiClient.convertToType(data['provisioningState'], 'String');
            }
            if (data.hasOwnProperty('uniqueIdentifier')) {
                obj['uniqueIdentifier'] = ApiClient.convertToType(data['uniqueIdentifier'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GalleryImagePropertiesFragment</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GalleryImagePropertiesFragment</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['provisioningState'] && !(typeof data['provisioningState'] === 'string' || data['provisioningState'] instanceof String)) {
            throw new Error("Expected the field `provisioningState` to be a primitive type in the JSON string but got " + data['provisioningState']);
        }
        // ensure the json data is a string
        if (data['uniqueIdentifier'] && !(typeof data['uniqueIdentifier'] === 'string' || data['uniqueIdentifier'] instanceof String)) {
            throw new Error("Expected the field `uniqueIdentifier` to be a primitive type in the JSON string but got " + data['uniqueIdentifier']);
        }

        return true;
    }


}



/**
 * Indicates whether this gallery image is enabled.
 * @member {Boolean} isEnabled
 */
GalleryImagePropertiesFragment.prototype['isEnabled'] = undefined;

/**
 * Indicates whether this gallery has been overridden for this lab account
 * @member {Boolean} isOverride
 */
GalleryImagePropertiesFragment.prototype['isOverride'] = undefined;

/**
 * Indicates if the plan has been authorized for programmatic deployment.
 * @member {Boolean} isPlanAuthorized
 */
GalleryImagePropertiesFragment.prototype['isPlanAuthorized'] = undefined;

/**
 * The provisioning status of the resource.
 * @member {String} provisioningState
 */
GalleryImagePropertiesFragment.prototype['provisioningState'] = undefined;

/**
 * The unique immutable identifier of a resource (Guid).
 * @member {String} uniqueIdentifier
 */
GalleryImagePropertiesFragment.prototype['uniqueIdentifier'] = undefined;






export default GalleryImagePropertiesFragment;

