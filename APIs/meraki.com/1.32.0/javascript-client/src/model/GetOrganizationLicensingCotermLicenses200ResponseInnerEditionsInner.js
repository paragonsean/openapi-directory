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
 * The GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner model module.
 * @module model/GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner
 * @version 1.32.0
 */
class GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner {
    /**
     * Constructs a new <code>GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner</code>.
     * @alias module:model/GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner
     */
    constructor() { 
        
        GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner} obj Optional instance to populate.
     * @return {module:model/GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner} The populated <code>GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner();

            if (data.hasOwnProperty('edition')) {
                obj['edition'] = ApiClient.convertToType(data['edition'], 'String');
            }
            if (data.hasOwnProperty('productType')) {
                obj['productType'] = ApiClient.convertToType(data['productType'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['edition'] && !(typeof data['edition'] === 'string' || data['edition'] instanceof String)) {
            throw new Error("Expected the field `edition` to be a primitive type in the JSON string but got " + data['edition']);
        }
        // ensure the json data is a string
        if (data['productType'] && !(typeof data['productType'] === 'string' || data['productType'] instanceof String)) {
            throw new Error("Expected the field `productType` to be a primitive type in the JSON string but got " + data['productType']);
        }

        return true;
    }


}



/**
 * The name of the license edition
 * @member {String} edition
 */
GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner.prototype['edition'] = undefined;

/**
 * The product type of the license edition
 * @member {String} productType
 */
GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner.prototype['productType'] = undefined;






export default GetOrganizationLicensingCotermLicenses200ResponseInnerEditionsInner;

