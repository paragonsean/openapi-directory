/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UpdateNetworkMerakiAuthUserRequestAuthorizationsInner model module.
 * @module model/UpdateNetworkMerakiAuthUserRequestAuthorizationsInner
 * @version 1.32.0
 */
class UpdateNetworkMerakiAuthUserRequestAuthorizationsInner {
    /**
     * Constructs a new <code>UpdateNetworkMerakiAuthUserRequestAuthorizationsInner</code>.
     * @alias module:model/UpdateNetworkMerakiAuthUserRequestAuthorizationsInner
     * @param ssidNumber {Number} SSID for which the user is being authorized
     */
    constructor(ssidNumber) { 
        
        UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.initialize(this, ssidNumber);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, ssidNumber) { 
        obj['expiresAt'] = 'Never';
        obj['ssidNumber'] = ssidNumber;
    }

    /**
     * Constructs a <code>UpdateNetworkMerakiAuthUserRequestAuthorizationsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkMerakiAuthUserRequestAuthorizationsInner} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkMerakiAuthUserRequestAuthorizationsInner} The populated <code>UpdateNetworkMerakiAuthUserRequestAuthorizationsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkMerakiAuthUserRequestAuthorizationsInner();

            if (data.hasOwnProperty('expiresAt')) {
                obj['expiresAt'] = ApiClient.convertToType(data['expiresAt'], 'String');
            }
            if (data.hasOwnProperty('ssidNumber')) {
                obj['ssidNumber'] = ApiClient.convertToType(data['ssidNumber'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkMerakiAuthUserRequestAuthorizationsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkMerakiAuthUserRequestAuthorizationsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['expiresAt'] && !(typeof data['expiresAt'] === 'string' || data['expiresAt'] instanceof String)) {
            throw new Error("Expected the field `expiresAt` to be a primitive type in the JSON string but got " + data['expiresAt']);
        }

        return true;
    }


}

UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.RequiredProperties = ["ssidNumber"];

/**
 * Date for authorization to expire. Default is for authorization to not expire.
 * @member {String} expiresAt
 * @default 'Never'
 */
UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.prototype['expiresAt'] = 'Never';

/**
 * SSID for which the user is being authorized
 * @member {Number} ssidNumber
 */
UpdateNetworkMerakiAuthUserRequestAuthorizationsInner.prototype['ssidNumber'] = undefined;






export default UpdateNetworkMerakiAuthUserRequestAuthorizationsInner;

