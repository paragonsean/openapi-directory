/**
 * Climate FieldView Platform APIs
 * **Last Modified**: Wed Jan  4 12:47:29 UTC 2023   All endpoints are only accessible via HTTPS.  * All API endpoints are located at `https://platform.climate.com` (e.g. `https://platform.climate.com/v4/fields`).  * The authorization token endpoint is located at `https://api.climate.com/api/oauth/token`.  ## Troubleshooting  `X-Http-Request-Id` response header will be returned on every call, successful or not. If you experience an issue with our api and need to contact technical support, please supply the value of the `X-Http-Request-Id` header along with an approximate time of when the request was made.  ## Request Limits  When you’re onboarded to Climate’s API platform, your `x-api-key` is assigned a custom usage plan. Usage plans are unique to each partner and have the following key attributes:   1. Throttling information     * burstLimit: Maximum rate limit over a period ranging from 1 second to a few seconds     * rateLimit: A steady-state rate limit  2. Quota information     * Limit: The maximum number of requests that can be made in a given month  When the request rate threshold is exceeded, a `429` response code is returned. Optionally, the [`Retry-After`](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.37) header may be returned:   Following are examples of rate limit errors:  1. Rate limit exceeded:  <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 32     {\"message\":\"Too Many Requests\"}  2. Quota exhausted: <br>HTTP/1.1 429  <br>Content-Type: application/json <br>Content-Length: 29      {\"message\":\"Limit Exceeded\"}  ## Pagination  Pagination is performed via headers. Any request which returns a `\"results\"` array may be paginated. The following figure shows how query results are laid out with X-Limit=4 and no filter applied.  <img style=\"width:70%;height:auto;\" src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/paging.png\">  * If there are no results, a response code of `304` will be returned.  * If the response is the last set of results, a response code of `200` or `206` will be returned.  * If there are more results, a response code of `206` will be returned.  * If `X-Next-Token` is provided in the request headers but the token has expired, a response code of `409` will be returned. This is only applicable for some endpoints; see specific endpoint documentation below.  #### X-Limit  The page size can be controlled with the `X-Limit` header. Valid values are `1-100` and defaults to `100`.  #### X-Next-Token  If the results are paginated, a response header of `X-Next-Token` will be returned. Use the associated value in the subsequent request (via the `X-Next-Token` request header) to retrieve the next page. The following sequence diagram shows how to use `X-Next-Token` to fetch all the records.  <img src=\"https://s3-us-west-2.amazonaws.com/climate-com/images/svg_upload_tests/x-next-token.svg\">   ## Chunked Uploads  Uploads larger than `5MiB` (`5242880 bytes`) must be done in `5MiB` chunks (with the exception of the final chunk). Each chunk request MUST contain a `Content-Range` header specifying the portion of the upload, and a `Content-Type` header specifying binary content type (`application/octet-stream`). Range uploads must be contiguous. The maximum upload size is capped at `500MiB` (`524288000 bytes`).  ## Chunked Downloads  Downloads larger than `5MiB` (`5242880 bytes`) must be done in `1-5MiB` chunks (with the exception of the final chunk, which may be less than `1MiB`). Each chunk request MUST contain a `Range` header specifying the requested portion of the download, and an `Accept` header specifying binary and json content types  (`application/octet-stream,application/json`) or all content types (`*_/_*`).  ## Drivers  If you need drivers to process agronomic data, download the ADAPT plugin below. We only support the plugin in the Windows environment, minimum is Windows 7 SP1.  For asPlanted, asHarvested and asApplied data: * [ADAPT Plugin](https://dev.fieldview.com/drivers/ClimateADAPTPlugin_latest.exe) <br>Release notes can be found [here](https://dev.fieldview.com/drivers/adapt-release-notes.txt). <br>Download and use of the ADAPT plugin means that you agree to the EULA for use of the ADAPT plugin.  <br>Please review the [EULA](https://dev.fieldview.com/EULA/ADAPT%20Plugin%20EULA-06-19.pdf) (last updated on June 6th, 2019) before download and use of the ADAPT plugin. <br>For more information, please refer to:   * [ADAPT Resources](https://adaptframework.org/)   * [ADAPT Overview](https://aggateway.atlassian.net/wiki/spaces/ADM/overview)   * [ADAPT FAQ](https://aggateway.atlassian.net/wiki/spaces/ADM/pages/165942474/ADAPT+Frequently-Asked+Questions+FAQ)   * [ADAPT Videos](https://adaptframework.org/adapt-videos/)  ## Sample Test Data  Sample agronomic data: * [asPlanted and asHarvested data](https://dev.fieldview.com/sample-agronomic-data/Planting_Harvesting_data_04_18_2018_21_46_18.zip) * [asApplied data set 1](https://dev.fieldview.com/sample-agronomic-data/as-applied-data1.zip) * [asApplied data set 2](https://dev.fieldview.com/sample-agronomic-data/as-applied-data2.zip) <br>To upload the sample data to your account, please follow the instructions in this [link](https://support.climate.com/kt#/kA02A000000AaxzSAC/en_US).  Sample soil data: * [Sample soil data](https://dev.fieldview.com/sample-soil-data/soil-sample.xml) --- 
 *
 * The version of the OpenAPI document: 4.0.11
 * Contact: developer@climate.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */


