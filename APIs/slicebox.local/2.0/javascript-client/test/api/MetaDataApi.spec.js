/**
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
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
    factory(root.expect, root.SliceboxApi);
  }
}(this, function(expect, SliceboxApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new SliceboxApi.MetaDataApi();
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

  describe('MetaDataApi', function() {
    describe('metadataFlatseriesGet', function() {
      it('should call metadataFlatseriesGet successfully', function(done) {
        //uncomment below and update the code to test metadataFlatseriesGet
        //instance.metadataFlatseriesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataFlatseriesIdGet', function() {
      it('should call metadataFlatseriesIdGet successfully', function(done) {
        //uncomment below and update the code to test metadataFlatseriesIdGet
        //instance.metadataFlatseriesIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataFlatseriesQueryPost', function() {
      it('should call metadataFlatseriesQueryPost successfully', function(done) {
        //uncomment below and update the code to test metadataFlatseriesQueryPost
        //instance.metadataFlatseriesQueryPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataImagesGet', function() {
      it('should call metadataImagesGet successfully', function(done) {
        //uncomment below and update the code to test metadataImagesGet
        //instance.metadataImagesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataImagesIdGet', function() {
      it('should call metadataImagesIdGet successfully', function(done) {
        //uncomment below and update the code to test metadataImagesIdGet
        //instance.metadataImagesIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataImagesQueryPost', function() {
      it('should call metadataImagesQueryPost successfully', function(done) {
        //uncomment below and update the code to test metadataImagesQueryPost
        //instance.metadataImagesQueryPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataPatientsGet', function() {
      it('should call metadataPatientsGet successfully', function(done) {
        //uncomment below and update the code to test metadataPatientsGet
        //instance.metadataPatientsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataPatientsIdGet', function() {
      it('should call metadataPatientsIdGet successfully', function(done) {
        //uncomment below and update the code to test metadataPatientsIdGet
        //instance.metadataPatientsIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataPatientsIdImagesGet', function() {
      it('should call metadataPatientsIdImagesGet successfully', function(done) {
        //uncomment below and update the code to test metadataPatientsIdImagesGet
        //instance.metadataPatientsIdImagesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataPatientsQueryPost', function() {
      it('should call metadataPatientsQueryPost successfully', function(done) {
        //uncomment below and update the code to test metadataPatientsQueryPost
        //instance.metadataPatientsQueryPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesGet', function() {
      it('should call metadataSeriesGet successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesGet
        //instance.metadataSeriesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesIdGet', function() {
      it('should call metadataSeriesIdGet successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesIdGet
        //instance.metadataSeriesIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesIdSeriestagsGet', function() {
      it('should call metadataSeriesIdSeriestagsGet successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesIdSeriestagsGet
        //instance.metadataSeriesIdSeriestagsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesIdSeriestagsPost', function() {
      it('should call metadataSeriesIdSeriestagsPost successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesIdSeriestagsPost
        //instance.metadataSeriesIdSeriestagsPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesIdSeriestypesDelete', function() {
      it('should call metadataSeriesIdSeriestypesDelete successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesIdSeriestypesDelete
        //instance.metadataSeriesIdSeriestypesDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesIdSeriestypesGet', function() {
      it('should call metadataSeriesIdSeriestypesGet successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesIdSeriestypesGet
        //instance.metadataSeriesIdSeriestypesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesIdSourceGet', function() {
      it('should call metadataSeriesIdSourceGet successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesIdSourceGet
        //instance.metadataSeriesIdSourceGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesQueryPost', function() {
      it('should call metadataSeriesQueryPost successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesQueryPost
        //instance.metadataSeriesQueryPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete', function() {
      it('should call metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete
        //instance.metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete', function() {
      it('should call metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete
        //instance.metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut', function() {
      it('should call metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut successfully', function(done) {
        //uncomment below and update the code to test metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut
        //instance.metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataSeriestagsGet', function() {
      it('should call metadataSeriestagsGet successfully', function(done) {
        //uncomment below and update the code to test metadataSeriestagsGet
        //instance.metadataSeriestagsGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataStudiesGet', function() {
      it('should call metadataStudiesGet successfully', function(done) {
        //uncomment below and update the code to test metadataStudiesGet
        //instance.metadataStudiesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataStudiesIdGet', function() {
      it('should call metadataStudiesIdGet successfully', function(done) {
        //uncomment below and update the code to test metadataStudiesIdGet
        //instance.metadataStudiesIdGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataStudiesIdImagesGet', function() {
      it('should call metadataStudiesIdImagesGet successfully', function(done) {
        //uncomment below and update the code to test metadataStudiesIdImagesGet
        //instance.metadataStudiesIdImagesGet(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('metadataStudiesQueryPost', function() {
      it('should call metadataStudiesQueryPost successfully', function(done) {
        //uncomment below and update the code to test metadataStudiesQueryPost
        //instance.metadataStudiesQueryPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('seriestypesSeriesQueryPost', function() {
      it('should call seriestypesSeriesQueryPost successfully', function(done) {
        //uncomment below and update the code to test seriestypesSeriesQueryPost
        //instance.seriestypesSeriesQueryPost(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
