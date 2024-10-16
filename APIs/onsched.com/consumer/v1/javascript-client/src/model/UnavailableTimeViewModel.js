/**
 * OnSched Consumer API
 * Build secure and scalable custom apps for Online Booking. Our flexible API provides many options for availability and booking.  <br><br>  Take the API for a test drive. Just click on the Authorize button below and authenticate.   You can access our demo company profile if you are not a customer, or your own profile by using your assigned ClientId and Secret.  <br><br>  The API has two interfaces, consumer and setup.   <ul>  <li>  The consumer interface provides all the endpoints required for implementing consumer booking flows.  </li>  <li>  The setup interface provides endpoints for profile configuration and setup.  </li>  </ul>  Toggle freely between the two interfaces using the swagger tool bar option labelled 'Select a definition'.  
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The UnavailableTimeViewModel model module.
 * @module model/UnavailableTimeViewModel
 * @version v1
 */
class UnavailableTimeViewModel {
    /**
     * Constructs a new <code>UnavailableTimeViewModel</code>.
     * @alias module:model/UnavailableTimeViewModel
     */
    constructor() { 
        
        UnavailableTimeViewModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UnavailableTimeViewModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UnavailableTimeViewModel} obj Optional instance to populate.
     * @return {module:model/UnavailableTimeViewModel} The populated <code>UnavailableTimeViewModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UnavailableTimeViewModel();

