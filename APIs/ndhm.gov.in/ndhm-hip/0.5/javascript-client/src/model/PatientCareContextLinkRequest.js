/**
 * Health Repository Provider Specifications for HIP
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIP. The specs are essentially duplicates from the Gateway and Health Repository, but put together so as to make it clear to *HIPs* which set of APIs they should implement to participate in the network.  
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
import PatientCareContextLink from './PatientCareContextLink';

/**
 * The PatientCareContextLinkRequest model module.
 * @module model/PatientCareContextLinkRequest
 * @version 0.5
 */
class PatientCareContextLinkRequest {
    /**
     * Constructs a new <code>PatientCareContextLinkRequest</code>.
     * @alias module:model/PatientCareContextLinkRequest
     * @param link {module:model/PatientCareContextLink} 
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(link, requestId, timestamp) { 
        
        PatientCareContextLinkRequest.initialize(this, link, requestId, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, link, requestId, timestamp) { 
        obj['link'] = link;
        obj['requestId'] = requestId;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>PatientCareContextLinkRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientCareContextLinkRequest} obj Optional instance to populate.
     * @return {module:model/PatientCareContextLinkRequest} The populated <code>PatientCareContextLinkRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientCareContextLinkRequest();

            if (data.hasOwnProperty('link')) {
                obj['link'] = PatientCareContextLink.constructFromObject(data['link']);
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientCareContextLinkRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientCareContextLinkRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientCareContextLinkRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `link`
        if (data['link']) { // data not null
          PatientCareContextLink.validateJSON(data['link']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }

        return true;
    }


}

PatientCareContextLinkRequest.RequiredProperties = ["link", "requestId", "timestamp"];

/**
 * @member {module:model/PatientCareContextLink} link
 */
PatientCareContextLinkRequest.prototype['link'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
PatientCareContextLinkRequest.prototype['requestId'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
PatientCareContextLinkRequest.prototype['timestamp'] = undefined;






export default PatientCareContextLinkRequest;

