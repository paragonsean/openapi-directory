/**
 * Figshare API
 * Figshare apiv2. Using Swagger 2.0
 *
 * The version of the OpenAPI document: 2.0.0
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
    factory(root.expect, root.FigshareApi);
  }
}(this, function(expect, FigshareApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new FigshareApi.ProjectsApi();
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

  describe('ProjectsApi', function() {
    describe('privateProjectArticleDelete', function() {
      it('should call privateProjectArticleDelete successfully', function(done) {
        //uncomment below and update the code to test privateProjectArticleDelete
        //instance.privateProjectArticleDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectArticleDetails', function() {
      it('should call privateProjectArticleDetails successfully', function(done) {
        //uncomment below and update the code to test privateProjectArticleDetails
        //instance.privateProjectArticleDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectArticleFile', function() {
      it('should call privateProjectArticleFile successfully', function(done) {
        //uncomment below and update the code to test privateProjectArticleFile
        //instance.privateProjectArticleFile(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectArticleFiles', function() {
      it('should call privateProjectArticleFiles successfully', function(done) {
        //uncomment below and update the code to test privateProjectArticleFiles
        //instance.privateProjectArticleFiles(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectArticlesCreate', function() {
      it('should call privateProjectArticlesCreate successfully', function(done) {
        //uncomment below and update the code to test privateProjectArticlesCreate
        //instance.privateProjectArticlesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectArticlesList', function() {
      it('should call privateProjectArticlesList successfully', function(done) {
        //uncomment below and update the code to test privateProjectArticlesList
        //instance.privateProjectArticlesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectCollaboratorDelete', function() {
      it('should call privateProjectCollaboratorDelete successfully', function(done) {
        //uncomment below and update the code to test privateProjectCollaboratorDelete
        //instance.privateProjectCollaboratorDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectCollaboratorsInvite', function() {
      it('should call privateProjectCollaboratorsInvite successfully', function(done) {
        //uncomment below and update the code to test privateProjectCollaboratorsInvite
        //instance.privateProjectCollaboratorsInvite(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectCollaboratorsList', function() {
      it('should call privateProjectCollaboratorsList successfully', function(done) {
        //uncomment below and update the code to test privateProjectCollaboratorsList
        //instance.privateProjectCollaboratorsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectCreate', function() {
      it('should call privateProjectCreate successfully', function(done) {
        //uncomment below and update the code to test privateProjectCreate
        //instance.privateProjectCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectDelete', function() {
      it('should call privateProjectDelete successfully', function(done) {
        //uncomment below and update the code to test privateProjectDelete
        //instance.privateProjectDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectDetails', function() {
      it('should call privateProjectDetails successfully', function(done) {
        //uncomment below and update the code to test privateProjectDetails
        //instance.privateProjectDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectLeave', function() {
      it('should call privateProjectLeave successfully', function(done) {
        //uncomment below and update the code to test privateProjectLeave
        //instance.privateProjectLeave(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectNote', function() {
      it('should call privateProjectNote successfully', function(done) {
        //uncomment below and update the code to test privateProjectNote
        //instance.privateProjectNote(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectNoteDelete', function() {
      it('should call privateProjectNoteDelete successfully', function(done) {
        //uncomment below and update the code to test privateProjectNoteDelete
        //instance.privateProjectNoteDelete(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectNoteUpdate', function() {
      it('should call privateProjectNoteUpdate successfully', function(done) {
        //uncomment below and update the code to test privateProjectNoteUpdate
        //instance.privateProjectNoteUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectNotesCreate', function() {
      it('should call privateProjectNotesCreate successfully', function(done) {
        //uncomment below and update the code to test privateProjectNotesCreate
        //instance.privateProjectNotesCreate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectNotesList', function() {
      it('should call privateProjectNotesList successfully', function(done) {
        //uncomment below and update the code to test privateProjectNotesList
        //instance.privateProjectNotesList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectPublish', function() {
      it('should call privateProjectPublish successfully', function(done) {
        //uncomment below and update the code to test privateProjectPublish
        //instance.privateProjectPublish(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectUpdate', function() {
      it('should call privateProjectUpdate successfully', function(done) {
        //uncomment below and update the code to test privateProjectUpdate
        //instance.privateProjectUpdate(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectsList', function() {
      it('should call privateProjectsList successfully', function(done) {
        //uncomment below and update the code to test privateProjectsList
        //instance.privateProjectsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('privateProjectsSearch', function() {
      it('should call privateProjectsSearch successfully', function(done) {
        //uncomment below and update the code to test privateProjectsSearch
        //instance.privateProjectsSearch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectArticles', function() {
      it('should call projectArticles successfully', function(done) {
        //uncomment below and update the code to test projectArticles
        //instance.projectArticles(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectDetails', function() {
      it('should call projectDetails successfully', function(done) {
        //uncomment below and update the code to test projectDetails
        //instance.projectDetails(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectsList', function() {
      it('should call projectsList successfully', function(done) {
        //uncomment below and update the code to test projectsList
        //instance.projectsList(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
    describe('projectsSearch', function() {
      it('should call projectsSearch successfully', function(done) {
        //uncomment below and update the code to test projectsSearch
        //instance.projectsSearch(function(error) {
        //  if (error) throw error;
        //expect().to.be();
        //});
        done();
      });
    });
  });

}));
