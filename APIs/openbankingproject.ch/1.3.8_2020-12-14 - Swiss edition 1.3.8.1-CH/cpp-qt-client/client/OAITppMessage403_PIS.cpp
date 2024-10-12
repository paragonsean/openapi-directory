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

#include "OAITppMessage403_PIS.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAITppMessage403_PIS::OAITppMessage403_PIS(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAITppMessage403_PIS::OAITppMessage403_PIS() {
    this->initializeModel();
}

OAITppMessage403_PIS::~OAITppMessage403_PIS() {}

void OAITppMessage403_PIS::initializeModel() {

    m_category_isSet = false;
    m_category_isValid = false;

    m_code_isSet = false;
    m_code_isValid = false;

    m_path_isSet = false;
    m_path_isValid = false;

    m_text_isSet = false;
    m_text_isValid = false;
}

void OAITppMessage403_PIS::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAITppMessage403_PIS::fromJsonObject(QJsonObject json) {

    m_category_isValid = ::OpenAPI::fromJsonValue(m_category, json[QString("category")]);
    m_category_isSet = !json[QString("category")].isNull() && m_category_isValid;

    m_code_isValid = ::OpenAPI::fromJsonValue(m_code, json[QString("code")]);
    m_code_isSet = !json[QString("code")].isNull() && m_code_isValid;

    m_path_isValid = ::OpenAPI::fromJsonValue(m_path, json[QString("path")]);
    m_path_isSet = !json[QString("path")].isNull() && m_path_isValid;

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;
}

QString OAITppMessage403_PIS::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAITppMessage403_PIS::asJsonObject() const {
    QJsonObject obj;
    if (m_category.isSet()) {
        obj.insert(QString("category"), ::OpenAPI::toJsonValue(m_category));
    }
    if (m_code.isSet()) {
        obj.insert(QString("code"), ::OpenAPI::toJsonValue(m_code));
    }
    if (m_path_isSet) {
        obj.insert(QString("path"), ::OpenAPI::toJsonValue(m_path));
    }
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    return obj;
}

OAITppMessageCategory OAITppMessage403_PIS::getCategory() const {
    return m_category;
}
void OAITppMessage403_PIS::setCategory(const OAITppMessageCategory &category) {
    m_category = category;
    m_category_isSet = true;
}

bool OAITppMessage403_PIS::is_category_Set() const{
    return m_category_isSet;
}

bool OAITppMessage403_PIS::is_category_Valid() const{
    return m_category_isValid;
}

OAIMessageCode403_PIS OAITppMessage403_PIS::getCode() const {
    return m_code;
}
void OAITppMessage403_PIS::setCode(const OAIMessageCode403_PIS &code) {
    m_code = code;
    m_code_isSet = true;
}

bool OAITppMessage403_PIS::is_code_Set() const{
    return m_code_isSet;
}

bool OAITppMessage403_PIS::is_code_Valid() const{
    return m_code_isValid;
}

QString OAITppMessage403_PIS::getPath() const {
    return m_path;
}
void OAITppMessage403_PIS::setPath(const QString &path) {
    m_path = path;
    m_path_isSet = true;
}

bool OAITppMessage403_PIS::is_path_Set() const{
    return m_path_isSet;
}

bool OAITppMessage403_PIS::is_path_Valid() const{
    return m_path_isValid;
}

QString OAITppMessage403_PIS::getText() const {
    return m_text;
}
void OAITppMessage403_PIS::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAITppMessage403_PIS::is_text_Set() const{
    return m_text_isSet;
}

bool OAITppMessage403_PIS::is_text_Valid() const{
    return m_text_isValid;
}

bool OAITppMessage403_PIS::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_category.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_code.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_path_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_text_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAITppMessage403_PIS::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_category_isValid && m_code_isValid && true;
}

} // namespace OpenAPI
