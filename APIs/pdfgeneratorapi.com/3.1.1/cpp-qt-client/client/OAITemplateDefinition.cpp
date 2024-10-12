/**
 * PDF Generator API
 * # Introduction PDF Generator API allows you easily generate transactional PDF documents and reduce the development and support costs by enabling your users to create and manage their document templates using a browser-based drag-and-drop document editor.  The PDF Generator API features a web API architecture, allowing you to code in the language of your choice. This API supports the JSON media type, and uses UTF-8 character encoding.  You can find our previous API documentation page with references to Simple and Signature authentication [here](https://docs.pdfgeneratorapi.com/legacy).  ## Base URL The base URL for all the API endpoints is `https://us1.pdfgeneratorapi.com/api/v3`  For example * `https://us1.pdfgeneratorapi.com/api/v3/templates` * `https://us1.pdfgeneratorapi.com/api/v3/workspaces` * `https://us1.pdfgeneratorapi.com/api/v3/templates/123123`  ## Editor PDF Generator API comes with a powerful drag & drop editor that allows to create any kind of document templates, from barcode labels to invoices, quotes and reports. You can find tutorials and videos from our [Support Portal](https://support.pdfgeneratorapi.com). * [Component specification](https://support.pdfgeneratorapi.com/en/category/components-1ffseaj/) * [Expression Language documentation](https://support.pdfgeneratorapi.com/en/category/expression-language-q203pa/) * [Frequently asked questions and answers](https://support.pdfgeneratorapi.com/en/category/qanda-1ov519d/)  ## Definitions  ### Organization Organization is a group of workspaces owned by your account.  ### Workspace Workspace contains templates. Each workspace has access to their own templates and organization default templates.  ### Master Workspace Master Workspace is the main/default workspace of your Organization. The Master Workspace identifier is the email you signed up with.  ### Default Template Default template is a template that is available for all workspaces by default. You can set the template access type under Page Setup. If template has \"Organization\" access then your users can use them from the \"New\" menu in the Editor.  ### Data Field Data Field is a placeholder for the specific data in your JSON data set. In this example JSON you can access the buyer name using Data Field `{paymentDetails::buyerName}`. The separator between depth levels is :: (two colons). When designing the template you don’t have to know every Data Field, our editor automatically extracts all the available fields from your data set and provides an easy way to insert them into the template. ``` {     \"documentNumber\": 1,     \"paymentDetails\": {         \"method\": \"Credit Card\",         \"buyerName\": \"John Smith\"     },     \"items\": [         {             \"id\": 1,             \"name\": \"Item one\"         }     ] } ```  *  *  *  *  * # Authentication The PDF Generator API uses __JSON Web Tokens (JWT)__ to authenticate all API requests. These tokens offer a method to establish secure server-to-server authentication by transferring a compact JSON object with a signed payload of your account’s API Key and Secret. When authenticating to the PDF Generator API, a JWT should be generated uniquely by a __server-side application__ and included as a __Bearer Token__ in the header of each request.  ## Legacy Simple and Signature authentication You can find our legacy documentation for Simple and Signature authentication [here](https://docs.pdfgeneratorapi.com/legacy).  <SecurityDefinitions />  ## Accessing your API Key and Secret You can find your __API Key__ and __API Secret__ from the __Account Settings__ page after you login to PDF Generator API [here](https://pdfgeneratorapi.com/login).  ## Creating a JWT JSON Web Tokens are composed of three sections: a header, a payload (containing a claim set), and a signature. The header and payload are JSON objects, which are serialized to UTF-8 bytes, then encoded using base64url encoding.  The JWT's header, payload, and signature are concatenated with periods (.). As a result, a JWT typically takes the following form: ``` {Base64url encoded header}.{Base64url encoded payload}.{Base64url encoded signature} ```  We recommend and support libraries provided on [jwt.io](https://jwt.io/). While other libraries can create JWT, these recommended libraries are the most robust.  ### Header Property `alg` defines which signing algorithm is being used. PDF Generator API users HS256. Property `typ` defines the type of token and it is always JWT. ``` {   \"alg\": \"HS256\",   \"typ\": \"JWT\" } ```  ### Payload The second part of the token is the payload, which contains the claims  or the pieces of information being passed about the user and any metadata required. It is mandatory to specify the following claims: * issuer (`iss`): Your API key * subject (`sub`): Workspace identifier * expiration time (`exp`): Timestamp (unix epoch time) until the token is valid. It is highly recommended to set the exp timestamp for a short period, i.e. a matter of seconds. This way, if a token is intercepted or shared, the token will only be valid for a short period of time.  ``` {   \"iss\": \"ad54aaff89ffdfeff178bb8a8f359b29fcb20edb56250b9f584aa2cb0162ed4a\",   \"sub\": \"demo.example@actualreports.com\",   \"exp\": 1586112639 } ```  ### Signature To create the signature part you have to take the encoded header, the encoded payload, a secret, the algorithm specified in the header, and sign that. The signature is used to verify the message wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is. ``` HMACSHA256(     base64UrlEncode(header) + \".\" +     base64UrlEncode(payload),     API_SECRET) ```  ### Putting all together The output is three Base64-URL strings separated by dots. The following shows a JWT that has the previous header and payload encoded, and it is signed with a secret. ``` eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0.SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q  // Base64 encoded header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9 // Base64 encoded payload: eyJpc3MiOiJhZDU0YWFmZjg5ZmZkZmVmZjE3OGJiOGE4ZjM1OWIyOWZjYjIwZWRiNTYyNTBiOWY1ODRhYTJjYjAxNjJlZDRhIiwic3ViIjoiZGVtby5leGFtcGxlQGFjdHVhbHJlcG9ydHMuY29tIn0 // Signature: SxO-H7UYYYsclS8RGWO1qf0z1cB1m73wF9FLl9RCc1Q ```  ## Testing with JWTs You can create a temporary token in [Account Settings](https://pdfgeneratorapi.com/account/organization) page after you login to PDF Generator API. The generated token uses your email address as the subject (`sub`) value and is valid for __5 minutes__. You can also use [jwt.io](https://jwt.io/) to generate test tokens for your API calls. These test tokens should never be used in production applications. *  *  *  *  *  # Libraries and SDKs ## Postman Collection We have created a [Postman](https://www.postman.com) Collection so you can easily test all the API endpoints wihtout developing and code. You can download the collection [here](https://app.getpostman.com/run-collection/329f09618ec8a957dbc4) or just click the button below.  [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/329f09618ec8a957dbc4)  ## Client Libraries All our Client Libraries are auto-generated using [OpenAPI Generator](https://openapi-generator.tech/) which uses the OpenAPI v3 specification to automatically generate a client library in specific programming language.  * [PHP Client](https://github.com/pdfgeneratorapi/php-client) * [Java Client](https://github.com/pdfgeneratorapi/java-client) * [Ruby Client](https://github.com/pdfgeneratorapi/ruby-client) * [Python Client](https://github.com/pdfgeneratorapi/python-client) * [Javascript Client](https://github.com/pdfgeneratorapi/javascript-client)  We have validated the generated libraries, but let us know if you find any anomalies in the client code. *  *  *  *  *  # Error codes  | Code   | Description                    | |--------|--------------------------------| | 401    | Unauthorized                   | | 403    | Forbidden                      | | 404    | Not Found                      | | 422    | Unprocessable Entity           | | 500    | Internal Server Error          |  ## 401 - Unauthorized | Description                                                             | |-------------------------------------------------------------------------| | Authentication failed: request expired                                  | | Authentication failed: workspace missing                                | | Authentication failed: key missing                                      | | Authentication failed: property 'iss' (issuer) missing in JWT           | | Authentication failed: property 'sub' (subject) missing in JWT          | | Authentication failed: property 'exp' (expiration time) missing in JWT  | | Authentication failed: incorrect signature                              |  ## 403 - Forbidden | Description                                                             | |-------------------------------------------------------------------------| | Your account has exceeded the monthly document generation limit.        | | Access not granted: You cannot delete master workspace via API          | | Access not granted: Template is not accessible by this organization     | | Your session has expired, please close and reopen the editor.           |  ## 404 Entity not found | Description                                                             | |-------------------------------------------------------------------------| | Entity not found                                                        | | Resource not found                                                      | | None of the templates is available for the workspace.                   |  ## 422 Unprocessable Entity | Description                                                             | |-------------------------------------------------------------------------| | Unable to parse JSON, please check formatting                           | | Required parameter missing                                              | | Required parameter missing: template definition not defined             | | Required parameter missing: template not defined                        | 
 *
 * The version of the OpenAPI document: 3.1.1
 * Contact: support@pdfgeneratorapi.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAITemplateDefinition.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITemplateDefinition::OAITemplateDefinition(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITemplateDefinition::OAITemplateDefinition() {
    this->initializeModel();
}

OAITemplateDefinition::~OAITemplateDefinition() {}

void OAITemplateDefinition::initializeModel() {

    m_data_settings_isSet = false;
    m_data_settings_isValid = false;

    m_editor_isSet = false;
    m_editor_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_is_draft_isSet = false;
    m_is_draft_isValid = false;

    m_layout_isSet = false;
    m_layout_isValid = false;

    m_name_isSet = false;
    m_name_isValid = false;

    m_pages_isSet = false;
    m_pages_isValid = false;

    m_tags_isSet = false;
    m_tags_isValid = false;
}

void OAITemplateDefinition::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITemplateDefinition::fromJsonObject(QJsonObject json) {

    m_data_settings_isValid = ::OpenAPI::fromJsonValue(m_data_settings, json[QString("dataSettings")]);
    m_data_settings_isSet = !json[QString("dataSettings")].isNull() && m_data_settings_isValid;

    m_editor_isValid = ::OpenAPI::fromJsonValue(m_editor, json[QString("editor")]);
    m_editor_isSet = !json[QString("editor")].isNull() && m_editor_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_is_draft_isValid = ::OpenAPI::fromJsonValue(m_is_draft, json[QString("isDraft")]);
    m_is_draft_isSet = !json[QString("isDraft")].isNull() && m_is_draft_isValid;

    m_layout_isValid = ::OpenAPI::fromJsonValue(m_layout, json[QString("layout")]);
    m_layout_isSet = !json[QString("layout")].isNull() && m_layout_isValid;

    m_name_isValid = ::OpenAPI::fromJsonValue(m_name, json[QString("name")]);
    m_name_isSet = !json[QString("name")].isNull() && m_name_isValid;

    m_pages_isValid = ::OpenAPI::fromJsonValue(m_pages, json[QString("pages")]);
    m_pages_isSet = !json[QString("pages")].isNull() && m_pages_isValid;

    m_tags_isValid = ::OpenAPI::fromJsonValue(m_tags, json[QString("tags")]);
    m_tags_isSet = !json[QString("tags")].isNull() && m_tags_isValid;
}

QString OAITemplateDefinition::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITemplateDefinition::asJsonObject() const {
    QJsonObject obj;
    if (m_data_settings.isSet()) {
        obj.insert(QString("dataSettings"), ::OpenAPI::toJsonValue(m_data_settings));
    }
    if (m_editor.isSet()) {
        obj.insert(QString("editor"), ::OpenAPI::toJsonValue(m_editor));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_is_draft_isSet) {
        obj.insert(QString("isDraft"), ::OpenAPI::toJsonValue(m_is_draft));
    }
    if (m_layout.isSet()) {
        obj.insert(QString("layout"), ::OpenAPI::toJsonValue(m_layout));
    }
    if (m_name_isSet) {
        obj.insert(QString("name"), ::OpenAPI::toJsonValue(m_name));
    }
    if (m_pages.size() > 0) {
        obj.insert(QString("pages"), ::OpenAPI::toJsonValue(m_pages));
    }
    if (m_tags.size() > 0) {
        obj.insert(QString("tags"), ::OpenAPI::toJsonValue(m_tags));
    }
    return obj;
}

OAITemplateDefinition_dataSettings OAITemplateDefinition::getDataSettings() const {
    return m_data_settings;
}
void OAITemplateDefinition::setDataSettings(const OAITemplateDefinition_dataSettings &data_settings) {
    m_data_settings = data_settings;
    m_data_settings_isSet = true;
}

bool OAITemplateDefinition::is_data_settings_Set() const{
    return m_data_settings_isSet;
}

bool OAITemplateDefinition::is_data_settings_Valid() const{
    return m_data_settings_isValid;
}

OAITemplateDefinition_editor OAITemplateDefinition::getEditor() const {
    return m_editor;
}
void OAITemplateDefinition::setEditor(const OAITemplateDefinition_editor &editor) {
    m_editor = editor;
    m_editor_isSet = true;
}

bool OAITemplateDefinition::is_editor_Set() const{
    return m_editor_isSet;
}

bool OAITemplateDefinition::is_editor_Valid() const{
    return m_editor_isValid;
}

qint32 OAITemplateDefinition::getId() const {
    return m_id;
}
void OAITemplateDefinition::setId(const qint32 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAITemplateDefinition::is_id_Set() const{
    return m_id_isSet;
}

bool OAITemplateDefinition::is_id_Valid() const{
    return m_id_isValid;
}

bool OAITemplateDefinition::isIsDraft() const {
    return m_is_draft;
}
void OAITemplateDefinition::setIsDraft(const bool &is_draft) {
    m_is_draft = is_draft;
    m_is_draft_isSet = true;
}

bool OAITemplateDefinition::is_is_draft_Set() const{
    return m_is_draft_isSet;
}

bool OAITemplateDefinition::is_is_draft_Valid() const{
    return m_is_draft_isValid;
}

OAITemplateDefinition_layout OAITemplateDefinition::getLayout() const {
    return m_layout;
}
void OAITemplateDefinition::setLayout(const OAITemplateDefinition_layout &layout) {
    m_layout = layout;
    m_layout_isSet = true;
}

bool OAITemplateDefinition::is_layout_Set() const{
    return m_layout_isSet;
}

bool OAITemplateDefinition::is_layout_Valid() const{
    return m_layout_isValid;
}

QString OAITemplateDefinition::getName() const {
    return m_name;
}
void OAITemplateDefinition::setName(const QString &name) {
    m_name = name;
    m_name_isSet = true;
}

bool OAITemplateDefinition::is_name_Set() const{
    return m_name_isSet;
}

bool OAITemplateDefinition::is_name_Valid() const{
    return m_name_isValid;
}

QList<OAITemplateDefinition_pages_inner> OAITemplateDefinition::getPages() const {
    return m_pages;
}
void OAITemplateDefinition::setPages(const QList<OAITemplateDefinition_pages_inner> &pages) {
    m_pages = pages;
    m_pages_isSet = true;
}

bool OAITemplateDefinition::is_pages_Set() const{
    return m_pages_isSet;
}

bool OAITemplateDefinition::is_pages_Valid() const{
    return m_pages_isValid;
}

QList<QString> OAITemplateDefinition::getTags() const {
    return m_tags;
}
void OAITemplateDefinition::setTags(const QList<QString> &tags) {
    m_tags = tags;
    m_tags_isSet = true;
}

bool OAITemplateDefinition::is_tags_Set() const{
    return m_tags_isSet;
}

bool OAITemplateDefinition::is_tags_Valid() const{
    return m_tags_isValid;
}

bool OAITemplateDefinition::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data_settings.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_editor.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_is_draft_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_layout.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_name_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_pages.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_tags.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITemplateDefinition::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
