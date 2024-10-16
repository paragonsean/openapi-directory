/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import GetDetailedRefundsOut from '../model/GetDetailedRefundsOut';
import GetRefundsOut from '../model/GetRefundsOut';
import GetSettlementOut from '../model/GetSettlementOut';
import GetSettlementSummaryOut from '../model/GetSettlementSummaryOut';

/**
* Settlement service.
* @module api/SettlementApi
* @version 1
*/
export default class SettlementApi {

    /**
    * Constructs a new SettlementApi. 
    * @alias module:api/SettlementApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the getDetailedRefunds operation.
     * @callback module:api/SettlementApi~getDetailedRefundsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetDetailedRefundsOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Detailed refunds
     * @param {Object} opts Optional parameters
     * @param {String} [format] Output format. 'json' or 'csv'. Default value is 'json'
     * @param {String} [countryCodes] Comma separated list of 2-letter country codes
     * @param {String} [dateFrom] Take only refunds issued at or after the date. Format: yyyy-MM-dd
     * @param {String} [dateTo] Take only refunds issued at or before the date. Format: yyyy-MM-dd
     * @param {Number} [limit] Limit (no more than 1000, defaults to 100).
     * @param {Number} [offset] Offset. Defaults to 0
     * @param {module:api/SettlementApi~getDetailedRefundsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetDetailedRefundsOut}
     */
    getDetailedRefunds(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'format': opts['format'],
        'country_codes': opts['countryCodes'],
        'date_from': opts['dateFrom'],
        'date_to': opts['dateTo'],
        'limit': opts['limit'],
        'offset': opts['offset']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetDetailedRefundsOut;
      return this.apiClient.callApi(
        '/api/v1/settlement/detailed_refunds', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getRefunds operation.
     * @callback module:api/SettlementApi~getRefundsCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetRefundsOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Fetch refunds
     * @param {String} dateFrom Take only refunds issued at or after the date. Format: yyyy-MM-dd
     * @param {Object} opts Optional parameters
     * @param {String} [format] Output format. 'csv' value is accepted as well
     * @param {String} [mossCountryCode] MOSS country code, used to determine currency. If ommited, merchant default setting is used.
     * @param {String} [taxRegion] Tax region key, defaults to EU for backwards compatibility.
     * @param {module:api/SettlementApi~getRefundsCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetRefundsOut}
     */
    getRefunds(dateFrom, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'dateFrom' is set
      if (dateFrom === undefined || dateFrom === null) {
        throw new Error("Missing the required parameter 'dateFrom' when calling getRefunds");
      }

      let pathParams = {
      };
      let queryParams = {
        'format': opts['format'],
        'moss_country_code': opts['mossCountryCode'],
        'tax_region': opts['taxRegion'],
        'date_from': dateFrom
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetRefundsOut;
      return this.apiClient.callApi(
        '/api/v1/settlement/refunds', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSettlement operation.
     * @callback module:api/SettlementApi~getSettlementCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSettlementOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Fetch settlement
     * @param {String} quarter Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to 'range'.
     * @param {Object} opts Optional parameters
     * @param {String} [mossTaxId] MOSS-assigned tax ID - if not provided, merchant's national tax number will be used. Deprecated, please use tax-id.
     * @param {String} [currencyCode] ISO 3-letter currency code, e.g. EUR or USD. If provided, all amounts will be coerced for this currency. Defaults to region's currency code.
     * @param {String} [endMonth] Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
     * @param {String} [taxId] MOSS-assigned tax ID - if not provided, merchant's national tax number will be used. Deprecated, please use tax-id.
     * @param {String} [refundDateKindOverride] Set to 'order_date' to show only refunds for the transactions in the selected reporting period. Set to 'refund_timestamp' to show refunds that were created in the selected reporting period. Do not set to use the default region's setting.
     * @param {String} [startMonth] Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
     * @param {String} [mossCountryCode] MOSS country code, used to determine currency/region. If ommited, merchant default setting is used. Deprecated: please use tax-country-code.
     * @param {String} [format] Output format. 'csv' value is accepted as well
     * @param {String} [taxCountryCode] Tax entity country code, used to determine currency/region. 
     * @param {module:api/SettlementApi~getSettlementCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSettlementOut}
     */
    getSettlement(quarter, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'quarter' is set
      if (quarter === undefined || quarter === null) {
        throw new Error("Missing the required parameter 'quarter' when calling getSettlement");
      }

      let pathParams = {
        'quarter': quarter
      };
      let queryParams = {
        'moss_tax_id': opts['mossTaxId'],
        'currency_code': opts['currencyCode'],
        'end_month': opts['endMonth'],
        'tax_id': opts['taxId'],
        'refund_date_kind_override': opts['refundDateKindOverride'],
        'start_month': opts['startMonth'],
        'moss_country_code': opts['mossCountryCode'],
        'format': opts['format'],
        'tax_country_code': opts['taxCountryCode']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetSettlementOut;
      return this.apiClient.callApi(
        '/api/v1/settlement/{quarter}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getSettlementSummary operation.
     * @callback module:api/SettlementApi~getSettlementSummaryCallback
     * @param {String} error Error message, if any.
     * @param {module:model/GetSettlementSummaryOut} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Fetch summary
     * @param {String} quarter Quarter in yyyy-MM format. If start-date and end-date are provided, quarter is ignored and should be set to 'range'.
     * @param {Object} opts Optional parameters
     * @param {String} [mossCountryCode] MOSS country code, used to determine currency. If ommited, merchant default setting is used.
     * @param {String} [taxRegion] Tax region key
     * @param {String} [startMonth] Period start month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
     * @param {String} [endMonth] Period end month in yyyy-MM format. Either quarter or start-month and end-month have to be provided.
     * @param {module:api/SettlementApi~getSettlementSummaryCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/GetSettlementSummaryOut}
     */
    getSettlementSummary(quarter, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'quarter' is set
      if (quarter === undefined || quarter === null) {
        throw new Error("Missing the required parameter 'quarter' when calling getSettlementSummary");
      }

      let pathParams = {
        'quarter': quarter
      };
      let queryParams = {
        'moss_country_code': opts['mossCountryCode'],
        'tax_region': opts['taxRegion'],
        'start_month': opts['startMonth'],
        'end_month': opts['endMonth']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = GetSettlementSummaryOut;
      return this.apiClient.callApi(
        '/api/v1/settlement/summary/{quarter}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
