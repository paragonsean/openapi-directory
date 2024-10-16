/**
 * Random Lovecraft
 * Random sentences from the complete works of H.P. Lovecraft. CORS-enabled.
 *
 * The version of the OpenAPI document: 1.0
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGet_specific_sentence_200_response.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGet_specific_sentence_200_response::OAIGet_specific_sentence_200_response(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGet_specific_sentence_200_response::OAIGet_specific_sentence_200_response() {
    this->initializeModel();
}

OAIGet_specific_sentence_200_response::~OAIGet_specific_sentence_200_response() {}

void OAIGet_specific_sentence_200_response::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;
}

void OAIGet_specific_sentence_200_response::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGet_specific_sentence_200_response::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;
}

QString OAIGet_specific_sentence_200_response::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGet_specific_sentence_200_response::asJsonObject() const {
    QJsonObject obj;
    if (m_data.isSet()) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    return obj;
}

OAISentence OAIGet_specific_sentence_200_response::getData() const {
    return m_data;
}
void OAIGet_specific_sentence_200_response::setData(const OAISentence &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAIGet_specific_sentence_200_response::is_data_Set() const{
    return m_data_isSet;
}

bool OAIGet_specific_sentence_200_response::is_data_Valid() const{
    return m_data_isValid;
}

bool OAIGet_specific_sentence_200_response::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGet_specific_sentence_200_response::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
