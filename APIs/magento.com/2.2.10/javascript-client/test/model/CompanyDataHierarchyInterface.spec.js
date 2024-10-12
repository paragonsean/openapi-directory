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
    instance = new MagentoB2B.CompanyDataHierarchyInterface();
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

  describe('CompanyDataHierarchyInterface', function() {
    it('should create an instance of CompanyDataHierarchyInterface', function() {
      // uncomment below and update the code to test CompanyDataHierarchyInterface
      //var instance = new MagentoB2B.CompanyDataHierarchyInterface();
      //expect(instance).to.be.a(MagentoB2B.CompanyDataHierarchyInterface);
    });

    it('should have the property entityId (base name: "entity_id")', function() {
      // uncomment below and update the code to test the property entityId
      //var instance = new MagentoB2B.CompanyDataHierarchyInterface();
      //expect(instance).to.be();
    });

    it('should have the property entityType (base name: "entity_type")', function() {
      // uncomment below and update the code to test the property entityType
      //var instance = new MagentoB2B.CompanyDataHierarchyInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.CompanyDataHierarchyInterface();
      //expect(instance).to.be();
    });

    it('should have the property structureId (base name: "structure_id")', function() {
      // uncomment below and update the code to test the property structureId
      //var instance = new MagentoB2B.CompanyDataHierarchyInterface();
      //expect(instance).to.be();
    });

    it('should have the property structureParentId (base name: "structure_parent_id")', function() {
      // uncomment below and update the code to test the property structureParentId
      //var instance = new MagentoB2B.CompanyDataHierarchyInterface();
      //expect(instance).to.be();
    });

  });

}));
