/**
 * CallFire API Documentation
 * CallFire
 *
 * The version of the OpenAPI document: V2
 * Contact: support@callfire.com
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
    factory(root.expect, root.CallFireApiDocumentation);
  }
}(this, function(expect, CallFireApiDocumentation) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CallFireApiDocumentation.CallsApi();
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

  describe('CallsApi', function() {
    describe('addCallBroadcastBatch', function() {
      it('should call addCallBroadcastBatch successfully', function(done) {
        //uncomment below and update the code to test addCallBroadcastBatch
        //instance.addCallBroadcastBatch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('addCallBroadcastRecipients', function() {
      it('should call addCallBroadcastRecipients successfully', function(done) {
        //uncomment below and update the code to test addCallBroadcastRecipients
        //instance.addCallBroadcastRecipients(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('archiveVoiceBroadcast', function() {
      it('should call archiveVoiceBroadcast successfully', function(done) {
        //uncomment below and update the code to test archiveVoiceBroadcast
        //instance.archiveVoiceBroadcast(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('createCallBroadcast', function() {
      it('should call createCallBroadcast successfully', function(done) {
        //uncomment below and update the code to test createCallBroadcast
        //instance.createCallBroadcast(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('findCallBroadcasts', function() {
      it('should call findCallBroadcasts successfully', function(done) {
        //uncomment below and update the code to test findCallBroadcasts
        //instance.findCallBroadcasts(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('findCalls', function() {
      it('should call findCalls successfully', function(done) {
        //uncomment below and update the code to test findCalls
        //instance.findCalls(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCall', function() {
      it('should call getCall successfully', function(done) {
        //uncomment below and update the code to test getCall
        //instance.getCall(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallBroadcast', function() {
      it('should call getCallBroadcast successfully', function(done) {
        //uncomment below and update the code to test getCallBroadcast
        //instance.getCallBroadcast(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallBroadcastBatches', function() {
      it('should call getCallBroadcastBatches successfully', function(done) {
        //uncomment below and update the code to test getCallBroadcastBatches
        //instance.getCallBroadcastBatches(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallBroadcastCalls', function() {
      it('should call getCallBroadcastCalls successfully', function(done) {
        //uncomment below and update the code to test getCallBroadcastCalls
        //instance.getCallBroadcastCalls(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallBroadcastStats', function() {
      it('should call getCallBroadcastStats successfully', function(done) {
        //uncomment below and update the code to test getCallBroadcastStats
        //instance.getCallBroadcastStats(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallRecording', function() {
      it('should call getCallRecording successfully', function(done) {
        //uncomment below and update the code to test getCallRecording
        //instance.getCallRecording(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallRecordingByName', function() {
      it('should call getCallRecordingByName successfully', function(done) {
        //uncomment below and update the code to test getCallRecordingByName
        //instance.getCallRecordingByName(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallRecordingMp3', function() {
      it('should call getCallRecordingMp3 successfully', function(done) {
        //uncomment below and update the code to test getCallRecordingMp3
        //instance.getCallRecordingMp3(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallRecordingMp3ByName', function() {
      it('should call getCallRecordingMp3ByName successfully', function(done) {
        //uncomment below and update the code to test getCallRecordingMp3ByName
        //instance.getCallRecordingMp3ByName(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('getCallRecordings', function() {
      it('should call getCallRecordings successfully', function(done) {
        //uncomment below and update the code to test getCallRecordings
        //instance.getCallRecordings(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('sendCalls', function() {
      it('should call sendCalls successfully', function(done) {
        //uncomment below and update the code to test sendCalls
        //instance.sendCalls(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('startVoiceBroadcast', function() {
      it('should call startVoiceBroadcast successfully', function(done) {
        //uncomment below and update the code to test startVoiceBroadcast
        //instance.startVoiceBroadcast(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('stopVoiceBroadcast', function() {
      it('should call stopVoiceBroadcast successfully', function(done) {
        //uncomment below and update the code to test stopVoiceBroadcast
        //instance.stopVoiceBroadcast(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('toggleCallBroadcastRecipientsStatus', function() {
      it('should call toggleCallBroadcastRecipientsStatus successfully', function(done) {
        //uncomment below and update the code to test toggleCallBroadcastRecipientsStatus
        //instance.toggleCallBroadcastRecipientsStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('updateCallBroadcast', function() {
      it('should call updateCallBroadcast successfully', function(done) {
        //uncomment below and update the code to test updateCallBroadcast
        //instance.updateCallBroadcast(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
