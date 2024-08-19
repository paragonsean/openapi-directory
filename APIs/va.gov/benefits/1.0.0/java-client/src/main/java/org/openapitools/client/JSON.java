/*
 * Benefits Intake
 * The Benefits Intake API allows authorized third-party systems used by Veteran Service Organizations (VSOs), agencies, and Veterans to digitally submit VA benefits claim documents directly to the Veterans Benefits Administration's (VBA) claims intake process. This API handles documents related to the following benefit claim types:   * Compensation * Pension/Survivors Benefits * Education * Fiduciary * Insurance * Veteran Readiness & Employment (VRE) * Board of Veteran Appeals (BVA)  This API also provides submission status updates until documents are successfully established for VBA claim processing, eliminating the need for users to switch between systems to manually check whether documents have been successfully uploaded.  ## Background  This API provides a secure, efficient, and tracked alternative to mail or fax for VA benefit claim document submissions. Documents are uploaded directly to the VBA so they can be processed as quickly as possible.  ## Technical overview The Benefits Intake API first provides an upload location and unique submission identifier, and then accepts a payload consisting of a document in PDF format, zero or more optional attachments in PDF format, and some JSON metadata.   The metadata describes the document and attachments, and identifies the person for whom it is being submitted. This payload is encoded as binary multipart/form-data (not base64). The unique identifier supplied with the payload can subsequently be used to request the processing status of the uploaded document package.  To avoid errors and processing delays, API consumers are encouraged to validate the `zipcode`,`fileNumber`, `veteranFirstName`, `veteranLastName` and `businessLine` fields before submission according to their description in the DocumentUploadMetadata model and use the 'businessLine' attribute for the most efficient processing. Additionally, please ensure no PDF user passwords are used in submitted PDFs.   ### Attachment & file size limits There is no limit on the number of files a payload can contain, but size limits do apply.  * Uploaded documents cannot be larger than 21\" x 21\" * The entire payload cannot exceed 5 GB * No single file in a payload can exceed 100 MB  ### Date of receipt The date that documents are successfully submitted through the Benefits Intake API is used as the official VA date of receipt. However, note that until a document status of `received`, `processing`, `success`, or `vbms` is returned, a client cannot consider the document received by VA.   A status of `received` means that the document package has been transmitted, but may not be validated. Any errors with the document package, such as unreadable PDFs or a Veteran not found, will cause the status to change to `error`.  If the document status is `error`, VA has not received the submission and cannot honor the submission date as the date of receipt.  ### Authentication and Authorization API requests are authorized through a symmetric API token, provided in an HTTP header with name 'apikey'. [Request an API key.](https://developer.va.gov/apply)  ### Testing in the sandbox environment In the sandbox environment, the final status of a submission is `received` and submissions do not actually progress to the central mail repository or VBMS.   Progress beyond the `received` status can be simulated for testing. We allow passing in a `Status-Override` header on the `/uploads/{id}` endpoint so that you can change the status of your submission to simulate the various scenarios.   The available statuses are `pending`, `uploaded`, `received`, `processing`, `success`, `vbms`, and `error`. The meaning of the various statuses is listed below in Models under DocumentUploadStatusAttributes.  ### Test data We use mock test data in the sandbox environment. Data is not sent upstream and it is not necessary to align submitted test data with any other systems' data.  ### Validating documents Use the POST `/uploads/validate_document` endpoint to make sure your documents will pass system file requirements and validations before you send them through the submissions process. This step is optional but decreases the likelihood of individual document errors during the submission process.  Validations performed: * Document is a valid PDF (Note: `Content-Type` header value must be \"application/pdf\") * Document does not have a user password (an owner password is acceptable) * File size does not exceed 100 MB * Page size does not exceed 21\" x 21\"  ### Upload operation Allows a client to upload a multi-part document package (form + attachments + metadata).  1. Client Request: POST https://sandbox-api.va.gov/services/vba_documents/v1/     * No request body or parameters required  2. Service Response: A JSON API object with the following attributes:     * `guid`: An identifier used for subsequent status requests     * `location`: A URL to which the actual document package payload can be submitted in the next step. The URL is specific to this upload request, and should not be re-used for subsequent uploads. The URL is valid for 900 seconds (15 minutes) from the time of this response. If the location is not used within 15 minutes, the GUID will expire. Once expired, status checks on the GUID will return a status of `expired`.         * Note: If, after you've submitted a document, the status hasn't changed to `uploaded` before 15 minutes has elapsed, we recommend retrying the upload in order to make sure the document properly reaches our servers. If the upload continues to fail, try encoding the payload as Base64 (See below).   3. Client Request: PUT to the location URL returned in Step 2.     * Request body should be encoded as binary multipart/form-data (base64 also available - see details below), equivalent to that generated by an HTML form submission or using \"curl -F…\". The format is described in more detail below.     * No `apikey` authorization header is required for this request, as authorization is embedded in the signed location URL.  4. Service Response: The HTTP status indicates whether the upload was successful.     * Additionally, the response includes an ETag header containing an MD5 hash of the submitted payload. This can be compared to the submitted payload to ensure data integrity of the upload.  ### Status caching Due to current system limitations, data for the `/uploads/report` endpoint is cached for one hour.  A request to the `/uploads/{id}` endpoint will return a real-time status for that GUID, and update its status in `/uploads/report`.  The `updated_at` field indicates the last time the status for a given GUID was updated.  ### Document Submission Statuses **Important note:** a submission has not been received by VA until it has a status of Received, Processing, Success,  or VBMS. Detailed descriptions of what each status means are found in this table.  | Status        | What it means | | ---           |     ---     | | **Pending**   | Initial status.<br /><br />Indicates no document package has been uploaded yet.<br /><br />Date of Receipt is not yet established with this status | | **Uploaded**  | Indicates document package has been successfully uploaded (PUT) from your system to the API server but has not yet been validated.<br /><br />Date of Receipt is not yet established with this status. Any errors with the document package, such as having an unreadable PDF, may cause an Error status. | | **Received**  | Indicates document package has been received upstream of the API and is awaiting Processing.<br /><br />The VA Date of Receipt is set when this status is achieved.<br /><br />This is the final status in the sandbox environment unless further progress is simulated. | | **Processing**| Indicates the document package is being validated, processed, and made ready to route and work. | | **Success**   | Indicates the document package has been successfully received within VA's mail handling system.<br /><br />Success is the final status for a small percentage of submitted packages with claim types, Veteran types, or exception processes that are not worked in VBMS. Most submissions reach a Success status within 1 business day. A small portion will take longer; however, some submissions may take up to 2 weeks to reach a Success status. | | **VBMS**      | Indicates this document package was successfully uploaded into a Veteran's eFolder within VBMS.<br /><br />On average, submissions reach VBMS status within 3 business days; however, processing times vary and some submissions may remain in a Success status for several weeks before reaching a VBMS status.<br /><br />Some document packages are worked in VA systems other than VBMS. For these submissions, Success is the final status. | | **Error**     | Indicates that there was an error. Refer to the error code and message for further information. | | **Expired**   | After a POST request, there is a 15-minute window during which documents must be uploaded via a PUT request.<br /><br />An Expired status means the documents were not successfully uploaded within this 15-minute window. We recommend coding to retry unsuccessful uploads within 15 minutes using the same submission in case of connection issues. |  ### Optional Base64 encoding  Base64 is an encoding scheme that converts binary data into text format, so that encoded textual data can be easily transported over networks uncorrupted and without data loss.   Base64 can be used to encode binary multipart/form-data it in its entirety.  Note that the whole payload must be encoded, not individual parts/attachments.  After encoding your payload, you'll be required to preface your base64 string with `data:multipart/form-data;base64,` in order to allow our system to distinguish the file type. Your final string payload would look something like `data:multipart/form-data;base64,(encryption string)==` and close with the standard == marker.  Note that the multipart boundaries i.e. -----WebKitFormBoundaryVfOwzCyvug0JmWYo and ending ------WebKitFormBoundaryVfOwzCyvug0JmWYo- must also be included.  ### Consumer onboarding process When you're ready to move to production, [request a production API key.](https://developer.va.gov/go-live) 
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


package org.openapitools.client;

import com.google.gson.Gson;
import com.google.gson.GsonBuilder;
import com.google.gson.JsonParseException;
import com.google.gson.TypeAdapter;
import com.google.gson.internal.bind.util.ISO8601Utils;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import com.google.gson.JsonElement;
import io.gsonfire.GsonFireBuilder;
import io.gsonfire.TypeSelector;

import okio.ByteString;

import java.io.IOException;
import java.io.StringReader;
import java.lang.reflect.Type;
import java.text.DateFormat;
import java.text.ParseException;
import java.text.ParsePosition;
import java.time.LocalDate;
import java.time.OffsetDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Date;
import java.util.Locale;
import java.util.Map;
import java.util.HashMap;

/*
 * A JSON utility class
 *
 * NOTE: in the future, this class may be converted to static, which may break
 *       backward-compatibility
 */
