/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 05 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 1.32.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest model module.
 * @module model/CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
 * @version 1.32.0
 */
class CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest {
    /**
     * Constructs a new <code>CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest</code>.
     * @alias module:model/CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest
     * @param logEvent {String} The type of log event this is recording, e.g. download or opening a banner
     * @param timestamp {Number} A JavaScript UTC datetime stamp for when the even occurred
     */
    constructor(logEvent, timestamp) { 
        
        CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.initialize(this, logEvent, timestamp);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, logEvent, timestamp) { 
        obj['logEvent'] = logEvent;
        obj['timestamp'] = timestamp;
    }

    /**
     * Constructs a <code>CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest} obj Optional instance to populate.
     * @return {module:model/CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest} The populated <code>CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest();

            if (data.hasOwnProperty('logEvent')) {
                obj['logEvent'] = ApiClient.convertToType(data['logEvent'], 'String');
            }
            if (data.hasOwnProperty('request')) {
                obj['request'] = ApiClient.convertToType(data['request'], 'String');
            }
            if (data.hasOwnProperty('targetOS')) {
                obj['targetOS'] = ApiClient.convertToType(data['targetOS'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['logEvent'] && !(typeof data['logEvent'] === 'string' || data['logEvent'] instanceof String)) {
            throw new Error("Expected the field `logEvent` to be a primitive type in the JSON string but got " + data['logEvent']);
        }
        // ensure the json data is a string
        if (data['request'] && !(typeof data['request'] === 'string' || data['request'] instanceof String)) {
            throw new Error("Expected the field `request` to be a primitive type in the JSON string but got " + data['request']);
        }
        // ensure the json data is a string
        if (data['targetOS'] && !(typeof data['targetOS'] === 'string' || data['targetOS'] instanceof String)) {
            throw new Error("Expected the field `targetOS` to be a primitive type in the JSON string but got " + data['targetOS']);
        }

        return true;
    }


}

CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.RequiredProperties = ["logEvent", "timestamp"];

/**
 * The type of log event this is recording, e.g. download or opening a banner
 * @member {String} logEvent
 */
CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.prototype['logEvent'] = undefined;

/**
 * Used to describe if this event was the result of a redirect. E.g. a query param if an info banner is being used
 * @member {String} request
 */
CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.prototype['request'] = undefined;

/**
 * The name of the onboarding distro being downloaded
 * @member {String} targetOS
 */
CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.prototype['targetOS'] = undefined;

/**
 * A JavaScript UTC datetime stamp for when the even occurred
 * @member {Number} timestamp
 */
CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest.prototype['timestamp'] = undefined;






export default CreateOrganizationInventoryOnboardingCloudMonitoringExportEventRequest;

