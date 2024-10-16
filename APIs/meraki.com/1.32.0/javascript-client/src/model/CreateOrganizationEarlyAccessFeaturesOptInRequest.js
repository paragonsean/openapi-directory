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
 * The CreateOrganizationEarlyAccessFeaturesOptInRequest model module.
 * @module model/CreateOrganizationEarlyAccessFeaturesOptInRequest
 * @version 1.32.0
 */
class CreateOrganizationEarlyAccessFeaturesOptInRequest {
    /**
     * Constructs a new <code>CreateOrganizationEarlyAccessFeaturesOptInRequest</code>.
     * @alias module:model/CreateOrganizationEarlyAccessFeaturesOptInRequest
     * @param shortName {String} Short name of the early access feature
     */
    constructor(shortName) { 
        
        CreateOrganizationEarlyAccessFeaturesOptInRequest.initialize(this, shortName);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, shortName) { 
        obj['shortName'] = shortName;
    }

    /**
     * Constructs a <code>CreateOrganizationEarlyAccessFeaturesOptInRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateOrganizationEarlyAccessFeaturesOptInRequest} obj Optional instance to populate.
     * @return {module:model/CreateOrganizationEarlyAccessFeaturesOptInRequest} The populated <code>CreateOrganizationEarlyAccessFeaturesOptInRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateOrganizationEarlyAccessFeaturesOptInRequest();

            if (data.hasOwnProperty('limitScopeToNetworks')) {
                obj['limitScopeToNetworks'] = ApiClient.convertToType(data['limitScopeToNetworks'], ['String']);
            }
            if (data.hasOwnProperty('shortName')) {
                obj['shortName'] = ApiClient.convertToType(data['shortName'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateOrganizationEarlyAccessFeaturesOptInRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateOrganizationEarlyAccessFeaturesOptInRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateOrganizationEarlyAccessFeaturesOptInRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['limitScopeToNetworks'])) {
            throw new Error("Expected the field `limitScopeToNetworks` to be an array in the JSON data but got " + data['limitScopeToNetworks']);
        }
        // ensure the json data is a string
        if (data['shortName'] && !(typeof data['shortName'] === 'string' || data['shortName'] instanceof String)) {
            throw new Error("Expected the field `shortName` to be a primitive type in the JSON string but got " + data['shortName']);
        }

        return true;
    }


}

CreateOrganizationEarlyAccessFeaturesOptInRequest.RequiredProperties = ["shortName"];

/**
 * A list of network IDs to apply the opt-in to
 * @member {Array.<String>} limitScopeToNetworks
 */
CreateOrganizationEarlyAccessFeaturesOptInRequest.prototype['limitScopeToNetworks'] = undefined;

/**
 * Short name of the early access feature
 * @member {String} shortName
 */
CreateOrganizationEarlyAccessFeaturesOptInRequest.prototype['shortName'] = undefined;






export default CreateOrganizationEarlyAccessFeaturesOptInRequest;