import ApiClient from "../ApiClient";
import CreatedExport from '../model/CreatedExport';
import Error from '../model/Error';
import Export from '../model/Export';
import ExportContents from '../model/ExportContents';
import ExportStatus from '../model/ExportStatus';

/**
* Exports service.
* @module api/ExportsApi
* @version 4.0.11
*/
export default class ExportsApi {

    /**
    * Constructs a new ExportsApi. 
    * @alias module:api/ExportsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the fetchExportContentsById operation.
     * @callback module:api/ExportsApi~fetchExportContentsByIdCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the binary contents of a processed export request.
     * Downloads larger than `5MiB` (`5242880 bytes`) in size must be downloaded in chunks no larger than `5MiB` (`5242880 bytes`) and no smaller than `1MiB` (`1048576 bytes`). The last chunk could be less than `1MiB` (`1048576 bytes`).
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {String} exportId Unique identifier of an Export.
     * @param {String} range Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
     * @param {module:api/ExportsApi~fetchExportContentsByIdCallback} callback The callback function, accepting three arguments: error, data, response
     */
    fetchExportContentsById(accept, exportId, range, callback) {
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling fetchExportContentsById");
      }
      // verify the required parameter 'exportId' is set
      if (exportId === undefined || exportId === null) {
        throw new Error("Missing the required parameter 'exportId' when calling fetchExportContentsById");
      }
      // verify the required parameter 'range' is set
      if (range === undefined || range === null) {
        throw new Error("Missing the required parameter 'range' when calling fetchExportContentsById");
      }

      let pathParams = {
        'exportId': exportId
      };
      let queryParams = {
      };
      let headerParams = {
        'Accept': accept,
        'Range': range
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/octet-stream', 'application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/v4/exports/{exportId}/contents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchExportStatusById operation.
     * @callback module:api/ExportsApi~fetchExportStatusByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ExportStatus} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the status of an Export.
     * Check the status of an **Export** by ID.
     * @param {String} exportId Unique identifier of an Export.
     * @param {module:api/ExportsApi~fetchExportStatusByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ExportStatus}
     */
    fetchExportStatusById(exportId, callback) {
      let postBody = null;
      // verify the required parameter 'exportId' is set
      if (exportId === undefined || exportId === null) {
        throw new Error("Missing the required parameter 'exportId' when calling fetchExportStatusById");
      }

      let pathParams = {
        'exportId': exportId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ExportStatus;
      return this.apiClient.callApi(
        '/v4/exports/{exportId}/status', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postExport operation.
     * @callback module:api/ExportsApi~postExportCallback
     * @param {String} error Error message, if any.
     * @param {module:model/CreatedExport} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Initiate a new export request.
     * Step one in requesting a data product. The method will return an **Export** ID which the caller will use in subsequent `GET` requests. The following `contentTypes` may be requested:   * __application/vnd.climate.acrsi.geojson__ (Beta)      Exports the planting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * plantingStartDate        * plantingEndDate        * resourceOwnerId       Requires `exports:read` and `plantingActivitySummary:read` scope.      * __application/vnd.climate.harvest.geojson__      Exports the harvesting activities accessible by the authenticated user and optionally filtered by resource owner      as a [GeoJSON Feature Collection](https://tools.ietf.org/html/rfc7946#page-12).       The export request definition must contain the following properties:        * harvestStartDate        * harvestEndDate        * resourceOwnerId       Requires `exports:read` and `plantingActivitySummary:read` scope.
     * @param {Object} opts Optional parameters
     * @param {module:model/Export} [_export] 
     * @param {module:api/ExportsApi~postExportCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/CreatedExport}
     */
    postExport(opts, callback) {
      opts = opts || {};
      let postBody = opts['_export'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = CreatedExport;
      return this.apiClient.callApi(
        '/v4/exports', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
