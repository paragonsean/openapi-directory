/*
 * Slicebox API
 * Slicebox - safe sharing of medical images
 *
 * The version of the OpenAPI document: 2.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.FlatSeries;
import org.openapitools.client.model.Idsquery;
import org.openapitools.client.model.Image;
import org.openapitools.client.model.Patient;
import org.openapitools.client.model.Query;
import org.openapitools.client.model.Series;
import org.openapitools.client.model.Seriesidseriestypesresult;
import org.openapitools.client.model.Seriestag;
import org.openapitools.client.model.Seriestype;
import org.openapitools.client.model.Source;
import org.openapitools.client.model.Study;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for MetaDataApi
 */
@Disabled
public class MetaDataApiTest {

    private final MetaDataApi api = new MetaDataApi();

    /**
     * Returns a list of flattened metadata on the patient, study and series levels
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataFlatseriesGetTest() throws ApiException {
        Long startindex = null;
        Long count = null;
        String orderby = null;
        Boolean orderascending = null;
        String filter = null;
        String sources = null;
        String seriestypes = null;
        String seriestags = null;
        List<FlatSeries> response = api.metadataFlatseriesGet(startindex, count, orderby, orderascending, filter, sources, seriestypes, seriestags);
        // TODO: test validations
    }

    /**
     * Return the flat series with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataFlatseriesIdGetTest() throws ApiException {
        Long id = null;
        FlatSeries response = api.metadataFlatseriesIdGet(id);
        // TODO: test validations
    }

    /**
     * submit a query for flat series
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataFlatseriesQueryPostTest() throws ApiException {
        Query query = null;
        List<FlatSeries> response = api.metadataFlatseriesQueryPost(query);
        // TODO: test validations
    }

    /**
     * Returns a list of metadata on the image level of the DICOM hierarchy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataImagesGetTest() throws ApiException {
        Long seriesid = null;
        Long startindex = null;
        Long count = null;
        List<Image> response = api.metadataImagesGet(seriesid, startindex, count);
        // TODO: test validations
    }

    /**
     * Return the image with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataImagesIdGetTest() throws ApiException {
        Long id = null;
        Image response = api.metadataImagesIdGet(id);
        // TODO: test validations
    }

    /**
     * submit a query for images
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataImagesQueryPostTest() throws ApiException {
        Query query = null;
        List<Image> response = api.metadataImagesQueryPost(query);
        // TODO: test validations
    }

    /**
     * Returns a list of metadata on the patient level of the DICOM hierarchy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataPatientsGetTest() throws ApiException {
        Long startindex = null;
        Long count = null;
        String orderby = null;
        Boolean orderascending = null;
        String filter = null;
        String sources = null;
        String seriestypes = null;
        String seriestags = null;
        List<Patient> response = api.metadataPatientsGet(startindex, count, orderby, orderascending, filter, sources, seriestypes, seriestags);
        // TODO: test validations
    }

    /**
     * Return the patient with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataPatientsIdGetTest() throws ApiException {
        Long id = null;
        Patient response = api.metadataPatientsIdGet(id);
        // TODO: test validations
    }

    /**
     * Returns all images for the patient with the supplied patient ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataPatientsIdImagesGetTest() throws ApiException {
        Long id = null;
        String sources = null;
        String seriestypes = null;
        String seriestags = null;
        List<Image> response = api.metadataPatientsIdImagesGet(id, sources, seriestypes, seriestags);
        // TODO: test validations
    }

    /**
     * submit a query for patients
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataPatientsQueryPostTest() throws ApiException {
        Query query = null;
        List<Patient> response = api.metadataPatientsQueryPost(query);
        // TODO: test validations
    }

    /**
     * Returns a list of metadata on the series level of the DICOM hierarchy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesGetTest() throws ApiException {
        Long studyid = null;
        Long startindex = null;
        Long count = null;
        String sources = null;
        String seriestypes = null;
        String seriestags = null;
        List<Series> response = api.metadataSeriesGet(studyid, startindex, count, sources, seriestypes, seriestags);
        // TODO: test validations
    }

    /**
     * Return the series with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesIdGetTest() throws ApiException {
        Long id = null;
        Series response = api.metadataSeriesIdGet(id);
        // TODO: test validations
    }

    /**
     * get the list of series tags for the series with the supplied ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesIdSeriestagsGetTest() throws ApiException {
        Long id = null;
        List<Seriestag> response = api.metadataSeriesIdSeriestagsGet(id);
        // TODO: test validations
    }

    /**
     * add a series tag to the series with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesIdSeriestagsPostTest() throws ApiException {
        Long id = null;
        Seriestag query = null;
        Seriestag response = api.metadataSeriesIdSeriestagsPost(id, query);
        // TODO: test validations
    }

    /**
     * Delete all series types for the series with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesIdSeriestypesDeleteTest() throws ApiException {
        Long id = null;
        api.metadataSeriesIdSeriestypesDelete(id);
        // TODO: test validations
    }

    /**
     * get the list of series types for the series with the supplied ID.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesIdSeriestypesGetTest() throws ApiException {
        Long id = null;
        List<Seriestype> response = api.metadataSeriesIdSeriestypesGet(id);
        // TODO: test validations
    }

    /**
     * Return the source of the series with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesIdSourceGetTest() throws ApiException {
        Long id = null;
        Source response = api.metadataSeriesIdSourceGet(id);
        // TODO: test validations
    }

    /**
     * submit a query for series
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesQueryPostTest() throws ApiException {
        Query query = null;
        List<Series> response = api.metadataSeriesQueryPost(query);
        // TODO: test validations
    }

    /**
     * Delete the series tag with the supplied series tag ID from the series with the supplied series ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesSeriesIdSeriestagsSeriesTagIdDeleteTest() throws ApiException {
        Long seriesId = null;
        Long seriesTagId = null;
        api.metadataSeriesSeriesIdSeriestagsSeriesTagIdDelete(seriesId, seriesTagId);
        // TODO: test validations
    }

    /**
     * Delete the series type with the supplied series type ID from the series with the supplied series ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesSeriesIdSeriestypesSeriesTypeIdDeleteTest() throws ApiException {
        Long seriesId = null;
        Long seriesTypeId = null;
        api.metadataSeriesSeriesIdSeriestypesSeriesTypeIdDelete(seriesId, seriesTypeId);
        // TODO: test validations
    }

    /**
     * Add the series type with the supplied series type ID to the series with the supplied series ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriesSeriesIdSeriestypesSeriesTypeIdPutTest() throws ApiException {
        Long seriesId = null;
        Long seriesTypeId = null;
        api.metadataSeriesSeriesIdSeriestypesSeriesTypeIdPut(seriesId, seriesTypeId);
        // TODO: test validations
    }

    /**
     * Returns a list of series tags currently currently in use.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataSeriestagsGetTest() throws ApiException {
        List<Seriestag> response = api.metadataSeriestagsGet();
        // TODO: test validations
    }

    /**
     * Returns a list of metadata on the study level of the DICOM hierarchy
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataStudiesGetTest() throws ApiException {
        Long patientid = null;
        Long startindex = null;
        Long count = null;
        String sources = null;
        String seriestypes = null;
        String seriestags = null;
        List<Study> response = api.metadataStudiesGet(patientid, startindex, count, sources, seriestypes, seriestags);
        // TODO: test validations
    }

    /**
     * Return the study with the supplied ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataStudiesIdGetTest() throws ApiException {
        Long id = null;
        Study response = api.metadataStudiesIdGet(id);
        // TODO: test validations
    }

    /**
     * Returns all images for the study with the supplied study ID
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataStudiesIdImagesGetTest() throws ApiException {
        Long id = null;
        String sources = null;
        String seriestypes = null;
        String seriestags = null;
        List<Image> response = api.metadataStudiesIdImagesGet(id, sources, seriestypes, seriestags);
        // TODO: test validations
    }

    /**
     * submit a query for studies
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void metadataStudiesQueryPostTest() throws ApiException {
        Query query = null;
        List<Study> response = api.metadataStudiesQueryPost(query);
        // TODO: test validations
    }

    /**
     * submit a query for seriestypes for a list of series
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void seriestypesSeriesQueryPostTest() throws ApiException {
        Idsquery query = null;
        Seriesidseriestypesresult response = api.seriestypesSeriesQueryPost(query);
        // TODO: test validations
    }

}
