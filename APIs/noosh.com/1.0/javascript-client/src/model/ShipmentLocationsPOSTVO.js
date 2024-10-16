/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ShipmentLocationsPOSTVO model module.
 * @module model/ShipmentLocationsPOSTVO
 * @version 1.0
 */
class ShipmentLocationsPOSTVO {
    /**
     * Constructs a new <code>ShipmentLocationsPOSTVO</code>.
     * Java type: com.noosh.nooshapi.vo.ShipmentLocationsPOSTVO
     * @alias module:model/ShipmentLocationsPOSTVO
     */
    constructor() { 
        
        ShipmentLocationsPOSTVO.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ShipmentLocationsPOSTVO</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ShipmentLocationsPOSTVO} obj Optional instance to populate.
     * @return {module:model/ShipmentLocationsPOSTVO} The populated <code>ShipmentLocationsPOSTVO</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ShipmentLocationsPOSTVO();

            if (data.hasOwnProperty('location_id')) {
                obj['location_id'] = ApiClient.convertToType(data['location_id'], 'Number');
            }
            if (data.hasOwnProperty('shipment_id')) {
                obj['shipment_id'] = ApiClient.convertToType(data['shipment_id'], 'Number');
            }
            if (data.hasOwnProperty('spec_id')) {
                obj['spec_id'] = ApiClient.convertToType(data['spec_id'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ShipmentLocationsPOSTVO</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ShipmentLocationsPOSTVO</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * 
 * @member {Number} location_id
 */
ShipmentLocationsPOSTVO.prototype['location_id'] = undefined;

/**
 * 
 * @member {Number} shipment_id
 */
ShipmentLocationsPOSTVO.prototype['shipment_id'] = undefined;

/**
 * 
 * @member {Number} spec_id
 */
ShipmentLocationsPOSTVO.prototype['spec_id'] = undefined;






export default ShipmentLocationsPOSTVO;