public class JSON {
    private static Gson gson;
    private static boolean isLenientOnJson = false;
    private static DateTypeAdapter dateTypeAdapter = new DateTypeAdapter();
    private static SqlDateTypeAdapter sqlDateTypeAdapter = new SqlDateTypeAdapter();
    private static OffsetDateTimeTypeAdapter offsetDateTimeTypeAdapter = new OffsetDateTimeTypeAdapter();
    private static LocalDateTypeAdapter localDateTypeAdapter = new LocalDateTypeAdapter();
    private static ByteArrayAdapter byteArrayAdapter = new ByteArrayAdapter();

    @SuppressWarnings("unchecked")
    public static GsonBuilder createGson() {
        GsonFireBuilder fireBuilder = new GsonFireBuilder()
        ;
        GsonBuilder builder = fireBuilder.createGsonBuilder();
        return builder;
    }

    private static String getDiscriminatorValue(JsonElement readElement, String discriminatorField) {
        JsonElement element = readElement.getAsJsonObject().get(discriminatorField);
        if (null == element) {
            throw new IllegalArgumentException("missing discriminator field: <" + discriminatorField + ">");
        }
        return element.getAsString();
    }

    /**
     * Returns the Java class that implements the OpenAPI schema for the specified discriminator value.
     *
     * @param classByDiscriminatorValue The map of discriminator values to Java classes.
     * @param discriminatorValue The value of the OpenAPI discriminator in the input data.
     * @return The Java class that implements the OpenAPI schema
     */
    private static Class getClassByDiscriminator(Map classByDiscriminatorValue, String discriminatorValue) {
        Class clazz = (Class) classByDiscriminatorValue.get(discriminatorValue);
        if (null == clazz) {
            throw new IllegalArgumentException("cannot determine model class of name: <" + discriminatorValue + ">");
        }
        return clazz;
    }

