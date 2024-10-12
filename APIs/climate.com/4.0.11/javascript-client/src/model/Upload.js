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

import ApiClient from '../ApiClient';

/**
 * The Upload model module.
 * @module model/Upload
 * @version 4.0.11
 */
class Upload {
    /**
     * Constructs a new <code>Upload</code>.
     * Client request to upload data for a user.
     * @alias module:model/Upload
     * @param contentType {module:model/Upload.ContentTypeEnum} Content type representing data being uploaded (e.g. image/vnd.climate.rgb.geotiff)
     * @param length {Number} Content size in bytes
     * @param md5 {String} Base64 encoded md5 hash of the content
     */
    constructor(contentType, length, md5) { 
        
        Upload.initialize(this, contentType, length, md5);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, contentType, length, md5) { 
        obj['contentType'] = contentType;
        obj['length'] = length;
        obj['md5'] = md5;
    }

    /**
     * Constructs a <code>Upload</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/Upload} obj Optional instance to populate.
     * @return {module:model/Upload} The populated <code>Upload</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new Upload();

            if (data.hasOwnProperty('contentType')) {
                obj['contentType'] = ApiClient.convertToType(data['contentType'], 'String');
            }
            if (data.hasOwnProperty('length')) {
                obj['length'] = ApiClient.convertToType(data['length'], 'Number');
            }
            if (data.hasOwnProperty('md5')) {
                obj['md5'] = ApiClient.convertToType(data['md5'], 'String');
            }
            if (data.hasOwnProperty('metadata')) {
                obj['metadata'] = ApiClient.convertToType(data['metadata'], {'String': Object});
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>Upload</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>Upload</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of Upload.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['contentType'] && !(typeof data['contentType'] === 'string' || data['contentType'] instanceof String)) {
            throw new Error("Expected the field `contentType` to be a primitive type in the JSON string but got " + data['contentType']);
        }
        // ensure the json data is a string
        if (data['md5'] && !(typeof data['md5'] === 'string' || data['md5'] instanceof String)) {
            throw new Error("Expected the field `md5` to be a primitive type in the JSON string but got " + data['md5']);
        }

        return true;
    }


}

Upload.RequiredProperties = ["contentType", "length", "md5"];

/**
 * Content type representing data being uploaded (e.g. image/vnd.climate.rgb.geotiff)
 * @member {module:model/Upload.ContentTypeEnum} contentType
 */
Upload.prototype['contentType'] = undefined;

/**
 * Content size in bytes
 * @member {Number} length
 */
Upload.prototype['length'] = undefined;

/**
 * Base64 encoded md5 hash of the content
 * @member {String} md5
 */
Upload.prototype['md5'] = undefined;

/**
 * @member {Object.<String, Object>} metadata
 */
Upload.prototype['metadata'] = undefined;





/**
 * Allowed values for the <code>contentType</code> property.
 * @enum {String}
 * @readonly
 */
Upload['ContentTypeEnum'] = {

    /**
     * value: "image/vnd.climate.thermal.geotiff"
     * @const
     */
    "image/vnd.climate.thermal.geotiff": "image/vnd.climate.thermal.geotiff",

    /**
     * value: "image/vnd.climate.ndvi.geotiff"
     * @const
     */
    "image/vnd.climate.ndvi.geotiff": "image/vnd.climate.ndvi.geotiff",

    /**
     * value: "image/vnd.climate.rgb.geotiff"
     * @const
     */
    "image/vnd.climate.rgb.geotiff": "image/vnd.climate.rgb.geotiff",

    /**
     * value: "image/vnd.climate.rgb-nir.geotiff"
     * @const
     */
    "image/vnd.climate.rgb-nir.geotiff": "image/vnd.climate.rgb-nir.geotiff",

    /**
     * value: "image/vnd.climate.rgb-cir.geotiff"
     * @const
     */
    "image/vnd.climate.rgb-cir.geotiff": "image/vnd.climate.rgb-cir.geotiff",

    /**
     * value: "image/vnd.climate.waterstress.geotiff"
     * @const
     */
    "image/vnd.climate.waterstress.geotiff": "image/vnd.climate.waterstress.geotiff",

    /**
     * value: "image/vnd.climate.elevation.geotiff"
     * @const
     */
    "image/vnd.climate.elevation.geotiff": "image/vnd.climate.elevation.geotiff",

    /**
     * value: "image/vnd.climate.raw.geotiff"
     * @const
     */
    "image/vnd.climate.raw.geotiff": "image/vnd.climate.raw.geotiff",

    /**
     * value: "application/vnd.climate.field.geojson"
     * @const
     */
    "application/vnd.climate.field.geojson": "application/vnd.climate.field.geojson",

    /**
     * value: "application/vnd.climate.rx.planting.shp"
     * @const
     */
    "application/vnd.climate.rx.planting.shp": "application/vnd.climate.rx.planting.shp",

    /**
     * value: "application/vnd.climate.prescription.zones.shp"
     * @const
     */
    "application/vnd.climate.prescription.zones.shp": "application/vnd.climate.prescription.zones.shp",

    /**
     * value: "application/vnd.climate.modus.xml"
     * @const
     */
    "application/vnd.climate.modus.xml": "application/vnd.climate.modus.xml",

    /**
     * value: "application/vnd.climate.stand-count.geojson"
     * @const
     */
    "application/vnd.climate.stand-count.geojson": "application/vnd.climate.stand-count.geojson",

    /**
     * value: "application/vnd.climate.weed-count.geojson"
     * @const
     */
    "application/vnd.climate.weed-count.geojson": "application/vnd.climate.weed-count.geojson",

    /**
     * value: "application/vnd.climate.as-applied.zip"
     * @const
     */
    "application/vnd.climate.as-applied.zip": "application/vnd.climate.as-applied.zip",

    /**
     * value: "application/vnd.climate.as-planted.zip"
     * @const
     */
    "application/vnd.climate.as-planted.zip": "application/vnd.climate.as-planted.zip",

    /**
     * value: "application/vnd.climate.as-harvested.zip"
     * @const
     */
    "application/vnd.climate.as-harvested.zip": "application/vnd.climate.as-harvested.zip"
};



export default Upload;

