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


package org.openapitools.client;

import java.io.IOException;

import java.util.Map;
import java.util.List;

/**
 * Callback for asynchronous API call.
 *
 * @param <T> The return type
 */
public interface ApiCallback<T> {
    /**
     * This is called when the API call fails.
     *
     * @param e The exception causing the failure
     * @param statusCode Status code of the response if available, otherwise it would be 0
     * @param responseHeaders Headers of the response if available, otherwise it would be null
     */
    void onFailure(ApiException e, int statusCode, Map<String, List<String>> responseHeaders);

    /**
     * This is called when the API call succeeded.
     *
     * @param result The result deserialized from response
     * @param statusCode Status code of the response
     * @param responseHeaders Headers of the response
     */
    void onSuccess(T result, int statusCode, Map<String, List<String>> responseHeaders);

    /**
     * This is called when the API upload processing.
     *
     * @param bytesWritten bytes Written
     * @param contentLength content length of request body
     * @param done write end
     */
    void onUploadProgress(long bytesWritten, long contentLength, boolean done);

    /**
     * This is called when the API download processing.
     *
     * @param bytesRead bytes Read
     * @param contentLength content length of the response
     * @param done Read end
     */
    void onDownloadProgress(long bytesRead, long contentLength, boolean done);
}
