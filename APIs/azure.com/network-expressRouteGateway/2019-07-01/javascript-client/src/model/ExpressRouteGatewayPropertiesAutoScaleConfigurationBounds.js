/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-07-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds model module.
 * @module model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds
 * @version 2019-07-01
 */
class ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds {
    /**
     * Constructs a new <code>ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds</code>.
     * Minimum and maximum number of scale units to deploy.
     * @alias module:model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds
     */
    constructor() { 
        
        ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds} obj Optional instance to populate.
     * @return {module:model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds} The populated <code>ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds();

            if (data.hasOwnProperty('max')) {
                obj['max'] = ApiClient.convertToType(data['max'], 'Number');
            }
            if (data.hasOwnProperty('min')) {
                obj['min'] = ApiClient.convertToType(data['min'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds</code>.
     */
    static validateJSON(data) {

        return true;
    }


}



/**
 * Maximum number of scale units deployed for ExpressRoute gateway.
 * @member {Number} max
 */
ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.prototype['max'] = undefined;

/**
 * Minimum number of scale units deployed for ExpressRoute gateway.
 * @member {Number} min
 */
ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.prototype['min'] = undefined;






export default ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds;

