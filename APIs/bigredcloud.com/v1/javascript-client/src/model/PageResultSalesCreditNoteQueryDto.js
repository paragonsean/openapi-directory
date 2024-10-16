/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
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
import SalesCreditNoteQueryDto from './SalesCreditNoteQueryDto';

/**
 * The PageResultSalesCreditNoteQueryDto model module.
 * @module model/PageResultSalesCreditNoteQueryDto
 * @version v1
 */
class PageResultSalesCreditNoteQueryDto {
    /**
     * Constructs a new <code>PageResultSalesCreditNoteQueryDto</code>.
     * @alias module:model/PageResultSalesCreditNoteQueryDto
     */
    constructor() { 
        
        PageResultSalesCreditNoteQueryDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>PageResultSalesCreditNoteQueryDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/PageResultSalesCreditNoteQueryDto} obj Optional instance to populate.
     * @return {module:model/PageResultSalesCreditNoteQueryDto} The populated <code>PageResultSalesCreditNoteQueryDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new PageResultSalesCreditNoteQueryDto();

            if (data.hasOwnProperty('Count')) {
                obj['Count'] = ApiClient.convertToType(data['Count'], 'Number');
            }
            if (data.hasOwnProperty('Items')) {
                obj['Items'] = ApiClient.convertToType(data['Items'], [SalesCreditNoteQueryDto]);
            }
            if (data.hasOwnProperty('NextPageLink')) {
                obj['NextPageLink'] = ApiClient.convertToType(data['NextPageLink'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>PageResultSalesCreditNoteQueryDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>PageResultSalesCreditNoteQueryDto</code>.
     */
    static validateJSON(data) {
        if (data['Items']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['Items'])) {
                throw new Error("Expected the field `Items` to be an array in the JSON data but got " + data['Items']);
            }
            // validate the optional field `Items` (array)
            for (const item of data['Items']) {
                SalesCreditNoteQueryDto.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['NextPageLink'] && !(typeof data['NextPageLink'] === 'string' || data['NextPageLink'] instanceof String)) {
            throw new Error("Expected the field `NextPageLink` to be a primitive type in the JSON string but got " + data['NextPageLink']);
        }

        return true;
    }


}



/**
 * @member {Number} Count
 */
PageResultSalesCreditNoteQueryDto.prototype['Count'] = undefined;

/**
 * @member {Array.<module:model/SalesCreditNoteQueryDto>} Items
 */
PageResultSalesCreditNoteQueryDto.prototype['Items'] = undefined;

/**
 * @member {String} NextPageLink
 */
PageResultSalesCreditNoteQueryDto.prototype['NextPageLink'] = undefined;






export default PageResultSalesCreditNoteQueryDto;

