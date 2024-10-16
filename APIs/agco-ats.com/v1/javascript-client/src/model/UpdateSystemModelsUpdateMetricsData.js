/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord from './UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord';
import UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord from './UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord';
import UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord from './UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord';

/**
 * The UpdateSystemModelsUpdateMetricsData model module.
 * @module model/UpdateSystemModelsUpdateMetricsData
 * @version v1
 */
class UpdateSystemModelsUpdateMetricsData {
    /**
     * Constructs a new <code>UpdateSystemModelsUpdateMetricsData</code>.
     * Model that retrieves the data for UpdateMetrics
     * @alias module:model/UpdateSystemModelsUpdateMetricsData
     */
    constructor() { 
        
        UpdateSystemModelsUpdateMetricsData.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>UpdateSystemModelsUpdateMetricsData</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/UpdateSystemModelsUpdateMetricsData} obj Optional instance to populate.
     * @return {module:model/UpdateSystemModelsUpdateMetricsData} The populated <code>UpdateSystemModelsUpdateMetricsData</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new UpdateSystemModelsUpdateMetricsData();

            if (data.hasOwnProperty('ActiveVersion')) {
                obj['ActiveVersion'] = ApiClient.convertToType(data['ActiveVersion'], 'String');
            }
            if (data.hasOwnProperty('ActiveVersionByClient')) {
                obj['ActiveVersionByClient'] = ApiClient.convertToType(data['ActiveVersionByClient'], [UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord]);
            }
            if (data.hasOwnProperty('CurrentStateByClient')) {
                obj['CurrentStateByClient'] = ApiClient.convertToType(data['CurrentStateByClient'], [UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord]);
            }
            if (data.hasOwnProperty('CutOffDate')) {
                obj['CutOffDate'] = ApiClient.convertToType(data['CutOffDate'], 'Date');
            }
            if (data.hasOwnProperty('DataRefreshed')) {
                obj['DataRefreshed'] = ApiClient.convertToType(data['DataRefreshed'], 'Date');
            }
            if (data.hasOwnProperty('FilteredClientCount')) {
                obj['FilteredClientCount'] = ApiClient.convertToType(data['FilteredClientCount'], 'Number');
            }
            if (data.hasOwnProperty('PackageErrors')) {
                obj['PackageErrors'] = ApiClient.convertToType(data['PackageErrors'], [UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord]);
            }
            if (data.hasOwnProperty('TotalClientCount')) {
                obj['TotalClientCount'] = ApiClient.convertToType(data['TotalClientCount'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>UpdateSystemModelsUpdateMetricsData</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>UpdateSystemModelsUpdateMetricsData</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ActiveVersion'] && !(typeof data['ActiveVersion'] === 'string' || data['ActiveVersion'] instanceof String)) {
            throw new Error("Expected the field `ActiveVersion` to be a primitive type in the JSON string but got " + data['ActiveVersion']);
        }
        if (data['ActiveVersionByClient']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['ActiveVersionByClient'])) {
                throw new Error("Expected the field `ActiveVersionByClient` to be an array in the JSON data but got " + data['ActiveVersionByClient']);
            }
            // validate the optional field `ActiveVersionByClient` (array)
            for (const item of data['ActiveVersionByClient']) {
                UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord.validateJSON(item);
            };
        }
        if (data['CurrentStateByClient']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['CurrentStateByClient'])) {
                throw new Error("Expected the field `CurrentStateByClient` to be an array in the JSON data but got " + data['CurrentStateByClient']);
            }
            // validate the optional field `CurrentStateByClient` (array)
            for (const item of data['CurrentStateByClient']) {
                UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord.validateJSON(item);
            };
        }
        if (data['PackageErrors']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['PackageErrors'])) {
                throw new Error("Expected the field `PackageErrors` to be an array in the JSON data but got " + data['PackageErrors']);
            }
            // validate the optional field `PackageErrors` (array)
            for (const item of data['PackageErrors']) {
                UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * Active version (bundle number) of update type.
 * @member {String} ActiveVersion
 */
UpdateSystemModelsUpdateMetricsData.prototype['ActiveVersion'] = undefined;

/**
 * Generic collection that is of type ActiveVersionByClientRecord
 * @member {Array.<module:model/UpdateSystemModelsUpdateMetricsDataActiveVersionByClientRecord>} ActiveVersionByClient
 */
UpdateSystemModelsUpdateMetricsData.prototype['ActiveVersionByClient'] = undefined;

/**
 * Generic collection that is of type CurrentStateByClientRecord
 * @member {Array.<module:model/UpdateSystemModelsUpdateMetricsDataCurrentStateByClientRecord>} CurrentStateByClient
 */
UpdateSystemModelsUpdateMetricsData.prototype['CurrentStateByClient'] = undefined;

/**
 * Date that has been configured to only show the most recent clients with a cut off date. (Ex. year from current date)
 * @member {Date} CutOffDate
 */
UpdateSystemModelsUpdateMetricsData.prototype['CutOffDate'] = undefined;

/**
 * Data was refreshed at this time.
 * @member {Date} DataRefreshed
 */
UpdateSystemModelsUpdateMetricsData.prototype['DataRefreshed'] = undefined;

/**
 * Sum of clients represented              Filtered by updateType and lastCheckedInDate
 * @member {Number} FilteredClientCount
 */
UpdateSystemModelsUpdateMetricsData.prototype['FilteredClientCount'] = undefined;

/**
 * Generic collection that is of type PackageErrorsRecord
 * @member {Array.<module:model/UpdateSystemModelsUpdateMetricsDataPackageErrorsRecord>} PackageErrors
 */
UpdateSystemModelsUpdateMetricsData.prototype['PackageErrors'] = undefined;

/**
 * Total clients we have ever serviced
 * @member {Number} TotalClientCount
 */
UpdateSystemModelsUpdateMetricsData.prototype['TotalClientCount'] = undefined;






export default UpdateSystemModelsUpdateMetricsData;

