/**
 * ExaVault
 * ExaVaults API allows you to incorporate ExaVaults suite of file transfer and user management tools into your own application.\\nExaVault supports both POST (recommended when requesting large data sets) and GET operations, and requires an API key in order to use.
 *
 * The version of the OpenAPI document: 2.0
 * Contact: support@exavault.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import Share from './Share';
import ShareCollectionResponseIncludedInner from './ShareCollectionResponseIncludedInner';

/**
 * The ShareResponse model module.
 * @module model/ShareResponse
 * @version 2.0
 */
class ShareResponse {
    /**
     * Constructs a new <code>ShareResponse</code>.
     * Response object for shares.
     * @alias module:model/ShareResponse
     */
    constructor() { 
        
        ShareResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ShareResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShareResponse} obj Optional instance to populate.
     * @return {module:model/ShareResponse} The populated <code>ShareResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShareResponse();

            if (data.hasOwnProperty('data')) {
                obj['data'] = Share.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('included')) {
                obj['included'] = ApiClient.convertToType(data['included'], [ShareCollectionResponseIncludedInner]);
            }
            if (data.hasOwnProperty('responseStatus')) {
                obj['responseStatus'] = ApiClient.convertToType(data['responseStatus'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ShareResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShareResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          Share.validateJSON(data['data']);
        }
        if (data['included']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['included'])) {
                throw new Error("Expected the field `included` to be an array in the JSON data but got " + data['included']);
            }
            // validate the optional field `included` (array)
            for (const item of data['included']) {
                ShareCollectionResponseIncludedInner.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {module:model/Share} data
 */
ShareResponse.prototype['data'] = undefined;

/**
 * @member {Array.<module:model/ShareCollectionResponseIncludedInner>} included
 */
ShareResponse.prototype['included'] = undefined;

/**
 * Http status code of the response.
 * @member {Number} responseStatus
 */
ShareResponse.prototype['responseStatus'] = undefined;






export default ShareResponse;

