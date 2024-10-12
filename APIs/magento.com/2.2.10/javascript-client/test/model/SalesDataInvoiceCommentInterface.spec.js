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
    instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
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

  describe('SalesDataInvoiceCommentInterface', function() {
    it('should create an instance of SalesDataInvoiceCommentInterface', function() {
      // uncomment below and update the code to test SalesDataInvoiceCommentInterface
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be.a(MagentoB2B.SalesDataInvoiceCommentInterface);
    });

    it('should have the property comment (base name: "comment")', function() {
      // uncomment below and update the code to test the property comment
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

    it('should have the property createdAt (base name: "created_at")', function() {
      // uncomment below and update the code to test the property createdAt
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

    it('should have the property entityId (base name: "entity_id")', function() {
      // uncomment below and update the code to test the property entityId
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

    it('should have the property isCustomerNotified (base name: "is_customer_notified")', function() {
      // uncomment below and update the code to test the property isCustomerNotified
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

    it('should have the property isVisibleOnFront (base name: "is_visible_on_front")', function() {
      // uncomment below and update the code to test the property isVisibleOnFront
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

    it('should have the property parentId (base name: "parent_id")', function() {
      // uncomment below and update the code to test the property parentId
      //var instance = new MagentoB2B.SalesDataInvoiceCommentInterface();
      //expect(instance).to.be();
    });

  });

}));
