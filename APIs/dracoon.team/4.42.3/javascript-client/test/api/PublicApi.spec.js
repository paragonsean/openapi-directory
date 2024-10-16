/**
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
    factory(root.expect, root.DracoonApi);
  }
}(this, function(expect, DracoonApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DracoonApi.PublicApi();
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

  describe('PublicApi', function() {
    describe('cancelFileUploadViaShare', function() {
      it('should call cancelFileUploadViaShare successfully', function(done) {
        //uncomment below and update the code to test cancelFileUploadViaShare
        //instance.cancelFileUploadViaShare(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('checkPublicDownloadSharePassword', function() {
      it('should call checkPublicDownloadSharePassword successfully', function(done) {
        //uncomment below and update the code to test checkPublicDownloadSharePassword
        //instance.checkPublicDownloadSharePassword(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('completeFileUploadViaShare', function() {
      it('should call completeFileUploadViaShare successfully', function(done) {
        //uncomment below and update the code to test completeFileUploadViaShare
        //instance.completeFileUploadViaShare(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('completeS3FileUploadViaShare', function() {
      it('should call completeS3FileUploadViaShare successfully', function(done) {
        //uncomment below and update the code to test completeS3FileUploadViaShare
        //instance.completeS3FileUploadViaShare(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createShareUploadChannel', function() {
      it('should call createShareUploadChannel successfully', function(done) {
        //uncomment below and update the code to test createShareUploadChannel
        //instance.createShareUploadChannel(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('downloadFileViaTokenPublic', function() {
      it('should call downloadFileViaTokenPublic successfully', function(done) {
        //uncomment below and update the code to test downloadFileViaTokenPublic
        //instance.downloadFileViaTokenPublic(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('downloadFileViaTokenPublic1', function() {
      it('should call downloadFileViaTokenPublic1 successfully', function(done) {
        //uncomment below and update the code to test downloadFileViaTokenPublic1
        //instance.downloadFileViaTokenPublic1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('generateDownloadUrlPublic', function() {
      it('should call generateDownloadUrlPublic successfully', function(done) {
        //uncomment below and update the code to test generateDownloadUrlPublic
        //instance.generateDownloadUrlPublic(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('generatePresignedUrlsPublic', function() {
      it('should call generatePresignedUrlsPublic successfully', function(done) {
        //uncomment below and update the code to test generatePresignedUrlsPublic
        //instance.generatePresignedUrlsPublic(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestActiveDirectoryAuthInfo', function() {
      it('should call requestActiveDirectoryAuthInfo successfully', function(done) {
        //uncomment below and update the code to test requestActiveDirectoryAuthInfo
        //instance.requestActiveDirectoryAuthInfo(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestOpenIdAuthInfo', function() {
      it('should call requestOpenIdAuthInfo successfully', function(done) {
        //uncomment below and update the code to test requestOpenIdAuthInfo
        //instance.requestOpenIdAuthInfo(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestPublicDownloadShareInfo', function() {
      it('should call requestPublicDownloadShareInfo successfully', function(done) {
        //uncomment below and update the code to test requestPublicDownloadShareInfo
        //instance.requestPublicDownloadShareInfo(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestPublicUploadShareInfo', function() {
      it('should call requestPublicUploadShareInfo successfully', function(done) {
        //uncomment below and update the code to test requestPublicUploadShareInfo
        //instance.requestPublicUploadShareInfo(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestSoftwareVersion', function() {
      it('should call requestSoftwareVersion successfully', function(done) {
        //uncomment below and update the code to test requestSoftwareVersion
        //instance.requestSoftwareVersion(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestSystemInfo', function() {
      it('should call requestSystemInfo successfully', function(done) {
        //uncomment below and update the code to test requestSystemInfo
        //instance.requestSystemInfo(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestSystemTime', function() {
      it('should call requestSystemTime successfully', function(done) {
        //uncomment below and update the code to test requestSystemTime
        //instance.requestSystemTime(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestThirdPartyDependencies', function() {
      it('should call requestThirdPartyDependencies successfully', function(done) {
        //uncomment below and update the code to test requestThirdPartyDependencies
        //instance.requestThirdPartyDependencies(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('requestUploadStatusPublic', function() {
      it('should call requestUploadStatusPublic successfully', function(done) {
        //uncomment below and update the code to test requestUploadStatusPublic
        //instance.requestUploadStatusPublic(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('uploadFileAsMultipartPublic1', function() {
      it('should call uploadFileAsMultipartPublic1 successfully', function(done) {
        //uncomment below and update the code to test uploadFileAsMultipartPublic1
        //instance.uploadFileAsMultipartPublic1(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
