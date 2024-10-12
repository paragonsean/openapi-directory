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
import Error from './Error';
import PatientAuthInitResponseAuth from './PatientAuthInitResponseAuth';
import RequestReference from './RequestReference';

/**
 * The PatientAuthInitResponse model module.
 * @module model/PatientAuthInitResponse
 * @version 0.5
 */
class PatientAuthInitResponse {
    /**
     * Constructs a new <code>PatientAuthInitResponse</code>.
     * @alias module:model/PatientAuthInitResponse
     * @param requestId {String} a nonce, unique for each HTTP request
     * @param resp {module:model/RequestReference} 
     * @param timestamp {Date} Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
     */
    constructor(requestId, resp, timestamp) { 
        
        PatientAuthInitResponse.initialize(this, requestId, resp, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, requestId, resp, timestamp) { 
        obj['requestId'] = requestId;
        obj['resp'] = resp;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>PatientAuthInitResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PatientAuthInitResponse} obj Optional instance to populate.
     * @return {module:model/PatientAuthInitResponse} The populated <code>PatientAuthInitResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PatientAuthInitResponse();

            if (data.hasOwnProperty('auth')) {
                obj['auth'] = PatientAuthInitResponseAuth.constructFromObject(data['auth']);
            }
            if (data.hasOwnProperty('error')) {
                obj['error'] = Error.constructFromObject(data['error']);
            }
            if (data.hasOwnProperty('requestId')) {
                obj['requestId'] = ApiClient.convertToType(data['requestId'], 'String');
            }
            if (data.hasOwnProperty('resp')) {
                obj['resp'] = RequestReference.constructFromObject(data['resp']);
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PatientAuthInitResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PatientAuthInitResponse</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of PatientAuthInitResponse.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // validate the optional field `auth`
        if (data['auth']) { // data not null
          PatientAuthInitResponseAuth.validateJSON(data['auth']);
        }
        // validate the optional field `error`
        if (data['error']) { // data not null
          Error.validateJSON(data['error']);
        }
        // ensure the json data is a string
        if (data['requestId'] && !(typeof data['requestId'] === 'string' || data['requestId'] instanceof String)) {
            throw new Error("Expected the field `requestId` to be a primitive type in the JSON string but got " + data['requestId']);
        }
        // validate the optional field `resp`
        if (data['resp']) { // data not null
          RequestReference.validateJSON(data['resp']);
        }

        return true;
    }


}

PatientAuthInitResponse.RequiredProperties = ["requestId", "resp", "timestamp"];

/**
 * @member {module:model/PatientAuthInitResponseAuth} auth
 */
PatientAuthInitResponse.prototype['auth'] = undefined;

/**
 * @member {module:model/Error} error
 */
PatientAuthInitResponse.prototype['error'] = undefined;

/**
 * a nonce, unique for each HTTP request
 * @member {String} requestId
 */
PatientAuthInitResponse.prototype['requestId'] = undefined;

/**
 * @member {module:model/RequestReference} resp
 */
PatientAuthInitResponse.prototype['resp'] = undefined;

/**
 * Date time format in UTC, includes miliseconds YYYY-MM-DDThh:mm:ss.vZ
 * @member {Date} timestamp
 */
PatientAuthInitResponse.prototype['timestamp'] = undefined;






export default PatientAuthInitResponse;

