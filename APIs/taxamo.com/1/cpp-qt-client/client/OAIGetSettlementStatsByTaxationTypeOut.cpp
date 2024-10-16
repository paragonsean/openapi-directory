/**
 * Taxamo
 * Taxamo’s elegant suite of APIs and comprehensive reporting dashboard enables digital merchants to easily comply with EU regulatory requirements on tax calculation, evidence collection, tax return creation and data storage.
 *
 * The version of the OpenAPI document: 1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIGetSettlementStatsByTaxationTypeOut.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIGetSettlementStatsByTaxationTypeOut::OAIGetSettlementStatsByTaxationTypeOut(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIGetSettlementStatsByTaxationTypeOut::OAIGetSettlementStatsByTaxationTypeOut() {
    this->initializeModel();
}

OAIGetSettlementStatsByTaxationTypeOut::~OAIGetSettlementStatsByTaxationTypeOut() {}

void OAIGetSettlementStatsByTaxationTypeOut::initializeModel() {

    m_by_taxation_type_isSet = false;
    m_by_taxation_type_isValid = false;
}

void OAIGetSettlementStatsByTaxationTypeOut::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIGetSettlementStatsByTaxationTypeOut::fromJsonObject(QJsonObject json) {

    m_by_taxation_type_isValid = ::OpenAPI::fromJsonValue(m_by_taxation_type, json[QString("by_taxation_type")]);
    m_by_taxation_type_isSet = !json[QString("by_taxation_type")].isNull() && m_by_taxation_type_isValid;
}

QString OAIGetSettlementStatsByTaxationTypeOut::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIGetSettlementStatsByTaxationTypeOut::asJsonObject() const {
    QJsonObject obj;
    if (m_by_taxation_type.isSet()) {
        obj.insert(QString("by_taxation_type"), ::OpenAPI::toJsonValue(m_by_taxation_type));
    }
    return obj;
}

OAIBy_taxation_type OAIGetSettlementStatsByTaxationTypeOut::getByTaxationType() const {
    return m_by_taxation_type;
}
void OAIGetSettlementStatsByTaxationTypeOut::setByTaxationType(const OAIBy_taxation_type &by_taxation_type) {
    m_by_taxation_type = by_taxation_type;
    m_by_taxation_type_isSet = true;
}

bool OAIGetSettlementStatsByTaxationTypeOut::is_by_taxation_type_Set() const{
    return m_by_taxation_type_isSet;
}

bool OAIGetSettlementStatsByTaxationTypeOut::is_by_taxation_type_Valid() const{
    return m_by_taxation_type_isValid;
}

bool OAIGetSettlementStatsByTaxationTypeOut::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_by_taxation_type.isSet()) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIGetSettlementStatsByTaxationTypeOut::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
