/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The RmaDataTrackInterface model module.
 * @module model/RmaDataTrackInterface
 * @version 2.2.10
 */
class RmaDataTrackInterface {
    /**
     * Constructs a new <code>RmaDataTrackInterface</code>.
     * Interface TrackInterface
     * @alias module:model/RmaDataTrackInterface
     * @param carrierCode {String} Carrier code
     * @param carrierTitle {String} Carrier title
     * @param entityId {Number} Entity id
     * @param rmaEntityId {Number} Rma entity id
     * @param trackNumber {String} Track number
     */
    constructor(carrierCode, carrierTitle, entityId, rmaEntityId, trackNumber) { 
        
        RmaDataTrackInterface.initialize(this, carrierCode, carrierTitle, entityId, rmaEntityId, trackNumber);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, carrierCode, carrierTitle, entityId, rmaEntityId, trackNumber) { 
        obj['carrier_code'] = carrierCode;
        obj['carrier_title'] = carrierTitle;
        obj['entity_id'] = entityId;
        obj['rma_entity_id'] = rmaEntityId;
        obj['track_number'] = trackNumber;
    }

    /**
     * Constructs a <code>RmaDataTrackInterface</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/RmaDataTrackInterface} obj Optional instance to populate.
     * @return {module:model/RmaDataTrackInterface} The populated <code>RmaDataTrackInterface</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new RmaDataTrackInterface();

            if (data.hasOwnProperty('carrier_code')) {
                obj['carrier_code'] = ApiClient.convertToType(data['carrier_code'], 'String');
            }
            if (data.hasOwnProperty('carrier_title')) {
                obj['carrier_title'] = ApiClient.convertToType(data['carrier_title'], 'String');
            }
            if (data.hasOwnProperty('entity_id')) {
                obj['entity_id'] = ApiClient.convertToType(data['entity_id'], 'Number');
            }
            if (data.hasOwnProperty('extension_attributes')) {
                obj['extension_attributes'] = ApiClient.convertToType(data['extension_attributes'], Object);
            }
            if (data.hasOwnProperty('rma_entity_id')) {
                obj['rma_entity_id'] = ApiClient.convertToType(data['rma_entity_id'], 'Number');
            }
            if (data.hasOwnProperty('track_number')) {
                obj['track_number'] = ApiClient.convertToType(data['track_number'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>RmaDataTrackInterface</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>RmaDataTrackInterface</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of RmaDataTrackInterface.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['carrier_code'] && !(typeof data['carrier_code'] === 'string' || data['carrier_code'] instanceof String)) {
            throw new Error("Expected the field `carrier_code` to be a primitive type in the JSON string but got " + data['carrier_code']);
        }
        // ensure the json data is a string
        if (data['carrier_title'] && !(typeof data['carrier_title'] === 'string' || data['carrier_title'] instanceof String)) {
            throw new Error("Expected the field `carrier_title` to be a primitive type in the JSON string but got " + data['carrier_title']);
        }
        // ensure the json data is a string
        if (data['track_number'] && !(typeof data['track_number'] === 'string' || data['track_number'] instanceof String)) {
            throw new Error("Expected the field `track_number` to be a primitive type in the JSON string but got " + data['track_number']);
        }

        return true;
    }


}

RmaDataTrackInterface.RequiredProperties = ["carrier_code", "carrier_title", "entity_id", "rma_entity_id", "track_number"];

/**
 * Carrier code
 * @member {String} carrier_code
 */
RmaDataTrackInterface.prototype['carrier_code'] = undefined;

/**
 * Carrier title
 * @member {String} carrier_title
 */
RmaDataTrackInterface.prototype['carrier_title'] = undefined;

/**
 * Entity id
 * @member {Number} entity_id
 */
RmaDataTrackInterface.prototype['entity_id'] = undefined;

/**
 * ExtensionInterface class for @see \\Magento\\Rma\\Api\\Data\\TrackInterface
 * @member {Object} extension_attributes
 */
RmaDataTrackInterface.prototype['extension_attributes'] = undefined;

/**
 * Rma entity id
 * @member {Number} rma_entity_id
 */
RmaDataTrackInterface.prototype['rma_entity_id'] = undefined;

/**
 * Track number
 * @member {String} track_number
 */
RmaDataTrackInterface.prototype['track_number'] = undefined;






export default RmaDataTrackInterface;

