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
    instance = new NooshApiApplication.ShipmentRequestBaseVO();
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

  describe('ShipmentRequestBaseVO', function() {
    it('should create an instance of ShipmentRequestBaseVO', function() {
      // uncomment below and update the code to test ShipmentRequestBaseVO
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be.a(NooshApiApplication.ShipmentRequestBaseVO);
    });

    it('should have the property city (base name: "city")', function() {
      // uncomment below and update the code to test the property city
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property companyName (base name: "company_name")', function() {
      // uncomment below and update the code to test the property companyName
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property country (base name: "country")', function() {
      // uncomment below and update the code to test the property country
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property countryCode (base name: "country_code")', function() {
      // uncomment below and update the code to test the property countryCode
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property customFields (base name: "custom_fields")', function() {
      // uncomment below and update the code to test the property customFields
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property descriptionOrTitle (base name: "description_or_title")', function() {
      // uncomment below and update the code to test the property descriptionOrTitle
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property dueDate (base name: "due_date")', function() {
      // uncomment below and update the code to test the property dueDate
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property firstName (base name: "first_name")', function() {
      // uncomment below and update the code to test the property firstName
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property isUseSpecPackaging (base name: "is_use_spec_packaging")', function() {
      // uncomment below and update the code to test the property isUseSpecPackaging
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property lastName (base name: "last_name")', function() {
      // uncomment below and update the code to test the property lastName
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property line1 (base name: "line_1")', function() {
      // uncomment below and update the code to test the property line1
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property line2 (base name: "line_2")', function() {
      // uncomment below and update the code to test the property line2
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property line3 (base name: "line_3")', function() {
      // uncomment below and update the code to test the property line3
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property locationId (base name: "location_id")', function() {
      // uncomment below and update the code to test the property locationId
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property middleName (base name: "middle_name")', function() {
      // uncomment below and update the code to test the property middleName
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property postal (base name: "postal")', function() {
      // uncomment below and update the code to test the property postal
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property proofType (base name: "proof_type")', function() {
      // uncomment below and update the code to test the property proofType
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property qtyReceived (base name: "qty_received")', function() {
      // uncomment below and update the code to test the property qtyReceived
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property qtyRequested (base name: "qty_requested")', function() {
      // uncomment below and update the code to test the property qtyRequested
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property qtyShipped (base name: "qty_shipped")', function() {
      // uncomment below and update the code to test the property qtyShipped
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property receivedComments (base name: "received_comments")', function() {
      // uncomment below and update the code to test the property receivedComments
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property receivedDate (base name: "received_date")', function() {
      // uncomment below and update the code to test the property receivedDate
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property requestedShippingCarrier (base name: "requested_shipping_carrier")', function() {
      // uncomment below and update the code to test the property requestedShippingCarrier
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property requestedShippingMethod (base name: "requested_shipping_method")', function() {
      // uncomment below and update the code to test the property requestedShippingMethod
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippedComments (base name: "shipped_comments")', function() {
      // uncomment below and update the code to test the property shippedComments
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippedDate (base name: "shipped_date")', function() {
      // uncomment below and update the code to test the property shippedDate
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippedInUnits (base name: "shipped_in_units")', function() {
      // uncomment below and update the code to test the property shippedInUnits
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippedInUofm (base name: "shipped_in_uofm")', function() {
      // uncomment below and update the code to test the property shippedInUofm
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippedShippingCarrier (base name: "shipped_shipping_carrier")', function() {
      // uncomment below and update the code to test the property shippedShippingCarrier
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippedShippingMethod (base name: "shipped_shipping_method")', function() {
      // uncomment below and update the code to test the property shippedShippingMethod
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippingCost (base name: "shipping_cost")', function() {
      // uncomment below and update the code to test the property shippingCost
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property shippingInstruction (base name: "shipping_instruction")', function() {
      // uncomment below and update the code to test the property shippingInstruction
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property state (base name: "state")', function() {
      // uncomment below and update the code to test the property state
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property tax (base name: "tax")', function() {
      // uncomment below and update the code to test the property tax
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property trackingNumber (base name: "tracking_number")', function() {
      // uncomment below and update the code to test the property trackingNumber
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property weight (base name: "weight")', function() {
      // uncomment below and update the code to test the property weight
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property weightUofm (base name: "weight_uofm")', function() {
      // uncomment below and update the code to test the property weightUofm
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property workPhoneNumber (base name: "work_phone_number")', function() {
      // uncomment below and update the code to test the property workPhoneNumber
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

    it('should have the property workgroupName (base name: "workgroup_name")', function() {
      // uncomment below and update the code to test the property workgroupName
      //var instance = new NooshApiApplication.ShipmentRequestBaseVO();
      //expect(instance).to.be();
    });

  });

}));
