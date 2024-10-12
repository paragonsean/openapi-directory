/**
 * Radio & Music Services
 * We encapsulate Radio & Music business logic for iPlayer Radio and BBC Music products on all platforms. We add value by reliably providing the right blend of metadata needed by clients.
 *
 * The version of the OpenAPI document: 1.0.0
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
    factory(root.expect, root.RadioMusicServices);
  }
}(this, function(expect, RadioMusicServices) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new RadioMusicServices.BroadcastsApi();
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

  describe('BroadcastsApi', function() {
    describe('broadcastsGet', function() {
      it('should call broadcastsGet successfully', function(done) {
        //uncomment below and update the code to test broadcastsGet
        //instance.broadcastsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('broadcastsLatestGet', function() {
      it('should call broadcastsLatestGet successfully', function(done) {
        //uncomment below and update the code to test broadcastsLatestGet
        //instance.broadcastsLatestGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getBroadcastByPid', function() {
      it('should call getBroadcastByPid successfully', function(done) {
        //uncomment below and update the code to test getBroadcastByPid
        //instance.getBroadcastByPid(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
