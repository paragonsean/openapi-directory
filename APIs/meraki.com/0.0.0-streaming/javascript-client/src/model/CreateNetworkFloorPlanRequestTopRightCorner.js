/**
 * Meraki Dashboard API
 * The Cisco Meraki Dashboard API is a modern REST API based on the OpenAPI specification.  > Date: 23 April, 2023 > > [Recent Updates](https://meraki.io/whats-new/)  ---  [API Documentation](https://meraki.io/api)  [Community Support](https://meraki.io/community)  [Meraki Homepage](https://www.meraki.com) 
 *
 * The version of the OpenAPI document: 0.0.0-streaming
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The CreateNetworkFloorPlanRequestTopRightCorner model module.
 * @module model/CreateNetworkFloorPlanRequestTopRightCorner
 * @version 0.0.0-streaming
 */
class CreateNetworkFloorPlanRequestTopRightCorner {
    /**
     * Constructs a new <code>CreateNetworkFloorPlanRequestTopRightCorner</code>.
     * The longitude and latitude of the top right corner of your floor plan.
     * @alias module:model/CreateNetworkFloorPlanRequestTopRightCorner
     */
    constructor() { 
        
        CreateNetworkFloorPlanRequestTopRightCorner.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>CreateNetworkFloorPlanRequestTopRightCorner</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CreateNetworkFloorPlanRequestTopRightCorner} obj Optional instance to populate.
     * @return {module:model/CreateNetworkFloorPlanRequestTopRightCorner} The populated <code>CreateNetworkFloorPlanRequestTopRightCorner</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CreateNetworkFloorPlanRequestTopRightCorner();

            if (data.hasOwnProperty('lat')) {
                obj['lat'] = ApiClient.convertToType(data['lat'], 'Number');
            }
            if (data.hasOwnProperty('lng')) {
                obj['lng'] = ApiClient.convertToType(data['lng'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CreateNetworkFloorPlanRequestTopRightCorner</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CreateNetworkFloorPlanRequestTopRightCorner</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Latitude
 * @member {Number} lat
 */
CreateNetworkFloorPlanRequestTopRightCorner.prototype['lat'] = undefined;

/**
 * Longitude
 * @member {Number} lng
 */
CreateNetworkFloorPlanRequestTopRightCorner.prototype['lng'] = undefined;






export default CreateNetworkFloorPlanRequestTopRightCorner;

