/**
 * Quick start - Telematics SDK
 * # Introduction We have prepared a set of APIs for quick start to integrate telematics SDK that powers mobile telematics inside 3rd party mobile applications.  * [CONTACT US](https://telematicssdk.com) * [SANDBOX](https://userdatahub.com) * [DEV.PORTAL](https://docs.telematicssdk.com) * [DEMO APP](https://raxeltelematics.com/telematics-app)   # Overview Datamotion provides telematics infrastructure for mobile applications.   Telematics SDK turns any smartphone into telematics data gathering device to collect Location, driving and behavior data. API services unlocks power of your mobile application  There are 3 groups of methods: * 1 - user management * 2 - statistics for mobile app * 3 - statistics for back-end(s)  in certain cases you will need SNS or any other notification services. read more [here](https://docs.telematicssdk.com/platform-features/sns) # Possible architecture  There are three common schemes that are used by our clients. These schemes can be combined * Collect, Process, Store (required: 1&2) * Collect, Process (required: 1& sns) * Collect (required 1&sns)   ## Collect, Process, Store ![Collect, Process, Store](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection%2C+processing%2C+storage)  ## Collect, Process ![Collect, Process](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+and+processing)  ## Collect ![Collect](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Dev.portal/Architecture+-+Collection+only)  *** ![Telematic sdk](https://website-cliparts-datamotion.s3.us-east-2.amazonaws.com/Github/transportation_small.png)  # Common use-cases: * Safe and efficient driving * Usage-based insurance * Safe driving assessment * Driver assessment * Trip log * Geo-analysis * Accident monitoring * Driving engagements * Location based services * Realtime Tracking and beyond  # How to start * Register a [SANDBOX ACCOUNT](https://userdatahub.com) * Get [CREDENTIALS](https://docs.userdatahub.com/sandbox/credentials)  * Follow the guide from [DEVELOPER POERTAL](https://docs.telematicssdk.com)  # Authentication To create a user on datamotion platform, you require to use InstanceID and InstanceKEY. You can get it in Datahub -> management -> user-service credentials  Once you create a user, you will get Device token, JWT token and refresh token. then, you will use it for APIs
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import V1ScoringsConsolidatedDaily200ResponseResultInner from './V1ScoringsConsolidatedDaily200ResponseResultInner';

/**
 * The V1ScoringsConsolidatedDaily200Response model module.
 * @module model/V1ScoringsConsolidatedDaily200Response
 * @version 1.0.0
 */
class V1ScoringsConsolidatedDaily200Response {
    /**
     * Constructs a new <code>V1ScoringsConsolidatedDaily200Response</code>.
     * @alias module:model/V1ScoringsConsolidatedDaily200Response
     */
    constructor() { 
        
        V1ScoringsConsolidatedDaily200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>V1ScoringsConsolidatedDaily200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/V1ScoringsConsolidatedDaily200Response} obj Optional instance to populate.
     * @return {module:model/V1ScoringsConsolidatedDaily200Response} The populated <code>V1ScoringsConsolidatedDaily200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new V1ScoringsConsolidatedDaily200Response();

            if (data.hasOwnProperty('Errors')) {
                obj['Errors'] = ApiClient.convertToType(data['Errors'], [Object]);
            }
            if (data.hasOwnProperty('Result')) {
                obj['Result'] = ApiClient.convertToType(data['Result'], [V1ScoringsConsolidatedDaily200ResponseResultInner]);
            }
            if (data.hasOwnProperty('Status')) {
                obj['Status'] = ApiClient.convertToType(data['Status'], 'Number');
            }
            if (data.hasOwnProperty('Title')) {
                obj['Title'] = ApiClient.convertToType(data['Title'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>V1ScoringsConsolidatedDaily200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>V1ScoringsConsolidatedDaily200Response</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['Errors'])) {
            throw new Error("Expected the field `Errors` to be an array in the JSON data but got " + data['Errors']);
        }
        if (data['Result']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Result'])) {
                throw new Error("Expected the field `Result` to be an array in the JSON data but got " + data['Result']);
            }
            // validate the optional field `Result` (array)
            for (const item of data['Result']) {
                V1ScoringsConsolidatedDaily200ResponseResultInner.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['Title'] && !(typeof data['Title'] === 'string' || data['Title'] instanceof String)) {
            throw new Error("Expected the field `Title` to be a primitive type in the JSON string but got " + data['Title']);
        }

        return true;
    }


}



/**
 * @member {Array.<Object>} Errors
 */
V1ScoringsConsolidatedDaily200Response.prototype['Errors'] = undefined;

/**
 * @member {Array.<module:model/V1ScoringsConsolidatedDaily200ResponseResultInner>} Result
 */
V1ScoringsConsolidatedDaily200Response.prototype['Result'] = undefined;

/**
 * @member {Number} Status
 */
V1ScoringsConsolidatedDaily200Response.prototype['Status'] = undefined;

/**
 * @member {String} Title
 */
V1ScoringsConsolidatedDaily200Response.prototype['Title'] = undefined;






export default V1ScoringsConsolidatedDaily200Response;

