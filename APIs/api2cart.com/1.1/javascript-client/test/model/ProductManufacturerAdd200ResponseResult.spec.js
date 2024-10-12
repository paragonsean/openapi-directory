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
    instance = new SwaggerApi2Cart.ProductManufacturerAdd200ResponseResult();
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

  describe('ProductManufacturerAdd200ResponseResult', function() {
    it('should create an instance of ProductManufacturerAdd200ResponseResult', function() {
      // uncomment below and update the code to test ProductManufacturerAdd200ResponseResult
      //var instance = new SwaggerApi2Cart.ProductManufacturerAdd200ResponseResult();
      //expect(instance).to.be.a(SwaggerApi2Cart.ProductManufacturerAdd200ResponseResult);
    });

    it('should have the property manufacturerId (base name: "manufacturer_id")', function() {
      // uncomment below and update the code to test the property manufacturerId
      //var instance = new SwaggerApi2Cart.ProductManufacturerAdd200ResponseResult();
      //expect(instance).to.be();
    });

  });

}));
