/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import BillingAggregatedInformationGetByApp200Response from './BillingAggregatedInformationGetByApp200Response';

/**
 * The BillingAggregatedInformationGetAll200Response model module.
 * @module model/BillingAggregatedInformationGetAll200Response
 * @version v0.1
 */
class BillingAggregatedInformationGetAll200Response {
    /**
     * Constructs a new <code>BillingAggregatedInformationGetAll200Response</code>.
     * Aggregated Billing Information for a user an the organizations in which the user is an admin.
     * @alias module:model/BillingAggregatedInformationGetAll200Response
     */
    constructor() { 
        
        BillingAggregatedInformationGetAll200Response.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>BillingAggregatedInformationGetAll200Response</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/BillingAggregatedInformationGetAll200Response} obj Optional instance to populate.
     * @return {module:model/BillingAggregatedInformationGetAll200Response} The populated <code>BillingAggregatedInformationGetAll200Response</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new BillingAggregatedInformationGetAll200Response();

            if (data.hasOwnProperty('aggregatedBillings')) {
                obj['aggregatedBillings'] = BillingAggregatedInformationGetByApp200Response.constructFromObject(data['aggregatedBillings']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>BillingAggregatedInformationGetAll200Response</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>BillingAggregatedInformationGetAll200Response</code>.
     */
    static validateJSON(data) {
        // validate the optional field `aggregatedBillings`
        if (data['aggregatedBillings']) { // data not null
          BillingAggregatedInformationGetByApp200Response.validateJSON(data['aggregatedBillings']);
        }

        return true;
    }


}



/**
 * @member {module:model/BillingAggregatedInformationGetByApp200Response} aggregatedBillings
 */
BillingAggregatedInformationGetAll200Response.prototype['aggregatedBillings'] = undefined;






export default BillingAggregatedInformationGetAll200Response;

