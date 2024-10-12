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
    instance = new MagentoB2B.BundleDataOptionInterface();
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

  describe('BundleDataOptionInterface', function() {
    it('should create an instance of BundleDataOptionInterface', function() {
      // uncomment below and update the code to test BundleDataOptionInterface
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be.a(MagentoB2B.BundleDataOptionInterface);
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property optionId (base name: "option_id")', function() {
      // uncomment below and update the code to test the property optionId
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property productLinks (base name: "product_links")', function() {
      // uncomment below and update the code to test the property productLinks
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property required (base name: "required")', function() {
      // uncomment below and update the code to test the property required
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property sku (base name: "sku")', function() {
      // uncomment below and update the code to test the property sku
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new MagentoB2B.BundleDataOptionInterface();
      //expect(instance).to.be();
    });

  });

}));
