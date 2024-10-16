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
 * The UpdateNetworkAlertsSettingsRequestDefaultDestinations model module.
 * @module model/UpdateNetworkAlertsSettingsRequestDefaultDestinations
 * @version 1.32.0
 */
class UpdateNetworkAlertsSettingsRequestDefaultDestinations {
    /**
     * Constructs a new <code>UpdateNetworkAlertsSettingsRequestDefaultDestinations</code>.
     * The network-wide destinations for all alerts on the network.
     * @alias module:model/UpdateNetworkAlertsSettingsRequestDefaultDestinations
     */
    constructor() { 
        
        UpdateNetworkAlertsSettingsRequestDefaultDestinations.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateNetworkAlertsSettingsRequestDefaultDestinations</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateNetworkAlertsSettingsRequestDefaultDestinations} obj Optional instance to populate.
     * @return {module:model/UpdateNetworkAlertsSettingsRequestDefaultDestinations} The populated <code>UpdateNetworkAlertsSettingsRequestDefaultDestinations</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateNetworkAlertsSettingsRequestDefaultDestinations();

            if (data.hasOwnProperty('allAdmins')) {
                obj['allAdmins'] = ApiClient.convertToType(data['allAdmins'], 'Boolean');
            }
            if (data.hasOwnProperty('emails')) {
                obj['emails'] = ApiClient.convertToType(data['emails'], ['String']);
            }
            if (data.hasOwnProperty('httpServerIds')) {
                obj['httpServerIds'] = ApiClient.convertToType(data['httpServerIds'], ['String']);
            }
            if (data.hasOwnProperty('snmp')) {
                obj['snmp'] = ApiClient.convertToType(data['snmp'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateNetworkAlertsSettingsRequestDefaultDestinations</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateNetworkAlertsSettingsRequestDefaultDestinations</code>.
     */
    static validateJSON(data) {
        // ensure the json data is an array
        if (!Array.isArray(data['emails'])) {
            throw new Error("Expected the field `emails` to be an array in the JSON data but got " + data['emails']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['httpServerIds'])) {
            throw new Error("Expected the field `httpServerIds` to be an array in the JSON data but got " + data['httpServerIds']);
        }

        return true;
    }


}



/**
 * If true, then all network admins will receive emails.
 * @member {Boolean} allAdmins
 */
UpdateNetworkAlertsSettingsRequestDefaultDestinations.prototype['allAdmins'] = undefined;

/**
 * A list of emails that will recieve the alert(s).
 * @member {Array.<String>} emails
 */
UpdateNetworkAlertsSettingsRequestDefaultDestinations.prototype['emails'] = undefined;

/**
 * A list of HTTP server IDs to send a Webhook to
 * @member {Array.<String>} httpServerIds
 */
UpdateNetworkAlertsSettingsRequestDefaultDestinations.prototype['httpServerIds'] = undefined;

/**
 * If true, then an SNMP trap will be sent if there is an SNMP trap server configured for this network.
 * @member {Boolean} snmp
 */
UpdateNetworkAlertsSettingsRequestDefaultDestinations.prototype['snmp'] = undefined;






export default UpdateNetworkAlertsSettingsRequestDefaultDestinations;

