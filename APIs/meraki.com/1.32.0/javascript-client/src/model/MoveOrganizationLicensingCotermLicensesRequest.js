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
import MoveOrganizationLicensingCotermLicensesRequestDestination from './MoveOrganizationLicensingCotermLicensesRequestDestination';
import MoveOrganizationLicensingCotermLicensesRequestLicensesInner from './MoveOrganizationLicensingCotermLicensesRequestLicensesInner';

/**
 * The MoveOrganizationLicensingCotermLicensesRequest model module.
 * @module model/MoveOrganizationLicensingCotermLicensesRequest
 * @version 1.32.0
 */
class MoveOrganizationLicensingCotermLicensesRequest {
    /**
     * Constructs a new <code>MoveOrganizationLicensingCotermLicensesRequest</code>.
     * @alias module:model/MoveOrganizationLicensingCotermLicensesRequest
     * @param destination {module:model/MoveOrganizationLicensingCotermLicensesRequestDestination} 
     * @param licenses {Array.<module:model/MoveOrganizationLicensingCotermLicensesRequestLicensesInner>} The list of licenses to move
     */
    constructor(destination, licenses) { 
        
        MoveOrganizationLicensingCotermLicensesRequest.initialize(this, destination, licenses);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, destination, licenses) { 
        obj['destination'] = destination;
        obj['licenses'] = licenses;
    }

    /**
     * Constructs a <code>MoveOrganizationLicensingCotermLicensesRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MoveOrganizationLicensingCotermLicensesRequest} obj Optional instance to populate.
     * @return {module:model/MoveOrganizationLicensingCotermLicensesRequest} The populated <code>MoveOrganizationLicensingCotermLicensesRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MoveOrganizationLicensingCotermLicensesRequest();

            if (data.hasOwnProperty('destination')) {
                obj['destination'] = MoveOrganizationLicensingCotermLicensesRequestDestination.constructFromObject(data['destination']);
            }
            if (data.hasOwnProperty('licenses')) {
                obj['licenses'] = ApiClient.convertToType(data['licenses'], [MoveOrganizationLicensingCotermLicensesRequestLicensesInner]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MoveOrganizationLicensingCotermLicensesRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MoveOrganizationLicensingCotermLicensesRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MoveOrganizationLicensingCotermLicensesRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `destination`
        if (data['destination']) { // data not null
          MoveOrganizationLicensingCotermLicensesRequestDestination.validateJSON(data['destination']);
        }
        if (data['licenses']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['licenses'])) {
                throw new Error("Expected the field `licenses` to be an array in the JSON data but got " + data['licenses']);
            }
            // validate the optional field `licenses` (array)
            for (const item of data['licenses']) {
                MoveOrganizationLicensingCotermLicensesRequestLicensesInner.validateJSON(item);
            };
        }

        return true;
    }


}

MoveOrganizationLicensingCotermLicensesRequest.RequiredProperties = ["destination", "licenses"];

/**
 * @member {module:model/MoveOrganizationLicensingCotermLicensesRequestDestination} destination
 */
MoveOrganizationLicensingCotermLicensesRequest.prototype['destination'] = undefined;

/**
 * The list of licenses to move
 * @member {Array.<module:model/MoveOrganizationLicensingCotermLicensesRequestLicensesInner>} licenses
 */
MoveOrganizationLicensingCotermLicensesRequest.prototype['licenses'] = undefined;






export default MoveOrganizationLicensingCotermLicensesRequest;

