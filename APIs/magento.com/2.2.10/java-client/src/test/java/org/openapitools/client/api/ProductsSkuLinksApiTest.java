/*
 * Magento B2B
 * Magento Commerce is the leading provider of open omnichannel innovation.
 *
 * The version of the OpenAPI document: 2.2.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.openapitools.client.model.CatalogProductLinkManagementV1SetProductLinksPostRequest;
import org.openapitools.client.model.CatalogProductLinkRepositoryV1SavePutRequest;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProductsSkuLinksApi
 */
@Disabled
public class ProductsSkuLinksApiTest {

    private final ProductsSkuLinksApi api = new ProductsSkuLinksApi();

    /**
     * products/{sku}/links
     *
     * Assign a product link to another product
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void catalogProductLinkManagementV1SetProductLinksPostTest() throws ApiException {
        String sku = null;
        CatalogProductLinkManagementV1SetProductLinksPostRequest catalogProductLinkManagementV1SetProductLinksPostRequest = null;
        Boolean response = api.catalogProductLinkManagementV1SetProductLinksPost(sku, catalogProductLinkManagementV1SetProductLinksPostRequest);
        // TODO: test validations
    }

    /**
     * products/{sku}/links
     *
     * Save product link
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void catalogProductLinkRepositoryV1SavePutTest() throws ApiException {
        String sku = null;
        CatalogProductLinkRepositoryV1SavePutRequest catalogProductLinkRepositoryV1SavePutRequest = null;
        Boolean response = api.catalogProductLinkRepositoryV1SavePut(sku, catalogProductLinkRepositoryV1SavePutRequest);
        // TODO: test validations
    }

}
