/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2018-12-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ExpressRouteGateway from './ExpressRouteGateway';

/**
 * The ExpressRouteGatewayList model module.
 * @module model/ExpressRouteGatewayList
 * @version 2018-12-01
 */
class ExpressRouteGatewayList {
    /**
     * Constructs a new <code>ExpressRouteGatewayList</code>.
     * List of ExpressRoute gateways.
     * @alias module:model/ExpressRouteGatewayList
     */
    constructor() { 
        
        ExpressRouteGatewayList.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ExpressRouteGatewayList</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExpressRouteGatewayList} obj Optional instance to populate.
     * @return {module:model/ExpressRouteGatewayList} The populated <code>ExpressRouteGatewayList</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExpressRouteGatewayList();

            if (data.hasOwnProperty('value')) {
                obj['value'] = ApiClient.convertToType(data['value'], [ExpressRouteGateway]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExpressRouteGatewayList</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExpressRouteGatewayList</code>.
     */
    static validateJSON(data) {
        if (data['value']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['value'])) {
                throw new Error("Expected the field `value` to be an array in the JSON data but got " + data['value']);
            }
            // validate the optional field `value` (array)
            for (const item of data['value']) {
                ExpressRouteGateway.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * List of ExpressRoute gateways.
 * @member {Array.<module:model/ExpressRouteGateway>} value
 */
ExpressRouteGatewayList.prototype['value'] = undefined;






export default ExpressRouteGatewayList;

