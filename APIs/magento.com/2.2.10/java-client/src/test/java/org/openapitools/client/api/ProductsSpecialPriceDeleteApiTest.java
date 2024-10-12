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
import org.openapitools.client.model.CatalogDataPriceUpdateResultInterface;
import org.openapitools.client.model.CatalogSpecialPriceStorageV1UpdatePostRequest;
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProductsSpecialPriceDeleteApi
 */
@Disabled
public class ProductsSpecialPriceDeleteApiTest {

    private final ProductsSpecialPriceDeleteApi api = new ProductsSpecialPriceDeleteApi();

    /**
     * products/special-price-delete
     *
     * Delete product&#39;s special price. If any items will have invalid price, store id, sku or dates, they will be marked as failed and excluded from delete list and \\Magento\\Catalog\\Api\\Data\\PriceUpdateResultInterface[] with problem description will be returned. If there were no failed items during update empty array will be returned. If error occurred during the delete exception will be thrown.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void catalogSpecialPriceStorageV1DeletePostTest() throws ApiException {
        CatalogSpecialPriceStorageV1UpdatePostRequest catalogSpecialPriceStorageV1UpdatePostRequest = null;
        List<CatalogDataPriceUpdateResultInterface> response = api.catalogSpecialPriceStorageV1DeletePost(catalogSpecialPriceStorageV1UpdatePostRequest);
        // TODO: test validations
    }

}
