/**
 * LoL v3 Projections
 * LoL v3 Projections
 *
 * The version of the OpenAPI document: 1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import DfsSlate from '../model/DfsSlate';
import PlayerGameProjection from '../model/PlayerGameProjection';

/**
* Default service.
* @module api/DefaultApi
* @version 1.0
*/
export default class DefaultApi {

    /**
    * Constructs a new DefaultApi. 
    * @alias module:api/DefaultApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the dfsSlatesByDate operation.
     * @callback module:api/DefaultApi~dfsSlatesByDateCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/DfsSlate>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Dfs Slates By Date
     * @param {module:model/String} format Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
     * @param {String} date The date of the game(s). <br>Examples: <code>2017-02-27</code>, <code>2017-09-01</code>.
     * @param {module:api/DefaultApi~dfsSlatesByDateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/DfsSlate>}
     */
    dfsSlatesByDate(format, date, callback) {
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling dfsSlatesByDate");
      }
      // verify the required parameter 'date' is set
      if (date === undefined || date === null) {
        throw new Error("Missing the required parameter 'date' when calling dfsSlatesByDate");
      }

      let pathParams = {
        'format': format,
        'date': date
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKeyQuery', 'apiKeyHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [DfsSlate];
      return this.apiClient.callApi(
        '/{format}/DfsSlatesByDate/{date}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectedPlayerGameStatsByDate operation.
     * @callback module:api/DefaultApi~projectedPlayerGameStatsByDateCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/PlayerGameProjection>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Projected Player Game Stats by Date
     * Projected Player Game Stats by Date
     * @param {module:model/String} format Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
     * @param {String} date The date of the game(s). <br>Example: <code>2019-01-20</code>
     * @param {module:api/DefaultApi~projectedPlayerGameStatsByDateCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/PlayerGameProjection>}
     */
    projectedPlayerGameStatsByDate(format, date, callback) {
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling projectedPlayerGameStatsByDate");
      }
      // verify the required parameter 'date' is set
      if (date === undefined || date === null) {
        throw new Error("Missing the required parameter 'date' when calling projectedPlayerGameStatsByDate");
      }

      let pathParams = {
        'format': format,
        'date': date
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKeyQuery', 'apiKeyHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [PlayerGameProjection];
      return this.apiClient.callApi(
        '/{format}/PlayerGameProjectionStatsByDate/{date}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the projectedPlayerGameStatsByPlayer operation.
     * @callback module:api/DefaultApi~projectedPlayerGameStatsByPlayerCallback
     * @param {String} error Error message, if any.
     * @param {Array.<module:model/PlayerGameProjection>} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Projected Player Game Stats by Player
     * Projected Player Game Stats by Date
     * @param {module:model/String} format Desired response format. Valid entries are <code>XML</code> or <code>JSON</code>.
     * @param {String} date The date of the game(s). <br>Example: <code>2019-01-20</code>
     * @param {String} playerid Unique FantasyData Player ID. Example:<code>100001500</code>.
     * @param {module:api/DefaultApi~projectedPlayerGameStatsByPlayerCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Array.<module:model/PlayerGameProjection>}
     */
    projectedPlayerGameStatsByPlayer(format, date, playerid, callback) {
      let postBody = null;
      // verify the required parameter 'format' is set
      if (format === undefined || format === null) {
        throw new Error("Missing the required parameter 'format' when calling projectedPlayerGameStatsByPlayer");
      }
      // verify the required parameter 'date' is set
      if (date === undefined || date === null) {
        throw new Error("Missing the required parameter 'date' when calling projectedPlayerGameStatsByPlayer");
      }
      // verify the required parameter 'playerid' is set
      if (playerid === undefined || playerid === null) {
        throw new Error("Missing the required parameter 'playerid' when calling projectedPlayerGameStatsByPlayer");
      }

      let pathParams = {
        'format': format,
        'date': date,
        'playerid': playerid
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['apiKeyQuery', 'apiKeyHeader'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = [PlayerGameProjection];
      return this.apiClient.callApi(
        '/{format}/PlayerGameProjectionStatsByPlayer/{date}/{playerid}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
