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
import org.openapitools.client.model.ErrorResponse;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for ProductsDownloadableLinksSamplesIdApi
 */
@Disabled
public class ProductsDownloadableLinksSamplesIdApiTest {

    private final ProductsDownloadableLinksSamplesIdApi api = new ProductsDownloadableLinksSamplesIdApi();

    /**
     * products/downloadable-links/samples/{id}
     *
     * Delete downloadable sample
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void downloadableSampleRepositoryV1DeleteDeleteTest() throws ApiException {
        Integer id = null;
        Boolean response = api.downloadableSampleRepositoryV1DeleteDelete(id);
        // TODO: test validations
    }

}
