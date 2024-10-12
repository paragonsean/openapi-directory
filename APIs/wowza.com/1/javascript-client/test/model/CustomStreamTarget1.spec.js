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
    instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
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

  describe('CustomStreamTarget1', function() {
    it('should create an instance of CustomStreamTarget1', function() {
      // uncomment below and update the code to test CustomStreamTarget1
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be.a(WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1);
    });

    it('should have the property enableHls (base name: "enable_hls")', function() {
      // uncomment below and update the code to test the property enableHls
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property enabled (base name: "enabled")', function() {
      // uncomment below and update the code to test the property enabled
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property ingestIpWhitelist (base name: "ingest_ip_whitelist")', function() {
      // uncomment below and update the code to test the property ingestIpWhitelist
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property provider (base name: "provider")', function() {
      // uncomment below and update the code to test the property provider
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property regionOverride (base name: "region_override")', function() {
      // uncomment below and update the code to test the property regionOverride
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property sourceDeliveryMethod (base name: "source_delivery_method")', function() {
      // uncomment below and update the code to test the property sourceDeliveryMethod
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property sourceUrl (base name: "source_url")', function() {
      // uncomment below and update the code to test the property sourceUrl
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new WowzaStreamingCloudRestApiReferenceDocumentation.CustomStreamTarget1();
      //expect(instance).to.be();
    });

  });

}));
