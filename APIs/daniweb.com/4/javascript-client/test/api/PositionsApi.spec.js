/**
 * DaniWeb Connect API
 * User Recommendation Engine and Chat Network
 *
 * The version of the OpenAPI document: 4
 * Contact: dani@daniwebmail.com
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
    factory(root.expect, root.DaniWebConnectApi);
  }
}(this, function(expect, DaniWebConnectApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DaniWebConnectApi.PositionsApi();
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

  describe('PositionsApi', function() {
    describe('positionsIDDelete', function() {
      it('should call positionsIDDelete successfully', function(done) {
        //uncomment below and update the code to test positionsIDDelete
        //instance.positionsIDDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('positionsIDPatch', function() {
      it('should call positionsIDPatch successfully', function(done) {
        //uncomment below and update the code to test positionsIDPatch
        //instance.positionsIDPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('positionsPost', function() {
      it('should call positionsPost successfully', function(done) {
        //uncomment below and update the code to test positionsPost
        //instance.positionsPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
