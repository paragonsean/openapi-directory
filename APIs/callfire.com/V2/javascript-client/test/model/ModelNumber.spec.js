/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
    factory(root.expect, root.CallFireApiDocumentation);
  }
}(this, function(expect, CallFireApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CallFireApiDocumentation.ModelNumber();
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

  describe('ModelNumber', function() {
    it('should create an instance of ModelNumber', function() {
      // uncomment below and update the code to test ModelNumber
      //var instance = new CallFireApiDocumentation.ModelNumber();
      //expect(instance).to.be.a(CallFireApiDocumentation.ModelNumber);
    });

    it('should have the property nationalFormat (base name: "nationalFormat")', function() {
      // uncomment below and update the code to test the property nationalFormat
      //var instance = new CallFireApiDocumentation.ModelNumber();
      //expect(instance).to.be();
    });

    it('should have the property number (base name: "number")', function() {
      // uncomment below and update the code to test the property number
      //var instance = new CallFireApiDocumentation.ModelNumber();
      //expect(instance).to.be();
    });

    it('should have the property region (base name: "region")', function() {
      // uncomment below and update the code to test the property region
      //var instance = new CallFireApiDocumentation.ModelNumber();
      //expect(instance).to.be();
    });

    it('should have the property sendEmailOnCreate (base name: "sendEmailOnCreate")', function() {
      // uncomment below and update the code to test the property sendEmailOnCreate
      //var instance = new CallFireApiDocumentation.ModelNumber();
      //expect(instance).to.be();
    });

    it('should have the property tollFree (base name: "tollFree")', function() {
      // uncomment below and update the code to test the property tollFree
      //var instance = new CallFireApiDocumentation.ModelNumber();
      //expect(instance).to.be();
    });

  });

}));
