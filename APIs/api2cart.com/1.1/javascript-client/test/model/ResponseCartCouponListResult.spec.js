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
    instance = new SwaggerApi2Cart.ResponseCartCouponListResult();
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

  describe('ResponseCartCouponListResult', function() {
    it('should create an instance of ResponseCartCouponListResult', function() {
      // uncomment below and update the code to test ResponseCartCouponListResult
      //var instance = new SwaggerApi2Cart.ResponseCartCouponListResult();
      //expect(instance).to.be.a(SwaggerApi2Cart.ResponseCartCouponListResult);
    });

    it('should have the property additionalFields (base name: "additional_fields")', function() {
      // uncomment below and update the code to test the property additionalFields
      //var instance = new SwaggerApi2Cart.ResponseCartCouponListResult();
      //expect(instance).to.be();
    });

    it('should have the property coupon (base name: "coupon")', function() {
      // uncomment below and update the code to test the property coupon
      //var instance = new SwaggerApi2Cart.ResponseCartCouponListResult();
      //expect(instance).to.be();
    });

    it('should have the property couponCount (base name: "coupon_count")', function() {
      // uncomment below and update the code to test the property couponCount
      //var instance = new SwaggerApi2Cart.ResponseCartCouponListResult();
      //expect(instance).to.be();
    });

    it('should have the property customFields (base name: "custom_fields")', function() {
      // uncomment below and update the code to test the property customFields
      //var instance = new SwaggerApi2Cart.ResponseCartCouponListResult();
      //expect(instance).to.be();
    });

  });

}));
