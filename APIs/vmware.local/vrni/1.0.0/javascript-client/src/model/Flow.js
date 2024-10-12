/**
 * vRealize Network Insight API Reference
 * vRealize Network Insight API Reference
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
import BaseEntity from './BaseEntity';
import EntityType from './EntityType';
import FirewallAction from './FirewallAction';
import FlowTag from './FlowTag';
import FlowTrafficType from './FlowTrafficType';
import IpV4Address from './IpV4Address';
import PortRange from './PortRange';
import Protocol from './Protocol';
import Reference from './Reference';

/**
 * The Flow model module.
 * @module model/Flow
 * @version 1.0.0
 */
class Flow {
    /**
     * Constructs a new <code>Flow</code>.
     * @alias module:model/Flow
     * @extends module:model/BaseEntity
     * @implements module:model/BaseEntity
     */
    constructor() { 
        BaseEntity.initialize(this);
        Flow.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>Flow</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Flow} obj Optional instance to populate.
     * @return {module:model/Flow} The populated <code>Flow</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Flow();
            BaseEntity.constructFromObject(data, obj);
            BaseEntity.constructFromObject(data, obj);

            if (data.hasOwnProperty('destination_cluster')) {
                obj['destination_cluster'] = Reference.constructFromObject(data['destination_cluster']);
            }
            if (data.hasOwnProperty('destination_datacenter')) {
                obj['destination_datacenter'] = Reference.constructFromObject(data['destination_datacenter']);
            }
            if (data.hasOwnProperty('destination_folders')) {
                obj['destination_folders'] = ApiClient.convertToType(data['destination_folders'], [Reference]);
            }
            if (data.hasOwnProperty('destination_host')) {
                obj['destination_host'] = Reference.constructFromObject(data['destination_host']);
            }
            if (data.hasOwnProperty('destination_ip')) {
                obj['destination_ip'] = IpV4Address.constructFromObject(data['destination_ip']);
            }
            if (data.hasOwnProperty('destination_ip_sets')) {
                obj['destination_ip_sets'] = ApiClient.convertToType(data['destination_ip_sets'], [Reference]);
            }
            if (data.hasOwnProperty('destination_l2_network')) {
                obj['destination_l2_network'] = Reference.constructFromObject(data['destination_l2_network']);
            }
            if (data.hasOwnProperty('destination_resource_pool')) {
                obj['destination_resource_pool'] = Reference.constructFromObject(data['destination_resource_pool']);
            }
            if (data.hasOwnProperty('destination_security_groups')) {
                obj['destination_security_groups'] = ApiClient.convertToType(data['destination_security_groups'], [Reference]);
            }
            if (data.hasOwnProperty('destination_security_tags')) {
                obj['destination_security_tags'] = ApiClient.convertToType(data['destination_security_tags'], [Reference]);
            }
            if (data.hasOwnProperty('destination_vm')) {
                obj['destination_vm'] = Reference.constructFromObject(data['destination_vm']);
            }
            if (data.hasOwnProperty('destination_vm_tags')) {
                obj['destination_vm_tags'] = ApiClient.convertToType(data['destination_vm_tags'], ['String']);
            }
            if (data.hasOwnProperty('destination_vnic')) {
                obj['destination_vnic'] = Reference.constructFromObject(data['destination_vnic']);
            }
            if (data.hasOwnProperty('destination_vpc')) {
                obj['destination_vpc'] = Reference.constructFromObject(data['destination_vpc']);
            }
            if (data.hasOwnProperty('firewall_action')) {
                obj['firewall_action'] = FirewallAction.constructFromObject(data['firewall_action']);
            }
            if (data.hasOwnProperty('flow_tag')) {
                obj['flow_tag'] = ApiClient.convertToType(data['flow_tag'], [FlowTag]);
            }
            if (data.hasOwnProperty('port')) {
                obj['port'] = PortRange.constructFromObject(data['port']);
            }
            if (data.hasOwnProperty('protocol')) {
                obj['protocol'] = Protocol.constructFromObject(data['protocol']);
            }
            if (data.hasOwnProperty('source_cluster')) {
                obj['source_cluster'] = Reference.constructFromObject(data['source_cluster']);
            }
            if (data.hasOwnProperty('source_datacenter')) {
                obj['source_datacenter'] = Reference.constructFromObject(data['source_datacenter']);
            }
            if (data.hasOwnProperty('source_folders')) {
                obj['source_folders'] = ApiClient.convertToType(data['source_folders'], [Reference]);
            }
            if (data.hasOwnProperty('source_host')) {
                obj['source_host'] = Reference.constructFromObject(data['source_host']);
            }
            if (data.hasOwnProperty('source_ip')) {
                obj['source_ip'] = IpV4Address.constructFromObject(data['source_ip']);
            }
            if (data.hasOwnProperty('source_ip_sets')) {
                obj['source_ip_sets'] = ApiClient.convertToType(data['source_ip_sets'], [Reference]);
            }
            if (data.hasOwnProperty('source_l2_network')) {
                obj['source_l2_network'] = Reference.constructFromObject(data['source_l2_network']);
            }
            if (data.hasOwnProperty('source_resource_pool')) {
                obj['source_resource_pool'] = Reference.constructFromObject(data['source_resource_pool']);
            }
            if (data.hasOwnProperty('source_security_groups')) {
                obj['source_security_groups'] = ApiClient.convertToType(data['source_security_groups'], [Reference]);
            }
            if (data.hasOwnProperty('source_security_tags')) {
                obj['source_security_tags'] = ApiClient.convertToType(data['source_security_tags'], [Reference]);
            }
            if (data.hasOwnProperty('source_vm')) {
                obj['source_vm'] = Reference.constructFromObject(data['source_vm']);
            }
            if (data.hasOwnProperty('source_vm_tags')) {
                obj['source_vm_tags'] = ApiClient.convertToType(data['source_vm_tags'], ['String']);
            }
            if (data.hasOwnProperty('source_vnic')) {
                obj['source_vnic'] = Reference.constructFromObject(data['source_vnic']);
            }
            if (data.hasOwnProperty('source_vpc')) {
                obj['source_vpc'] = Reference.constructFromObject(data['source_vpc']);
            }
            if (data.hasOwnProperty('traffic_type')) {
                obj['traffic_type'] = FlowTrafficType.constructFromObject(data['traffic_type']);
            }
            if (data.hasOwnProperty('within_host')) {
                obj['within_host'] = ApiClient.convertToType(data['within_host'], 'Boolean');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Flow</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Flow</code>.
     */
    static validateJSON(data) {
        // validate the optional field `destination_cluster`
        if (data['destination_cluster']) { // data not null
          Reference.validateJSON(data['destination_cluster']);
        }
        // validate the optional field `destination_datacenter`
        if (data['destination_datacenter']) { // data not null
          Reference.validateJSON(data['destination_datacenter']);
        }
        if (data['destination_folders']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['destination_folders'])) {
                throw new Error("Expected the field `destination_folders` to be an array in the JSON data but got " + data['destination_folders']);
            }
            // validate the optional field `destination_folders` (array)
            for (const item of data['destination_folders']) {
                Reference.validateJSON(item);
            };
        }
        // validate the optional field `destination_host`
        if (data['destination_host']) { // data not null
          Reference.validateJSON(data['destination_host']);
        }
        // validate the optional field `destination_ip`
        if (data['destination_ip']) { // data not null
          IpV4Address.validateJSON(data['destination_ip']);
        }
        if (data['destination_ip_sets']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['destination_ip_sets'])) {
                throw new Error("Expected the field `destination_ip_sets` to be an array in the JSON data but got " + data['destination_ip_sets']);
            }
            // validate the optional field `destination_ip_sets` (array)
            for (const item of data['destination_ip_sets']) {
                Reference.validateJSON(item);
            };
        }
        // validate the optional field `destination_l2_network`
        if (data['destination_l2_network']) { // data not null
          Reference.validateJSON(data['destination_l2_network']);
        }
        // validate the optional field `destination_resource_pool`
        if (data['destination_resource_pool']) { // data not null
          Reference.validateJSON(data['destination_resource_pool']);
        }
        if (data['destination_security_groups']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['destination_security_groups'])) {
                throw new Error("Expected the field `destination_security_groups` to be an array in the JSON data but got " + data['destination_security_groups']);
            }
            // validate the optional field `destination_security_groups` (array)
            for (const item of data['destination_security_groups']) {
                Reference.validateJSON(item);
            };
        }
        if (data['destination_security_tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['destination_security_tags'])) {
                throw new Error("Expected the field `destination_security_tags` to be an array in the JSON data but got " + data['destination_security_tags']);
            }
            // validate the optional field `destination_security_tags` (array)
            for (const item of data['destination_security_tags']) {
                Reference.validateJSON(item);
            };
        }
        // validate the optional field `destination_vm`
        if (data['destination_vm']) { // data not null
          Reference.validateJSON(data['destination_vm']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['destination_vm_tags'])) {
            throw new Error("Expected the field `destination_vm_tags` to be an array in the JSON data but got " + data['destination_vm_tags']);
        }
        // validate the optional field `destination_vnic`
        if (data['destination_vnic']) { // data not null
          Reference.validateJSON(data['destination_vnic']);
        }
        // validate the optional field `destination_vpc`
        if (data['destination_vpc']) { // data not null
          Reference.validateJSON(data['destination_vpc']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['flow_tag'])) {
            throw new Error("Expected the field `flow_tag` to be an array in the JSON data but got " + data['flow_tag']);
        }
        // validate the optional field `port`
        if (data['port']) { // data not null
          PortRange.validateJSON(data['port']);
        }
        // validate the optional field `source_cluster`
        if (data['source_cluster']) { // data not null
          Reference.validateJSON(data['source_cluster']);
        }
        // validate the optional field `source_datacenter`
        if (data['source_datacenter']) { // data not null
          Reference.validateJSON(data['source_datacenter']);
        }
        if (data['source_folders']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['source_folders'])) {
                throw new Error("Expected the field `source_folders` to be an array in the JSON data but got " + data['source_folders']);
            }
            // validate the optional field `source_folders` (array)
            for (const item of data['source_folders']) {
                Reference.validateJSON(item);
            };
        }
        // validate the optional field `source_host`
        if (data['source_host']) { // data not null
          Reference.validateJSON(data['source_host']);
        }
        // validate the optional field `source_ip`
        if (data['source_ip']) { // data not null
          IpV4Address.validateJSON(data['source_ip']);
        }
        if (data['source_ip_sets']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['source_ip_sets'])) {
                throw new Error("Expected the field `source_ip_sets` to be an array in the JSON data but got " + data['source_ip_sets']);
            }
            // validate the optional field `source_ip_sets` (array)
            for (const item of data['source_ip_sets']) {
                Reference.validateJSON(item);
            };
        }
        // validate the optional field `source_l2_network`
        if (data['source_l2_network']) { // data not null
          Reference.validateJSON(data['source_l2_network']);
        }
        // validate the optional field `source_resource_pool`
        if (data['source_resource_pool']) { // data not null
          Reference.validateJSON(data['source_resource_pool']);
        }
        if (data['source_security_groups']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['source_security_groups'])) {
                throw new Error("Expected the field `source_security_groups` to be an array in the JSON data but got " + data['source_security_groups']);
            }
            // validate the optional field `source_security_groups` (array)
            for (const item of data['source_security_groups']) {
                Reference.validateJSON(item);
            };
        }
        if (data['source_security_tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['source_security_tags'])) {
                throw new Error("Expected the field `source_security_tags` to be an array in the JSON data but got " + data['source_security_tags']);
            }
            // validate the optional field `source_security_tags` (array)
            for (const item of data['source_security_tags']) {
                Reference.validateJSON(item);
            };
        }
        // validate the optional field `source_vm`
        if (data['source_vm']) { // data not null
          Reference.validateJSON(data['source_vm']);
        }
        // ensure the json data is an array
        if (!Array.isArray(data['source_vm_tags'])) {
            throw new Error("Expected the field `source_vm_tags` to be an array in the JSON data but got " + data['source_vm_tags']);
        }
        // validate the optional field `source_vnic`
        if (data['source_vnic']) { // data not null
          Reference.validateJSON(data['source_vnic']);
        }
        // validate the optional field `source_vpc`
        if (data['source_vpc']) { // data not null
          Reference.validateJSON(data['source_vpc']);
        }

        return true;
    }


}



