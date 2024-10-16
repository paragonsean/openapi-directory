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
import CreateOrganizationAlertsProfileRequestAlertCondition from './CreateOrganizationAlertsProfileRequestAlertCondition';
import CreateOrganizationAlertsProfileRequestRecipients from './CreateOrganizationAlertsProfileRequestRecipients';

/**
 * The UpdateOrganizationAlertsProfileRequest model module.
 * @module model/UpdateOrganizationAlertsProfileRequest
 * @version 1.32.0
 */
class UpdateOrganizationAlertsProfileRequest {
    /**
     * Constructs a new <code>UpdateOrganizationAlertsProfileRequest</code>.
     * @alias module:model/UpdateOrganizationAlertsProfileRequest
     */
    constructor() { 
        
        UpdateOrganizationAlertsProfileRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateOrganizationAlertsProfileRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateOrganizationAlertsProfileRequest} obj Optional instance to populate.
     * @return {module:model/UpdateOrganizationAlertsProfileRequest} The populated <code>UpdateOrganizationAlertsProfileRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateOrganizationAlertsProfileRequest();

            if (data.hasOwnProperty('alertCondition')) {
                obj['alertCondition'] = CreateOrganizationAlertsProfileRequestAlertCondition.constructFromObject(data['alertCondition']);
            }
            if (data.hasOwnProperty('description')) {
                obj['description'] = ApiClient.convertToType(data['description'], 'String');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('networkTags')) {
                obj['networkTags'] = ApiClient.convertToType(data['networkTags'], ['String']);
            }
            if (data.hasOwnProperty('recipients')) {
                obj['recipients'] = CreateOrganizationAlertsProfileRequestRecipients.constructFromObject(data['recipients']);
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateOrganizationAlertsProfileRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateOrganizationAlertsProfileRequest</code>.
     */
    static validateJSON(data) {
        // validate the optional field `alertCondition`
        if (data['alertCondition']) { // data not null
          CreateOrganizationAlertsProfileRequestAlertCondition.validateJSON(data['alertCondition']);
        }
        // ensure the json data is a string
        if (data['description'] && !(typeof data['description'] === 'string' || data['description'] instanceof String)) {
            throw new Error("Expected the field `description` to be a primitive type in the JSON string but got " + data['description']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['networkTags'])) {
            throw new Error("Expected the field `networkTags` to be an array in the JSON data but got " + data['networkTags']);
        }
        // validate the optional field `recipients`
        if (data['recipients']) { // data not null
          CreateOrganizationAlertsProfileRequestRecipients.validateJSON(data['recipients']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}



/**
 * @member {module:model/CreateOrganizationAlertsProfileRequestAlertCondition} alertCondition
 */
UpdateOrganizationAlertsProfileRequest.prototype['alertCondition'] = undefined;

/**
 * User supplied description of the alert
 * @member {String} description
 */
UpdateOrganizationAlertsProfileRequest.prototype['description'] = undefined;

/**
 * Is the alert config enabled
 * @member {Boolean} enabled
 */
UpdateOrganizationAlertsProfileRequest.prototype['enabled'] = undefined;

/**
 * Networks with these tags will be monitored for the alert
 * @member {Array.<String>} networkTags
 */
UpdateOrganizationAlertsProfileRequest.prototype['networkTags'] = undefined;

/**
 * @member {module:model/CreateOrganizationAlertsProfileRequestRecipients} recipients
 */
UpdateOrganizationAlertsProfileRequest.prototype['recipients'] = undefined;

/**
 * The alert type
 * @member {module:model/UpdateOrganizationAlertsProfileRequest.TypeEnum} type
 */
UpdateOrganizationAlertsProfileRequest.prototype['type'] = undefined;





/**
 * Allowed values for the <code>type</code> property.
 * @enum {String}
 * @readonly
 */
UpdateOrganizationAlertsProfileRequest['TypeEnum'] = {

    /**
     * value: "appOutage"
     * @const
     */
    "appOutage": "appOutage",

    /**
     * value: "voipJitter"
     * @const
     */
    "voipJitter": "voipJitter",

    /**
     * value: "voipMos"
     * @const
     */
    "voipMos": "voipMos",

    /**
     * value: "voipPacketLoss"
     * @const
     */
    "voipPacketLoss": "voipPacketLoss",

    /**
     * value: "wanLatency"
     * @const
     */
    "wanLatency": "wanLatency",

    /**
     * value: "wanPacketLoss"
     * @const
     */
    "wanPacketLoss": "wanPacketLoss",

    /**
     * value: "wanStatus"
     * @const
     */
    "wanStatus": "wanStatus",

    /**
     * value: "wanUtilization"
     * @const
     */
    "wanUtilization": "wanUtilization"
};



export default UpdateOrganizationAlertsProfileRequest;

