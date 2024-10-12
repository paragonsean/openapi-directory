/*
 * TruAnon Private API
 * Welcome to TruAnon! Thank you for helping make the Internet a safer place to be.  Adopting TruAnon is simple. There is no setup or dependencies, nothing to store or process. Making identity part of your service is fun, and you’ll be up and running in a matter of minutes.  TruAnon Private Token is used anytime you request information from TruAnon and you must edit this into the Variables section for this collection.  This API contains two endpoints and both require these same two arguments, also found in the Variables section of this collection.  These two arguments are:  TruAnon Service Identifier  and  Your Member Name  Your TruAnon Service Identifier was provided by TruAnon and is likely the root domain of your site or service. Your Member Name is the unique member ID on your system that you would like to query.  Information is continuously updated for display purposes and aside from performance considerations, there should be no need to capture or save anything from TruAnon.
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import okhttp3.MediaType;
import okhttp3.ResponseBody;

import java.io.IOException;

import okio.Buffer;
import okio.BufferedSource;
import okio.ForwardingSource;
import okio.Okio;
import okio.Source;

public class ProgressResponseBody extends ResponseBody {

    private final ResponseBody responseBody;
    private final ApiCallback callback;
    private BufferedSource bufferedSource;

    public ProgressResponseBody(ResponseBody responseBody, ApiCallback callback) {
        this.responseBody = responseBody;
        this.callback = callback;
    }

    @Override
    public MediaType contentType() {
        return responseBody.contentType();
    }

    @Override
    public long contentLength() {
        return responseBody.contentLength();
    }

    @Override
    public BufferedSource source() {
        if (bufferedSource == null) {
            bufferedSource = Okio.buffer(source(responseBody.source()));
        }
        return bufferedSource;
    }

    private Source source(Source source) {
        return new ForwardingSource(source) {
            long totalBytesRead = 0L;

            @Override
            public long read(Buffer sink, long byteCount) throws IOException {
                long bytesRead = super.read(sink, byteCount);
                // read() returns the number of bytes read, or -1 if this source is exhausted.
                totalBytesRead += bytesRead != -1 ? bytesRead : 0;
                callback.onDownloadProgress(totalBytesRead, responseBody.contentLength(), bytesRead == -1);
                return bytesRead;
            }
        };
    }
}