/**
 * @member {module:model/Reference} destination_cluster
 */
Flow.prototype['destination_cluster'] = undefined;

/**
 * @member {module:model/Reference} destination_datacenter
 */
Flow.prototype['destination_datacenter'] = undefined;

/**
 * @member {Array.<module:model/Reference>} destination_folders
 */
Flow.prototype['destination_folders'] = undefined;

/**
 * @member {module:model/Reference} destination_host
 */
Flow.prototype['destination_host'] = undefined;

/**
 * @member {module:model/IpV4Address} destination_ip
 */
Flow.prototype['destination_ip'] = undefined;

/**
 * @member {Array.<module:model/Reference>} destination_ip_sets
 */
Flow.prototype['destination_ip_sets'] = undefined;

/**
 * @member {module:model/Reference} destination_l2_network
 */
Flow.prototype['destination_l2_network'] = undefined;

/**
 * @member {module:model/Reference} destination_resource_pool
 */
Flow.prototype['destination_resource_pool'] = undefined;

/**
 * @member {Array.<module:model/Reference>} destination_security_groups
 */
Flow.prototype['destination_security_groups'] = undefined;

/**
 * @member {Array.<module:model/Reference>} destination_security_tags
 */
Flow.prototype['destination_security_tags'] = undefined;

/**
 * @member {module:model/Reference} destination_vm
 */
