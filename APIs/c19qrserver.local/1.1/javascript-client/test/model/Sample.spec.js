/**
 * API for the COVID-19 Tracking QR Code Signin Server.
 * This is the API for the COVID-19 Contact Tracing QRCode Signin Server
 *
 * The version of the OpenAPI document: 1.1
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
    factory(root.expect, root.ApiForTheCovid19TrackingQrCodeSigninServer);
  }
}(this, function(expect, ApiForTheCovid19TrackingQrCodeSigninServer) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample();
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

  describe('Sample', function() {
    it('should create an instance of Sample', function() {
      // uncomment below and update the code to test Sample
      //var instance = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample();
      //expect(instance).to.be.a(ApiForTheCovid19TrackingQrCodeSigninServer.Sample);
    });

    it('should have the property oldPassword (base name: "old_password")', function() {
      // uncomment below and update the code to test the property oldPassword
      //var instance = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample();
      //expect(instance).to.be();
    });

    it('should have the property password (base name: "password")', function() {
      // uncomment below and update the code to test the property password
      //var instance = new ApiForTheCovid19TrackingQrCodeSigninServer.Sample();
      //expect(instance).to.be();
    });

  });

}));
