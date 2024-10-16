/**
 * NaviPlan API
 * An API for accessing NaviPlan plan data for a client.
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
import FormattedEnumTypeDistributionDividendType from './FormattedEnumTypeDistributionDividendType';
import FormattedEnumTypePrivateCorporationShareType from './FormattedEnumTypePrivateCorporationShareType';
import IActivityData from './IActivityData';

/**
 * The IManualDividendDistribution model module.
 * @module model/IManualDividendDistribution
 * @version v1
 */
class IManualDividendDistribution {
    /**
     * Constructs a new <code>IManualDividendDistribution</code>.
     * @alias module:model/IManualDividendDistribution
     */
    constructor() { 
        
        IManualDividendDistribution.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>IManualDividendDistribution</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/IManualDividendDistribution} obj Optional instance to populate.
     * @return {module:model/IManualDividendDistribution} The populated <code>IManualDividendDistribution</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new IManualDividendDistribution();

            if (data.hasOwnProperty('activityData')) {
                obj['activityData'] = IActivityData.constructFromObject(data['activityData']);
            }
            if (data.hasOwnProperty('directCoClientAfterTaxProceedsTo')) {
                obj['directCoClientAfterTaxProceedsTo'] = ApiClient.convertToType(data['directCoClientAfterTaxProceedsTo'], 'String');
            }
            if (data.hasOwnProperty('dividendType')) {
                obj['dividendType'] = FormattedEnumTypeDistributionDividendType.constructFromObject(data['dividendType']);
            }
            if (data.hasOwnProperty('shareId')) {
                obj['shareId'] = ApiClient.convertToType(data['shareId'], 'Number');
            }
            if (data.hasOwnProperty('shareType')) {
                obj['shareType'] = FormattedEnumTypePrivateCorporationShareType.constructFromObject(data['shareType']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>IManualDividendDistribution</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>IManualDividendDistribution</code>.
     */
    static validateJSON(data) {
        // validate the optional field `activityData`
        if (data['activityData']) { // data not null
          IActivityData.validateJSON(data['activityData']);
        }
        // ensure the json data is a string
        if (data['directCoClientAfterTaxProceedsTo'] && !(typeof data['directCoClientAfterTaxProceedsTo'] === 'string' || data['directCoClientAfterTaxProceedsTo'] instanceof String)) {
            throw new Error("Expected the field `directCoClientAfterTaxProceedsTo` to be a primitive type in the JSON string but got " + data['directCoClientAfterTaxProceedsTo']);
        }
        // validate the optional field `dividendType`
        if (data['dividendType']) { // data not null
          FormattedEnumTypeDistributionDividendType.validateJSON(data['dividendType']);
        }
        // validate the optional field `shareType`
        if (data['shareType']) { // data not null
          FormattedEnumTypePrivateCorporationShareType.validateJSON(data['shareType']);
        }

        return true;
    }


}



/**
 * @member {module:model/IActivityData} activityData
 */
IManualDividendDistribution.prototype['activityData'] = undefined;

/**
 * @member {String} directCoClientAfterTaxProceedsTo
 */
IManualDividendDistribution.prototype['directCoClientAfterTaxProceedsTo'] = undefined;

/**
 * @member {module:model/FormattedEnumTypeDistributionDividendType} dividendType
 */
IManualDividendDistribution.prototype['dividendType'] = undefined;

/**
 * @member {Number} shareId
 */
IManualDividendDistribution.prototype['shareId'] = undefined;

/**
 * @member {module:model/FormattedEnumTypePrivateCorporationShareType} shareType
 */
IManualDividendDistribution.prototype['shareType'] = undefined;






export default IManualDividendDistribution;

