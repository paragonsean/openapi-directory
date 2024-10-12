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
import ApplicationActivities from '../model/ApplicationActivities';
import ApplicationActivityContents from '../model/ApplicationActivityContents';
import Error from '../model/Error';
import HarvestActivities from '../model/HarvestActivities';
import HarvestActivityContents from '../model/HarvestActivityContents';
import PlantingActivities from '../model/PlantingActivities';
import PlantingActivityContents from '../model/PlantingActivityContents';
import ScoutingObservation from '../model/ScoutingObservation';
import ScoutingObservationAttachmentContents from '../model/ScoutingObservationAttachmentContents';
import ScoutingObservationAttachments from '../model/ScoutingObservationAttachments';
import ScoutingObservations from '../model/ScoutingObservations';

/**
* Layers service.
* @module api/LayersApi
* @version 4.0.11
*/
export default class LayersApi {

    /**
    * Constructs a new LayersApi. 
    * @alias module:api/LayersApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the v4LayersAsAppliedActivityIdContentsGet operation.
     * @callback module:api/LayersApi~v4LayersAsAppliedActivityIdContentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApplicationActivityContents} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the raw application activity
     * Retrieve an individual application activity by id.  Ids are retrieved via the  /layers/asApplied route. Downloads larger than `5MiB` (`5242880 bytes`) in size, must be downloaded in chunks no larger than `5MiB` (`5242880 bytes`) and no smaller than `1MiB`  (`1048576 bytes`). The last chunk could be less than `1MiB` (`1048576 bytes`). The data is compressed using .zip format.
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {String} activityId Unique identifier of the Application Activity.
     * @param {String} range Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
     * @param {module:api/LayersApi~v4LayersAsAppliedActivityIdContentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApplicationActivityContents}
     */
    v4LayersAsAppliedActivityIdContentsGet(accept, activityId, range, callback) {
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersAsAppliedActivityIdContentsGet");
      }
      // verify the required parameter 'activityId' is set
      if (activityId === undefined || activityId === null) {
        throw new Error("Missing the required parameter 'activityId' when calling v4LayersAsAppliedActivityIdContentsGet");
      }
      // verify the required parameter 'range' is set
      if (range === undefined || range === null) {
        throw new Error("Missing the required parameter 'range' when calling v4LayersAsAppliedActivityIdContentsGet");
      }

