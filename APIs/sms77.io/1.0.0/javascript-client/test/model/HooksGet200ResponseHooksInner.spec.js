/**
 * seven.io API
 * seven.io Swagger API. Get your API-Key now at seven.io.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@seven.io
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
    factory(root.expect, root.SevenIoApi);
  }
}(this, function(expect, SevenIoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SevenIoApi.HooksGet200ResponseHooksInner();
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

  describe('HooksGet200ResponseHooksInner', function() {
    it('should create an instance of HooksGet200ResponseHooksInner', function() {
      // uncomment below and update the code to test HooksGet200ResponseHooksInner
      //var instance = new SevenIoApi.HooksGet200ResponseHooksInner();
      //expect(instance).to.be.a(SevenIoApi.HooksGet200ResponseHooksInner);
    });

    it('should have the property created (base name: "created")', function() {
      // uncomment below and update the code to test the property created
      //var instance = new SevenIoApi.HooksGet200ResponseHooksInner();
      //expect(instance).to.be();
    });

    it('should have the property eventType (base name: "event_type")', function() {
      // uncomment below and update the code to test the property eventType
      //var instance = new SevenIoApi.HooksGet200ResponseHooksInner();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new SevenIoApi.HooksGet200ResponseHooksInner();
      //expect(instance).to.be();
    });

    it('should have the property requestMethod (base name: "request_method")', function() {
      // uncomment below and update the code to test the property requestMethod
      //var instance = new SevenIoApi.HooksGet200ResponseHooksInner();
      //expect(instance).to.be();
    });

    it('should have the property targetUrl (base name: "target_url")', function() {
      // uncomment below and update the code to test the property targetUrl
      //var instance = new SevenIoApi.HooksGet200ResponseHooksInner();
      //expect(instance).to.be();
    });

  });

}));
