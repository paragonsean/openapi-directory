/**
 * MIMIC REST API
 * This is the API for MIMIC client to connect to MIMIC daemon.
 *
 * The version of the OpenAPI document: 21.00
 * Contact: support@gambitcomm.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAIConfigSFLOW.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAIConfigSFLOW::OAIConfigSFLOW(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAIConfigSFLOW::OAIConfigSFLOW() {
    this->initializeModel();
}

OAIConfigSFLOW::~OAIConfigSFLOW() {}

void OAIConfigSFLOW::initializeModel() {

    m_collector_isSet = false;
    m_collector_isValid = false;

    m_collectorport_isSet = false;
    m_collectorport_isValid = false;

    m_encoding_type_isSet = false;
    m_encoding_type_isValid = false;

    m_filename_isSet = false;
    m_filename_isValid = false;

    m_flows_per_min_isSet = false;
    m_flows_per_min_isValid = false;

    m_include_samples_isSet = false;
    m_include_samples_isValid = false;

    m_records_per_sample_isSet = false;
    m_records_per_sample_isValid = false;

    m_samples_per_datagram_isSet = false;
    m_samples_per_datagram_isValid = false;
}

void OAIConfigSFLOW::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAIConfigSFLOW::fromJsonObject(QJsonObject json) {

    m_collector_isValid = ::OpenAPI::fromJsonValue(m_collector, json[QString("collector")]);
    m_collector_isSet = !json[QString("collector")].isNull() && m_collector_isValid;

    m_collectorport_isValid = ::OpenAPI::fromJsonValue(m_collectorport, json[QString("collectorport")]);
    m_collectorport_isSet = !json[QString("collectorport")].isNull() && m_collectorport_isValid;

    m_encoding_type_isValid = ::OpenAPI::fromJsonValue(m_encoding_type, json[QString("encoding_type")]);
    m_encoding_type_isSet = !json[QString("encoding_type")].isNull() && m_encoding_type_isValid;

    m_filename_isValid = ::OpenAPI::fromJsonValue(m_filename, json[QString("filename")]);
    m_filename_isSet = !json[QString("filename")].isNull() && m_filename_isValid;

    m_flows_per_min_isValid = ::OpenAPI::fromJsonValue(m_flows_per_min, json[QString("flows_per_min")]);
    m_flows_per_min_isSet = !json[QString("flows_per_min")].isNull() && m_flows_per_min_isValid;

    m_include_samples_isValid = ::OpenAPI::fromJsonValue(m_include_samples, json[QString("include_samples")]);
    m_include_samples_isSet = !json[QString("include_samples")].isNull() && m_include_samples_isValid;

    m_records_per_sample_isValid = ::OpenAPI::fromJsonValue(m_records_per_sample, json[QString("records_per_sample")]);
    m_records_per_sample_isSet = !json[QString("records_per_sample")].isNull() && m_records_per_sample_isValid;

    m_samples_per_datagram_isValid = ::OpenAPI::fromJsonValue(m_samples_per_datagram, json[QString("samples_per_datagram")]);
    m_samples_per_datagram_isSet = !json[QString("samples_per_datagram")].isNull() && m_samples_per_datagram_isValid;
}

QString OAIConfigSFLOW::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAIConfigSFLOW::asJsonObject() const {
    QJsonObject obj;
    if (m_collector_isSet) {
        obj.insert(QString("collector"), ::OpenAPI::toJsonValue(m_collector));
    }
    if (m_collectorport_isSet) {
        obj.insert(QString("collectorport"), ::OpenAPI::toJsonValue(m_collectorport));
    }
    if (m_encoding_type_isSet) {
        obj.insert(QString("encoding_type"), ::OpenAPI::toJsonValue(m_encoding_type));
    }
    if (m_filename_isSet) {
        obj.insert(QString("filename"), ::OpenAPI::toJsonValue(m_filename));
    }
    if (m_flows_per_min_isSet) {
        obj.insert(QString("flows_per_min"), ::OpenAPI::toJsonValue(m_flows_per_min));
    }
    if (m_include_samples_isSet) {
        obj.insert(QString("include_samples"), ::OpenAPI::toJsonValue(m_include_samples));
    }
    if (m_records_per_sample_isSet) {
        obj.insert(QString("records_per_sample"), ::OpenAPI::toJsonValue(m_records_per_sample));
    }
    if (m_samples_per_datagram_isSet) {
        obj.insert(QString("samples_per_datagram"), ::OpenAPI::toJsonValue(m_samples_per_datagram));
    }
    return obj;
}

QString OAIConfigSFLOW::getCollector() const {
    return m_collector;
}
void OAIConfigSFLOW::setCollector(const QString &collector) {
    m_collector = collector;
    m_collector_isSet = true;
}

bool OAIConfigSFLOW::is_collector_Set() const{
    return m_collector_isSet;
}

bool OAIConfigSFLOW::is_collector_Valid() const{
    return m_collector_isValid;
}

qint32 OAIConfigSFLOW::getCollectorport() const {
    return m_collectorport;
}
void OAIConfigSFLOW::setCollectorport(const qint32 &collectorport) {
    m_collectorport = collectorport;
    m_collectorport_isSet = true;
}

bool OAIConfigSFLOW::is_collectorport_Set() const{
    return m_collectorport_isSet;
}

bool OAIConfigSFLOW::is_collectorport_Valid() const{
    return m_collectorport_isValid;
}

QString OAIConfigSFLOW::getEncodingType() const {
    return m_encoding_type;
}
void OAIConfigSFLOW::setEncodingType(const QString &encoding_type) {
    m_encoding_type = encoding_type;
    m_encoding_type_isSet = true;
}

bool OAIConfigSFLOW::is_encoding_type_Set() const{
    return m_encoding_type_isSet;
}

bool OAIConfigSFLOW::is_encoding_type_Valid() const{
    return m_encoding_type_isValid;
}

QString OAIConfigSFLOW::getFilename() const {
    return m_filename;
}
void OAIConfigSFLOW::setFilename(const QString &filename) {
    m_filename = filename;
    m_filename_isSet = true;
}

bool OAIConfigSFLOW::is_filename_Set() const{
    return m_filename_isSet;
}

bool OAIConfigSFLOW::is_filename_Valid() const{
    return m_filename_isValid;
}

qint32 OAIConfigSFLOW::getFlowsPerMin() const {
    return m_flows_per_min;
}
void OAIConfigSFLOW::setFlowsPerMin(const qint32 &flows_per_min) {
    m_flows_per_min = flows_per_min;
    m_flows_per_min_isSet = true;
}

bool OAIConfigSFLOW::is_flows_per_min_Set() const{
    return m_flows_per_min_isSet;
}

bool OAIConfigSFLOW::is_flows_per_min_Valid() const{
    return m_flows_per_min_isValid;
}

QString OAIConfigSFLOW::getIncludeSamples() const {
    return m_include_samples;
}
void OAIConfigSFLOW::setIncludeSamples(const QString &include_samples) {
    m_include_samples = include_samples;
    m_include_samples_isSet = true;
}

bool OAIConfigSFLOW::is_include_samples_Set() const{
    return m_include_samples_isSet;
}

bool OAIConfigSFLOW::is_include_samples_Valid() const{
    return m_include_samples_isValid;
}

QString OAIConfigSFLOW::getRecordsPerSample() const {
    return m_records_per_sample;
}
void OAIConfigSFLOW::setRecordsPerSample(const QString &records_per_sample) {
    m_records_per_sample = records_per_sample;
    m_records_per_sample_isSet = true;
}

bool OAIConfigSFLOW::is_records_per_sample_Set() const{
    return m_records_per_sample_isSet;
}

bool OAIConfigSFLOW::is_records_per_sample_Valid() const{
    return m_records_per_sample_isValid;
}

QString OAIConfigSFLOW::getSamplesPerDatagram() const {
    return m_samples_per_datagram;
}
void OAIConfigSFLOW::setSamplesPerDatagram(const QString &samples_per_datagram) {
    m_samples_per_datagram = samples_per_datagram;
    m_samples_per_datagram_isSet = true;
}

bool OAIConfigSFLOW::is_samples_per_datagram_Set() const{
    return m_samples_per_datagram_isSet;
}

bool OAIConfigSFLOW::is_samples_per_datagram_Valid() const{
    return m_samples_per_datagram_isValid;
}

bool OAIConfigSFLOW::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_collector_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_collectorport_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_encoding_type_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_filename_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_flows_per_min_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_include_samples_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_records_per_sample_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_samples_per_datagram_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAIConfigSFLOW::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