    static {
        GsonBuilder gsonBuilder = createGson();
        gsonBuilder.registerTypeAdapter(Date.class, dateTypeAdapter);
        gsonBuilder.registerTypeAdapter(java.sql.Date.class, sqlDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(OffsetDateTime.class, offsetDateTimeTypeAdapter);
        gsonBuilder.registerTypeAdapter(LocalDate.class, localDateTypeAdapter);
        gsonBuilder.registerTypeAdapter(byte[].class, byteArrayAdapter);
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadAttributes.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadFailure.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadMetadata.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadPath.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadStatus.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadStatusAttributes.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadStatusGuidList.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadSubmission.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentUploadSubmissionAttributes.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.DocumentValidationErrorModel.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.ErrorModel.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetBenefitsDocumentUploadStatus200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetBenefitsDocumentUploadStatus404Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.GetBenefitsDocumentUploadStatusReport200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PdfDimensionAttributes.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PdfUploadAttributes.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PdfUploadAttributesContent.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PdfUploadAttributesContentAttachmentsInner.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBenefitsDocumentUpload202Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBenefitsDocumentUpload403Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBenefitsDocumentUploadValidateDocument200Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBenefitsDocumentUploadValidateDocument200ResponseData.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBenefitsDocumentUploadValidateDocument200ResponseDataAttributes.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PostBenefitsDocumentUploadValidateDocument422Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutBenefitsDocumentUpload401Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutBenefitsDocumentUpload422Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutBenefitsDocumentUpload429Response.CustomTypeAdapterFactory());
        gsonBuilder.registerTypeAdapterFactory(new org.openapitools.client.model.PutBenefitsDocumentUpload500Response.CustomTypeAdapterFactory());
        gson = gsonBuilder.create();
    }

    /**
     * Get Gson.
     *
     * @return Gson
     */
    public static Gson getGson() {
        return gson;
    }

    /**
     * Set Gson.
     *
     * @param gson Gson
     */
    public static void setGson(Gson gson) {
        JSON.gson = gson;
    }

    public static void setLenientOnJson(boolean lenientOnJson) {
        isLenientOnJson = lenientOnJson;
    }

    /**
     * Serialize the given Java object into JSON string.
     *
     * @param obj Object
     * @return String representation of the JSON
     */
    public static String serialize(Object obj) {
        return gson.toJson(obj);
    }

    /**
     * Deserialize the given JSON string to Java object.
     *
     * @param <T>        Type
     * @param body       The JSON string
     * @param returnType The type to deserialize into
     * @return The deserialized Java object
     */
    @SuppressWarnings("unchecked")
    public static <T> T deserialize(String body, Type returnType) {
        try {
            if (isLenientOnJson) {
                JsonReader jsonReader = new JsonReader(new StringReader(body));
                // see https://google-gson.googlecode.com/svn/trunk/gson/docs/javadocs/com/google/gson/stream/JsonReader.html#setLenient(boolean)
                jsonReader.setLenient(true);
                return gson.fromJson(jsonReader, returnType);
            } else {
                return gson.fromJson(body, returnType);
            }
        } catch (JsonParseException e) {
            // Fallback processing when failed to parse JSON form response body:
            // return the response body string directly for the String return type;
            if (returnType.equals(String.class)) {
                return (T) body;
            } else {
                throw (e);
            }
        }
    }

