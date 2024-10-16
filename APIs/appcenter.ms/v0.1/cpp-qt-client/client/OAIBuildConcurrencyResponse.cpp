/**
 * App Center Client
 * Microsoft Visual Studio App Center API
 *
 * The version of the OpenAPI document: v0.1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIBuildConcurrencyResponse.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIBuildConcurrencyResponse::OAIBuildConcurrencyResponse(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIBuildConcurrencyResponse::OAIBuildConcurrencyResponse() {
    this->initializeModel();
}

OAIBuildConcurrencyResponse::~OAIBuildConcurrencyResponse() {}

void OAIBuildConcurrencyResponse::initializeModel() {

    m_committed_quantity_isSet = false;
    m_committed_quantity_isValid = false;

    m_quantity_isSet = false;
    m_quantity_isValid = false;
}

void OAIBuildConcurrencyResponse::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIBuildConcurrencyResponse::fromJsonObject(QJsonObject json) {

    m_committed_quantity_isValid = ::OpenAPI::fromJsonValue(m_committed_quantity, json[QString("committed_quantity")]);
    m_committed_quantity_isSet = !json[QString("committed_quantity")].isNull() && m_committed_quantity_isValid;

    m_quantity_isValid = ::OpenAPI::fromJsonValue(m_quantity, json[QString("quantity")]);
    m_quantity_isSet = !json[QString("quantity")].isNull() && m_quantity_isValid;
}

QString OAIBuildConcurrencyResponse::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIBuildConcurrencyResponse::asJsonObject() const {
    QJsonObject obj;
    if (m_committed_quantity_isSet) {
        obj.insert(QString("committed_quantity"), ::OpenAPI::toJsonValue(m_committed_quantity));
    }
    if (m_quantity_isSet) {
        obj.insert(QString("quantity"), ::OpenAPI::toJsonValue(m_quantity));
    }
    return obj;
}

double OAIBuildConcurrencyResponse::getCommittedQuantity() const {
    return m_committed_quantity;
}
void OAIBuildConcurrencyResponse::setCommittedQuantity(const double &committed_quantity) {
    m_committed_quantity = committed_quantity;
    m_committed_quantity_isSet = true;
}

bool OAIBuildConcurrencyResponse::is_committed_quantity_Set() const{
    return m_committed_quantity_isSet;
}

bool OAIBuildConcurrencyResponse::is_committed_quantity_Valid() const{
    return m_committed_quantity_isValid;
}

double OAIBuildConcurrencyResponse::getQuantity() const {
    return m_quantity;
}
void OAIBuildConcurrencyResponse::setQuantity(const double &quantity) {
    m_quantity = quantity;
    m_quantity_isSet = true;
}

bool OAIBuildConcurrencyResponse::is_quantity_Set() const{
    return m_quantity_isSet;
}

bool OAIBuildConcurrencyResponse::is_quantity_Valid() const{
    return m_quantity_isValid;
}

bool OAIBuildConcurrencyResponse::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_committed_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_quantity_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIBuildConcurrencyResponse::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
