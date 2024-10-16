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
    instance = new PdfBrokerIoApi.PdfToImageOptions();
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

  describe('PdfToImageOptions', function() {
    it('should create an instance of PdfToImageOptions', function() {
      // uncomment below and update the code to test PdfToImageOptions
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be.a(PdfBrokerIoApi.PdfToImageOptions);
    });

    it('should have the property height (base name: "height")', function() {
      // uncomment below and update the code to test the property height
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property horizontalResolution (base name: "horizontalResolution")', function() {
      // uncomment below and update the code to test the property horizontalResolution
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property imageFormat (base name: "imageFormat")', function() {
      // uncomment below and update the code to test the property imageFormat
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property jpegQuality (base name: "jpegQuality")', function() {
      // uncomment below and update the code to test the property jpegQuality
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property pageNumber (base name: "pageNumber")', function() {
      // uncomment below and update the code to test the property pageNumber
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property pngCompressionLevel (base name: "pngCompressionLevel")', function() {
      // uncomment below and update the code to test the property pngCompressionLevel
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property transparent (base name: "transparent")', function() {
      // uncomment below and update the code to test the property transparent
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property verticalResolution (base name: "verticalResolution")', function() {
      // uncomment below and update the code to test the property verticalResolution
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

    it('should have the property width (base name: "width")', function() {
      // uncomment below and update the code to test the property width
      //var instance = new PdfBrokerIoApi.PdfToImageOptions();
      //expect(instance).to.be();
    });

  });

}));
