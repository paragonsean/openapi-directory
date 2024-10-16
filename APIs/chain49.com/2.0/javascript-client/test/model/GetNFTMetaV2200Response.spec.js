/**
 * Chain49 API
 * Kickstart your next crypto project - extended trezor/blockbook API with 10+ blockchains available instantly and 50+ possible on request running on the finest hardware in Germany's best datacenters at Hetzner  Websocket only via api.chain49.com endpoint possible (RapidAPI does not support it yet)
 *
 * The version of the OpenAPI document: 2.0
 * Contact: contact@chain49.com
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
    factory(root.expect, root.Chain49Api);
  }
}(this, function(expect, Chain49Api) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Chain49Api.GetNFTMetaV2200Response();
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

  describe('GetNFTMetaV2200Response', function() {
    it('should create an instance of GetNFTMetaV2200Response', function() {
      // uncomment below and update the code to test GetNFTMetaV2200Response
      //var instance = new Chain49Api.GetNFTMetaV2200Response();
      //expect(instance).to.be.a(Chain49Api.GetNFTMetaV2200Response);
    });

    it('should have the property contractInfo (base name: "contractInfo")', function() {
      // uncomment below and update the code to test the property contractInfo
      //var instance = new Chain49Api.GetNFTMetaV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property tokenId (base name: "tokenId")', function() {
      // uncomment below and update the code to test the property tokenId
      //var instance = new Chain49Api.GetNFTMetaV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property uri (base name: "uri")', function() {
      // uncomment below and update the code to test the property uri
      //var instance = new Chain49Api.GetNFTMetaV2200Response();
      //expect(instance).to.be();
    });

  });

}));
