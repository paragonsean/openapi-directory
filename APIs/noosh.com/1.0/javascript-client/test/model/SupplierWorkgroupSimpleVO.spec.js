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
    instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
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

  describe('SupplierWorkgroupSimpleVO', function() {
    it('should create an instance of SupplierWorkgroupSimpleVO', function() {
      // uncomment below and update the code to test SupplierWorkgroupSimpleVO
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be.a(NooshApiApplication.SupplierWorkgroupSimpleVO);
    });

    it('should have the property buSupplierWorkgroupId (base name: "bu_supplier_workgroup_id")', function() {
      // uncomment below and update the code to test the property buSupplierWorkgroupId
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property buSupplierWorkgroupName (base name: "bu_supplier_workgroup_name")', function() {
      // uncomment below and update the code to test the property buSupplierWorkgroupName
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property clientWorkgroupId (base name: "client_workgroup_id")', function() {
      // uncomment below and update the code to test the property clientWorkgroupId
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property clientWorkgroupName (base name: "client_workgroup_name")', function() {
      // uncomment below and update the code to test the property clientWorkgroupName
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property isApproved (base name: "is_approved")', function() {
      // uncomment below and update the code to test the property isApproved
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property supplierCode (base name: "supplier_code")', function() {
      // uncomment below and update the code to test the property supplierCode
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property supplierWorkgroupId (base name: "supplier_workgroup_id")', function() {
      // uncomment below and update the code to test the property supplierWorkgroupId
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

    it('should have the property supplierWorkgroupName (base name: "supplier_workgroup_name")', function() {
      // uncomment below and update the code to test the property supplierWorkgroupName
      //var instance = new NooshApiApplication.SupplierWorkgroupSimpleVO();
      //expect(instance).to.be();
    });

  });

}));
