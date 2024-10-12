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
    instance = new SwaggerApi2Cart.ProductChildItemFind200Response();
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

  describe('ProductChildItemFind200Response', function() {
    it('should create an instance of ProductChildItemFind200Response', function() {
      // uncomment below and update the code to test ProductChildItemFind200Response
      //var instance = new SwaggerApi2Cart.ProductChildItemFind200Response();
      //expect(instance).to.be.a(SwaggerApi2Cart.ProductChildItemFind200Response);
    });

    it('should have the property result (base name: "result")', function() {
      // uncomment below and update the code to test the property result
      //var instance = new SwaggerApi2Cart.ProductChildItemFind200Response();
      //expect(instance).to.be();
    });

    it('should have the property returnCode (base name: "return_code")', function() {
      // uncomment below and update the code to test the property returnCode
      //var instance = new SwaggerApi2Cart.ProductChildItemFind200Response();
      //expect(instance).to.be();
    });

    it('should have the property returnMessage (base name: "return_message")', function() {
      // uncomment below and update the code to test the property returnMessage
      //var instance = new SwaggerApi2Cart.ProductChildItemFind200Response();
      //expect(instance).to.be();
    });

  });

}));
