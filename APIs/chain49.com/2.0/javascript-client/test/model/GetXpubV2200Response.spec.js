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
    instance = new Chain49Api.GetXpubV2200Response();
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

  describe('GetXpubV2200Response', function() {
    it('should create an instance of GetXpubV2200Response', function() {
      // uncomment below and update the code to test GetXpubV2200Response
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be.a(Chain49Api.GetXpubV2200Response);
    });

    it('should have the property address (base name: "address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property balance (base name: "balance")', function() {
      // uncomment below and update the code to test the property balance
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property itemsOnPage (base name: "itemsOnPage")', function() {
      // uncomment below and update the code to test the property itemsOnPage
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property page (base name: "page")', function() {
      // uncomment below and update the code to test the property page
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property secondaryValue (base name: "secondaryValue")', function() {
      // uncomment below and update the code to test the property secondaryValue
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property tokens (base name: "tokens")', function() {
      // uncomment below and update the code to test the property tokens
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property totalPages (base name: "totalPages")', function() {
      // uncomment below and update the code to test the property totalPages
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property totalReceived (base name: "totalReceived")', function() {
      // uncomment below and update the code to test the property totalReceived
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property totalSent (base name: "totalSent")', function() {
      // uncomment below and update the code to test the property totalSent
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property txids (base name: "txids")', function() {
      // uncomment below and update the code to test the property txids
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property txs (base name: "txs")', function() {
      // uncomment below and update the code to test the property txs
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property unconfirmedBalance (base name: "unconfirmedBalance")', function() {
      // uncomment below and update the code to test the property unconfirmedBalance
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property unconfirmedTxs (base name: "unconfirmedTxs")', function() {
      // uncomment below and update the code to test the property unconfirmedTxs
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

    it('should have the property usedTokens (base name: "usedTokens")', function() {
      // uncomment below and update the code to test the property usedTokens
      //var instance = new Chain49Api.GetXpubV2200Response();
      //expect(instance).to.be();
    });

  });

}));
