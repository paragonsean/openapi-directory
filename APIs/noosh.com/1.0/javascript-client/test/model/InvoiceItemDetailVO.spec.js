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
    instance = new NooshApiApplication.InvoiceItemDetailVO();
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

  describe('InvoiceItemDetailVO', function() {
    it('should create an instance of InvoiceItemDetailVO', function() {
      // uncomment below and update the code to test InvoiceItemDetailVO
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be.a(NooshApiApplication.InvoiceItemDetailVO);
    });

    it('should have the property customFields (base name: "custom_fields")', function() {
      // uncomment below and update the code to test the property customFields
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property invoiceItemId (base name: "invoice_item_id")', function() {
      // uncomment below and update the code to test the property invoiceItemId
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property itemCost (base name: "item_cost")', function() {
      // uncomment below and update the code to test the property itemCost
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property itemQuantity (base name: "item_quantity")', function() {
      // uncomment below and update the code to test the property itemQuantity
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property itemShipping (base name: "item_shipping")', function() {
      // uncomment below and update the code to test the property itemShipping
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property itemSubTotal (base name: "item_sub_total")', function() {
      // uncomment below and update the code to test the property itemSubTotal
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property itemTax (base name: "item_tax")', function() {
      // uncomment below and update the code to test the property itemTax
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property jobId (base name: "job_id")', function() {
      // uncomment below and update the code to test the property jobId
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property shipmentId (base name: "shipment_id")', function() {
      // uncomment below and update the code to test the property shipmentId
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property specName (base name: "spec_name")', function() {
      // uncomment below and update the code to test the property specName
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property transactionalItemCost (base name: "transactional_item_cost")', function() {
      // uncomment below and update the code to test the property transactionalItemCost
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property transactionalItemShipping (base name: "transactional_item_shipping")', function() {
      // uncomment below and update the code to test the property transactionalItemShipping
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property transactionalItemSubTotal (base name: "transactional_item_sub_total")', function() {
      // uncomment below and update the code to test the property transactionalItemSubTotal
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

    it('should have the property transactionalItemTax (base name: "transactional_item_tax")', function() {
      // uncomment below and update the code to test the property transactionalItemTax
      //var instance = new NooshApiApplication.InvoiceItemDetailVO();
      //expect(instance).to.be();
    });

  });

}));
