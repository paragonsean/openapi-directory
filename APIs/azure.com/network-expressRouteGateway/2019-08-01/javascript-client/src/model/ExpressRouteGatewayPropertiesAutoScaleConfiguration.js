/**
 * NetworkManagementClient
 * The Microsoft Azure Network management API provides a RESTful set of web services that interact with Microsoft Azure Networks service to manage your network resources. The API has entities that capture the relationship between an end user and the Microsoft Azure Networks service.
 *
 * The version of the OpenAPI document: 2019-08-01
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds from './ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds';

/**
 * The ExpressRouteGatewayPropertiesAutoScaleConfiguration model module.
 * @module model/ExpressRouteGatewayPropertiesAutoScaleConfiguration
 * @version 2019-08-01
 */
class ExpressRouteGatewayPropertiesAutoScaleConfiguration {
    /**
     * Constructs a new <code>ExpressRouteGatewayPropertiesAutoScaleConfiguration</code>.
     * Configuration for auto scaling.
     * @alias module:model/ExpressRouteGatewayPropertiesAutoScaleConfiguration
     */
    constructor() { 
        
        ExpressRouteGatewayPropertiesAutoScaleConfiguration.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ExpressRouteGatewayPropertiesAutoScaleConfiguration</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ExpressRouteGatewayPropertiesAutoScaleConfiguration} obj Optional instance to populate.
     * @return {module:model/ExpressRouteGatewayPropertiesAutoScaleConfiguration} The populated <code>ExpressRouteGatewayPropertiesAutoScaleConfiguration</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ExpressRouteGatewayPropertiesAutoScaleConfiguration();

            if (data.hasOwnProperty('bounds')) {
                obj['bounds'] = ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.constructFromObject(data['bounds']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ExpressRouteGatewayPropertiesAutoScaleConfiguration</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ExpressRouteGatewayPropertiesAutoScaleConfiguration</code>.
     */
    static validateJSON(data) {
        // validate the optional field `bounds`
        if (data['bounds']) { // data not null
          ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds.validateJSON(data['bounds']);
        }

        return true;
    }


}



/**
 * @member {module:model/ExpressRouteGatewayPropertiesAutoScaleConfigurationBounds} bounds
 */
ExpressRouteGatewayPropertiesAutoScaleConfiguration.prototype['bounds'] = undefined;






export default ExpressRouteGatewayPropertiesAutoScaleConfiguration;

