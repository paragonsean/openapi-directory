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

#include "OAITemplateDefinitionNew_layout.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITemplateDefinitionNew_layout::OAITemplateDefinitionNew_layout(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITemplateDefinitionNew_layout::OAITemplateDefinitionNew_layout() {
    this->initializeModel();
}

OAITemplateDefinitionNew_layout::~OAITemplateDefinitionNew_layout() {}

void OAITemplateDefinitionNew_layout::initializeModel() {

    m_empty_labels_isSet = false;
    m_empty_labels_isValid = false;

    m_format_isSet = false;
    m_format_isValid = false;

    m_height_isSet = false;
    m_height_isValid = false;

    m_margins_isSet = false;
    m_margins_isValid = false;

    m_orientation_isSet = false;
    m_orientation_isValid = false;

    m_repeat_layout_isSet = false;
    m_repeat_layout_isValid = false;

    m_rotaion_isSet = false;
    m_rotaion_isValid = false;

    m_unit_isSet = false;
    m_unit_isValid = false;

    m_width_isSet = false;
    m_width_isValid = false;
}

void OAITemplateDefinitionNew_layout::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITemplateDefinitionNew_layout::fromJsonObject(QJsonObject json) {

    m_empty_labels_isValid = ::OpenAPI::fromJsonValue(m_empty_labels, json[QString("emptyLabels")]);
    m_empty_labels_isSet = !json[QString("emptyLabels")].isNull() && m_empty_labels_isValid;

    m_format_isValid = ::OpenAPI::fromJsonValue(m_format, json[QString("format")]);
    m_format_isSet = !json[QString("format")].isNull() && m_format_isValid;

    m_height_isValid = ::OpenAPI::fromJsonValue(m_height, json[QString("height")]);
    m_height_isSet = !json[QString("height")].isNull() && m_height_isValid;

    m_margins_isValid = ::OpenAPI::fromJsonValue(m_margins, json[QString("margins")]);
    m_margins_isSet = !json[QString("margins")].isNull() && m_margins_isValid;

    m_orientation_isValid = ::OpenAPI::fromJsonValue(m_orientation, json[QString("orientation")]);
    m_orientation_isSet = !json[QString("orientation")].isNull() && m_orientation_isValid;

    m_repeat_layout_isValid = ::OpenAPI::fromJsonValue(m_repeat_layout, json[QString("repeatLayout")]);
    m_repeat_layout_isSet = !json[QString("repeatLayout")].isNull() && m_repeat_layout_isValid;

    m_rotaion_isValid = ::OpenAPI::fromJsonValue(m_rotaion, json[QString("rotaion")]);
    m_rotaion_isSet = !json[QString("rotaion")].isNull() && m_rotaion_isValid;

    m_unit_isValid = ::OpenAPI::fromJsonValue(m_unit, json[QString("unit")]);
    m_unit_isSet = !json[QString("unit")].isNull() && m_unit_isValid;

    m_width_isValid = ::OpenAPI::fromJsonValue(m_width, json[QString("width")]);
    m_width_isSet = !json[QString("width")].isNull() && m_width_isValid;
}

QString OAITemplateDefinitionNew_layout::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITemplateDefinitionNew_layout::asJsonObject() const {
    QJsonObject obj;
    if (m_empty_labels_isSet) {
        obj.insert(QString("emptyLabels"), ::OpenAPI::toJsonValue(m_empty_labels));
    }
    if (m_format_isSet) {
        obj.insert(QString("format"), ::OpenAPI::toJsonValue(m_format));
    }
    if (m_height_isSet) {
        obj.insert(QString("height"), ::OpenAPI::toJsonValue(m_height));
    }
    if (m_margins.isSet()) {
        obj.insert(QString("margins"), ::OpenAPI::toJsonValue(m_margins));
    }
    if (m_orientation_isSet) {
        obj.insert(QString("orientation"), ::OpenAPI::toJsonValue(m_orientation));
    }
    if (m_repeat_layout.isSet()) {
        obj.insert(QString("repeatLayout"), ::OpenAPI::toJsonValue(m_repeat_layout));
    }
    if (m_rotaion_isSet) {
        obj.insert(QString("rotaion"), ::OpenAPI::toJsonValue(m_rotaion));
    }
    if (m_unit_isSet) {
        obj.insert(QString("unit"), ::OpenAPI::toJsonValue(m_unit));
    }
    if (m_width_isSet) {
        obj.insert(QString("width"), ::OpenAPI::toJsonValue(m_width));
    }
    return obj;
}

