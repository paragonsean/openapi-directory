/**
 * PowerTools Developer
 * Apptigent PowerTools Developer Edition is a powerful suite of API endpoints for custom applications running on any stack. Manipulate text, modify collections, format dates and times, convert currency, perform advanced mathematical calculations, shorten URL's, encode strings, convert text to speech, translate content into multiple languages, process images, and more. PowerTools is the ultimate developer toolkit.
 *
 * The version of the OpenAPI document: 2021.1.01
 * Contact: support@apptigent.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIOutputStockPrice.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIOutputStockPrice::OAIOutputStockPrice(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIOutputStockPrice::OAIOutputStockPrice() {
    this->initializeModel();
}

OAIOutputStockPrice::~OAIOutputStockPrice() {}

void OAIOutputStockPrice::initializeModel() {

    m_result_isSet = false;
    m_result_isValid = false;
}

void OAIOutputStockPrice::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIOutputStockPrice::fromJsonObject(QJsonObject json) {

    m_result_isValid = ::OpenAPI::fromJsonValue(m_result, json[QString("result")]);
    m_result_isSet = !json[QString("result")].isNull() && m_result_isValid;
}

QString OAIOutputStockPrice::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIOutputStockPrice::asJsonObject() const {
    QJsonObject obj;
    if (m_result.size() > 0) {
        obj.insert(QString("result"), ::OpenAPI::toJsonValue(m_result));
    }
    return obj;
}

QList<OAIOutputStockPrice_result_inner> OAIOutputStockPrice::getResult() const {
    return m_result;
}
void OAIOutputStockPrice::setResult(const QList<OAIOutputStockPrice_result_inner> &result) {
    m_result = result;
    m_result_isSet = true;
}

bool OAIOutputStockPrice::is_result_Set() const{
    return m_result_isSet;
}

bool OAIOutputStockPrice::is_result_Valid() const{
    return m_result_isValid;
}

bool OAIOutputStockPrice::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_result.size() > 0) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIOutputStockPrice::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
