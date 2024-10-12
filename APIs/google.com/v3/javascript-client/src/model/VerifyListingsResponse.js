/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ParsedListing from './ParsedListing';

/**
 * The VerifyListingsResponse model module.
 * @module model/VerifyListingsResponse
 * @version v3
 */
class VerifyListingsResponse {
    /**
     * Constructs a new <code>VerifyListingsResponse</code>.
     * Response message for VRPartnerListingVerificationService.VerifyPartnerListings.
     * @alias module:model/VerifyListingsResponse
     */
    constructor() { 
        
        VerifyListingsResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>VerifyListingsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/VerifyListingsResponse} obj Optional instance to populate.
     * @return {module:model/VerifyListingsResponse} The populated <code>VerifyListingsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new VerifyListingsResponse();

            if (data.hasOwnProperty('parsedListing')) {
                obj['parsedListing'] = ParsedListing.constructFromObject(data['parsedListing']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>VerifyListingsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>VerifyListingsResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `parsedListing`
        if (data['parsedListing']) { // data not null
          ParsedListing.validateJSON(data['parsedListing']);
        }

        return true;
    }


}



/**
 * @member {module:model/ParsedListing} parsedListing
 */
VerifyListingsResponse.prototype['parsedListing'] = undefined;






export default VerifyListingsResponse;

