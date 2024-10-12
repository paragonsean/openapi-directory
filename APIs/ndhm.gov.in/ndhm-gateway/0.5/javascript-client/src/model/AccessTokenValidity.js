/**
 * Gateway
 * Gateway is the hub that routes/orchestrates the interaction between consent managers and API bridges. There are 5 categories of APIs; discovery, link, consent flow, data flow and  monitoring. To reflect the consumers of APIs, the above apis are also categorized under cm facing, hiu facing and hip facing  
 *
 * The version of the OpenAPI document: 0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import PatientAuthPurpose from './PatientAuthPurpose';
import PatientAuthRequester from './PatientAuthRequester';

/**
 * The AccessTokenValidity model module.
 * @module model/AccessTokenValidity
 * @version 0.5
 */
class AccessTokenValidity {
    /**
     * Constructs a new <code>AccessTokenValidity</code>.
     * @alias module:model/AccessTokenValidity
     * @param expiry {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     * @param limit {Number} number of times, the token can be used
     * @param purpose {module:model/PatientAuthPurpose} 
     * @param requester {module:model/PatientAuthRequester} 
     */
    constructor(expiry, limit, purpose, requester) { 
        
        AccessTokenValidity.initialize(this, expiry, limit, purpose, requester);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, expiry, limit, purpose, requester) { 
        obj['expiry'] = expiry;
        obj['limit'] = limit;
        obj['purpose'] = purpose;
        obj['requester'] = requester;
    }

    /**
     * Constructs a <code>AccessTokenValidity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/AccessTokenValidity} obj Optional instance to populate.
     * @return {module:model/AccessTokenValidity} The populated <code>AccessTokenValidity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new AccessTokenValidity();

            if (data.hasOwnProperty('expiry')) {
                obj['expiry'] = ApiClient.convertToType(data['expiry'], 'Date');
            }
            if (data.hasOwnProperty('limit')) {
                obj['limit'] = ApiClient.convertToType(data['limit'], 'Number');
            }
            if (data.hasOwnProperty('purpose')) {
                obj['purpose'] = PatientAuthPurpose.constructFromObject(data['purpose']);
            }
            if (data.hasOwnProperty('requester')) {
                obj['requester'] = PatientAuthRequester.constructFromObject(data['requester']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>AccessTokenValidity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>AccessTokenValidity</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of AccessTokenValidity.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `requester`
        if (data['requester']) { // data not null
          PatientAuthRequester.validateJSON(data['requester']);
        }

        return true;
    }


}

AccessTokenValidity.RequiredProperties = ["expiry", "limit", "purpose", "requester"];

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} expiry
 */
AccessTokenValidity.prototype['expiry'] = undefined;

/**
 * number of times, the token can be used
 * @member {Number} limit
 */
AccessTokenValidity.prototype['limit'] = undefined;

/**
 * @member {module:model/PatientAuthPurpose} purpose
 */
AccessTokenValidity.prototype['purpose'] = undefined;

/**
 * @member {module:model/PatientAuthRequester} requester
 */
AccessTokenValidity.prototype['requester'] = undefined;






export default AccessTokenValidity;