    /**
     * Gson TypeAdapter for Byte Array type
     */
    public static class ByteArrayAdapter extends TypeAdapter<byte[]> {

        @Override
        public void write(JsonWriter out, byte[] value) throws IOException {
            if (value == null) {
                out.nullValue();
            } else {
                out.value(ByteString.of(value).base64());
            }
        }

        @Override
        public byte[] read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String bytesAsBase64 = in.nextString();
                    ByteString byteString = ByteString.decodeBase64(bytesAsBase64);
                    return byteString.toByteArray();
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 OffsetDateTime type
     */
    public static class OffsetDateTimeTypeAdapter extends TypeAdapter<OffsetDateTime> {

        private DateTimeFormatter formatter;

        public OffsetDateTimeTypeAdapter() {
            this(DateTimeFormatter.ISO_OFFSET_DATE_TIME);
        }

        public OffsetDateTimeTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, OffsetDateTime date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public OffsetDateTime read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    if (date.endsWith("+0000")) {
                        date = date.substring(0, date.length()-5) + "Z";
                    }
                    return OffsetDateTime.parse(date, formatter);
            }
        }
    }

    /**
     * Gson TypeAdapter for JSR310 LocalDate type
     */
    public static class LocalDateTypeAdapter extends TypeAdapter<LocalDate> {

        private DateTimeFormatter formatter;

        public LocalDateTypeAdapter() {
            this(DateTimeFormatter.ISO_LOCAL_DATE);
        }

        public LocalDateTypeAdapter(DateTimeFormatter formatter) {
            this.formatter = formatter;
        }

        public void setFormat(DateTimeFormatter dateFormat) {
            this.formatter = dateFormat;
        }

        @Override
        public void write(JsonWriter out, LocalDate date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                out.value(formatter.format(date));
            }
        }

        @Override
        public LocalDate read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    return LocalDate.parse(date, formatter);
            }
        }
    }

    public static void setOffsetDateTimeFormat(DateTimeFormatter dateFormat) {
        offsetDateTimeTypeAdapter.setFormat(dateFormat);
    }

    public static void setLocalDateFormat(DateTimeFormatter dateFormat) {
        localDateTypeAdapter.setFormat(dateFormat);
    }

    /**
     * Gson TypeAdapter for java.sql.Date type
     * If the dateFormat is null, a simple "yyyy-MM-dd" format will be used
     * (more efficient than SimpleDateFormat).
     */
    public static class SqlDateTypeAdapter extends TypeAdapter<java.sql.Date> {

        private DateFormat dateFormat;

        public SqlDateTypeAdapter() {}

        public SqlDateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, java.sql.Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = date.toString();
                }
                out.value(value);
            }
        }

        @Override
        public java.sql.Date read(JsonReader in) throws IOException {
            switch (in.peek()) {
                case NULL:
                    in.nextNull();
                    return null;
                default:
                    String date = in.nextString();
                    try {
                        if (dateFormat != null) {
                            return new java.sql.Date(dateFormat.parse(date).getTime());
                        }
                        return new java.sql.Date(ISO8601Utils.parse(date, new ParsePosition(0)).getTime());
                    } catch (ParseException e) {
                        throw new JsonParseException(e);
                    }
            }
        }
    }

    /**
     * Gson TypeAdapter for java.util.Date type
     * If the dateFormat is null, ISO8601Utils will be used.
     */
    public static class DateTypeAdapter extends TypeAdapter<Date> {

        private DateFormat dateFormat;

        public DateTypeAdapter() {}

        public DateTypeAdapter(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        public void setFormat(DateFormat dateFormat) {
            this.dateFormat = dateFormat;
        }

        @Override
        public void write(JsonWriter out, Date date) throws IOException {
            if (date == null) {
                out.nullValue();
            } else {
                String value;
                if (dateFormat != null) {
                    value = dateFormat.format(date);
                } else {
                    value = ISO8601Utils.format(date, true);
                }
                out.value(value);
            }
        }

        @Override
        public Date read(JsonReader in) throws IOException {
            try {
                switch (in.peek()) {
                    case NULL:
                        in.nextNull();
                        return null;
                    default:
                        String date = in.nextString();
                        try {
                            if (dateFormat != null) {
                                return dateFormat.parse(date);
                            }
                            return ISO8601Utils.parse(date, new ParsePosition(0));
                        } catch (ParseException e) {
                            throw new JsonParseException(e);
                        }
                }
            } catch (IllegalArgumentException e) {
                throw new JsonParseException(e);
            }
        }
    }

    public static void setDateFormat(DateFormat dateFormat) {
        dateTypeAdapter.setFormat(dateFormat);
    }

    public static void setSqlDateFormat(DateFormat dateFormat) {
        sqlDateTypeAdapter.setFormat(dateFormat);
    }
}
