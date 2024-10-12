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
    instance = new MagentoB2B.CatalogDataProductRenderInterface();
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

  describe('CatalogDataProductRenderInterface', function() {
    it('should create an instance of CatalogDataProductRenderInterface', function() {
      // uncomment below and update the code to test CatalogDataProductRenderInterface
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be.a(MagentoB2B.CatalogDataProductRenderInterface);
    });

    it('should have the property addToCartButton (base name: "add_to_cart_button")', function() {
      // uncomment below and update the code to test the property addToCartButton
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property addToCompareButton (base name: "add_to_compare_button")', function() {
      // uncomment below and update the code to test the property addToCompareButton
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property currencyCode (base name: "currency_code")', function() {
      // uncomment below and update the code to test the property currencyCode
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property images (base name: "images")', function() {
      // uncomment below and update the code to test the property images
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property isSalable (base name: "is_salable")', function() {
      // uncomment below and update the code to test the property isSalable
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property priceInfo (base name: "price_info")', function() {
      // uncomment below and update the code to test the property priceInfo
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property storeId (base name: "store_id")', function() {
      // uncomment below and update the code to test the property storeId
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new MagentoB2B.CatalogDataProductRenderInterface();
      //expect(instance).to.be();
    });

  });

}));
