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
import CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner from './CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner';
import CreateNetworkFirmwareUpgradesRollbackRequestToVersion from './CreateNetworkFirmwareUpgradesRollbackRequestToVersion';

/**
 * The CreateNetworkFirmwareUpgradesRollbackRequest model module.
 * @module model/CreateNetworkFirmwareUpgradesRollbackRequest
 * @version 1.32.0
 */
class CreateNetworkFirmwareUpgradesRollbackRequest {
    /**
     * Constructs a new <code>CreateNetworkFirmwareUpgradesRollbackRequest</code>.
     * @alias module:model/CreateNetworkFirmwareUpgradesRollbackRequest
     * @param reasons {Array.<module:model/CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner>} Reasons for the rollback
     */
    constructor(reasons) { 
        
        CreateNetworkFirmwareUpgradesRollbackRequest.initialize(this, reasons);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, reasons) { 
        obj['reasons'] = reasons;
    }

    /**
     * Constructs a <code>CreateNetworkFirmwareUpgradesRollbackRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkFirmwareUpgradesRollbackRequest} obj Optional instance to populate.
     * @return {module:model/CreateNetworkFirmwareUpgradesRollbackRequest} The populated <code>CreateNetworkFirmwareUpgradesRollbackRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkFirmwareUpgradesRollbackRequest();

            if (data.hasOwnProperty('product')) {
                obj['product'] = ApiClient.convertToType(data['product'], 'String');
            }
            if (data.hasOwnProperty('reasons')) {
                obj['reasons'] = ApiClient.convertToType(data['reasons'], [CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner]);
            }
            if (data.hasOwnProperty('time')) {
                obj['time'] = ApiClient.convertToType(data['time'], 'Date');
            }
            if (data.hasOwnProperty('toVersion')) {
                obj['toVersion'] = CreateNetworkFirmwareUpgradesRollbackRequestToVersion.constructFromObject(data['toVersion']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkFirmwareUpgradesRollbackRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkFirmwareUpgradesRollbackRequest</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CreateNetworkFirmwareUpgradesRollbackRequest.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['product'] && !(typeof data['product'] === 'string' || data['product'] instanceof String)) {
            throw new Error("Expected the field `product` to be a primitive type in the JSON string but got " + data['product']);
        }
        if (data['reasons']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['reasons'])) {
                throw new Error("Expected the field `reasons` to be an array in the JSON data but got " + data['reasons']);
            }
            // validate the optional field `reasons` (array)
            for (const item of data['reasons']) {
                CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner.validateJSON(item);
            };
        }
        // validate the optional field `toVersion`
        if (data['toVersion']) { // data not null
          CreateNetworkFirmwareUpgradesRollbackRequestToVersion.validateJSON(data['toVersion']);
        }

        return true;
    }


}

CreateNetworkFirmwareUpgradesRollbackRequest.RequiredProperties = ["reasons"];

/**
 * Product type to rollback (if the network is a combined network)
 * @member {module:model/CreateNetworkFirmwareUpgradesRollbackRequest.ProductEnum} product
 */
CreateNetworkFirmwareUpgradesRollbackRequest.prototype['product'] = undefined;

/**
 * Reasons for the rollback
 * @member {Array.<module:model/CreateNetworkFirmwareUpgradesRollbackRequestReasonsInner>} reasons
 */
CreateNetworkFirmwareUpgradesRollbackRequest.prototype['reasons'] = undefined;

/**
 * Scheduled time for the rollback
 * @member {Date} time
 */
CreateNetworkFirmwareUpgradesRollbackRequest.prototype['time'] = undefined;

/**
 * @member {module:model/CreateNetworkFirmwareUpgradesRollbackRequestToVersion} toVersion
 */
CreateNetworkFirmwareUpgradesRollbackRequest.prototype['toVersion'] = undefined;





/**
 * Allowed values for the <code>product</code> property.
 * @enum {String}
 * @readonly
 */
CreateNetworkFirmwareUpgradesRollbackRequest['ProductEnum'] = {

    /**
     * value: "appliance"
     * @const
     */
    "appliance": "appliance",

    /**
     * value: "camera"
     * @const
     */
    "camera": "camera",

    /**
     * value: "cellularGateway"
     * @const
     */
    "cellularGateway": "cellularGateway",

    /**
     * value: "switch"
     * @const
     */
    "switch": "switch",

    /**
     * value: "wireless"
     * @const
     */
    "wireless": "wireless"
};



export default CreateNetworkFirmwareUpgradesRollbackRequest;

