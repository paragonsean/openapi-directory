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
    instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
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

  describe('GiftMessageDataMessageExtensionInterface', function() {
    it('should create an instance of GiftMessageDataMessageExtensionInterface', function() {
      // uncomment below and update the code to test GiftMessageDataMessageExtensionInterface
      //var instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
      //expect(instance).to.be.a(MagentoB2B.GiftMessageDataMessageExtensionInterface);
    });

    it('should have the property entityId (base name: "entity_id")', function() {
      // uncomment below and update the code to test the property entityId
      //var instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
      //expect(instance).to.be();
    });

    it('should have the property entityType (base name: "entity_type")', function() {
      // uncomment below and update the code to test the property entityType
      //var instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
      //expect(instance).to.be();
    });

    it('should have the property wrappingAddPrintedCard (base name: "wrapping_add_printed_card")', function() {
      // uncomment below and update the code to test the property wrappingAddPrintedCard
      //var instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
      //expect(instance).to.be();
    });

    it('should have the property wrappingAllowGiftReceipt (base name: "wrapping_allow_gift_receipt")', function() {
      // uncomment below and update the code to test the property wrappingAllowGiftReceipt
      //var instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
      //expect(instance).to.be();
    });

    it('should have the property wrappingId (base name: "wrapping_id")', function() {
      // uncomment below and update the code to test the property wrappingId
      //var instance = new MagentoB2B.GiftMessageDataMessageExtensionInterface();
      //expect(instance).to.be();
    });

  });

}));
