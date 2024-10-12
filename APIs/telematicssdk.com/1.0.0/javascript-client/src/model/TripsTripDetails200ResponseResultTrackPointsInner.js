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
 * The TripsTripDetails200ResponseResultTrackPointsInner model module.
 * @module model/TripsTripDetails200ResponseResultTrackPointsInner
 * @version 1.0.0
 */
class TripsTripDetails200ResponseResultTrackPointsInner {
    /**
     * Constructs a new <code>TripsTripDetails200ResponseResultTrackPointsInner</code>.
     * @alias module:model/TripsTripDetails200ResponseResultTrackPointsInner
     */
    constructor() { 
        
        TripsTripDetails200ResponseResultTrackPointsInner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TripsTripDetails200ResponseResultTrackPointsInner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TripsTripDetails200ResponseResultTrackPointsInner} obj Optional instance to populate.
     * @return {module:model/TripsTripDetails200ResponseResultTrackPointsInner} The populated <code>TripsTripDetails200ResponseResultTrackPointsInner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TripsTripDetails200ResponseResultTrackPointsInner();

            if (data.hasOwnProperty('AlertType')) {
                obj['AlertType'] = ApiClient.convertToType(data['AlertType'], 'String');
            }
            if (data.hasOwnProperty('AlertValue')) {
                obj['AlertValue'] = ApiClient.convertToType(data['AlertValue'], 'Number');
            }
            if (data.hasOwnProperty('Cornering')) {
                obj['Cornering'] = ApiClient.convertToType(data['Cornering'], 'Boolean');
            }
            if (data.hasOwnProperty('Course')) {
                obj['Course'] = ApiClient.convertToType(data['Course'], 'Number');
            }
            if (data.hasOwnProperty('Height')) {
                obj['Height'] = ApiClient.convertToType(data['Height'], 'Number');
            }
            if (data.hasOwnProperty('Id')) {
                obj['Id'] = ApiClient.convertToType(data['Id'], 'Number');
            }
            if (data.hasOwnProperty('Lateral')) {
                obj['Lateral'] = ApiClient.convertToType(data['Lateral'], 'Number');
            }
            if (data.hasOwnProperty('Latitude')) {
                obj['Latitude'] = ApiClient.convertToType(data['Latitude'], 'Number');
            }
            if (data.hasOwnProperty('Longitude')) {
                obj['Longitude'] = ApiClient.convertToType(data['Longitude'], 'Number');
            }
            if (data.hasOwnProperty('MidSpeed')) {
                obj['MidSpeed'] = ApiClient.convertToType(data['MidSpeed'], 'Number');
            }
            if (data.hasOwnProperty('Number')) {
                obj['Number'] = ApiClient.convertToType(data['Number'], 'Number');
            }
            if (data.hasOwnProperty('PhoneUsage')) {
                obj['PhoneUsage'] = ApiClient.convertToType(data['PhoneUsage'], 'Boolean');
            }
            if (data.hasOwnProperty('PointDate')) {
                obj['PointDate'] = ApiClient.convertToType(data['PointDate'], 'String');
            }
            if (data.hasOwnProperty('Speed')) {
                obj['Speed'] = ApiClient.convertToType(data['Speed'], 'Number');
            }
            if (data.hasOwnProperty('SpeedLimit')) {
                obj['SpeedLimit'] = ApiClient.convertToType(data['SpeedLimit'], 'Number');
            }
            if (data.hasOwnProperty('SpeedType')) {
                obj['SpeedType'] = ApiClient.convertToType(data['SpeedType'], 'String');
            }
            if (data.hasOwnProperty('TotalMeters')) {
                obj['TotalMeters'] = ApiClient.convertToType(data['TotalMeters'], 'Number');
            }
            if (data.hasOwnProperty('Yaw')) {
                obj['Yaw'] = ApiClient.convertToType(data['Yaw'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TripsTripDetails200ResponseResultTrackPointsInner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TripsTripDetails200ResponseResultTrackPointsInner</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['AlertType'] && !(typeof data['AlertType'] === 'string' || data['AlertType'] instanceof String)) {
            throw new Error("Expected the field `AlertType` to be a primitive type in the JSON string but got " + data['AlertType']);
        }
        // ensure the json data is a string
        if (data['PointDate'] && !(typeof data['PointDate'] === 'string' || data['PointDate'] instanceof String)) {
            throw new Error("Expected the field `PointDate` to be a primitive type in the JSON string but got " + data['PointDate']);
        }
        // ensure the json data is a string
        if (data['SpeedType'] && !(typeof data['SpeedType'] === 'string' || data['SpeedType'] instanceof String)) {
            throw new Error("Expected the field `SpeedType` to be a primitive type in the JSON string but got " + data['SpeedType']);
        }

        return true;
    }


}



/**
 * @member {String} AlertType
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['AlertType'] = undefined;

/**
 * @member {Number} AlertValue
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['AlertValue'] = undefined;

/**
 * @member {Boolean} Cornering
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Cornering'] = undefined;

/**
 * @member {Number} Course
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Course'] = undefined;

/**
 * @member {Number} Height
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Height'] = undefined;

/**
 * @member {Number} Id
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Id'] = undefined;

/**
 * @member {Number} Lateral
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Lateral'] = undefined;

/**
 * @member {Number} Latitude
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Latitude'] = undefined;

/**
 * @member {Number} Longitude
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Longitude'] = undefined;

/**
 * @member {Number} MidSpeed
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['MidSpeed'] = undefined;

/**
 * @member {Number} Number
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Number'] = undefined;

/**
 * @member {Boolean} PhoneUsage
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['PhoneUsage'] = undefined;

/**
 * @member {String} PointDate
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['PointDate'] = undefined;

/**
 * @member {Number} Speed
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Speed'] = undefined;

/**
 * @member {Number} SpeedLimit
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['SpeedLimit'] = undefined;

/**
 * @member {String} SpeedType
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['SpeedType'] = undefined;

/**
 * @member {Number} TotalMeters
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['TotalMeters'] = undefined;

/**
 * @member {Number} Yaw
 */
TripsTripDetails200ResponseResultTrackPointsInner.prototype['Yaw'] = undefined;






export default TripsTripDetails200ResponseResultTrackPointsInner;

