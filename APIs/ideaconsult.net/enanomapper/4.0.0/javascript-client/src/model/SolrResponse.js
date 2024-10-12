/**
 * eNanoMapper database
 * AMBIT REST web services [eNanoMapper profile] with free text & faceted search
 *
 * The version of the OpenAPI document: 4.0.0
 * Contact: support@ideaconsult.net
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';
import SolrResponseResponse from './SolrResponseResponse';
import SolrResponseResponseHeader from './SolrResponseResponseHeader';

/**
 * The SolrResponse model module.
 * @module model/SolrResponse
 * @version 4.0.0
 */
class SolrResponse {
    /**
     * Constructs a new <code>SolrResponse</code>.
     * @alias module:model/SolrResponse
     */
    constructor() { 
        
        SolrResponse.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SolrResponse</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SolrResponse} obj Optional instance to populate.
     * @return {module:model/SolrResponse} The populated <code>SolrResponse</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SolrResponse();

            if (data.hasOwnProperty('response')) {
                obj['response'] = SolrResponseResponse.constructFromObject(data['response']);
            }
            if (data.hasOwnProperty('responseHeader')) {
                obj['responseHeader'] = SolrResponseResponseHeader.constructFromObject(data['responseHeader']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SolrResponse</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SolrResponse</code>.
     */
    static validateJSON(data) {
        // validate the optional field `response`
        if (data['response']) { // data not null
          SolrResponseResponse.validateJSON(data['response']);
        }
        // validate the optional field `responseHeader`
        if (data['responseHeader']) { // data not null
          SolrResponseResponseHeader.validateJSON(data['responseHeader']);
        }

        return true;
    }


}



/**
 * @member {module:model/SolrResponseResponse} response
 */
SolrResponse.prototype['response'] = undefined;

/**
 * @member {module:model/SolrResponseResponseHeader} responseHeader
 */
SolrResponse.prototype['responseHeader'] = undefined;






export default SolrResponse;

