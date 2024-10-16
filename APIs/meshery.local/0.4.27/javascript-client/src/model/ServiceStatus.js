/**
 * Meshery API.
 * the purpose of this application is to provide an application that is using plain go code to define an API  This should demonstrate all the possible comment annotations that are available to turn go code into a fully compliant swagger 2.0 spec
 *
 * The version of the OpenAPI document: 0.4.27
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import LoadBalancerStatus from './LoadBalancerStatus';

/**
 * The ServiceStatus model module.
 * @module model/ServiceStatus
 * @version 0.4.27
 */
class ServiceStatus {
    /**
     * Constructs a new <code>ServiceStatus</code>.
     * @alias module:model/ServiceStatus
     */
    constructor() { 
        
        ServiceStatus.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ServiceStatus</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ServiceStatus} obj Optional instance to populate.
     * @return {module:model/ServiceStatus} The populated <code>ServiceStatus</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ServiceStatus();

            if (data.hasOwnProperty('loadBalancer')) {
                obj['loadBalancer'] = LoadBalancerStatus.constructFromObject(data['loadBalancer']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ServiceStatus</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ServiceStatus</code>.
     */
    static validateJSON(data) {
        // validate the optional field `loadBalancer`
        if (data['loadBalancer']) { // data not null
          LoadBalancerStatus.validateJSON(data['loadBalancer']);
        }

        return true;
    }


}



/**
 * @member {module:model/LoadBalancerStatus} loadBalancer
 */
ServiceStatus.prototype['loadBalancer'] = undefined;






export default ServiceStatus;

