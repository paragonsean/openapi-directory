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
    instance = new SwaggerApi2Cart.BasketLiveShippingService();
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

  describe('BasketLiveShippingService', function() {
    it('should create an instance of BasketLiveShippingService', function() {
      // uncomment below and update the code to test BasketLiveShippingService
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be.a(SwaggerApi2Cart.BasketLiveShippingService);
    });

    it('should have the property additionalFields (base name: "additional_fields")', function() {
      // uncomment below and update the code to test the property additionalFields
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

    it('should have the property callback (base name: "callback")', function() {
      // uncomment below and update the code to test the property callback
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

    it('should have the property callbackErrCnt (base name: "callback_err_cnt")', function() {
      // uncomment below and update the code to test the property callbackErrCnt
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

    it('should have the property customFields (base name: "custom_fields")', function() {
      // uncomment below and update the code to test the property customFields
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

    it('should have the property enabledOnStore (base name: "enabled_on_store")', function() {
      // uncomment below and update the code to test the property enabledOnStore
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

    it('should have the property name (base name: "name")', function() {
      // uncomment below and update the code to test the property name
      //var instance = new SwaggerApi2Cart.BasketLiveShippingService();
      //expect(instance).to.be();
    });

  });

}));
