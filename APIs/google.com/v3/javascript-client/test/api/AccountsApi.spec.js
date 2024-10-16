/**
 * Travel Partner API
 * The Travel Partner API provides you with a RESTful interface to the Google Hotel Center platform. It enables an app to efficiently retrieve and change Hotel Center data, and is thus suitable for managing large or complex accounts.
 *
 * The version of the OpenAPI document: v3
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
    factory(root.expect, root.TravelPartnerApi);
  }
}(this, function(expect, TravelPartnerApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new TravelPartnerApi.AccountsApi();
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

  describe('AccountsApi', function() {
    describe('travelpartnerAccountsAccountLinksCreate', function() {
      it('should call travelpartnerAccountsAccountLinksCreate successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsAccountLinksCreate
        //instance.travelpartnerAccountsAccountLinksCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsAccountLinksDelete', function() {
      it('should call travelpartnerAccountsAccountLinksDelete successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsAccountLinksDelete
        //instance.travelpartnerAccountsAccountLinksDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsAccountLinksList', function() {
      it('should call travelpartnerAccountsAccountLinksList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsAccountLinksList
        //instance.travelpartnerAccountsAccountLinksList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsBrandsCreate', function() {
      it('should call travelpartnerAccountsBrandsCreate successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsBrandsCreate
        //instance.travelpartnerAccountsBrandsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsBrandsList', function() {
      it('should call travelpartnerAccountsBrandsList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsBrandsList
        //instance.travelpartnerAccountsBrandsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsBrandsPatch', function() {
      it('should call travelpartnerAccountsBrandsPatch successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsBrandsPatch
        //instance.travelpartnerAccountsBrandsPatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsFreeBookingLinksReportViewsQuery', function() {
      it('should call travelpartnerAccountsFreeBookingLinksReportViewsQuery successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsFreeBookingLinksReportViewsQuery
        //instance.travelpartnerAccountsFreeBookingLinksReportViewsQuery(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsHotelViewsList', function() {
      it('should call travelpartnerAccountsHotelViewsList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsHotelViewsList
        //instance.travelpartnerAccountsHotelViewsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsHotelViewsSummarize', function() {
      it('should call travelpartnerAccountsHotelViewsSummarize successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsHotelViewsSummarize
        //instance.travelpartnerAccountsHotelViewsSummarize(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsHotelsSetLiveOnGoogle', function() {
      it('should call travelpartnerAccountsHotelsSetLiveOnGoogle successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsHotelsSetLiveOnGoogle
        //instance.travelpartnerAccountsHotelsSetLiveOnGoogle(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsIconsCreate', function() {
      it('should call travelpartnerAccountsIconsCreate successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsIconsCreate
        //instance.travelpartnerAccountsIconsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsIconsList', function() {
      it('should call travelpartnerAccountsIconsList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsIconsList
        //instance.travelpartnerAccountsIconsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsListingsVerify', function() {
      it('should call travelpartnerAccountsListingsVerify successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsListingsVerify
        //instance.travelpartnerAccountsListingsVerify(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsParticipationReportViewsQuery', function() {
      it('should call travelpartnerAccountsParticipationReportViewsQuery successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsParticipationReportViewsQuery
        //instance.travelpartnerAccountsParticipationReportViewsQuery(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsPriceAccuracyViewsList', function() {
      it('should call travelpartnerAccountsPriceAccuracyViewsList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsPriceAccuracyViewsList
        //instance.travelpartnerAccountsPriceAccuracyViewsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsPriceAccuracyViewsSummarize', function() {
      it('should call travelpartnerAccountsPriceAccuracyViewsSummarize successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsPriceAccuracyViewsSummarize
        //instance.travelpartnerAccountsPriceAccuracyViewsSummarize(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsPriceCoverageViewsGetLatest', function() {
      it('should call travelpartnerAccountsPriceCoverageViewsGetLatest successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsPriceCoverageViewsGetLatest
        //instance.travelpartnerAccountsPriceCoverageViewsGetLatest(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsPriceCoverageViewsList', function() {
      it('should call travelpartnerAccountsPriceCoverageViewsList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsPriceCoverageViewsList
        //instance.travelpartnerAccountsPriceCoverageViewsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsPropertyPerformanceReportViewsQuery', function() {
      it('should call travelpartnerAccountsPropertyPerformanceReportViewsQuery successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsPropertyPerformanceReportViewsQuery
        //instance.travelpartnerAccountsPropertyPerformanceReportViewsQuery(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsReconciliationReportsCreate', function() {
      it('should call travelpartnerAccountsReconciliationReportsCreate successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsReconciliationReportsCreate
        //instance.travelpartnerAccountsReconciliationReportsCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsReconciliationReportsGet', function() {
      it('should call travelpartnerAccountsReconciliationReportsGet successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsReconciliationReportsGet
        //instance.travelpartnerAccountsReconciliationReportsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsReconciliationReportsList', function() {
      it('should call travelpartnerAccountsReconciliationReportsList successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsReconciliationReportsList
        //instance.travelpartnerAccountsReconciliationReportsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('travelpartnerAccountsReconciliationReportsValidate', function() {
      it('should call travelpartnerAccountsReconciliationReportsValidate successfully', function(done) {
        //uncomment below and update the code to test travelpartnerAccountsReconciliationReportsValidate
        //instance.travelpartnerAccountsReconciliationReportsValidate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
