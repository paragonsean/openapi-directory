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
 * The CustomStreamTarget1 model module.
 * @module model/CustomStreamTarget1
 * @version 1
 */
class CustomStreamTarget1 {
    /**
     * Constructs a new <code>CustomStreamTarget1</code>.
     * @alias module:model/CustomStreamTarget1
     * @param name {String} A descriptive name for the stream target. Maximum 255 characters.
     * @param sourceDeliveryMethod {String} Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong>. The type of connection between the stream source and the stream target. **push** instructs the source to push the stream to the stream target. **pull** instructs the stream target to pull the stream from the source.
     * @param sourceUrl {String} Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong> and <em>source_delivery_method</em> is **pull**. The URL of a source IP camera or encoder connecting to the stream target.
     */
    constructor(name, sourceDeliveryMethod, sourceUrl) { 
        
        CustomStreamTarget1.initialize(this, name, sourceDeliveryMethod, sourceUrl);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, name, sourceDeliveryMethod, sourceUrl) { 
        obj['name'] = name;
        obj['source_delivery_method'] = sourceDeliveryMethod;
        obj['source_url'] = sourceUrl;
    }

    /**
     * Constructs a <code>CustomStreamTarget1</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/CustomStreamTarget1} obj Optional instance to populate.
     * @return {module:model/CustomStreamTarget1} The populated <code>CustomStreamTarget1</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new CustomStreamTarget1();

            if (data.hasOwnProperty('enable_hls')) {
                obj['enable_hls'] = ApiClient.convertToType(data['enable_hls'], 'Boolean');
            }
            if (data.hasOwnProperty('enabled')) {
                obj['enabled'] = ApiClient.convertToType(data['enabled'], 'Boolean');
            }
            if (data.hasOwnProperty('ingest_ip_whitelist')) {
                obj['ingest_ip_whitelist'] = ApiClient.convertToType(data['ingest_ip_whitelist'], ['String']);
            }
            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('provider')) {
                obj['provider'] = ApiClient.convertToType(data['provider'], 'String');
            }
            if (data.hasOwnProperty('region_override')) {
                obj['region_override'] = ApiClient.convertToType(data['region_override'], 'String');
            }
            if (data.hasOwnProperty('source_delivery_method')) {
                obj['source_delivery_method'] = ApiClient.convertToType(data['source_delivery_method'], 'String');
            }
            if (data.hasOwnProperty('source_url')) {
                obj['source_url'] = ApiClient.convertToType(data['source_url'], 'String');
            }
            if (data.hasOwnProperty('type')) {
                obj['type'] = ApiClient.convertToType(data['type'], 'String');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>CustomStreamTarget1</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>CustomStreamTarget1</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of CustomStreamTarget1.RequiredProperties) {
            if (!data.hasOwnProperty(property)) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is an array
        if (!Array.isArray(data['ingest_ip_whitelist'])) {
            throw new Error("Expected the field `ingest_ip_whitelist` to be an array in the JSON data but got " + data['ingest_ip_whitelist']);
        }
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['provider'] && !(typeof data['provider'] === 'string' || data['provider'] instanceof String)) {
            throw new Error("Expected the field `provider` to be a primitive type in the JSON string but got " + data['provider']);
        }
        // ensure the json data is a string
        if (data['region_override'] && !(typeof data['region_override'] === 'string' || data['region_override'] instanceof String)) {
            throw new Error("Expected the field `region_override` to be a primitive type in the JSON string but got " + data['region_override']);
        }
        // ensure the json data is a string
        if (data['source_delivery_method'] && !(typeof data['source_delivery_method'] === 'string' || data['source_delivery_method'] instanceof String)) {
            throw new Error("Expected the field `source_delivery_method` to be a primitive type in the JSON string but got " + data['source_delivery_method']);
        }
        // ensure the json data is a string
        if (data['source_url'] && !(typeof data['source_url'] === 'string' || data['source_url'] instanceof String)) {
            throw new Error("Expected the field `source_url` to be a primitive type in the JSON string but got " + data['source_url']);
        }
        // ensure the json data is a string
        if (data['type'] && !(typeof data['type'] === 'string' || data['type'] instanceof String)) {
            throw new Error("Expected the field `type` to be a primitive type in the JSON string but got " + data['type']);
        }

        return true;
    }


}

CustomStreamTarget1.RequiredProperties = ["name", "source_delivery_method", "source_url"];

/**
 * Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong>. If <strong>true</strong>, creates an Apple HLS URL for playback on iOS devices (<em>hls_playback_url</em>). The default is <strong>false</strong>.
 * @member {Boolean} enable_hls
 */
CustomStreamTarget1.prototype['enable_hls'] = undefined;

/**
 * Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong>. If <strong>true</strong> (the default), the source stream is ready to be ingested. If **false**, the source stream won't be ingested by the target's origin server.
 * @member {Boolean} enabled
 */
CustomStreamTarget1.prototype['enabled'] = undefined;

/**
 * Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong> and <em>source_delivery_method</em> is **push**. A list of IP addresses that can be used to connect to the target's origin server.
 * @member {Array.<String>} ingest_ip_whitelist
 */
CustomStreamTarget1.prototype['ingest_ip_whitelist'] = undefined;

/**
 * A descriptive name for the stream target. Maximum 255 characters.
 * @member {String} name
 */
CustomStreamTarget1.prototype['name'] = undefined;

/**
 * The CDN for the target. <br /><br />Required for targets whose <em>type</em> is <strong>CustomStreamTarget</strong>. Valid values for <strong>CustomStreamTarget</strong> are <strong>akamai</strong>, <strong>akamai_cupertino</strong>, <strong>akamai_rtmp</strong>, <strong>limelight</strong>, <strong>rtmp</strong>, and <strong>ustream</strong>. Values can be appended with **_mock** to use in the sandbox environment. <br /><br />Valid values for <strong>WowzaStreamTarget</strong> are <strong>akamai</strong>, <strong>akamai_cupertino</strong> (default), <strong>akamai_legacy_rtmp</strong>, and <strong>wowza</strong>. <br /><br /><strong>UltraLowLatencyStreamTarget</strong> defaults to and must be <strong>wowza</strong>.
 * @member {String} provider
 */
CustomStreamTarget1.prototype['provider'] = undefined;

/**
 * Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong> and <em>source_delivery_method</em> is **pull**. The location of the stream target's origin server. If unspecified, Wowza Streaming Cloud determines the optimal region for the origin server.
 * @member {String} region_override
 */
CustomStreamTarget1.prototype['region_override'] = undefined;

/**
 * Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong>. The type of connection between the stream source and the stream target. **push** instructs the source to push the stream to the stream target. **pull** instructs the stream target to pull the stream from the source.
 * @member {String} source_delivery_method
 */
CustomStreamTarget1.prototype['source_delivery_method'] = undefined;

/**
 * Only for targets whose <em>type</em> is <strong>UltraLowLatencyStreamTarget</strong> and <em>source_delivery_method</em> is **pull**. The URL of a source IP camera or encoder connecting to the stream target.
 * @member {String} source_url
 */
CustomStreamTarget1.prototype['source_url'] = undefined;

/**
 * <strong>WowzaStreamTarget</strong> is a Wowza CDN target. <strong>UltraLowLatencyStreamTarget</strong> is an ultra low latency Wowza stream target. <strong>CustomStreamTarget</strong> (the default) is an external, third-party destination. <!--and <strong>FacebookStreamTarget</strong> (a Facebook Live target).-->
 * @member {String} type
 */
CustomStreamTarget1.prototype['type'] = undefined;






export default CustomStreamTarget1;

