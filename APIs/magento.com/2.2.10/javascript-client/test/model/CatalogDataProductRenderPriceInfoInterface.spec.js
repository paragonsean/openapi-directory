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
    instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
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

  describe('CatalogDataProductRenderPriceInfoInterface', function() {
    it('should create an instance of CatalogDataProductRenderPriceInfoInterface', function() {
      // uncomment below and update the code to test CatalogDataProductRenderPriceInfoInterface
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be.a(MagentoB2B.CatalogDataProductRenderPriceInfoInterface);
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property finalPrice (base name: "final_price")', function() {
      // uncomment below and update the code to test the property finalPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property formattedPrices (base name: "formatted_prices")', function() {
      // uncomment below and update the code to test the property formattedPrices
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property maxPrice (base name: "max_price")', function() {
      // uncomment below and update the code to test the property maxPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property maxRegularPrice (base name: "max_regular_price")', function() {
      // uncomment below and update the code to test the property maxRegularPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property minimalPrice (base name: "minimal_price")', function() {
      // uncomment below and update the code to test the property minimalPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property minimalRegularPrice (base name: "minimal_regular_price")', function() {
      // uncomment below and update the code to test the property minimalRegularPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property regularPrice (base name: "regular_price")', function() {
      // uncomment below and update the code to test the property regularPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

    it('should have the property specialPrice (base name: "special_price")', function() {
      // uncomment below and update the code to test the property specialPrice
      //var instance = new MagentoB2B.CatalogDataProductRenderPriceInfoInterface();
      //expect(instance).to.be();
    });

  });

}));