Flow.prototype['destination_vm'] = undefined;

/**
 * @member {Array.<String>} destination_vm_tags
 */
Flow.prototype['destination_vm_tags'] = undefined;

/**
 * @member {module:model/Reference} destination_vnic
 */
Flow.prototype['destination_vnic'] = undefined;

/**
 * @member {module:model/Reference} destination_vpc
 */
Flow.prototype['destination_vpc'] = undefined;

/**
 * @member {module:model/FirewallAction} firewall_action
 */
Flow.prototype['firewall_action'] = undefined;

/**
 * @member {Array.<module:model/FlowTag>} flow_tag
 */
Flow.prototype['flow_tag'] = undefined;

/**
 * @member {module:model/PortRange} port
 */
Flow.prototype['port'] = undefined;

/**
 * @member {module:model/Protocol} protocol
 */
Flow.prototype['protocol'] = undefined;

/**
 * @member {module:model/Reference} source_cluster
 */
Flow.prototype['source_cluster'] = undefined;

/**
 * @member {module:model/Reference} source_datacenter
 */
Flow.prototype['source_datacenter'] = undefined;

/**
 * @member {Array.<module:model/Reference>} source_folders
 */
Flow.prototype['source_folders'] = undefined;

/**
 * @member {module:model/Reference} source_host
 */
