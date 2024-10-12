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
import ApiPagination from './ApiPagination';
import EndpointGetConversationsIDStatusesDataInner from './EndpointGetConversationsIDStatusesDataInner';

/**
 * The EndpointGetConversationsStatuses model module.
 * @module model/EndpointGetConversationsStatuses
 * @version 4
 */
class EndpointGetConversationsStatuses {
    /**
     * Constructs a new <code>EndpointGetConversationsStatuses</code>.
     * @alias module:model/EndpointGetConversationsStatuses
     */
    constructor() { 
        
        EndpointGetConversationsStatuses.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointGetConversationsStatuses</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointGetConversationsStatuses} obj Optional instance to populate.
     * @return {module:model/EndpointGetConversationsStatuses} The populated <code>EndpointGetConversationsStatuses</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointGetConversationsStatuses();

            if (data.hasOwnProperty('data')) {
                obj['data'] = ApiClient.convertToType(data['data'], [EndpointGetConversationsIDStatusesDataInner]);
            }
            if (data.hasOwnProperty('pagination')) {
                obj['pagination'] = ApiPagination.constructFromObject(data['pagination']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointGetConversationsStatuses</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointGetConversationsStatuses</code>.
     */
    static validateJSON(data) {
        if (data['data']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['data'])) {
                throw new Error("Expected the field `data` to be an array in the JSON data but got " + data['data']);
            }
            // validate the optional field `data` (array)
            for (const item of data['data']) {
                EndpointGetConversationsIDStatusesDataInner.validateJSON(item);
            };
        }
        // validate the optional field `pagination`
        if (data['pagination']) { // data not null
          ApiPagination.validateJSON(data['pagination']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/EndpointGetConversationsIDStatusesDataInner>} data
 */
EndpointGetConversationsStatuses.prototype['data'] = undefined;

/**
 * @member {module:model/ApiPagination} pagination
 */
EndpointGetConversationsStatuses.prototype['pagination'] = undefined;






export default EndpointGetConversationsStatuses;

