/**
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
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
    factory(root.expect, root.ZalandoShop);
  }
}(this, function(expect, ZalandoShop) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ZalandoShop.Category();
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

  describe('Category', function() {
    it('should create an instance of Category', function() {
      // uncomment below and update the code to test Category
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be.a(ZalandoShop.Category);
    });

    it('should have the property childKeys (base name: "childKeys")', function() {
      // uncomment below and update the code to test the property childKeys
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property cid (base name: "cid")', function() {
      // uncomment below and update the code to test the property cid
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property hidden (base name: "hidden")', function() {
      // uncomment below and update the code to test the property hidden
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property outlet (base name: "outlet")', function() {
      // uncomment below and update the code to test the property outlet
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property parentKey (base name: "parentKey")', function() {
      // uncomment below and update the code to test the property parentKey
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property suggestedFilters (base name: "suggestedFilters")', function() {
      // uncomment below and update the code to test the property suggestedFilters
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property targetGroup (base name: "targetGroup")', function() {
      // uncomment below and update the code to test the property targetGroup
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new ZalandoShop.Category();
      //expect(instance).to.be();
    });

  });

}));
