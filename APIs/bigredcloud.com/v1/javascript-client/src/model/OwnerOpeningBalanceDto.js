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
import OwnerOpeningBalanceVatEntryDto from './OwnerOpeningBalanceVatEntryDto';

/**
 * The OwnerOpeningBalanceDto model module.
 * @module model/OwnerOpeningBalanceDto
 * @version v1
 */
class OwnerOpeningBalanceDto {
    /**
     * Constructs a new <code>OwnerOpeningBalanceDto</code>.
     * @alias module:model/OwnerOpeningBalanceDto
     */
    constructor() { 
        
        OwnerOpeningBalanceDto.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>OwnerOpeningBalanceDto</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/OwnerOpeningBalanceDto} obj Optional instance to populate.
     * @return {module:model/OwnerOpeningBalanceDto} The populated <code>OwnerOpeningBalanceDto</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new OwnerOpeningBalanceDto();

            if (data.hasOwnProperty('entryDate')) {
                obj['entryDate'] = ApiClient.convertToType(data['entryDate'], 'Date');
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'Number');
            }
            if (data.hasOwnProperty('isChanged')) {
                obj['isChanged'] = ApiClient.convertToType(data['isChanged'], 'Boolean');
            }
            if (data.hasOwnProperty('procDate')) {
                obj['procDate'] = ApiClient.convertToType(data['procDate'], 'Date');
            }
            if (data.hasOwnProperty('reference')) {
                obj['reference'] = ApiClient.convertToType(data['reference'], 'String');
            }
            if (data.hasOwnProperty('timestamp')) {
                obj['timestamp'] = ApiClient.convertToType(data['timestamp'], 'Blob');
            }
            if (data.hasOwnProperty('total')) {
                obj['total'] = ApiClient.convertToType(data['total'], 'Number');
            }
            if (data.hasOwnProperty('totalVAT')) {
                obj['totalVAT'] = ApiClient.convertToType(data['totalVAT'], 'Number');
            }
            if (data.hasOwnProperty('unpaid')) {
                obj['unpaid'] = ApiClient.convertToType(data['unpaid'], 'Number');
            }
            if (data.hasOwnProperty('vatEntries')) {
                obj['vatEntries'] = ApiClient.convertToType(data['vatEntries'], [OwnerOpeningBalanceVatEntryDto]);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>OwnerOpeningBalanceDto</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>OwnerOpeningBalanceDto</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['reference'] && !(typeof data['reference'] === 'string' || data['reference'] instanceof String)) {
            throw new Error("Expected the field `reference` to be a primitive type in the JSON string but got " + data['reference']);
        }
        if (data['vatEntries']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['vatEntries'])) {
                throw new Error("Expected the field `vatEntries` to be an array in the JSON data but got " + data['vatEntries']);
            }
            // validate the optional field `vatEntries` (array)
            for (const item of data['vatEntries']) {
                OwnerOpeningBalanceVatEntryDto.validateJSON(item);
            };
        }

        return true;
    }


}



/**
 * @member {Date} entryDate
 */
OwnerOpeningBalanceDto.prototype['entryDate'] = undefined;

/**
 * @member {Number} id
 */
OwnerOpeningBalanceDto.prototype['id'] = undefined;

/**
 * @member {Boolean} isChanged
 */
OwnerOpeningBalanceDto.prototype['isChanged'] = undefined;

/**
 * @member {Date} procDate
 */
OwnerOpeningBalanceDto.prototype['procDate'] = undefined;

/**
 * @member {String} reference
 */
OwnerOpeningBalanceDto.prototype['reference'] = undefined;

/**
 * @member {Blob} timestamp
 */
OwnerOpeningBalanceDto.prototype['timestamp'] = undefined;

/**
 * @member {Number} total
 */
OwnerOpeningBalanceDto.prototype['total'] = undefined;

/**
 * @member {Number} totalVAT
 */
OwnerOpeningBalanceDto.prototype['totalVAT'] = undefined;

/**
 * @member {Number} unpaid
 */
OwnerOpeningBalanceDto.prototype['unpaid'] = undefined;

/**
 * @member {Array.<module:model/OwnerOpeningBalanceVatEntryDto>} vatEntries
 */
OwnerOpeningBalanceDto.prototype['vatEntries'] = undefined;






export default OwnerOpeningBalanceDto;

