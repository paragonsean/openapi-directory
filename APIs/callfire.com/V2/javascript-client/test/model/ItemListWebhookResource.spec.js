/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
    factory(root.expect, root.CallFireApiDocumentation);
  }
}(this, function(expect, CallFireApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CallFireApiDocumentation.ItemListWebhookResource();
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

  describe('ItemListWebhookResource', function() {
    it('should create an instance of ItemListWebhookResource', function() {
      // uncomment below and update the code to test ItemListWebhookResource
      //var instance = new CallFireApiDocumentation.ItemListWebhookResource();
      //expect(instance).to.be.a(CallFireApiDocumentation.ItemListWebhookResource);
    });

    it('should have the property items (base name: "items")', function() {
      // uncomment below and update the code to test the property items
      //var instance = new CallFireApiDocumentation.ItemListWebhookResource();
      //expect(instance).to.be();
    });

  });

}));
