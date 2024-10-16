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
import AcudfValueDto from './AcudfValueDto';
import ProductTranQueryDto from './ProductTranQueryDto';

/**
 * The SalesCreditNoteQueryDto model module.
 * @module model/SalesCreditNoteQueryDto
 * @version v1
 */
class SalesCreditNoteQueryDto {
    /**
     * Constructs a new <code>SalesCreditNoteQueryDto</code>.
     * @alias module:model/SalesCreditNoteQueryDto
     */
    constructor() { 
        
        SalesCreditNoteQueryDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>SalesCreditNoteQueryDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SalesCreditNoteQueryDto} obj Optional instance to populate.
     * @return {module:model/SalesCreditNoteQueryDto} The populated <code>SalesCreditNoteQueryDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SalesCreditNoteQueryDto();

            if (data.hasOwnProperty('acCode')) {
                obj['acCode'] = ApiClient.convertToType(data['acCode'], 'String');
            }
            if (data.hasOwnProperty('bookTranTypeId')) {
                obj['bookTranTypeId'] = ApiClient.convertToType(data['bookTranTypeId'], 'Number');
            }
            if (data.hasOwnProperty('customFields')) {
                obj['customFields'] = ApiClient.convertToType(data['customFields'], [AcudfValueDto]);
            }
            if (data.hasOwnProperty('customerId')) {
                obj['customerId'] = ApiClient.convertToType(data['customerId'], 'Number');
            }
            if (data.hasOwnProperty('deliveryTo')) {
                obj['deliveryTo'] = ApiClient.convertToType(data['deliveryTo'], ['String']);
            }
            if (data.hasOwnProperty('details')) {
                obj['details'] = ApiClient.convertToType(data['details'], 'String');
            }
            if (data.hasOwnProperty('entryDate')) {
                obj['entryDate'] = ApiClient.convertToType(data['entryDate'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('loType')) {
                obj['loType'] = ApiClient.convertToType(data['loType'], 'String');
            }
            if (data.hasOwnProperty('netGoods')) {
                obj['netGoods'] = ApiClient.convertToType(data['netGoods'], 'Number');
            }
            if (data.hasOwnProperty('netServices')) {
                obj['netServices'] = ApiClient.convertToType(data['netServices'], 'Number');
            }
            if (data.hasOwnProperty('note')) {
                obj['note'] = ApiClient.convertToType(data['note'], 'String');
            }
            if (data.hasOwnProperty('ourReference')) {
                obj['ourReference'] = ApiClient.convertToType(data['ourReference'], 'String');
            }
            if (data.hasOwnProperty('procDate')) {
                obj['procDate'] = ApiClient.convertToType(data['procDate'], 'Date');
            }
            if (data.hasOwnProperty('productTrans')) {
                obj['productTrans'] = ApiClient.convertToType(data['productTrans'], [ProductTranQueryDto]);
            }
            if (data.hasOwnProperty('quoteId')) {
                obj['quoteId'] = ApiClient.convertToType(data['quoteId'], 'Number');
            }
            if (data.hasOwnProperty('reference')) {
                obj['reference'] = ApiClient.convertToType(data['reference'], 'String');
            }
            if (data.hasOwnProperty('saleRepCode')) {
                obj['saleRepCode'] = ApiClient.convertToType(data['saleRepCode'], 'String');
            }
            if (data.hasOwnProperty('saleRepId')) {
                obj['saleRepId'] = ApiClient.convertToType(data['saleRepId'], 'Number');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Blob');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('totalNet')) {
                obj['totalNet'] = ApiClient.convertToType(data['totalNet'], 'Number');
            }
            if (data.hasOwnProperty('totalVAT')) {
                obj['totalVAT'] = ApiClient.convertToType(data['totalVAT'], 'Number');
            }
            if (data.hasOwnProperty('unpaid')) {
                obj['unpaid'] = ApiClient.convertToType(data['unpaid'], 'Number');
            }
            if (data.hasOwnProperty('vatTypeId')) {
                obj['vatTypeId'] = ApiClient.convertToType(data['vatTypeId'], 'Number');
            }
            if (data.hasOwnProperty('yourReference')) {
                obj['yourReference'] = ApiClient.convertToType(data['yourReference'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SalesCreditNoteQueryDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SalesCreditNoteQueryDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['acCode'] && !(typeof data['acCode'] === 'string' || data['acCode'] instanceof String)) {
            throw new Error("Expected the field `acCode` to be a primitive type in the JSON string but got " + data['acCode']);
        }
        if (data['customFields']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['customFields'])) {
                throw new Error("Expected the field `customFields` to be an array in the JSON data but got " + data['customFields']);
            }
            // validate the optional field `customFields` (array)
            for (const item of data['customFields']) {
                AcudfValueDto.validateJSON(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['deliveryTo'])) {
            throw new Error("Expected the field `deliveryTo` to be an array in the JSON data but got " + data['deliveryTo']);
        }
        // ensure the json data is a string
        if (data['details'] && !(typeof data['details'] === 'string' || data['details'] instanceof String)) {
            throw new Error("Expected the field `details` to be a primitive type in the JSON string but got " + data['details']);
        }
        // ensure the json data is a string
        if (data['loType'] && !(typeof data['loType'] === 'string' || data['loType'] instanceof String)) {
            throw new Error("Expected the field `loType` to be a primitive type in the JSON string but got " + data['loType']);
        }
        // ensure the json data is a string
        if (data['note'] && !(typeof data['note'] === 'string' || data['note'] instanceof String)) {
            throw new Error("Expected the field `note` to be a primitive type in the JSON string but got " + data['note']);
        }
        // ensure the json data is a string
        if (data['ourReference'] && !(typeof data['ourReference'] === 'string' || data['ourReference'] instanceof String)) {
            throw new Error("Expected the field `ourReference` to be a primitive type in the JSON string but got " + data['ourReference']);
        }
        if (data['productTrans']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['productTrans'])) {
                throw new Error("Expected the field `productTrans` to be an array in the JSON data but got " + data['productTrans']);
            }
            // validate the optional field `productTrans` (array)
            for (const item of data['productTrans']) {
                ProductTranQueryDto.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['reference'] && !(typeof data['reference'] === 'string' || data['reference'] instanceof String)) {
            throw new Error("Expected the field `reference` to be a primitive type in the JSON string but got " + data['reference']);
        }
        // ensure the json data is a string
        if (data['saleRepCode'] && !(typeof data['saleRepCode'] === 'string' || data['saleRepCode'] instanceof String)) {
            throw new Error("Expected the field `saleRepCode` to be a primitive type in the JSON string but got " + data['saleRepCode']);
        }
        // ensure the json data is a string
        if (data['yourReference'] && !(typeof data['yourReference'] === 'string' || data['yourReference'] instanceof String)) {
            throw new Error("Expected the field `yourReference` to be a primitive type in the JSON string but got " + data['yourReference']);
        }

        return true;
    }


}



/**
 * @member {String} acCode
 */
SalesCreditNoteQueryDto.prototype['acCode'] = undefined;

/**
 * @member {Number} bookTranTypeId
 */
SalesCreditNoteQueryDto.prototype['bookTranTypeId'] = undefined;

/**
 * @member {Array.<module:model/AcudfValueDto>} customFields
 */
SalesCreditNoteQueryDto.prototype['customFields'] = undefined;

/**
 * @member {Number} customerId
 */
SalesCreditNoteQueryDto.prototype['customerId'] = undefined;

/**
 * @member {Array.<String>} deliveryTo
 */
SalesCreditNoteQueryDto.prototype['deliveryTo'] = undefined;

/**
 * @member {String} details
 */
SalesCreditNoteQueryDto.prototype['details'] = undefined;

/**
 * @member {Date} entryDate
 */
SalesCreditNoteQueryDto.prototype['entryDate'] = undefined;

/**
 * @member {Number} id
 */
SalesCreditNoteQueryDto.prototype['id'] = undefined;

/**
 * @member {String} loType
 */
SalesCreditNoteQueryDto.prototype['loType'] = undefined;

/**
 * @member {Number} netGoods
 */
SalesCreditNoteQueryDto.prototype['netGoods'] = undefined;

/**
 * @member {Number} netServices
 */
SalesCreditNoteQueryDto.prototype['netServices'] = undefined;

/**
 * @member {String} note
 */
SalesCreditNoteQueryDto.prototype['note'] = undefined;

/**
 * @member {String} ourReference
 */
SalesCreditNoteQueryDto.prototype['ourReference'] = undefined;

/**
 * @member {Date} procDate
 */
SalesCreditNoteQueryDto.prototype['procDate'] = undefined;

/**
 * @member {Array.<module:model/ProductTranQueryDto>} productTrans
 */
SalesCreditNoteQueryDto.prototype['productTrans'] = undefined;

/**
 * @member {Number} quoteId
 */
SalesCreditNoteQueryDto.prototype['quoteId'] = undefined;

/**
 * @member {String} reference
 */
SalesCreditNoteQueryDto.prototype['reference'] = undefined;

/**
 * @member {String} saleRepCode
 */
SalesCreditNoteQueryDto.prototype['saleRepCode'] = undefined;

/**
 * @member {Number} saleRepId
 */
SalesCreditNoteQueryDto.prototype['saleRepId'] = undefined;

/**
 * @member {Blob} timestamp
 */
SalesCreditNoteQueryDto.prototype['timestamp'] = undefined;

/**
 * @member {Number} total
 */
SalesCreditNoteQueryDto.prototype['total'] = undefined;

/**
 * @member {Number} totalNet
 */
SalesCreditNoteQueryDto.prototype['totalNet'] = undefined;

/**
 * @member {Number} totalVAT
 */
SalesCreditNoteQueryDto.prototype['totalVAT'] = undefined;

/**
 * @member {Number} unpaid
 */
SalesCreditNoteQueryDto.prototype['unpaid'] = undefined;

/**
 * @member {Number} vatTypeId
 */
SalesCreditNoteQueryDto.prototype['vatTypeId'] = undefined;

/**
 * @member {String} yourReference
 */
SalesCreditNoteQueryDto.prototype['yourReference'] = undefined;






export default SalesCreditNoteQueryDto;

