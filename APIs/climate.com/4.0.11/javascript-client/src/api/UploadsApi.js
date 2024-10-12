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
import Error from '../model/Error';
import Upload from '../model/Upload';
import UploadStatus from '../model/UploadStatus';
import UploadStatusQuery from '../model/UploadStatusQuery';
import UploadStatuses from '../model/UploadStatuses';

/**
* Uploads service.
* @module api/UploadsApi
* @version 4.0.11
*/
export default class UploadsApi {

    /**
    * Constructs a new UploadsApi. 
    * @alias module:api/UploadsApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the chunkedUpload operation.
     * @callback module:api/UploadsApi~chunkedUploadCallback
     * @param {String} error Error message, if any.
     * @param data This operation does not return a value.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Chunked upload of data
     * Send chunked data for an **Upload**.
     * @param {String} contentRange Byte range `bytes start-end/total` (https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.16). e.g. bytes 0-5242880/10242880. Downloads larger than 5MiB (5242880 bytes) in size must be downloaded in chunks no larger than 5MiB (5242880 bytes) and no smaller than 1MiB (1048576 bytes). The last chunk could be less than 1MiB (1048576 bytes).
     * @param {String} uploadId Unique identifier of an Upload.
     * @param {String} contentType Must be `application/octet-stream`
     * @param {module:api/UploadsApi~chunkedUploadCallback} callback The callback function, accepting three arguments: error, data, response
     */
    chunkedUpload(contentRange, uploadId, contentType, callback) {
      let postBody = null;
      // verify the required parameter 'contentRange' is set
      if (contentRange === undefined || contentRange === null) {
        throw new Error("Missing the required parameter 'contentRange' when calling chunkedUpload");
      }
      // verify the required parameter 'uploadId' is set
      if (uploadId === undefined || uploadId === null) {
        throw new Error("Missing the required parameter 'uploadId' when calling chunkedUpload");
      }
      // verify the required parameter 'contentType' is set
      if (contentType === undefined || contentType === null) {
        throw new Error("Missing the required parameter 'contentType' when calling chunkedUpload");
      }

      let pathParams = {
        'uploadId': uploadId
      };
      let queryParams = {
      };
      let headerParams = {
        'Content-Range': contentRange,
        'Content-Type': contentType
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = null;
      return this.apiClient.callApi(
        '/v4/uploads/{uploadId}', 'PUT',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchUploadStatusById operation.
     * @callback module:api/UploadsApi~fetchUploadStatusByIdCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UploadStatus} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve Upload status
     * Check the status of an **Upload** by ID.
     * @param {String} uploadId Unique identifier of an Upload.
     * @param {module:api/UploadsApi~fetchUploadStatusByIdCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UploadStatus}
     */
    fetchUploadStatusById(uploadId, callback) {
      let postBody = null;
      // verify the required parameter 'uploadId' is set
      if (uploadId === undefined || uploadId === null) {
        throw new Error("Missing the required parameter 'uploadId' when calling fetchUploadStatusById");
      }

      let pathParams = {
        'uploadId': uploadId
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
      let returnType = UploadStatus;
      return this.apiClient.callApi(
        '/v4/uploads/{uploadId}/status', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the fetchUploadStatuses operation.
     * @callback module:api/UploadsApi~fetchUploadStatusesCallback
     * @param {String} error Error message, if any.
     * @param {module:model/UploadStatuses} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Retrieve Upload statuses in batch
     * Check the status of multiple **Uploads** (up to 100 per request).
     * @param {Object} opts Optional parameters
     * @param {module:model/UploadStatusQuery} [uploadStatusQuery] 
     * @param {module:api/UploadsApi~fetchUploadStatusesCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/UploadStatuses}
     */
    fetchUploadStatuses(opts, callback) {
      opts = opts || {};
      let postBody = opts['uploadStatusQuery'];

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
      let returnType = UploadStatuses;
      return this.apiClient.callApi(
        '/v4/uploads/status/query', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the postUpload operation.
     * @callback module:api/UploadsApi~postUploadCallback
     * @param {String} error Error message, if any.
     * @param {String} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Initiate a new upload
     * Step one in uploading a data product. The method will return an **Upload** ID which the caller will use in subsequent `PUT` requests. The following `contentTypes` may be uploaded:     <details><summary>__image/vnd.climate.thermal.geotiff__</summary>      Allows for the upload of a thermal image. The image is a single band geotiff with 64 bit signed floating point values in degrees Celsius. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner's system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner's branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   </details>   <details><summary>__image/vnd.climate.ndvi.geotiff__</summary>      Allows for the upload of a NDVI image. The image is a single band geotiff with 64 bit signed floating point values in the range of -1 to 1 inclusive. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner's system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner's branding in the Climate system       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   </details>   <details><summary> __image/vnd.climate.rgb.geotiff__</summary>      Allows for the upload of a true color image. The image is a multi band geotiff with 24-bit composite values. Each band is 8 bits with values in the range of 0 to 255. The Coordinate Reference System (CRS) must be UTM with WGS84 datum. The geotiff must contain 3 bands in the order Red, Green, Blue.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner's system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner's branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   </details>   <details><summary> __image/vnd.climate.rgb-nir.geotiff__</summary>      Allows for the upload of a Near Infrared (NIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner's system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner's branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   </details>   <details><summary>__image/vnd.climate.rgb-cir.geotiff__</summary>      Allows for the upload of a Color Infrared (CIR) image. The Coordinate Reference System (CRS) must be UTM with WGS84 datum.      The following metadata entries are required to be embedded in the geotiff:       * acquisitionStartDate - ISO8601 date       * acquisitionEndDate - ISO8601 date       * isCalibrated - boolean      The following metadata entries are optional:       * sourceId - uuid referencing the asset in the partner's system       * fieldId - uuid referencing a field in the Climate system       * boundaryId - uuid referencing a boundary in the Climate system       * brandId - uuid referencing a partner's branding in the Climate system       * reflectanceComputeMethod - either TOA or GROUND       * name - name of the layer. The maximum number of characters that will be accepted as input is 20.      Requires either imagery:write or platform scope.   </details>   <details><summary> __application/vnd.climate.rx.planting.shp__</summary>      Allows for the upload of a planting prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      Requires either rx:write or platform scope.   </details>   <details><summary> __application/vnd.climate.prescription.zones.shp__</summary>      Allows for the upload of a zones prescription in shapefile format.  The upload must be an archive in the zip format.  It should contain one and only one of each of the following file types:       * .shp       * .shx       * .dbf      All files with the above suffixes must have the same prefix, ie Back40.shp, Back40.shx and Back40.dbf.      The following metadata entries are required:       * fieldId - field identifier for prescription zones.          Requires either rxZones:write or platform scope.   </details>   <details><summary> __application/vnd.climate.modus.xml__</summary>      Allows for the upload of a soil sampling file in the modus 1.0 format with some restrictions.  The upload must be a single xml file.      The following elements are required to be present in the modus file.       * EventCode - Max length of 64 bytes       * EventDate - Must be in ISO8601       * SoilSample - Has a maxOccurs of 20k       * Depth - Has a maxOccurs of 50       * LabName - Must be non-empty.       * StartingDepth - 0 to 36 inclusive, default 0       * EndingDepth - 1 - 36 inclusive, default 1       * ColumnDepth       * DepthUnit - must be inches       * Geometry - point in wgs84          Requires the soil:write scope.    </details>    <details><summary> __application/vnd.climate.stand-count.geojson__</summary>      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature's geometry field must be:       * Point      Requires `imagery:write` scope.    </details>    <details><summary> __application/vnd.climate.weed-count.geojson__</summary>      Allows for the upload of a valid [geojson feature collection](https://tools.ietf.org/html/rfc7946#section-3.3).      Each feature in the collection must contain the following entry in its properties section:       * StandPPA - A count of the number of plants per acre:      Additionally, the type field of each feature's geometry field must be:       * Point      Requires `imagery:write` scope.    </details>    <details><summary> __application/vnd.climate.as-applied.zip__</summary>      Allows for the upload of a valid application data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower's account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires `asApplied:write` scope.    </details>    <details><summary> __application/vnd.climate.as-planted.zip__</summary>      Allows for the upload of a valid planting data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower's account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires `asPlanted:write` scope.    </details>    <details><summary> __application/vnd.climate.as-harvested.zip__</summary>      Allows for the upload of a valid harvest data [supported formats](https://support.climate.com/kt#/kA02A000000DjvOSAS/en_US).      The following metadata entries are required:       * fileName - name of the file being uploaded.      The following metadata entries are optional:       * resourceOwner - the grower's account email, where dealer/partner wants to upload data. As a prerequisite the grower must share their operation with the dealer/partner.      Requires `asHarvested:write` scope.    </details>
     * @param {Object} opts Optional parameters
     * @param {String} [xRecipientEmail] Email address associated with a Climate account, used when to sending to another user.
     * @param {module:model/Upload} [upload] 
     * @param {module:api/UploadsApi~postUploadCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link String}
     */
    postUpload(opts, callback) {
      opts = opts || {};
      let postBody = opts['upload'];

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
        'X-Recipient-Email': opts['xRecipientEmail']
      };
      let formParams = {
      };

      let authNames = ['api_key', 'oauth2_authorization_code'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = 'String';
      return this.apiClient.callApi(
        '/v4/uploads', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
