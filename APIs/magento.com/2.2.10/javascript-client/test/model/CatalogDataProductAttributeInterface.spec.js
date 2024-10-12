/**
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
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
    factory(root.expect, root.MagentoB2B);
  }
}(this, function(expect, MagentoB2B) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new MagentoB2B.CatalogDataProductAttributeInterface();
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

  describe('CatalogDataProductAttributeInterface', function() {
    it('should create an instance of CatalogDataProductAttributeInterface', function() {
      // uncomment below and update the code to test CatalogDataProductAttributeInterface
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be.a(MagentoB2B.CatalogDataProductAttributeInterface);
    });

    it('should have the property applyTo (base name: "apply_to")', function() {
      // uncomment below and update the code to test the property applyTo
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property attributeCode (base name: "attribute_code")', function() {
      // uncomment below and update the code to test the property attributeCode
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property attributeId (base name: "attribute_id")', function() {
      // uncomment below and update the code to test the property attributeId
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property backendModel (base name: "backend_model")', function() {
      // uncomment below and update the code to test the property backendModel
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property backendType (base name: "backend_type")', function() {
      // uncomment below and update the code to test the property backendType
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property customAttributes (base name: "custom_attributes")', function() {
      // uncomment below and update the code to test the property customAttributes
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property defaultFrontendLabel (base name: "default_frontend_label")', function() {
      // uncomment below and update the code to test the property defaultFrontendLabel
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property defaultValue (base name: "default_value")', function() {
      // uncomment below and update the code to test the property defaultValue
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property entityTypeId (base name: "entity_type_id")', function() {
      // uncomment below and update the code to test the property entityTypeId
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property extensionAttributes (base name: "extension_attributes")', function() {
      // uncomment below and update the code to test the property extensionAttributes
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property frontendClass (base name: "frontend_class")', function() {
      // uncomment below and update the code to test the property frontendClass
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property frontendInput (base name: "frontend_input")', function() {
      // uncomment below and update the code to test the property frontendInput
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property frontendLabels (base name: "frontend_labels")', function() {
      // uncomment below and update the code to test the property frontendLabels
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isComparable (base name: "is_comparable")', function() {
      // uncomment below and update the code to test the property isComparable
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isFilterable (base name: "is_filterable")', function() {
      // uncomment below and update the code to test the property isFilterable
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isFilterableInGrid (base name: "is_filterable_in_grid")', function() {
      // uncomment below and update the code to test the property isFilterableInGrid
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isFilterableInSearch (base name: "is_filterable_in_search")', function() {
      // uncomment below and update the code to test the property isFilterableInSearch
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isHtmlAllowedOnFront (base name: "is_html_allowed_on_front")', function() {
      // uncomment below and update the code to test the property isHtmlAllowedOnFront
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isRequired (base name: "is_required")', function() {
      // uncomment below and update the code to test the property isRequired
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isSearchable (base name: "is_searchable")', function() {
      // uncomment below and update the code to test the property isSearchable
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isUnique (base name: "is_unique")', function() {
      // uncomment below and update the code to test the property isUnique
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isUsedForPromoRules (base name: "is_used_for_promo_rules")', function() {
      // uncomment below and update the code to test the property isUsedForPromoRules
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isUsedInGrid (base name: "is_used_in_grid")', function() {
      // uncomment below and update the code to test the property isUsedInGrid
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isUserDefined (base name: "is_user_defined")', function() {
      // uncomment below and update the code to test the property isUserDefined
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isVisible (base name: "is_visible")', function() {
      // uncomment below and update the code to test the property isVisible
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isVisibleInAdvancedSearch (base name: "is_visible_in_advanced_search")', function() {
      // uncomment below and update the code to test the property isVisibleInAdvancedSearch
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isVisibleInGrid (base name: "is_visible_in_grid")', function() {
      // uncomment below and update the code to test the property isVisibleInGrid
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isVisibleOnFront (base name: "is_visible_on_front")', function() {
      // uncomment below and update the code to test the property isVisibleOnFront
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property isWysiwygEnabled (base name: "is_wysiwyg_enabled")', function() {
      // uncomment below and update the code to test the property isWysiwygEnabled
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property note (base name: "note")', function() {
      // uncomment below and update the code to test the property note
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property options (base name: "options")', function() {
      // uncomment below and update the code to test the property options
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property position (base name: "position")', function() {
      // uncomment below and update the code to test the property position
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property scope (base name: "scope")', function() {
      // uncomment below and update the code to test the property scope
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property sourceModel (base name: "source_model")', function() {
      // uncomment below and update the code to test the property sourceModel
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property usedForSortBy (base name: "used_for_sort_by")', function() {
      // uncomment below and update the code to test the property usedForSortBy
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property usedInProductListing (base name: "used_in_product_listing")', function() {
      // uncomment below and update the code to test the property usedInProductListing
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

    it('should have the property validationRules (base name: "validation_rules")', function() {
      // uncomment below and update the code to test the property validationRules
      //var instance = new MagentoB2B.CatalogDataProductAttributeInterface();
      //expect(instance).to.be();
    });

  });

}));