Flow.prototype['source_host'] = undefined;

/**
 * @member {module:model/IpV4Address} source_ip
 */
Flow.prototype['source_ip'] = undefined;

/**
 * @member {Array.<module:model/Reference>} source_ip_sets
 */
Flow.prototype['source_ip_sets'] = undefined;

/**
 * @member {module:model/Reference} source_l2_network
 */
Flow.prototype['source_l2_network'] = undefined;

/**
 * @member {module:model/Reference} source_resource_pool
 */
Flow.prototype['source_resource_pool'] = undefined;

/**
 * @member {Array.<module:model/Reference>} source_security_groups
 */
Flow.prototype['source_security_groups'] = undefined;

/**
 * @member {Array.<module:model/Reference>} source_security_tags
 */
Flow.prototype['source_security_tags'] = undefined;

/**
 * @member {module:model/Reference} source_vm
 */
Flow.prototype['source_vm'] = undefined;

/**
 * @member {Array.<String>} source_vm_tags
 */
Flow.prototype['source_vm_tags'] = undefined;

/**
 * @member {module:model/Reference} source_vnic
 */
Flow.prototype['source_vnic'] = undefined;

/**
 * @member {module:model/Reference} source_vpc
 */
Flow.prototype['source_vpc'] = undefined;

/**
 * @member {module:model/FlowTrafficType} traffic_type
 */
Flow.prototype['traffic_type'] = undefined;

/**
 * @member {Boolean} within_host
 */
Flow.prototype['within_host'] = undefined;


// Implement BaseEntity interface:
/**
 * @member {String} entity_id
 */
BaseEntity.prototype['entity_id'] = undefined;
/**
 * @member {module:model/EntityType} entity_type
 */
BaseEntity.prototype['entity_type'] = undefined;
/**
 * @member {String} name
 */
BaseEntity.prototype['name'] = undefined;




export default Flow;

