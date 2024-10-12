/**
 * OpenAPI Generator Online
 * This is an online openapi generator server.  You can find out more at https://github.com/OpenAPITools/openapi-generator.
 *
 * The version of the OpenAPI document: 6.5.0
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
    factory(root.expect, root.OpenApiGeneratorOnline);
  }
}(this, function(expect, OpenApiGeneratorOnline) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new OpenApiGeneratorOnline.ClientsApi();
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

  describe('ClientsApi', function() {
    describe('clientOptions', function() {
      it('should call clientOptions successfully', function(done) {
        //uncomment below and update the code to test clientOptions
        //instance.clientOptions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('downloadFile', function() {
      it('should call downloadFile successfully', function(done) {
        //uncomment below and update the code to test downloadFile
        //instance.downloadFile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('generateClient', function() {
      it('should call generateClient successfully', function(done) {
        //uncomment below and update the code to test generateClient
        //instance.generateClient(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getClientOptions', function() {
      it('should call getClientOptions successfully', function(done) {
        //uncomment below and update the code to test getClientOptions
        //instance.getClientOptions(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
