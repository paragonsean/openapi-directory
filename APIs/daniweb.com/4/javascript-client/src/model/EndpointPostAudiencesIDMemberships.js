/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import EndpointPostAudiencesIDMembershipsData from './EndpointPostAudiencesIDMembershipsData';

/**
 * The EndpointPostAudiencesIDMemberships model module.
 * @module model/EndpointPostAudiencesIDMemberships
 * @version 4
 */
class EndpointPostAudiencesIDMemberships {
    /**
     * Constructs a new <code>EndpointPostAudiencesIDMemberships</code>.
     * @alias module:model/EndpointPostAudiencesIDMemberships
     */
    constructor() { 
        
        EndpointPostAudiencesIDMemberships.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointPostAudiencesIDMemberships</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointPostAudiencesIDMemberships} obj Optional instance to populate.
     * @return {module:model/EndpointPostAudiencesIDMemberships} The populated <code>EndpointPostAudiencesIDMemberships</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointPostAudiencesIDMemberships();

            if (data.hasOwnProperty('data')) {
                obj['data'] = EndpointPostAudiencesIDMembershipsData.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointPostAudiencesIDMemberships</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointPostAudiencesIDMemberships</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          EndpointPostAudiencesIDMembershipsData.validateJSON(data['data']);
        }

        return true;
    }


}



/**
 * @member {module:model/EndpointPostAudiencesIDMembershipsData} data
 */
EndpointPostAudiencesIDMemberships.prototype['data'] = undefined;

/**
 * @member {Boolean} success
 */
EndpointPostAudiencesIDMemberships.prototype['success'] = undefined;






export default EndpointPostAudiencesIDMemberships;

