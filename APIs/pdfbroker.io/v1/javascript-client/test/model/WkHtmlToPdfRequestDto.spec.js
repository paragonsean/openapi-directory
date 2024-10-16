/**
 * PdfBroker.io API
 * PdfBroker.io is an api for creating pdf files from Xsl-Fo or Html and other useful pdf utilities.
 *
 * The version of the OpenAPI document: v1
 * Contact: support@pdfbroker.io
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
    factory(root.expect, root.PdfBrokerIoApi);
  }
}(this, function(expect, PdfBrokerIoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new PdfBrokerIoApi.WkHtmlToPdfRequestDto();
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

  describe('WkHtmlToPdfRequestDto', function() {
    it('should create an instance of WkHtmlToPdfRequestDto', function() {
      // uncomment below and update the code to test WkHtmlToPdfRequestDto
      //var instance = new PdfBrokerIoApi.WkHtmlToPdfRequestDto();
      //expect(instance).to.be.a(PdfBrokerIoApi.WkHtmlToPdfRequestDto);
    });

    it('should have the property htmlBase64String (base name: "htmlBase64String")', function() {
      // uncomment below and update the code to test the property htmlBase64String
      //var instance = new PdfBrokerIoApi.WkHtmlToPdfRequestDto();
      //expect(instance).to.be();
    });

    it('should have the property resources (base name: "resources")', function() {
      // uncomment below and update the code to test the property resources
      //var instance = new PdfBrokerIoApi.WkHtmlToPdfRequestDto();
      //expect(instance).to.be();
    });

    it('should have the property url (base name: "url")', function() {
      // uncomment below and update the code to test the property url
      //var instance = new PdfBrokerIoApi.WkHtmlToPdfRequestDto();
      //expect(instance).to.be();
    });

    it('should have the property wkHtmlToPdfArguments (base name: "wkHtmlToPdfArguments")', function() {
      // uncomment below and update the code to test the property wkHtmlToPdfArguments
      //var instance = new PdfBrokerIoApi.WkHtmlToPdfRequestDto();
      //expect(instance).to.be();
    });

  });

}));
