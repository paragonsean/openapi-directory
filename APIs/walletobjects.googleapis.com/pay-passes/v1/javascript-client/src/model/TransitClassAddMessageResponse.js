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
import TransitClass from './TransitClass';

/**
 * The TransitClassAddMessageResponse model module.
 * @module model/TransitClassAddMessageResponse
 * @version v1
 */
class TransitClassAddMessageResponse {
    /**
     * Constructs a new <code>TransitClassAddMessageResponse</code>.
     * @alias module:model/TransitClassAddMessageResponse
     */
    constructor() { 
        
        TransitClassAddMessageResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TransitClassAddMessageResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TransitClassAddMessageResponse} obj Optional instance to populate.
     * @return {module:model/TransitClassAddMessageResponse} The populated <code>TransitClassAddMessageResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TransitClassAddMessageResponse();

            if (data.hasOwnProperty('resource')) {
                obj['resource'] = TransitClass.constructFromObject(data['resource']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TransitClassAddMessageResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TransitClassAddMessageResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `resource`
        if (data['resource']) { // data not null
          TransitClass.validateJSON(data['resource']);
        }

        return true;
    }


}



/**
 * @member {module:model/TransitClass} resource
 */
TransitClassAddMessageResponse.prototype['resource'] = undefined;






export default TransitClassAddMessageResponse;

