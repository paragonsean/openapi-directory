/**
 * reverb
 * reverb
 *
 * The version of the OpenAPI document: 3.0
 * Contact: integrations@reverb.com
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
    factory(root.expect, root.Reverb);
  }
}(this, function(expect, Reverb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Reverb.ShopPutRequest();
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

  describe('ShopPutRequest', function() {
    it('should create an instance of ShopPutRequest', function() {
      // uncomment below and update the code to test ShopPutRequest
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be.a(Reverb.ShopPutRequest);
    });

    it('should have the property address (base name: "address")', function() {
      // uncomment below and update the code to test the property address
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property currency (base name: "currency")', function() {
      // uncomment below and update the code to test the property currency
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property legalCountryCode (base name: "legal_country_code")', function() {
      // uncomment below and update the code to test the property legalCountryCode
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property legalCountryCodeConfirmed (base name: "legal_country_code_confirmed")', function() {
      // uncomment below and update the code to test the property legalCountryCodeConfirmed
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property paymentPolicy (base name: "payment_policy")', function() {
      // uncomment below and update the code to test the property paymentPolicy
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property returnPolicy (base name: "return_policy")', function() {
      // uncomment below and update the code to test the property returnPolicy
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property shippingPolicy (base name: "shipping_policy")', function() {
      // uncomment below and update the code to test the property shippingPolicy
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property shopType (base name: "shop_type")', function() {
      // uncomment below and update the code to test the property shopType
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

    it('should have the property website (base name: "website")', function() {
      // uncomment below and update the code to test the property website
      //var instance = new Reverb.ShopPutRequest();
      //expect(instance).to.be();
    });

  });

}));
