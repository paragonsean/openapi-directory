/**
 *  API Client
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
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
import DeploymentLocationsHostingEnvironmentsInner from './DeploymentLocationsHostingEnvironmentsInner';
import GeoRegion from './GeoRegion';
import HostingEnvironmentDeploymentInfo from './HostingEnvironmentDeploymentInfo';

/**
 * The DeploymentLocations model module.
 * @module model/DeploymentLocations
 * @version 2019-08-01
 */
class DeploymentLocations {
    /**
     * Constructs a new <code>DeploymentLocations</code>.
     * List of available locations (regions or App Service Environments) for deployment of App Service resources.
     * @alias module:model/DeploymentLocations
     */
    constructor() { 
        
        DeploymentLocations.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>DeploymentLocations</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/DeploymentLocations} obj Optional instance to populate.
     * @return {module:model/DeploymentLocations} The populated <code>DeploymentLocations</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new DeploymentLocations();

            if (data.hasOwnProperty('hostingEnvironmentDeploymentInfos')) {
                obj['hostingEnvironmentDeploymentInfos'] = ApiClient.convertToType(data['hostingEnvironmentDeploymentInfos'], [HostingEnvironmentDeploymentInfo]);
            }
            if (data.hasOwnProperty('hostingEnvironments')) {
                obj['hostingEnvironments'] = ApiClient.convertToType(data['hostingEnvironments'], [DeploymentLocationsHostingEnvironmentsInner]);
            }
            if (data.hasOwnProperty('locations')) {
                obj['locations'] = ApiClient.convertToType(data['locations'], [GeoRegion]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>DeploymentLocations</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>DeploymentLocations</code>.
     */
    static validateJSON(data) {
        if (data['hostingEnvironmentDeploymentInfos']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['hostingEnvironmentDeploymentInfos'])) {
                throw new Error("Expected the field `hostingEnvironmentDeploymentInfos` to be an array in the JSON data but got " + data['hostingEnvironmentDeploymentInfos']);
            }
            // validate the optional field `hostingEnvironmentDeploymentInfos` (array)
            for (const item of data['hostingEnvironmentDeploymentInfos']) {
                HostingEnvironmentDeploymentInfo.validateJSON(item);
            };
        }
        if (data['hostingEnvironments']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['hostingEnvironments'])) {
                throw new Error("Expected the field `hostingEnvironments` to be an array in the JSON data but got " + data['hostingEnvironments']);
            }
            // validate the optional field `hostingEnvironments` (array)
            for (const item of data['hostingEnvironments']) {
                DeploymentLocationsHostingEnvironmentsInner.validateJSON(item);
            };
        }
        if (data['locations']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['locations'])) {
                throw new Error("Expected the field `locations` to be an array in the JSON data but got " + data['locations']);
            }
            // validate the optional field `locations` (array)
            for (const item of data['locations']) {
                GeoRegion.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Available App Service Environments with basic information.
 * @member {Array.<module:model/HostingEnvironmentDeploymentInfo>} hostingEnvironmentDeploymentInfos
 */
DeploymentLocations.prototype['hostingEnvironmentDeploymentInfos'] = undefined;

/**
 * Available App Service Environments with full descriptions of the environments.
 * @member {Array.<module:model/DeploymentLocationsHostingEnvironmentsInner>} hostingEnvironments
 */
DeploymentLocations.prototype['hostingEnvironments'] = undefined;

/**
 * Available regions.
 * @member {Array.<module:model/GeoRegion>} locations
 */
DeploymentLocations.prototype['locations'] = undefined;






export default DeploymentLocations;

