/**
 * Wowza Streaming Cloud REST API Reference Documentation
 *  # About the REST API  The Wowza Streaming Cloud<sup>TM</sup> REST API (application programming interface) offers complete programmatic control over live streams, transcoders, stream sources, and stream targets. Anything you can do in the Wowza Streaming Cloud UI can also be achieved by making HTTP-based requests to cloud-based servers through the REST API.  The Wowza Streaming Cloud REST API features *cross-origin resource sharing*, or CORS. CORS is a [W3C specification](https://www.w3.org/TR/cors/) that provides headers in HTTP requests to enable a web server to safely make a network request to another domain.  In order to protect shared resources, the Wowza Streaming Cloud REST API is subject to limits. For details, see [Wowza Streaming Cloud REST API limits](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api-limits). # About this documentation This reference documentation is based on the open-source [Swagger framework](http://swagger.io/specification/). It allows you to view the operations, parameters, and request and reponse schemas for every resource. Request samples are presented in cURL (Shell) and JavaScript; some samples also include just the JSON object. Response samples are all JSON.  For more information and examples on using the Wowza Streaming Cloud REST API, see our [library of Wowza Streaming Cloud REST API technical articles](https://www.wowza.com/docs/wowza-streaming-cloud-rest-api).  # Query requirements The Wowza Streaming Cloud REST API uses HTTP requests to retrieve data from cloud-based servers. Requests must contain proper JSON, two authentication keys, and the correct version number in the base path.  ## JSON The Wowza Streaming Cloud REST API uses the [JSON API specification](http://jsonapi.org/format/) to request and return data. This means requests must include the header `Content-Type: application/json` and must include a single resource object in JSON format as primary data.  Responses include HTTP status codes that indicate whether the query was successful. If there was an error, a description explains the problem so that you can fix it and try again.  ## Authentication Requests to the Wowza Streaming Cloud REST API must be authenticated with two keys: an API key and an access key. Each key is a 64-character alphanumeric string that you can find on the **API Access** page in Wowza Streaming Cloud.  Use the `wsc-api-key` and `wsc-access-key` headers to authenticate requests, like this (in cURL):  ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]' ```  <!-- ReDoc-Inject: <security-definitions> -->  ## Version The Wowza Streaming Cloud API is currently at version 1.0.0. Use `v1` in your base path in every request, like this path to the live_streams endpoint: ``` https://api.cloud.wowza.com/api/v1/live_streams ``` ## Example query Here is a complete example POST request, in cURL, with proper JSON syntax, headers, authentication, and version information: ```bash curl -H 'wsc-api-key: [64-character-api-key-goes-here]' -H 'wsc-access-key: [64-character-access-key-goes-here]'   -H 'Content-Type: application/json' -X POST -d '{     \"live_stream\": {       \"name\": \"My live Stream\",       \"...\": \"...\"     }   }' https://api.cloud.wowza.com/api/v1/live_streams ``` 
 *
 * The version of the OpenAPI document: 1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

import ApiClient from '../ApiClient';

/**
 * The TokenAuth model module.
 * @module model/TokenAuth
 * @version 1
 */
class TokenAuth {
    /**
     * Constructs a new <code>TokenAuth</code>.
     * @alias module:model/TokenAuth
     */
    constructor() { 
        
        TokenAuth.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TokenAuth</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TokenAuth} obj Optional instance to populate.
     * @return {module:model/TokenAuth} The populated <code>TokenAuth</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TokenAuth();

            if (data.hasOwnProperty('created_at')) {
                obj['created_at'] = ApiClient.convertToType(data['created_at'], 'Date');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('stream_target_id')) {
                obj['stream_target_id'] = ApiClient.convertToType(data['stream_target_id'], 'String');
            }
            if (data.hasOwnProperty('trusted_shared_secret')) {
                obj['trusted_shared_secret'] = ApiClient.convertToType(data['trusted_shared_secret'], 'String');
            }
            if (data.hasOwnProperty('updated_at')) {
                obj['updated_at'] = ApiClient.convertToType(data['updated_at'], 'Date');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TokenAuth</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TokenAuth</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['stream_target_id'] && !(typeof data['stream_target_id'] === 'string' || data['stream_target_id'] instanceof String)) {
            throw new Error("Expected the field `stream_target_id` to be a primitive type in the JSON string but got " + data['stream_target_id']);
        }
        // ensure the json data is a string
        if (data['trusted_shared_secret'] && !(typeof data['trusted_shared_secret'] === 'string' || data['trusted_shared_secret'] instanceof String)) {
            throw new Error("Expected the field `trusted_shared_secret` to be a primitive type in the JSON string but got " + data['trusted_shared_secret']);
        }

        return true;
    }


}



/**
 * The date and time that the token authorization was created.
 * @member {Date} created_at
 */
TokenAuth.prototype['created_at'] = undefined;

/**
 * Specify <strong>true</strong> to enable token authorization or <strong>false</strong> to disable.
 * @member {Boolean} enabled
 */
TokenAuth.prototype['enabled'] = undefined;

/**
 * The unique alphanumeric string that identifies the stream target.
 * @member {String} stream_target_id
 */
TokenAuth.prototype['stream_target_id'] = undefined;

/**
 * The trusted shared secret of the token authorization. Must contain only hexadecimal characters and be an even number of total characters not exceeding 32.
 * @member {String} trusted_shared_secret
 */
TokenAuth.prototype['trusted_shared_secret'] = undefined;

/**
 * The date and time that the token authorization was updated.
 * @member {Date} updated_at
 */
TokenAuth.prototype['updated_at'] = undefined;






export default TokenAuth;

