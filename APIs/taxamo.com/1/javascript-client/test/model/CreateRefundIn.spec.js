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
    instance = new Taxamo.CreateRefundIn();
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

  describe('CreateRefundIn', function() {
    it('should create an instance of CreateRefundIn', function() {
      // uncomment below and update the code to test CreateRefundIn
      //var instance = new Taxamo.CreateRefundIn();
      //expect(instance).to.be.a(Taxamo.CreateRefundIn);
    });

    it('should have the property amount (base name: "amount")', function() {
      // uncomment below and update the code to test the property amount
      //var instance = new Taxamo.CreateRefundIn();
      //expect(instance).to.be();
    });

    it('should have the property customId (base name: "custom_id")', function() {
      // uncomment below and update the code to test the property customId
      //var instance = new Taxamo.CreateRefundIn();
      //expect(instance).to.be();
    });

    it('should have the property lineKey (base name: "line_key")', function() {
      // uncomment below and update the code to test the property lineKey
      //var instance = new Taxamo.CreateRefundIn();
      //expect(instance).to.be();
    });

    it('should have the property refundReason (base name: "refund_reason")', function() {
      // uncomment below and update the code to test the property refundReason
      //var instance = new Taxamo.CreateRefundIn();
      //expect(instance).to.be();
    });

    it('should have the property totalAmount (base name: "total_amount")', function() {
      // uncomment below and update the code to test the property totalAmount
      //var instance = new Taxamo.CreateRefundIn();
      //expect(instance).to.be();
    });

  });

}));
