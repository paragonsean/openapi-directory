/*
 * SheerSEO API
 * Sheerseo API has 2 stages:<br>First stage - initiating the task: You fill in your task and receive in return the task id. <br>Second stage - collecting the results: send a request containing the task ids you got at the first stage and collecting the results.
 *
 * The version of the OpenAPI document: 0.0.1
 * 
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
