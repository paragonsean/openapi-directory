/**
 * Authorized Partner API Specification
 * To access files in user’s DigiLocker account from your application, you must first obtain user’s authorization.
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: support@digitallocker.gov.in
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIEaadharXamlSchema_KycRes_UidData_Prn.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIEaadharXamlSchema_KycRes_UidData_Prn::OAIEaadharXamlSchema_KycRes_UidData_Prn(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIEaadharXamlSchema_KycRes_UidData_Prn::OAIEaadharXamlSchema_KycRes_UidData_Prn() {
    this->initializeModel();
}

OAIEaadharXamlSchema_KycRes_UidData_Prn::~OAIEaadharXamlSchema_KycRes_UidData_Prn() {}

void OAIEaadharXamlSchema_KycRes_UidData_Prn::initializeModel() {

    m_text_isSet = false;
    m_text_isValid = false;

    m_type_isSet = false;
    m_type_isValid = false;
}

void OAIEaadharXamlSchema_KycRes_UidData_Prn::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIEaadharXamlSchema_KycRes_UidData_Prn::fromJsonObject(QJsonObject json) {

    m_text_isValid = ::OpenAPI::fromJsonValue(m_text, json[QString("text")]);
    m_text_isSet = !json[QString("text")].isNull() && m_text_isValid;

    m_type_isValid = ::OpenAPI::fromJsonValue(m_type, json[QString("type")]);
    m_type_isSet = !json[QString("type")].isNull() && m_type_isValid;
}

QString OAIEaadharXamlSchema_KycRes_UidData_Prn::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIEaadharXamlSchema_KycRes_UidData_Prn::asJsonObject() const {
    QJsonObject obj;
    if (m_text_isSet) {
        obj.insert(QString("text"), ::OpenAPI::toJsonValue(m_text));
    }
    if (m_type_isSet) {
        obj.insert(QString("type"), ::OpenAPI::toJsonValue(m_type));
    }
    return obj;
}

QString OAIEaadharXamlSchema_KycRes_UidData_Prn::getText() const {
    return m_text;
}
void OAIEaadharXamlSchema_KycRes_UidData_Prn::setText(const QString &text) {
    m_text = text;
    m_text_isSet = true;
}

bool OAIEaadharXamlSchema_KycRes_UidData_Prn::is_text_Set() const{
    return m_text_isSet;
}

bool OAIEaadharXamlSchema_KycRes_UidData_Prn::is_text_Valid() const{
    return m_text_isValid;
}

QString OAIEaadharXamlSchema_KycRes_UidData_Prn::getType() const {
    return m_type;
}
void OAIEaadharXamlSchema_KycRes_UidData_Prn::setType(const QString &type) {
    m_type = type;
    m_type_isSet = true;
}

bool OAIEaadharXamlSchema_KycRes_UidData_Prn::is_type_Set() const{
    return m_type_isSet;
}

bool OAIEaadharXamlSchema_KycRes_UidData_Prn::is_type_Valid() const{
    return m_type_isValid;
}

bool OAIEaadharXamlSchema_KycRes_UidData_Prn::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_text_isSet) {
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

bool OAIEaadharXamlSchema_KycRes_UidData_Prn::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_text_isValid && m_type_isValid && true;
}

} // namespace OpenAPI
