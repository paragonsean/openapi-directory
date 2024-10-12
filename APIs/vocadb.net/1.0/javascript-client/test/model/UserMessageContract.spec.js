/**
 * VocaDbWeb
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.VocaDbWeb);
  }
}(this, function(expect, VocaDbWeb) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new VocaDbWeb.UserMessageContract();
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

  describe('UserMessageContract', function() {
    it('should create an instance of UserMessageContract', function() {
      // uncomment below and update the code to test UserMessageContract
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be.a(VocaDbWeb.UserMessageContract);
    });

    it('should have the property body (base name: "body")', function() {
      // uncomment below and update the code to test the property body
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property createdFormatted (base name: "createdFormatted")', function() {
      // uncomment below and update the code to test the property createdFormatted
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property highPriority (base name: "highPriority")', function() {
      // uncomment below and update the code to test the property highPriority
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property inbox (base name: "inbox")', function() {
      // uncomment below and update the code to test the property inbox
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property read (base name: "read")', function() {
      // uncomment below and update the code to test the property read
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property receiver (base name: "receiver")', function() {
      // uncomment below and update the code to test the property receiver
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property sender (base name: "sender")', function() {
      // uncomment below and update the code to test the property sender
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

    it('should have the property subject (base name: "subject")', function() {
      // uncomment below and update the code to test the property subject
      //var instance = new VocaDbWeb.UserMessageContract();
      //expect(instance).to.be();
    });

  });

}));
