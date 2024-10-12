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
    instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
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

  describe('CatalogDataCategoryTreeInterface', function() {
    it('should create an instance of CatalogDataCategoryTreeInterface', function() {
      // uncomment below and update the code to test CatalogDataCategoryTreeInterface
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be.a(MagentoB2B.CatalogDataCategoryTreeInterface);
    });

    it('should have the property childrenData (base name: "children_data")', function() {
      // uncomment below and update the code to test the property childrenData
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isActive (base name: "is_active")', function() {
      // uncomment below and update the code to test the property isActive
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property level (base name: "level")', function() {
      // uncomment below and update the code to test the property level
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property parentId (base name: "parent_id")', function() {
      // uncomment below and update the code to test the property parentId
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

    it('should have the property productCount (base name: "product_count")', function() {
      // uncomment below and update the code to test the property productCount
      //var instance = new MagentoB2B.CatalogDataCategoryTreeInterface();
      //expect(instance).to.be();
    });

  });

}));