      let pathParams = {
        'activityId': activityId
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
      let returnType = ApplicationActivityContents;
      return this.apiClient.callApi(
        '/v4/layers/asApplied/{activityId}/contents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersAsAppliedGet operation.
     * @callback module:api/LayersApi~v4LayersAsAppliedGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ApplicationActivities} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of application activities
     * Retrieve a list of application activities. The id in the response is used for  GET /v4/layers/asApplied/{activityId}/contents.
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {Object} opts Optional parameters
     * @param {String} [xNextToken] Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
     * @param {Number} [xLimit] Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
     * @param {String} [resourceOwnerId] Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
     * @param {Date} [occurredAfter] Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [occurredBefore] Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [updatedAfter] Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
     * @param {module:api/LayersApi~v4LayersAsAppliedGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ApplicationActivities}
     */
    v4LayersAsAppliedGet(accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersAsAppliedGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'resourceOwnerId': opts['resourceOwnerId'],
        'occurredAfter': opts['occurredAfter'],
        'occurredBefore': opts['occurredBefore'],
        'updatedAfter': opts['updatedAfter']
      };
      let headerParams = {
        'Accept': accept,
        'X-Next-Token': opts['xNextToken'],
        'X-Limit': opts['xLimit']
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ApplicationActivities;
      return this.apiClient.callApi(
        '/v4/layers/asApplied', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersAsHarvestedActivityIdContentsGet operation.
     * @callback module:api/LayersApi~v4LayersAsHarvestedActivityIdContentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/HarvestActivityContents} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the raw harvest activity
     * Retrieve an individual harvest activity by id.  Ids are retrieved via the  /layers/asHarvested route. Downloads larger than `5MiB` (`5242880 bytes`) in size, must be downloaded in chunks no larger than `5MiB` (`5242880 bytes`) and no smaller than `1MiB`  (`1048576 bytes`). The last chunk could be less than `1MiB` (`1048576 bytes`). The data is compressed using .zip format.
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {String} activityId Unique identifier of the Harvest Activity.
     * @param {String} range Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
     * @param {module:api/LayersApi~v4LayersAsHarvestedActivityIdContentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/HarvestActivityContents}
     */
    v4LayersAsHarvestedActivityIdContentsGet(accept, activityId, range, callback) {
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersAsHarvestedActivityIdContentsGet");
      }
      // verify the required parameter 'activityId' is set
      if (activityId === undefined || activityId === null) {
        throw new Error("Missing the required parameter 'activityId' when calling v4LayersAsHarvestedActivityIdContentsGet");
      }
      // verify the required parameter 'range' is set
      if (range === undefined || range === null) {
        throw new Error("Missing the required parameter 'range' when calling v4LayersAsHarvestedActivityIdContentsGet");
      }

      let pathParams = {
        'activityId': activityId
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
      let returnType = HarvestActivityContents;
      return this.apiClient.callApi(
        '/v4/layers/asHarvested/{activityId}/contents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersAsHarvestedGet operation.
     * @callback module:api/LayersApi~v4LayersAsHarvestedGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/HarvestActivities} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of harvest activities
     * Retrieve a list of harvest activities. The id in the response is used for  GET /v4/layers/asHarvested/{activityId}/contents.
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {Object} opts Optional parameters
     * @param {String} [xNextToken] Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
     * @param {Number} [xLimit] Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
     * @param {String} [resourceOwnerId] Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
     * @param {Date} [occurredAfter] Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [occurredBefore] Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [updatedAfter] Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
     * @param {module:api/LayersApi~v4LayersAsHarvestedGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/HarvestActivities}
     */
    v4LayersAsHarvestedGet(accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersAsHarvestedGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'resourceOwnerId': opts['resourceOwnerId'],
        'occurredAfter': opts['occurredAfter'],
        'occurredBefore': opts['occurredBefore'],
        'updatedAfter': opts['updatedAfter']
      };
      let headerParams = {
        'Accept': accept,
        'X-Next-Token': opts['xNextToken'],
        'X-Limit': opts['xLimit']
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = HarvestActivities;
      return this.apiClient.callApi(
        '/v4/layers/asHarvested', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersAsPlantedActivityIdContentsGet operation.
     * @callback module:api/LayersApi~v4LayersAsPlantedActivityIdContentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PlantingActivityContents} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the raw planting activity
     * Retrieve an individual planting activity by id.  Ids are retrieved via the  /layers/asPlanted route. Downloads larger than `5MiB` (`5242880 bytes`) in size, must be downloaded in chunks no larger than `5MiB` (`5242880 bytes`) and no smaller than `1MiB`  (`1048576 bytes`). The last chunk could be less than `1MiB` (`1048576 bytes`).  The data is compressed using .zip format.
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {String} activityId Unique identifier of the Planting Activity.
     * @param {String} range Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
     * @param {module:api/LayersApi~v4LayersAsPlantedActivityIdContentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PlantingActivityContents}
     */
    v4LayersAsPlantedActivityIdContentsGet(accept, activityId, range, callback) {
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersAsPlantedActivityIdContentsGet");
      }
      // verify the required parameter 'activityId' is set
      if (activityId === undefined || activityId === null) {
        throw new Error("Missing the required parameter 'activityId' when calling v4LayersAsPlantedActivityIdContentsGet");
      }
      // verify the required parameter 'range' is set
      if (range === undefined || range === null) {
        throw new Error("Missing the required parameter 'range' when calling v4LayersAsPlantedActivityIdContentsGet");
      }

      let pathParams = {
        'activityId': activityId
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
      let returnType = PlantingActivityContents;
      return this.apiClient.callApi(
        '/v4/layers/asPlanted/{activityId}/contents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersAsPlantedGet operation.
     * @callback module:api/LayersApi~v4LayersAsPlantedGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/PlantingActivities} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of planting activities
     * Retrieve a list of planting activities. The id in the response is used for  GET /v4/layers/asPlanted/{activityId}/contents.
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {Object} opts Optional parameters
     * @param {String} [xNextToken] Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
     * @param {Number} [xLimit] Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
     * @param {String} [resourceOwnerId] Optional unique identifier of the resource owner.  If resourceOwnerId is not specified, it defaults to the x-authenticated-user-uuid.
     * @param {Date} [occurredAfter] Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [occurredBefore] Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [updatedAfter] Optional updated time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a modification time at or after (inclusive) the specified time.
     * @param {module:api/LayersApi~v4LayersAsPlantedGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/PlantingActivities}
     */
    v4LayersAsPlantedGet(accept, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersAsPlantedGet");
      }

      let pathParams = {
      };
      let queryParams = {
        'resourceOwnerId': opts['resourceOwnerId'],
        'occurredAfter': opts['occurredAfter'],
        'occurredBefore': opts['occurredBefore'],
        'updatedAfter': opts['updatedAfter']
      };
      let headerParams = {
        'Accept': accept,
        'X-Next-Token': opts['xNextToken'],
        'X-Limit': opts['xLimit']
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = PlantingActivities;
      return this.apiClient.callApi(
        '/v4/layers/asPlanted', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersScoutingObservationsGet operation.
     * @callback module:api/LayersApi~v4LayersScoutingObservationsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScoutingObservations} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve a list of scouting observations
     * Retrieve a list of scouting observations created or updated by the user identified by the Authorization header.
     * @param {Object} opts Optional parameters
     * @param {String} [xNextToken] Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
     * @param {Number} [xLimit] Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
     * @param {Date} [occurredAfter] Optional start time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with an end time at or after (inclusive) the specified time will match this filter. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {Date} [occurredBefore] Optional end time by which to filter layer results. Time must be in ISO 8601 format with time zone, e.g. 2016-05-13T00:00:00Z (https://tools.ietf.org/html/rfc3339). Layers with a start time at or before (inclusive) the specified time. If both occurredAfter and occurredBefore are populated, occurredAfter must be <= occurredBefore.
     * @param {module:api/LayersApi~v4LayersScoutingObservationsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScoutingObservations}
     */
    v4LayersScoutingObservationsGet(opts, callback) {
      opts = opts || {};
      let postBody = null;

      let pathParams = {
      };
      let queryParams = {
        'occurredAfter': opts['occurredAfter'],
        'occurredBefore': opts['occurredBefore']
      };
      let headerParams = {
        'X-Next-Token': opts['xNextToken'],
        'X-Limit': opts['xLimit']
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ScoutingObservations;
      return this.apiClient.callApi(
        '/v4/layers/scoutingObservations', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet operation.
     * @callback module:api/LayersApi~v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScoutingObservationAttachmentContents} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve the binary contents of a scouting observation’s attachment.
     * Photos added to scouting notes in the FieldView app are capped to `20MiB` (`20971520 bytes`), and we won’t store photos larger than that in a scouting note. Downloads larger than `5MiB` (`5242880 bytes`) in size, must be downloaded in chunks no larger than `5MiB` (`5242880 bytes`) and no smaller than `1MiB` (`1048576 bytes`). The last chunk could be less than `1MiB` (`1048576 bytes`).
     * @param {String} accept Must be either \\*_/_* or application/octet-stream,application/json
     * @param {String} scoutingObservationId Unique identifier of the Scouting Observation.
     * @param {String} attachmentId Unique identifier of the attachment.
     * @param {String} range Byte range `bytes=start-end` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.35.1). e.g. bytes=0-1048576. Currently only single range value is supported. Both start and end need to be specified, end value should be greater than start and end - start should not be greater than 5MiB.
     * @param {module:api/LayersApi~v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScoutingObservationAttachmentContents}
     */
    v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet(accept, scoutingObservationId, attachmentId, range, callback) {
      let postBody = null;
      // verify the required parameter 'accept' is set
      if (accept === undefined || accept === null) {
        throw new Error("Missing the required parameter 'accept' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet");
      }
      // verify the required parameter 'scoutingObservationId' is set
      if (scoutingObservationId === undefined || scoutingObservationId === null) {
        throw new Error("Missing the required parameter 'scoutingObservationId' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet");
      }
      // verify the required parameter 'attachmentId' is set
      if (attachmentId === undefined || attachmentId === null) {
        throw new Error("Missing the required parameter 'attachmentId' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet");
      }
      // verify the required parameter 'range' is set
      if (range === undefined || range === null) {
        throw new Error("Missing the required parameter 'range' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsAttachmentIdContentsGet");
      }

      let pathParams = {
        'scoutingObservationId': scoutingObservationId,
        'attachmentId': attachmentId
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
      let accepts = ['image/jpeg', 'image/png', 'application/json'];
      let returnType = ScoutingObservationAttachmentContents;
      return this.apiClient.callApi(
        '/v4/layers/scoutingObservations/{scoutingObservationId}/attachments/{attachmentId}/contents', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet operation.
     * @callback module:api/LayersApi~v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScoutingObservationAttachments} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve attachments associated with a given scouting observation.
     * Retrieve attachments associated with a given scouting observation. Photos added to scouting notes in the FieldView app are capped to 20MB, and we won’t store photos larger than that in a scouting note.
     * @param {String} scoutingObservationId Unique identifier of the Scouting Observation.
     * @param {Object} opts Optional parameters
     * @param {String} [xNextToken] Opaque string which allows for fetching the next batch of results.  Can be used to poll for changes.
     * @param {Number} [xLimit] Max number of results to return per batch.  Must be between 1 and 100 inclusive.  Defaults to 100.
     * @param {module:api/LayersApi~v4LayersScoutingObservationsScoutingObservationIdAttachmentsGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScoutingObservationAttachments}
     */
    v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet(scoutingObservationId, opts, callback) {
      opts = opts || {};
      let postBody = null;
      // verify the required parameter 'scoutingObservationId' is set
      if (scoutingObservationId === undefined || scoutingObservationId === null) {
        throw new Error("Missing the required parameter 'scoutingObservationId' when calling v4LayersScoutingObservationsScoutingObservationIdAttachmentsGet");
      }

      let pathParams = {
        'scoutingObservationId': scoutingObservationId
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Next-Token': opts['xNextToken'],
        'X-Limit': opts['xLimit']
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = ScoutingObservationAttachments;
      return this.apiClient.callApi(
        '/v4/layers/scoutingObservations/{scoutingObservationId}/attachments', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the v4LayersScoutingObservationsScoutingObservationIdGet operation.
     * @callback module:api/LayersApi~v4LayersScoutingObservationsScoutingObservationIdGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/ScoutingObservation} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve individual scouting observation
     * Retrieve an individual scouting observation by id.  Ids are retrieved via the /layers/scoutingObservations route.
     * @param {String} scoutingObservationId Unique identifier of the Scouting Observation.
     * @param {module:api/LayersApi~v4LayersScoutingObservationsScoutingObservationIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/ScoutingObservation}
     */
    v4LayersScoutingObservationsScoutingObservationIdGet(scoutingObservationId, callback) {
      let postBody = null;
      // verify the required parameter 'scoutingObservationId' is set
      if (scoutingObservationId === undefined || scoutingObservationId === null) {
        throw new Error("Missing the required parameter 'scoutingObservationId' when calling v4LayersScoutingObservationsScoutingObservationIdGet");
      }

      let pathParams = {
        'scoutingObservationId': scoutingObservationId
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
      let returnType = ScoutingObservation;
      return this.apiClient.callApi(
        '/v4/layers/scoutingObservations/{scoutingObservationId}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
