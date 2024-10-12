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

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.WowzaStreamingCloudRestApiReferenceDocumentation);
  }
}(this, function(expect, WowzaStreamingCloudRestApiReferenceDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('Transcoder', function() {
    it('should create an instance of Transcoder', function() {
      // uncomment below and update the code to test Transcoder
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be.a(WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder);
    });

    it('should have the property applicationName (base name: "application_name")', function() {
      // uncomment below and update the code to test the property applicationName
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property billingMode (base name: "billing_mode")', function() {
      // uncomment below and update the code to test the property billingMode
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property broadcastLocation (base name: "broadcast_location")', function() {
      // uncomment below and update the code to test the property broadcastLocation
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property bufferSize (base name: "buffer_size")', function() {
      // uncomment below and update the code to test the property bufferSize
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property closedCaptionType (base name: "closed_caption_type")', function() {
      // uncomment below and update the code to test the property closedCaptionType
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "created_at")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property deliveryMethod (base name: "delivery_method")', function() {
      // uncomment below and update the code to test the property deliveryMethod
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property deliveryProtocols (base name: "delivery_protocols")', function() {
      // uncomment below and update the code to test the property deliveryProtocols
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property directPlaybackUrls (base name: "direct_playback_urls")', function() {
      // uncomment below and update the code to test the property directPlaybackUrls
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property disableAuthentication (base name: "disable_authentication")', function() {
      // uncomment below and update the code to test the property disableAuthentication
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property domainName (base name: "domain_name")', function() {
      // uncomment below and update the code to test the property domainName
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property idleTimeout (base name: "idle_timeout")', function() {
      // uncomment below and update the code to test the property idleTimeout
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property lowLatency (base name: "low_latency")', function() {
      // uncomment below and update the code to test the property lowLatency
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property outputs (base name: "outputs")', function() {
      // uncomment below and update the code to test the property outputs
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property password (base name: "password")', function() {
      // uncomment below and update the code to test the property password
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property playMaximumConnections (base name: "play_maximum_connections")', function() {
      // uncomment below and update the code to test the property playMaximumConnections
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property protocol (base name: "protocol")', function() {
      // uncomment below and update the code to test the property protocol
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property recording (base name: "recording")', function() {
      // uncomment below and update the code to test the property recording
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property sourcePort (base name: "source_port")', function() {
      // uncomment below and update the code to test the property sourcePort
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property sourceUrl (base name: "source_url")', function() {
      // uncomment below and update the code to test the property sourceUrl
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property streamExtension (base name: "stream_extension")', function() {
      // uncomment below and update the code to test the property streamExtension
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property streamName (base name: "stream_name")', function() {
      // uncomment below and update the code to test the property streamName
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property streamSmoother (base name: "stream_smoother")', function() {
      // uncomment below and update the code to test the property streamSmoother
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property streamSourceId (base name: "stream_source_id")', function() {
      // uncomment below and update the code to test the property streamSourceId
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property suppressStreamTargetStart (base name: "suppress_stream_target_start")', function() {
      // uncomment below and update the code to test the property suppressStreamTargetStart
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property transcoderType (base name: "transcoder_type")', function() {
      // uncomment below and update the code to test the property transcoderType
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property updatedAt (base name: "updated_at")', function() {
      // uncomment below and update the code to test the property updatedAt
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property videoFallback (base name: "video_fallback")', function() {
      // uncomment below and update the code to test the property videoFallback
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property watermark (base name: "watermark")', function() {
      // uncomment below and update the code to test the property watermark
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property watermarkHeight (base name: "watermark_height")', function() {
      // uncomment below and update the code to test the property watermarkHeight
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property watermarkImageUrl (base name: "watermark_image_url")', function() {
      // uncomment below and update the code to test the property watermarkImageUrl
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property watermarkOpacity (base name: "watermark_opacity")', function() {
      // uncomment below and update the code to test the property watermarkOpacity
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property watermarkPosition (base name: "watermark_position")', function() {
      // uncomment below and update the code to test the property watermarkPosition
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

    it('should have the property watermarkWidth (base name: "watermark_width")', function() {
      // uncomment below and update the code to test the property watermarkWidth
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.Transcoder();
      //expect(instance).to.be();
    });

  });

}));
