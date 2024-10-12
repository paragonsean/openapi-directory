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
import Geometry from './Geometry';
import ScoutingTag from './ScoutingTag';

/**
 * The ScoutingObservation model module.
 * @module model/ScoutingObservation
 * @version 4.0.11
 */
class ScoutingObservation {
    /**
     * Constructs a new <code>ScoutingObservation</code>.
     * @alias module:model/ScoutingObservation
     * @param endTime {Date} The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).
     * @param fieldIds {Array.<String>} Array of field ids associated with this observation.
     * @param id {String} The id of a scouting observation.
     * @param location {module:model/Geometry} 
     * @param locationDisplayColor {module:model/ScoutingObservation.LocationDisplayColorEnum} Color of scouting pin assigned in the Climate FieldView app. Limited in the Ux to a set of RGB values. * #307af7 * #38d753 * #b037e4 * #ef3e3e * #f7ec41 * #ff8439 * #808080 
     * @param note {String} The text of the scouting observation. Maximum of 4000 characters.
     * @param startTime {Date} The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).
     * @param status {module:model/ScoutingObservation.StatusEnum} The status of the scouting observation For example : ACTIVE, DELETED
     * @param tags {Array.<module:model/ScoutingTag>} For example, ROCK_STONE, PONDING_WET, HAIL Maximum 20 tags allowed, 40 characters per tag.
     * @param timespan {module:model/ScoutingObservation.TimespanEnum} Permanent or seasonal
     * @param title {String} The title or summary of the scouting observation. 40 Characters long, no emojis, and leading and trailing whitespace will be trimmed.
     * @param updatedAt {Date} The time the scouting observation or any of its attachments was last updated.Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339).
     */
    constructor(endTime, fieldIds, id, location, locationDisplayColor, note, startTime, status, tags, timespan, title, updatedAt) { 
        
        ScoutingObservation.initialize(this, endTime, fieldIds, id, location, locationDisplayColor, note, startTime, status, tags, timespan, title, updatedAt);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, endTime, fieldIds, id, location, locationDisplayColor, note, startTime, status, tags, timespan, title, updatedAt) { 
        obj['endTime'] = endTime;
        obj['fieldIds'] = fieldIds;
        obj['id'] = id;
        obj['location'] = location;
        obj['locationDisplayColor'] = locationDisplayColor;
        obj['note'] = note;
        obj['startTime'] = startTime;
        obj['status'] = status;
        obj['tags'] = tags;
        obj['timespan'] = timespan;
        obj['title'] = title;
        obj['updatedAt'] = updatedAt;
    }

