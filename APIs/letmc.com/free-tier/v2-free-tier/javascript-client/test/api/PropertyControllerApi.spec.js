/**
 * LetMC Api V2, Free (Tier 1)
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v2-free-tier
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
    factory(root.expect, root.LetMcApiV2FreeTier1);
  }
}(this, function(expect, LetMcApiV2FreeTier1) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new LetMcApiV2FreeTier1.PropertyControllerApi();
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

  describe('PropertyControllerApi', function() {
    describe('propertyControllerGetPropertiesFacilities', function() {
      it('should call propertyControllerGetPropertiesFacilities successfully', function(done) {
        //uncomment below and update the code to test propertyControllerGetPropertiesFacilities
        //instance.propertyControllerGetPropertiesFacilities(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('propertyControllerGetPropertiesPhotos', function() {
      it('should call propertyControllerGetPropertiesPhotos successfully', function(done) {
        //uncomment below and update the code to test propertyControllerGetPropertiesPhotos
        //instance.propertyControllerGetPropertiesPhotos(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('propertyControllerGetPropertiesRooms', function() {
      it('should call propertyControllerGetPropertiesRooms successfully', function(done) {
        //uncomment below and update the code to test propertyControllerGetPropertiesRooms
        //instance.propertyControllerGetPropertiesRooms(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('propertyControllerGetPropertiesTenancies', function() {
      it('should call propertyControllerGetPropertiesTenancies successfully', function(done) {
        //uncomment below and update the code to test propertyControllerGetPropertiesTenancies
        //instance.propertyControllerGetPropertiesTenancies(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('propertyControllerGetPropertyEERDownload', function() {
      it('should call propertyControllerGetPropertyEERDownload successfully', function(done) {
        //uncomment below and update the code to test propertyControllerGetPropertyEERDownload
        //instance.propertyControllerGetPropertyEERDownload(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('propertyControllerGetPropertyEIRDownload', function() {
      it('should call propertyControllerGetPropertyEIRDownload successfully', function(done) {
        //uncomment below and update the code to test propertyControllerGetPropertyEIRDownload
        //instance.propertyControllerGetPropertyEIRDownload(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier1ShortNamePropertyPropertiesGet', function() {
      it('should call v2Tier1ShortNamePropertyPropertiesGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier1ShortNamePropertyPropertiesGet
        //instance.v2Tier1ShortNamePropertyPropertiesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('v2Tier1ShortNamePropertyPropertiesPropertyIDGet', function() {
      it('should call v2Tier1ShortNamePropertyPropertiesPropertyIDGet successfully', function(done) {
        //uncomment below and update the code to test v2Tier1ShortNamePropertyPropertiesPropertyIDGet
        //instance.v2Tier1ShortNamePropertyPropertiesPropertyIDGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
