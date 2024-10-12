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
import EndpointPostConversationsIDSearchesDataInnerRelevance from './EndpointPostConversationsIDSearchesDataInnerRelevance';
import Message from './Message';

/**
 * The EndpointPostConversationsIDSearchesDataInner model module.
 * @module model/EndpointPostConversationsIDSearchesDataInner
 * @version 4
 */
class EndpointPostConversationsIDSearchesDataInner {
    /**
     * Constructs a new <code>EndpointPostConversationsIDSearchesDataInner</code>.
     * @alias module:model/EndpointPostConversationsIDSearchesDataInner
     */
    constructor() { 
        
        EndpointPostConversationsIDSearchesDataInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>EndpointPostConversationsIDSearchesDataInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EndpointPostConversationsIDSearchesDataInner} obj Optional instance to populate.
     * @return {module:model/EndpointPostConversationsIDSearchesDataInner} The populated <code>EndpointPostConversationsIDSearchesDataInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EndpointPostConversationsIDSearchesDataInner();

            if (data.hasOwnProperty('message')) {
                obj['message'] = Message.constructFromObject(data['message']);
            }
            if (data.hasOwnProperty('relevance')) {
                obj['relevance'] = EndpointPostConversationsIDSearchesDataInnerRelevance.constructFromObject(data['relevance']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EndpointPostConversationsIDSearchesDataInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EndpointPostConversationsIDSearchesDataInner</code>.
     */
    static validateJSON(data) {
        // validate the optional field `message`
        if (data['message']) { // data not null
          Message.validateJSON(data['message']);
        }
        // validate the optional field `relevance`
        if (data['relevance']) { // data not null
          EndpointPostConversationsIDSearchesDataInnerRelevance.validateJSON(data['relevance']);
        }

        return true;
    }


}



/**
 * @member {module:model/Message} message
 */
EndpointPostConversationsIDSearchesDataInner.prototype['message'] = undefined;

/**
 * @member {module:model/EndpointPostConversationsIDSearchesDataInnerRelevance} relevance
 */
EndpointPostConversationsIDSearchesDataInner.prototype['relevance'] = undefined;






export default EndpointPostConversationsIDSearchesDataInner;

