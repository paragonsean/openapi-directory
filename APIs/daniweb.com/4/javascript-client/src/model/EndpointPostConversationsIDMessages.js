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
 * The EndpointPostConversationsIDMessages model module.
 * @module model/EndpointPostConversationsIDMessages
 * @version 4
 */
class EndpointPostConversationsIDMessages {
    /**
     * Constructs a new <code>EndpointPostConversationsIDMessages</code>.
     * @alias module:model/EndpointPostConversationsIDMessages
     */
    constructor() { 
        
        EndpointPostConversationsIDMessages.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointPostConversationsIDMessages</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointPostConversationsIDMessages} obj Optional instance to populate.
     * @return {module:model/EndpointPostConversationsIDMessages} The populated <code>EndpointPostConversationsIDMessages</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointPostConversationsIDMessages();

            if (data.hasOwnProperty('data')) {
                obj['data'] = Message.constructFromObject(data['data']);
            }
            if (data.hasOwnProperty('success')) {
                obj['success'] = ApiClient.convertToType(data['success'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointPostConversationsIDMessages</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointPostConversationsIDMessages</code>.
     */
    static validateJSON(data) {
        // validate the optional field `data`
        if (data['data']) { // data not null
          Message.validateJSON(data['data']);
        }

        return true;
    }


}



/**
 * @member {module:model/Message} data
 */
EndpointPostConversationsIDMessages.prototype['data'] = undefined;

/**
 * @member {Boolean} success
 */
EndpointPostConversationsIDMessages.prototype['success'] = undefined;






export default EndpointPostConversationsIDMessages;

