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
import ConsentArtefactResponseConsentConsentDetailHip from './ConsentArtefactResponseConsentConsentDetailHip';
import ConsentArtefactResponseConsentConsentDetailHiu from './ConsentArtefactResponseConsentConsentDetailHiu';
import ConsentRequestConsentPatient from './ConsentRequestConsentPatient';
import HITypeEnum from './HITypeEnum';
import Permission from './Permission';
import Requester from './Requester';
import UsePurpose from './UsePurpose';

/**
 * The ConsentRequestConsent model module.
 * @module model/ConsentRequestConsent
 * @version 0.5
 */
class ConsentRequestConsent {
    /**
     * Constructs a new <code>ConsentRequestConsent</code>.
     * @alias module:model/ConsentRequestConsent
     * @param hiTypes {Array.<module:model/HITypeEnum>} 
     * @param hiu {module:model/ConsentArtefactResponseConsentConsentDetailHiu} 
     * @param patient {module:model/ConsentRequestConsentPatient} 
     * @param permission {module:model/Permission} 
     * @param purpose {module:model/UsePurpose} 
     * @param requester {module:model/Requester} 
     */
    constructor(hiTypes, hiu, patient, permission, purpose, requester) { 
        
        ConsentRequestConsent.initialize(this, hiTypes, hiu, patient, permission, purpose, requester);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, hiTypes, hiu, patient, permission, purpose, requester) { 
        obj['hiTypes'] = hiTypes;
        obj['hiu'] = hiu;
        obj['patient'] = patient;
        obj['permission'] = permission;
        obj['purpose'] = purpose;
        obj['requester'] = requester;
    }

    /**
     * Constructs a <code>ConsentRequestConsent</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ConsentRequestConsent} obj Optional instance to populate.
     * @return {module:model/ConsentRequestConsent} The populated <code>ConsentRequestConsent</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ConsentRequestConsent();

            if (data.hasOwnProperty('careContexts')) {
                obj['careContexts'] = ApiClient.convertToType(data['careContexts'], [CareContextDefinition]);
            }
            if (data.hasOwnProperty('hiTypes')) {
                obj['hiTypes'] = ApiClient.convertToType(data['hiTypes'], [HITypeEnum]);
            }
            if (data.hasOwnProperty('hip')) {
                obj['hip'] = ConsentArtefactResponseConsentConsentDetailHip.constructFromObject(data['hip']);
            }
            if (data.hasOwnProperty('hiu')) {
                obj['hiu'] = ConsentArtefactResponseConsentConsentDetailHiu.constructFromObject(data['hiu']);
            }
            if (data.hasOwnProperty('patient')) {
                obj['patient'] = ConsentRequestConsentPatient.constructFromObject(data['patient']);
            }
            if (data.hasOwnProperty('permission')) {
                obj['permission'] = Permission.constructFromObject(data['permission']);
            }
            if (data.hasOwnProperty('purpose')) {
                obj['purpose'] = UsePurpose.constructFromObject(data['purpose']);
            }
            if (data.hasOwnProperty('requester')) {
                obj['requester'] = Requester.constructFromObject(data['requester']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ConsentRequestConsent</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ConsentRequestConsent</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ConsentRequestConsent.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        if (data['careContexts']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['careContexts'])) {
                throw new Error("Expected the field `careContexts` to be an array in the JSON data but got " + data['careContexts']);
            }
            // validate the optional field `careContexts` (array)
            for (const item of data['careContexts']) {
                CareContextDefinition.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['hiTypes'])) {
            throw new Error("Expected the field `hiTypes` to be an array in the JSON data but got " + data['hiTypes']);
        }
        // validate the optional field `hip`
        if (data['hip']) { // data not null
          ConsentArtefactResponseConsentConsentDetailHip.validateJSON(data['hip']);
        }
        // validate the optional field `hiu`
        if (data['hiu']) { // data not null
          ConsentArtefactResponseConsentConsentDetailHiu.validateJSON(data['hiu']);
        }
        // validate the optional field `patient`
        if (data['patient']) { // data not null
          ConsentRequestConsentPatient.validateJSON(data['patient']);
        }
        // validate the optional field `permission`
        if (data['permission']) { // data not null
          Permission.validateJSON(data['permission']);
        }
        // validate the optional field `purpose`
        if (data['purpose']) { // data not null
          UsePurpose.validateJSON(data['purpose']);
        }
        // validate the optional field `requester`
        if (data['requester']) { // data not null
          Requester.validateJSON(data['requester']);
        }

        return true;
    }


}

ConsentRequestConsent.RequiredProperties = ["hiTypes", "hiu", "patient", "permission", "purpose", "requester"];

/**
 * @member {Array.<module:model/CareContextDefinition>} careContexts
 */
ConsentRequestConsent.prototype['careContexts'] = undefined;

/**
 * @member {Array.<module:model/HITypeEnum>} hiTypes
 */
ConsentRequestConsent.prototype['hiTypes'] = undefined;

/**
 * @member {module:model/ConsentArtefactResponseConsentConsentDetailHip} hip
 */
ConsentRequestConsent.prototype['hip'] = undefined;

/**
 * @member {module:model/ConsentArtefactResponseConsentConsentDetailHiu} hiu
 */
ConsentRequestConsent.prototype['hiu'] = undefined;

/**
 * @member {module:model/ConsentRequestConsentPatient} patient
 */
ConsentRequestConsent.prototype['patient'] = undefined;

/**
 * @member {module:model/Permission} permission
 */
ConsentRequestConsent.prototype['permission'] = undefined;

/**
 * @member {module:model/UsePurpose} purpose
 */
ConsentRequestConsent.prototype['purpose'] = undefined;

/**
 * @member {module:model/Requester} requester
 */
ConsentRequestConsent.prototype['requester'] = undefined;






export default ConsentRequestConsent;

