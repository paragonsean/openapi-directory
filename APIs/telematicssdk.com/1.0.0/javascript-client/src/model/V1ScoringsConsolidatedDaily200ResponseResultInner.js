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

/**
 * The V1ScoringsConsolidatedDaily200ResponseResultInner model module.
 * @module model/V1ScoringsConsolidatedDaily200ResponseResultInner
 * @version 1.0.0
 */
class V1ScoringsConsolidatedDaily200ResponseResultInner {
    /**
     * Constructs a new <code>V1ScoringsConsolidatedDaily200ResponseResultInner</code>.
     * @alias module:model/V1ScoringsConsolidatedDaily200ResponseResultInner
     */
    constructor() { 
        
        V1ScoringsConsolidatedDaily200ResponseResultInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>V1ScoringsConsolidatedDaily200ResponseResultInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/V1ScoringsConsolidatedDaily200ResponseResultInner} obj Optional instance to populate.
     * @return {module:model/V1ScoringsConsolidatedDaily200ResponseResultInner} The populated <code>V1ScoringsConsolidatedDaily200ResponseResultInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new V1ScoringsConsolidatedDaily200ResponseResultInner();

            if (data.hasOwnProperty('AccelerationScore')) {
                obj['AccelerationScore'] = ApiClient.convertToType(data['AccelerationScore'], 'Number');
            }
            if (data.hasOwnProperty('AppId')) {
                obj['AppId'] = ApiClient.convertToType(data['AppId'], 'String');
            }
            if (data.hasOwnProperty('BrakingScore')) {
                obj['BrakingScore'] = ApiClient.convertToType(data['BrakingScore'], 'Number');
            }
            if (data.hasOwnProperty('CompanyId')) {
                obj['CompanyId'] = ApiClient.convertToType(data['CompanyId'], 'String');
            }
            if (data.hasOwnProperty('CorneringScore')) {
                obj['CorneringScore'] = ApiClient.convertToType(data['CorneringScore'], 'Number');
            }
            if (data.hasOwnProperty('DeviceToken')) {
                obj['DeviceToken'] = ApiClient.convertToType(data['DeviceToken'], 'String');
            }
            if (data.hasOwnProperty('DistractedScore')) {
                obj['DistractedScore'] = ApiClient.convertToType(data['DistractedScore'], 'Number');
            }
            if (data.hasOwnProperty('InstanceId')) {
                obj['InstanceId'] = ApiClient.convertToType(data['InstanceId'], 'String');
            }
            if (data.hasOwnProperty('OverallScore')) {
                obj['OverallScore'] = ApiClient.convertToType(data['OverallScore'], 'Number');
            }
            if (data.hasOwnProperty('ReportDate')) {
                obj['ReportDate'] = ApiClient.convertToType(data['ReportDate'], 'String');
            }
            if (data.hasOwnProperty('SpeedingScore')) {
                obj['SpeedingScore'] = ApiClient.convertToType(data['SpeedingScore'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>V1ScoringsConsolidatedDaily200ResponseResultInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>V1ScoringsConsolidatedDaily200ResponseResultInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AppId'] && !(typeof data['AppId'] === 'string' || data['AppId'] instanceof String)) {
            throw new Error("Expected the field `AppId` to be a primitive type in the JSON string but got " + data['AppId']);
        }
        // ensure the json data is a string
        if (data['CompanyId'] && !(typeof data['CompanyId'] === 'string' || data['CompanyId'] instanceof String)) {
            throw new Error("Expected the field `CompanyId` to be a primitive type in the JSON string but got " + data['CompanyId']);
        }
        // ensure the json data is a string
        if (data['DeviceToken'] && !(typeof data['DeviceToken'] === 'string' || data['DeviceToken'] instanceof String)) {
            throw new Error("Expected the field `DeviceToken` to be a primitive type in the JSON string but got " + data['DeviceToken']);
        }
        // ensure the json data is a string
        if (data['InstanceId'] && !(typeof data['InstanceId'] === 'string' || data['InstanceId'] instanceof String)) {
            throw new Error("Expected the field `InstanceId` to be a primitive type in the JSON string but got " + data['InstanceId']);
        }
        // ensure the json data is a string
        if (data['ReportDate'] && !(typeof data['ReportDate'] === 'string' || data['ReportDate'] instanceof String)) {
            throw new Error("Expected the field `ReportDate` to be a primitive type in the JSON string but got " + data['ReportDate']);
        }

        return true;
    }


}



/**
 * @member {Number} AccelerationScore
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['AccelerationScore'] = undefined;

/**
 * @member {String} AppId
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['AppId'] = undefined;

/**
 * @member {Number} BrakingScore
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['BrakingScore'] = undefined;

/**
 * @member {String} CompanyId
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['CompanyId'] = undefined;

/**
 * @member {Number} CorneringScore
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['CorneringScore'] = undefined;

/**
 * @member {String} DeviceToken
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['DeviceToken'] = undefined;

/**
 * @member {Number} DistractedScore
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['DistractedScore'] = undefined;

/**
 * @member {String} InstanceId
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['InstanceId'] = undefined;

/**
 * @member {Number} OverallScore
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['OverallScore'] = undefined;

/**
 * @member {String} ReportDate
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['ReportDate'] = undefined;

/**
 * @member {Number} SpeedingScore
 */
V1ScoringsConsolidatedDaily200ResponseResultInner.prototype['SpeedingScore'] = undefined;






export default V1ScoringsConsolidatedDaily200ResponseResultInner;

