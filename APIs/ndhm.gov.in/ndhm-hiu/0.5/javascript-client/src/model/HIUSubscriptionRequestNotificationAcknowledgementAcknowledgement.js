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

/**
 * The HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement model module.
 * @module model/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement
 * @version 0.5
 */
class HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement {
    /**
     * Constructs a new <code>HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement</code>.
     * @alias module:model/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement
     * @param status {module:model/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.StatusEnum} 
     * @param subscriptionRequestId {String} 
     */
    constructor(status, subscriptionRequestId) { 
        
        HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.initialize(this, status, subscriptionRequestId);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, status, subscriptionRequestId) { 
        obj['status'] = status;
        obj['subscriptionRequestId'] = subscriptionRequestId;
    }

    /**
     * Constructs a <code>HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement} obj Optional instance to populate.
     * @return {module:model/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement} The populated <code>HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement();

            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('subscriptionRequestId')) {
                obj['subscriptionRequestId'] = ApiClient.convertToType(data['subscriptionRequestId'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        // ensure the json data is a string
        if (data['subscriptionRequestId'] && !(typeof data['subscriptionRequestId'] === 'string' || data['subscriptionRequestId'] instanceof String)) {
            throw new Error("Expected the field `subscriptionRequestId` to be a primitive type in the JSON string but got " + data['subscriptionRequestId']);
        }

        return true;
    }


}

HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.RequiredProperties = ["status", "subscriptionRequestId"];

/**
 * @member {module:model/HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.StatusEnum} status
 */
HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.prototype['status'] = undefined;

/**
 * @member {String} subscriptionRequestId
 */
HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement.prototype['subscriptionRequestId'] = undefined;





/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement['StatusEnum'] = {

    /**
     * value: "OK"
     * @const
     */
    "OK": "OK"
};



export default HIUSubscriptionRequestNotificationAcknowledgementAcknowledgement;

