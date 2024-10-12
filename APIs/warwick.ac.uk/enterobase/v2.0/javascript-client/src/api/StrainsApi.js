/**
 * Enterobase-API
 *  API for EnteroBase (https://enterobase.warwick.ac.uk)   EnteroBase is a user-friendly online resource, where users can upload their  own sequencing data for de novo assembly by a stream-lined pipeline. The assemblies  are used for calling MLST and wgMLST patterns, allowing users to compare their strains  to publically available genotyping data from other EnteroBase users, GenBank and classical MLST databases.  Click here to find how to get and use an API token: http://bit.ly/1TKlaOU 
 *
 * The version of the OpenAPI document: v2.0
 * Contact: enterobase@warwick.ac.uk
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import ApiV20DatabaseStrainsBarcodeGetRequest from '../model/ApiV20DatabaseStrainsBarcodeGetRequest';

/**
* Strains service.
* @module api/StrainsApi
* @version v2.0
*/
export default class StrainsApi {

    /**
    * Constructs a new StrainsApi. 
    * @alias module:api/StrainsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the apiV20DatabaseStrainsBarcodeGet operation.
     * @callback module:api/StrainsApi~apiV20DatabaseStrainsBarcodeGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Strain metadata
     * @param {String} database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
     * @param {String} barcode Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiV20DatabaseStrainsBarcodeGetRequest} [apiV20DatabaseStrainsBarcodeGetRequest] 
     * @param {module:api/StrainsApi~apiV20DatabaseStrainsBarcodeGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV20DatabaseStrainsBarcodeGet(database, barcode, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiV20DatabaseStrainsBarcodeGetRequest'];
      // verify the required parameter 'database' is set
      if (database === undefined || database === null) {
        throw new Error("Missing the required parameter 'database' when calling apiV20DatabaseStrainsBarcodeGet");
      }
      // verify the required parameter 'barcode' is set
      if (barcode === undefined || barcode === null) {
        throw new Error("Missing the required parameter 'barcode' when calling apiV20DatabaseStrainsBarcodeGet");
      }

      let pathParams = {
        'database': database,
        'barcode': barcode
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2.0/{database}/strains/{barcode}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV20DatabaseStrainsBarcodePost operation.
     * @callback module:api/StrainsApi~apiV20DatabaseStrainsBarcodePostCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Strain metadata
     * @param {String} database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
     * @param {String} barcode Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiV20DatabaseStrainsBarcodeGetRequest} [apiV20DatabaseStrainsBarcodeGetRequest] 
     * @param {module:api/StrainsApi~apiV20DatabaseStrainsBarcodePostCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV20DatabaseStrainsBarcodePost(database, barcode, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiV20DatabaseStrainsBarcodeGetRequest'];
      // verify the required parameter 'database' is set
      if (database === undefined || database === null) {
        throw new Error("Missing the required parameter 'database' when calling apiV20DatabaseStrainsBarcodePost");
      }
      // verify the required parameter 'barcode' is set
      if (barcode === undefined || barcode === null) {
        throw new Error("Missing the required parameter 'barcode' when calling apiV20DatabaseStrainsBarcodePost");
      }

      let pathParams = {
        'database': database,
        'barcode': barcode
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2.0/{database}/strains/{barcode}', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV20DatabaseStrainsBarcodePut operation.
     * @callback module:api/StrainsApi~apiV20DatabaseStrainsBarcodePutCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Strain metadata
     * @param {String} database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
     * @param {String} barcode Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
     * @param {Object} opts Optional parameters
     * @param {module:model/ApiV20DatabaseStrainsBarcodeGetRequest} [apiV20DatabaseStrainsBarcodeGetRequest] 
     * @param {module:api/StrainsApi~apiV20DatabaseStrainsBarcodePutCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV20DatabaseStrainsBarcodePut(database, barcode, opts, callback) {
      opts = opts || {};
      let postBody = opts['apiV20DatabaseStrainsBarcodeGetRequest'];
      // verify the required parameter 'database' is set
      if (database === undefined || database === null) {
        throw new Error("Missing the required parameter 'database' when calling apiV20DatabaseStrainsBarcodePut");
      }
      // verify the required parameter 'barcode' is set
      if (barcode === undefined || barcode === null) {
        throw new Error("Missing the required parameter 'barcode' when calling apiV20DatabaseStrainsBarcodePut");
      }

      let pathParams = {
        'database': database,
        'barcode': barcode
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2.0/{database}/strains/{barcode}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the apiV20DatabaseStrainsGet operation.
     * @callback module:api/StrainsApi~apiV20DatabaseStrainsGetCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Strain metadata
     * @param {String} database Species database name (senterica, ecoli, yersinia, mcatarrhalis) for Salmonella, Escherichia, Yersinia, Moraxella respectively
     * @param {Object} opts Optional parameters
     * @param {String} [continent] 
     * @param {Number} [offset = 0)] Cursor position in results
     * @param {String} [sampleAccession] 
     * @param {Number} [latitude] 
     * @param {Number} [collectionMonth] 
     * @param {String} [antigenicFormulas] 
     * @param {String} [strainName] 
     * @param {String} [labContact] 
     * @param {String} [sortorder = 'asc')] Order of search results: asc or desc
     * @param {Number} [limit = 50)] Number of results per page
     * @param {String} [serotype] 
     * @param {String} [region] 
     * @param {String} [country] 
     * @param {Number} [collectionDate] 
     * @param {Boolean} [returnAll] 
     * @param {Array.<String>} [onlyFields] 
     * @param {String} [sourceNiche] 
     * @param {Number} [collectionYear] 
     * @param {String} [secondarySampleAccession] 
     * @param {String} [sourceDetails] 
     * @param {Boolean} [substrains] 
     * @param {Number} [version] 
     * @param {String} [sourceType] 
     * @param {String} [orderby = 'barcode')] Field to order by. Default: barcode
     * @param {Boolean} [myStrains] 
     * @param {String} [collectionTime] 
     * @param {String} [county] 
     * @param {String} [uberstrain] 
     * @param {String} [comment] 
     * @param {Number} [longitude] 
     * @param {Number} [reldate] 
     * @param {String} [assemblyBarcode] 
     * @param {Array.<String>} [barcode] Unique barcode for Strain records, <database prefix>_<ID code> e.g. SAL_AA0001AA
     * @param {String} [postcode] 
     * @param {String} [city] 
     * @param {module:api/StrainsApi~apiV20DatabaseStrainsGetCallback} callback The callback function, accepting three arguments: error, data, response
     */
    apiV20DatabaseStrainsGet(database, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'database' is set
      if (database === undefined || database === null) {
        throw new Error("Missing the required parameter 'database' when calling apiV20DatabaseStrainsGet");
      }

      let pathParams = {
        'database': database
      };
      let queryParams = {
        'continent': opts['continent'],
        'offset': opts['offset'],
        'sample_accession': opts['sampleAccession'],
        'latitude': opts['latitude'],
        'collection_month': opts['collectionMonth'],
        'antigenic_formulas': opts['antigenicFormulas'],
        'strain_name': opts['strainName'],
        'lab_contact': opts['labContact'],
        'sortorder': opts['sortorder'],
        'limit': opts['limit'],
        'serotype': opts['serotype'],
        'region': opts['region'],
        'country': opts['country'],
        'collection_date': opts['collectionDate'],
        'return_all': opts['returnAll'],
        'only_fields': this.apiClient.buildCollectionParam(opts['onlyFields'], 'multi'),
        'source_niche': opts['sourceNiche'],
        'collection_year': opts['collectionYear'],
        'secondary_sample_accession': opts['secondarySampleAccession'],
        'source_details': opts['sourceDetails'],
        'substrains': opts['substrains'],
        'version': opts['version'],
        'source_type': opts['sourceType'],
        'orderby': opts['orderby'],
        'my_strains': opts['myStrains'],
        'collection_time': opts['collectionTime'],
        'county': opts['county'],
        'uberstrain': opts['uberstrain'],
        'comment': opts['comment'],
        'longitude': opts['longitude'],
        'reldate': opts['reldate'],
        'assembly_barcode': opts['assemblyBarcode'],
        'barcode': this.apiClient.buildCollectionParam(opts['barcode'], 'multi'),
        'postcode': opts['postcode'],
        'city': opts['city']
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = [];
      let accepts = [];
      let returnType = null;
      return this.apiClient.callApi(
        '/api/v2.0/{database}/strains', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
