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
    instance = new BbcNitroApi.AvailableMediaSetsMediaSetsMediaSetInnerMediaSets();
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

  describe('AvailableMediaSetsMediaSetsMediaSetInnerMediaSets', function() {
    it('should create an instance of AvailableMediaSetsMediaSetsMediaSetInnerMediaSets', function() {
      // uncomment below and update the code to test AvailableMediaSetsMediaSetsMediaSetInnerMediaSets
      //var instance = new BbcNitroApi.AvailableMediaSetsMediaSetsMediaSetInnerMediaSets();
      //expect(instance).to.be.a(BbcNitroApi.AvailableMediaSetsMediaSetsMediaSetInnerMediaSets);
    });

    it('should have the property mediaSet (base name: "media_set")', function() {
      // uncomment below and update the code to test the property mediaSet
      //var instance = new BbcNitroApi.AvailableMediaSetsMediaSetsMediaSetInnerMediaSets();
      //expect(instance).to.be();
    });

  });

}));
