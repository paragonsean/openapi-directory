/**
 * Swiss NextGen Banking API-Framework
 * # Summary The **Swiss NextGen API** is based on the NextGenPSD2 *Framework Version 1.3.4* of the Berlin Group which offers a modern, open, harmonised and interoperable set of Application Programming Interfaces (APIs) as the safest and most efficient way to provide data securely. The NextGen Framework reduces XS2A complexity and costs, addresses the problem of multiple competing standards in Europe and, aligned with the goals of the Euro Retail Payments Board, enables European banking customers to benefit from innovative products and services ('Banking as a Service') by granting TPPs safe and secure (authenticated and authorised) access to their bank accounts and financial data.  The Swiss edtion refines the message formats specific to Switzerland and defines some matching examples.  The possible Approaches are:   * Redirect SCA Approach   * *(Not recommended by obp.ch community) OAuth SCA Approach*   * *(Not recommended by obp.ch community) Decoupled SCA Approach*   * *(Not recommended by obp.ch community) Embedded SCA Approach without SCA method*   * *(Not recommended by obp.ch community) Embedded SCA Approach with only one SCA method available*   * *(Not recommended by obp.ch community) Embedded SCA Approach with Selection of a SCA method*    Not every message defined in this API definition is necessary for all approaches.   Furthermore this API definition does not differ between methods which are mandatory, conditional, or optional   Therefore for a particular implementation of a compliant API it is only necessary to support   a certain subset of the methods defined in this API definition.    **Please have a look at the implementation guidelines if you are not sure   which message has to be used for the approach you are going to use.**  ## Some General Remarks Related to this version of the OpenAPI Specification: * **This API definition is based on the Implementation Guidelines of the [Berlin Group API](https://www.berlin-group.org/nextgenpsd2-downloads).**   It is not a replacement in any sense.   The main specification is (at the moment) always the Implementation Guidelines of the Berlin Group API. * **This API definition contains the REST-API for requests from the PISP to the ASPSP.** * **This API definition contains the messages for all different approaches defined in the Implementation Guidelines.** * According to the OpenAPI-Specification [https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.1.md]      \"If in is \"header\" and the name field is \"Accept\", \"Content-Type\" or \"Authorization\", the parameter definition SHALL be ignored.\"    The element \"Accept\" will not be defined in this file at any place.    The elements \"Content-Type\" and \"Authorization\" are implicitly defined by the OpenApi tags \"content\" and \"security\".  * There are several predefined types which might occur in payment initiation messages,   but are not used in the standard JSON messages in the Implementation Guidelines.   Therefore they are not used in the corresponding messages in this file either.   We added them for the convenience of the user.   If there is a payment product, which needs these fields, one can easily use the predefined types.   But the ASPSP need not to accept them in general.  * **We omit the definition of all standard HTTP header elements (mandatory/optional/conditional)   except they are mentioned in the Implementation Guidelines.**   Therefore the implementer might add these in his own realisation of a comlient API in addition to the elements defined in this file.  ## General Remarks on Data Types  The Berlin Group definition of UTF-8 strings in context of the API have to support at least the following characters  a b c d e f g h i j k l m n o p q r s t u v w x y z  A B C D E F G H I J K L M N O P Q R S T U V W X Y Z  0 1 2 3 4 5 6 7 8 9  / - ? : ( ) . , ' +  Space 
 *
 * The version of the OpenAPI document: 1.3.8_2020-12-14 - Swiss edition 1.3.8.1-CH
 * Contact: info@obp.ch
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIError406_AIS.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIError406_AIS::OAIError406_AIS(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIError406_AIS::OAIError406_AIS() {
    this->initializeModel();
}

OAIError406_AIS::~OAIError406_AIS() {}

void OAIError406_AIS::initializeModel() {

    m__links_isSet = false;
    m__links_isValid = false;

    m_additional_errors_isSet = false;
    m_additional_errors_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_detail_isSet = false;
    m_detail_isValid = false;

    m_title_isSet = false;
    m_title_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIError406_AIS::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIError406_AIS::fromJsonObject(QJsonObject json) {

    m__links_isValid = ::OpenAPI::fromJsonValue(m__links, json[QString("_links")]);
    m__links_isSet = !json[QString("_links")].isNull() && m__links_isValid;

    m_additional_errors_isValid = ::OpenAPI::fromJsonValue(m_additional_errors, json[QString("additionalErrors")]);
    m_additional_errors_isSet = !json[QString("additionalErrors")].isNull() && m_additional_errors_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_detail_isValid = ::OpenAPI::fromJsonValue(m_detail, json[QString("detail")]);
    m_detail_isSet = !json[QString("detail")].isNull() && m_detail_isValid;

    m_title_isValid = ::OpenAPI::fromJsonValue(m_title, json[QString("title")]);
    m_title_isSet = !json[QString("title")].isNull() && m_title_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIError406_AIS::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIError406_AIS::asJsonObject() const {
    QJsonObject obj;
    if (m__links.isSet()) {
        obj.insert(QString("_links"), ::OpenAPI::toJsonValue(m__links));
    }
    if (m_additional_errors.size() > 0) {
        obj.insert(QString("additionalErrors"), ::OpenAPI::toJsonValue(m_additional_errors));
    }
    if (m_code.isSet()) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_detail_isSet) {
        obj.insert(QString("detail"), ::OpenAPI::toJsonValue(m_detail));
    }
    if (m_title_isSet) {
        obj.insert(QString("title"), ::OpenAPI::toJsonValue(m_title));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

OAI_linksAll OAIError406_AIS::getLinks() const {
    return m__links;
}
void OAIError406_AIS::setLinks(const OAI_linksAll &_links) {
    m__links = _links;
    m__links_isSet = true;
}

bool OAIError406_AIS::is__links_Set() const{
    return m__links_isSet;
}

bool OAIError406_AIS::is__links_Valid() const{
    return m__links_isValid;
}

QList<OAIError406_AIS_additionalErrors_inner> OAIError406_AIS::getAdditionalErrors() const {
    return m_additional_errors;
}
void OAIError406_AIS::setAdditionalErrors(const QList<OAIError406_AIS_additionalErrors_inner> &additional_errors) {
    m_additional_errors = additional_errors;
    m_additional_errors_isSet = true;
}

bool OAIError406_AIS::is_additional_errors_Set() const{
    return m_additional_errors_isSet;
}

bool OAIError406_AIS::is_additional_errors_Valid() const{
    return m_additional_errors_isValid;
}

OAIMessageCode406_AIS OAIError406_AIS::getCode() const {
    return m_code;
}
void OAIError406_AIS::setCode(const OAIMessageCode406_AIS &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAIError406_AIS::is_code_Set() const{
    return m_code_isSet;
}

bool OAIError406_AIS::is_code_Valid() const{
    return m_code_isValid;
}

QString OAIError406_AIS::getDetail() const {
    return m_detail;
}
void OAIError406_AIS::setDetail(const QString &detail) {
    m_detail = detail;
    m_detail_isSet = true;
}

bool OAIError406_AIS::is_detail_Set() const{
    return m_detail_isSet;
}

bool OAIError406_AIS::is_detail_Valid() const{
    return m_detail_isValid;
}

QString OAIError406_AIS::getTitle() const {
    return m_title;
}
void OAIError406_AIS::setTitle(const QString &title) {
    m_title = title;
    m_title_isSet = true;
}

bool OAIError406_AIS::is_title_Set() const{
    return m_title_isSet;
}

bool OAIError406_AIS::is_title_Valid() const{
    return m_title_isValid;
}

QString OAIError406_AIS::getType() const {
    return m_type;
}
void OAIError406_AIS::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIError406_AIS::is_type_Set() const{
    return m_type_isSet;
}

bool OAIError406_AIS::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIError406_AIS::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m__links.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_additional_errors.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_code.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_detail_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_title_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_type_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIError406_AIS::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_code_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
