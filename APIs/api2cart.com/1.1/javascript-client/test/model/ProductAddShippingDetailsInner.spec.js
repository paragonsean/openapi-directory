/**
 * Swagger API2Cart
 * API2Cart
 *
 * The version of the OpenAPI document: 1.1
 * Contact: contact@api2cart.com
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
    factory(root.expect, root.SwaggerApi2Cart);
  }
}(this, function(expect, SwaggerApi2Cart) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SwaggerApi2Cart.ProductAddShippingDetailsInner();
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

  describe('ProductAddShippingDetailsInner', function() {
    it('should create an instance of ProductAddShippingDetailsInner', function() {
      // uncomment below and update the code to test ProductAddShippingDetailsInner
      //var instance = new SwaggerApi2Cart.ProductAddShippingDetailsInner();
      //expect(instance).to.be.a(SwaggerApi2Cart.ProductAddShippingDetailsInner);
    });

    it('should have the property shippingCost (base name: "shipping_cost")', function() {
      // uncomment below and update the code to test the property shippingCost
      //var instance = new SwaggerApi2Cart.ProductAddShippingDetailsInner();
      //expect(instance).to.be();
    });

    it('should have the property shippingService (base name: "shipping_service")', function() {
      // uncomment below and update the code to test the property shippingService
      //var instance = new SwaggerApi2Cart.ProductAddShippingDetailsInner();
      //expect(instance).to.be();
    });

    it('should have the property shippingType (base name: "shipping_type")', function() {
      // uncomment below and update the code to test the property shippingType
      //var instance = new SwaggerApi2Cart.ProductAddShippingDetailsInner();
      //expect(instance).to.be();
    });

  });

}));
