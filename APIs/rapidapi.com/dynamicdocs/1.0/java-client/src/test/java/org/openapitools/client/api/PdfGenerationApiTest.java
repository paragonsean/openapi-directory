/*
 * DynamicDocs
 * ADVICEment's [DynamicDocs API automates your document generation](https://advicement.io/dynamic-documents-api) and creates dynamic, optimized, interactive PDFs. Write your templates in LaTeX and call the API with JSON data to get your PDFs in seconds.  The template files are stored in your dashboard and can be edited, tested and published online. Document templates can contain dynamic text using logic statements, include tables stretching multiple pages and show great-looking charts based on the underlying data. LaTeX creates crisp, high-quality documents where every detail is well-positioned and styled.  Integrate with ADVICEment DynamicDocs API in minutes and start creating beautiful [dynamic PDF documents](https://advicement.io/dynamic-documents-api) for your needs.  For more information, visit [DynamicDocs API Home page](https://advicement.io/dynamic-documents-api).
 *
 * The version of the OpenAPI document: 1.0
 * Contact: info@advicement.io
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
 * API tests for PdfGenerationApi
 */
@Disabled
public class PdfGenerationApiTest {

    private final PdfGenerationApi api = new PdfGenerationApi();

    /**
     * Compile New Document PDF
     *
     * Compile a PDF document from a specific template
     *
     * @throws ApiException if the Api call fails
     */
    @Test
    public void compileTest() throws ApiException {
        String templateToken = null;
        String contentType = null;
        Integer docUrlExpiresIn = null;
        String latexCompiler = null;
        Integer latexRuns = null;
        String mainFileName = null;
        String docFileName = null;
        Object body = null;
        Object response = api.compile(templateToken, contentType, docUrlExpiresIn, latexCompiler, latexRuns, mainFileName, docFileName, body);
        // TODO: test validations
    }

}
