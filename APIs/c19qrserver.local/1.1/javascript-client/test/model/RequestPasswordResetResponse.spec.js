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
    instance = new ApiForTheCovid19TrackingQrCodeSigninServer.RequestPasswordResetResponse();
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

  describe('RequestPasswordResetResponse', function() {
    it('should create an instance of RequestPasswordResetResponse', function() {
      // uncomment below and update the code to test RequestPasswordResetResponse
      //var instance = new ApiForTheCovid19TrackingQrCodeSigninServer.RequestPasswordResetResponse();
      //expect(instance).to.be.a(ApiForTheCovid19TrackingQrCodeSigninServer.RequestPasswordResetResponse);
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new ApiForTheCovid19TrackingQrCodeSigninServer.RequestPasswordResetResponse();
      //expect(instance).to.be();
    });

    it('should have the property guid (base name: "guid")', function() {
      // uncomment below and update the code to test the property guid
      //var instance = new ApiForTheCovid19TrackingQrCodeSigninServer.RequestPasswordResetResponse();
      //expect(instance).to.be();
    });

  });

}));
