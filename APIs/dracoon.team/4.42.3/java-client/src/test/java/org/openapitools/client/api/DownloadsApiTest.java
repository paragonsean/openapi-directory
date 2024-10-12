/*
 * DRACOON API
 * REST Web Services for DRACOON<br><br>This page provides an overview of all available and documented DRACOON APIs, which are grouped by tags.<br>Each tag provides a collection of APIs that are intended for a specific area of the DRACOON.<br><br><a title='Developer Information' href='https://developer.dracoon.com'>Developer Information</a>&emsp;&emsp;<a title='Get SDKs on GitHub' href='https://github.com/dracoon'>Get SDKs on GitHub</a><br><br><a title='Terms of service' href='https://www.dracoon.com/terms/general-terms-and-conditions/'>Terms of service</a>
 *
 * The version of the OpenAPI document: 4.42.3
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
 * API tests for DownloadsApi
 */
@Disabled
public class DownloadsApiTest {

    private final DownloadsApi api = new DownloadsApi();

    /**
     * Download avatar
     *
     * &lt;h3 style&#x3D;&#39;padding: 5px; background-color: #F6F7F8; border: 1px solid #AAA; border-radius: 5px; display: table-cell;&#39;&gt;&amp;#128640; Since v4.11.0&lt;/h3&gt;  ### Description: Download avatar for given user ID and UUID.  ### Precondition: Valid UUID.  ### Postcondition: Stream is returned.  ### Further Information: None.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void downloadAvatarTest() throws ApiException {
        Long userId = null;
        String uuid = null;
        String response = api.downloadAvatar(userId, uuid);
        // TODO: test validations
    }

    /**
     * Download file
     *
     * ### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void downloadFileViaTokenTest() throws ApiException {
        String token = null;
        String range = null;
        Boolean genericMimetype = null;
        Boolean inline = null;
        api.downloadFileViaToken(token, range, genericMimetype, inline);
        // TODO: test validations
    }

    /**
     * Download file
     *
     * ### Description: Download a file.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Range requests are supported.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void downloadFileViaToken1Test() throws ApiException {
        String token = null;
        String range = null;
        Boolean genericMimetype = null;
        Boolean inline = null;
        api.downloadFileViaToken1(token, range, genericMimetype, inline);
        // TODO: test validations
    }

    /**
     * Download ZIP archive
     *
     * ### Description: Download multiple files in a ZIP archive.  ### Precondition: Valid download token.  ### Postcondition: Stream is returned.  ### Further Information: Create a download token with &#x60;POST /nodes/zip&#x60; API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void downloadZipArchiveViaTokenTest() throws ApiException {
        String token = null;
        api.downloadZipArchiveViaToken(token);
        // TODO: test validations
    }

}
