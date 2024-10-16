/**
 * TrapStreet API
 * The TrapStreet API finds trap streets in Google Maps, Bing Maps and OpenStreetMap data.
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.TrapStreetApi);
  }
}(this, function(expect, TrapStreetApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TrapStreetApi.AddressGet200Response();
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

  describe('AddressGet200Response', function() {
    it('should create an instance of AddressGet200Response', function() {
      // uncomment below and update the code to test AddressGet200Response
      //var instance = new TrapStreetApi.AddressGet200Response();
      //expect(instance).to.be.a(TrapStreetApi.AddressGet200Response);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instance = new TrapStreetApi.AddressGet200Response();
      //expect(instance).to.be();
    });

    it('should have the property trap (base name: "trap")', function() {
      // uncomment below and update the code to test the property trap
      //var instance = new TrapStreetApi.AddressGet200Response();
      //expect(instance).to.be();
    });

  });

}));
