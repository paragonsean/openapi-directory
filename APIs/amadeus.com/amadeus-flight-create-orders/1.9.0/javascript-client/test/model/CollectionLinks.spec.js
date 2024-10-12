/**
 * Flight Create Orders
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.9.0
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
    factory(root.expect, root.FlightCreateOrders);
  }
}(this, function(expect, FlightCreateOrders) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FlightCreateOrders.CollectionLinks();
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

  describe('CollectionLinks', function() {
    it('should create an instance of CollectionLinks', function() {
      // uncomment below and update the code to test CollectionLinks
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be.a(FlightCreateOrders.CollectionLinks);
    });

    it('should have the property first (base name: "first")', function() {
      // uncomment below and update the code to test the property first
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be();
    });

    it('should have the property last (base name: "last")', function() {
      // uncomment below and update the code to test the property last
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be();
    });

    it('should have the property next (base name: "next")', function() {
      // uncomment below and update the code to test the property next
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be();
    });

    it('should have the property previous (base name: "previous")', function() {
      // uncomment below and update the code to test the property previous
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be();
    });

    it('should have the property self (base name: "self")', function() {
      // uncomment below and update the code to test the property self
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be();
    });

    it('should have the property up (base name: "up")', function() {
      // uncomment below and update the code to test the property up
      //var instance = new FlightCreateOrders.CollectionLinks();
      //expect(instance).to.be();
    });

  });

}));
