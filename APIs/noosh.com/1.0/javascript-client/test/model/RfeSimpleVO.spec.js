/**
 * Noosh API application
 * Full description of Noosh API
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.NooshApiApplication);
  }
}(this, function(expect, NooshApiApplication) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new NooshApiApplication.RfeSimpleVO();
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

  describe('RfeSimpleVO', function() {
    it('should create an instance of RfeSimpleVO', function() {
      // uncomment below and update the code to test RfeSimpleVO
      //var instance = new NooshApiApplication.RfeSimpleVO();
      //expect(instance).to.be.a(NooshApiApplication.RfeSimpleVO);
    });

    it('should have the property estimateDueDate (base name: "estimate_due_date")', function() {
      // uncomment below and update the code to test the property estimateDueDate
      //var instance = new NooshApiApplication.RfeSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property rfeId (base name: "rfe_id")', function() {
      // uncomment below and update the code to test the property rfeId
      //var instance = new NooshApiApplication.RfeSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property rfeItems (base name: "rfe_items")', function() {
      // uncomment below and update the code to test the property rfeItems
      //var instance = new NooshApiApplication.RfeSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property rfeTitle (base name: "rfe_title")', function() {
      // uncomment below and update the code to test the property rfeTitle
      //var instance = new NooshApiApplication.RfeSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property supplierEstimates (base name: "supplier_estimates")', function() {
      // uncomment below and update the code to test the property supplierEstimates
      //var instance = new NooshApiApplication.RfeSimpleVO();
      //expect(instance).to.be();
    });

  });

}));
