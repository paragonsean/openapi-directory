/*
 * Adobe Experience Manager (AEM) API
 * Swagger AEM is an OpenAPI specification for Adobe Experience Manager (AEM) API
 *
 * The version of the OpenAPI document: 3.7.1-pre.0
 * Contact: opensource@shinesolutions.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import java.io.File;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for GraniteApi
 */
@Disabled
public class GraniteApiTest {

    private final GraniteApi api = new GraniteApi();

    /**
     * @throws ApiException if the Api call fails
     */
    @Test
    public void sslSetupTest() throws ApiException {
        String keystorePassword = null;
        String keystorePasswordConfirm = null;
        String truststorePassword = null;
        String truststorePasswordConfirm = null;
        String httpsHostname = null;
        String httpsPort = null;
        File certificateFile = null;
        File privatekeyFile = null;
        String response = api.sslSetup(keystorePassword, keystorePasswordConfirm, truststorePassword, truststorePasswordConfirm, httpsHostname, httpsPort, certificateFile, privatekeyFile);
        // TODO: test validations
    }

}
