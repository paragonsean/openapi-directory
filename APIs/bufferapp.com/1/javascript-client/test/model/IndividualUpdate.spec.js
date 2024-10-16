/**
 * Bufferapp
 * Social media management for marketers and agencies
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
    factory(root.expect, root.Bufferapp);
  }
}(this, function(expect, Bufferapp) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new Bufferapp.IndividualUpdate();
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

  describe('IndividualUpdate', function() {
    it('should create an instance of IndividualUpdate', function() {
      // uncomment below and update the code to test IndividualUpdate
      //var instance = new Bufferapp.IndividualUpdate();
      //expect(instance).to.be.a(Bufferapp.IndividualUpdate);
    });

    it('should have the property bufferCount (base name: "buffer_count")', function() {
      // uncomment below and update the code to test the property bufferCount
      //var instance = new Bufferapp.IndividualUpdate();
      //expect(instance).to.be();
    });

    it('should have the property bufferPercentage (base name: "buffer_percentage")', function() {
      // uncomment below and update the code to test the property bufferPercentage
      //var instance = new Bufferapp.IndividualUpdate();
      //expect(instance).to.be();
    });

    it('should have the property success (base name: "success")', function() {
      // uncomment below and update the code to test the property success
      //var instance = new Bufferapp.IndividualUpdate();
      //expect(instance).to.be();
    });

    it('should have the property update (base name: "update")', function() {
      // uncomment below and update the code to test the property update
      //var instance = new Bufferapp.IndividualUpdate();
      //expect(instance).to.be();
    });

  });

}));
