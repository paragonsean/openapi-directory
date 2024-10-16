/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.Thread();
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

  describe('Thread', function() {
    it('should create an instance of Thread', function() {
      // uncomment below and update the code to test Thread
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be.a(AppCenterClient.Thread);
    });

    it('should have the property crashed (base name: "crashed")', function() {
      // uncomment below and update the code to test the property crashed
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be();
    });

    it('should have the property exception (base name: "exception")', function() {
      // uncomment below and update the code to test the property exception
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be();
    });

    it('should have the property frames (base name: "frames")', function() {
      // uncomment below and update the code to test the property frames
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be();
    });

    it('should have the property platform (base name: "platform")', function() {
      // uncomment below and update the code to test the property platform
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be();
    });

    it('should have the property relevant (base name: "relevant")', function() {
      // uncomment below and update the code to test the property relevant
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new AppCenterClient.Thread();
      //expect(instance).to.be();
    });

  });

}));
