/*
 * OOXML Automation
 * This API helps users convert Excel and Powerpoint documents into rich, live dashboards and stories.
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ChildObjects;
import java.io.File;
import org.openapitools.client.model.OoxmlDTO;
import org.openapitools.client.model.ProblemDetails;
import org.openapitools.client.model.SlideSlides;
import org.openapitools.client.model.SlideSlidesDetails;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for SlidesApi
 */
@Disabled
public class SlidesApiTest {

    private final SlidesApi api = new SlidesApi();

    /**
     * Slides: Get Dependent Objects Tree
     *
     * This endpoint is helpful for helping users and bots identify dependent objects to this Slide and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void slidesSlidesChildobjectsGetIdTest() throws ApiException {
        UUID id = null;
        List<ChildObjects> response = api.slidesSlidesChildobjectsGetId(id);
        // TODO: test validations
    }

    /**
     * Slides: Get Details
     *
     * Returns object metadata and information about relative dependent objects 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void slidesSlidesDetailsGetIdTest() throws ApiException {
        UUID id = null;
        SlideSlidesDetails response = api.slidesSlidesDetailsGetId(id);
        // TODO: test validations
    }

    /**
     * Slides: Get by Id
     *
     * Get by Id: Use this method to retrieve a Slides object by its primary key (id)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void slidesSlidesGetIdTest() throws ApiException {
        UUID id = null;
        SlideSlides response = api.slidesSlidesGetId(id);
        // TODO: test validations
    }

    /**
     * Slides: Get Underlying Xml
     *
     * Return the subset of the xml content from within the latest edited version of the OpenXmlDocument from this Slide object.  The returned xml data conforms to the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm).  Use this endpoint a starting point for building client-side extensions that modify Presalytics widgets containing Slide objects.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void slidesSlidesOpenofficexmlGetIdUpdatedTest() throws ApiException {
        UUID id = null;
        Boolean updated = null;
        OoxmlDTO response = api.slidesSlidesOpenofficexmlGetIdUpdated(id, updated);
        // TODO: test validations
    }

    /**
     * Slides: Modify Underlying Xml
     *
     * Directly eidt the underlying xml of a Slide object within an OpenOpenXml (e.g. Excel, Powerpoint) document. This endpoint will validatate the submitted xml against the [Ecma-376 standard](http://www.ecma-international.org/publications/standards/Ecma-376.htm) prior to saving modification.  Invalid xml will rejected by this endpoint and a (hopefully) helpful error message will be returned.  Use this endpoint for client-side automation of modifications ot Slide objects.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void slidesSlidesOpenofficexmlPutIdTest() throws ApiException {
        String id = null;
        OoxmlDTO ooxmlDTO = null;
        api.slidesSlidesOpenofficexmlPutId(id, ooxmlDTO);
        // TODO: test validations
    }

    /**
     * Slides: Get Svg file
     *
     * This endpoint is helpful for rending this Slide as an svg or image object that can then be rendered in a story, dashboard or website.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void slidesSlidesSvgGetIdUseCacheTest() throws ApiException {
        UUID id = null;
        Boolean useCache = null;
        File response = api.slidesSlidesSvgGetIdUseCache(id, useCache);
        // TODO: test validations
    }

}
