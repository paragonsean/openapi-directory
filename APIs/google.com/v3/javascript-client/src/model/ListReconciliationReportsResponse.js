/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import ReconciliationReport from './ReconciliationReport';

/**
 * The ListReconciliationReportsResponse model module.
 * @module model/ListReconciliationReportsResponse
 * @version v3
 */
class ListReconciliationReportsResponse {
    /**
     * Constructs a new <code>ListReconciliationReportsResponse</code>.
     * Response message for ReconciliationReportService.ListReconciliationReports.
     * @alias module:model/ListReconciliationReportsResponse
     */
    constructor() { 
        
        ListReconciliationReportsResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ListReconciliationReportsResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ListReconciliationReportsResponse} obj Optional instance to populate.
     * @return {module:model/ListReconciliationReportsResponse} The populated <code>ListReconciliationReportsResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ListReconciliationReportsResponse();

            if (data.hasOwnProperty('reconciliationReports')) {
                obj['reconciliationReports'] = ApiClient.convertToType(data['reconciliationReports'], [ReconciliationReport]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ListReconciliationReportsResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ListReconciliationReportsResponse</code>.
     */
    static validateJSON(data) {
        if (data['reconciliationReports']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['reconciliationReports'])) {
                throw new Error("Expected the field `reconciliationReports` to be an array in the JSON data but got " + data['reconciliationReports']);
            }
            // validate the optional field `reconciliationReports` (array)
            for (const item of data['reconciliationReports']) {
                ReconciliationReport.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * The list of names of reconciliation reports. Note that the `contents` and `fileName` fields of each `ReconciliationReport` object are not returned by this call.
 * @member {Array.<module:model/ReconciliationReport>} reconciliationReports
 */
ListReconciliationReportsResponse.prototype['reconciliationReports'] = undefined;






export default ListReconciliationReportsResponse;

