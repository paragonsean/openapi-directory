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
import org.openapitools.client.model.Document;
import org.openapitools.client.model.DocumentCloneDTO;
import java.io.File;
import java.util.UUID;
import org.junit.jupiter.api.Disabled;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * API tests for DocumentsApi
 */
@Disabled
public class DocumentsApiTest {

    private final DocumentsApi api = new DocumentsApi();

    /**
     * DocumentsController: Get Dependent Objects Tree
     *
     * This endpoint is helpful for helping users and bots identify dependent objects to this DocumentsController and retreive their corresponding metadata in order to make modifications to those objects in downstream operations.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsChildobjectsGetIdTest() throws ApiException {
        UUID id = null;
        List<ChildObjects> response = api.documentsChildobjectsGetId(id);
        // TODO: test validations
    }

    /**
     * Documents: Clone an existing Ooxml Document to new Parent Story
     *
     * Clone A Document that has already been uploaded to a new Story
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsClonePostIdTest() throws ApiException {
        UUID id = null;
        DocumentCloneDTO documentCloneDTO = null;
        Document response = api.documentsClonePostId(id, documentCloneDTO);
        // TODO: test validations
    }

    /**
     * Documents: Delete by Id
     *
     * Permantly delete a document from the Ooxml Automation API. Note that is does not make changes to the related Presalytics APIs.  Please use the delete endpoint in the story API to ensure that stories are not left with orphaned references to the Ooxml Automation API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsDeleteIdTest() throws ApiException {
        UUID id = null;
        api.documentsDeleteId(id);
        // TODO: test validations
    }

    /**
     * Documents: Download
     *
     * Download the into a bytestream for client-side processing.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsDownloadGetIdOrginalTest() throws ApiException {
        UUID id = null;
        Boolean orginal = null;
        File response = api.documentsDownloadGetIdOrginal(id, orginal);
        // TODO: test validations
    }

    /**
     * Documents: Get by Id
     *
     * Get by Id: Use this method to retrieve a Documents object by its primary key (id)
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsGetIdTest() throws ApiException {
        UUID id = null;
        Document response = api.documentsGetId(id);
        // TODO: test validations
    }

    /**
     * Documents: Upload
     *
     * Upload an OpenOfficeXml document (e.g., .xlsx, .pptx) for processing by the API.
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void documentsPostTest() throws ApiException {
        File _file = null;
        UUID storyId = null;
        List<Document> response = api.documentsPost(_file, storyId);
        // TODO: test validations
    }

}
