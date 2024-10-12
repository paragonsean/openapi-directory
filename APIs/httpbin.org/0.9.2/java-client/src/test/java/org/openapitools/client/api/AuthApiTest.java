/*
 * httpbin.org
 * A simple HTTP Request & Response Service.<br/> <br/> <b>Run locally: </b> <code>$ docker run -p 80:80 kennethreitz/httpbin</code>
 *
 * The version of the OpenAPI document: 0.9.2
 * Contact: me@kennethreitz.org
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client.api;

import org.openapitools.client.ApiException;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for AuthApi
 */
@Disabled
public class AuthApiTest {

    private final AuthApi api = new AuthApi();

    /**
     * Prompts the user for authorization using HTTP Basic Auth.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void basicAuthUserPasswdGetTest() throws ApiException {
        String user = null;
        String passwd = null;
        api.basicAuthUserPasswdGet(user, passwd);
        // TODO: test validations
    }

    /**
     * Prompts the user for authorization using bearer authentication.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void bearerGetTest() throws ApiException {
        String authorization = null;
        api.bearerGet(authorization);
        // TODO: test validations
    }

    /**
     * Prompts the user for authorization using Digest Auth + Algorithm.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void digestAuthQopUserPasswdAlgorithmGetTest() throws ApiException {
        String qop = null;
        String user = null;
        String passwd = null;
        String algorithm = null;
        api.digestAuthQopUserPasswdAlgorithmGet(qop, user, passwd, algorithm);
        // TODO: test validations
    }

    /**
     * Prompts the user for authorization using Digest Auth + Algorithm.
     *
     * allow settings the stale_after argument. 
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void digestAuthQopUserPasswdAlgorithmStaleAfterGetTest() throws ApiException {
        String qop = null;
        String user = null;
        String passwd = null;
        String algorithm = null;
        String staleAfter = null;
        api.digestAuthQopUserPasswdAlgorithmStaleAfterGet(qop, user, passwd, algorithm, staleAfter);
        // TODO: test validations
    }

    /**
     * Prompts the user for authorization using Digest Auth.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void digestAuthQopUserPasswdGetTest() throws ApiException {
        String qop = null;
        String user = null;
        String passwd = null;
        api.digestAuthQopUserPasswdGet(qop, user, passwd);
        // TODO: test validations
    }

    /**
     * Prompts the user for authorization using HTTP Basic Auth.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void hiddenBasicAuthUserPasswdGetTest() throws ApiException {
        String user = null;
        String passwd = null;
        api.hiddenBasicAuthUserPasswdGet(user, passwd);
        // TODO: test validations
    }

}
