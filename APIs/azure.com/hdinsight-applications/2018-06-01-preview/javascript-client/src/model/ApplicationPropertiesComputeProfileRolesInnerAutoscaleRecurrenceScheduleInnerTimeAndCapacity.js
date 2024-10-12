/**
 * HDInsightManagementClient
 * The HDInsight Management Client.
 *
 * The version of the OpenAPI document: 2018-06-01-preview
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity model module.
 * @module model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity
 * @version 2018-06-01-preview
 */
class ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity {
    /**
     * Constructs a new <code>ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity</code>.
     * Time and capacity request parameters
     * @alias module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity
     */
    constructor() { 
        
        ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity} obj Optional instance to populate.
     * @return {module:model/ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity} The populated <code>ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity();

            if (data.hasOwnProperty('maxInstanceCount')) {
                obj['maxInstanceCount'] = ApiClient.convertToType(data['maxInstanceCount'], 'Number');
            }
            if (data.hasOwnProperty('minInstanceCount')) {
                obj['minInstanceCount'] = ApiClient.convertToType(data['minInstanceCount'], 'Number');
            }
            if (data.hasOwnProperty('time')) {
                obj['time'] = ApiClient.convertToType(data['time'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['time'] && !(typeof data['time'] === 'string' || data['time'] instanceof String)) {
            throw new Error("Expected the field `time` to be a primitive type in the JSON string but got " + data['time']);
        }

        return true;
    }


}



/**
 * The maximum instance count of the cluster
 * @member {Number} maxInstanceCount
 */
ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity.prototype['maxInstanceCount'] = undefined;

/**
 * The minimum instance count of the cluster
 * @member {Number} minInstanceCount
 */
ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity.prototype['minInstanceCount'] = undefined;

/**
 * 24-hour time in the form xx:xx
 * @member {String} time
 */
ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity.prototype['time'] = undefined;






export default ApplicationPropertiesComputeProfileRolesInnerAutoscaleRecurrenceScheduleInnerTimeAndCapacity;

