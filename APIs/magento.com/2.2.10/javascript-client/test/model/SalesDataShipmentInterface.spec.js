/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.SalesDataShipmentInterface();
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

  describe('SalesDataShipmentInterface', function() {
    it('should create an instance of SalesDataShipmentInterface', function() {
      // uncomment below and update the code to test SalesDataShipmentInterface
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be.a(MagentoB2B.SalesDataShipmentInterface);
    });

    it('should have the property billingAddressId (base name: "billing_address_id")', function() {
      // uncomment below and update the code to test the property billingAddressId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property comments (base name: "comments")', function() {
      // uncomment below and update the code to test the property comments
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "created_at")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property customerId (base name: "customer_id")', function() {
      // uncomment below and update the code to test the property customerId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property emailSent (base name: "email_sent")', function() {
      // uncomment below and update the code to test the property emailSent
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property entityId (base name: "entity_id")', function() {
      // uncomment below and update the code to test the property entityId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property incrementId (base name: "increment_id")', function() {
      // uncomment below and update the code to test the property incrementId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property items (base name: "items")', function() {
      // uncomment below and update the code to test the property items
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property orderId (base name: "order_id")', function() {
      // uncomment below and update the code to test the property orderId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property packages (base name: "packages")', function() {
      // uncomment below and update the code to test the property packages
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property shipmentStatus (base name: "shipment_status")', function() {
      // uncomment below and update the code to test the property shipmentStatus
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property shippingAddressId (base name: "shipping_address_id")', function() {
      // uncomment below and update the code to test the property shippingAddressId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property shippingLabel (base name: "shipping_label")', function() {
      // uncomment below and update the code to test the property shippingLabel
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property storeId (base name: "store_id")', function() {
      // uncomment below and update the code to test the property storeId
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property totalQty (base name: "total_qty")', function() {
      // uncomment below and update the code to test the property totalQty
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property totalWeight (base name: "total_weight")', function() {
      // uncomment below and update the code to test the property totalWeight
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property tracks (base name: "tracks")', function() {
      // uncomment below and update the code to test the property tracks
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

    it('should have the property updatedAt (base name: "updated_at")', function() {
      // uncomment below and update the code to test the property updatedAt
      //var instance = new MagentoB2B.SalesDataShipmentInterface();
      //expect(instance).to.be();
    });

  });

}));
