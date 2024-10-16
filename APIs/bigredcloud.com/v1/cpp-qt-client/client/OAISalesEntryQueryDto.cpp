/**
 * Big Red Cloud API
 *   <div style='line-height: 30px;'>      <strong>Welcome to the Big Red Cloud API</strong><br/>      This API enables programmatic access to Big Red Cloud data.<br/>      We have used Swagger to auto generate the API documentation on this page, and it also enables direct interaction with the API in this page. <br/>      To get started, you will require an API Key - check out our guide at <a target='_blank' href='https://www.bigredcloud.com/support/generating-api-key-guide/'>https://www.bigredcloud.com/support/generating-api-key-guide/</a> for information on how to get one. <br/>      Use the  'Enter API Key' button below to enter your API key and start interacting with your Big Red Cloud data right on this page. <br/>      The API key will be stored in your browsers local storage for convenience, but you will be able to delete it at any time if you wish. <br/>      For additional information on the API, check out our support article at <a target='_blank' href='https://www.bigredcloud.com/support/api/'>https://www.bigredcloud.com/support/api/</a><br/>  </div>
 *
 * The version of the OpenAPI document: v1
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

#include "OAISalesEntryQueryDto.h"

#include <QDebug>
#include <QJsonArray>
#include <QJsonDocument>
#include <QObject>

#include "OAIHelpers.h"

namespace OpenAPI {

OAISalesEntryQueryDto::OAISalesEntryQueryDto(QString json) {
    this->initializeModel();
    this->fromJson(json);
}

OAISalesEntryQueryDto::OAISalesEntryQueryDto() {
    this->initializeModel();
}

OAISalesEntryQueryDto::~OAISalesEntryQueryDto() {}

void OAISalesEntryQueryDto::initializeModel() {

    m_ac_code_isSet = false;
    m_ac_code_isValid = false;

    m_ac_entries_isSet = false;
    m_ac_entries_isValid = false;

    m_book_tran_type_id_isSet = false;
    m_book_tran_type_id_isValid = false;

    m_custom_fields_isSet = false;
    m_custom_fields_isValid = false;

    m_customer_id_isSet = false;
    m_customer_id_isValid = false;

    m_detail_collection_isSet = false;
    m_detail_collection_isValid = false;

    m_details_isSet = false;
    m_details_isValid = false;

    m_entry_date_isSet = false;
    m_entry_date_isValid = false;

    m_id_isSet = false;
    m_id_isValid = false;

    m_net_goods_isSet = false;
    m_net_goods_isValid = false;

    m_net_services_isSet = false;
    m_net_services_isValid = false;

    m_note_isSet = false;
    m_note_isValid = false;

    m_proc_date_isSet = false;
    m_proc_date_isValid = false;

    m_reference_isSet = false;
    m_reference_isValid = false;

    m_timestamp_isSet = false;
    m_timestamp_isValid = false;

    m_total_isSet = false;
    m_total_isValid = false;

    m_total_net_isSet = false;
    m_total_net_isValid = false;

    m_total_vat_isSet = false;
    m_total_vat_isValid = false;

    m_unpaid_isSet = false;
    m_unpaid_isValid = false;

    m_vat_entries_isSet = false;
    m_vat_entries_isValid = false;

    m_vat_type_id_isSet = false;
    m_vat_type_id_isValid = false;
}

void OAISalesEntryQueryDto::fromJson(QString jsonString) {
    QByteArray array(jsonString.toStdString().c_str());
    QJsonDocument doc = QJsonDocument::fromJson(array);
    QJsonObject jsonObject = doc.object();
    this->fromJsonObject(jsonObject);
}

void OAISalesEntryQueryDto::fromJsonObject(QJsonObject json) {

    m_ac_code_isValid = ::OpenAPI::fromJsonValue(m_ac_code, json[QString("acCode")]);
    m_ac_code_isSet = !json[QString("acCode")].isNull() && m_ac_code_isValid;

    m_ac_entries_isValid = ::OpenAPI::fromJsonValue(m_ac_entries, json[QString("acEntries")]);
    m_ac_entries_isSet = !json[QString("acEntries")].isNull() && m_ac_entries_isValid;

    m_book_tran_type_id_isValid = ::OpenAPI::fromJsonValue(m_book_tran_type_id, json[QString("bookTranTypeId")]);
    m_book_tran_type_id_isSet = !json[QString("bookTranTypeId")].isNull() && m_book_tran_type_id_isValid;

    m_custom_fields_isValid = ::OpenAPI::fromJsonValue(m_custom_fields, json[QString("customFields")]);
    m_custom_fields_isSet = !json[QString("customFields")].isNull() && m_custom_fields_isValid;

    m_customer_id_isValid = ::OpenAPI::fromJsonValue(m_customer_id, json[QString("customerId")]);
    m_customer_id_isSet = !json[QString("customerId")].isNull() && m_customer_id_isValid;

    m_detail_collection_isValid = ::OpenAPI::fromJsonValue(m_detail_collection, json[QString("detailCollection")]);
    m_detail_collection_isSet = !json[QString("detailCollection")].isNull() && m_detail_collection_isValid;

    m_details_isValid = ::OpenAPI::fromJsonValue(m_details, json[QString("details")]);
    m_details_isSet = !json[QString("details")].isNull() && m_details_isValid;

    m_entry_date_isValid = ::OpenAPI::fromJsonValue(m_entry_date, json[QString("entryDate")]);
    m_entry_date_isSet = !json[QString("entryDate")].isNull() && m_entry_date_isValid;

    m_id_isValid = ::OpenAPI::fromJsonValue(m_id, json[QString("id")]);
    m_id_isSet = !json[QString("id")].isNull() && m_id_isValid;

    m_net_goods_isValid = ::OpenAPI::fromJsonValue(m_net_goods, json[QString("netGoods")]);
    m_net_goods_isSet = !json[QString("netGoods")].isNull() && m_net_goods_isValid;

    m_net_services_isValid = ::OpenAPI::fromJsonValue(m_net_services, json[QString("netServices")]);
    m_net_services_isSet = !json[QString("netServices")].isNull() && m_net_services_isValid;

    m_note_isValid = ::OpenAPI::fromJsonValue(m_note, json[QString("note")]);
    m_note_isSet = !json[QString("note")].isNull() && m_note_isValid;

    m_proc_date_isValid = ::OpenAPI::fromJsonValue(m_proc_date, json[QString("procDate")]);
    m_proc_date_isSet = !json[QString("procDate")].isNull() && m_proc_date_isValid;

    m_reference_isValid = ::OpenAPI::fromJsonValue(m_reference, json[QString("reference")]);
    m_reference_isSet = !json[QString("reference")].isNull() && m_reference_isValid;

    m_timestamp_isValid = ::OpenAPI::fromJsonValue(m_timestamp, json[QString("timestamp")]);
    m_timestamp_isSet = !json[QString("timestamp")].isNull() && m_timestamp_isValid;

    m_total_isValid = ::OpenAPI::fromJsonValue(m_total, json[QString("total")]);
    m_total_isSet = !json[QString("total")].isNull() && m_total_isValid;

    m_total_net_isValid = ::OpenAPI::fromJsonValue(m_total_net, json[QString("totalNet")]);
    m_total_net_isSet = !json[QString("totalNet")].isNull() && m_total_net_isValid;

    m_total_vat_isValid = ::OpenAPI::fromJsonValue(m_total_vat, json[QString("totalVAT")]);
    m_total_vat_isSet = !json[QString("totalVAT")].isNull() && m_total_vat_isValid;

    m_unpaid_isValid = ::OpenAPI::fromJsonValue(m_unpaid, json[QString("unpaid")]);
    m_unpaid_isSet = !json[QString("unpaid")].isNull() && m_unpaid_isValid;

    m_vat_entries_isValid = ::OpenAPI::fromJsonValue(m_vat_entries, json[QString("vatEntries")]);
    m_vat_entries_isSet = !json[QString("vatEntries")].isNull() && m_vat_entries_isValid;

    m_vat_type_id_isValid = ::OpenAPI::fromJsonValue(m_vat_type_id, json[QString("vatTypeId")]);
    m_vat_type_id_isSet = !json[QString("vatTypeId")].isNull() && m_vat_type_id_isValid;
}

QString OAISalesEntryQueryDto::asJson() const {
    QJsonObject obj = this->asJsonObject();
    QJsonDocument doc(obj);
    QByteArray bytes = doc.toJson();
    return QString(bytes);
}

QJsonObject OAISalesEntryQueryDto::asJsonObject() const {
    QJsonObject obj;
    if (m_ac_code_isSet) {
        obj.insert(QString("acCode"), ::OpenAPI::toJsonValue(m_ac_code));
    }
    if (m_ac_entries.size() > 0) {
        obj.insert(QString("acEntries"), ::OpenAPI::toJsonValue(m_ac_entries));
    }
    if (m_book_tran_type_id_isSet) {
        obj.insert(QString("bookTranTypeId"), ::OpenAPI::toJsonValue(m_book_tran_type_id));
    }
    if (m_custom_fields.size() > 0) {
        obj.insert(QString("customFields"), ::OpenAPI::toJsonValue(m_custom_fields));
    }
    if (m_customer_id_isSet) {
        obj.insert(QString("customerId"), ::OpenAPI::toJsonValue(m_customer_id));
    }
    if (m_detail_collection.size() > 0) {
        obj.insert(QString("detailCollection"), ::OpenAPI::toJsonValue(m_detail_collection));
    }
    if (m_details_isSet) {
        obj.insert(QString("details"), ::OpenAPI::toJsonValue(m_details));
    }
    if (m_entry_date_isSet) {
        obj.insert(QString("entryDate"), ::OpenAPI::toJsonValue(m_entry_date));
    }
    if (m_id_isSet) {
        obj.insert(QString("id"), ::OpenAPI::toJsonValue(m_id));
    }
    if (m_net_goods_isSet) {
        obj.insert(QString("netGoods"), ::OpenAPI::toJsonValue(m_net_goods));
    }
    if (m_net_services_isSet) {
        obj.insert(QString("netServices"), ::OpenAPI::toJsonValue(m_net_services));
    }
    if (m_note_isSet) {
        obj.insert(QString("note"), ::OpenAPI::toJsonValue(m_note));
    }
    if (m_proc_date_isSet) {
        obj.insert(QString("procDate"), ::OpenAPI::toJsonValue(m_proc_date));
    }
    if (m_reference_isSet) {
        obj.insert(QString("reference"), ::OpenAPI::toJsonValue(m_reference));
    }
    if (m_timestamp_isSet) {
        obj.insert(QString("timestamp"), ::OpenAPI::toJsonValue(m_timestamp));
    }
    if (m_total_isSet) {
        obj.insert(QString("total"), ::OpenAPI::toJsonValue(m_total));
    }
    if (m_total_net_isSet) {
        obj.insert(QString("totalNet"), ::OpenAPI::toJsonValue(m_total_net));
    }
    if (m_total_vat_isSet) {
        obj.insert(QString("totalVAT"), ::OpenAPI::toJsonValue(m_total_vat));
    }
    if (m_unpaid_isSet) {
        obj.insert(QString("unpaid"), ::OpenAPI::toJsonValue(m_unpaid));
    }
    if (m_vat_entries.size() > 0) {
        obj.insert(QString("vatEntries"), ::OpenAPI::toJsonValue(m_vat_entries));
    }
    if (m_vat_type_id_isSet) {
        obj.insert(QString("vatTypeId"), ::OpenAPI::toJsonValue(m_vat_type_id));
    }
    return obj;
}

QString OAISalesEntryQueryDto::getAcCode() const {
    return m_ac_code;
}
void OAISalesEntryQueryDto::setAcCode(const QString &ac_code) {
    m_ac_code = ac_code;
    m_ac_code_isSet = true;
}

bool OAISalesEntryQueryDto::is_ac_code_Set() const{
    return m_ac_code_isSet;
}

bool OAISalesEntryQueryDto::is_ac_code_Valid() const{
    return m_ac_code_isValid;
}

QList<OAIAcEntryDto> OAISalesEntryQueryDto::getAcEntries() const {
    return m_ac_entries;
}
void OAISalesEntryQueryDto::setAcEntries(const QList<OAIAcEntryDto> &ac_entries) {
    m_ac_entries = ac_entries;
    m_ac_entries_isSet = true;
}

bool OAISalesEntryQueryDto::is_ac_entries_Set() const{
    return m_ac_entries_isSet;
}

bool OAISalesEntryQueryDto::is_ac_entries_Valid() const{
    return m_ac_entries_isValid;
}

qint64 OAISalesEntryQueryDto::getBookTranTypeId() const {
    return m_book_tran_type_id;
}
void OAISalesEntryQueryDto::setBookTranTypeId(const qint64 &book_tran_type_id) {
    m_book_tran_type_id = book_tran_type_id;
    m_book_tran_type_id_isSet = true;
}

bool OAISalesEntryQueryDto::is_book_tran_type_id_Set() const{
    return m_book_tran_type_id_isSet;
}

bool OAISalesEntryQueryDto::is_book_tran_type_id_Valid() const{
    return m_book_tran_type_id_isValid;
}

QList<OAIAcudfValueDto> OAISalesEntryQueryDto::getCustomFields() const {
    return m_custom_fields;
}
void OAISalesEntryQueryDto::setCustomFields(const QList<OAIAcudfValueDto> &custom_fields) {
    m_custom_fields = custom_fields;
    m_custom_fields_isSet = true;
}

bool OAISalesEntryQueryDto::is_custom_fields_Set() const{
    return m_custom_fields_isSet;
}

bool OAISalesEntryQueryDto::is_custom_fields_Valid() const{
    return m_custom_fields_isValid;
}

qint64 OAISalesEntryQueryDto::getCustomerId() const {
    return m_customer_id;
}
void OAISalesEntryQueryDto::setCustomerId(const qint64 &customer_id) {
    m_customer_id = customer_id;
    m_customer_id_isSet = true;
}

bool OAISalesEntryQueryDto::is_customer_id_Set() const{
    return m_customer_id_isSet;
}

bool OAISalesEntryQueryDto::is_customer_id_Valid() const{
    return m_customer_id_isValid;
}

QList<QString> OAISalesEntryQueryDto::getDetailCollection() const {
    return m_detail_collection;
}
void OAISalesEntryQueryDto::setDetailCollection(const QList<QString> &detail_collection) {
    m_detail_collection = detail_collection;
    m_detail_collection_isSet = true;
}

bool OAISalesEntryQueryDto::is_detail_collection_Set() const{
    return m_detail_collection_isSet;
}

bool OAISalesEntryQueryDto::is_detail_collection_Valid() const{
    return m_detail_collection_isValid;
}

QString OAISalesEntryQueryDto::getDetails() const {
    return m_details;
}
void OAISalesEntryQueryDto::setDetails(const QString &details) {
    m_details = details;
    m_details_isSet = true;
}

bool OAISalesEntryQueryDto::is_details_Set() const{
    return m_details_isSet;
}

bool OAISalesEntryQueryDto::is_details_Valid() const{
    return m_details_isValid;
}

QDateTime OAISalesEntryQueryDto::getEntryDate() const {
    return m_entry_date;
}
void OAISalesEntryQueryDto::setEntryDate(const QDateTime &entry_date) {
    m_entry_date = entry_date;
    m_entry_date_isSet = true;
}

bool OAISalesEntryQueryDto::is_entry_date_Set() const{
    return m_entry_date_isSet;
}

bool OAISalesEntryQueryDto::is_entry_date_Valid() const{
    return m_entry_date_isValid;
}

qint64 OAISalesEntryQueryDto::getId() const {
    return m_id;
}
void OAISalesEntryQueryDto::setId(const qint64 &id) {
    m_id = id;
    m_id_isSet = true;
}

bool OAISalesEntryQueryDto::is_id_Set() const{
    return m_id_isSet;
}

bool OAISalesEntryQueryDto::is_id_Valid() const{
    return m_id_isValid;
}

double OAISalesEntryQueryDto::getNetGoods() const {
    return m_net_goods;
}
void OAISalesEntryQueryDto::setNetGoods(const double &net_goods) {
    m_net_goods = net_goods;
    m_net_goods_isSet = true;
}

bool OAISalesEntryQueryDto::is_net_goods_Set() const{
    return m_net_goods_isSet;
}

bool OAISalesEntryQueryDto::is_net_goods_Valid() const{
    return m_net_goods_isValid;
}

double OAISalesEntryQueryDto::getNetServices() const {
    return m_net_services;
}
void OAISalesEntryQueryDto::setNetServices(const double &net_services) {
    m_net_services = net_services;
    m_net_services_isSet = true;
}

bool OAISalesEntryQueryDto::is_net_services_Set() const{
    return m_net_services_isSet;
}

bool OAISalesEntryQueryDto::is_net_services_Valid() const{
    return m_net_services_isValid;
}

QString OAISalesEntryQueryDto::getNote() const {
    return m_note;
}
void OAISalesEntryQueryDto::setNote(const QString &note) {
    m_note = note;
    m_note_isSet = true;
}

bool OAISalesEntryQueryDto::is_note_Set() const{
    return m_note_isSet;
}

bool OAISalesEntryQueryDto::is_note_Valid() const{
    return m_note_isValid;
}

QDateTime OAISalesEntryQueryDto::getProcDate() const {
    return m_proc_date;
}
void OAISalesEntryQueryDto::setProcDate(const QDateTime &proc_date) {
    m_proc_date = proc_date;
    m_proc_date_isSet = true;
}

bool OAISalesEntryQueryDto::is_proc_date_Set() const{
    return m_proc_date_isSet;
}

bool OAISalesEntryQueryDto::is_proc_date_Valid() const{
    return m_proc_date_isValid;
}

QString OAISalesEntryQueryDto::getReference() const {
    return m_reference;
}
void OAISalesEntryQueryDto::setReference(const QString &reference) {
    m_reference = reference;
    m_reference_isSet = true;
}

bool OAISalesEntryQueryDto::is_reference_Set() const{
    return m_reference_isSet;
}

bool OAISalesEntryQueryDto::is_reference_Valid() const{
    return m_reference_isValid;
}

QByteArray OAISalesEntryQueryDto::getTimestamp() const {
    return m_timestamp;
}
void OAISalesEntryQueryDto::setTimestamp(const QByteArray &timestamp) {
    m_timestamp = timestamp;
    m_timestamp_isSet = true;
}

bool OAISalesEntryQueryDto::is_timestamp_Set() const{
    return m_timestamp_isSet;
}

bool OAISalesEntryQueryDto::is_timestamp_Valid() const{
    return m_timestamp_isValid;
}

double OAISalesEntryQueryDto::getTotal() const {
    return m_total;
}
void OAISalesEntryQueryDto::setTotal(const double &total) {
    m_total = total;
    m_total_isSet = true;
}

bool OAISalesEntryQueryDto::is_total_Set() const{
    return m_total_isSet;
}

bool OAISalesEntryQueryDto::is_total_Valid() const{
    return m_total_isValid;
}

double OAISalesEntryQueryDto::getTotalNet() const {
    return m_total_net;
}
void OAISalesEntryQueryDto::setTotalNet(const double &total_net) {
    m_total_net = total_net;
    m_total_net_isSet = true;
}

bool OAISalesEntryQueryDto::is_total_net_Set() const{
    return m_total_net_isSet;
}

bool OAISalesEntryQueryDto::is_total_net_Valid() const{
    return m_total_net_isValid;
}

double OAISalesEntryQueryDto::getTotalVat() const {
    return m_total_vat;
}
void OAISalesEntryQueryDto::setTotalVat(const double &total_vat) {
    m_total_vat = total_vat;
    m_total_vat_isSet = true;
}

bool OAISalesEntryQueryDto::is_total_vat_Set() const{
    return m_total_vat_isSet;
}

bool OAISalesEntryQueryDto::is_total_vat_Valid() const{
    return m_total_vat_isValid;
}

double OAISalesEntryQueryDto::getUnpaid() const {
    return m_unpaid;
}
void OAISalesEntryQueryDto::setUnpaid(const double &unpaid) {
    m_unpaid = unpaid;
    m_unpaid_isSet = true;
}

bool OAISalesEntryQueryDto::is_unpaid_Set() const{
    return m_unpaid_isSet;
}

bool OAISalesEntryQueryDto::is_unpaid_Valid() const{
    return m_unpaid_isValid;
}

QList<OAIVatEntryDto> OAISalesEntryQueryDto::getVatEntries() const {
    return m_vat_entries;
}
void OAISalesEntryQueryDto::setVatEntries(const QList<OAIVatEntryDto> &vat_entries) {
    m_vat_entries = vat_entries;
    m_vat_entries_isSet = true;
}

bool OAISalesEntryQueryDto::is_vat_entries_Set() const{
    return m_vat_entries_isSet;
}

bool OAISalesEntryQueryDto::is_vat_entries_Valid() const{
    return m_vat_entries_isValid;
}

qint64 OAISalesEntryQueryDto::getVatTypeId() const {
    return m_vat_type_id;
}
void OAISalesEntryQueryDto::setVatTypeId(const qint64 &vat_type_id) {
    m_vat_type_id = vat_type_id;
    m_vat_type_id_isSet = true;
}

bool OAISalesEntryQueryDto::is_vat_type_id_Set() const{
    return m_vat_type_id_isSet;
}

bool OAISalesEntryQueryDto::is_vat_type_id_Valid() const{
    return m_vat_type_id_isValid;
}

bool OAISalesEntryQueryDto::isSet() const {
    bool isObjectUpdated = false;
    do {
        if (m_ac_code_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_ac_entries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_book_tran_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_custom_fields.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_customer_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_detail_collection.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_details_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_entry_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_id_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_goods_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_net_services_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_note_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_proc_date_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_reference_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_timestamp_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_net_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_total_vat_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_unpaid_isSet) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_entries.size() > 0) {
            isObjectUpdated = true;
            break;
        }

        if (m_vat_type_id_isSet) {
            isObjectUpdated = true;
            break;
        }
    } while (false);
    return isObjectUpdated;
}

bool OAISalesEntryQueryDto::isValid() const {
    // only required properties are required for the object to be considered valid
    return true;
}

} // namespace OpenAPI