    /**
     * Constructs a <code>ScoutingObservation</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/ScoutingObservation} obj Optional instance to populate.
     * @return {module:model/ScoutingObservation} The populated <code>ScoutingObservation</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new ScoutingObservation();

            if (data.hasOwnProperty('endTime')) {
                obj['endTime'] = ApiClient.convertToType(data['endTime'], 'Date');
            }
            if (data.hasOwnProperty('fieldIds')) {
                obj['fieldIds'] = ApiClient.convertToType(data['fieldIds'], ['String']);
            }
            if (data.hasOwnProperty('id')) {
                obj['id'] = ApiClient.convertToType(data['id'], 'String');
            }
            if (data.hasOwnProperty('location')) {
                obj['location'] = Geometry.constructFromObject(data['location']);
            }
            if (data.hasOwnProperty('locationDisplayColor')) {
                obj['locationDisplayColor'] = ApiClient.convertToType(data['locationDisplayColor'], 'String');
            }
            if (data.hasOwnProperty('note')) {
                obj['note'] = ApiClient.convertToType(data['note'], 'String');
            }
            if (data.hasOwnProperty('startTime')) {
                obj['startTime'] = ApiClient.convertToType(data['startTime'], 'Date');
            }
            if (data.hasOwnProperty('status')) {
                obj['status'] = ApiClient.convertToType(data['status'], 'String');
            }
            if (data.hasOwnProperty('tags')) {
                obj['tags'] = ApiClient.convertToType(data['tags'], [ScoutingTag]);
            }
            if (data.hasOwnProperty('timespan')) {
                obj['timespan'] = ApiClient.convertToType(data['timespan'], 'String');
            }
            if (data.hasOwnProperty('title')) {
                obj['title'] = ApiClient.convertToType(data['title'], 'String');
            }
            if (data.hasOwnProperty('updatedAt')) {
                obj['updatedAt'] = ApiClient.convertToType(data['updatedAt'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>ScoutingObservation</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>ScoutingObservation</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of ScoutingObservation.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['fieldIds'])) {
            throw new Error("Expected the field `fieldIds` to be an array in the JSON data but got " + data['fieldIds']);
        }
        // ensure the json data is a string
        if (data['id'] && !(typeof data['id'] === 'string' || data['id'] instanceof String)) {
            throw new Error("Expected the field `id` to be a primitive type in the JSON string but got " + data['id']);
        }
        // validate the optional field `location`
        if (data['location']) { // data not null
          Geometry.validateJSON(data['location']);
        }
        // ensure the json data is a string
        if (data['locationDisplayColor'] && !(typeof data['locationDisplayColor'] === 'string' || data['locationDisplayColor'] instanceof String)) {
            throw new Error("Expected the field `locationDisplayColor` to be a primitive type in the JSON string but got " + data['locationDisplayColor']);
        }
        // ensure the json data is a string
        if (data['note'] && !(typeof data['note'] === 'string' || data['note'] instanceof String)) {
            throw new Error("Expected the field `note` to be a primitive type in the JSON string but got " + data['note']);
        }
        // ensure the json data is a string
        if (data['status'] && !(typeof data['status'] === 'string' || data['status'] instanceof String)) {
            throw new Error("Expected the field `status` to be a primitive type in the JSON string but got " + data['status']);
        }
        if (data['tags']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['tags'])) {
                throw new Error("Expected the field `tags` to be an array in the JSON data but got " + data['tags']);
            }
            // validate the optional field `tags` (array)
            for (const item of data['tags']) {
                ScoutingTag.validateJSON(item);
            };
        }
        // ensure the json data is a string
        if (data['timespan'] && !(typeof data['timespan'] === 'string' || data['timespan'] instanceof String)) {
            throw new Error("Expected the field `timespan` to be a primitive type in the JSON string but got " + data['timespan']);
        }
        // ensure the json data is a string
        if (data['title'] && !(typeof data['title'] === 'string' || data['title'] instanceof String)) {
            throw new Error("Expected the field `title` to be a primitive type in the JSON string but got " + data['title']);
        }

        return true;
    }


}

ScoutingObservation.RequiredProperties = ["endTime", "fieldIds", "id", "location", "locationDisplayColor", "note", "startTime", "status", "tags", "timespan", "title", "updatedAt"];

/**
 * The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).
 * @member {Date} endTime
 */
ScoutingObservation.prototype['endTime'] = undefined;

/**
 * Array of field ids associated with this observation.
 * @member {Array.<String>} fieldIds
 */
ScoutingObservation.prototype['fieldIds'] = undefined;

/**
 * The id of a scouting observation.
 * @member {String} id
 */
ScoutingObservation.prototype['id'] = undefined;

/**
 * @member {module:model/Geometry} location
 */
ScoutingObservation.prototype['location'] = undefined;

/**
 * Color of scouting pin assigned in the Climate FieldView app. Limited in the Ux to a set of RGB values. * #307af7 * #38d753 * #b037e4 * #ef3e3e * #f7ec41 * #ff8439 * #808080 
 * @member {module:model/ScoutingObservation.LocationDisplayColorEnum} locationDisplayColor
 */
ScoutingObservation.prototype['locationDisplayColor'] = undefined;

/**
 * The text of the scouting observation. Maximum of 4000 characters.
 * @member {String} note
 */
ScoutingObservation.prototype['note'] = undefined;

/**
 * The start time of the scouting observation. Time in ISO 8601 format with UTC timezone, 3 fractional seconds (https://tools.ietf.org/html/rfc3339).
 * @member {Date} startTime
 */
ScoutingObservation.prototype['startTime'] = undefined;

/**
 * The status of the scouting observation For example : ACTIVE, DELETED
 * @member {module:model/ScoutingObservation.StatusEnum} status
 */
ScoutingObservation.prototype['status'] = undefined;

/**
 * For example, ROCK_STONE, PONDING_WET, HAIL Maximum 20 tags allowed, 40 characters per tag.
 * @member {Array.<module:model/ScoutingTag>} tags
 */
ScoutingObservation.prototype['tags'] = undefined;

/**
 * Permanent or seasonal
 * @member {module:model/ScoutingObservation.TimespanEnum} timespan
 */
ScoutingObservation.prototype['timespan'] = undefined;

/**
 * The title or summary of the scouting observation. 40 Characters long, no emojis, and leading and trailing whitespace will be trimmed.
 * @member {String} title
 */
ScoutingObservation.prototype['title'] = undefined;

/**
 * The time the scouting observation or any of its attachments was last updated.Time in ISO 8601 format with UTC timezone, 3 fractional seconds. (https://tools.ietf.org/html/rfc3339).
 * @member {Date} updatedAt
 */
ScoutingObservation.prototype['updatedAt'] = undefined;





/**
 * Allowed values for the <code>locationDisplayColor</code> property.
 * @enum {String}
 * @readonly
 */
ScoutingObservation['LocationDisplayColorEnum'] = {

    /**
     * value: "#307af7"
     * @const
     */
    "307af7": "#307af7",

    /**
     * value: "#38d753"
     * @const
     */
    "38d753": "#38d753",

    /**
     * value: "#b037e4"
     * @const
     */
    "b037e4": "#b037e4",

    /**
     * value: "#ef3e3e"
     * @const
     */
    "ef3e3e": "#ef3e3e",

    /**
     * value: "#f7ec41"
     * @const
     */
    "f7ec41": "#f7ec41",

    /**
     * value: "#ff8439"
     * @const
     */
    "ff8439": "#ff8439",

    /**
     * value: "#808080"
     * @const
     */
    "808080": "#808080"
};


/**
 * Allowed values for the <code>status</code> property.
 * @enum {String}
 * @readonly
 */
ScoutingObservation['StatusEnum'] = {

    /**
     * value: "ACTIVE"
     * @const
     */
    "ACTIVE": "ACTIVE",

    /**
     * value: "DELETED"
     * @const
     */
    "DELETED": "DELETED"
};


/**
 * Allowed values for the <code>timespan</code> property.
 * @enum {String}
 * @readonly
 */
ScoutingObservation['TimespanEnum'] = {

    /**
     * value: "PERMANENT"
     * @const
     */
    "PERMANENT": "PERMANENT",

    /**
     * value: "SEASONAL"
     * @const
     */
    "SEASONAL": "SEASONAL"
};



export default ScoutingObservation;

