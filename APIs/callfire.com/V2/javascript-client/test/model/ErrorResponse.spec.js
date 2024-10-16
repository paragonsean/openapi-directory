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
    instance = new CallFireApiDocumentation.ErrorResponse();
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

  describe('ErrorResponse', function() {
    it('should create an instance of ErrorResponse', function() {
      // uncomment below and update the code to test ErrorResponse
      //var instance = new CallFireApiDocumentation.ErrorResponse();
      //expect(instance).to.be.a(CallFireApiDocumentation.ErrorResponse);
    });

    it('should have the property developerMessage (base name: "developerMessage")', function() {
      // uncomment below and update the code to test the property developerMessage
      //var instance = new CallFireApiDocumentation.ErrorResponse();
      //expect(instance).to.be();
    });

    it('should have the property helpLink (base name: "helpLink")', function() {
      // uncomment below and update the code to test the property helpLink
      //var instance = new CallFireApiDocumentation.ErrorResponse();
      //expect(instance).to.be();
    });

    it('should have the property httpStatusCode (base name: "httpStatusCode")', function() {
      // uncomment below and update the code to test the property httpStatusCode
      //var instance = new CallFireApiDocumentation.ErrorResponse();
      //expect(instance).to.be();
    });

    it('should have the property internalCode (base name: "internalCode")', function() {
      // uncomment below and update the code to test the property internalCode
      //var instance = new CallFireApiDocumentation.ErrorResponse();
      //expect(instance).to.be();
    });

    it('should have the property message (base name: "message")', function() {
      // uncomment below and update the code to test the property message
      //var instance = new CallFireApiDocumentation.ErrorResponse();
      //expect(instance).to.be();
    });

  });

}));