            if (data.hasOwnProperty('calendarId')) {
                obj['calendarId'] = ApiClient.convertToType(data['calendarId'], 'String');
            }
            if (data.hasOwnProperty('date')) {
                obj['date'] = ApiClient.convertToType(data['date'], 'String');
            }
            if (data.hasOwnProperty('endDateTime')) {
                obj['endDateTime'] = ApiClient.convertToType(data['endDateTime'], 'String');
            }
            if (data.hasOwnProperty('entityId')) {
                obj['entityId'] = ApiClient.convertToType(data['entityId'], 'Number');
            }
            if (data.hasOwnProperty('entityType')) {
                obj['entityType'] = ApiClient.convertToType(data['entityType'], 'String');
            }
            if (data.hasOwnProperty('fromTime')) {
                obj['fromTime'] = ApiClient.convertToType(data['fromTime'], 'Number');
            }
            if (data.hasOwnProperty('locationId')) {
                obj['locationId'] = ApiClient.convertToType(data['locationId'], 'String');
            }
            if (data.hasOwnProperty('objectName')) {
                obj['objectName'] = ApiClient.convertToType(data['objectName'], 'String');
            }
            if (data.hasOwnProperty('reason')) {
                obj['reason'] = ApiClient.convertToType(data['reason'], 'String');
            }
            if (data.hasOwnProperty('reasonCode')) {
                obj['reasonCode'] = ApiClient.convertToType(data['reasonCode'], 'String');
            }
            if (data.hasOwnProperty('resourceId')) {
                obj['resourceId'] = ApiClient.convertToType(data['resourceId'], 'String');
            }
            if (data.hasOwnProperty('resourceName')) {
                obj['resourceName'] = ApiClient.convertToType(data['resourceName'], 'String');
            }
            if (data.hasOwnProperty('serviceId')) {
                obj['serviceId'] = ApiClient.convertToType(data['serviceId'], 'String');
            }
            if (data.hasOwnProperty('serviceName')) {
                obj['serviceName'] = ApiClient.convertToType(data['serviceName'], 'String');
            }
            if (data.hasOwnProperty('startDateTime')) {
                obj['startDateTime'] = ApiClient.convertToType(data['startDateTime'], 'String');
            }
            if (data.hasOwnProperty('toTime')) {
                obj['toTime'] = ApiClient.convertToType(data['toTime'], 'Number');
            }
            if (data.hasOwnProperty('tzOffset')) {
                obj['tzOffset'] = ApiClient.convertToType(data['tzOffset'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UnavailableTimeViewModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UnavailableTimeViewModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['calendarId'] && !(typeof data['calendarId'] === 'string' || data['calendarId'] instanceof String)) {
            throw new Error("Expected the field `calendarId` to be a primitive type in the JSON string but got " + data['calendarId']);
        }
        // ensure the json data is a string
        if (data['date'] && !(typeof data['date'] === 'string' || data['date'] instanceof String)) {
            throw new Error("Expected the field `date` to be a primitive type in the JSON string but got " + data['date']);
        }
        // ensure the json data is a string
        if (data['endDateTime'] && !(typeof data['endDateTime'] === 'string' || data['endDateTime'] instanceof String)) {
            throw new Error("Expected the field `endDateTime` to be a primitive type in the JSON string but got " + data['endDateTime']);
        }
        // ensure the json data is a string
        if (data['entityType'] && !(typeof data['entityType'] === 'string' || data['entityType'] instanceof String)) {
            throw new Error("Expected the field `entityType` to be a primitive type in the JSON string but got " + data['entityType']);
        }
        // ensure the json data is a string
        if (data['locationId'] && !(typeof data['locationId'] === 'string' || data['locationId'] instanceof String)) {
            throw new Error("Expected the field `locationId` to be a primitive type in the JSON string but got " + data['locationId']);
        }
        // ensure the json data is a string
        if (data['objectName'] && !(typeof data['objectName'] === 'string' || data['objectName'] instanceof String)) {
            throw new Error("Expected the field `objectName` to be a primitive type in the JSON string but got " + data['objectName']);
        }
        // ensure the json data is a string
        if (data['reason'] && !(typeof data['reason'] === 'string' || data['reason'] instanceof String)) {
            throw new Error("Expected the field `reason` to be a primitive type in the JSON string but got " + data['reason']);
        }
        // ensure the json data is a string
        if (data['reasonCode'] && !(typeof data['reasonCode'] === 'string' || data['reasonCode'] instanceof String)) {
            throw new Error("Expected the field `reasonCode` to be a primitive type in the JSON string but got " + data['reasonCode']);
        }
        // ensure the json data is a string
        if (data['resourceId'] && !(typeof data['resourceId'] === 'string' || data['resourceId'] instanceof String)) {
            throw new Error("Expected the field `resourceId` to be a primitive type in the JSON string but got " + data['resourceId']);
        }
        // ensure the json data is a string
        if (data['resourceName'] && !(typeof data['resourceName'] === 'string' || data['resourceName'] instanceof String)) {
            throw new Error("Expected the field `resourceName` to be a primitive type in the JSON string but got " + data['resourceName']);
        }
        // ensure the json data is a string
        if (data['serviceId'] && !(typeof data['serviceId'] === 'string' || data['serviceId'] instanceof String)) {
            throw new Error("Expected the field `serviceId` to be a primitive type in the JSON string but got " + data['serviceId']);
        }
        // ensure the json data is a string
        if (data['serviceName'] && !(typeof data['serviceName'] === 'string' || data['serviceName'] instanceof String)) {
            throw new Error("Expected the field `serviceName` to be a primitive type in the JSON string but got " + data['serviceName']);
        }
        // ensure the json data is a string
        if (data['startDateTime'] && !(typeof data['startDateTime'] === 'string' || data['startDateTime'] instanceof String)) {
            throw new Error("Expected the field `startDateTime` to be a primitive type in the JSON string but got " + data['startDateTime']);
        }

        return true;
    }


}



/**
 * @member {String} calendarId
 */
UnavailableTimeViewModel.prototype['calendarId'] = undefined;

/**
 * @member {String} date
 */
UnavailableTimeViewModel.prototype['date'] = undefined;

/**
 * @member {String} endDateTime
 */
UnavailableTimeViewModel.prototype['endDateTime'] = undefined;

/**
 * @member {Number} entityId
 */
UnavailableTimeViewModel.prototype['entityId'] = undefined;

/**
 * @member {String} entityType
 */
UnavailableTimeViewModel.prototype['entityType'] = undefined;

/**
 * @member {Number} fromTime
 */
UnavailableTimeViewModel.prototype['fromTime'] = undefined;

/**
 * @member {String} locationId
 */
UnavailableTimeViewModel.prototype['locationId'] = undefined;

/**
 * @member {String} objectName
 */
UnavailableTimeViewModel.prototype['objectName'] = undefined;

/**
 * @member {String} reason
 */
UnavailableTimeViewModel.prototype['reason'] = undefined;

/**
 * @member {String} reasonCode
 */
UnavailableTimeViewModel.prototype['reasonCode'] = undefined;

/**
 * @member {String} resourceId
 */
UnavailableTimeViewModel.prototype['resourceId'] = undefined;

/**
 * @member {String} resourceName
 */
UnavailableTimeViewModel.prototype['resourceName'] = undefined;

/**
 * @member {String} serviceId
 */
UnavailableTimeViewModel.prototype['serviceId'] = undefined;

/**
 * @member {String} serviceName
 */
UnavailableTimeViewModel.prototype['serviceName'] = undefined;

/**
 * @member {String} startDateTime
 */
UnavailableTimeViewModel.prototype['startDateTime'] = undefined;

/**
 * @member {Number} toTime
 */
UnavailableTimeViewModel.prototype['toTime'] = undefined;

/**
 * @member {Number} tzOffset
 */
UnavailableTimeViewModel.prototype['tzOffset'] = undefined;






export default UnavailableTimeViewModel;

