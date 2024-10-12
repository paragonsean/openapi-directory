/**
 * Health Repository Provider Specifications for HIU
 * The following are the specifications for the APIs to be implemented at the Health Repository end if an entity is only serving the role of a HIU. The specs are essentially duplicates from the Gateway and Bridge, but put together so as to make it clear to *HIUs* which set of APIs they should implement to participate in the network.     1. The APIs are organized by the flows - **identification**, **consent flow**, **data flow** and **monitoring**. They represent the APIs that are expected to be available at the HIU end by the Gateway.    2. For majority of the APIs, if Gateway has initiated a call, there are corresponding callback APIs on the Gateway. e.g for **_/consents/hiu/notify** API on HIU end, its expected that a corresponding callback API **_/consents/hiu/on-notify** on Gateway is called. Such APIs are organized under the **Gateway** label.    3. Gateway relevant APIs for HIUs are grouped under **Gateway** label. These include the APIs that HIPs are required to call on the Gateway. For example, to request a CM for consent, HIU would call **_/consent-requests/init** API on gateway.    4. **NOTE**, in some of the API documentations below, **X-HIP-ID** is mentioned in header (for example in /auth/on-init). These are the cases, when a particular API is applicable for both HIU and HIP (e.g an entity is playing the role of HRP representing both HIU and HIP). If you are only playing the role of HIP, then only X-HIU-ID header will be sent  
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
import CareContextDefinition from './CareContextDefinition';
import HITypeEnum from './HITypeEnum';

/**
 * The EventCategoryDetail model module.
 * @module model/EventCategoryDetail
 * @version 0.5
 */
class EventCategoryDetail {
    /**
     * Constructs a new <code>EventCategoryDetail</code>.
     * @alias module:model/EventCategoryDetail
     * @param careContext {module:model/CareContextDefinition} 
     * @param hiTypes {Array.<module:model/HITypeEnum>} 
     */
    constructor(careContext, hiTypes) { 
        
        EventCategoryDetail.initialize(this, careContext, hiTypes);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, careContext, hiTypes) { 
        obj['careContext'] = careContext;
        obj['hiTypes'] = hiTypes;
    }

    /**
     * Constructs a <code>EventCategoryDetail</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/EventCategoryDetail} obj Optional instance to populate.
     * @return {module:model/EventCategoryDetail} The populated <code>EventCategoryDetail</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new EventCategoryDetail();

            if (data.hasOwnProperty('careContext')) {
                obj['careContext'] = CareContextDefinition.constructFromObject(data['careContext']);
            }
            if (data.hasOwnProperty('hiTypes')) {
                obj['hiTypes'] = ApiClient.convertToType(data['hiTypes'], [HITypeEnum]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>EventCategoryDetail</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>EventCategoryDetail</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of EventCategoryDetail.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `careContext`
        if (data['careContext']) { // data not null
          CareContextDefinition.validateJSON(data['careContext']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['hiTypes'])) {
            throw new Error("Expected the field `hiTypes` to be an array in the JSON data but got " + data['hiTypes']);
        }

        return true;
    }


}

EventCategoryDetail.RequiredProperties = ["careContext", "hiTypes"];

/**
 * @member {module:model/CareContextDefinition} careContext
 */
EventCategoryDetail.prototype['careContext'] = undefined;

/**
 * @member {Array.<module:model/HITypeEnum>} hiTypes
 */
EventCategoryDetail.prototype['hiTypes'] = undefined;






export default EventCategoryDetail;

