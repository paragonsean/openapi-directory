/**
 * LetMC Api V3, reporting
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v3-reporting
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The ReportingReceivershipLitigationModel model module.
 * @module model/ReportingReceivershipLitigationModel
 * @version v3-reporting
 */
class ReportingReceivershipLitigationModel {
    /**
     * Constructs a new <code>ReportingReceivershipLitigationModel</code>.
     * Helper Model - Litigation
     * @alias module:model/ReportingReceivershipLitigationModel
     */
    constructor() { 
        
        ReportingReceivershipLitigationModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>ReportingReceivershipLitigationModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ReportingReceivershipLitigationModel} obj Optional instance to populate.
     * @return {module:model/ReportingReceivershipLitigationModel} The populated <code>ReportingReceivershipLitigationModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ReportingReceivershipLitigationModel();

            if (data.hasOwnProperty('ClosedLitigationDate')) {
                obj['ClosedLitigationDate'] = ApiClient.convertToType(data['ClosedLitigationDate'], 'Date');
            }
            if (data.hasOwnProperty('ClosedLitigationReason')) {
                obj['ClosedLitigationReason'] = ApiClient.convertToType(data['ClosedLitigationReason'], 'String');
            }
            if (data.hasOwnProperty('CompiledBySolicitorID')) {
                obj['CompiledBySolicitorID'] = ApiClient.convertToType(data['CompiledBySolicitorID'], 'String');
            }
            if (data.hasOwnProperty('DisplayCompiledBySolicitor')) {
                obj['DisplayCompiledBySolicitor'] = ApiClient.convertToType(data['DisplayCompiledBySolicitor'], 'String');
            }
            if (data.hasOwnProperty('EvictionDate')) {
                obj['EvictionDate'] = ApiClient.convertToType(data['EvictionDate'], 'Date');
            }
            if (data.hasOwnProperty('EvictionOutcome')) {
                obj['EvictionOutcome'] = ApiClient.convertToType(data['EvictionOutcome'], 'String');
            }
            if (data.hasOwnProperty('ExtraNotes')) {
                obj['ExtraNotes'] = ApiClient.convertToType(data['ExtraNotes'], 'String');
            }
            if (data.hasOwnProperty('HearingDate')) {
                obj['HearingDate'] = ApiClient.convertToType(data['HearingDate'], 'Date');
            }
            if (data.hasOwnProperty('HearingOutcome')) {
                obj['HearingOutcome'] = ApiClient.convertToType(data['HearingOutcome'], 'String');
            }
            if (data.hasOwnProperty('LitigationType')) {
                obj['LitigationType'] = ApiClient.convertToType(data['LitigationType'], 'String');
            }
            if (data.hasOwnProperty('NoticeExpiryDate')) {
                obj['NoticeExpiryDate'] = ApiClient.convertToType(data['NoticeExpiryDate'], 'Date');
            }
            if (data.hasOwnProperty('NoticeServedDate')) {
                obj['NoticeServedDate'] = ApiClient.convertToType(data['NoticeServedDate'], 'Date');
            }
            if (data.hasOwnProperty('ProceedingsIssuedDate')) {
                obj['ProceedingsIssuedDate'] = ApiClient.convertToType(data['ProceedingsIssuedDate'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ReportingReceivershipLitigationModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ReportingReceivershipLitigationModel</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['ClosedLitigationReason'] && !(typeof data['ClosedLitigationReason'] === 'string' || data['ClosedLitigationReason'] instanceof String)) {
            throw new Error("Expected the field `ClosedLitigationReason` to be a primitive type in the JSON string but got " + data['ClosedLitigationReason']);
        }
        // ensure the json data is a string
        if (data['CompiledBySolicitorID'] && !(typeof data['CompiledBySolicitorID'] === 'string' || data['CompiledBySolicitorID'] instanceof String)) {
            throw new Error("Expected the field `CompiledBySolicitorID` to be a primitive type in the JSON string but got " + data['CompiledBySolicitorID']);
        }
        // ensure the json data is a string
        if (data['DisplayCompiledBySolicitor'] && !(typeof data['DisplayCompiledBySolicitor'] === 'string' || data['DisplayCompiledBySolicitor'] instanceof String)) {
            throw new Error("Expected the field `DisplayCompiledBySolicitor` to be a primitive type in the JSON string but got " + data['DisplayCompiledBySolicitor']);
        }
        // ensure the json data is a string
        if (data['EvictionOutcome'] && !(typeof data['EvictionOutcome'] === 'string' || data['EvictionOutcome'] instanceof String)) {
            throw new Error("Expected the field `EvictionOutcome` to be a primitive type in the JSON string but got " + data['EvictionOutcome']);
        }
        // ensure the json data is a string
        if (data['ExtraNotes'] && !(typeof data['ExtraNotes'] === 'string' || data['ExtraNotes'] instanceof String)) {
            throw new Error("Expected the field `ExtraNotes` to be a primitive type in the JSON string but got " + data['ExtraNotes']);
        }
        // ensure the json data is a string
        if (data['HearingOutcome'] && !(typeof data['HearingOutcome'] === 'string' || data['HearingOutcome'] instanceof String)) {
            throw new Error("Expected the field `HearingOutcome` to be a primitive type in the JSON string but got " + data['HearingOutcome']);
        }
        // ensure the json data is a string
        if (data['LitigationType'] && !(typeof data['LitigationType'] === 'string' || data['LitigationType'] instanceof String)) {
            throw new Error("Expected the field `LitigationType` to be a primitive type in the JSON string but got " + data['LitigationType']);
        }

        return true;
    }


}



/**
 * Closed Litigation Date
 * @member {Date} ClosedLitigationDate
 */
ReportingReceivershipLitigationModel.prototype['ClosedLitigationDate'] = undefined;

/**
 * Closed Litigation Reason
 * @member {module:model/ReportingReceivershipLitigationModel.ClosedLitigationReasonEnum} ClosedLitigationReason
 */
ReportingReceivershipLitigationModel.prototype['ClosedLitigationReason'] = undefined;

/**
 * Compiled By Solicitor ID (SalesSolicitor)
 * @member {String} CompiledBySolicitorID
 */
ReportingReceivershipLitigationModel.prototype['CompiledBySolicitorID'] = undefined;

/**
 * Display Compiled By Solicitor
 * @member {String} DisplayCompiledBySolicitor
 */
ReportingReceivershipLitigationModel.prototype['DisplayCompiledBySolicitor'] = undefined;

/**
 * Eviction Date
 * @member {Date} EvictionDate
 */
ReportingReceivershipLitigationModel.prototype['EvictionDate'] = undefined;

/**
 * Eviction Outcome
 * @member {module:model/ReportingReceivershipLitigationModel.EvictionOutcomeEnum} EvictionOutcome
 */
ReportingReceivershipLitigationModel.prototype['EvictionOutcome'] = undefined;

/**
 * Extra Notes
 * @member {String} ExtraNotes
 */
ReportingReceivershipLitigationModel.prototype['ExtraNotes'] = undefined;

/**
 * Hearing Date
 * @member {Date} HearingDate
 */
ReportingReceivershipLitigationModel.prototype['HearingDate'] = undefined;

/**
 * Hearing Outcome
 * @member {String} HearingOutcome
 */
ReportingReceivershipLitigationModel.prototype['HearingOutcome'] = undefined;

/**
 * Litigation Type
 * @member {String} LitigationType
 */
ReportingReceivershipLitigationModel.prototype['LitigationType'] = undefined;

/**
 * Notice Expiry Date
 * @member {Date} NoticeExpiryDate
 */
ReportingReceivershipLitigationModel.prototype['NoticeExpiryDate'] = undefined;

/**
 * Notice Served Date
 * @member {Date} NoticeServedDate
 */
ReportingReceivershipLitigationModel.prototype['NoticeServedDate'] = undefined;

/**
 * Proceedings Issued Date
 * @member {Date} ProceedingsIssuedDate
 */
ReportingReceivershipLitigationModel.prototype['ProceedingsIssuedDate'] = undefined;





/**
 * Allowed values for the <code>ClosedLitigationReason</code> property.
 * @enum {String}
 * @readonly
 */
ReportingReceivershipLitigationModel['ClosedLitigationReasonEnum'] = {

    /**
     * value: "PossessionObtained"
     * @const
     */
    "PossessionObtained": "PossessionObtained",

    /**
     * value: "TenantVacated"
     * @const
     */
    "TenantVacated": "TenantVacated",

    /**
     * value: "LitigationCancelled"
     * @const
     */
    "LitigationCancelled": "LitigationCancelled",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other"
};


/**
 * Allowed values for the <code>EvictionOutcome</code> property.
 * @enum {String}
 * @readonly
 */
ReportingReceivershipLitigationModel['EvictionOutcomeEnum'] = {

    /**
     * value: "EvictionComplete"
     * @const
     */
    "EvictionComplete": "EvictionComplete",

    /**
     * value: "EvictionCancelled"
     * @const
     */
    "EvictionCancelled": "EvictionCancelled",

    /**
     * value: "Other"
     * @const
     */
    "Other": "Other"
};



export default ReportingReceivershipLitigationModel;

