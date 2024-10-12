/*
 * Zalando Shop
 * The shop API empowers developers to build amazing new apps or websites using Zalando shop data and services.
 *
 * The version of the OpenAPI document: v1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.ErrorMessage;
import org.openapitools.client.model.Facet;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for FacetsApi
 */
@Disabled
public class FacetsApiTest {

    private final FacetsApi api = new FacetsApi();

    /**
     * Shop Facets
     *
     * Zalando API Facets Schema
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void facetsGetTest() throws ApiException {
        List<String> ageGroup = null;
        List<String> articleId = null;
        List<String> activationDate = null;
        List<String> articleModelId = null;
        List<String> assortmentArea = null;
        List<String> brand = null;
        List<String> brandfamily = null;
        List<String> category = null;
        List<String> color = null;
        List<String> den = null;
        List<String> filling = null;
        List<String> gender = null;
        List<String> heelForm = null;
        List<String> heelHeight = null;
        String length = null;
        List<String> occasion = null;
        List<String> pattern = null;
        String price = null;
        List<String> sale = null;
        List<String> season = null;
        List<String> shaftHeight = null;
        List<String> shaftWidth = null;
        List<String> shirtCollar = null;
        List<String> shoeFastener = null;
        List<String> shoeToecap = null;
        List<String> shopArea = null;
        String size = null;
        List<String> sports = null;
        List<String> technology = null;
        List<String> trouserRise = null;
        List<String> upperMaterial = null;
        List<String> volume = null;
        String acceptLanguage = null;
        List<String> fields = null;
        List<Facet> response = api.facetsGet(ageGroup, articleId, activationDate, articleModelId, assortmentArea, brand, brandfamily, category, color, den, filling, gender, heelForm, heelHeight, length, occasion, pattern, price, sale, season, shaftHeight, shaftWidth, shirtCollar, shoeFastener, shoeToecap, shopArea, size, sports, technology, trouserRise, upperMaterial, volume, acceptLanguage, fields);
        // TODO: test validations
    }

}
