/**
 * AGCO API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: v1
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
    factory(root.expect, root.AgcoApi);
  }
}(this, function(expect, AgcoApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AgcoApi.BundlesApi();
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

  describe('BundlesApi', function() {
    describe('bundlesDeleteBundle', function() {
      it('should call bundlesDeleteBundle successfully', function(done) {
        //uncomment below and update the code to test bundlesDeleteBundle
        //instance.bundlesDeleteBundle(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('bundlesGetBundle', function() {
      it('should call bundlesGetBundle successfully', function(done) {
        //uncomment below and update the code to test bundlesGetBundle
        //instance.bundlesGetBundle(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('bundlesGetBundles', function() {
      it('should call bundlesGetBundles successfully', function(done) {
        //uncomment below and update the code to test bundlesGetBundles
        //instance.bundlesGetBundles(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('bundlesPostBundle', function() {
      it('should call bundlesPostBundle successfully', function(done) {
        //uncomment below and update the code to test bundlesPostBundle
        //instance.bundlesPostBundle(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('bundlesPutBundle', function() {
      it('should call bundlesPutBundle successfully', function(done) {
        //uncomment below and update the code to test bundlesPutBundle
        //instance.bundlesPutBundle(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
