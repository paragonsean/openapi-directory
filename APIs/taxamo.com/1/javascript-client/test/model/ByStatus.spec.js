/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
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
    factory(root.expect, root.Taxamo);
  }
}(this, function(expect, Taxamo) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Taxamo.ByStatus();
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

  describe('ByStatus', function() {
    it('should create an instance of ByStatus', function() {
      // uncomment below and update the code to test ByStatus
      //var instance = new Taxamo.ByStatus();
      //expect(instance).to.be.a(Taxamo.ByStatus);
    });

    it('should have the property C (base name: "C")', function() {
      // uncomment below and update the code to test the property C
      //var instance = new Taxamo.ByStatus();
      //expect(instance).to.be();
    });

    it('should have the property N (base name: "N")', function() {
      // uncomment below and update the code to test the property N
      //var instance = new Taxamo.ByStatus();
      //expect(instance).to.be();
    });

  });

}));
