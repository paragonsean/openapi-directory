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
    instance = new ZalandoShop.ErrorDetail();
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

  describe('ErrorDetail', function() {
    it('should create an instance of ErrorDetail', function() {
      // uncomment below and update the code to test ErrorDetail
      //var instance = new ZalandoShop.ErrorDetail();
      //expect(instance).to.be.a(ZalandoShop.ErrorDetail);
    });

    it('should have the property invalidName (base name: "invalidName")', function() {
      // uncomment below and update the code to test the property invalidName
      //var instance = new ZalandoShop.ErrorDetail();
      //expect(instance).to.be();
    });

    it('should have the property invalidValues (base name: "invalidValues")', function() {
      // uncomment below and update the code to test the property invalidValues
      //var instance = new ZalandoShop.ErrorDetail();
      //expect(instance).to.be();
    });

    it('should have the property key (base name: "key")', function() {
      // uncomment below and update the code to test the property key
      //var instance = new ZalandoShop.ErrorDetail();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new ZalandoShop.ErrorDetail();
      //expect(instance).to.be();
    });

    it('should have the property value (base name: "value")', function() {
      // uncomment below and update the code to test the property value
      //var instance = new ZalandoShop.ErrorDetail();
      //expect(instance).to.be();
    });

  });

}));
