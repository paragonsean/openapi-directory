/**
 * nextAuth API
 * API for the nextAuth server
 *
 * The version of the OpenAPI document: 2.2
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
    factory(root.expect, root.NextAuthApi);
  }
}(this, function(expect, NextAuthApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NextAuthApi.TransactionResult();
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

  describe('TransactionResult', function() {
    it('should create an instance of TransactionResult', function() {
      // uncomment below and update the code to test TransactionResult
      //var instance = new NextAuthApi.TransactionResult();
      //expect(instance).to.be.a(NextAuthApi.TransactionResult);
    });

    it('should have the property tstatus (base name: "tstatus")', function() {
      // uncomment below and update the code to test the property tstatus
      //var instance = new NextAuthApi.TransactionResult();
      //expect(instance).to.be();
    });

  });

}));
