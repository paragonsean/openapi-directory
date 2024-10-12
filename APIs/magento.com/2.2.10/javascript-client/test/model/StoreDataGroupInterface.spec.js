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
    instance = new MagentoB2B.StoreDataGroupInterface();
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

  describe('StoreDataGroupInterface', function() {
    it('should create an instance of StoreDataGroupInterface', function() {
      // uncomment below and update the code to test StoreDataGroupInterface
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be.a(MagentoB2B.StoreDataGroupInterface);
    });

    it('should have the property code (base name: "code")', function() {
      // uncomment below and update the code to test the property code
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

    it('should have the property defaultStoreId (base name: "default_store_id")', function() {
      // uncomment below and update the code to test the property defaultStoreId
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

    it('should have the property rootCategoryId (base name: "root_category_id")', function() {
      // uncomment below and update the code to test the property rootCategoryId
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

    it('should have the property websiteId (base name: "website_id")', function() {
      // uncomment below and update the code to test the property websiteId
      //var instance = new MagentoB2B.StoreDataGroupInterface();
      //expect(instance).to.be();
    });

  });

}));
