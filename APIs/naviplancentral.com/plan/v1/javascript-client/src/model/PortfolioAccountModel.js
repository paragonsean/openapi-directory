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
import IPortfolioAccount from './IPortfolioAccount';
import ObjectLink from './ObjectLink';

/**
 * The PortfolioAccountModel model module.
 * @module model/PortfolioAccountModel
 * @version v1
 */
class PortfolioAccountModel {
    /**
     * Constructs a new <code>PortfolioAccountModel</code>.
     * @alias module:model/PortfolioAccountModel
     */
    constructor() { 
        
        PortfolioAccountModel.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PortfolioAccountModel</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PortfolioAccountModel} obj Optional instance to populate.
     * @return {module:model/PortfolioAccountModel} The populated <code>PortfolioAccountModel</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PortfolioAccountModel();

            if (data.hasOwnProperty('links')) {
                obj['links'] = ApiClient.convertToType(data['links'], [ObjectLink]);
            }
            if (data.hasOwnProperty('portfolioAccount')) {
                obj['portfolioAccount'] = IPortfolioAccount.constructFromObject(data['portfolioAccount']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PortfolioAccountModel</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PortfolioAccountModel</code>.
     */
    static validateJSON(data) {
        if (data['links']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['links'])) {
                throw new Error("Expected the field `links` to be an array in the JSON data but got " + data['links']);
            }
            // validate the optional field `links` (array)
            for (const item of data['links']) {
                ObjectLink.validateJSON(item);
            };
        }
        // validate the optional field `portfolioAccount`
        if (data['portfolioAccount']) { // data not null
          IPortfolioAccount.validateJSON(data['portfolioAccount']);
        }

        return true;
    }


}



/**
 * @member {Array.<module:model/ObjectLink>} links
 */
PortfolioAccountModel.prototype['links'] = undefined;

/**
 * @member {module:model/IPortfolioAccount} portfolioAccount
 */
PortfolioAccountModel.prototype['portfolioAccount'] = undefined;






export default PortfolioAccountModel;

