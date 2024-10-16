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
    instance = new CallFireApiDocumentation.GoogleAnalytics();
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

  describe('GoogleAnalytics', function() {
    it('should create an instance of GoogleAnalytics', function() {
      // uncomment below and update the code to test GoogleAnalytics
      //var instance = new CallFireApiDocumentation.GoogleAnalytics();
      //expect(instance).to.be.a(CallFireApiDocumentation.GoogleAnalytics);
    });

    it('should have the property category (base name: "category")', function() {
      // uncomment below and update the code to test the property category
      //var instance = new CallFireApiDocumentation.GoogleAnalytics();
      //expect(instance).to.be();
    });

    it('should have the property domain (base name: "domain")', function() {
      // uncomment below and update the code to test the property domain
      //var instance = new CallFireApiDocumentation.GoogleAnalytics();
      //expect(instance).to.be();
    });

    it('should have the property googleAccountId (base name: "googleAccountId")', function() {
      // uncomment below and update the code to test the property googleAccountId
      //var instance = new CallFireApiDocumentation.GoogleAnalytics();
      //expect(instance).to.be();
    });

  });

}));
