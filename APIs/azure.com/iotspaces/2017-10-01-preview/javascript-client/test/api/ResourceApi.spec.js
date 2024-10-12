/**
 * IoTSpacesClient
 * Use this API to manage the IoTSpaces service instances in your Azure subscription.
 *
 * The version of the OpenAPI document: 2017-10-01-preview
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
    factory(root.expect, root.IoTSpacesClient);
  }
}(this, function(expect, IoTSpacesClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new IoTSpacesClient.ResourceApi();
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

  describe('ResourceApi', function() {
    describe('ioTSpacesCreateOrUpdate', function() {
      it('should call ioTSpacesCreateOrUpdate successfully', function(done) {
        //uncomment below and update the code to test ioTSpacesCreateOrUpdate
        //instance.ioTSpacesCreateOrUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('ioTSpacesDelete', function() {
      it('should call ioTSpacesDelete successfully', function(done) {
        //uncomment below and update the code to test ioTSpacesDelete
        //instance.ioTSpacesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('ioTSpacesGet', function() {
      it('should call ioTSpacesGet successfully', function(done) {
        //uncomment below and update the code to test ioTSpacesGet
        //instance.ioTSpacesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('ioTSpacesUpdate', function() {
      it('should call ioTSpacesUpdate successfully', function(done) {
        //uncomment below and update the code to test ioTSpacesUpdate
        //instance.ioTSpacesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
