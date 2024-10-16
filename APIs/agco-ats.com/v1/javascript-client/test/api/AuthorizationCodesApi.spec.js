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
    instance = new AgcoApi.AuthorizationCodesApi();
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

  describe('AuthorizationCodesApi', function() {
    describe('authorizationCodesDeleteAuthorizationCode', function() {
      it('should call authorizationCodesDeleteAuthorizationCode successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesDeleteAuthorizationCode
        //instance.authorizationCodesDeleteAuthorizationCode(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authorizationCodesGetAuthorizationCode', function() {
      it('should call authorizationCodesGetAuthorizationCode successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesGetAuthorizationCode
        //instance.authorizationCodesGetAuthorizationCode(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authorizationCodesGetAuthorizationCodes', function() {
      it('should call authorizationCodesGetAuthorizationCodes successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesGetAuthorizationCodes
        //instance.authorizationCodesGetAuthorizationCodes(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authorizationCodesGetContactInformation', function() {
      it('should call authorizationCodesGetContactInformation successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesGetContactInformation
        //instance.authorizationCodesGetContactInformation(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authorizationCodesPostAuthorizationCode', function() {
      it('should call authorizationCodesPostAuthorizationCode successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesPostAuthorizationCode
        //instance.authorizationCodesPostAuthorizationCode(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authorizationCodesPutAuthorizationCode', function() {
      it('should call authorizationCodesPutAuthorizationCode successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesPutAuthorizationCode
        //instance.authorizationCodesPutAuthorizationCode(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('authorizationCodesValidateAuthorizationCode', function() {
      it('should call authorizationCodesValidateAuthorizationCode successfully', function(done) {
        //uncomment below and update the code to test authorizationCodesValidateAuthorizationCode
        //instance.authorizationCodesValidateAuthorizationCode(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
