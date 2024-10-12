/**
 * Face Client
 * An API for face detection, verification, and identification.
 *
 * The version of the OpenAPI document: 1.0
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
    factory(root.expect, root.FaceClient);
  }
}(this, function(expect, FaceClient) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FaceClient.DefaultApi();
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

  describe('DefaultApi', function() {
    describe('faceDetectWithUrl', function() {
      it('should call faceDetectWithUrl successfully', function(done) {
        //uncomment below and update the code to test faceDetectWithUrl
        //instance.faceDetectWithUrl(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceFindSimilar', function() {
      it('should call faceFindSimilar successfully', function(done) {
        //uncomment below and update the code to test faceFindSimilar
        //instance.faceFindSimilar(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceGroup', function() {
      it('should call faceGroup successfully', function(done) {
        //uncomment below and update the code to test faceGroup
        //instance.faceGroup(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceIdentify', function() {
      it('should call faceIdentify successfully', function(done) {
        //uncomment below and update the code to test faceIdentify
        //instance.faceIdentify(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListAddFaceFromUrl', function() {
      it('should call faceListAddFaceFromUrl successfully', function(done) {
        //uncomment below and update the code to test faceListAddFaceFromUrl
        //instance.faceListAddFaceFromUrl(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListCreate', function() {
      it('should call faceListCreate successfully', function(done) {
        //uncomment below and update the code to test faceListCreate
        //instance.faceListCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListDelete', function() {
      it('should call faceListDelete successfully', function(done) {
        //uncomment below and update the code to test faceListDelete
        //instance.faceListDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListDeleteFace', function() {
      it('should call faceListDeleteFace successfully', function(done) {
        //uncomment below and update the code to test faceListDeleteFace
        //instance.faceListDeleteFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListGet', function() {
      it('should call faceListGet successfully', function(done) {
        //uncomment below and update the code to test faceListGet
        //instance.faceListGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListList', function() {
      it('should call faceListList successfully', function(done) {
        //uncomment below and update the code to test faceListList
        //instance.faceListList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceListUpdate', function() {
      it('should call faceListUpdate successfully', function(done) {
        //uncomment below and update the code to test faceListUpdate
        //instance.faceListUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('faceVerifyFaceToFace', function() {
      it('should call faceVerifyFaceToFace successfully', function(done) {
        //uncomment below and update the code to test faceVerifyFaceToFace
        //instance.faceVerifyFaceToFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListAddFaceFromUrl', function() {
      it('should call largeFaceListAddFaceFromUrl successfully', function(done) {
        //uncomment below and update the code to test largeFaceListAddFaceFromUrl
        //instance.largeFaceListAddFaceFromUrl(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListCreate', function() {
      it('should call largeFaceListCreate successfully', function(done) {
        //uncomment below and update the code to test largeFaceListCreate
        //instance.largeFaceListCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListDelete', function() {
      it('should call largeFaceListDelete successfully', function(done) {
        //uncomment below and update the code to test largeFaceListDelete
        //instance.largeFaceListDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListDeleteFace', function() {
      it('should call largeFaceListDeleteFace successfully', function(done) {
        //uncomment below and update the code to test largeFaceListDeleteFace
        //instance.largeFaceListDeleteFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListGet', function() {
      it('should call largeFaceListGet successfully', function(done) {
        //uncomment below and update the code to test largeFaceListGet
        //instance.largeFaceListGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListGetFace', function() {
      it('should call largeFaceListGetFace successfully', function(done) {
        //uncomment below and update the code to test largeFaceListGetFace
        //instance.largeFaceListGetFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListGetTrainingStatus', function() {
      it('should call largeFaceListGetTrainingStatus successfully', function(done) {
        //uncomment below and update the code to test largeFaceListGetTrainingStatus
        //instance.largeFaceListGetTrainingStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListList', function() {
      it('should call largeFaceListList successfully', function(done) {
        //uncomment below and update the code to test largeFaceListList
        //instance.largeFaceListList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListListFaces', function() {
      it('should call largeFaceListListFaces successfully', function(done) {
        //uncomment below and update the code to test largeFaceListListFaces
        //instance.largeFaceListListFaces(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListTrain', function() {
      it('should call largeFaceListTrain successfully', function(done) {
        //uncomment below and update the code to test largeFaceListTrain
        //instance.largeFaceListTrain(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListUpdate', function() {
      it('should call largeFaceListUpdate successfully', function(done) {
        //uncomment below and update the code to test largeFaceListUpdate
        //instance.largeFaceListUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largeFaceListUpdateFace', function() {
      it('should call largeFaceListUpdateFace successfully', function(done) {
        //uncomment below and update the code to test largeFaceListUpdateFace
        //instance.largeFaceListUpdateFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupCreate', function() {
      it('should call largePersonGroupCreate successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupCreate
        //instance.largePersonGroupCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupDelete', function() {
      it('should call largePersonGroupDelete successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupDelete
        //instance.largePersonGroupDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupGet', function() {
      it('should call largePersonGroupGet successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupGet
        //instance.largePersonGroupGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupGetTrainingStatus', function() {
      it('should call largePersonGroupGetTrainingStatus successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupGetTrainingStatus
        //instance.largePersonGroupGetTrainingStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupList', function() {
      it('should call largePersonGroupList successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupList
        //instance.largePersonGroupList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonAddFaceFromUrl', function() {
      it('should call largePersonGroupPersonAddFaceFromUrl successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonAddFaceFromUrl
        //instance.largePersonGroupPersonAddFaceFromUrl(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonCreate', function() {
      it('should call largePersonGroupPersonCreate successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonCreate
        //instance.largePersonGroupPersonCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonDelete', function() {
      it('should call largePersonGroupPersonDelete successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonDelete
        //instance.largePersonGroupPersonDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonDeleteFace', function() {
      it('should call largePersonGroupPersonDeleteFace successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonDeleteFace
        //instance.largePersonGroupPersonDeleteFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonGet', function() {
      it('should call largePersonGroupPersonGet successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonGet
        //instance.largePersonGroupPersonGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonGetFace', function() {
      it('should call largePersonGroupPersonGetFace successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonGetFace
        //instance.largePersonGroupPersonGetFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonList', function() {
      it('should call largePersonGroupPersonList successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonList
        //instance.largePersonGroupPersonList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonUpdate', function() {
      it('should call largePersonGroupPersonUpdate successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonUpdate
        //instance.largePersonGroupPersonUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupPersonUpdateFace', function() {
      it('should call largePersonGroupPersonUpdateFace successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupPersonUpdateFace
        //instance.largePersonGroupPersonUpdateFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupTrain', function() {
      it('should call largePersonGroupTrain successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupTrain
        //instance.largePersonGroupTrain(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('largePersonGroupUpdate', function() {
      it('should call largePersonGroupUpdate successfully', function(done) {
        //uncomment below and update the code to test largePersonGroupUpdate
        //instance.largePersonGroupUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupCreate', function() {
      it('should call personGroupCreate successfully', function(done) {
        //uncomment below and update the code to test personGroupCreate
        //instance.personGroupCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupDelete', function() {
      it('should call personGroupDelete successfully', function(done) {
        //uncomment below and update the code to test personGroupDelete
        //instance.personGroupDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupGet', function() {
      it('should call personGroupGet successfully', function(done) {
        //uncomment below and update the code to test personGroupGet
        //instance.personGroupGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupGetTrainingStatus', function() {
      it('should call personGroupGetTrainingStatus successfully', function(done) {
        //uncomment below and update the code to test personGroupGetTrainingStatus
        //instance.personGroupGetTrainingStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupList', function() {
      it('should call personGroupList successfully', function(done) {
        //uncomment below and update the code to test personGroupList
        //instance.personGroupList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonAddFaceFromUrl', function() {
      it('should call personGroupPersonAddFaceFromUrl successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonAddFaceFromUrl
        //instance.personGroupPersonAddFaceFromUrl(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonCreate', function() {
      it('should call personGroupPersonCreate successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonCreate
        //instance.personGroupPersonCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonDelete', function() {
      it('should call personGroupPersonDelete successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonDelete
        //instance.personGroupPersonDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonDeleteFace', function() {
      it('should call personGroupPersonDeleteFace successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonDeleteFace
        //instance.personGroupPersonDeleteFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonGet', function() {
      it('should call personGroupPersonGet successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonGet
        //instance.personGroupPersonGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonGetFace', function() {
      it('should call personGroupPersonGetFace successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonGetFace
        //instance.personGroupPersonGetFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonList', function() {
      it('should call personGroupPersonList successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonList
        //instance.personGroupPersonList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonUpdate', function() {
      it('should call personGroupPersonUpdate successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonUpdate
        //instance.personGroupPersonUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupPersonUpdateFace', function() {
      it('should call personGroupPersonUpdateFace successfully', function(done) {
        //uncomment below and update the code to test personGroupPersonUpdateFace
        //instance.personGroupPersonUpdateFace(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupTrain', function() {
      it('should call personGroupTrain successfully', function(done) {
        //uncomment below and update the code to test personGroupTrain
        //instance.personGroupTrain(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('personGroupUpdate', function() {
      it('should call personGroupUpdate successfully', function(done) {
        //uncomment below and update the code to test personGroupUpdate
        //instance.personGroupUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotApply', function() {
      it('should call snapshotApply successfully', function(done) {
        //uncomment below and update the code to test snapshotApply
        //instance.snapshotApply(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotDelete', function() {
      it('should call snapshotDelete successfully', function(done) {
        //uncomment below and update the code to test snapshotDelete
        //instance.snapshotDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotGet', function() {
      it('should call snapshotGet successfully', function(done) {
        //uncomment below and update the code to test snapshotGet
        //instance.snapshotGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotGetOperationStatus', function() {
      it('should call snapshotGetOperationStatus successfully', function(done) {
        //uncomment below and update the code to test snapshotGetOperationStatus
        //instance.snapshotGetOperationStatus(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotList', function() {
      it('should call snapshotList successfully', function(done) {
        //uncomment below and update the code to test snapshotList
        //instance.snapshotList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotTake', function() {
      it('should call snapshotTake successfully', function(done) {
        //uncomment below and update the code to test snapshotTake
        //instance.snapshotTake(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('snapshotUpdate', function() {
      it('should call snapshotUpdate successfully', function(done) {
        //uncomment below and update the code to test snapshotUpdate
        //instance.snapshotUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
