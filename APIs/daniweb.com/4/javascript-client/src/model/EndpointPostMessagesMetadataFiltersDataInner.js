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
import Message from './Message';

/**
 * The EndpointPostMessagesMetadataFiltersDataInner model module.
 * @module model/EndpointPostMessagesMetadataFiltersDataInner
 * @version 4
 */
class EndpointPostMessagesMetadataFiltersDataInner {
    /**
     * Constructs a new <code>EndpointPostMessagesMetadataFiltersDataInner</code>.
     * @alias module:model/EndpointPostMessagesMetadataFiltersDataInner
     */
    constructor() { 
        
        EndpointPostMessagesMetadataFiltersDataInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointPostMessagesMetadataFiltersDataInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointPostMessagesMetadataFiltersDataInner} obj Optional instance to populate.
     * @return {module:model/EndpointPostMessagesMetadataFiltersDataInner} The populated <code>EndpointPostMessagesMetadataFiltersDataInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointPostMessagesMetadataFiltersDataInner();

            if (data.hasOwnProperty('matched_metadata')) {
                obj['matched_metadata'] = ApiClient.convertToType(data['matched_metadata'], {'String': ['String']});
            }
            if (data.hasOwnProperty('message')) {
                obj['message'] = Message.constructFromObject(data['message']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointPostMessagesMetadataFiltersDataInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointPostMessagesMetadataFiltersDataInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `message`
        if (data['message']) { // data not null
          Message.validateJSON(data['message']);
        }

        return true;
    }


}



/**
 * @member {Object.<String, Array.<String>>} matched_metadata
 */
EndpointPostMessagesMetadataFiltersDataInner.prototype['matched_metadata'] = undefined;

/**
 * @member {module:model/Message} message
 */
EndpointPostMessagesMetadataFiltersDataInner.prototype['message'] = undefined;






export default EndpointPostMessagesMetadataFiltersDataInner;

