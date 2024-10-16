/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
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
    factory(root.expect, root.AppCenterClient);
  }
}(this, function(expect, AppCenterClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new AppCenterClient.DistributeApi();
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

  describe('DistributeApi', function() {
    describe('appleMappingCreate', function() {
      it('should call appleMappingCreate successfully', function(done) {
        //uncomment below and update the code to test appleMappingCreate
        //instance.appleMappingCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appleMappingDelete', function() {
      it('should call appleMappingDelete successfully', function(done) {
        //uncomment below and update the code to test appleMappingDelete
        //instance.appleMappingDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appleMappingGet', function() {
      it('should call appleMappingGet successfully', function(done) {
        //uncomment below and update the code to test appleMappingGet
        //instance.appleMappingGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('appleMappingTestFlightGroups', function() {
      it('should call appleMappingTestFlightGroups successfully', function(done) {
        //uncomment below and update the code to test appleMappingTestFlightGroups
        //instance.appleMappingTestFlightGroups(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesDeviceDetails', function() {
      it('should call devicesDeviceDetails successfully', function(done) {
        //uncomment below and update the code to test devicesDeviceDetails
        //instance.devicesDeviceDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesGetReleaseUpdateDevicesStatus', function() {
      it('should call devicesGetReleaseUpdateDevicesStatus successfully', function(done) {
        //uncomment below and update the code to test devicesGetReleaseUpdateDevicesStatus
        //instance.devicesGetReleaseUpdateDevicesStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesList', function() {
      it('should call devicesList successfully', function(done) {
        //uncomment below and update the code to test devicesList
        //instance.devicesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesListCsvFormat', function() {
      it('should call devicesListCsvFormat successfully', function(done) {
        //uncomment below and update the code to test devicesListCsvFormat
        //instance.devicesListCsvFormat(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesRegisterUserForDevice', function() {
      it('should call devicesRegisterUserForDevice successfully', function(done) {
        //uncomment below and update the code to test devicesRegisterUserForDevice
        //instance.devicesRegisterUserForDevice(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesRemoveUserDevice', function() {
      it('should call devicesRemoveUserDevice successfully', function(done) {
        //uncomment below and update the code to test devicesRemoveUserDevice
        //instance.devicesRemoveUserDevice(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('devicesUserDevicesList', function() {
      it('should call devicesUserDevicesList successfully', function(done) {
        //uncomment below and update the code to test devicesUserDevicesList
        //instance.devicesUserDevicesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('distibutionReleasesInstallAnalytics', function() {
      it('should call distibutionReleasesInstallAnalytics successfully', function(done) {
        //uncomment below and update the code to test distibutionReleasesInstallAnalytics
        //instance.distibutionReleasesInstallAnalytics(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('provisioningProfile', function() {
      it('should call provisioningProfile successfully', function(done) {
        //uncomment below and update the code to test provisioningProfile
        //instance.provisioningProfile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesAddDistributionGroup', function() {
      it('should call releasesAddDistributionGroup successfully', function(done) {
        //uncomment below and update the code to test releasesAddDistributionGroup
        //instance.releasesAddDistributionGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesAddStore', function() {
      it('should call releasesAddStore successfully', function(done) {
        //uncomment below and update the code to test releasesAddStore
        //instance.releasesAddStore(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesAddTesters', function() {
      it('should call releasesAddTesters successfully', function(done) {
        //uncomment below and update the code to test releasesAddTesters
        //instance.releasesAddTesters(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesAvailableToTester', function() {
      it('should call releasesAvailableToTester successfully', function(done) {
        //uncomment below and update the code to test releasesAvailableToTester
        //instance.releasesAvailableToTester(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesCreateReleaseUpload', function() {
      it('should call releasesCreateReleaseUpload successfully', function(done) {
        //uncomment below and update the code to test releasesCreateReleaseUpload
        //instance.releasesCreateReleaseUpload(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesDelete', function() {
      it('should call releasesDelete successfully', function(done) {
        //uncomment below and update the code to test releasesDelete
        //instance.releasesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesDeleteDistributionGroup', function() {
      it('should call releasesDeleteDistributionGroup successfully', function(done) {
        //uncomment below and update the code to test releasesDeleteDistributionGroup
        //instance.releasesDeleteDistributionGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesDeleteDistributionStore', function() {
      it('should call releasesDeleteDistributionStore successfully', function(done) {
        //uncomment below and update the code to test releasesDeleteDistributionStore
        //instance.releasesDeleteDistributionStore(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesDeleteDistributionTester', function() {
      it('should call releasesDeleteDistributionTester successfully', function(done) {
        //uncomment below and update the code to test releasesDeleteDistributionTester
        //instance.releasesDeleteDistributionTester(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesDeleteTesterFromDestinations', function() {
      it('should call releasesDeleteTesterFromDestinations successfully', function(done) {
        //uncomment below and update the code to test releasesDeleteTesterFromDestinations
        //instance.releasesDeleteTesterFromDestinations(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesDeleteWithDistributionGroupId', function() {
      it('should call releasesDeleteWithDistributionGroupId successfully', function(done) {
        //uncomment below and update the code to test releasesDeleteWithDistributionGroupId
        //instance.releasesDeleteWithDistributionGroupId(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetIosManifest', function() {
      it('should call releasesGetIosManifest successfully', function(done) {
        //uncomment below and update the code to test releasesGetIosManifest
        //instance.releasesGetIosManifest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetLatestByDistributionGroup', function() {
      it('should call releasesGetLatestByDistributionGroup successfully', function(done) {
        //uncomment below and update the code to test releasesGetLatestByDistributionGroup
        //instance.releasesGetLatestByDistributionGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetLatestByHash', function() {
      it('should call releasesGetLatestByHash successfully', function(done) {
        //uncomment below and update the code to test releasesGetLatestByHash
        //instance.releasesGetLatestByHash(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetLatestByPublicDistributionGroup', function() {
      it('should call releasesGetLatestByPublicDistributionGroup successfully', function(done) {
        //uncomment below and update the code to test releasesGetLatestByPublicDistributionGroup
        //instance.releasesGetLatestByPublicDistributionGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetLatestByUser', function() {
      it('should call releasesGetLatestByUser successfully', function(done) {
        //uncomment below and update the code to test releasesGetLatestByUser
        //instance.releasesGetLatestByUser(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetLatestPrivateRelease', function() {
      it('should call releasesGetLatestPrivateRelease successfully', function(done) {
        //uncomment below and update the code to test releasesGetLatestPrivateRelease
        //instance.releasesGetLatestPrivateRelease(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetLatestPublicRelease', function() {
      it('should call releasesGetLatestPublicRelease successfully', function(done) {
        //uncomment below and update the code to test releasesGetLatestPublicRelease
        //instance.releasesGetLatestPublicRelease(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetPublicGroupsForReleaseByHash', function() {
      it('should call releasesGetPublicGroupsForReleaseByHash successfully', function(done) {
        //uncomment below and update the code to test releasesGetPublicGroupsForReleaseByHash
        //instance.releasesGetPublicGroupsForReleaseByHash(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetReleaseUploadStatus', function() {
      it('should call releasesGetReleaseUploadStatus successfully', function(done) {
        //uncomment below and update the code to test releasesGetReleaseUploadStatus
        //instance.releasesGetReleaseUploadStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesGetSparkleFeed', function() {
      it('should call releasesGetSparkleFeed successfully', function(done) {
        //uncomment below and update the code to test releasesGetSparkleFeed
        //instance.releasesGetSparkleFeed(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesList', function() {
      it('should call releasesList successfully', function(done) {
        //uncomment below and update the code to test releasesList
        //instance.releasesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesListByDistributionGroup', function() {
      it('should call releasesListByDistributionGroup successfully', function(done) {
        //uncomment below and update the code to test releasesListByDistributionGroup
        //instance.releasesListByDistributionGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesListLatest', function() {
      it('should call releasesListLatest successfully', function(done) {
        //uncomment below and update the code to test releasesListLatest
        //instance.releasesListLatest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesPutDistributionGroup', function() {
      it('should call releasesPutDistributionGroup successfully', function(done) {
        //uncomment below and update the code to test releasesPutDistributionGroup
        //instance.releasesPutDistributionGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesPutDistributionTester', function() {
      it('should call releasesPutDistributionTester successfully', function(done) {
        //uncomment below and update the code to test releasesPutDistributionTester
        //instance.releasesPutDistributionTester(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesUpdate', function() {
      it('should call releasesUpdate successfully', function(done) {
        //uncomment below and update the code to test releasesUpdate
        //instance.releasesUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesUpdateDetails', function() {
      it('should call releasesUpdateDetails successfully', function(done) {
        //uncomment below and update the code to test releasesUpdateDetails
        //instance.releasesUpdateDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('releasesUpdateReleaseUploadStatus', function() {
      it('should call releasesUpdateReleaseUploadStatus successfully', function(done) {
        //uncomment below and update the code to test releasesUpdateReleaseUploadStatus
        //instance.releasesUpdateReleaseUploadStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeNotificationsGetNotificationByAppId', function() {
      it('should call storeNotificationsGetNotificationByAppId successfully', function(done) {
        //uncomment below and update the code to test storeNotificationsGetNotificationByAppId
        //instance.storeNotificationsGetNotificationByAppId(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasePublishLogsGet', function() {
      it('should call storeReleasePublishLogsGet successfully', function(done) {
        //uncomment below and update the code to test storeReleasePublishLogsGet
        //instance.storeReleasePublishLogsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasesDelete', function() {
      it('should call storeReleasesDelete successfully', function(done) {
        //uncomment below and update the code to test storeReleasesDelete
        //instance.storeReleasesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasesGet', function() {
      it('should call storeReleasesGet successfully', function(done) {
        //uncomment below and update the code to test storeReleasesGet
        //instance.storeReleasesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasesGetLatest', function() {
      it('should call storeReleasesGetLatest successfully', function(done) {
        //uncomment below and update the code to test storeReleasesGetLatest
        //instance.storeReleasesGetLatest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasesGetPublishError', function() {
      it('should call storeReleasesGetPublishError successfully', function(done) {
        //uncomment below and update the code to test storeReleasesGetPublishError
        //instance.storeReleasesGetPublishError(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasesGetRealTimeStatusByReleaseId', function() {
      it('should call storeReleasesGetRealTimeStatusByReleaseId successfully', function(done) {
        //uncomment below and update the code to test storeReleasesGetRealTimeStatusByReleaseId
        //instance.storeReleasesGetRealTimeStatusByReleaseId(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storeReleasesList', function() {
      it('should call storeReleasesList successfully', function(done) {
        //uncomment below and update the code to test storeReleasesList
        //instance.storeReleasesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storesCreate', function() {
      it('should call storesCreate successfully', function(done) {
        //uncomment below and update the code to test storesCreate
        //instance.storesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storesDelete', function() {
      it('should call storesDelete successfully', function(done) {
        //uncomment below and update the code to test storesDelete
        //instance.storesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storesGet', function() {
      it('should call storesGet successfully', function(done) {
        //uncomment below and update the code to test storesGet
        //instance.storesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storesList', function() {
      it('should call storesList successfully', function(done) {
        //uncomment below and update the code to test storesList
        //instance.storesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('storesPatch', function() {
      it('should call storesPatch successfully', function(done) {
        //uncomment below and update the code to test storesPatch
        //instance.storesPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
