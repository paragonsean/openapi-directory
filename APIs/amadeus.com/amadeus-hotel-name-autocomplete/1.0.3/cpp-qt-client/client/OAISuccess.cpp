/**
 * Hotel Name Autocomplete
 * Before using this API, we recommend you read our **[Authorization Guide](https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262)** for more information on how to generate an access token.   Please also be aware that our test environment is based on a subset of the production for this API it may change dynamically. For your tests, use big cities like LON (London) or NYC (New-York).
 *
 * The version of the OpenAPI document: 1.0.3
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISuccess.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISuccess::OAISuccess(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISuccess::OAISuccess() {
    this->initializeModel();
}

OAISuccess::~OAISuccess() {}

void OAISuccess::initializeModel() {

    m_data_isSet = false;
    m_data_isValid = false;
}

void OAISuccess::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISuccess::fromJsonObject(QJsonObject json) {

    m_data_isValid = ::OpenAPI::fromJsonValue(m_data, json[QString("data")]);
    m_data_isSet = !json[QString("data")].isNull() && m_data_isValid;
}

QString OAISuccess::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISuccess::asJsonObject() const {
    QJsonObject obj;
    if (m_data.size() > 0) {
        obj.insert(QString("data"), ::OpenAPI::toJsonValue(m_data));
    }
    return obj;
}

QList<OAISuccess_data_inner> OAISuccess::getData() const {
    return m_data;
}
void OAISuccess::setData(const QList<OAISuccess_data_inner> &data) {
    m_data = data;
    m_data_isSet = true;
}

bool OAISuccess::is_data_Set() const{
    return m_data_isSet;
}

bool OAISuccess::is_data_Valid() const{
    return m_data_isValid;
}

bool OAISuccess::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_data.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISuccess::isValid() const {
    // only required properties are required for the object to be considered valid
    return m_data_isValid && true;
}

} // namespace OpenAPI
