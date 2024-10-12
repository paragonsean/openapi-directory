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
    instance = new SwaggerApi2Cart.AccountCartAddHybrisWebsitesInner();
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

  describe('AccountCartAddHybrisWebsitesInner', function() {
    it('should create an instance of AccountCartAddHybrisWebsitesInner', function() {
      // uncomment below and update the code to test AccountCartAddHybrisWebsitesInner
      //var instance = new SwaggerApi2Cart.AccountCartAddHybrisWebsitesInner();
      //expect(instance).to.be.a(SwaggerApi2Cart.AccountCartAddHybrisWebsitesInner);
    });

    it('should have the property storeIds (base name: "storeIds")', function() {
      // uncomment below and update the code to test the property storeIds
      //var instance = new SwaggerApi2Cart.AccountCartAddHybrisWebsitesInner();
      //expect(instance).to.be();
    });

    it('should have the property uid (base name: "uid")', function() {
      // uncomment below and update the code to test the property uid
      //var instance = new SwaggerApi2Cart.AccountCartAddHybrisWebsitesInner();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new SwaggerApi2Cart.AccountCartAddHybrisWebsitesInner();
      //expect(instance).to.be();
    });

  });

}));
