/**
 * Flight Availibilities Search
 *  Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production, if you are not returning any results try with big cities/airports like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.2
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISuccess_Availability.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISuccess_Availability::OAISuccess_Availability(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISuccess_Availability::OAISuccess_Availability() {
    this->initializeModel();
}

OAISuccess_Availability::~OAISuccess_Availability() {}

void OAISuccess_Availability::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;

    m_dictionaries_isSet = false;
    m_dictionaries_isValid = false;

    m_meta_isSet = false;
    m_meta_isValid = false;

    m_warnings_isSet = false;
    m_warnings_isValid = false;
}

void OAISuccess_Availability::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISuccess_Availability::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;

    m_dictionaries_isValid = ::OpenAPI::fromJsonValue(m_dictionaries, json[QString("dictionaries")]);
    m_dictionaries_isSet = !json[QString("dictionaries")].isNull() && m_dictionaries_isValid;

    m_meta_isValid = ::OpenAPI::fromJsonValue(m_meta, json[QString("meta")]);
    m_meta_isSet = !json[QString("meta")].isNull() && m_meta_isValid;

    m_warnings_isValid = ::OpenAPI::fromJsonValue(m_warnings, json[QString("warnings")]);
    m_warnings_isSet = !json[QString("warnings")].isNull() && m_warnings_isValid;
}

QString OAISuccess_Availability::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISuccess_Availability::asJsonObject() const {
    QJsonObject obj;
    if (m_data.size() > 0) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    if (m_dictionaries.isSet()) {
        obj.insert(QString("dictionaries"), ::OpenAPI::toJsonValue(m_dictionaries));
    }
    if (m_meta.isSet()) {
        obj.insert(QString("meta"), ::OpenAPI::toJsonValue(m_meta));
    }
    if (m_warnings.size() > 0) {
        obj.insert(QString("warnings"), ::OpenAPI::toJsonValue(m_warnings));
    }
    return obj;
}

QList<OAIFlightAvailability> OAISuccess_Availability::getData() const {
    return m_data;
}
void OAISuccess_Availability::setData(const QList<OAIFlightAvailability> &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAISuccess_Availability::is_data_Set() const{
    return m_data_isSet;
}

bool OAISuccess_Availability::is_data_Valid() const{
    return m_data_isValid;
}

OAIDictionaries OAISuccess_Availability::getDictionaries() const {
    return m_dictionaries;
}
void OAISuccess_Availability::setDictionaries(const OAIDictionaries &dictionaries) {
    m_dictionaries = dictionaries;
    m_dictionaries_isSet = true;
}

bool OAISuccess_Availability::is_dictionaries_Set() const{
    return m_dictionaries_isSet;
}

bool OAISuccess_Availability::is_dictionaries_Valid() const{
    return m_dictionaries_isValid;
}

OAICollection_Meta_AvailSearch OAISuccess_Availability::getMeta() const {
    return m_meta;
}
void OAISuccess_Availability::setMeta(const OAICollection_Meta_AvailSearch &meta) {
    m_meta = meta;
    m_meta_isSet = true;
}

bool OAISuccess_Availability::is_meta_Set() const{
    return m_meta_isSet;
}

bool OAISuccess_Availability::is_meta_Valid() const{
    return m_meta_isValid;
}

QList<OAIIssue> OAISuccess_Availability::getWarnings() const {
    return m_warnings;
}
void OAISuccess_Availability::setWarnings(const QList<OAIIssue> &warnings) {
    m_warnings = warnings;
    m_warnings_isSet = true;
}

bool OAISuccess_Availability::is_warnings_Set() const{
    return m_warnings_isSet;
}

bool OAISuccess_Availability::is_warnings_Valid() const{
    return m_warnings_isValid;
}

bool OAISuccess_Availability::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_dictionaries.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_meta.isSet()) {
            isObjectUpdated = true;
            break;
        }

        if (m_warnings.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISuccess_Availability::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && true;
}

} // namespace OpenAPI
