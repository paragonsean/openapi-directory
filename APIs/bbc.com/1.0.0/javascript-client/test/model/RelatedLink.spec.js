/**
 * BBC Nitro API
 * BBC Nitro is the BBC's application programming interface (API) for BBC Programmes Metadata.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: nitro@bbc.co.uk
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
    factory(root.expect, root.BbcNitroApi);
  }
}(this, function(expect, BbcNitroApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new BbcNitroApi.RelatedLink();
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

  describe('RelatedLink', function() {
    it('should create an instance of RelatedLink', function() {
      // uncomment below and update the code to test RelatedLink
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be.a(BbcNitroApi.RelatedLink);
    });

    it('should have the property availability (base name: "availability")', function() {
      // uncomment below and update the code to test the property availability
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property isExternal (base name: "is_external")', function() {
      // uncomment below and update the code to test the property isExternal
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property pid (base name: "pid")', function() {
      // uncomment below and update the code to test the property pid
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property synopses (base name: "synopses")', function() {
      // uncomment below and update the code to test the property synopses
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property title (base name: "title")', function() {
      // uncomment below and update the code to test the property title
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property type (base name: "type")', function() {
      // uncomment below and update the code to test the property type
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

    it('should have the property uri (base name: "uri")', function() {
      // uncomment below and update the code to test the property uri
      //var instance = new BbcNitroApi.RelatedLink();
      //expect(instance).to.be();
    });

  });

}));
