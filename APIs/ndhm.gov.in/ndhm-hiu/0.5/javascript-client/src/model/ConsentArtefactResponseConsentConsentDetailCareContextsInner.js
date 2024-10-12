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
 * The ConsentArtefactResponseConsentConsentDetailCareContextsInner model module.
 * @module model/ConsentArtefactResponseConsentConsentDetailCareContextsInner
 * @version 0.5
 */
class ConsentArtefactResponseConsentConsentDetailCareContextsInner {
    /**
     * Constructs a new <code>ConsentArtefactResponseConsentConsentDetailCareContextsInner</code>.
     * @alias module:model/ConsentArtefactResponseConsentConsentDetailCareContextsInner
     * @param careContextReference {String} 
     * @param patientReference {String} 
     */
    constructor(careContextReference, patientReference) { 
        
        ConsentArtefactResponseConsentConsentDetailCareContextsInner.initialize(this, careContextReference, patientReference);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, careContextReference, patientReference) { 
        obj['careContextReference'] = careContextReference;
        obj['patientReference'] = patientReference;
    }

    /**
     * Constructs a <code>ConsentArtefactResponseConsentConsentDetailCareContextsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConsentArtefactResponseConsentConsentDetailCareContextsInner} obj Optional instance to populate.
     * @return {module:model/ConsentArtefactResponseConsentConsentDetailCareContextsInner} The populated <code>ConsentArtefactResponseConsentConsentDetailCareContextsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConsentArtefactResponseConsentConsentDetailCareContextsInner();

            if (data.hasOwnProperty('careContextReference')) {
                obj['careContextReference'] = ApiClient.convertToType(data['careContextReference'], 'String');
            }
            if (data.hasOwnProperty('patientReference')) {
                obj['patientReference'] = ApiClient.convertToType(data['patientReference'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConsentArtefactResponseConsentConsentDetailCareContextsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConsentArtefactResponseConsentConsentDetailCareContextsInner</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConsentArtefactResponseConsentConsentDetailCareContextsInner.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['careContextReference'] && !(typeof data['careContextReference'] === 'string' || data['careContextReference'] instanceof String)) {
            throw new Error("Expected the field `careContextReference` to be a primitive type in the JSON string but got " + data['careContextReference']);
        }
        // ensure the json data is a string
        if (data['patientReference'] && !(typeof data['patientReference'] === 'string' || data['patientReference'] instanceof String)) {
            throw new Error("Expected the field `patientReference` to be a primitive type in the JSON string but got " + data['patientReference']);
        }

        return true;
    }


}

ConsentArtefactResponseConsentConsentDetailCareContextsInner.RequiredProperties = ["careContextReference", "patientReference"];

/**
 * @member {String} careContextReference
 */
ConsentArtefactResponseConsentConsentDetailCareContextsInner.prototype['careContextReference'] = undefined;

/**
 * @member {String} patientReference
 */
ConsentArtefactResponseConsentConsentDetailCareContextsInner.prototype['patientReference'] = undefined;






export default ConsentArtefactResponseConsentConsentDetailCareContextsInner;