qint32 OAITemplateDefinitionNew_layout::getEmptyLabels() const {
    return m_empty_labels;
}
void OAITemplateDefinitionNew_layout::setEmptyLabels(const qint32 &empty_labels) {
    m_empty_labels = empty_labels;
    m_empty_labels_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_empty_labels_Set() const{
    return m_empty_labels_isSet;
}

bool OAITemplateDefinitionNew_layout::is_empty_labels_Valid() const{
    return m_empty_labels_isValid;
}

QString OAITemplateDefinitionNew_layout::getFormat() const {
    return m_format;
}
void OAITemplateDefinitionNew_layout::setFormat(const QString &format) {
    m_format = format;
    m_format_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_format_Set() const{
    return m_format_isSet;
}

bool OAITemplateDefinitionNew_layout::is_format_Valid() const{
    return m_format_isValid;
}

double OAITemplateDefinitionNew_layout::getHeight() const {
    return m_height;
}
void OAITemplateDefinitionNew_layout::setHeight(const double &height) {
    m_height = height;
    m_height_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_height_Set() const{
    return m_height_isSet;
}

bool OAITemplateDefinitionNew_layout::is_height_Valid() const{
    return m_height_isValid;
}

OAITemplateDefinition_layout_margins OAITemplateDefinitionNew_layout::getMargins() const {
    return m_margins;
}
void OAITemplateDefinitionNew_layout::setMargins(const OAITemplateDefinition_layout_margins &margins) {
    m_margins = margins;
    m_margins_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_margins_Set() const{
    return m_margins_isSet;
}

bool OAITemplateDefinitionNew_layout::is_margins_Valid() const{
    return m_margins_isValid;
}

QString OAITemplateDefinitionNew_layout::getOrientation() const {
    return m_orientation;
}
void OAITemplateDefinitionNew_layout::setOrientation(const QString &orientation) {
    m_orientation = orientation;
    m_orientation_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_orientation_Set() const{
    return m_orientation_isSet;
}

bool OAITemplateDefinitionNew_layout::is_orientation_Valid() const{
    return m_orientation_isValid;
}

OAITemplateDefinition_layout_repeatLayout OAITemplateDefinitionNew_layout::getRepeatLayout() const {
    return m_repeat_layout;
}
void OAITemplateDefinitionNew_layout::setRepeatLayout(const OAITemplateDefinition_layout_repeatLayout &repeat_layout) {
    m_repeat_layout = repeat_layout;
    m_repeat_layout_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_repeat_layout_Set() const{
    return m_repeat_layout_isSet;
}

bool OAITemplateDefinitionNew_layout::is_repeat_layout_Valid() const{
    return m_repeat_layout_isValid;
}

qint32 OAITemplateDefinitionNew_layout::getRotaion() const {
    return m_rotaion;
}
void OAITemplateDefinitionNew_layout::setRotaion(const qint32 &rotaion) {
    m_rotaion = rotaion;
    m_rotaion_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_rotaion_Set() const{
    return m_rotaion_isSet;
}

bool OAITemplateDefinitionNew_layout::is_rotaion_Valid() const{
    return m_rotaion_isValid;
}

QString OAITemplateDefinitionNew_layout::getUnit() const {
    return m_unit;
}
void OAITemplateDefinitionNew_layout::setUnit(const QString &unit) {
    m_unit = unit;
    m_unit_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_unit_Set() const{
    return m_unit_isSet;
}

bool OAITemplateDefinitionNew_layout::is_unit_Valid() const{
    return m_unit_isValid;
}

double OAITemplateDefinitionNew_layout::getWidth() const {
    return m_width;
}
void OAITemplateDefinitionNew_layout::setWidth(const double &width) {
    m_width = width;
    m_width_isSet = true;
}

bool OAITemplateDefinitionNew_layout::is_width_Set() const{
    return m_width_isSet;
}

bool OAITemplateDefinitionNew_layout::is_width_Valid() const{
    return m_width_isValid;
}

bool OAITemplateDefinitionNew_layout::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_empty_labels_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_format_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_height_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_margins.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_orientation_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_repeat_layout.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_rotaion_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unit_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_width_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITemplateDefinitionNew_layout::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
