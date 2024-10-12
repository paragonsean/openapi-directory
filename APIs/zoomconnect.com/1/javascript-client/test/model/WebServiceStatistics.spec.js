/**
 * www.zoomconnect.com
 * The world's greatest SMS API
 *
 * The version of the OpenAPI document: 1
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
    factory(root.expect, root.WwwZoomconnectCom);
  }
}(this, function(expect, WwwZoomconnectCom) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new WwwZoomconnectCom.WebServiceStatistics();
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

  describe('WebServiceStatistics', function() {
    it('should create an instance of WebServiceStatistics', function() {
      // uncomment below and update the code to test WebServiceStatistics
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be.a(WwwZoomconnectCom.WebServiceStatistics);
    });

    it('should have the property delivered (base name: "delivered")', function() {
      // uncomment below and update the code to test the property delivered
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be();
    });

    it('should have the property failed (base name: "failed")', function() {
      // uncomment below and update the code to test the property failed
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be();
    });

    it('should have the property failedOptout (base name: "failedOptout")', function() {
      // uncomment below and update the code to test the property failedOptout
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be();
    });

    it('should have the property failedRefunded (base name: "failedRefunded")', function() {
      // uncomment below and update the code to test the property failedRefunded
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be();
    });

    it('should have the property sent (base name: "sent")', function() {
      // uncomment below and update the code to test the property sent
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be();
    });

    it('should have the property total (base name: "total")', function() {
      // uncomment below and update the code to test the property total
      //var instance = new WwwZoomconnectCom.WebServiceStatistics();
      //expect(instance).to.be();
    });

  });

}));
